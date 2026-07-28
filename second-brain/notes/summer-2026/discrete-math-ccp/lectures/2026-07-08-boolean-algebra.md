# Boolean Algebras — CS/MATH Discrete Math (CCP)
**Date:** 2026-07-08
**Source:** Boolean Algebra Notes.pdf

## Overview
Boolean Algebra is the third of three parallel systems (alongside Sets and Propositional Calculus) satisfying the same axioms under different names. This note covers the BA axioms/derived theorems, the translation algorithm between Sets/PC/BA, canonical (sum-of-products) forms for Boolean expressions, and the consensus method for finding prime implicants and minimal sum-of-products (MSOP) forms — heavily exam-tested with exact formatting requirements.

## Key Concepts

### Axioms and primary connectives
Primary connectives chosen per system: Sets `({}, 𝒰, ( )ᶜ, ∪, ∩)`; PC `(⊥, ⊺, ¬, ∨, ∧)`; BA `(0, 1, ( )', +, ·)`. A Boolean algebra is a set B with nullary `0,1`, unary complementation `( )'`, and binary `+, ·` satisfying: commutativity, distributivity (`x+(y·z)=(x+y)·(x+z)` and dually), identity (`x+0=x`, `x·1=x`), complement (`x+x'=1`, `x·x'=0`). Shorthand `xy ≔ x·y`.

**Derived theorems** (provable from axioms): idempotent (`x+x=x`), boundedness (`x+1=1`, `x·0=0`), absorption (`x+(x·y)=x`), associativity, `0'=1`,`1'=0`, De Morgan's (`(x+y)'=x'y'`, `(xy)'=x'+y'`), involution (`(x')'=x`), and uniqueness of complement: if `x+y=1` and `x·y=0` then `y=x'`.

### Translation algorithm (Sets ⟷ PC ⟷ BA)
1. Rewrite the expression making all connectives explicit (in PC, `ab := a·b`).
2. Rewrite using only the allowed primitive connectives of the target system (in Sets, `A\B = A∩Bᶜ`; in PC, `p⟶q = (¬p)∨q`, `p⟷q = ((¬p)∨q)∧(p∨(¬q))`).
3. Insert parentheses to make order of operations explicit.
4. Apply the correspondence table (see `2026-07-08-logic.md` for the full 3-column law table) term by term.

Worked example: `ab'+c` in PC is `(p∧(¬q))∨r`; in Sets, `(A∩Bᶜ)∪C`. A full identity proof (e.g. `(p⟶q) = ((p∧(¬q))⟶⊥)`) can be carried out entirely in BA (often easiest, since BA resembles ordinary algebra) and then translated back line-by-line into the other systems — **all substitutions must be shown explicitly** with the `⟨a⟵x⟩` bracket notation, and the rule used cited in parentheses on each line, starting from whichever side looks more complex.

### Literals, fundamental products, and canonical forms
- **Literal**: a variable or its complement, e.g. `x` or `x'`. Literals are ordered: alphabetically, and for the same variable, uncomplemented precedes complemented (`a, a', b, b', ...`).
- **Fundamental product (FP)**: a product of literals in *distinct* unknowns.
- `Ukn(E)` = unknowns occurring in E; `SLtr(E)` = set of literals in E; `MSLtr(E)` = multiset of literals (with counts).
- Inclusion of fundamental products: `P₁⊆P₂ :⟺ Ltr(P₁)⊆Ltr(P₂)`; theorem `P₁⊆P₂ ⟹ P₁+P₂=P₁` (absorption).
- **SOP form**: `SOPFrm(E) :⟺ E = Σ Pₖ` where each `Pₖ` is a fundamental product and no `Pₖ⊆Pₗ` for `k≠l`. Not unique.
- **CSOP (complete SOP)**: additionally every summand contains exactly the same unknowns as `Ukn(E)`. **Unique**, so it's used to test equality: `CSOP(E₁)=CSOP(E₂) ⟺ E₁=E₂`.

### Algorithms (exact exam format required — see below)
**Producing SOP(E)**:
1. Use De Morgan's + involution to push complementation down to individual unknowns.
2. Multiply out factors using a **tree** (show every branch), reducing each node with commutativity/idempotence/complementation, literals ordered alphabetically within each term.
3. Use absorption/identity to reduce the sum.
4. Order literals alphabetically within terms, and terms lexicographically among summands.

**Producing CSOP(E) from SOP(E)**:
1. For each summand missing an unknown `x_k`, insert `(1)` in its place.
2. Replace each inserted `1` with `(x_k + x_k')`.
3. Multiply out via tree.
4. Keep only the first instance of each repeated fundamental product.
5. Order summands lexicographically.

**All multiplication of sums-of-products must be shown via an explicit tree** — this is stated repeatedly and bluntly: "Any departure from correct format will lead to a score of 0." A full worked tree example (multiplying `(xy'+z)(xy+yz'+xz)`) appears in the source PDF and should be used as the template for exam answers.

### Prime implicants and minimal SOP (MSOP)
- `E_L ≔ ν(MSLtr(E))` (total literal count); `E_S ≔ ν(Smnd(E))` (summand count).
- `Smplr(E,F) :⟺ ((E_L<F_L)∧(E_S≤F_S)) ∨ ((E_L≤F_L)∧(E_S<F_S))` — E is simpler than F.
- `Mnml(E) :⟺` no equivalent F is simpler than E (E is minimal SOP).
- **Prime implicant**: `PI(P,E) :⟺ (P+E=E) ∧ (∀Q⊊P, Q+E≠E)` — P absorbs into E, but no larger sub-product of P does. `PI(E)` = set of all prime implicants of E.
- **MSOP form**: E expressed as a sum of prime implicants, none of which is redundant (removable while the sum still equals E). Not unique — multiple valid MSOPs can exist for the same E.
- **Consensus** of two fundamental products P, Q (where at least one has length >1, and exactly one variable appears complemented in one and uncomplemented in the other): `Cns(P,Q)` = the reduced word from juxtaposing P,Q and deleting that variable/its complement in both forms. Law: `P+Q+Cns(P,Q) = P+Q`. If zero or ≥2 variables satisfy the complement-mismatch condition, `Cns(P,Q)` does not exist (written `C̶n̶s̶(P,Q)`).

**Consensus method for all prime implicants**:
1. Delete any fundamental product that includes (absorbs into) another.
2. Add any consensus `Cns(Pₖ,Pₗ)` not already included by another summand.
3. Repeat until neither step applies. (You must explicitly verify and show that no step applies, to prove the algorithm has terminated.)

**Finding MSOP from the prime-implicant sum**: express each prime implicant as its own CSOP, then delete redundant prime implicants one at a time (those whose summands all reappear among the other prime implicants' CSOP expansions) — a bookkeeping scheme with row/column indices `(mn)` tracks which summands repeat across which prime implicant. Multiple valid deletions can yield multiple distinct MSOPs of the same E.

## Important Formulas / Definitions
Full three-column law correspondence table (BA axioms/theorems ↔ PC ↔ Sets) is reproduced in `2026-07-08-logic.md` and `2026-07-08-sets.md` — same table, three languages.

## Summary
Boolean Algebra packages the same laws as Sets and Propositional Calculus into ordinary-algebra notation (`+, ·, '`), making some proofs easier if translated there first. The bulk of exam-relevant material is mechanical but format-strict: SOP/CSOP normal forms (used to test equivalence uniquely), and the consensus method for finding all prime implicants and minimal sum-of-products forms — every multiplication must show a tree, every step must cite its justifying law, and skipping steps costs all credit. This chapter closes the loop on the "three languages" theme that runs through Sets, Logic, and Boolean Algebra.
