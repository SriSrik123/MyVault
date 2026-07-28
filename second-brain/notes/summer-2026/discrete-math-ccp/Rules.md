# Math 163 Allowed-Content Rules

This file is the mathematical and notational authority for filling Math 163 exams. Its companion `styleguide.md` (vault: `second-brain/notes/summer-2026/discrete-math-ccp/styleguide.md`) is the formatting authority; every token must pass this file's content gate and that file's format gate.

Fully compiled sources (every page read; locator below):

- `Symbols.pdf` - 3 PDF pages, printed pages 0-2.
- `Sets Notes.pdf` - 36 PDF pages, printed pages 0-35.
- `Relations Notes.pdf` - 33 PDF pages, printed pages 0-32.
- `Functions Notes.pdf` - 16 PDF pages, printed pages 0-15.

Additional authorized sources for the Exam 1C scope (counting, binomial/multinomial theorem, recursion, induction). These are course-content authorities of equal rank, but their page locators have NOT yet been compiled - open the PDF and cite the page before using any fact from them:

- `Counting Notes.pdf`
- `Binomial Theorem Notes.pdf`
- `Induction and Recursion Notes.pdf`

All note PDFs live in the vault at `second-brain/notes/summer-2026/discrete-math-ccp/lectures/pdfs/`.

The PDFs above are the only course-content sources. The solved exams (`exams/163Exam1C-Solutions-2020.pdf`, `exams/163Exam1C-Solutions-2024.pdf`) are formatting references only. Their mathematics must not be copied or treated as authority.

## Note Page Locator

Covers the four fully compiled PDFs (Exam 1B scope). A locator for `Counting Notes.pdf`, `Binomial Theorem Notes.pdf`, and `Induction and Recursion Notes.pdf` is still to be compiled; until then, locate and cite pages manually before use.

PDF page numbers below are one greater than the printed footer number.

- `Symbols.pdf`, PDF pp. 1-3: abbreviations, special sets, logic, membership/inclusion, set operations, and inference markers.
- `Sets Notes.pdf`, PDF pp. 1-6: listing/set-builder specifications, `{ }`, `𝒰`, `p..q`, J-number tables, and prime predicates.
- `Sets Notes.pdf`, PDF pp. 7-11: membership, quantified assertions, conclusion bars, and equivalence bars.
- `Sets Notes.pdf`, PDF pp. 12-16: inclusion, equality, and power sets.
- `Sets Notes.pdf`, PDF pp. 17-25: union, intersection, complements, products, coproducts, diagonals, trees, and symbolic proofs.
- `Sets Notes.pdf`, PDF pp. 26-30: further symbolic proofs, cardinality, algebra-of-sets laws, and homework forms.
- `Sets Notes.pdf`, PDF pp. 31-36: recursive specifications and indexed operations.
- `Relations Notes.pdf`, PDF pp. 1-7: relation typing and subset/graph/arrow-diagram/matrix/directed-graph specifications.
- `Relations Notes.pdf`, PDF pp. 8-16: functional/special relations, opposite relations, composition, matrices, and iteration.
- `Relations Notes.pdf`, PDF pp. 17-24: reflexivity, symmetry, antisymmetry, transitivity, equivalence, closures, equivalence classes, partial orders, and Hasse diagrams.
- `Relations Notes.pdf`, PDF pp. 25-31: divisibility, factor sets, partitions, and the partition/equivalence-relation correspondence.
- `Relations Notes.pdf`, PDF pp. 32-33: homework forms.
- `Functions Notes.pdf`, PDF pp. 1-4: function typing, source/target/image/graph, finite displays, and special functions.
- `Functions Notes.pdf`, PDF pp. 5-9: composition, products/pairs, restrictions, target adjustment, and induced image/pre-image.
- `Functions Notes.pdf`, PDF pp. 10-15: equality, injectivity, surjectivity, bijectivity, invertibility, and inverses.
- `Functions Notes.pdf`, PDF p. 16: homework forms.

A topic in this locator authorizes only the definitions, methods, and facts actually stated on those pages. It does not authorize every standard theorem associated with that topic.

## Non-Negotiable Seen-Symbol Rule

Never place a rendered mathematical symbol, abbreviation, operator, delimiter, arrow, proof marker, or diagram convention in an exam answer merely because it is standard mathematics or available in LaTeX.

A rendered token is admissible only after both gates below pass:

1. **Content gate:** its exact rendered form and meaning occur in the current exam or in an approved course-note PDF.
2. **Format gate:** its use is permitted by the `styleguide.md` template selected for that exact solution type. A symbol listed in `Symbols.pdf` is not automatically permitted in every answer format.

The exact glyph matters. Seeing one notation does not authorize a mathematically equivalent notation. Seeing a token in prose or in the symbol catalog does not authorize using it as a proof transition when the worked examples use bars instead.

If either gate fails or is uncertain:

1. Do not use the token.
2. Do not invent a substitute.
3. Re-open the relevant note page and the controlling solved-example page.
4. Use an already observed construction for that solution type if one exists.
5. Otherwise stop and report the notation gap before producing the PDF.

### Explicit Submission Prohibitions

- Do not use the therefore mark `∴` in a submitted answer. It appears in the symbol catalog, but it is not the proof-transition format used by the approved worked solutions, and the project owner has explicitly prohibited it.
- Do not use the because mark `∵` as a proof-transition shortcut. Show the premise above the required conclusion bar instead. Known trap: the 2024 solved Exam 1C itself writes `∵` once (work piece 1a.i.3, justifying a "does not make sense" verdict). The samples are formatting references only and this prohibition outranks them; use the two-premise conclusion bar shown in `styleguide.md` §5.3 instead.
- Do not replace a single conclusion bar with `⟹`, prose such as “therefore,” or a bullet-step transition.
- Do not replace a double equivalence bar with `⟺`, an equals-chain, or two implication arrows.
- A token printed in the current question may be repeated to answer that question, but it does not become generally authorized for other questions.

## Strict Content Source Rule

Every symbol, definition, theorem, proof step, algorithm, and term used in an answer must be supported by the notes or supplied literally in the current exam question.

The exam question may supply names, sets, relations, functions, numerals, predicates, or special notation needed for that question. Those items may be repeated and instantiated, but they do not authorize an outside synonym, theorem, or convention.

If the notes and question do not authorize an item:

1. Do not use it.
2. Do not silently replace it with standard textbook notation.
3. Rewrite the step using authorized notation and facts if possible.
4. If no authorized rewrite is possible, flag the gap before producing the final exam PDF.

Lean, a computer algebra system, or a script may check correctness. Such tools are verifiers, not sources of notation or new mathematical facts for the submitted solution. Do not include Lean syntax or proof-assistant terminology in the exam.

## Source Precedence

When sources differ, use this order:

1. An explicit project-owner instruction, including a prohibition.
2. A literal instruction or notation on the current exam page.
3. These notes and the rules below for mathematical content.
4. `styleguide.md` (vault: `second-brain/notes/summer-2026/discrete-math-ccp/styleguide.md`) for solution-type notation, visual placement, and LaTeX implementation.
5. The solved exams (2020 and 2024 Exam 1C solutions) for visual appearance only; where the two disagree, follow 2024.

Never use a mathematically incorrect solved-exam answer to resolve a mathematical question.

## Submission Mechanics (printed on Exam 1C page 301; binding)

- All work in MECHANICAL PENCIL on the submitted paper copy. A LaTeX build is a master/reference; the submitted document must satisfy this rule.
- Every straight-line segment other than `=, ≠, ≡, <, ≤, >, ≥, +, −, ×, ÷, ¬, ∨, ∧, ∥, ⊥, ∖, →, ↔, ⟼` must be drawn with a ruler (bars, boxes, tables, tree edges, strikethroughs, underlines). At least 1 point off per violation.
- Signs of equality or equivalence must be aligned vertically, one below the other, on the left side of expressions.
- Answers go on the printed page at the indicated areas; all work goes on blank (not ruled) sheets inserted after the page they serve, foliated `n0, n1, n2, ...` in the lower right-hand corner (work for page 304 goes on 3040, 3041, ...). Pieces of work are separated by ruler-drawn straight lines parallel to the paper edges and labelled by problem index plus 0-based completion order.
- Submit a SINGLE document. Do NOT include pages that were not attempted.
- No partial credit: show absolutely all work exactly as in the notes, with no changes, variations, or omissions in form. A correct answer with a disallowed procedure earns no credit.
- "Does not make sense" is a possible answer.
- "As shown in the class" means as shown in the notes.
- Losing conditions to design against: extraneous marks, contradictory answers across instances (zero for every instance), unfinished work, sloppiness or format departures (score of 0).

## Command Rule

The restriction concerns the rendered symbol and mathematical meaning, not the internal LaTeX command name. For example, `\coloneqq` and a carefully constructed `\mathrel{\vcentcolon=}` are both acceptable only if they render as the notes' definition symbol `≔`.

## Authorized Abbreviations

The following labels may be used with their note meanings:

- `A`: Algorithm.
- `BC`: Base case. Printed by Exam 1C on pages 314 and 319; use it exactly where the exam prints it.
- `C`: Corollary. On Exam 1C computation pages, `C(n, k)` is instead the counting function printed by the exam; context decides.
- `D`: Definition.
- `E`: Example.
- `EPf`: End of proof.
- `F`: Fact.
- `L`: Lemma.
- `LS`: Left side.
- `RS`: Right side.
- `N`: Notation.
- `OM`: Order matters. Struck through (`OM` with a horizontal strikethrough): order does not matter. The strikethrough is the negation; there is no separate label. Copy the struck or unstruck state exactly as the current question prints it, and reproduce it in restatements of that question's expressions.
- `P`: Proposition.
- `Pf`: Proof.
- `Q`: Question.
- `RcS`: Recursive step. Printed by Exam 1C on pages 314 and 319; use it exactly where the exam prints it.
- `RA`: Repetition allowed. Struck through (`RA` with a horizontal strikethrough): repetition is not allowed. Same strikethrough convention as `OM`: copy the printed state exactly.
- `S`: Specification.
- `SPf`: Start of proof.
- `T`: Theorem.
- `W`: Witness.
- `Y`, `N`, `Pf`: Yes, No, Proof - defined by Exam 1C on page 303 (`Y := Yes`, `N := No`, `Pf := Proof`, `W := Witness`). On a printed `Y N Pf W` answer row, circle the verdict letter and circle `Pf` or `W`; the proof or witness itself goes on the work sheets.

Do not introduce labels such as “Claim,” “Observation,” “Case,” “Solution,” “QED,” or a tombstone unless the exam itself prints them.

## Authorized Core Symbols

Use these symbols with the meanings given in `Symbols.pdf`:

- Special sets: `ℕ`, `ℤ`, `ℚ`, `ℝ`, `ℂ`.
- Equality and definition: `=`, `≔`, `≠`, `:⟺`.
- Logic: `¬`, `∧`, `∨`, `⟹`, `⟺`, `∃`, `∄`, `∀`.
- Membership and inclusion: `∈`, `∉`, `⊆`, `⊈`.
- Set operations: `∪`, `⨃`, `∩`, `\`, `⊓`, `×`, `⊔`.
- The catalog displays `∵` and `∴`, but they are not authorized for submitted proof transitions; use the course's single and double horizontal bars as specified below.

Symbols visibly defined or used in the topic notes are also authorized only with their note meanings. These include braces, parentheses, brackets, commas, vertical bars, colons, semicolons, arithmetic comparisons and operations, composition circles, assignment arrows, source-to-target arrows, superscripts, subscripts, indexed unions/intersections/products/coproducts, conclusion bars, equivalence bars, and the named notation catalogued below.

## Definition Symbols

- Use `≔` when the left side is being defined by the right side.
- Use `:⟺` when a predicate or assertion is being defined by an equivalent condition.
- Use `=` only for equality after both sides already have meanings.
- Use `⟺` for ordinary logical equivalence, not for a definition.
- Preserve the notes' direction: the item being defined is on the left.

Do not use `:=`, `=:`, `def`, `iff` written as prose, or a plain equality sign when the notes require a definition symbol. If the printed exam itself uses an ASCII-looking `:=`, match the printed glyph exactly on that page.

## Sets: Authorized Content

The following content from `Sets Notes.pdf` may be used:

- The universe `𝒰` and empty set `{ }`.
- Set specification by listing and by set-builder notation.
- Set-builder form `{x∈S|P(x)}` and its membership test.
- Integer/natural intervals `p..q` as defined in the notes.
- Membership and non-membership.
- Existential and universal quantification, including clustered variables such as `∀x,y∈S`.
- Inferences displayed with a horizontal conclusion bar.
- Two-way inference displayed with a double equivalence bar.
- Inclusion, non-inclusion, proper inclusion where it appears in the notes, and set equality.
- Power set `𝒫(A)`.
- Union, intersection, relative complementation, absolute complementation, Cartesian product, coproduct, and disjoint union.
- The diagonal set notation defined in the notes.
- Tables with `Y` and `N` choices and circled qualifying entries.
- Tree generation for Cartesian products when the notes require that construction.
- Cardinality `ν(S)` and the cardinality formulas stated in the notes.
- The algebra-of-sets laws displayed in the notes.
- Recursive specifications illustrated in the appendix.
- Indexed sums, products, coproducts, unions, intersections, conjunctions, and disjunctions in the exact forms used on printed pages 34-35.

### Required Set Methods

- List each element of a finite set exactly once.
- When the notes require increasing order, use increasing order.
- For J-number set-builder questions, show the prescribed table, circle `Y` or `N`, circle the selected source entries, and then list the resulting set.
- For union, intersection, and relative complement computations, align equality signs vertically when showing successive set reductions.
- For Cartesian products, generate elements systematically in the notes' order. Draw the two-level tree when the prompt or grading format calls for it.
- For symbolic set proofs, use a sequence of inference/equivalence bars and the minimal vocabulary shown in the notes. Do not replace the symbolic proof with a prose proof.

### Forbidden Set Alternatives

- Never use `∅` or `\varnothing`; use `{ }`. The notes explicitly say use of `∅` loses points.
- Do not use `|A|`, `#A`, `card(A)`, or `\operatorname{card}(A)` for cardinality; use `ν(A)`.
- Do not use `A-B` for relative complementation; use `A\B`.
- Do not use an overline for complement. Use the absolute-complement notation from the notes only when the universe `𝒰` is the intended ambient set.
- Do not use interval notation such as `[p,q]∩ℤ` when the notes' `p..q` is intended.
- Do not use `⊂` as a casual synonym for `⊆`. Use each only with the distinction made in the notes.
- Do not use braces around an ordered pair where parentheses are required.
- Do not omit the universe from set-builder notation when it is needed to establish membership.

## Relations: Authorized Content

The following content from `Relations Notes.pdf` may be used:

- A relation as a typed subset, with source `Src(R)`, target `Tgt(R)`, and graph `Gr(R)`.
- Relation statements in the forms `R(x,y)`, `xRy`, `Rxy`, and `(x,y)∈R` when context permits.
- Relation specification as a subset, graph, arrow diagram `AD(R)`, matrix `M(R)`, and directed graph `DG(R)` under the conditions given in the notes.
- The set of relations notation defined in the notes.
- Functional relation predicate `Fncl(R)`.
- Empty, total, and diagonal relations.
- Opposite relation `R^op` in the notes' notation.
- Relation composition in the notes' order.
- Iteration of a relation with the given base case and recursive step.
- Reflexivity `Rflx(R)`, symmetry `Sym(R)`, antisymmetry `AntSym(R)`, transitivity `Trns(R)`, equivalence `Equ(R)`, and partial order `PrtOrd(R)`.
- Reflexive, symmetric, transitive, and equivalence closures with the exact names used in the notes: `RflxClsr`, `SymClsr`, `TrnsClsr`, and `EquClsr`.
- Equivalence classes, the quotient/set of equivalence classes, partitions, and the correspondence between partitions and equivalence relations.
- Hasse diagrams `HsDgrm` for partial orders.
- Divisibility and factor-set notation exactly as defined in the notes.
- Boolean matrix computation for relation composition, including replacing any result greater than `1` by `1`.

### Required Relation Displays

- A graph display places source values along the horizontal axis and target values along the vertical axis as shown in the notes.
- An arrow diagram uses two vertical lists. Put entries in rectangles and draw assignment arrows from source to target.
- To compute `M(R)`, first show the labeled source/target table, then a horizontal conclusion bar, then the bracketed matrix. Follow the exact source and target ordering from the question.
- A directed graph is allowed only when source and target are the same carrying set.
- For a carrying set `1..n`, place vertices on a regular `n`-gon. Put `1` and `2` on the horizontal base and label anticlockwise.
- Directed-graph vertices are circles on exams. Arrow-diagram entries are rectangles.
- A loop is drawn without an arrowhead.
- For closure computations, show added arrows/entries as the work requires and repeat the prescribed construction until the defining defect is gone.
- For Hasse diagrams, remove loops and arrows implied by transitivity, orient by the notes' convention, and preserve the factor/order construction used there.

### Forbidden Relation Alternatives

- Do not use `R^{-1}` for the opposite relation; use the notes' `R^op` notation.
- Do not use `R*`, `R+`, “transitive-reflexive closure,” or unnamed closure operators.
- Do not rename `Src`, `Tgt`, or `Gr` as `dom`, `codom`, field, support, or range.
- Do not use adjacency-list or edge-list terminology in the submitted answer unless the exam prints it.
- Do not draw arrow-diagram entries as free text, circles, or ovals; use rectangles.
- Do not draw directed-graph vertices as rectangles; use circles.
- Do not put an arrowhead on a loop.
- Do not skip the labeled matrix work table and conclusion bar when computing a relation matrix.
- Do not reverse the order of relation composition. Follow the typed source/target chain in the notes.
- Do not use ordinary arithmetic matrix multiplication as the final relation matrix without the notes' `>1` to `1` conversion.

## Functions: Authorized Content

The following content from `Functions Notes.pdf` may be used:

- Functions as functional relations and the set `Fnc(S,T)`.
- Function specification in the five-part form `α ≔ x ↦ α(x): Src(α) ⟶ Tgt(α)`.
- Lowercase Greek function names and defined Latin strings such as those used in the notes.
- Source `Src(α)`, target `Tgt(α)`, image `Im(α)`, and graph `Gr(α)`.
- Finite functions displayed by assignment tables/arrows.
- Identity, inclusion, constant, projection, and insertion functions in the exact notations defined in the notes.
- Floor `Flr` and ceiling `Clg` notation and the facts stated in the notes.
- Function composition in the order `β∘α`, with `α` applied first.
- Iterated composition with the notes' base case and recursive step.
- Product functions and paired functions.
- Restriction of source, extension of target, and adjustment of target to image in the notes' bar notation.
- Induced image and pre-image functions in the notes' `α^>` and `α^<` notation.
- Function equality using equality of source, target, and values.
- Injectivity `Inj`, surjectivity `Srj`, bijectivity `Bij`, and invertibility `Inv`.
- Inverse-function notation exactly as defined in the notes.
- The sets of injective/surjective functions when their names appear in the notes or current exam.

### Required Function Displays

- A complete function specification has a name, generic input, output expression, source, and target in the notes' order.
- Use `↦` for assignment. Use `⟶` between source and target.
- For a finite function, draw the assignment table with every source element assigned exactly one target element.
- For finite injectivity or surjectivity questions, use the display/inspection method required by the notes.
- To disprove injectivity, provide distinct source elements with the same output.
- To disprove surjectivity, identify a target element that is not hit or show `Im(α)≠Tgt(α)`.
- To prove surjectivity for an infinite source, use only the solve-for-input method described in the notes when applicable.
- To find an inverse, follow the notes' displayed procedure and retain source/target information.

### Forbidden Function Alternatives

- Do not abbreviate the course specification to only `f:S→T`; include the five items when specifying a function.
- Do not use `D`, `Dom`, `domain`, `Cod`, `codomain`, or `range` in place of `Src`, `Tgt`, and `Im` in submitted notation. The notes mention alternate terminology but the course format uses `Src`, `Tgt`, and `Im`.
- Do not use `x→f(x)` for assignment; use `x↦f(x)`.
- Do not use `id_S`; use the identity notation defined in the notes.
- Do not use standard `f^{-1}(B)` for set pre-images when the induced pre-image notation `f^<(B)` is required.
- Do not use a superscript `-1` for the inverse function unless the current exam prints it; use the inverse notation defined in the notes.
- Do not replace `Flr` and `Clg` with unrelated floor/ceiling function names.
- Do not omit unused target elements from a function's target.
- Do not infer surjectivity merely from functionality, or injectivity merely from distinct-looking labels.

## Counting, Binomial Theorem, and Recursion: Authorized Content (Exam 1C scope)

Exam 1C prints, and thereby authorizes for this exam, the following. Exact general formulas, definitions, and display procedures behind them must still be taken from `Counting Notes.pdf`, `Binomial Theorem Notes.pdf`, and `Induction and Recursion Notes.pdf` (cite the page; no locator compiled yet):

- `St( J)`, `MltSt( J)`, `Lst( J)` and the exam's local names `SJ`, `MSJ`; `ν` applied to sets and multisets; multiset elements displayed as `value:multiplicity` pairs.
- `mxm{...}` and `mnm{...}` for maximum and minimum of a set, exactly as printed on pages 302-303.
- `Evn(x)`, `Odd(x)`, `Prm(x)` as defined on page 303.
- `∤` (does not divide) - authorized by the printed R note on page 306; type it only against the source/target typing that the defining set-builder expression gives it.
- `C(n, k)` and `P(n, m)` counting functions and `Wrd(n, {alphabet}, OM, RA)` with struck/unstruck `OM`/`RA` states copied from the print (pages 304, 310).
- `BnmlCfn` and `MltnmlCfn` as printed on page 316. The general-formula names used on work sheets must match the Binomial Theorem notes exactly - the 2020 sample appears to write `BnmlCfnt`/`MltnmlCfnt`, the 2024 sample writes `BnmlCfn`/`MltnmlCfn` for both roles; verify against the notes before use and do not guess.
- Binomial coefficients as tall-paren stacks (upper entry over lower entry) and multinomial coefficients (upper entry over a row of lower entries), with no fraction bar; factorial `!`; factorial expansions and cancellation displays in the notes' parenthesized forms.
- The indexed sum `∑` with a constraint subscript such as `p+q=4`, as printed on page 317.
- The substitution witness `⟨ x ⟵ e ⟩` (one assignment per stacked row; ditto form `⟨ " ⟩` after the full list has appeared once) for displaying substitution into a general formula, as required by the printed instruction "show computations or substitutions into appropriate formulas" and exhibited by both solved exams; layout in `styleguide.md` §5.2.
- `BC` and `RcS` labels for base case and recursive step (printed on pages 314 and 319).
- The prose verdict `does not make sense` (authorized by page 301), displayed per `styleguide.md` §5.3.
- Tree generation for word/number enumeration (root of slot dashes, prefix nodes, increasing children, visible dead branches) and the exhaustive-table method with circled qualifying entries - display grammar in `styleguide.md` §6.

Counting facts, identities (for example the symmetry of binomial coefficients), and proof methods for induction/recursion questions must be located in the three note PDFs before they appear in an answer. If a needed fact cannot be located there or in the current exam, flag the gap; do not import it from memory.

## Proof Syntax

Proofs in this course are displayed as sequences of inferences.

- A **single horizontal conclusion bar** means that the statement or statements immediately above imply the statement immediately below.
- A **double horizontal equivalence bar** means that the statement immediately above implies and is implied by the statement immediately below.
- Put premises above the applicable bar and the resulting statement below it. Never place `∴`, `∵`, `⟹`, or `⟺` between proof rows.
- Multiple premises written side by side on one level have implicit conjunctions. Do not insert a new conjunction symbol unless the controlling example writes the conjunction explicitly on that row.
- Use a double bar only for a reversible transformation. Use a single bar when introducing or eliminating a quantifier, applying a premise in only one direction, moving from elementwise reasoning to inclusion/equality, or drawing a final conclusion.
- A sequence proof alternates formula rows with the required bar type. Bar count is mathematical syntax, not decoration: one stroke and two strokes are never interchangeable.
- For set equality proofs, follow the observed structure: begin with element-membership assertions, use double bars only for reversible membership rewrites, then use single bars for the quantified membership equivalence and the final set equality.
- For inclusion proofs, use the observed one-way inference stack and a single bar at every deduction level.
- For relation/function property proofs, place the facts or witnesses at the top, derive each predicate through single-bar steps, and place the quantified property statement below the final single bar.
- LS/RS verification is a separate format, not an equivalence-bar proof. Put assignments above the two columns, compute LS and RS independently, and compare them below full-width single bars.
- Use `SPf` and `EPf` when the note/example format calls for proof delimiters.
- Keep quantified variables and their universes explicit.
- Use witnesses and counterexamples in the forms shown in the notes.
- Read each step both symbolically and in words during checking, but submit the compact symbolic form used in the examples.

Do not replace a required inference proof with paragraph prose, a truth-table argument not present in the notes, set extensionality jargon, tactic names, or a citation to an outside theorem.

## Information That Is Not Authorized

Unless a current exam question states it explicitly, do not use:

- Any theorem, lemma, identity, algorithm, terminology, or notation from another textbook, website, class, or memory that does not occur in these notes.
- Category-theory language, abstract algebra terminology, graph-theory terminology beyond the notes, or proof-assistant vocabulary.
- Standard shorthand merely because it is mathematically equivalent.
- An unstated convention about whether natural numbers start at `0`; these notes explicitly define `ℕ` as starting at `0`.
- Empty-set, inverse, cardinality, domain/range, closure, or identity notation from another course.
- A calculator/computer result without the note-prescribed displayed work when the method is graded.
- Facts copied from the solved exams unless independently justified from the notes and current question.

## Conservative Decision Test

Before placing any mathematical token in the PDF, ask:

1. Does the current exam print or define it?
2. If not, can its rendered symbol and meaning be located in one of the four note PDFs?
3. Does the selected solution-type template in `styleguide.md` permit this token in this position?
4. Is the construction method the same one the notes and examples require for this problem type?
5. Is there a course-specific notation or bar construction that must replace a more familiar standard form?

If any answer is uncertain, do not improvise. Re-open only the relevant note page, resolve the ambiguity, and update this file if a genuinely missing authorized convention is found.

## Final Compliance Check

- Empty set is `{ }`, never `∅`.
- Definitions use `≔` or `:⟺` correctly.
- Set cardinality uses `ν`.
- Sources, targets, images, and graphs use `Src`, `Tgt`, `Im`, and `Gr`.
- Assignment uses `↦`; source-to-target typing uses `⟶`.
- Relation opposite, closures, equivalence classes, and induced image/pre-image use course notation.
- Required tables, trees, matrix work, conclusion bars, and diagrams are shown.
- Every rendered token passed both the content gate and the format gate.
- No `∴` or `∵` occurs in a submitted answer.
- Every proof transition uses the correct single or double horizontal bar; no arrow or prose substitutes for a bar.
- Finite-set entries are unique and ordered as required.
- Signs of equality/equivalence are aligned vertically on the left; first line of a chain is the bare expression.
- Work sheets are foliated `n0, n1, ...` lower right; pieces are boxed, labelled, and 0-base counted; no unattempted pages included.
- Struck/unstruck `OM`/`RA` states match the print everywhere they are restated.
- Every answer sits at a printed anchor or inside a work-sheet piece (`styleguide.md` §3-§4); no extraneous marks.
- No external theorem, synonym, or notation appears.
- The mathematical content was not copied from the intentionally incorrect solved exams.
