#!/usr/bin/env python3
"""
auto_morning_briefing.py — runs on Mac each morning.

Flow:
  1. Poll WHOOP API until today's recovery score is available (max 2 hours).
  2. Get calendar events via icalBuddy.
  3. Read vault: TODO.md, semester context, latest WHOOP daily note.
  4. Call Claude API to synthesise the briefing.
  5. Write second-brain/morning-briefing/YYYY-MM-DD.md.
  6. Git commit + push.
  7. Run notebooklm_upload.py to create the audio.

Install as a launchd job at 5:30 AM — see com.sri.morning-briefing.plist.
"""

import asyncio
import json
import os
import random
import ssl
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

import certifi

# ── Paths ──────────────────────────────────────────────────────────────────────
VAULT        = Path.home() / "Documents" / "MyVault"
TOKEN_FILE   = VAULT / ".obsidian/plugins/obsidian-whoop-plugin/data.json"
TODO_FILE    = VAULT / "second-brain/notes/TODO.md"
SEMESTER_FILE= VAULT / "second-brain/context/semester-spring-2026.md"
QUOTES_FILE  = VAULT / "scripts/quotes.json"
BRIEFING_DIR = VAULT / "second-brain/morning-briefing"
LOG_FILE     = VAULT / "scripts/upload.log"
UPLOAD_SCRIPT= VAULT / "scripts/notebooklm_upload.py"

# ── WHOOP ──────────────────────────────────────────────────────────────────────
API           = "https://api.prod.whoop.com/developer/v2"
TOKEN_URL     = "https://api.prod.whoop.com/oauth/oauth2/token"
CLIENT_ID     = "1637e4a7-5b98-479d-bc74-85d711110b86"
CLIENT_SECRET = "f8a24cacf97b339cd7160d7a8c3e7a1772105b976f9539df17b294cf6a1d099e"
BROWSER_UA    = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

SSL_CTX = ssl.create_default_context(cafile=certifi.where())


def log(msg: str) -> None:
    line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


# ── WHOOP auth ─────────────────────────────────────────────────────────────────

def _whoop_headers(token: str | None = None) -> dict:
    h = {
        "User-Agent": BROWSER_UA,
        "Accept": "application/json, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://app.whoop.com",
        "Referer": "https://app.whoop.com/",
    }
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def get_access_token() -> str:
    with open(TOKEN_FILE) as f:
        d = json.load(f)
    tokens = d.get("tokens", {})
    post_data = urllib.parse.urlencode({
        "grant_type":    "refresh_token",
        "refresh_token": tokens["refresh_token"],
        "client_id":     CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope":         "offline read:workout read:recovery read:sleep read:cycles",
    }).encode()
    req = urllib.request.Request(
        TOKEN_URL, data=post_data,
        headers={**_whoop_headers(), "Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(req, timeout=15, context=SSL_CTX) as r:
        new = json.loads(r.read())
    tokens.update(new)
    d["tokens"] = tokens
    with open(TOKEN_FILE, "w") as f:
        json.dump(d, f, indent=2)
    return new["access_token"]


def whoop_get(path: str, token: str) -> dict:
    req = urllib.request.Request(f"{API}{path}", headers=_whoop_headers(token))
    with urllib.request.urlopen(req, timeout=15, context=SSL_CTX) as r:
        return json.loads(r.read())


# ── Poll until today's recovery is ready ──────────────────────────────────────

def wait_for_recovery(max_minutes: int = 180) -> dict:
    """Return the recovery record for today; poll every 5 min until available."""
    today = date.today().isoformat()
    deadline = time.time() + max_minutes * 60

    while time.time() < deadline:
        try:
            token = get_access_token()
            data  = whoop_get("/recovery?limit=1", token)
            records = data.get("records", [])
            if records:
                rec = records[0]
                # created_at is UTC ISO; check it covers today
                created = rec.get("created_at", "")[:10]
                score   = rec.get("score", {})
                recovery_score = score.get("recovery_score")
                if created >= today and recovery_score is not None:
                    log(f"WHOOP recovery ready: {recovery_score}%")
                    return rec
        except Exception as e:
            log(f"WHOOP poll error: {e}")

        log("Recovery not yet available, waiting 5 min…")
        time.sleep(300)

    raise RuntimeError(f"WHOOP recovery not available after {max_minutes} minutes")


def get_sleep(token: str) -> dict:
    data = whoop_get("/activity/sleep?limit=1", token)
    return (data.get("records") or [{}])[0]


# ── Calendar via icalBuddy ─────────────────────────────────────────────────────

def get_ical_events(target_date: date) -> str:
    from_str = target_date.strftime("%m/%d/%Y")
    to_str   = target_date.strftime("%m/%d/%Y")
    try:
        result = subprocess.run(
            ["icalBuddy", "-f", "-b", "• ", "-nc", "-npn",
             "-iep", "title,datetime",
             "eventsFrom:" + from_str, "to:" + to_str],
            capture_output=True, text=True, timeout=10,
        )
        return result.stdout.strip() or "No events"
    except FileNotFoundError:
        return "(icalBuddy not installed — install with: brew install ical-buddy)"
    except Exception as e:
        return f"(calendar error: {e})"


# ── Vault reads ────────────────────────────────────────────────────────────────

def read_file_safe(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return f"(could not read {path})"


def get_whoop_daily_note() -> tuple[str, str]:
    """Return (filename_stem, content) of the most recent WHOOP daily note."""
    whoop_dir = VAULT / "sports-fitness/Health/WHOOP/2026"
    try:
        files = sorted(whoop_dir.glob("daily-*.md"))
        if not files:
            return ("", "(no WHOOP notes found)")
        latest = files[-1]
        return (latest.stem, latest.read_text(encoding="utf-8"))
    except Exception as e:
        return ("", f"(error reading WHOOP notes: {e})")


def pick_quote() -> str:
    try:
        quotes = json.loads(QUOTES_FILE.read_text())
        q = random.choice(quotes)
        return f'"{q["text"]}" — {q["author"]}'
    except Exception:
        return '"Suffer now and live the rest of your life as a champion." — Muhammad Ali'


# ── Claude briefing generation ─────────────────────────────────────────────────

def build_prompt(
    today: date,
    recovery_rec: dict,
    sleep_rec: dict,
    today_events: str,
    tomorrow_events: str,
    todo_content: str,
    semester_content: str,
    whoop_note_name: str,
    whoop_note_content: str,
    quote: str,
) -> str:
    weekday   = today.strftime("%A")
    date_str  = today.strftime("%B %d %Y")
    tomorrow  = today + timedelta(days=1)

    score  = recovery_rec.get("score", {})
    rec_pct     = score.get("recovery_score", "?")
    hrv         = score.get("hrv_rmssd_milli", "?")
    rhr         = score.get("resting_heart_rate", "?")

    ss = sleep_rec.get("score", {}) or {}
    sleep_perf  = ss.get("sleep_performance_percentage", "?")
    deep_pct    = ss.get("slow_wave_sleep_percentage", "?")
    rem_pct     = ss.get("rem_sleep_percentage", "?")
    total_min   = (sleep_rec.get("end") and sleep_rec.get("start") and
                   _duration_minutes(sleep_rec["start"], sleep_rec["end"])) or "?"
    strain_data = recovery_rec.get("score", {}).get("user_calibrating", "?")

    # Format sleep duration as Xh Ymin
    if isinstance(total_min, int):
        sleep_fmt = f"{total_min // 60}h {total_min % 60}min"
    else:
        sleep_fmt = "?"

    return f"""You are generating Sri's daily morning briefing. Today is {weekday}, {date_str}.

Write the briefing in EXACTLY this markdown format — substitute every bracketed placeholder with real data from the inputs below. Do not add extra sections. Do not invent data. Use only unchecked [ ] items from TODO.md — never checked [x] items.

---

# Daily Briefing — [{weekday}, {date_str}]

> {quote}

## 💪 WHOOP — {whoop_note_name}
| Metric | Value |
|--------|-------|
| Recovery | {rec_pct}% |
| HRV | {hrv} ms |
| Resting HR | {rhr} bpm |
| Sleep | {sleep_fmt} · {sleep_perf}% performance |
| Deep Sleep | {deep_pct}% |
| REM Sleep | {rem_pct}% |
| Day Strain | [extract from WHOOP note below, or "—"] |
| Workouts | [any workouts in WHOOP note, or "None logged"] |

[[sports-fitness/Health/WHOOP/2026/{whoop_note_name}|View WHOOP Note]] · [[sports-fitness/Health/WHOOP/index|WHOOP Index]]

---

## 🏊 Today's Workout
[From today's calendar events: any swim practice, gym, or workout. If none: "No workout on calendar today."]

---

## 📅 Today's Schedule
[List every calendar event today as: `HH:MM AM/PM — Event Title`. If none: "No events on calendar today."]

## 🗓️ Tomorrow ({tomorrow.strftime("%A, %B %d")})
[Tomorrow's calendar events: `HH:MM AM/PM — Event Title`. Keep it brief. If none: "No events."]

---

## 🔴 Due Today / Tomorrow
[Unchecked TODO items due today ({today.isoformat()}) or tomorrow ({tomorrow.isoformat()}). Format: `- **COURSE-XXX** — Assignment name · due DATE`. If none: "Nothing due in the next 24 hours."]

## 📅 This Week
[All unchecked TODO items due within 7 days of today, sorted by date. Same format. Exclude items already listed above.]

---

## 🧠 Priority Focus
[1–3 sentences MAX. What is highest-stakes right now? Name the specific assignment and exactly why it matters first.]

## ⚠️ Watch Out For
[Flag: SE-201 Saturday 5AM deadlines, async course drift (MATH-201/COM-270), or any patterns of repeated mentions without action. If nothing to flag, omit this section entirely.]

---

Now fill in the above template using only this data:

### Today's Calendar ({today.isoformat()})
{today_events}

### Tomorrow's Calendar ({tomorrow.isoformat()})
{tomorrow_events}

### TODO.md (use ONLY unchecked [ ] items)
{todo_content}

### Semester Context
{semester_content}

### Latest WHOOP Daily Note ({whoop_note_name})
{whoop_note_content}

Output only the completed markdown briefing — no preamble, no explanation."""


def _duration_minutes(start_iso: str, end_iso: str) -> int:
    fmt = "%Y-%m-%dT%H:%M:%S.%fZ"
    try:
        s = datetime.strptime(start_iso, fmt)
        e = datetime.strptime(end_iso, fmt)
        return int((e - s).total_seconds() / 60)
    except Exception:
        return 0


def call_claude(prompt: str) -> str:
    import anthropic
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


# ── Git ────────────────────────────────────────────────────────────────────────

def git_commit_push(briefing_path: Path, today: date) -> None:
    rel = briefing_path.relative_to(VAULT)
    subprocess.run(["git", "-C", str(VAULT), "add", str(rel)], check=True)
    subprocess.run(
        ["git", "-C", str(VAULT), "commit", "-m", f"briefing: {today.isoformat()}"],
        check=True,
    )
    # push with retry
    for delay in [0, 2, 4, 8, 16]:
        if delay:
            time.sleep(delay)
        result = subprocess.run(
            ["git", "-C", str(VAULT), "push", "-u", "origin",
             "claude/morning-briefing-audio-M2WGq"],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            log("Git push succeeded")
            return
        log(f"Git push failed (attempt), retrying… {result.stderr.strip()}")
    raise RuntimeError("Git push failed after retries")


# ── Main ───────────────────────────────────────────────────────────────────────

async def main() -> None:
    today = date.today()
    log(f"=== Morning briefing starting for {today.isoformat()} ===")

    briefing_path = BRIEFING_DIR / f"{today.isoformat()}.md"
    if briefing_path.exists():
        log("Briefing already exists, skipping generation")
    else:
        # 1. Wait for WHOOP recovery
        recovery_rec = wait_for_recovery()
        token        = get_access_token()
        sleep_rec    = get_sleep(token)

        # 2. Calendar
        tomorrow = today + timedelta(days=1)
        today_events    = get_ical_events(today)
        tomorrow_events = get_ical_events(tomorrow)

        # 3. Vault
        todo_content     = read_file_safe(TODO_FILE)
        semester_content = read_file_safe(SEMESTER_FILE)
        whoop_note_name, whoop_note_content = get_whoop_daily_note()

        # 4. Quote
        quote = pick_quote()

        # 5. Generate
        log("Calling Claude API for briefing…")
        prompt   = build_prompt(
            today, recovery_rec, sleep_rec,
            today_events, tomorrow_events,
            todo_content, semester_content,
            whoop_note_name, whoop_note_content,
            quote,
        )
        briefing = call_claude(prompt)

        # 6. Write
        BRIEFING_DIR.mkdir(parents=True, exist_ok=True)
        briefing_path.write_text(briefing, encoding="utf-8")
        log(f"Briefing written: {briefing_path}")

        # 7. Commit + push
        git_commit_push(briefing_path, today)

    # 8. Upload to NotebookLM + generate audio
    log("Running NotebookLM upload…")
    result = subprocess.run(
        [sys.executable, str(UPLOAD_SCRIPT), str(briefing_path)],
        capture_output=True, text=True,
    )
    if result.stdout:
        log(result.stdout.strip())
    if result.returncode != 0:
        log(f"NotebookLM upload error: {result.stderr.strip()}")
    else:
        log("Audio overview generation started in NotebookLM.")

    log("=== Done ===")


if __name__ == "__main__":
    asyncio.run(main())
