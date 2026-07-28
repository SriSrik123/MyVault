# Induction and Recursion — CS/MATH Discrete Math (CCP)
**Date:** 2026-07-08
**Source:** Induction and Recursion Notes.pdf

## Overview
Recursion defines a family of objects where the (n+1)st is built from the earlier ones; induction is the proof method that establishes a property holds for every natural number given it holds at 0 and is preserved from n to n+1. This note covers the induction schema, recursive-definition template, the standard worked template for computing a recursively-defined value, and the fully worked induction proofs for arithmetic and geometric progressions (used as the template for any induction proof on the exam).

## Key Concepts

### Principle of mathematical induction (strong form as stated in the notes)
```
P(0)  P(1)  ⋯  P(n)
────────────────────
      P(n+1)
─────────────────────────  ∀P ∈ 𝒫(ℕ)
P(0)
──────────────────────────
∀n∈ℕ (P(n))
```
Read: if P(0) holds, and whenever P(0),...,P(n) all hold then P(n+1) holds, then P(n) holds for every natural number.

### Recursive definitions — general template
```
BC (0) ρ(0)  ≔ r₀
   (1) ρ(1)  ≔ r₁
   ⋮
   (p) ρ(p)  ≔ r_p
RcS ∀n∈ℕ  ρ(p+n+1) ≔ Φ((r₀,r₁,...,r_p), n)
```
i.e., one or more base cases, then a recursive step expressing the next output via a fixed function Φ of all earlier outputs (and n).

**Theorem** (properties of recursively defined functions are proved by induction): to show a recursively-defined `ρ:ℕ→ℕ` has property P, i.e. `P(ρ)` holds pointwise as `(P(ρ))(n)`, use exactly the induction schema above with `(P(ρ))(n)` in place of `P(n)`.

### Computing a recursively defined value — required worked template
To compute `φ(1)` given `φ(0)≔1`, `φ(n+1)≔(n+1)φ(n)` (factorial example):
1. Match the target to the RcS pattern via **explicit substitution**: `φ(1) = φ(0+1) = (φ(n+1))⟨n⟵0⟩`.
2. Substitute into the RHS of the RcS definition: `= ((n+1)φ(n))⟨n⟵0⟩ = (0+1)φ(0)`.
3. Substitute the BC value, citing it: `= (1)(1) (∵ φ(0)≔1) = 1`.
4. Repeat for each successive value, always citing the previously computed value in the `(∵ ...)` annotation.

This "running backward" (unfold to the base case, then substitute values back up) is explicitly called the origin of the word "recursion." The same template applies to Fibonacci (`ρ(0)≔0, ρ(1)≔1, ρ(n+2)≔ρ(n+1)+ρ(n)`) and to any other recursively defined sequence.

### Sequences
A sequence is a function `σ:ℕ⟶ℝ`; also written as a family `(σₙ | n∈ℕ)` with `σₙ := σ(n)`.

**Sum of initial segments** (partial sums), defined recursively:
`BC: Sm(σ,0) ≔ σ(0)`; `RcS: Sm(σ,n+1) ≔ Sm(σ,n) + σ(n+1)`, i.e. `Σ_{k=0}^{n+1} σ(k) ≔ Σ_{k=0}^{n} σ(k) + σ(n+1)`.

**Finding a recursive definition from a closed form** — worked examples:
- `(n | n∈ℕ)`: `α(0)≔0`, `α(n+1)≔α(n)+1`.
- `(2ⁿ | n∈ℕ)`: `β(0)≔1`, `β(n+1)≔2·β(n)`.
- `(n² | n∈ℕ)`: since `(n+1)² = n²+2n+1`, define `γ(0)≔0` (careful: source shows `γ(0)≔1` as a possible typo — verify against `0²=0` when doing this problem), `γ(n+1)≔γ(n)+2n+1`.
(Practice problems in the source ask for recursive definitions of `n+2`, `2n`, `2n+1`, `2n+3`, `n(n+1)`, `n(2n+1)`, `n(n+1)(n+2)`, `nⁿ` — good self-test drills.)

### Induction proof — required exam template
Worked example: prove `∀n∈ℕ (2ⁿ > n)`, recast via recursive functions `α(n)=n` (`α(0)≔0, α(n+1)≔α(n)+1`) and `β(n)=2ⁿ` (`β(0)≔1, β(n+1)≔2β(n)`), i.e. prove `∀n∈ℕ (β(n) > α(n))`. Required structure:

1. Define `P(n) ≔ (β(n) > α(n))` explicitly.
2. Show both substituted instances: `P(n)⟨n⟵0⟩` gives `P(0)`, and `P(n)⟨n⟵(n+1)⟩` gives `P(n+1)` — write out both substitutions explicitly before starting the proof.
3. **SPf, BC**: prove `P(0)` as a chain: `β(0) = 1 > 0 = α(0)`, concluding `P(0)`.
4. **RcS**: under the inference bar `P(0) P(1) ⋯ P(n)` (the induction hypothesis, invoked explicitly by name inline), derive `P(n+1)`:
 ```
 β(n+1) = β(n)+β(n)        (by RcS of definition of β)
        > α(n)+α(n)        (Induction hypothesis P(n))
        ≥ α(n)+1           (n≥1)
        = α(n+1)           (by RcS of definition of α)
 ```
 giving `P(n+1)`.
5. Close with the induction-schema inference-bar diagram and conclude `∀n∈ℕ(P(n))`.
6. **EPf**.

**Every line of the equality/inequality chain must cite its justification in parentheses on the right**, and the chain must be a vertical stack of single steps — never combine two algebraic moves into one line.

### Arithmetic progression
`BC: α(0)≔a`; `RcS: α(n+1)≔α(n)+d` (a = initial term, d = common difference).
**T0**: `∀n∈ℕ, α(n) = a+nd`. **T1**: `∀n∈ℕ, Sm(α,n) = (n+1)a + (n(n+1)/2)d`.
Both proved by induction using the exact template above (full worked proofs, including the `P(n)⟨n⟵0⟩`/`P(n)⟨n⟵(n+1)⟩` substitution-statement step, are in the source PDF and should be used as a direct template for any similar proof).

### Geometric progression
`BC: γ(0)≔a`; `RcS: γ(n+1)≔γ(n)·r` (a = initial term, r = common ratio, r≠1).
**T0**: `∀n∈ℕ, γ(n) = a·rⁿ`. **T1**: `∀n∈ℕ, Sm(γ,n) = a·(1−r^{n+1})/(1−r)`.
Both proved by induction using the same template (BC step shows `γ(0)=a=a·r⁰=a(1)`; RcS step uses `γ(n+1)=γ(n)·r` and algebraically manipulates the sum formula for `n+1` from the `n` case, citing the induction hypothesis explicitly).

## Important Formulas / Definitions
- Factorial: `0!≔1`, `(n+1)!≔(n+1)(n!)`; theorem `n! = ∏_{k∈1..n} k`.
- The "Euclid's rule" principle used throughout: *equals substituted into equals yield equals* — this justifies every substitution step in both the computation template and the induction proof template.

## Summary
Recursion and induction are two faces of the same coin: a recursive definition specifies BC + RcS, and induction is exactly the proof method matched to that shape (prove P(0), then prove P(n+1) from P(0),...,P(n)). Every computation of a recursively-defined value and every induction proof must show the explicit substitution steps (`⟨n⟵0⟩`, `⟨n⟵(n+1)⟩`) and cite the justifying rule on each line of an equality chain — skipping this loses points even when the final answer is correct. The arithmetic- and geometric-progression theorems (closed form + partial-sum formula, each proved by induction) are the two fully worked templates to imitate for any other induction exam question, including the combinatorial identities from the Counting notes and the theorems from the Sets/Relations chapters that are explicitly flagged as "to be proved by induction."
