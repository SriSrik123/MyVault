# First Order Logic (FOL) — CS-270
**Date:** 2026-04-14
**Source:** https://logic.boady.net/content/002_fol/002_fol.html

## Overview
First Order Logic (FOL) extends Boolean logic with predicates and quantifiers to reason about objects and their properties. It is "first order" because variables are inputs to functions — not functions themselves (unlike higher-order logic).

## Key Concepts

### What Makes It "First Order"
- Only **variables** are inputs to functions.
- Higher-order logic allows functions to accept other functions as inputs.

### Compressed Notation (Abbreviation Rules)
To simplify proofs, FOL uses shorthand:
- Drop domain specification if all variables share the same set
- Use single lowercase letters for variables
- Use single uppercase letters for predicates/functions
- Remove parentheses and commas from predicates

**Example:**  
`∀x(Even(x) ∨ ¬Even(x))` → `∀x(Ex ∨ ¬Ex)`

### Bound vs. Free Variables
- **Bound variable**: connected to a quantifier (e.g., `x` in `∀x P(x)`)
- **Free variable**: unbound — can be assigned any value
- Example in a GCD predicate: `x` is bound to `∀`, while `a`, `b`, `g` are free

## Important Formulas / Definitions

### Quantifier Rules

**For All (∀):**
- **Elimination (∀E)**: If `∀x P(x)` is true, then `P(c)` is true for any specific constant `c`
- **Introduction (∀I)**: If a proof holds for an arbitrary constant with no special assumptions, the result holds universally

**There Exists (∃):**
- **Introduction (∃I)**: If `P(c)` is true for some specific `c`, then `∃x P(x)` is true
- **Elimination (∃E)**: Requires a subproof — assume the existing value exists, then derive conclusions from it

### De Morgan's Laws for Quantifiers
$$\neg \forall x \, P(x) \iff \exists x \, \neg P(x)$$
$$\neg \exists x \, P(x) \iff \forall x \, \neg P(x)$$

These are biconditional (work in both directions).

### Interpretations
- An **interpretation** assigns meaning to the symbols in a logical expression.
- A statement may be true under one interpretation and false under another.
- **Validity** requires truth across *all* possible interpretations.

### Validity vs. Invalidity
- To prove **invalidity**: provide one counterexample model where premises are true but the conclusion is false.
- To prove **validity**: requires an exhaustive formal proof.

## Summary
FOL provides the formal machinery to write precise mathematical statements using variables, predicates, quantifiers, and inference rules. The key skills are applying quantifier elimination/introduction correctly and using De Morgan's laws to negate quantified statements.
