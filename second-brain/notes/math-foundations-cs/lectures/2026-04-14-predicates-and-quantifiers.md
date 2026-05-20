# Predicates and Quantifiers — CS-270
**Date:** 2026-04-14
**Source:** https://logic.boady.net/content/002_fol/001_predicates.html

## Overview
Predicates are Boolean-returning functions used as the foundation of first-order logic. This lecture covers how predicates work, the sets they operate over, and the two main quantifiers (∀ and ∃) that allow statements about collections of values.

## Key Concepts

### Predicates
- A **predicate** is a function that takes n ≥ 0 input arguments and returns a Boolean value.
- Common built-in predicates: comparison operators `>`, `≥`, `<`, `≤`, `≡`, `≠`
- Custom predicates can be defined using logical operators and existing predicates.
- Example: `positiveProduct(x, y)` — returns true if the product of x and y is positive.
  - True when both are positive, or both are negative (negatives cancel).

### Sets vs. Lists
| | Sets | Lists |
|---|---|---|
| Notation | `{,}` | `[,]` |
| Order | Unordered | Ordered |
| Duplicates | No | Yes |

**Standard mathematical sets:**
- ℕ — Natural numbers
- ℤ — Integers
- ℚ — Rational numbers
- ℝ — Real numbers
- ℂ — Complex numbers

- **Membership operator**: `∈` tests whether a value belongs to a collection (e.g., `5 ∈ ℕ`)

## Important Formulas / Definitions

### For All (∀)
- Tests whether a predicate holds for **every** element in a collection.
- Equivalent to a conjunction (AND) of all cases.
- **One false value makes the entire statement false.**
- Example: `∀x ∈ ℕ, x ≥ 0`

### There Exists (∃)
- Tests whether **at least one** element satisfies a predicate.
- Equivalent to a disjunction (OR) of all cases.
- **One true value makes the entire statement true.**
- Example: `∃x ∈ ℤ, x < 0`

> Both quantifiers support short-circuit evaluation in implementation.

## Summary
Predicates act as building blocks for logical statements about values. Quantifiers (∀ and ∃) allow us to express properties over entire collections. Understanding these is foundational for writing and reading proofs in discrete math and formal logic.
