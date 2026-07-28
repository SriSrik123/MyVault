# Exam Conventions — CCP Discrete Math (Summer 2026)

**Date:** 2026-07-08
**Source:** Sets Notes, Logic Notes, Relations Notes, Functions Notes, Boolean Algebra Notes, Counting Notes, Binomial Theorem Notes, Induction and Recursion Notes, Symbols.pdf (professor's handouts)

**Reference exam:** [[../exams/Exam1A-MySubmission.pdf]] — Sri's first completed/submitted exam (21-page scan: topsheet, instructions, printed problem pages, ruled work pages). Use this as the format model — page numbering (n0, n1, n2…), ruler-drawn separators, Y/N circling, "Why?" lines, J-number substitution — when working through future practice exams (1B, 1C, 2A, 2B, 2C).

## Overview

This professor grades almost entirely on **exact notational and procedural conformity**, not just correctness. The handouts repeat, dozens of times, some version of "you must follow exactly the same format on the exam or you will get 0 points." This file is the single most important reference for doing any problem/exam in this class — read it before attempting a problem, regardless of topic. Topic-specific content lives in the other files in this folder.

## Abbreviation key (from Symbols.pdf)

| Code | Meaning | Code | Meaning |
|---|---|---|---|
| A | Algorithm | Q | Question |
| C | Corollary | RA | Repetition allowed / not allowed (context-dependent) |
| D | Definition | S | Specification |
| E | Example | SPf | Start of proof |
| EPf | End of proof | T | Theorem |
| F | Fact | W | Witness |
| L | Lemma | OM | Order matters / does not matter (context-dependent) |
| LS / RS | Left side / Right side | Pf | Proof |
| N | Notation | | |

Special sets: ℕ (naturals incl. 0), ℤ (integers), ℚ (rationals), ℝ (reals), ℂ (complex).
Key logic symbols: `≔` defined as, `⟹` implies, `⟺` iff, `∃` there exists, `∄` there does not exist, `∀` for every, `∈ / ∉` is/isn't in, `⊆ / ⊈` subset / not subset, `∪ ∩ \ × ⊔(⨃)` union/intersection/relative complement/product/coproduct(disjoint union).

## The "circle the answer" question format

Many problems are given as: `Assertion   Y   N   Pf   W` — you circle **Y** or **N**, and depending on which, you must also supply either a **Pf** (proof, if true) or a **W** (witness/counterexample, if false). Always show the "Why?" line with the symbolic justification, not prose, e.g. `Why? (c ∈ LS) ∧ (c ∉ RS)`.

## The universal proof skeleton

Nearly every proof in every topic (sets, logic, relations, functions, counting, induction) is displayed as a **stack of horizontal inference bars** ("conclusion bars"), read top to bottom:

```
premise₁   premise₂   ⋯
──────────────────────────   (single bar = one-directional inference)
conclusion
```

A **double bar** (equivalence bar) means the inference goes both ways. Read a bar as "from the assertion(s) above, it follows that the assertion below holds." Proofs of `∀x ∈ 𝒰(...)` universally quantified statements follow this pattern:

1. **SPf** (start of proof): let an arbitrary element be given (e.g. "let A, B ∈ 𝒰, x ∈ 𝒰 be given").
2. Chain of inference bars combining definitions/known facts down to the target statement about that arbitrary element.
3. Generalize: since the element was arbitrary, `∀x ∈ 𝒰(...)` follows.
4. **EPf** (end of proof).

To prove `A ⊆ B`: assume `x ∈ A` (this is "the move of the sceptic"), derive `x ∈ B` using known facts, conclude `∀x(x∈A ⟹ x∈B)`, hence `A ⊆ B`.

To disprove a universal/inclusion claim: exhibit a **witness** — a specific element in the LHS but not the RHS (or vice versa) — and show `(elt ∈ LS) ∧ (elt ∉ RS)`.

## Substitution notation `⟨x ⟵ value⟩`

Whenever a formula/theorem is instantiated with specific values, this must be shown explicitly using angle-bracket substitution notation, e.g.:

```
φ(1) = φ(0+1) = (φ(n+1))⟨n ⟵ 0⟩
```

reads: "we get φ(1) by substituting 0 for n in φ(n+1)." **All exam work with recursive definitions, formulas, or law application must show this substitution step explicitly** — skipping straight to the numeric answer loses points.

## Recursive definitions (BC / RcS)

Every recursively defined object/function has:
- **BC** (Base Case): value(s) at the starting input(s).
- **RcS** (Recursive Step): `∀n ∈ ℕ, ρ(n+1) ≔ Φ(ρ(n), n)` — output at n+1 in terms of earlier outputs.

To *compute* a value, "run backwards": match the input to the RcS pattern via substitution, unfold until you hit the BC, then substitute values back up. Show every line (see Induction/Recursion notes file for worked template).

## Induction proofs — required template

To prove `∀n ∈ ℕ, P(n)`:

1. State `P(n) ≔ (...)` explicitly.
2. Show `P(n)⟨n ⟵ 0⟩` gives `P(0)`, and `P(n)⟨n ⟵ (n+1)⟩` gives `P(n+1)` — write both out.
3. **SPf, BC**: prove `P(0)` directly (chain of equalities LS = ... = RS).
4. **RcS**: assuming `P(0), P(1), ..., P(n)` (induction hypothesis — cite it explicitly as "Induction hypothesis" inline in the equality chain), prove `P(n+1)`, again as a chain `LS = ... = RS`, citing which rule/definition justifies each step in parentheses to the right.
5. Close with the inference-bar diagram (`P(0), P(1),...,P(n)` over `P(0)` and `P(n+1)` conclusion, i.e. strong induction schema) and conclude `∀n ∈ ℕ (P(n))`.
6. **EPf**.

## Equality/inequality chain formatting

When proving `LS = RS` (or manipulating an expression), write a **vertical stack** of `=` signs, lined up on the left, one algebraic step per line, with the justification for that step in parentheses at the right of the line. Never compress multiple algebraic steps into one line on an exam.

## Matrices, trees, and diagrams — must show work

- **Cartesian products**: must draw the generating **tree** (empty slots filled left→right, one level per factor set) — the tree itself is graded, not just the final listed set.
- **Relation matrices M(R)**: build via an intermediate labeled table (rows = source elements, columns = target elements, entries 0/1) before writing the final matrix — both the table and the matrix must appear.
- **Composition of relations via matrices**: `M(P∘Q) = (M(Q))(M(P))` with a `(0,1)` boolean-clamp notation appended if any entry after ordinary multiplication exceeds 1 (replace with 1). Show every entry-by-entry multiplication sum explicitly (e.g. `(0)(0)+(1)(0)+(0)(0)`), not just the final matrix.
- **Directed graphs / Hasse diagrams**: for an n-element relation's own-set digraph, draw a regular n-gon, vertices labeled 1..n going anticlockwise from a horizontal base pair (1,2). Loops (reflexive edges) drawn without arrowheads.
- **Boolean SOP/CSOP multiplication**: must show the multiplication **tree** with every intermediate branch reduced (commutativity/idempotence/complementation applied and simplified at each node) — no skipped steps.
- **Power sets**: list rows by subset size (0-element row, then 1-element row, etc.), trailing comma on every row except the last.

## General exam survival rules (stated explicitly across the notes)

- Maintain exact syntax/conventions shown in the notes (row ordering in power sets, alphabetical/lexicographic ordering of literals and terms in Boolean expressions, source/target element ordering in matrices) — "otherwise you will lose points" / "you will get no points."
- On a Y/N/Pf/W question, if asked to justify non-property (e.g., not reflexive, not injective), give **exactly one** reason even if multiple exist — the professor is testing whether you know how much evidence is sufficient.
- Every definition-based claim (`Fncl`, `Rflx`, `Sym`, `Trns`, `Inj`, `Srj`, etc.) should be checked against its formal `:⟺` definition, not intuition.
- Three equivalent frameworks are used throughout the course for the same laws: **Sets**, **Propositional Calculus (PC)**, and **Boolean Algebra (BA)**. A given identity can be translated between all three (see correspondence table in Boolean Algebra notes) — exam questions may ask to translate or may be easier to solve in one system than another.
