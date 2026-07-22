# Math 163 Exam Style Guide (`styleguide.md`)

This file is the **formatting authority** for producing Math 163 exam submissions,
including the LaTeX replica of `assignments/163Exm1C.pdf` (2026, folios 300–320,
due 2026‑07‑27). It is the companion to `Rules.md` (the mathematical/notational
authority). Division of labor:

- `Rules.md` decides **whether a token or method may be used at all** (content gate).
- This file decides **how every admissible answer is laid out on the page**
  (format gate): position, anchors, bars, boxes, tables, trees, fonts, folios.

## Source exhibits

Formatting is derived from the professor's own solved exams. **Their mathematics
is intentionally unreliable and must never be copied** (see the announcement
"Solved Exams Have Correct Formatting But May Contain Errors — DO NOT COPY
BLINDLY"). Format only.

| Exhibit | File | What it is |
|---|---|---|
| **SOL‑2020** | `exams/163Exam1C-Solutions-2020.pdf` | 2020 Online Exam 1C solved by "Cap'n Orangebeard". 15 pp: printed pages 300, 302, 303, 304, 306, 310, 312, 316, 317 + work sheets 3040, 3060, 3100, 3120, 3160, 3170. |
| **SOL‑2024** | `exams/163Exam1C-Solutions-2024.pdf` | 2024 Summer I Exam 1C solved by "Captain Yellowbeard". 16 pp: printed 300, 302, 303, 304, 306, 310, 312, 316, 317 + work sheets 3040, 3041, 3060, 3100, 3120, 3160, 3170. |
| **EXM‑2026** | `assignments/163Exm1C.pdf` | Sri's blank 2026 Exam 1C. 21 pp, folios 300–320. Question‑for‑question identical to SOL‑2024 (different J‑number data). |

When SOL‑2020 and SOL‑2024 disagree on a formatting detail, **follow SOL‑2024**
(same generation as EXM‑2026). Where a page‑301 printed instruction conflicts
with either sample, the printed instruction wins.

2026 question map (all mirrored in SOL‑2024): p302–303 setup fills · p304 6(1a)
C/P computations · p306 6(1b) ∤ tables · p308 5(1c) direct proof (no sample) ·
p310 6(2a) word trees · p312 6(2b) 4‑digit tree · p314 5(2c) recursive
definition (no sample) · p316 6(3a) binomial/multinomial fills + Y/N/Pf/W ·
p317 6(3b) multinomial sum · p319 5(3c) induction proof (no sample).

---

## 1. Page model

Two page species, both A4 (595×842 pt):

**Printed exam pages** (folios 300–320). Every page keeps its printed frame:
header left `Due by 2359 hours on 20260727`, header right `163 Exam 1C`, footer
left `You may discuss with anyone`, footer right the folio (`300`…`320`).
Body text is justified; question labels sit in the left margin column
(`6 (1a)`, `3 (i)`, `D`, `R`, `E`). Answers are added **only at the printed
anchors** (§3). Nothing else may be written on a printed page — any other mark
is an "extraneous mark" and loses points.

**Work sheets** (inserted after the printed page they serve). Blank pages — no
printed header or footer. Work for a problem on page *n* goes on sheets
foliated `n0, n1, n2, …` **written in the lower right corner inside a small
ruled rectangle** (e.g. `3040`, `3041` after page 304). Both samples draw this
folio box ≈ 3–4 mm high, flush to the corner margins. The printed blank pages
of EXM‑2026 (305, 307, 309, 311, 313, 315, 318, 320) are *not* work sheets —
work sheets are your own blank (not ruled) pages, and per page 301 you may NOT
include pages you have not attempted.

**Page‑301 straight‑line rule** (verbatim scope): every straight‑line segment
other than those in `=, ≠, ≡, <, ≤, >, ≥, +, −, ×, ÷, ¬, ∨, ∧, ∥, ⊥, ∖, →, ↔, ⟼`
must be ruler‑straight. In the LaTeX replica every rule, bar, box, table line,
tree edge and strikethrough is a drawn line, so this is satisfied by
construction; it binds the hand‑written transcription.

## 2. Typography

Match the exam's own embedded fonts (extract from the PDF as in the 1B
pipeline; do not substitute installed lookalikes):

| Role | Font |
|---|---|
| Body text, labels `D/R/E/Q`, prose | Book Antiqua (bold variant for bold runs) |
| All math, printed and answers | Cambria Math, set as **text runs** (Word GPOS kerning; TeX math mode kerns differently) |
| Occasional printed glyphs | SymbolMT, Arial, Times New Roman, Calibri (as they occur) |

**Answers are typeset in the same Cambria Math as the printed math.** The
samples distinguish answers only by being handwritten; the replica reproduces
the *format*, not the pen. Implement every answer through the answer macros
(§7) so a draft switch can tint them for proofreading; final build is black.

Handwriting‑only features of the samples that must NOT be imitated: letter
wobble, freehand circle shapes, pen weight. Everything else — placement,
ordering, bar counts, box tiling — is normative.

## 3. Printed‑page answer anchors

Only these anchor types exist on EXM‑2026, and each has one fill convention:

**A1 — Underline blank.** (p302 `JN … = ______`; p306 `ν(F) = ___`.)
Write the value centered **above the printed underline**, baseline sitting on
the line. The J‑number is written as an unbroken 8‑digit string.

**A2 — Inline `=` blank.** (p303 `s := … =`, `b := … =`; p304 part answers;
p310 `ν(…) =`; p316 coefficient answers; p317 sum value.) Write the result to
the right of the printed `=`, vertically centered on that line. Multi‑row
results (stacked coefficients) centre on the `=` baseline.

**A3 — Inside printed braces `{ }`.** (p302 `SJ = { }`, `MSJ = { }`; p306
`F = { }`, `G = { }`; p310 word lists; p312 `S = { }`.) Elements
comma‑separated, centered in the printed brace box, wrapped into as many rows
as needed (SOL rows hold 8–10 short items; break at commas, keep rows roughly
balanced). Numerical sets/multisets/lists in **increasing order**; pairs in
row‑major table order (§5); multisets as `value:multiplicity` entries ordered
by value (`0:4, 2:1, 4:1, 5:1, 7:1`).

**A4 — Inside printed parens `( )`.** (p302 `Lst(J) = ( )`.) Same as A3 but a
list: parentheses, increasing, comma‑separated.

**A5 — Positional template slots.** (p310 `My {s,b} = { }` and the printed
`Wrd(3, { , }, OM, RA)` argument braces; p316 exponent blanks `x^( ) y^( )`,
`(x+y)^( )`; p317 upper multinomial entry.) Fill each slot with the value of
the symbol printed in that position — SOL‑2024 writes `{ 7, 0 }` for
`{s, b}` with s = 7, b = 0 (positional, **not** re‑sorted; see Flagged
decisions). Exponent slots take numerals on the right‑hand instance and the
symbolic sum on the left‑hand instance exactly as the sample: LHS
`(x+y)^((b+s))`, RHS `x^((0)) y^((7)), (x+y)^((7))`.

**A6 — Y/N/Pf/W row.** (p316 (v), (vi).) Draw an ellipse around the chosen
verdict letter **and** a second ellipse around `Pf` or `W` — two circles per
row (samples: `Y`+`Pf`, `N`+`Pf`). The proof/witness itself lives on the work
sheets.

**A7 — Expected‑grade table.** (p300.) Write the expected points per part in
the matching `Part (i)…(ix)` cell, the per‑question total in `Expected Grade`,
and the sum in the `Total` row. Rows for unattempted questions stay empty.
`Received Grade` column stays empty. Name on the `Name (PLEASE PRINT)` line.

**A8 — On‑page answer areas.** (p308 proof start; p314 `BC` / `RcS` areas;
p319 `BC` / `RcS`.) Begin the display in the whitespace under the printed
label, using work‑sheet grammar (§4–6), continuing onto sheets `3080…`,
`3190…` as needed. p314's answers must fit entirely on the page ("Write your
answers on this page in the areas provided").

## 4. Work‑sheet grammar

The layout language every work sheet follows (both samples, all pages):

**Piece.** One rectangular region containing one displayed derivation, table,
or tree. Pieces tile the sheet left→right, top→bottom, and are separated by
**ruler‑straight lines parallel to the paper edges** (full‑width horizontal
rules between stacked pieces; vertical rules between side‑by‑side pieces —
SOL‑2024 3160 tiles up to 4 pieces across).

**Piece label.** Small rectangle at the piece's top‑left corner containing the
index: `<question‑part>[.<roman>][.<counter>]` — e.g. `1a.i.0`, `1a.ii`,
`1b.i`, `2b.0`, `3a.v.2`, `3b.1`. Rules:
- `<question‑part>` is the printed part label (`1a`, `1b`, `2a`, `3b` …).
- `.<roman>` = the printed sub‑part `(i), (ii)…` when one exists.
- `.<counter>` = 0‑based order of completion **within that sub‑part** when it
  needs more than one piece; a sub‑part answered in a single piece carries no
  counter (`1a.ii`); a preliminary piece shared by all sub‑parts carries the
  bare part label (`2a`, `3a`).
- Counters record the order the pieces were completed (page‑303 R rule).

**Sheet capacity.** Fill a sheet before opening the next (`3040` → `3041`).
A piece is never split across sheets; an oversized piece (big tree) gets its
own sheet.

## 5. Display formats

### 5.1 Chained equalities

The workhorse. First line: the bare expression, indented right of the `=`
column. Every subsequent line starts with `=` and **all `=` signs align
vertically on the left** (page‑301 instruction; both samples comply).

```
   C(C(ν(St(J)), ν(St(J))), P(ν(MltSt(J)), ν(MltSt(J))))
=  C(1, ((ν(MltSt(J)))!))
=  C(1, 8!)
=  (1 over (8!))                      [stacked coefficient, §5.5]
```

- **Parenthesization is preserved verbatim** through the chain — samples write
  `((ν(MltSt(J)))!)`, `(((ν(MltSt(J))) − (ν(St(J))))!)`, `(8−5)!`, `(3!)`,
  `(5!)`; nothing is silently de‑parenthesized.
- Substituted numerals keep the surrounding structure (`x^(7−7) y^7` before
  becoming the coefficient).
- Chains stop at the form the samples stop at: counting answers `ν(…)` end in
  a numeral; coefficient/sum computations end in grouped factorial
  expressions (`3!`, `(4!)/(3!)`, `2+(3!)+(2)((4!)/(3!))`) — **not** decimal
  evaluations.

### 5.2 Substitution into a general formula (⟨ ⟵ ⟩ witness)

Instantiating a notes formula is displayed as a **single‑bar inference**: the
general formula above a ruler‑straight horizontal bar, the instantiated
statement below, and the substitution witness in large angle brackets to the
right of the bar, one assignment per stacked line, `var ⟵ expression`:

```
 C(n, n) = 1
──────────────────────────────  ⟨ n ⟵ ν(St(J)) ⟩
 C(ν(St(J)), ν(St(J))) = 1
```

```
 P(n, m) = (n!)/((n−m)!)
─────────────────────────────────────────────────────────────  ⟨ n ⟵ ν(MltSt(J))
 P(ν(MltSt(J)), ν(St(J))) = ((ν(MltSt(J)))!)/(((ν(MltSt(J)))−(ν(St(J))))!)      m ⟵ ν(St(J)) ⟩
```

- Bar spans the wider of premise/conclusion. Angle brackets are tall chevrons
  embracing the whole assignment stack.
- Inside an equality chain, the general formula is applied inline as
  `(GeneralFormula(…)) ⟨subs⟩` — the formula in parentheses followed by the
  witness — then the next `=` line shows the result:

```
=  (BnmlCfn(a^(n−k) b^k, (a+b)^n)) ⟨ n ⟵ 7, k ⟵ 7, a ⟵ x, b ⟵ y ⟩
=  ((n over k)) ⟨ n ⟵ 7, k ⟵ 7 ⟩
=  (7 over 7)
```

- After the full witness has appeared once, a later line may carry the
  **ditto witness** `⟨ " ⟩` ("same substitutions") or a reduced explicit list
  (samples use both).
- Multi‑step numeric rewrites may stack bars directly (SOL‑2024 3160 piece
  `3a`): premises `s=7  b=0  k=s  n−k=b` over a bar, then `n−s=b` / bar /
  `n=b+s` / bar / `n=0+7` / bar / `n=7`. Side‑by‑side premises on one level
  are implicitly conjoined (Rules.md). A bar may carry its own witness
  (`⟨(p+q) ⟵ 4⟩` on the step that uses the constraint).

### 5.3 "Does not make sense" answers

When an expression is undefined (`k ∉ 0..n` in `(n over k)`, empty `mxm`/
`mnm`, …), the verdict is the prose **does not make sense** — printed page 301
authorizes it.

- **Answer line (A2):** `= (1 over (8!)) does not make sense` — expression
  first, prose after it, same line.
- **Work sheet:** a single‑bar inference whose conclusion is the verdict.
  SOL‑2024 (piece `1a.i.3`) writes the reason after the mark `∵`:
  `(1 over (8!)) does not make sense ∵ (8!) ∉ 0..1`. **`∵` is prohibited by
  Rules.md** (owner rule outranks the sample). Compliant layout — put the
  membership fact beside the domain premise above the bar:

```
 ∀n∈ℕ ∀k∈0..n (n over k)      (8!) ∉ 0..1
──────────────────────────────────────────
 (1 over (8!)) does not make sense
```

### 5.4 Long sums (stacked terms)

A sum too long for one line is stacked (SOL 3b.2, both years): the first `=`
line holds the first term; each following term goes on its own row prefixed
`+`, aligned under the first term; a **vertical ruler line drawn under the `=`
sign** spans the stacked rows, tying the stack to that single step. Parallel
stacks (coefficients | values) sit side by side, each with its own vertical
rule; the final collected expression closes the chain on the top row:

```
=  ( 4          │  =  1              =  2+(3!)+(2)((4!)/(3!))
   ( 0 0 4 )    │
+  ( 4          │  +  (4!)/(3!)
   ( 0 1 3 )    │
+  ( 4          │  +  3!
   ( 0 2 2 )    │      …
```

### 5.5 Binomial / multinomial coefficients

Tall‑paren stacks, **no fraction bar**:
- Binomial: `n` above `k` inside one paren pair — `(7 over 7)`.
- Multinomial: `n` centered on top, bottom row entries side by side —
  `(7 ; 0 7)` renders as top `7`, bottom `0  7`.
- Entries may themselves be parenthesized expressions:
  `((8!)/(3!)  over  (5!))` (SOL‑2024 p304 answer to 2(ii)).
- Factorial expansions keep every factor parenthesized and follow the notes'
  shapes: `(n over k) = (n!)/((k!)((n−k)!))`,
  `(n ; n₁ n₂) = (n!)/((n₁!)(n₂!))`.
- Symmetry rewrites are one `=` step re‑ordering the bottom row:
  `(4 ; 0 0 4) = (4 ; 0 4 0)`.
- **Cancellation** in factorial quotients is shown by striking through the
  cancelled factors with straight lines (SOL 3b pieces:
  `((4̶)(3)(2))/((1)(2̶)(2̶)) = 3!`). Strikethroughs are drawn rules.

### 5.6 Verification pieces (Y/N/Pf/W support)

The p316 (v)/(vi) circles are backed on the work sheets by:
- one piece per coefficient expanding it to factorials (pieces `3a.v.0`,
  `3a.v.1`, `3a.v.2`), each ending in the common value;
- a chain piece equating all forms (`3a.v.3`:
  `(7 over 7) = (7 over 0) = (7;0 7) = (7;7 0)`);
- the symbolic (data‑independent) versions with `b`, `s`, `b+s` for (vi)
  (pieces `3a.vi.0`–`3a.vi.3`).

## 6. Structured displays

### 6.1 Table method (p306, 1b)

Piece layout, top to bottom (SOL `1b.i` / `1b.ii`):
1. Restated definition line: `F := {(x,y) ∈ (St(J))×(St(J)) | x∤y}`.
2. The table. Corner cell `(x,y)`; column heads = y‑values increasing
   left→right; row heads = x‑values increasing top→bottom; **one vertical
   rule** after the row‑head column and **one horizontal rule** under the
   header row (no other grid lines). Every cell holds its pair `(x,y)`.
3. Qualifying cells get an **ellipse drawn around the pair** (circle the
   member pairs, nothing on the failures).
4. A **full‑width horizontal conclusion bar** under the table.
5. The result: `F = { … }` listing exactly the circled pairs,
   **row‑major order** (the order the table generates them), wrapped in
   balanced rows inside hand/drawn braces.

The printed page 306 then receives only the final set (A3) and `ν(F)` (A1/A2).

### 6.2 Trees (p310 2a, p312 2b)

Grammar (all four sample trees):
- Title `Tree` at the piece's top‑left, **double‑underlined**.
- Root at top center: one dash per slot (3‑letter word → `— — —`;
  4‑digit → `— — — —`).
- Every internal node = chosen prefix followed by one dash per unfilled slot
  (`0 _ _`, `70 _`, `20 _ _`, `457 _`). Leaves = complete strings, no dashes.
- Children ordered by chosen symbol, **increasing left→right**; edges are
  plain straight lines (drawn with ruler); no node circles or boxes.
- **Dead branches stay visible**: a node whose continuations are all
  disallowed is drawn with no children (SOL‑2024 2b: `0 _ _ _` dead at level
  1; `205_`, `207_`, `445_`, `447_` … dead at level 3).
- Constraint filtering happens at the level where it bites; only strings
  satisfying every constraint become leaves.
- Wide trees tile the sheet: subtrees are staggered into tiers (SOL‑2024
  `3120` spreads five level‑1 subtrees across the full page; SOL‑2020 routes
  the root's middle child down to a second tier). Keep each subtree internally
  ordered; tier placement is free.
- The listing is a **separate piece** (`2b.1`): `S = { … }` increasing,
  wrapped rows; count piece/blank per the printed question. Words are digit
  juxtapositions (`707`, `4574`) — no separators.

### 6.3 Proof questions (1c p308, 2c p314, 3c p319) — no sample exists

Both sample solvers skipped 1c/2c/3c (expected‑grade rows empty, totals 36).
Formats must come from the notes, under Rules.md's bar‑proof syntax:

- **2c (recursive definition):** fill the printed `BC` and `RcS` areas on
  p314 with the base case and recursive step in the notes' recursion format
  (Induction and Recursion Notes; recursive specifications also appear in
  Sets Notes appendix pp. 31–36). Five‑part function form per Rules.md if a
  function is (re)specified.
- **1c (direct proof) / 3c (induction proof):** begin on the printed page
  (A8), continue on `3080…` / `3190…` sheets in piece grammar; single/double
  bars per Rules.md Proof Syntax; `SPf`/`EPf` delimiters if the notes'
  examples use them; 3c's printed `BC`/`RcS` labels index the two proof
  obligations.
- **Flag before finalizing:** exact base‑case/step layout, induction‑
  hypothesis display, and divisibility‑proof steps must be matched against
  Induction and Recursion Notes pages before the PDF is produced
  (Rules.md conservative decision test). Do not improvise.

## 7. LaTeX implementation

Extends the Exam 1B replica pipeline
(`assignments/163Exm1B-latex/`, see its README; build `xelatex ×2`).

**Reuse unchanged:** fonts extracted from the source PDF (same families in
EXM‑2026: Book Antiqua, Book Antiqua Bold, Cambria Math, SymbolMT, Arial,
Calibri, Times New Roman); TikZ page overlay with coordinates in bp from the
page's top‑left; macros `\TL` (baseline text line), `\JL` (justified line),
`\CT` (Cambria text‑mode math run), `\TDEL` (ink‑measured tall delimiter),
`\RECT` (rules/underlines/strikethroughs); `gen2.py` to regenerate printed
pages from `163Exm1C.pdf`; `fixdel.py → xelatex ×2` iteration for tall
parens; `compare.py`/`measure.py` for verification.

**Answer layer — add:**

| Macro (proposed) | Renders |
|---|---|
| `\ANS{x}{y}{size}{…}` | answer run in Cambria at a printed anchor; draft‑mode tint switch |
| `\ANSU{x}{y}{w}{…}` | answer centered above a printed underline of width `w` |
| `\PIECE{x0}{y0}{x1}{y1}` | piece separation rules (ruler lines) |
| `\PLBL{x}{y}{1a.i.0}` | piece‑label rectangle, top‑left |
| `\FOLIO{3040}` | work‑sheet folio box, lower right |
| `\INFBAR{x}{y}{w}` + stacked `\CT` rows | single‑bar inference; width = max(premise, conclusion) |
| `\SUBS{x}{y}{h}{rows}` | tall‑chevron substitution witness `⟨ … ⟵ … ⟩`, one assignment per row; `⟨"⟩` ditto variant |
| `\CIRCLE{cx}{cy}{rx}{ry}` | ellipse around a printed/typeset token (Y/N/Pf/W, table pairs) |
| `\BINOM` / `\MLTNOM` | stacked coefficient in tall parens (size via `\TDEL` ink measurement — Word reports assembled parens at nominal size) |
| `\STRIKE{x0}{y0}{x1}{y1}` | cancellation stroke (thin `\RECT`) |
| tree/table pieces | TikZ straight‑segment edges + `\CT` node labels; table rules via `\RECT` |

**Work sheets** are generated pages (no scan underlay): plain A4, pieces laid
out in the §4 grammar, folio box via `\FOLIO`. Compose them after the answers
are fixed; verify geometry with `compare.py` against nothing (they have no
original) but keep margins ≥ the printed pages' text block.

**Known gotchas** (from the 1B build, still apply): Cambria math must be
placed as text runs, not TeX math mode; `unicode-math` maps `:` to U+2236 —
use a text colon inside `:=`/`:⟺` reproductions; measure tall delimiters by
painted ink, never by reported font size; two xelatex passes for TikZ page
anchoring.

## 8. Flagged decisions (owner sign‑off)

1. **`∵` on work sheets.** SOL‑2024 uses `∵` once (piece `1a.i.3`). Rules.md
   prohibits `∵`/`∴`. Default here: the two‑premise bar of §5.3. Change only
   by editing Rules.md first.
2. **`My {s,b}` fill order.** SOL‑2024 writes `{ 7, 0 }` positionally
   (s‑slot, b‑slot) even though the increasing‑order R‑rule would give
   `{0, 7}`. Default: follow the sample (positional) for A5 template fills;
   all *other* set listings stay increasing. If Sri prefers the conservative
   reading, sort — and accept divergence from the sample.
3. **General‑formula names.** SOL‑2020 appears to write `BnmlCfnt`/
   `MltnmlCfnt` (trailing *t*) for the general formulas; SOL‑2024 writes
   `BnmlCfn`/`MltnmlCfn` for both general and applied forms. Verify the exact
   names printed in Binomial Theorem Notes before use; default to SOL‑2024.
4. **Proof layouts for 1c/2c/3c** have no solved exhibit — must be matched
   to Induction and Recursion Notes pages before the final PDF (§6.3).
5. **2026 data edge cases** to anticipate at solve time: `s := mxm{k∈1..8|Jk=0}`
   and `b := mnm{Jk∈0..9|Evn(Jk)}` are undefined for some J‑numbers ("does
   not make sense" answers, §5.3, ripple into 2a/3a); if `s = b`, the p310
   alphabet `{s,b}` collapses to one letter and the trees narrow accordingly.

## 9. Format‑gate checklist (run before shipping any page)

- Every answer sits at a printed anchor (A1–A8) or inside a work‑sheet piece.
- Every piece has its label box; counters 0‑based, order‑of‑completion.
- Work‑sheet folios `n0, n1, …` boxed lower right; sheets appear after their
  printed page; no unattempted pages included.
- All `=`/`⟺` signs aligned vertically on the left; first chain line bare.
- Bars: single vs double per Rules.md; no `∴ ∵ ⟹ ⟺` between proof rows;
  substitution witnesses in `⟨ ⟵ ⟩` chevrons.
- Sets/lists/multisets increasing (except A5 positional template fills);
  pairs in table row‑major order; no repeated elements.
- Coefficients as tall‑paren stacks, no fraction‑bar binomials; factorials
  parenthesized exactly as the samples.
- Tables: two rules + circled qualifiers + conclusion bar + listed set.
- Trees: double‑underlined `Tree` title, slot dashes, increasing children,
  dead branches visible, separate listing piece.
- Y/N/Pf/W rows carry exactly two ellipses (verdict + Pf/W).
- Empty set would be `{ }`; `ν` for cardinality; every token passed the
  Rules.md content gate.
