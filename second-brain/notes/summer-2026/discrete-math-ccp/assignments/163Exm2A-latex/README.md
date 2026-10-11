# 163Exm2A — LaTeX replica

Pixel-faithful LaTeX reconstruction of `../163Exm2A.pdf` (Math 163 Exam 2A,
Sri's individually-seeded 2026 exam, 32 pages, folios 400–431, due
2026-08-03). Blank printed pages only so far — no answers yet.

**Not the same page size as Exam 1C/1B**: this exam is US Letter
(612×792bp), not A4 (595.32×841.92bp). Header/footer chrome text also
differs from 1C's ("Due by2359 hours on 20260803" / "163 Exam 2A" /
"You may discuss and work with anyone", vs. 1C's "Due by 2359..." /
"You may discuss with anyone" — note 2A's header genuinely has no space
after "by", reproduced verbatim, not a typo).

## Build

```bash
xelatex main.tex && xelatex main.tex   # two passes (TikZ page anchoring —
                                        # the first pass alone renders BLANK)
```

Output: `main.pdf`, 32 pp.

## Status

- All 32 printed pages generated and verified against the original by
  rendering both to PNG and comparing (spot-checked 404, 402/403, 411, 416,
  426, 430 directly; full build has zero unresolved `TALL-UNKNOWN`
  delimiters and only one remaining glyph gap, below).
- **Known gap:** page 430 is missing the italic "h" (U+210E) in the ordinal
  suffix "n^th" — the extracted `CambriaMath_22.ttf` subset's cmap doesn't
  expose this glyph even though the original PDF paints it. Cosmetic only
  (prose text, not a fillable answer). Same problem class as the 1C
  project's missing-glyph donor-map issue; not yet fixed here.
- No answer layer yet. Problems 1c (formation-trees), 2c (induction of the
  2a/2b conjectures), and 3c (repeating-decimal rational/irrational proofs)
  have **no solved exhibit in either reference PDF** — see
  `../styleguide.md` §8 items 8 and Rules.md's Exam 2A scope section before
  attempting them.

## How it works

Same approach as `163Exm1B-latex/` and `163Exm1C-latex/` — see those
READMEs for the full technique writeup (TikZ page overlay, `\CT`/`\TDEL`/
`\RECT` placement macros, ink-measured tall delimiters). Differences
specific to this build:

- `tools/gen2.py`'s `DELMAP`/`DELCHARS` were extended to route `⌊ ⌋ ⌈ ⌉`
  (floor/ceiling) through the same math-mode `\left/\right` mechanism as
  parens — the plain-text `\CT` path can't reach these glyphs in this
  font's subset. If a future page needs a delimiter still missing from
  `DELMAP`, it'll show up as a `% TALL-UNKNOWN` comment in `pages/*.tex`.
- Fonts extracted fresh from `163Exm2A.pdf` (do not reuse 1C's `fonts/` —
  different subsets, different glyph coverage: 2A needs α, φ, ρ and other
  characters 1C never printed).

## Tools (`tools/`)

Copied from `163Exm1C-latex/tools/` and repointed at `163Exm2A.pdf`/folio
400: `genfonts.py`, `genrules.py`, `gen2.py`, `fixdel.py`, `compare.py`,
`measure.py`. Exam-agnostic DSL/glyph tools copied unchanged: `inklib.py`,
`atoms.py`, `pieces.py`, `stack.py`, `table36.py`, `tree.py`, `expr.py`,
`splitct.py`, `mergefonts.py`, `fixglyph.py` (these last two not yet
needed — no answer layer, no cross-exam glyph donor requirement so far).
