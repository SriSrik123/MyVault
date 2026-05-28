---
name: morning-briefing
description: "Generate Sri's daily morning briefing from vault + calendar, write it to second-brain/morning-briefing/YYYY-MM-DD.md, then upload to NotebookLM and generate an audio overview."
---

# Morning Briefing Skill

You are generating Sri's daily morning briefing. Follow every step exactly — no skipping.

---

## Step 1 — Get Today's Date

Run:
```bash
date +%Y-%m-%d
date +%A
```

Store the date as `TODAY` (e.g. `2026-05-20`) and the weekday as `WEEKDAY` (e.g. `Wednesday`).

---

## Step 2 — Read the Vault

Read these two files in full:
- `/home/user/MyVault/second-brain/notes/TODO.md` — master task list
- `/home/user/MyVault/second-brain/context/semester-spring-2026.md` — course schedule

---

## Step 3 — Read the Latest WHOOP Data

**If `WHOOP_DATA_FILE` env var is set** (running via GitHub Actions — data was pre-fetched):
```bash
cat "$WHOOP_DATA_FILE"
```
Parse the JSON. The `recovery` key has `score.recovery_score`, `score.hrv_rmssd_milli`, `score.resting_heart_rate`. The `sleep` key has `score.sleep_performance_percentage`, `score.slow_wave_sleep_percentage`, `score.rem_sleep_percentage`, and `start`/`end` timestamps for duration. Extract all values for the briefing table.

**Otherwise** (interactive session — read from vault):
```bash
ls /home/user/MyVault/sports-fitness/Health/WHOOP/2026/ | sort | tail -1
```
Read that file. Extract: Recovery %, HRV, Resting HR, Sleep hours + performance %, Deep sleep %, REM sleep %, Day Strain, and any workouts logged.

---

## Step 4 — Get Calendar Events

**First, try the MCP tool** (works in interactive Claude Code sessions):
Use `mcp__e9cfcf73-4d07-429c-b8c1-b65ff7dfaa1f__list_events` to fetch:
- **Today**: time range `TODAY 00:00` → `TODAY 23:59` (local, America/New_York)
- **Tomorrow**: time range `TOMORROW 00:00` → `TOMORROW 23:59`

**If the MCP tool is unavailable** (e.g., running via GitHub Actions), fall back to `icalBuddy` on Mac:
```bash
icalBuddy -f -b "• " -nc -npn -iep "title,datetime" eventsFrom:TODAY to:TODAY
```

**If both are unavailable**, write in the briefing:
> *Calendar sync unavailable — check your calendar app for today's schedule.*

List all events including classes, swim practice, co-op meetings, and any personal events.

---

## Step 5 — Pick a Quote

Run:
```bash
python3 -c "
import json, random
quotes = json.load(open('/home/user/MyVault/scripts/quotes.json'))
q = random.choice(quotes)
print(f'\"{q[\"text\"]}\" — {q[\"author\"]}')
"
```

---

## Step 6 — Determine Today's Workout from Calendar

From the calendar events pulled in Step 4, identify any swim practice, gym sessions, or workout events today. List the specific event name and time. If none, say "No workout on calendar today."

---

## Step 7 — Analyze TODO.md

From TODO.md, only include **unchecked `[ ]` items** — skip anything `[x]` or in the Archive section.

Categorize them:
- **Due today or tomorrow** — highest urgency
- **Due this week** (within 7 days of TODAY) — sort by date
- **Watch-out patterns** — SE-201 Saturday 5AM deadlines, async course drift (MATH-201, COM-270), anything mentioned repeatedly but not acted on

---

## Step 8 — Write the Briefing File

Ensure the folder exists:
```bash
mkdir -p /home/user/MyVault/second-brain/morning-briefing
```

Write to: `/home/user/MyVault/second-brain/morning-briefing/TODAY.md`

Use **exactly** this format (substitute all bracketed values with real data):

```markdown
# Daily Briefing — [WEEKDAY, Month DD YYYY]

> "[quote text]" — Author

## 💪 WHOOP — [date of WHOOP file]
| Metric | Value |
|--------|-------|
| Recovery | [X]% |
| HRV | [X] ms |
| Resting HR | [X] bpm |
| Sleep | [X]h [X]min · [X]% performance |
| Deep Sleep | [X]% |
| REM Sleep | [X]% |
| Day Strain | [X] |
| Workouts | [workout name(s) or "None logged"] |

[[sports-fitness/Health/WHOOP/2026/daily-YYYY-MM-DD|View WHOOP Note]] · [[sports-fitness/Health/WHOOP/index|WHOOP Index]]

---

## 🏊 Today's Workout
[Workout from calendar, or "No workout on calendar today."]

---

## 📅 Today's Schedule
[Every calendar event today: `HH:MM AM/PM — Event Title`. If none: "No events on calendar today."]

## 🗓️ Tomorrow
[Tomorrow's events: `HH:MM AM/PM — Event Title`. Keep it brief.]

---

## 🔴 Due Today / Tomorrow
[Unchecked TODO items due today or tomorrow. Format: `- **COURSE-XXX** — Assignment name · due DATE`. If none: "Nothing due in the next 24 hours."]

## 📅 This Week
[All unchecked TODO items due within 7 days, sorted by date. Same format as above.]

---

## 🧠 Priority Focus
[1–3 sentences MAX. What's highest-stakes right now? Name the specific assignment and why it matters first. Be direct.]

## ⚠️ Watch Out For
[Flag any of: SE-201 Saturday 5AM deadlines approaching, async course drift (MATH-201/COM-270 — any recent activity?), or patterns of repeated mentions without action. If nothing to flag, omit this section.]
```

**Rules:**
- Only include `[ ]` unchecked items from TODO.md — never invent tasks
- Use real data only — no filler or invented events
- The briefing should take 30 seconds to read

---

## Step 9 — Commit and Push the Briefing

Commit the new briefing file so it's available on the Mac:
```bash
cd /home/user/MyVault
git add second-brain/morning-briefing/TODAY.md
git commit -m "briefing: TODAY"
git push origin HEAD
```

`git push origin HEAD` pushes to whichever branch is currently checked out — works in both interactive sessions (feature branch) and GitHub Actions (main).

The NotebookLM audio upload runs on the Mac (not here — Google blocks cloud IPs).
The Mac launchd job picks up the new file automatically after `git pull`.

---

## Step 10 — Confirm

Tell Sri:
- The file path of the briefing
- One sentence summary of what he most needs to do today
- Remind him the audio will be ready in NotebookLM within a few minutes of his Mac syncing

Do NOT narrate the steps you took. Just deliver the result.
