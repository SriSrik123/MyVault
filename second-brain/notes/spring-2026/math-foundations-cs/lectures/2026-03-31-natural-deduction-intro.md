# Natural Deduction — Introduction — CS-270
**Date:** 2026-03-31
**Source:** In-class notes, Lecture 1 (continuation)

## Overview
Natural deduction is a proof system where conclusions follow from premises using a fixed set of inference rules. Unlike truth tables (which enumerate all possibilities), natural deduction constructs a *proof* — a step-by-step derivation that shows *why* a conclusion must be true. Each step cites the rule used and the line numbers it applies to.

Key notation: **∴** (therefore), premises are assumed true, the conclusion must be derived.

---

## Key Inference Rules

### Conjunction Introduction (∧I) — "AND Introduction"
If you have both A and B separately, you can combine them into A∧B.

```
R , D ∴ R∧D

1. R        Premise
2. D        Premise
3. R∧D      ∧I 1,2   (order matters for which goes left/right)
4. D∧R      ∧I 2,1
```

### Conjunction Elimination (∧E) — "AND Elimination"
From a conjunction A∧B, you can extract either component individually.

```
C∧R ∴ C  and  C∧R ∴ R

1. C∧R      Premise
2. C        ∧E 1
3. R        ∧E 1
```

Works on nested conjunctions too:
```
1. (X∧Y) ∧ Z
2. (X∧Y)    ∧E 1
3. Z        ∧E 1
```

### Disjunction Introduction (∨I) — "OR Introduction"
If A is true, then A∨(anything) is true — you can add any second disjunct.

```
R ∴ R∨F    (R is true → R∨F is true)
R ∴ F∨R    (can put R on either side)
```

### Implication Elimination (→E) — "Modus Ponens"
If A→B is true and A is true, then B must be true. (The classic "if/then" rule.)

```
A→B, A ∴ B

1. A→B      Premise
2. A        Premise
3. B        →E 1,2
```

### Implication Introduction (→I) — "Conditional Proof"
To prove A→B, temporarily *assume* A, derive B, then discharge the assumption. The assumption lines are boxed/indented and the result is A→B.

```
1. S→¬C     Premise
2. ¬C→L     Premise
[3. S]      assume          ← temporary assumption
 4. ¬C      →E 1,3
 5. L       →E 2,4
6. S→L      →I 3–5         ← assumption discharged
```

---

## Worked Example — "Larry" Problem

**Given:** If Larry is sick, he doesn't come to class. If he doesn't come, he loses the course.
**Prove:** If Larry is sick, he loses the course. (S→L)

Let S = "Larry is sick", C = "Larry comes to class", L = "Larry loses the course."

```
1. S → ¬C       Premise
2. ¬C → L       Premise
[3. S]           assume
 4. ¬C           →E 1,3
 5. L            →E 2,4
6. S → L         →I 3–5
```

---

## Practice Problem — HW 1 Preview

**Prove:** (A∧B) ∧ (C∧D) ∴ (A∧C) ∧ (D∧B)

*Hint: Use ∧E to extract each letter, then ∧I to rebuild the target conjunction.*

---

## Summary

| Rule | Symbol | What it does |
|------|--------|--------------|
| Conjunction Introduction | ∧I | Combines A and B separately into A∧B |
| Conjunction Elimination | ∧E | Extracts A or B from A∧B |
| Disjunction Introduction | ∨I | Adds a disjunct: A → A∨X |
| Implication Elimination | →E | From A→B and A, concludes B (Modus Ponens) |
| Implication Introduction | →I | Proves A→B by assuming A and deriving B |

Natural deduction is mechanical once you know the rules — the key is recognizing *which rule to apply at each step* based on the shape of what you have and what you need.


---

## Related Notes

[[second-brain/notes/math-foundations-cs/syllabus|CS-270 Syllabus]]  [[2026-03-31-lecture-01-formal-logic-operators|Previous: Formal Logic Operators]]  [[2026-03-31-lab01-logic-operators|Lab 01 — Logic Operators]]