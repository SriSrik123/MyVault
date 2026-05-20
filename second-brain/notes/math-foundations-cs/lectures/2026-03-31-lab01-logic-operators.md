# Lab 01: Logic Operators & Conditionals — CS-270
**Date:** 2026-03-31
**Source:** cs270lab1

## Overview
This lab session (slides by Prof. Mark Boady) reviewed the five core propositional logic operators—AND, OR, NOT, Bi-Conditional, and Conditional—and connected them to programming constructs in Python. The lab included hands-on exercises applying conditional logic to real-world scenarios such as card games and age-verification.

## Key Concepts

### Conjunction (AND) — A ∧ B
- True **only** when both A and B are true.
- In code: `if A and B:`

### Disjunction (OR) — A ∨ B
- True when **at least one** of A or B is true.
- In code: `if A or B:`

### Negation (NOT) — ¬A
- Flips the truth value: True becomes False, False becomes True.
- In code: `not A`

### Bi-Conditional (EQUALS) — A ↔ B
- True when both sides have the **same** truth value (both true or both false).
- In code: `A == B`

### Conditional (IF/THEN) — A ⟹ B
- "If A is true, then B must be true."
- The conditional is **false only** when A is True and B is False (the "broken promise").
- When A is False, the conditional is vacuously True—no promise is made.
- Key distinction: a conditional is **not** cause-and-effect; it is a logical relationship.

**Truth table for A ⟹ B:**

| A | B | A ⟹ B |
|---|---|--------|
| T | T | T |
| T | F | **F** (promise broken) |
| F | T | T |
| F | F | T |

### Programming Connection
```python
# Example: (x == 7) ⟹ (y == 2)
y = 2
if x == 7:
    bunch of code  # if x==7, this runs → y=2
print(y)
```
- If x=7 and y=2 at print time → conditional **True**
- If x=7 and y≠2 at print time → conditional **False** (code is broken)
- If x≠7, y could be anything → conditional is **True** (no promise was made)

## Important Formulas / Definitions

| Operator | Symbol | Read As | False When |
|----------|--------|---------|-----------|
| AND | ∧ | "A and B" | Either side is false |
| OR | ∨ | "A or B" | Both sides false |
| NOT | ¬ | "not A" | A is true |
| Bi-Conditional | ↔ | "A equals B" | Sides differ |
| Conditional | ⟹ | "if A then B" | A=True, B=False only |

## Summary
Propositional logic provides the mathematical foundation for programming conditionals and formal reasoning. The conditional operator (⟹) is the most nuanced: it is only violated when its premise is true but its conclusion is false. Lab exercises applied these operators to card-game and law-enforcement scenarios, reinforcing the distinction between a logical relationship and a causal one.


---

## Related Notes

[[second-brain/notes/math-foundations-cs/syllabus|CS-270 Syllabus]]  [[2026-03-31-lecture-01-formal-logic-operators|Lecture Notes (same day)]]  [[2026-03-31-natural-deduction-intro|Next: Natural Deduction]]