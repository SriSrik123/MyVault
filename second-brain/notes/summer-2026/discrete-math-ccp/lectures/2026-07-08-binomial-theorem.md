# Binomial and Multinomial Theorem — CS/MATH Discrete Math (CCP)
**Date:** 2026-07-08
**Source:** Binomial Theorem Notes.pdf

## Overview
The binomial theorem (and its multinomial generalization) gives a closed formula for expanding `(a+b)ⁿ`, with the coefficients being exactly the `C(n,k)` combinations from the Counting notes. Covers expansion mechanics, coefficient-extraction notation, Pascal's triangle symmetry, and special summation identities (splitting even/odd-degree expansions, substitutions like `b←−b` and `b←x⁻¹`).

## Key Concepts

### The Binomial Theorem
`∀a,b∈ℝ, ∀n∈ℕ: (a+b)ⁿ = Σ_{k=0}^{n} C(n,k) a^{n−k} b^k`

**Why**: expanding `(a+b)ⁿ` means choosing, independently in each of the n factors, either `a` or `b`; choosing `b` in exactly `k` of the `n` slots can be done in `C(n,k)` ways, giving the term `a^{n−k}b^k` with coefficient `C(n,k)`.

**Coefficient notation**: `Cfcnt(a^{n−k}b^k, (a+b)ⁿ) = C(n,k)`. Example: `Cfcnt(a⁷b³,(a+b)¹⁰) = C(10,3)` (leave as a binomial coefficient — no need to compute the decimal value unless asked).

### Expansion procedure (exact exam format)
To expand something like `(2−3x)³`:
1. Rewrite as `(a+b)ⁿ` form: `(2+(−3x))³`, matching `a←2, b←(−3x), n←3` — show this substitution explicitly with `⟨...⟩` bracket notation.
2. Write out the general sum `Σ C(n,k) a^{n−k}b^k` with the substitution applied, before evaluating.
3. Expand term by term, k=0 to n, each term computed and simplified as its own numbered sub-step (label each term computation, e.g. "30", "31", "40", "41", ... in the source's bookkeeping scheme).
4. Present final terms in **numero-alphabetical order**: numbers before letters, letters alphabetical, and among the numbers only `−1` is allowed as a coefficient placeholder (it precedes all positive numbers); terms/words are then ordered lexicographically (numbers-only terms first).
5. Show all binomial-coefficient computations (`C(3,3)=1`, `C(3,2)=3`, etc.) as their own explicit sub-derivations.

**All work must be displayed in side-by-side indexed columns with a ruled vertical line separating them** — this formatting requirement is stated explicitly and repeatedly.

### The Multinomial Theorem
`∀x₁,...,x_p∈ℝ, ∀p,n∈ℕ: (x₁+x₂+⋯+x_p)ⁿ = Σ_{n₁+⋯+n_p=n} P(n; n₁,...,n_p) · x₁^{n₁}x₂^{n₂}⋯x_p^{n_p}`

Coefficient: `Cfcnt(x₁^{n₁}⋯x_p^{n_p}, (x₁+⋯+x_p)ⁿ) = P(n; n₁,...,n_p) = n!/(n₁!n₂!⋯n_p!)` (the multinomial coefficient from Counting notes). Example: `Cfcnt(x₁³x₂²x₃¹,(x₁+x₂+x₃)⁶) = P(6;3,2,1)`.

Alternative coefficient formula via sequential choosing: `C(n,n₁)·C(n−n₁,n₂)·C(n−n₁−n₂,n₃)⋯` — choose `n₁` slots for `x₁` out of n, then `n₂` slots for `x₂` out of the remainder, etc. (Exercise: show this equals the multinomial coefficient directly.)

**Expansion procedure** mirrors the binomial case: substitute into the general sum with explicit `⟨...⟩` brackets, enumerate all valid `(n₁,...,n_p)` decompositions of n in lexicographic order (e.g. for n=2, p=3, alphabet `{0,1,2}`: 002, 011, 020, 101, 110, 200), compute each coefficient and term as indexed sub-steps, then present the final answer in numero-alphabetical/lexicographic term order using condensed exponent notation (`x²` not `xx`).

### Pascal's Triangle and structural identities
```
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
   1 5 10 10 5 1
  1 6 15 20 15 6 1
```
- **Symmetry** (`C(n,k)=C(n,n−k)`) makes each row symmetric about its center.
- **Addition/Pascal's rule** (`C(n,k)+C(n,k+1)=C(n+1,k+1)`) generates each entry from the two above it in the preceding row.

### Special expansion identities (via substitution)
Splitting `(a+b)ⁿ` by even/odd n and adding the "forward" and "reversed" (`a↔b` swapped) expansions, dividing by 2, yields closed forms:

`(a+b)^{2n} = [Σ_{k=0}^{n} C(2n,k)(ab)^k(a^{2n−2k}+b^{2n−2k})] − C(2n,n)`

`(a+b)^{2n+1} = Σ_{k=0}^{n} C(2n+1,k)(ab)^k(a^{2n−2k+1}+b^{2n−2k+1})`

Substituting `b←−b` gives the corresponding `(a−b)ⁿ` forms (with alternating `(−1)^k`). Adding/subtracting the `(a+b)ⁿ` and `(a−b)ⁿ` forms gives further identities isolating even/odd-power terms. Substituting `a←x, b←x⁻¹` (so `ab←1`) gives the trigonometric-style identities:

`(x+x⁻¹)^{2n} = [Σ C(2n,k)(x^{2n−2k}+x^{−(2n−2k)})] − C(2n,n)`
`(x−x⁻¹)^{2n} = [Σ C(2n,k)(−1)^k(x^{2n−2k}+x^{−(2n−2k)})] − C(2n,n)`
`(x+x⁻¹)^{2n+1} = Σ C(2n+1,k)(x^{2n−2k+1}+x^{−(2n−2k+1)})`
`(x−x⁻¹)^{2n+1} = Σ C(2n+1,k)(−1)^k(x^{2n−2k+1}−x^{−(2n−2k+1)})`

## Important Formulas / Definitions — Combinatorial Identities (shared with Counting notes)
Same six identities as in Counting notes (Symmetry, Absorption, Trinomial Revision, Parallel Summation, Upper Summation, Vandermonde Convolution, Addition) — restated here because they're the algebraic backbone for manipulating binomial-coefficient sums that arise from expansions.

## Summary
The binomial/multinomial theorems are direct applications of the `C(n,k)` / multinomial-coefficient counting functions from the Counting chapter: expanding `(a+b)ⁿ` is equivalent to choosing, in each of n slots, which variable appears, so the coefficients are counts of choices. Exam grading is strict about showing the `⟨a⟵..., b⟵..., n⟵...⟩` substitution step, indexed/columned sub-calculations, and the numero-alphabetical/lexicographic ordering convention for final terms. Pascal's triangle symmetry and addition rules, plus the even/odd-splitting substitution tricks (`b←−b`, `a,b←x,x⁻¹`), round out the identities likely to be tested.
