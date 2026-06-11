---
title: Vault City visualization app built
last_updated: 2026-06-10
type: conversation
source: claude-code
---

# 2026-06-10 — Vault City Visualization App

## What Happened
Sri asked for a game/app that renders his entire vault as a navigable city — top-level folders as city districts, files as buildings, note links as roads, with cars and the ability to open any md file in-app. Claude built a two-part system: `scripts/build-vault-city.py` (scans the vault, excludes node_modules/graphify/hidden dirs, extracts wikilinks + markdown links, embeds everything as JSON) and `scripts/vault-city-template.html` (canvas renderer). The generated standalone app is `vault-city.html` at the vault root — 229 notes, 248 link-roads, 11 districts. Verified working in browser preview: pan/zoom, search, click-to-read markdown panel with clickable wikilinks, "Open in Obsidian" deep link, animated traffic, all-roads toggle.

## Key Decisions Made
- Excluded `graphify/` (1,090 auto-generated node files) and `Coding/.claude` (216 plugin-cache files) so the city only shows real notes
- Promoted `second-brain`'s subfolders (notes, morning-briefing, memory, context…) to top-level districts since it held 197 of 229 files and would otherwise be one giant monochrome blob
- Root-level loose files grouped into a "City Hall" district
- Single self-contained HTML with embedded note content (596 KB) — works offline, regenerate anytime with `python3 scripts/build-vault-city.py`

## Facts Learned About Sri
None — no new personal context surfaced.

## Tasks / Action Items Resulting
- Re-run `python3 scripts/build-vault-city.py` after adding notes to refresh the city (could be added to the nightly sorter schedule if Sri wants it auto-fresh)

## Follow-Up Questions / Gaps
- City could auto-rebuild nightly; not set up yet — Sri hasn't asked

---

## Related Notes
[[memory/entities/sri]]  [[memory/SCHEMA|Schema]]  [[memory/index|Memory Index]]  [[memory/log|Log]]
