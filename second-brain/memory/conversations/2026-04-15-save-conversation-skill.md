---
title: Save Conversation Skill Development
last_updated: 2026-04-15
type: conversation
source: claude-code
---

# 2026-04-15 — Save Conversation Skill Development

## What Happened
Sri and Claude built a skill to automatically save conversations to his Obsidian vault. The session focused on creating a system that mirrors the "save this conversation" workflow already designed in the memory wiki schema. Claude discovered that the .claude/skills folder is read-only in the sandbox environment, requiring skills to be distributed as .skill files (zipped archives).

## Key Decisions Made
- Conversation summaries follow the SCHEMA.md template: YAML header (title, last_updated, type, source) + content sections (What Happened, Key Decisions, Facts Learned, Tasks/Action Items, Follow-Up Questions)
- Skill must detect vault path, read session transcript, generate summary, write to conversations/ directory, update log.md and index.md, and append row to project-knowledge.md
- .claude/skills folder is read-only in sandbox — skills cannot be written there directly; must be packaged and distributed as .skill files (zip archives)
- Conversation summaries are filed at the end of every session (Cowork + Claude Code) without requiring user prompting
- Source field distinguishes: cowork, claude-code, or manual

## Facts Learned About Sri
- Wants persistent, accumulating memory across all sessions; each session builds on previous learnings
- Prefers seeing new files/entries as confirmation that the conversation was saved
- Working with both Obsidian vault structure and Claude's skill ecosystem
- Interested in automation workflows that integrate his tools (Obsidian, Claude)
- Vault location: `/sessions/festive-nice-edison/mnt/MyVault/second-brain/` with memory wiki at `memory/`

## Tasks / Action Items Resulting
- Implement save-conversation skill with full workflow (transcript → summary → file + log updates)
- Package skill as .skill file for distribution
- Test skill integration with Cowork and Claude Code session endings
- Document .skill file format and distribution process in SCHEMA.md or skill README

## Follow-Up Questions / Gaps
- Should the skill auto-detect session context (Cowork vs Claude Code) or require user input for source field?
- How should transcripts be accessed/parsed? Session IDs? Environment variables?
- Should conversation slug generation be based on title or timestamp, or both?
- Should there be validation before filing to prevent duplicate/malformed entries?

---

## Related Notes

[[memory/SCHEMA|Schema]] [[memory/index|Memory Index]] [[memory/log|Log]] [[memory/topics/projects|Projects]]
