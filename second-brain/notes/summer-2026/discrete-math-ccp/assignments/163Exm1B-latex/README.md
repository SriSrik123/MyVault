# 163Exm1B — LaTeX replica

Pixel-faithful LaTeX reconstruction of `../163Exm1B.pdf` (Math 163 Exam 1B,
30 pages, folios 200–229).

## Build

```bash
xelatex main.tex && xelatex main.tex   # two passes (TikZ page anchoring)
```

Output: `main.pdf` (kept here as `163Exm1B-latex.pdf`).

## How it works

- **Fonts** in `fonts/` were extracted from the original PDF (Book Antiqua
  regular/bold, Cambria Math, Calibri, Symbol), so glyphs match exactly.
  `CambriaMath_nokern.ttf` is the math font with its MATH cut-in kern table
  nulled (closer to Word's layout).
- Every page is a TikZ overlay; coordinates are in **bp from the page's
  top-left corner**, taken from the original PDF.
  - `\TL{x}{y}{...}` text line anchored at its baseline
  - `\JL{x}{y}{w}{...}` justified line stretched to the original ink width
  - `\CT{x}{y}{size}{...}` Cambria run set in text mode (matches Word's
    GPOS kerning, which TeX math mode would not apply)
  - `\TDEL{x}{y}{size}{h}{d}{delim}` tall delimiter forced to the measured
    ink height of the original
  - `\RECT{x0}{y0}{x1}{y1}` table rules / underlines / strikethroughs
    (auto-extracted, `pages/rulesNNN.tex`)
- Word draws tall parens as size variants and 2-piece assemblies that PDF
  metadata reports at nominal size, so the generator measures the **painted
  ink** to size them (`tools/inklib.py`).

## Tools (`tools/`)

Regeneration pipeline used to produce and verify the pages (needs
`pip install pymupdf pillow` and the original PDF path inside each script):

- `gen2.py` — regenerates `pages/pageNNN.tex` from the original PDF
- `fixdel.py` — feedback pass: compares rendered vs original delimiter ink
  and rewrites `\TDEL` anchors/sizes; run `fixdel → xelatex ×2` a few times
- `compare.py N…` — renders side-by-side + overlay diffs into `cmp/`
- `measure.py N…` — char-level position diff report

The same pipeline can convert other exams in this format (e.g. 163Exm1A).
