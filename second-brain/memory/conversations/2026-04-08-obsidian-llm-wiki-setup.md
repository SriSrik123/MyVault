---
title: Obsidian LLM Wiki Setup
last_updated: 2026-04-08
type: conversation
source: cowork
---

# 2026-04-08 — Obsidian LLM Wiki Setup

## What Happened
Sri asked Claude to set up an LLM Wiki system in his Obsidian vault based on the pattern from a document he shared. The goal: Claude maintains a persistent, accumulating knowledge base so every session builds on the last — no rediscovering facts from scratch.

## Key Decisions Made
- Memory wiki lives at `second-brain/memory/` with entities/, topics/, conversations/ subdirectories
- `context/` folder moved into `second-brain/` (cleaned up root-level duplicate in Obsidian)
- `Raw notes/` in notes/ is now a second unsorted inbox alongside `unsorted_notes/`
- `project-knowledge.md` created as a condensed snapshot for syncing to claude.ai Projects
- CLAUDE.md updated with mandatory session protocol: read memory at start, file summary at end
- Conversation summaries filed automatically by Claude at end of every Cowork + Claude Code session
- Claude.ai web chat cannot auto-sync (no file access); Sri uses project-knowledge.md to manually refresh Project Knowledge when needed

## Facts Learned About Sri
- Wants Claude to have persistent, accumulating memory across all sessions
- Uses the "LLM Wiki" mental model: Claude as programmer, Obsidian as IDE, wiki as codebase
- Prefers everything consolidated under second-brain (not scattered across vault root)
- Wants to SEE a new file/entry after each conversation as confirmation it was saved

## Tasks / Action Items Resulting
- Raw notes physics files (Phys102 intro, week2, lecture 4) sorted into fundamentals-of-physics-ii/lectures/
- Memory wiki seeded from all existing context files on day 1

## Follow-Up Questions / Gaps
- Does Sri want conversation entries for short/trivial sessions too, or only meaningful ones?
- Should there be a weekly summary entry that rolls up the week's conversations?

---

## Related Notes

[[memory/entities/sri]]  [[memory/SCHEMA|Schema]]  [[memory/index|Memory Index]]  [[memory/log|Log]]  [[memory/conversations/2026-04-08-vault-link-audit|Next Conversation →]]
