# Personal Dashboard Sync — Reference Guide

> Companion to the nightly scheduled task at
> `/Users/sri/Documents/Claude/Scheduled/training-hub-daily-sync/SKILL.md`
>
> This captures all the operational knowledge learned from actually running the sync,
> so you don't have to re-derive it each time.

---

## Files

| File | Path |
|---|---|
| Dashboard HTML | `/Users/sri/Documents/MyVault/personal-dashboard.html` |
| TODO source | `/Users/sri/Documents/MyVault/second-brain/notes/TODO.md` |
| Scheduled task | `/Users/sri/Documents/Claude/Scheduled/training-hub-daily-sync/SKILL.md` |

---

## Data Sources & Tools

All fetches can be fired in **parallel** in a single tool-call batch:

```
mcp__whoop__get_latest_recovery          → DATA_RECOVERY (single object)
mcp__whoop__get_recoveries (days: 7)     → DATA_RECOVERIES (array of 7)
mcp__whoop__get_workouts   (limit: 20)   → DATA_WORKOUTS
mcp__strava__get-recent-activities (perPage: 20) → DATA_STRAVA
mcp__e9cfcf73-...__list_events           → DATA_EVENTS
Read /Users/sri/.../TODO.md              → TASKS_PENDING / TASKS_DONE
```

Google Calendar tool ID: `mcp__e9cfcf73-4d07-429c-b8c1-b65ff7dfaa1f__list_events`
- Use `startTime: <today>T00:00:00`, `endTime: <today+14>T00:00:00`
- Use `orderBy: "startTime"` for clean ordering

---

## JS Constant Format (exact)

```js
const DATA_RECOVERY = {date:"YYYY-MM-DD", recovery_score:90, hrv_rmssd:163.5, resting_hr:50, spo2:97.6};

const DATA_RECOVERIES = [
  {date:"YYYY-MM-DD", recovery_score:90, hrv_rmssd:163.5, resting_hr:50, spo2:97.6},
  // ... 7 entries, newest first
];

const DATA_WORKOUTS = [
  {date:"YYYY-MM-DD", sport:"swimming", duration:73, strain:14.1, avg_hr:141, max_hr:179},
  // ... 20 entries, newest first
  // sport: raw WHOOP sport string (e.g. "swimming", "running", "activity", "spin", "cycling", "weightlifting_msk", "squash")
  // duration: in minutes
];

const DATA_STRAVA = [
  {id:"18471790987", name:"Night Swim", sport:"swim", dist_m:0, date:"YYYY-MM-DD"},
  // ... 20 entries, newest first
  // sport: mapped value — see sport mapping below
  // dist_m: use 0 when Strava returns "N/A"
];

const DATA_EVENTS = [
  {summary:"Event Name", start:{dateTime:"2026-05-12T09:00:00-04:00"}, location:"820B DISQUE"},
  {summary:"All-day Event", start:{date:"2026-05-15"}, location:""},
  // location: use "" when absent
];

// Tasks — synced from Obsidian · May 12, 2026   ← update this date
const TASKS_PENDING = [
  {name:"Task Name", detail:"due Fri May 15", course:"CS-270", urgent:true},
];
const TASKS_DONE = [
  {name:"Task Name", course:"PHYS-102"},
];
```

### Where to do the edit

Find the block starting with `const DATA_RECOVERY =` and ending just before `// ── Helpers`.
Use `Edit` with `old_string` = the entire old block, `new_string` = the new block.

---

## Sport Mapping: Strava

Infer from the activity **name** (Strava doesn't return a clean sport field):

| Name pattern | sport value |
|---|---|
| swim, pool | `swim` |
| run, jog, mile, easy run | `run` |
| bike, ride, indoor bike, cycling | `bike` |
| weight, lift, strength training | `lift` |
| workout, activity (generic) | `other` |

---

## Sport Mapping: WHOOP → display

The dashboard JS does its own mapping via `whoopSport()`, but for DATA_STRAVA you need to map manually. For DATA_WORKOUTS, pass the raw WHOOP sport string — the dashboard handles it.

---

## Google Calendar — Deduplication

The calendar often returns **duplicate all-day events** for the same deadline (e.g. two entries for "SE-201 — A6 Due" on the same date, one from the course outline and one added manually). Rule:
- When two all-day events have the same date and near-identical summaries, **keep the shorter/cleaner title**.
- Common duplicates: SE-201 assignments (two entries per week), PHYS-102 make-up midterm, MATH-201 midterm window.

---

## TODO.md Parsing

The file uses Obsidian Kanban board format. Sections:

```
## 🔴 This Week ...
### 📚 Academics
- [ ] **Task name** · detail · [[link]]   ← PENDING
- [x] **Done task** ...                   ← DONE (if above ## Archive)

## ✅ Done
- [x] **Done task** ...                   ← DONE

## Archive
- [x] **Old task** ...                    ← SKIP (archived, don't include)
```

**Parsing rules:**
- Pending: every line matching `- [ ]` in the file
- Done (non-archive): every `- [x]` line **above** the `## Archive` heading
- Strip markdown bold (`**...**`), Obsidian links (`[[...]]`), and leading/trailing whitespace from names
- Extract course code from name (e.g. `CS-270`, `PHYS-102`, `SE-201`, `MATH-201`, `CS-265`, `COM-270`) — set to `"Personal"` if none found
- `urgent: true` if the due date is within 7 days of today
- `detail`: the part after ` · ` (e.g. `"due Fri May 15"`, `"in-class, week of May 11"`)

---

## Urgency Threshold

`urgent: true` when due date ≤ today + 7 days.
If a task is already past due (e.g. "due Mon May 11" checked on May 12), mark urgent and add "(overdue)" to detail.

---

## Sync Date Comment

The line `// Tasks — synced from Obsidian · May 11, 2026` appears just above `const TASKS_PENDING`. Update the date to today every run. It's included inside the data block replaced by the Edit call, so it updates automatically.

---

## Common Pitfalls

1. **WHOOP `get_workouts` only returns runs and cycling** — the description says so, but in practice it also returns swimming, squash, spin, and "activity" (generic). Don't filter.

2. **Strava dist_m = 0 for swims/indoor** — that's correct, not missing data.

3. **Calendar `list_events` returns events ending after `startTime`**, not starting after. Events already in progress at the window start will appear. This is fine — the dashboard JS filters by `start.dateTime.slice(0,10)`.

4. **DATA_WORKOUTS sport field** — pass the raw WHOOP string (`"weightlifting_msk"`, `"spin"`, `"squash"`), not a mapped value. The dashboard's `whoopSport()` function handles display conversion.

5. **Don't include the `kj` field** — WHOOP returns it but it's not in the JS schema and the dashboard doesn't use it.

6. **Calendar event start format** — timed events use `{dateTime: "..."}`, all-day events use `{date: "YYYY-MM-DD"}`. Keep the original structure from the API response.
