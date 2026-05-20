# Formal Logic — Operators & Conditionals — CS-270
**Date:** 2026-03-31
**Source:** CS270Day1.md (in-class notes, Lecture 1)

## Overview
First lecture of CS-270 (Mathematical Foundations in CS). Introduced the five core logical operators used in formal logic and natural deduction. Covered truth conditions for each operator and worked through three card/bar-scenario exercises to build intuition for conditionals.

## Key Concepts

**Logical Operators**

| Operator | Name | Symbol | Truth Condition |
|----------|------|--------|-----------------|
| AND | Conjunction | ∧ | True only when **both** sides are true |
| OR | Disjunction | ∨ | True when **either** side is true |
| NOT | Negation | ¬ | True when the value is **false** |
| ↔ | Biconditional ("equals") | ⟺ | True when both sides are the **same** |
| IF/THEN | Conditional | → | False **only** when antecedent is true and consequent is false |

**The Conditional (→) — the tricky one**

Think of it like a contract: the contract is only *broken* (False) when the promise is made (True antecedent) but not kept (False consequent).

Example: "If it is raining → it is cold"

| Raining | Cold | Result |
|---------|------|--------|
| T | T | ✅ True |
| T | F | ❌ False (contract broken) |
| F | T | ✅ True (vacuously — no rain, no promise) |
| F | F | ✅ True (vacuously) |

Code analogy:
```python
if x == 7:
    y = 2
print(y)
```
The print only matters *if* x is 7. If x isn't 7, the condition is vacuously satisfied.

## Important Formulas / Definitions

- **P → Q** is logically equivalent to **¬P ∨ Q** (contrapositive intuition).
- To **disprove** a conditional, you only need one counterexample: P true, Q false.
- A conditional says **nothing** about the case when the antecedent is false — those rows are automatically true.

**Card-Flip / Verification Rule:**
When checking "If [vowel] → [even number]," you only need to flip cards that could *falsify* the rule:
- Flip the vowel side (could reveal an odd number → violation).
- Flip the odd-number side (could reveal a vowel → violation).
- No need to flip consonants or even numbers — they can't break the rule.

**Worked Exercises — Key Takeaways**

*Card game (vowel → even number). Cards: 2, 3, B, E*
- **2** → No flip needed (even number can't falsify)
- **3** → Flip needed (odd number could be hiding a vowel)
- **B** → No flip needed (consonant can't falsify)
- **E** → Flip needed (vowel must have even on back)

*Bar scenario (drinking alcohol → age ≥ 21). People: 80yr w/ unknown drink, 12yr w/ unknown drink, unknown age w/ Coke, unknown age w/ Martini*
- Person 1 (80yr): No check needed — over 21
- Person 2 (12yr): Check drink — under 21, drink unknown
- Person 3 (Coke): No check needed — Coke isn't alcohol
- Person 4 (Martini): Check ID — alcohol confirmed, age unknown

## Summary
Formal logic operators form the vocabulary of mathematical proof. The conditional (→) is the most unintuitive: it is only false when a true premise leads to a false conclusion. The card-flip exercises are a great mental model — always ask "what combination of values would break this rule?" and only investigate those. These operators (∧, ∨, ¬, →, ⟺) are the building blocks for all natural deduction proofs coming in later lectures.


---

## Related Notes

[[second-brain/notes/math-foundations-cs/syllabus|CS-270 Syllabus]]  [[2026-03-31-lab01-logic-operators|Lab 01 — Logic Operators (same day)]]  [[2026-03-31-natural-deduction-intro|Next: Natural Deduction]]