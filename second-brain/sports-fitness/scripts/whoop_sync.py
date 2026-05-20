#!/usr/bin/env python3
"""
Daily Whoop sync — runs every morning via scheduler.
Pulls recovery, sleep, HRV, strain and writes to:
  - sports-fitness/workouts/history/YYYY-MM-DD.md  (daily log)
  - sports-fitness/sleep/log.md                    (running sleep table)
"""

import requests
import json
from pathlib import Path
from datetime import date

VAULT       = Path(__file__).resolve().parents[1]   # sports-fitness/
CONFIG_FILE = VAULT / "scripts" / ".whoop_tokens.json"
HISTORY_DIR = VAULT / "workouts" / "history"
SLEEP_LOG   = VAULT / "sleep" / "log.md"

API = "https://api.prod.whoop.com/developer/v1"


# ── helpers ──────────────────────────────────────────────────────────────────

def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def refresh_access_token(config):
    resp = requests.post("https://api.prod.whoop.com/oauth/oauth2/token", data={
        "grant_type":    "refresh_token",
        "refresh_token": config["refresh_token"],
        "client_id":     config["client_id"],
        "client_secret": config["client_secret"],
    })
    resp.raise_for_status()
    config.update(resp.json())
    save_config(config)
    return config

def get(path, config):
    resp = requests.get(f"{API}{path}", headers={"Authorization": f"Bearer {config['access_token']}"})
    resp.raise_for_status()
    return resp.json()

def fmt(val, unit=""):
    if val is None or val == "":
        return "—"
    if isinstance(val, float):
        return f"{val:.1f}{unit}"
    return f"{val}{unit}"


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    config = load_config()
    if "refresh_token" in config:
        config = refresh_access_token(config)
    today  = date.today().isoformat()

    # ── fetch ─────────────────────────────────────────────────────────────────
    try:
        rec = get("/recovery?limit=1", config).get("records", [{}])[0].get("score", {})
    except Exception as e:
        rec = {}
        print(f"Warning: recovery fetch failed — {e}")

    try:
        slp_rec = get("/activity/sleep?limit=1", config).get("records", [{}])[0]
        slp     = slp_rec.get("score", {})
        stages  = slp.get("stage_summary", {})
    except Exception as e:
        slp, stages = {}, {}
        print(f"Warning: sleep fetch failed — {e}")

    try:
        cyc = get("/cycle?limit=1", config).get("records", [{}])[0].get("score", {})
    except Exception as e:
        cyc = {}
        print(f"Warning: cycle fetch failed — {e}")

    # ── parse ─────────────────────────────────────────────────────────────────
    recovery_score = rec.get("recovery_score")
    hrv            = rec.get("hrv_rmssd_milli")
    rhr            = rec.get("resting_heart_rate")
    spo2           = rec.get("spo2_percentage")

    sleep_ms       = stages.get("total_in_bed_time_milli", 0)
    sleep_hours    = round(sleep_ms / 3600000, 1) if sleep_ms else None
    sleep_perf     = slp.get("sleep_performance_percentage")
    sleep_eff      = slp.get("sleep_efficiency_percentage")
    rem_pct        = round(stages.get("rem_sleep_time_milli", 0) / sleep_ms * 100, 1) if sleep_ms else None
    deep_pct       = round(stages.get("slow_wave_sleep_time_milli", 0) / sleep_ms * 100, 1) if sleep_ms else None

    strain         = cyc.get("strain")
    avg_hr         = cyc.get("average_heart_rate")
    max_hr         = cyc.get("max_heart_rate")
    cal_kcal       = round(cyc.get("kilojoule", 0) / 4.184) if cyc.get("kilojoule") else None

    # ── write daily history file ──────────────────────────────────────────────
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    history_file = HISTORY_DIR / f"{today}.md"

    history_file.write_text(f"""# {today}

## Whoop Data

| Metric | Value |
|--------|-------|
| Recovery | {fmt(recovery_score, '%')} |
| HRV | {fmt(hrv, ' ms')} |
| Resting HR | {fmt(rhr, ' bpm')} |
| SpO2 | {fmt(spo2, '%')} |
| Sleep | {fmt(sleep_hours, ' hrs')} ({fmt(sleep_perf, '% perf')} · {fmt(sleep_eff, '% eff')}) |
| REM | {fmt(rem_pct, '%')} |
| Deep | {fmt(deep_pct, '%')} |
| Strain | {fmt(strain)} |
| Avg HR | {fmt(avg_hr, ' bpm')} |
| Max HR | {fmt(max_hr, ' bpm')} |
| Calories | {fmt(cal_kcal, ' kcal')} |

## Sessions

*(workouts logged from Whoop or add manually)*

## Notes

""")

    # ── append to sleep log ───────────────────────────────────────────────────
    import re
    new_row  = f"| {today} | {fmt(sleep_hours)} | {fmt(sleep_perf, '%')} | HRV {fmt(hrv, 'ms')} · RHR {fmt(rhr, 'bpm')} · Deep {fmt(deep_pct, '%')} · REM {fmt(rem_pct, '%')} |"
    log_text = SLEEP_LOG.read_text()

    if re.search(rf"^\| {re.escape(today)} \|", log_text, re.MULTILINE):
        # Update existing row for today
        log_text = re.sub(rf"^\| {re.escape(today)} \|.*", new_row, log_text, flags=re.MULTILINE)
    elif "| — | — | — | — |" in log_text:
        # Replace the first placeholder row only (in the data table, not weekly averages)
        log_text = log_text.replace("| — | — | — | — |", new_row, 1)
    else:
        # Insert new row before the divider
        log_text = log_text.replace("---\n\n## Weekly Averages", f"{new_row}\n\n---\n\n## Weekly Averages")

    SLEEP_LOG.write_text(log_text)

    print(f"✓ Whoop sync complete for {today}")
    print(f"  Recovery: {fmt(recovery_score, '%')}  HRV: {fmt(hrv, 'ms')}  Sleep: {fmt(sleep_hours, 'h')}  Strain: {fmt(strain)}")
    print(f"  → {history_file}")


if __name__ == "__main__":
    main()
