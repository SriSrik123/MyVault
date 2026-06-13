# Memory Wiki — Log

Append-only chronological record of all memory updates.
Format: `## [YYYY-MM-DD] <type> | <title>`

Quick parse: `grep "^## \[" log.md | tail -10`

---

## [2026-04-08] lint | Vault Link Audit & Memory Web Setup

- Full vault link audit — scanned all .md files using Obsidian suffix-matching logic
- Fixed 2 broken `[[Portfolio-Note]]` links — created `Coding/portfolio/Portfolio-Note.md`
- Added Daily Logs section to `memory/index.md` with links to Apr 7 and Apr 8 briefings
- Added back-links (Related Notes) to `context/daily-logs/2026-04-07.md` and `2026-04-08.md`
- Removed duplicate `conversations/2026-04-08-setup-llm-wiki.md` (canonical: `obsidian-llm-wiki-setup.md`)
- Updated `SCHEMA.md`: added daily-logs to directory layout, daily briefing workflow, vault paths
- Filed: `conversations/2026-04-08-vault-link-audit.md`

## [2026-04-08] conversation | Obsidian LLM Wiki Setup

- Filed: `conversations/2026-04-08-obsidian-llm-wiki-setup.md`
- Sri confirmed: wants a new file/entry after every conversation as proof it was saved
- Clarified: no automatic trigger exists — Claude files it manually at session end

## [2026-04-15] conversation | Save-Conversation Skill Implementation

- Filed: `conversations/2026-04-15-save-conversation-skill.md`
- Built new skill to auto-file conversations at end of every Cowork + Claude Code session
- Skill detects vault path dynamically, reads transcripts, generates summaries from SCHEMA template
- Discovered: .claude/skills is read-only; skills must be packaged as .skill files (zipped archives)
- Updated `memory/topics/projects.md` with new save-conversation skill project

## [2026-04-15] conversation | CS-270 Homework Submission Fix & Midterm Planning

- Filed: `conversations/2026-04-15-cs270-homework-debug.md`
- Updated `topics/academic.md` — added CS-270 midterm study plan and workflow friction note
- Sri debugged 403 error on Gradescope submission: root cause was renamed file not updated in zip
- Created two-phase CS-270 midterm study plan: practice ch 1-4 by Apr 25, proof review week before

## [2026-04-15] conversation | Comcast Co-op Transition & Portfolio Update

- Filed: `conversations/2026-04-15-comcast-coop-transition.md`
- Sri transitioning from AI Strategy to ML Engineering team at Comcast, starting May 1
- Expressed excitement about hands-on engineering but acknowledged some nervousness
- Decision: Add MCP Tools showcase section to portfolio to highlight Claude/Anthropic integration work
- Updated `topics/career-work.md` — documented role transition and timing
- Updated `topics/projects.md` — added MCP Tools project and portfolio website update notes

## [2026-04-08] setup | Initial memory wiki created

- Created memory wiki structure: `SCHEMA.md`, `index.md`, `log.md`
- Created entity pages: `entities/sri.md`, `entities/family.md`, `entities/collaborators.md`
- Created topic pages: `topics/academic.md`, `topics/career-work.md`, `topics/projects.md`, `topics/tech-stack.md`, `topics/fitness.md`, `topics/interests.md`, `topics/goals.md`
- Seeded all pages from existing context files (about-me, education-career, tech-stack, projects, relationships, interests, goals, fitness)
- Moved `context/` folder into `second-brain/`
- Sorted `Raw notes/` physics files into `fundamentals-of-physics-ii/lectures/`
- Filed conversation summary: `conversations/2026-04-08-setup-llm-wiki.md`
- Updated obsidian-notes-sorter skill to handle `Raw notes` folder
- Updated second-brain-add skill to reference memory wiki

## [2026-04-21] conversation | Workout File Move & Conversation Saving Setup

- Filed: `conversations/2026-04-21-workout-file-move-conversation-saving.md`
- Moved `sports-fitness/workouts/THIS-WEEK.md` → `notes/THIS-WEEK.md` (alongside TODO.md)
- Updated `rules/obsidian.md` — added memory wiki index + recent conversations to proactive context loading list
- Updated `memory/index.md` — added new conversation entry

## [2026-06-10] conversation | Vault City Visualization App

- Filed: `conversations/2026-06-10-vault-city-app.md`
- Built vault-city.html (city map of the vault) + scripts/build-vault-city.py generator

## [2026-06-12] conversation | Vault City Desktop App (Electron + React)

- Filed: `conversations/2026-06-12-vault-city-desktop-app.md`
- Rebuilt Vault City as an Electron + React + Vite desktop app (vault-city-app/) with live IPC vault scanning and a cyberpunk UI

## [2026-06-12] update | Vault City → 3D (Three.js)

- Rebuilt the renderer in Three.js: navigable 3D city, WASD + Google-Maps controls, cinematic fly-in zoom, neon bloom graphics
- Fixed layout bug: duplicate `sports-fitness` folders (root + second-brain) dropped 18 notes; recursive mergeNode → 233/233 buildings

## [2026-06-12] update | Vault City → Vault Heart (beating-heart graph)

- Moved app to Coding/vault-city-app/; deleted old 2D vault-city.html + scripts
- New Three.js HeartEngine: notes as cells in a beating heart-shaped volume, links as vessels, click a cell → fly in + trace its connections (neighbors lit, rest dimmed)

## [2026-06-12] update | Vault Heart → anatomical shape

- Replaced valentine-symbol sampler with a metaball anatomical heart (ventricles/atria/apex blobs, tapered pointed apex, flattened, leaning) + great vessels (aorta/pulmonary/vena cava tubes)

## [2026-06-12] update | Vault Heart — clumped/dense muscle

- Tightened scale (HS 13→10.5), bigger overlapping cells, denser tissue (7.4k pts), fatter apex → cells clump into a solid heart mass instead of a sparse cloud

## [2026-06-12] fix | Vault Heart — click-to-zoom + darker theme

- Bug: canvas clicks opened the reader but never flew the camera in (the click handler set selection but skipped focusNote). Fixed: clicks now route through focusNote → zoom-in + trace connections.
- Toned down the neon: lower exposure (0.92), much weaker bloom (0.32/threshold 0.48), dimmer emissive/lights/tissue/flow, near-black background. Darker, moodier heart.

## [2026-06-12] change | Vault Heart — circular popup over the cell

- Replaced the side reader panel with a circular popup centered over the zoomed cell (clipped circle, rim colored by the cell's region hue, content fades at the edges, connections as chips). Click flies head-on into the sphere; the note pops up in the circle.
