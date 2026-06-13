---
title: Vault City rebuilt as Electron desktop app
last_updated: 2026-06-12
type: conversation
source: claude-code
---

# 2026-06-12 — Vault City Desktop App (Electron + React)

## What Happened
Two days after building the standalone `vault-city.html`, Sri asked (via the ui-ux-pro-max skill) to make it "a city UI, use react or whatever, and make it a desktop app." Ran the design-system generator → **Cyberpunk UI** style, **Fira Code / Fira Sans**, neon-glow + scanline effects. Built a full **Electron + React + Vite** app in `vault-city-app/`: the Electron main process scans the live vault over IPC (no more baked-in data), and a React shell hosts an upgraded neon city canvas. Verified the whole feature set in the browser (preview MCP) and confirmed the actual Electron desktop window boots and the live IPC scan returns real data (232 files, 248 links).

## Key Decisions Made
- **Live IPC scan over baked-in data**: `electron/scan.cjs` is shared by the Electron main process (live `window.vaultAPI.getCity()`) and `gen-data.cjs` (static `public/vault-data.json` for browser dev). One scanner, two entry points.
- **Canvas stays imperative**: ported the proven renderer into a `CityEngine` class; React owns only the chrome (HUD, reader, search, legend) and bridges to the engine via a ref + callbacks. Keeps React out of the 60fps draw loop.
- Overrode the design system's recommended *light* palette — it contradicted its own "avoid light mode" anti-pattern — and went dark-neon as the Cyberpunk style intends.
- Added CSP, prefers-reduced-motion handling, SVG icons (no emoji), focus states — pre-delivery checklist.
- Kept the original `vault-city.html` as the zero-dependency "lite" version.

## Bugs Found & Fixed During QA
- **HUD stats race**: district count showed 0 until an unrelated re-render; fixed by bumping a `ready` state when the engine mounts.
- **In-reader link resolver**: only matched bare note names, so path-style `[[second-brain/notes/.../assignments]]` wikilinks silently no-op'd. Added `resolveLink` (name + vault-path + basename) and `resolveByPath` (folder-relative md links), mirroring the scanner's own resolution.

## Facts Learned About Sri
None — no new personal context surfaced.

## Tasks / Action Items Resulting
- Run the app with `cd vault-city-app && npm install && npm run app` (relaunch later with `npm start`).
- App code is uncommitted in the working tree — Sri to review and commit when ready. `node_modules/`, `dist/`, `release/`, and `public/vault-data.json` are gitignored.
- Optional: `electron-builder` is wired (`npm run dist`) but not installed yet — installs on demand to package a .dmg.

## Follow-Up Questions / Gaps
- Could auto-rescan on file-watch instead of the manual ⟳ button; not built yet.
- Packaging to a distributable .app/.dmg not done (heavy electron-builder download); only the runnable dev/IPC path is verified.

---

## Related Notes
[[memory/conversations/2026-06-10-vault-city-app]]  [[memory/entities/sri]]  [[memory/index|Memory Index]]  [[memory/log|Log]]
