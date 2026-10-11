# Math 163 Exam Style Guide (`styleguide.md`)

This file is the **formatting authority** for producing Math 163 exam submissions,
including the LaTeX replica of `assignments/163Exm1C.pdf` (2026, folios 300–320,
due 2026‑07‑27). It is the companion to `Rules.md` (the mathematical/notational
authority). Division of labor:

- `Rules.md` decides **whether a token or method may be used at all** (content gate).
- This file decides **how every admissible answer is laid out on the page**
  (format gate): position, anchors, bars, boxes, tables, trees, fonts, folios.

## Scope

Covers two exams:
- **Exam 1C** — replica of `assignments/163Exm1C.pdf`, folios 300–320, due 2026‑07‑27. **Submitted 2026‑07‑27.**
- **Exam 2A** — replica of `assignments/163Exm2A.pdf`, folios 400–431, due 2026‑08‑03. **In progress.**

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

| **SOL2A‑2020** | `exams/163Exam2A-Solutions-2020.pdf` | 2020 Online Exam 2A solved by "Cap'n Orangebeard" (19 pp). Printed + work‑sheet pages for 1a, 1b, 2a, 2b, 3a, 3b only — **1c/2c/3c don't exist in this exhibit** (its own grade table stops at 3b, total 36). |
| **SOL2A‑2024** | `exams/163Exam2A-Solutions-2024.pdf` | 2024 Summer I Exam 2A solved by "Captain Yellowbeard" (20 pp). Same six‑problem coverage as SOL2A‑2020. |
| **EXM2A‑2026** | `assignments/163Exm2A.pdf` | Sri's blank 2026 Exam 2A. 32 pp, folios 400–431. **Not** question‑for‑question identical to either SOL2A sample — adds three problems with **no solved sample in either exhibit**: 1c (folios 411–415, set‑cardinality formation‑trees, 5 pts), 2c (folio 421, induction‑proves the (2a)/(2b) conjectures, 5 pts), 3c (folios 428 + 430, split 3c1/3c2, repeating‑decimal rational/irrational proofs, 5 pts). Where 1a/1b/2a/2b/3a/3b overlap the samples, EXM2A‑2026's problem text matches SOL2A‑2024 — confirmed directly for 3b (formula `(abcd)^(1/(abcd+1))` matches 2024's wording, not 2020's differently‑worded `(a+b+1)^(1/(a+b+2))`). Total 51 pts (36+5+5+5), same total as Exam 1C. |

When a 2020 and a 2024 exhibit disagree on a formatting detail, **follow the
2024 exhibit** (same generation as EXM‑2026/EXM2A‑2026, and for 2A also
textually confirmed closer to Sri's own exam — see Flagged decisions #9).
Where a printed instruction on the current exam page conflicts with either
sample, the printed instruction wins.

2026 question map (all mirrored in SOL‑2024): p302–303 setup fills · p304 6(1a)
C/P computations · p306 6(1b) ∤ tables · p308 5(1c) direct proof (no sample) ·
p310 6(2a) word trees · p312 6(2b) 4‑digit tree · p314 5(2c) recursive
definition (no sample) · p316 6(3a) binomial/multinomial fills + Y/N/Pf/W ·
p317 6(3b) multinomial sum · p319 5(3c) induction proof (no sample).

2A question map (2026 folios; 1a/1b/2a/2b/3a/3b mirrored in SOL2A‑2024;
1c/2c/3c have no sample): p400 grade table · p402–403 a/b/c/d setup fills
(`c` a floor value, §5.7; `d` a prose‑defined value, §5.8) plus the exam‑wide
R‑rules incl. the (1a)‑only polynomial‑format rule (Rules.md) · p404–406
6(1a) binomial + multinomial "My problem:" expansions (A9) · p407–410 6(1b)
second‑order recurrence solves ×2, distinct‑ and repeated‑root cases (§6.4)
· p411–415 5(1c) set‑cardinality formation‑trees (**no sample**) · p416–417
6(2a) coupled α(n)/φ(n) recurrence + conjecture (§6.5) · p418–420 6(2b)
geometric‑sum conjecture `Sm(α,n)`/`Sm(φ,n)` (§6.5, exam‑supplied name) ·
p421 5(2c) induction proof of the (2a)/(2b) conjectures (**no sample**) ·
p424–425 6(3a) third recurrence + conjecture + induction proof (§6.4
pattern) · p426–427 6(3b) irrationality proof, `Rtl` predicate (§6.6) · p428
2(3c1) repeating‑decimal rationality proof (**no sample**) · p430 3(3c2)
repeating‑decimal irrationality proof (**no sample**).

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

**A9 — "My problem:"/"My expression:" full‑equation substitution.** (2A
p404–410, p416, p418, p424, p426.) The exam reprints the entire general
expression a second time with every parameter position blanked to `(  )`.
Fill each blank with that parameter's numeral (not re‑simplified), matching
the printed paren size; a following `=` line, still on the printed page,
gives the fully substituted/simplified form. A "My problem:" block can
appear twice for one question (e.g. p407: once with `(b+c)`/`(bc)` replaced
positionally, once collapsed to signed coefficients ready for the
characteristic equation).

**A10 — Labeled result blank.** (2A p407/p410/p424/p426 `My solution:`;
p410/p420 `My Conjectures:`; p424 `2(i) Conjecture:`.) A printed prose label
followed by whitespace (sometimes with `∀n∈ℕ` already printed above it);
write only the final closed‑form result there, no derivation — derivation
lives on the work sheets. Distinguish from A8: A10's label names the
*answer* ("solution", "conjecture"); A8's label names a *proof role* (`BC`,
`RcS`).

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

### 5.7 Floor‑valued definitions (halfway decomposition)

(2A p402/p403 `c := ⌊(b+a)/2⌋`.) Both SOL2A samples show the same four‑step
chain inside the floor brackets, never jumping straight to the integer:

```
c := ⌊(b+a)/2⌋ = ⌊(4+1)/2⌋ = ⌊5/2⌋ = ⌊(2)+(1/2)⌋ = 2
```

Steps: (1) substitute the parameters; (2) collapse the sum inside the
brackets to one fraction; (3) re‑express that fraction as
`⌊(integer)+(proper fraction)⌋` — the floor brackets stay drawn around the
whole sum, not just the fraction; (4) drop the brackets and the fractional
part, leaving the bare integer. Do not skip step 3 — both samples keep it
even though it adds no new information; it is the format, not an optional
simplification.

### 5.8 Prose‑defined values

(2A p402/p403 `d := the smallest odd number strictly greater than c`.) When
the exam defines a value by an English condition rather than set‑builder
notation, the answer is a bare A2 numeral after the printed `=` — neither
sample introduces a set‑builder translation (e.g. `mnm{x∈ℕ|Odd(x)∧x>c}`).
No work sheet is used for these single‑step definitions in either sample.

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

### 6.4 Second‑order linear recurrence solve (2A p407–410, p424–425)

Both SOL2A years solve this identically. Piece sequence:

1. **Monic rewrite** — single‑bar inference isolating `(1)(ρ(n+2))` (dividing
   a `(a²)(...)`‑style leading coefficient down to `1`): premise is the
   printed recurrence, conclusion is the coefficient‑1 form.
2. **Characteristic equation** — `(1)x²+(coef)x+(coef)=0`, factored,
   `∨`‑split into two root equations, each bar‑concluding `x=r`. Distinct
   roots: state `r₁≠r₂`, general solution `∀n∈ℕ ρ(n)=k₁(r₁)ⁿ+k₂(r₂)ⁿ`.
   Repeated root: state `r₁=r₂`, general solution
   `∀n∈ℕ ρ(n)=k₁(r)ⁿ+k₂(n(r)ⁿ)` — the second term carries an extra `n`.
3. **Initial‑condition substitution** — one bar‑inference piece per given
   value (`ρ(0):=…`, `ρ(1):=…`), each a `⟨n←0⟩`/`⟨n←1⟩` witness collapsing
   the general solution to a linear equation in `k₁,k₂`.
4. **System solve** — plain boxed algebra, *not* a bar‑inference: stack the
   two equations, eliminate one variable (divide‑both‑sides annotated
   directly under the division line, e.g. `÷2  ÷2`), back‑substitute, box
   the final `k₁=`/`k₂=` pair.
5. **Repeated‑root case only — verification piece.** After solving for
   `k₁,k₂`, both samples add a piece proving the closed form satisfies the
   recurrence: boxed `BC`/`BC` checks of `ρ(0)`, `ρ(1)` against the closed
   form, then an `RcS` piece substituting the closed form into the
   recurrence algebraically to confirm it collapses to `ρ(n+2)`. **This is
   direct algebraic substitution, not a `SPf…EPf` induction stack** — do not
   conflate with §6.3's induction‑proof grammar.
6. **On the printed page (A10):** `My solution: ρ(n) = …` gets the fully
   expanded closed form only, no derivation.

### 6.5 Coupled recurrence, parity closed form, geometric‑sum conjecture (2A p416–420)

The exam defines `α(n)` and `φ(n)` by mutual recursion (each references the
other's previous term). Both samples:

1. Unroll 4–5 terms of each sequence side by side, numeric.
2. Spot the pattern with a **vertically‑dashed ellipsis** under two aligned
   columns (three stacked dots directly under each other, one column per
   sequence — not a single centered `⋮`).
3. Build the closed form using a **parity selector**
   `((1+(−1)ⁿ)/2)` (evaluates to 1 when n is even, 0 when odd) to fold the
   even/odd base case into one formula, combined with `⌊n/2⌋` in the
   exponent and the **geometric partial‑sum shorthand**
   `Sm(base,n) := Σ_{k=0}^{n} baseᵏ = (base^(n+1)−1)/(base−1)` — this name
   is supplied by the exam's own printed p418 definition
   (`Sm(α,n):=S(α,n):=Σ_{k=0}^n α(k)`), so it is licensed **only** for 2b's
   two conjectures, not as general‑purpose notation elsewhere (Flagged
   decisions #10).
4. **Verification pieces** — two boxed pieces side by side, one per parity:
   `∀p∈ℕ(Evn(p)) ⟨n←p⟩ …` and `∀q∈ℕ(Odd(q)) ⟨n←q⟩ …`, each substituting the
   closed form back into itself under that parity and reducing to the
   unrolled base value. Same "direct substitution, not induction" caution
   as §6.4 step 5.
5. 2b's conjecture derivation additionally needs the geometric‑series closed
   form for `Sm` itself as an intermediate lemma piece (shown once, then
   cited by the `⟨"⟩` ditto witness, §5.2).

### 6.6 Irrationality/rationality proof (`Rtl`) (2A p426–427, p428, p430)

`Rtl` is a predicate meaning **"is rational"**; struck through (`R̶t̶l̶`) it
means **"is irrational"** — the same strikethrough‑negates‑the‑label
convention already used for `OM`/`RA` (Rules.md Authorized Abbreviations).
Confirmed directly from EXM2A‑2026's own gloss text (p428 "Prove that
`Rtl(x)`, that is, **x is rational**"; p430 "Prove that `R̶t̶l̶(y)`, that is,
**y is irrational**") — this ranks above the solved exhibits per Rules.md
Source Precedence. Proof shape (p426 and p430, same skeleton, contradiction
style):

1. `SPf`, hypothesis = negation of the goal, over a bar.
2. Unfold `Rtl(expr)` to `∃!p,q∈ℕ((gcd(p,q)=1)∧(expr=p/q))` — one bar step.
3. Raise both sides to the outer root's power, clear denominators, arrive at
   `(base)qᵏ = pᵏ`.
4. Prime‑divides step: a `prm(prime)` premise beside `prime|pᵏ` over a bar
   concludes `prime|p`, then `∃!r∈ℕ(p=prime·r)`; substitute back, simplify,
   repeat symmetrically for `q`.
5. Conclude `prime|(gcd(p,q))` against the premise `gcd(p,q)=1`, bar to
   `prime|1`, bar to `⊥` (the contradiction glyph, not a word).
6. Double‑negation close: `¬(¬(Rtl(expr)))` over a bar to `Rtl(expr)`, `EPf`.

**Flag before finalizing:** the exam instruction says "following the method
shown in class" — the proof *method* (not just the `Rtl` symbol) must still
be matched against Induction and Recursion Notes / Counting Notes before
p426/p428/p430 are produced; the samples fix the visual template but are not
themselves a content authority (Rules.md).

## 7. LaTeX implementation

Extends the Exam 1B replica pipeline
(`assignments/163Exm1B-latex/`, see its README; build `xelatex ×2`) and, for
the answer layer, the Exam 1C build (`assignments/163Exm1C-latex/`). For
Exam 2A, `gen2.py`'s `SRC` points at `assignments/163Exm2A.pdf`; deliverable
folder is `assignments/163Exm2A-latex/` (not yet created).

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
| `\MYBLANK{x}{y}{w}` | A9 "My problem:" per‑parameter blank inside a printed paren, sized `w` |
| `\SYS{x}{y}{rows}` | boxed system‑solve algebra (§6.4 step 4) — plain stacked `=` lines with divide‑annotations, not a bar‑inference |
| `\PARBOX{x}{y}{w}{h}` | side‑by‑side parity‑verification piece box (§6.5 step 4) |

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

1. **`∵` on work sheets — RESOLVED.** SOL‑2024 uses `∵` once (piece
   `1a.i.3`). Rules.md prohibits `∵`/`∴` outright (owner rule outranks the
   sample per Source Precedence). Used: the two‑premise single‑bar of §5.3
   (`∀n∈ℕ∀k∈0..n (n choose k)` and `(8!)∉0..1` side by side over one bar,
   `∉` drawn as `∈` with a manual slash — the font subset lacks a single
   `∉` glyph, see `tools/atoms.py: notin()`).
2. **`My {s,b}` fill order — CONFIRMED by Sri (2026‑07‑25): positional.**
   Follow the sample (`{s‑value, b‑value}`, not re‑sorted) for the one A5
   template slot on p310; all *other* set/list answers stay increasing.
3. **General‑formula names — RESOLVED, both guesses were wrong.** Binomial
   Theorem Notes (p.1) and Multinomial Theorem Notes (p.5) name the
   coefficient‑extraction function `𝐶𝑓𝑐𝑛𝑡` (**Cfcnt**) for *both* the
   binomial and multinomial case — neither `BnmlCfn`, `BnmlCfnt`,
   `MltnmlCfn`, nor `MltnmlCfnt` appears anywhere in the notes. However,
   **EXM‑2026 p316 itself already prints `BnmlCfn(...)` / `MltnmlCfn(...)`
   literally** in the problem statement (Rules.md: an exam‑supplied name
   "may be repeated and instantiated" for that question). Net effect: fill
   the blanks *inside* the already‑printed `BnmlCfn`/`MltnmlCfn(...)` calls
   on p316/317 and their work sheets — do not touch the printed function
   name, and do not introduce `Cfcnt` anywhere on this exam (it is not
   printed on EXM‑2026, so citing it would import an unauthorized synonym).
4. **`C(n,k)` / `P(n,k)` for `k>n` — RESOLVED via exam page, not notes.**
   Counting Notes (pp.9‑10) explicitly declines to pick a convention ("We
   shall not discuss the choice of 0 at this stage"). `EXM‑2026` p301
   itself prints "Remember that 'does not make sense' is a possible
   answer" — a literal page‑301 instruction outranks the notes (Source
   Precedence #2 > #3), so "does not make sense" is licensed independent of
   SOL‑2024 happening to use it too (confirmed independently correct, not
   copied).
5. **OM/RA strikethrough — CONFIRMED visually (SOL‑2024 sheet 3100,
   pieces `2a.i.1`/`2a.ii.1`).** The Counting Notes' `Wrd(n,Alphabet,OM,RA)`
   summary table prints literal duplicate labels ("OM"/"OM", "RA"/"RA")
   for the four order/repetition cases — the notes distinguish them only by
   a hand‑drawn strikethrough through the negated flag. SOL‑2024 confirms
   this on the exam itself: 2a(i) "order matters" shows plain `OM`; 2a(ii)
   "order does not matter" shows `OM` struck through. Reproduce with a
   `\DLINE` stroke through the glyph (pattern already in `tools/atoms.py`,
   used the same way `strike()` handles cancellation).
6. **Proof layouts for 1c/2c/3c** have no solved exhibit. Induction and
   Recursion Notes supply a confirmed general template (recursive
   definition: bare `BC`/`RcS` labels, §6.3; induction proof: `SPf`/`BC`
   bar, then `RcS` with hypotheses `P(0) P(1) ⋯ P(n)` over a bar, inline
   parenthetical justifications, closing `EPf`) — but **no worked example
   of a divisibility statement (`∀n(d∣f(n))`) exists anywhere in the
   searched notes**, by direct or induction proof. Bridging "n is even"
   (exam‑defined only in English prose, p303) to the formal divisibility
   witness (`a∣b:⟺∃c∈ℕ(b=ca)`, Relations Notes p.24) requires treating
   `Evn(n)` as licensing `∃c∈ℕ(n=2c)` — a standard reading, but not
   literally spelled out in either source. Flagged to Sri 2026‑07‑25 for
   sign‑off before finalizing 1c/3c.
7. **2026 data (J=00499317): confirmed, no edge case hit.** `s=2`, `b=0`,
   `b+s=2` — both well‑defined (`s≠b`, no p310 alphabet collapse). `ν(St(J))
   =6`, `ν(MltSt(J))=8` (this second value is a mathematical invariant —
   always 8 for every student, since it counts all 8 J‑digits — not
   personal data, so matching SOL‑2024's own `ν(MltSt(J))=8` is expected,
   not a copying concern).
8. **2A's 1c/2c/3c have no solved exhibit — same gap class as 1C.** Neither
   SOL2A‑2020 nor SOL2A‑2024 attempts 1c (set‑cardinality formation‑trees,
   p411–415), 2c (induction‑proving the (2a)/(2b) conjectures, p421), or 3c
   (repeating‑decimal rational/irrational proofs, p428/p430) — both samples'
   grade tables stop at 3b, total 36. Formats must come from the notes (see
   Rules.md's Exam 2A scope section); do not improvise. Flag to Sri for
   sign‑off before finalizing, per the 1C precedent (item 6 above).
9. **3b's exact formula — confirmed, not a live disagreement.** SOL2A‑2020
   and SOL2A‑2024 print textually different 3b problems
   (`(a+b+1)^(1/(a+b+2))` vs `(abcd)^(1/(abcd+1))`). EXM2A‑2026 p426 prints
   the 2024 wording verbatim — resolved by direct comparison against Sri's
   own exam page, not by the general "follow 2024" tie‑break rule.
10. **`Sm(α,n)`/`Sm(φ,n)` — exam‑supplied, scoped to 2b only.** Printed
    literally on p418 as part of the question. Per Rules.md's "exam may
    supply names… may be repeated and instantiated" clause this authorizes
    `Sm` for 2b's two conjectures; it does not become general geometric‑sum
    notation elsewhere (e.g. not inside 2a's unrolling pieces, where both
    samples instead write the sum out by hand).

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
- 2A: second‑order recurrence system‑solves use boxed elimination algebra,
  not a bar‑inference; repeated‑root/parity verification pieces are direct
  substitution, not `SPf…EPf` induction.
- 2A: `Rtl`/struck‑`Rtl` matches the exam's own rational/irrational gloss;
  no other rational/irrational notation substituted in.
- 2A: problems 1c/2c/3c flagged for Sri sign‑off before finalizing — no
  solved exhibit exists for any of the three.
- 2B: `Vld(·)`/`Tlg`/`Cdn`/`Cng` circle‑choices always come in the pair
  described above — never leave `Pf`/`W` unmarked once `Y`/`N` is marked.
- 2B: canonical‑DNF `φ`‑numbering uses the exhibits' dynamic bottom‑up scan
  (Rules.md), not the notes' fixed reference table — see Rules.md flag.
- 2B: no 1c/2c/3c gap — every problem has a solved exhibit in both years.

## 10. Exam 2B — Propositional Logic

Different domain from every prior exam (logic, not sets/recurrences) — new
display shapes, most existing atoms (`Chain`, `Infer`, `BarStack`, `smart`)
transfer unchanged.

1. **Connective‑list / T‑number setup (folios 502‑505)**: plain numeral
   fills into printed blanks — `J_k`, `C_k` (as the connective glyph, not
   the digit), `T_k` (0/1). No new atom needed, same `fit_centered`/`R`
   fills as 2A's setup page.
2. **Truth‑table piece — needs a new atom, `TruthTable` (not `DivTable`,
   which is single‑value‑grid only)**: two stacked header rows (raw
   `C`‑notation row exactly as printed, then a second row with connectives
   substituted in — both already printed on the blank exam, verify before
   assuming an answer‑layer fill is needed here at all), narrow bit columns
   for `p,q,(r),¬p,¬q,(¬r)`, wider columns per working sub‑expression,
   row‑pairs separated by a blank gap every 2 rows (matching the printed
   grid exactly — do not close the gaps up). Cell values are bare `0`/`1`
   glyphs (`CambriaM`, confirm digit coverage in this exam's own font
   subset before assuming, per the recurring per‑exam font‑gap lesson).
3. **DNF/CNF derivation (2b)**: print the generic 4‑literal disjunction/
   conjunction template line once (`(p∧q)∨(p∧¬q)∨(¬p∧q)∨(¬p∧¬q)`, all four
   terms), then strike the false ones directly on that same line
   (`atoms.strike()`, already built) rather than rewriting a shorter line —
   matches both exhibits exactly, including the case where every term gets
   struck (contradiction) or none does (tautology).
4. **3a classification pieces**: bare 2‑3 step `Chain` (⊺/⊥ substitution →
   simplify), closing with a **separate, un‑barred** line citing
   `Tlg(...)`/`Cdn(...)`/`Cng(...)` of the *substituted‑connective* form of
   the expression (not the `C`‑notation form) — confirmed from both
   exhibits, this closing line is not a `Chain` continuation, it's its own
   small piece.
5. **`Vld(premise/conclusion)` box (1c, 2c, 3b, 3c)**: same tall‑paren
   fraction‑style box already used for 2A's `Sm`/recurrence display —
   premises stacked or side‑by‑side above a bar, conclusion below, whole
   thing enclosed in one `wrap()`‑sized paren pair, Y/N/Pf/W row to the
   right at the box's vertical center.
6. **2c vs. 3b — same validity question, two required methods**: 2c uses
   algebra‑of‑propositions identity rewriting (`Chain` with inline‑cited
   identities, Rules.md's "named identities" note); 3b uses the axioms/
   rules‑of‑inference bar‑chain (`Infer`/`BarStack`, substitution witnesses
   in `⟨⟵⟩` chevrons — same primitive already built for 1C/2A). Do not
   answer one by restating the other's method.
