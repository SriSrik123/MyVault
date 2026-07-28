---
title: 163Exm1B PDF to LaTeX pixel replica
last_updated: 2026-07-20
type: conversation
source: claude-code
---

# 2026-07-20 — 163Exm1B PDF to LaTeX pixel replica

## What Happened
Sri asked for `163Exm1B.pdf` (Math 163 Exam 1B, discrete-math-ccp, 30 pages) to be converted to LaTeX with the exact same layout — same line positions, no visible difference — and reviewed multiple times. Claude built an automated pipeline: extracted the embedded fonts (Book Antiqua, Cambria Math, Calibri, Symbol) from the PDF itself, generated a per-page TikZ overlay placing every text line, math run, table rule, and tall delimiter at its measured coordinate, and compiled with XeLaTeX. Seven measure-and-fix review cycles (pixel overlay diffs + character-level position reports + an ink-measuring feedback loop for delimiter sizes) brought every page to sub-point alignment. Deliverable: `notes/summer-2026/discrete-math-ccp/assignments/163Exm1B-latex/` with `main.tex`, per-page sources, fonts, the reusable tools, a README, and the compiled `163Exm1B-latex.pdf`.

## Key Decisions Made
- Use the fonts embedded in the PDF (extracted via PyMuPDF) instead of substitutes — Book Antiqua/Cambria Math aren't installed on Sri's Mac; this makes glyphs match exactly.
- Place content by measured coordinates (TikZ overlay in bp) rather than reflowing — the only way to guarantee "lines in the exact same places."
- Set linear math as Cambria *text* runs, not TeX math: Word shapes math runs with GPOS kerning that TeX math mode ignores; this eliminated a whole class of ~2–3bp drifts.
- Detect and size tall parens/braces by rendering and measuring painted ink — PDF metadata reports Word's stretched delimiters at nominal size, so metadata-based detection is blind.
- Keep prose lines as justified blocks (readable .tex) but math rows word/segment-anchored (exactness where it matters).

## Facts Learned About Sri
- Sri is taking a discrete math course (Math 163) at CCP in Summer 2026 II; Exam 1B was due 2026-07-20 23:59.
- His J-number appears on the exam header as annotations ("Srinarayan Srikanth" — his full name).
- The course folder also holds `163Exm1A.pdf` — the same conversion may be wanted for it.

## Tasks / Action Items Resulting
- None for Sri. If he wants Exam 1A converted, re-run `tools/gen2.py` (per the folder README) against that PDF.

## Follow-Up Questions / Gaps
- Residual differences are sub-point: delimiter curve shapes (TeX size variants vs Word's two-piece assemblies) and justified-line space distribution — visually indistinguishable at print size, but not literally identical rasters.

---

## Related Notes
[[memory/entities/sri]]  [[memory/SCHEMA|Schema]]  [[memory/index|Memory Index]]  [[memory/log|Log]]
