# Functions — CS/MATH Discrete Math (CCP)
**Date:** 2026-07-08
**Source:** Functions Notes.pdf

## Overview
A function is a relation `R:S⟶T` satisfying `Fncl(R)` (every source element maps to exactly one target element). This note covers function notation, special functions, composition/products, restriction/extension, image/pre-image, and the core properties: equality, injectivity, surjectivity, bijectivity, invertibility.

## Key Concepts

### Notation
A function is specified as `α ≔ x ⟼ α(x) : Src(α) ⟶ Tgt(α)`. Lowercase Greek letters (α, β, ...) or defined strings (sin) denote functions; lowercase Latin letters denote the generic input. `α(x)` is read "alpha of x," never "alpha times x." On exams, since arrow notation for individual assignments (`k ⟼ v`) can't always be typeset, use a two-column input/output table instead.

**Image** (a.k.a. range): `Im(α) ≔ {y∈Tgt(α) | ∃x∈Src(α)(y=α(x))}`. Alternative terminology: Source=Domain, Target=Codomain, Image=Range. **Graph**: `Gr(α) ≔ {(x,α(x)) ∈ Src(α)×Tgt(α) | x∈Src(α)}`.

### Special functions
| Name | Definition |
|---|---|
| Identity | `ι_S ≔ x⟼x : S⟶S` |
| Inclusion (S⊆T) | `ι_{S⊆T} ≔ x⟼x : S⟶T` |
| Constant | `t̃ ≔ x⟼t : S⟶T` for fixed `t∈T` |
| kth projection | `π_k ≔ (s_k\|k∈1..n) ⟼ s_k : ∏S_k ⟶ S_k` |
| kth insertion | `ι_k ≔ s_k ⟼ (s_k,k) : S_k ⟶ ∐S_k` |
| Floor | `Flr(r) ≔ max{z∈ℤ \| z≤r}` |
| Ceiling | `Clg(r) ≔ min{z∈ℤ \| z≥r}` |

Theorems: `∀r∈ℝ, Flr(r)≤r≤Clg(r)`; `∀z∈ℤ, Flr(z)=z=Clg(z)`. Examples: `⌊2.377⌋=2`, `⌈2.377⌉=3`, `⌈−e⌉=−2`, `⌊−π⌋=−4`.

### Operations on functions
- **Composition**: given `α:Src(α)⟶Tgt(α)`, `β:Src(β)⟶Tgt(β)` with `Tgt(α)=Src(β)`, `β∘α ≔ x⟼β(α(x)) : Src(α)⟶Tgt(β)`. Agrees with relational composition. n-fold self-composite defined recursively: `α^{∘0}≔ι`, `α^{∘(n+1)}≔(α^{∘n})∘α`.
- **Product**: `α×β ≔ (x,y)⟼(α(x),β(y)) : Src(α)×Src(β) ⟶ Tgt(α)×Tgt(β)`.
- **Pair** (when `Src(α)=Src(β)=S`): `(α,β) ≔ s⟼(α(s),β(s)) : S ⟶ Tgt(α)×Tgt(β)`.
- **Restriction/Extension/Adjustment**: given `α`, subset `S⊆Src(α)`, superset `T⊇Tgt(α)`: restriction `α|_S ≔ x⟼α(x):S⟶Tgt(α)`; extension `α|^T ≔ x⟼α(x):Src(α)⟶T`; adjustment-to-image `α|^{Im} ≔ x⟼α(x):Src(α)⟶Im(α)`. Used to find **bijective restrictions** — restrict the source and adjust the target to the image until the map is bijective; a restriction is *maximal* if it can't be bijectively extended further.
- **Induced image/pre-image functions**: `α_>(S) ≔ {t∈Tgt(α) \| ∃s∈S(t=α(s))}` (image of a subset); `α_<(T) ≔ {s∈Src(α) \| α(s)∈T}` (pre-image of a subset). These extend to functions `α_>: 𝒫(Src(α))⟶𝒫(Tgt(α))` and `α_<: 𝒫(Tgt(α))⟶𝒫(Src(α))`.

### Properties (all definitions to quote exactly on exams)
- **Equality**: `α=β :⟺ (Src(α)=Src(β)) ∧ (Tgt(α)=Tgt(β)) ∧ (∀x∈Src(α), α(x)=β(x))`.
- **Injectivity**: `Inj(α) :⟺ ∀x,y∈Src(α)((x≠y)⟹(α(x)≠α(y)))`, equivalently `(α(x)=α(y))⟹(x=y)`. Preserves distinctness of inputs. To prove for finite sets: exhibit/inspect all pairs. For infinite source: check if `α(x)=α(y) ⟹ x=y` holds symbolically. To disprove: exhibit `x≠y` with `α(x)=α(y)`.
- **Surjectivity**: `Srj(α) :⟺ ∀y∈Tgt(α) ∃x∈Src(α)(y=α(x))`. Every target element is "hit," i.e. `Im(α)=Tgt(α)`. To prove for infinite source: solve `α(x)=y` for x in terms of y. To disprove: exhibit an un-hit target element.
- **Bijectivity**: `Bij(α) :⟺ Inj(α)∧Srj(α)`.
- **Invertibility**: `Inv(α) :⟺ ∃β:Tgt(α)⟶Src(α) ((β∘α=ι_{Src(α)}) ∧ (α∘β=ι_{Src(β)}))`. β is called *the* inverse of α (symmetric relationship — "inverse" is a historical/relative label, not absolute). Notation: `β=α⁻` (written `α⟵`), and `(α⟵)⟵=α`. **Theorem**: `Bij(α) ⟺ Inv(α)` (proof omitted in source, but stated as fact to use). To find the inverse: solve `α(x)=y` for x in terms of y, giving `β(y)`, then `α⟵ ≔ y⟼β(y) : Tgt(α)⟶Src(α)`.

## Important Formulas / Definitions
Recall from Relations: `Fncl(R) :⟺ ∀s∈S ∃!t∈T(sRt)`; `Fnc(S,T) ≔ {R∈𝒫(S×T) \| Fncl(R)}`. Everything in this chapter (composition, matrices, opposition = inverse when bijective) inherits directly from the Relations chapter — a function's inverse is literally its relational opposite `R^op`, restricted to the case where that opposite is itself functional.

## Summary
Functions are functional relations, and every function concept here (composition, restriction, image/preimage, inverse) is a specialization of the corresponding relation concept, so review Relations alongside this note. The four properties — injective, surjective, bijective, invertible — must each be checked against their exact `:⟺` definitions on exams (finite case: inspection/table; infinite case: solve the defining equation), and `Bij ⟺ Inv` is the key bridge theorem tying bijectivity to the existence of an inverse function.
