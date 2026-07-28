# Relations — CS/MATH Discrete Math (CCP)
**Date:** 2026-07-08
**Source:** Relations Notes.pdf

## Overview
A relation generalizes the intuitive idea of human relationships (sibling, parent, ancestor). Covers formal definition and specification methods (subset, graph, arrow-diagram, matrix, digraph), operations (opposition/converse, composition, iteration), the core properties (reflexive, symmetric, antisymmetric, transitive) with their closures, equivalence relations and partition, and partial orders with Hasse diagrams.

## Key Concepts

### Definition and specification
A relation `R:S⟶T` is a subset of `S×T` (its **graph**, `Gr(R)`); coded as the triple `(Src(R), Gr(R)⊆Src(R)×Tgt(R), Tgt(R))`. Notation: `(s,t)∈R ⟺ sRt ⟺ R(s,t)`. `Rln(S,T) ≔ 𝒫(S×T)`; if `S=T`, `Rln(S) ≔ Rln(S,S)`.

Five equivalent specification methods (each makes different properties easy to see):
1. **Subset** of S×T
2. **Graph** `Gr(R)` — plotted as circled points on a grid, S along horizontal, T along vertical
3. **Arrow-diagram** `AD(R)` — assignment arrows from each related source element to target element(s)
4. **Matrix** `M(R)` — build via an intermediate table (rows=source elements listed in order, columns=target elements listed in order, entries 0/1 for related/not), then write the matrix; **this intermediate table must be shown on exams**
5. **Directed graph** `DG(R)` — only when `Src(R)=Tgt(R)`; vertices arranged as a regular n-gon, labeled 1..n anticlockwise starting from a horizontal base pair (1,2); loops for reflexive pairs, drawn without arrowheads

### Functionality
`Fncl(R) :⟺ ∀s∈S ∃!t∈T (sRt)` — every source element has exactly one output. `Fnc(S,T) ≔ {R∈𝒫(S×T) | Fncl(R)}`. On exams, when a relation fails to be functional for two reasons (unassigned input AND an input with two outputs), you only need to give **one** reason.

### Special relations
- **Empty**: `Emp_{S×T} ≔ {} ⊆ S×T`
- **Total**: `Ttl_{S×T} ≔ S×T`
- **Diagonal/identity**: `Δ_S ≔ {(s,t)∈S×S | s=t}` — always functional

### Operations
- **Opposite/converse**: `R^op ≔ {(t,s)∈T×S | R(s,t)} ⊆ T×S`. Mechanically: interchange source/target, reverse every arrow (arrow diagram), reflect graph across the diagonal, **transpose the matrix** — `M(R^op) = (M(R))^T`, reverse all digraph arrows (loops unchanged).
- **Composition**: given `Q:S⟶U`, `P:U⟶T`, `P∘Q ≔ {(s,t)∈S×T | ∃u∈U(Q(s,u)∧P(u,t))}`. Associative but **not commutative** in general. Matrix form: `M(P∘Q) = (M(Q))(M(P))⟨0,1⟩` — note the **reversed order** of factors, and the `(0,1)` boolean clamp meaning "replace any entry >1 with 1" after ordinary matrix multiplication. Every entry-by-entry sum must be shown explicitly on exams (e.g. `(0)(0)+(1)(0)+(0)(0)`), and matrix computations may be cross-checked two ways: compute the composite relation directly then find its matrix, OR multiply the factor matrices in reverse order — both must agree.
- **Iteration**: `R^{∘0} ≔ Δ_S`; `R^{∘(n+1)} ≔ (R^{∘n})∘R` (recursive definition, same pattern for functional relations using `ι_S` as base case).

### Properties of a relation R:S⟶S (and their closures)
| Property | Definition | Closure formula | Digraph test |
|---|---|---|---|
| Reflexive | `Rflx(R):⟺∀s∈S(sRs)` | `RflxClsr(R) = R∪Δ_S` | every vertex has a loop |
| Symmetric | `Sym(R):⟺∀s,t∈S(sRt⟹tRs)` | `SymClsr(R) = R∪R^op` | every pair of distinct vertices has 0 or 2 (opposite) arrows |
| Antisymmetric | `AntSym(R):⟺∀s,t∈S((sRt)∧(tRs)⟹s=t)` | — | — |
| Transitive | `Trns(R):⟺∀r,s,t∈S((rRs)∧(sRt)⟹rRt)` | `TrnsClsr(R) = ⋃_{n=1}^{ν(S)} R^{∘n}` | no "incomplete directed triangle" (two of three sides present, third missing) |

To disprove a property, exhibit exactly one violating instance (a missing loop, a one-directional arrow, an incomplete triangle). To construct a closure: either apply the formula, or fix the digraph directly (add missing loops/arrows/triangle-closing edges, repeating until none remain) — both methods must agree.

### Equivalence relations
`Eqv(R):⟺ Rflx(R)∧Sym(R)∧Trns(R)`. Equivalence closure: `EqvClsr(R) = ⋃_{n=0}^{ν(S)} (R∪R^op)^{∘n}`.
Equivalence class: `EqvCl(s,E) ≔ {t∈S | tEs}`. Key theorems: two equivalence classes intersect iff their representatives are related (`EqvCl(s,E)∩EqvCl(t,E) ≠ {} ⟺ sEt`); `S = ⋃_{s∈S} EqvCl(s,E)`. The **quotient** `S/E ≔ {EqvCl(s,E) | s∈S}` partitions S: `S = ⨃ (equivalence classes)`. A canonical representative/normal form is a uniform choice of one distinguished element per class, when possible.

### Partial orders
`PrtOrd(R):⟺ Rflx(R)∧AntSym(R)∧Trns(R)`. Displayed via **Hasse diagram** `HsDgrm(R)`. Classic examples: `⊆` on `𝒫(S)`, and divisibility `|` on ℕ (`∀a,b∈ℕ a|b :⟺ ∃c∈ℕ(b=ca)`; note `∀n∈ℕ(n|0)`, and `0|0` holds but `0/0` remains undefined). `PO(ℕ\{0}, |)` is a standard proved theorem (full inference-bar proof in source PDF).

**Hasse diagram of divisors of 100** (worked example): factor via prime bookkeeping (`100 = 2²·5²`), enumerate factors as 2-letter words over exponents `{0,1,2}` for primes 2 and 5, giving `Fctrs(100) = {1,2,4,5,10,20,25,50,100}`, then draw the divisibility Hasse diagram (this factoring-into-exponent-words technique reappears in Counting notes).

## Summary
Relations are subsets of a Cartesian product, specifiable five equivalent ways, and functions are simply relations satisfying `Fncl`. The four core properties (reflexive/symmetric/antisymmetric/transitive) combine into equivalence relations (→ partition/quotient) and partial orders (→ Hasse diagrams); every property has both a formal definition and a mechanical digraph test, and every failure needs exactly one witness. Composition and opposition connect directly to matrix arithmetic (with the boolean `(0,1)` clamp), which is examined heavily and must be shown in full entry-by-entry detail. This chapter is the direct foundation for Functions (a function is a functional relation).
