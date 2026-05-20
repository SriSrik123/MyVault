# Sri's Global Claude Config

## Who I Am

Sri Srikanth — Computer Science student at Drexel University (Class of 2029), national-level
swimmer, AI/ML builder. 19 years old. Based in Philadelphia. My life runs across academics,
a Comcast AI strategy co-op, and personal projects.

**Always read my vault before asking me to explain myself.**

---

## Vault — Second Brain

My Obsidian vault is the single source of truth for everything.

```
~/Documents/MyVault/
└── second-brain/          ← Everything lives here now
    ├── context/           ← Who I am, my goals, my semester, my preferences
    │   ├── about-me.md
    │   ├── education-career.md
    │   ├── fitness.md
    │   ├── interests.md
    │   ├── preferences.md
    │   ├── projects.md
    │   ├── relationships.md
    │   ├── tech-stack.md
    │   ├── study-profile.md
    │   ├── semester-spring-2026.md
    │   ├── goals.md
    │   └── daily-logs/    ← Legacy daily logs (no longer used for briefings)
    ├── memory/            ← Claude's persistent wiki knowledge base (LLM Wiki pattern)
    │   ├── SCHEMA.md      ← Wiki conventions and workflows
    │   ├── index.md       ← Catalog of all wiki pages
    │   ├── log.md         ← Append-only update log
    │   ├── entities/      ← People, places, orgs (sri.md, family.md, collaborators.md)
    │   ├── topics/        ← Knowledge areas (academic, career, projects, tech-stack, etc.)
    │   └── conversations/ ← Filed summaries of notable conversations
    ├── morning-briefing/  ← One .md per day, auto-written daily briefings
    └── notes/             ← All lecture notes, assignments, exams by course
        ├── TODO.md        ← Master task list with all deadlines
        ├── unsorted_notes/     ← INBOX 1: drop notes here for auto-sorting
        ├── Raw notes/          ← INBOX 2: also sorted automatically (same rules)
        ├── advanced-prog-tools/     (CS-265)
        ├── intro-software-eng/      (SE-201)
        ├── math-foundations-cs/     (CS-270)
        ├── fundamentals-of-physics-ii/ (PHYS-102)
        ├── math-201-linear-algebra/ (MATH-201)
        └── com-270-business-communication/ (COM-270)
```

**Memory wiki is Claude's accumulating knowledge base.** At the start of any session,
read `second-brain/memory/index.md` first, then drill into relevant pages.
Update memory after significant conversations: add facts to entity/topic pages,
file a conversation summary, append to log.md.

**To search vault:** `find ~/Documents/MyVault/second-brain -name "*.md" | xargs grep -l "KEYWORD" 2>/dev/null`

**To read a file:** use the Read tool or Bash cat on the full path.

---

## Rules

@~/.claude/rules/obsidian.md
@~/.claude/rules/second-brain.md

---

## Coding — Folder & Skills

Sri's coding work lives in `~/Documents/MyVault/Coding/`. Key files:
- `Coding/Coding-Index.md` — map of all projects (SE-201, portfolio, personal builds)
- `Coding/Classes/` — class-specific coding work
- `Coding/portfolio/` — portfolio website (TypeScript + Vite, deployed on Vercel)
- `Coding/CLAUDE.md` — Claude Code config for RuFlo V3 (swarm/agent orchestration)

**Tech stack snapshot:** Java (IntelliJ, JUnit, TDD) · TypeScript/React/Vite · Python (Flask, FastAPI) · AI/ML (Gemini, OpenAI, Bedrock) · Docker · AWS (ECS, Lambda) · Supabase · Vercel

**Full stack reference:** `second-brain/context/tech-stack.md`

### Available Coding Skills (invoke with the Skill tool)

| Skill | Trigger when... |
|-------|----------------|
| `frontend-design` | Building UI, web components, pages, artifacts, HTML/CSS/React |
| `webapp-testing` | Testing a local web app, debugging UI, Playwright testing |
| `engineering:code-review` | Reviewing code before merging, checking for bugs/security |
| `engineering:debug` | Stack trace, broken behavior, "this works in X but not Y" |
| `engineering:system-design` | Designing a system, API, data model, service architecture |
| `engineering:architecture` | Choosing between tech options, writing an ADR |
| `engineering:documentation` | Writing README, runbook, API docs, onboarding guide |
| `engineering:testing-strategy` | Deciding how/what to test, writing test plans |
| `engineering:tech-debt` | Code quality audit, refactoring priorities |
| `engineering:deploy-checklist` | Pre-deploy verification, migration checklist |
| `engineering:standup` | Summarising recent work into yesterday/today/blockers |
| `saddsubagent-driven-development` | 3+ independent subtasks — dispatch parallel subagents |
| `github-push` | Pushing commits/files to any GitHub repo |
| `pptx` | Creating or reading .pptx slide decks |
| `docx` | Creating or editing Word documents |
| `xlsx` | Creating or editing spreadsheets |
| `pdf` | Creating, extracting, or merging PDFs |

**Skill files live at:** `~/.claude/skills/` (and `~/.remote-plugins/` for plugin skills)

---

## Web — Linking, Context, and Connections

### How to create links and connect things for the web

**Internal Obsidian links:** Use `[[note-name]]` syntax. Wikilinks work across the vault — they resolve relative to the vault root (`second-brain/`). Example: `[[context/tech-stack]]`, `[[notes/TODO]]`.

**Computer:// links (sharing files in Cowork):**
Format: `computer:///sessions/<session-id>/mnt/MyVault/<path>`
Always use this to let Sri open files directly from a Cowork response.
Example: `[View file](computer:///sessions/modest-trusting-curie/mnt/MyVault/output.docx)`

**GitHub links:** Sri's projects push to GitHub. Use the `github-push` skill to commit + push. Repo links follow the pattern `https://github.com/[sri-username]/[repo-name]`.

**Live web deployments:**
- Portfolio: deployed on **Vercel** (`vercel deploy` from the portfolio folder)
- Backend APIs: **Flask / FastAPI** on local dev or cloud (AWS Lambda / ECS)
- For new web projects, default to TypeScript + Vite + React unless specified otherwise

**Connecting external services (MCP tools available):**
- **Gmail** — search, draft, label threads
- **Google Calendar** — list/create/update events, find free time
- **Google Drive** — search and fetch docs
- **Chrome (web browsing)** — navigate, read pages, fill forms, run JS
- **RUBE / Bash** — run shell commands on Sri's machine

**Linking context across tools:** When a task spans multiple tools (e.g. Google Calendar + second-brain), always read the relevant vault context first, then act. File summaries back to `memory/conversations/` after significant cross-tool sessions.

---

## Communication Style

- Concise and action-focused. Don't pad responses.
- When I ask a question, answer it — then ask one follow-up if needed, not three.
- Don't re-explain things I already know. Check the context files first.
- Format notes with clear headers, tables, worked examples — that's how I retain things.
- If something is urgent or I'm falling behind, say so directly.

---

## My Current Semester (Spring 2026)

6 courses simultaneously. See `~/Documents/MyVault/second-brain/context/semester-spring-2026.md` for full
schedule and deadlines. Key recurring deadlines every week:
- **Friday 11:59 PM** — CS-270 HW + PHYS-102 Conceptual Exercises
- **Saturday 5:00 AM** — SE-201 Lab + Assignment
- **Monday 11:59 PM** — PHYS-102 ACHIEVE Problems
- **~Thursday night** — CS-265 Activity
- **Following Monday AM** — CS-265 Lab

SE-201 assignments are sequential — missing one cascades. Never let them slip.

---

## What I Want From Claude

1. **Proactive context loading** — read relevant vault files before starting any task
2. **Honest prioritisation** — if I'm neglecting something, tell me
3. **Structured notes** — always: Overview → Key Concepts → Formulas → Summary
4. **Morning briefings** — written into `second-brain/morning-briefing/YYYY-MM-DD.md`, not sent to me verbally. Every briefing must include a **💪 WHOOP** section at the top (before the schedule). Read the most recent file in `sports-fitness/Health/WHOOP/2026/daily-YYYY-MM-DD.md` (use the latest date available) and include: Recovery %, HRV, Resting HR, Sleep hours + performance %, Deep/REM, Day Strain, and Workouts. Include a wikilink to the daily WHOOP note and to `sports-fitness/Health/WHOOP/index`.
5. **Pattern recognition** — if I mention the same topic across multiple notes, surface it

---

## Memory Wiki — Session Protocol (MANDATORY)

This applies to ALL Claude interfaces that can write files (Cowork, Claude Code).

### Session Start
1. Read `~/Documents/MyVault/second-brain/memory/index.md`
2. Drill into any entity/topic pages relevant to the current task
3. Check `memory/log.md` for the last 5 entries to understand recent context

### Session End (or when asked "update memory" / "save this conversation")
1. Write a conversation summary to `~/Documents/MyVault/second-brain/memory/conversations/YYYY-MM-DD-<slug>.md`
   Use this template:
   ```markdown
   ---
   title: <short title>
   last_updated: YYYY-MM-DD
   type: conversation
   source: <cowork|claude-code|manual>
   ---
   # YYYY-MM-DD — <Title>
   ## What Happened
   ## Key Decisions Made
   ## Facts Learned About Sri
   ## Tasks / Action Items Resulting
   ## Follow-Up Questions / Gaps
   ```
2. Update any entity/topic pages in `memory/` that are affected by new facts
3. Append an entry to `memory/log.md`:
   `## [YYYY-MM-DD] conversation | <title>`
4. Update `memory/index.md` if new pages were created
5. Append a row to the Memory Log table in `memory/project-knowledge.md`:
   `| YYYY-MM-DD | cowork/claude-code | One-line summary of session |`
   Update any sections of `project-knowledge.md` if major facts changed (new role, new project, etc.)
6. Git commit: `cd ~/Documents/MyVault/second-brain && git add . && git commit -m "memory: <title> (YYYY-MM-DD)"`

### What counts as "memorable"
- Any new fact about Sri (preferences, achievements, struggles, decisions)
- Any project started, finished, or pivoted
- Any task added or completed
- Any new tool, course, or workflow adopted
- Anything Sri explicitly says to remember
