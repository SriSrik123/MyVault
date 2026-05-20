---
title: Workout file move and conversation saving setup
last_updated: 2026-04-21
type: conversation
source: claude-code
---

# 2026-04-21 — Workout File Move & Conversation Saving Setup

## What Happened
Sri asked to move his workout file from `second-brain/sports-fitness/workouts/THIS-WEEK.md` to the same directory as his `TODO.md` (`second-brain/notes/`). File was moved successfully. Sri then asked where conversations were being saved — discovered they weren't being auto-saved in Claude Code sessions. He asked to set that up so every conversation is filed to the memory wiki and context is loaded automatically each time.

## Key Decisions Made
- `THIS-WEEK.md` (weekly workout plan) now lives at `second-brain/notes/THIS-WEEK.md` alongside `TODO.md`
- Conversations should be saved to `second-brain/memory/conversations/` after every Claude Code session
- Memory wiki context should be loaded at the start of every session via CLAUDE.md rules

## Facts Learned About Sri
- Sri tracks weekly workouts in a file called `THIS-WEEK.md`
- He wants Claude to have persistent context across all conversations — not just the second brain context files, but also the conversation history in the memory wiki
- He wasn't aware conversations weren't being auto-saved in Claude Code (vs Cowork)

## Tasks / Action Items Resulting
- Claude should load `memory/index.md` and relevant `memory/conversations/` files at session start for context
- CLAUDE.md updated to reference memory wiki as part of proactive context loading

## Follow-Up Questions / Gaps
- Should old workout files be archived somewhere, or is `THIS-WEEK.md` replaced weekly in place?

---

## Related Notes
[[memory/entities/sri]]  [[memory/SCHEMA|Schema]]  [[memory/index|Memory Index]]  [[memory/log|Log]]
