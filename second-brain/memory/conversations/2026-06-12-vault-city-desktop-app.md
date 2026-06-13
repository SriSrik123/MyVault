---
title: Vault City — Electron + React + Three.js 3D desktop app
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

## Update — same session: rebuilt in 3D (Three.js)
Sri then asked to make it "like a video game… a real city with streets like Google Maps live view… control it… zoom into a building when clicked… good graphics." Swapped the 2D canvas renderer for a **Three.js WebGL** engine (`src/city/engine3d.js`), reusing the proven model/treemap (extracted to `src/city/layout.js`); the React shell/reader/search were untouched. Result: extruded 3D buildings (height = note size) with neon wireframes, district ground-plates, Tron grid floor, fog, **UnrealBloom** glow, patrolling cars; **MapControls + WASD** navigation; **raycast click → cinematic fly-in/zoom** into the building; CSS2D floating district labels.
- **Three bugs found & fixed during QA:** (1) `EffectComposer` pixel-ratio not synced → scene rendered into a sub-rectangle; (2) click raycast used the last `pointermove` NDC, so programmatic/touch clicks missed → now derives the ray from the click's own coords; (3) **layout dropped 18 notes** — the vault has two `sports-fitness` folders (root + `second-brain/`), and promoting the dominant `second-brain` *overwrote* the root one in the tree; fixed with a recursive `mergeNode` so same-named folders merge (sports-fitness district went 31 → 49 = all notes accounted for, 233/233 buildings).
- **Gotcha learned:** the preview MCP can't reliably screenshot a hi-DPI WebGL canvas — it cornered/clipped the capture. Verified the true render via `gl.readPixels` (98% canvas fill) and exercised all interactions through `preview_eval` instead of trusting screenshots.
- Verified in Electron: WebGL2 context live, 233 buildings, 11 districts, live IPC scan, no renderer errors.
- Added dep: `three@^0.171`. Enabled `preserveDrawingBuffer` so the city is screenshot/exportable.

## Update — same session: moved to Coding/ then reshaped into a BEATING HEART
- Moved the app to `~/Documents/MyVault/Coding/vault-city-app/` (same-volume `mv`, node_modules intact, all paths relative/home-absolute so nothing broke). Deleted the old 2D `vault-city.html` + its `scripts/` template/generator (superseded). Run with `cd ~/Documents/MyVault/Coding/vault-city-app && npm run app`.
- Sri then asked to make it "a beating heart… click something → zoom into that part and show the connections… good graphics." New engine `src/city/heart.js` (`HeartEngine`, OrbitControls), reusing `layout.js` for the model; React shell/reader/search unchanged again. Re-themed UI city→heart: "Vault Heart", cells/vessels/regions, blood-flow toggle, FLATLINE error screen.
- **How the heart is built:** notes = glowing cells rejection-sampled into a 3D puffy heart volume (implicit `(x²+y²−1)³ < x²y³`, z-puffed), clustered by folder via farthest-point seeds + size-ordered nearest-slot assignment (one slot per note so the union FILLS the heart). A 2,600-pt dim-crimson "tissue" particle cloud gives the silhouette its mass. Vessels = link edges; blood-flow = particles travelling each edge; pulsing red core light. Lub-dub beat = group scale envelope (two gaussian bumps/cycle) + emissive throb; reduced-motion disables it.
- **Click a cell → fly in + trace connections:** raycast select flies the camera to the node, lights the node (1.5× emissive, 1.7× scale) + its neighbors + their vessels, and dims every other cell to 16% opacity. Verified on TODO (19 connections). Region labels are clickable to fly to a folder cluster.
- **Tuning that mattered:** first pass was blown out (bloom 0.85 + big emissive cells = white blobs, no heart shape) and farthest-point seeds left gaps. Fixed by filling the heart (slots == note count), adding the tissue body, shrinking cells, and dropping bloom to 0.5/threshold 0.34. Then it read clearly as a valentine heart.
- Verified in Electron: WebGL2 live, 234 cells, 11 regions, no errors. `engine3d.js` (the 3D city) is left on disk unused; `heart.js` is the active engine.
- **Then: anatomical heart (not the valentine symbol).** Sri asked for "the shape of a real heart… like a human heart." Replaced the 2D-heart-curve sampler with a **metaball field** (7 blobs: two ventricles, broad base/atria, side bulges, a low apex blob) rejection-sampled into the body; added an apex taper (squeeze x/z for low y → pointed bent apex), front-to-back flattening (z×0.7), and a slight group tilt (lean). Added the **great vessels** as thin emissive TubeGeometry curves emerging from the base — aorta arch (red), pulmonary trunk + SVC (blue), pulmonary vein — the anatomical signature. Denser tissue (6,200 pts) defines the silhouette; cells shrunk so they read as embedded structures, not a lumpy blob. Two iterations to dial in: first pass was a blown-out diffuse cloud with fat slab-like vessels; fixing = thinner tubes, tighter ISO (1.42), pronounced apex taper, smaller cells, camera pulled back to dist 68. Reads clearly as a human heart now (broad vessel-topped base, bulging body, pointed apex). Click→fly→trace-connections unchanged and re-verified (TODO: 19 neighbors lit, rest dimmed to 16%).

---

## Related Notes
[[memory/conversations/2026-06-10-vault-city-app]]  [[memory/entities/sri]]  [[memory/index|Memory Index]]  [[memory/log|Log]]
