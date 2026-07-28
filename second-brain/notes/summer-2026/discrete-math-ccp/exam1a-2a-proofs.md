# Exam 1A — Problem 2a proofs (to hand-copy)

Format notes before copying:
- Every ⟺ lines up in one column on the left, ~5mm gap to the expressions.
- Write proofs on the work page that follows p. 109 (properly numbered), labeled 2a.i … 2a.vi, separated by ruler-drawn lines. Put the one-sentence reason on the "Why?" line only if it fits in your normal handwriting.
- Membership in a pair set unfolds as: x ∈ {a, b} ⟺ (x = a) ∨ (x = b). Subset unfolds as: X ⊆ Y ⟺ ∀x ∈ X (x ∈ Y).
- Verify one proof against the Solved Exams on Canvas before copying all six — the instructor requires the notes' format with no variations.

---

## 2a.i   1 ∈ {0, {1}}   — circle: N, Pf

SPf:
      1 ∈ {0, {1}}
⟺  (1 = 0) ∨ (1 = {1})
⟺  F ∨ F
⟺  F
1 = 0 is false because 0 ≠ 1. 1 = {1} is false because 1 is a number and {1} is a set.
∴ 1 ∉ {0, {1}}.   EPf

Why? line: 1 is neither 0 nor {1}; 1 is a number and {1} is a set.

## 2a.ii   {1} ∈ {0, {1}}   — circle: Y, Pf

SPf:
      {1} ∈ {0, {1}}
⟺  ({1} = 0) ∨ ({1} = {1})
⟺  F ∨ T
⟺  T
{1} = 0 is false because {1} is a set and 0 is a number. {1} = {1} is true because every object is equal to itself.
∴ {1} ∈ {0, {1}}.   EPf

Why? line: {1} is the second listed element of the set.

## 2a.iii   1 ⊆ {0, {1}}   — "does not make sense"

Why? line (complete sentences, no contraction):
This does not make sense. 1 is a number, not a set, and X ⊆ Y is defined only when X and Y are sets.

(No SPf/EPf chain — a statement that does not make sense is neither proved nor refuted. Check the Solved Exam for whether N gets circled here or nothing is circled; the exam instructions only say "does not make sense" is a possible answer.)

## 2a.iv   {0} ⊆ {0, {1}}   — circle: Y, Pf

SPf:
      {0} ⊆ {0, {1}}
⟺  ∀x ∈ {0} (x ∈ {0, {1}})
⟺  0 ∈ {0, {1}}
⟺  (0 = 0) ∨ (0 = {1})
⟺  T ∨ F
⟺  T
The only element of {0} is 0, and 0 = 0 is true because every object is equal to itself.
∴ {0} ⊆ {0, {1}}.   EPf

Why? line: the only element of {0} is 0, and 0 ∈ {0, {1}}.

## 2a.v   {{0}} ∈ {0, {1}}   — circle: N, Pf

SPf:
      {{0}} ∈ {0, {1}}
⟺  ({{0}} = 0) ∨ ({{0}} = {1})
⟺  F ∨ F
⟺  F
{{0}} = 0 is false because {{0}} is a set and 0 is a number. {{0}} = {1} is false because the only element of {{0}} is {0}, the only element of {1} is 1, and {0} ≠ 1 because {0} is a set and 1 is a number.
∴ {{0}} ∉ {0, {1}}.   EPf

Why? line: {{0}} is neither 0 nor {1}.

## 2a.vi   {{0}} ⊆ {0, {1}}   — circle: N, Pf

SPf:
      {{0}} ⊆ {0, {1}}
⟺  ∀x ∈ {{0}} (x ∈ {0, {1}})
⟺  {0} ∈ {0, {1}}
⟺  ({0} = 0) ∨ ({0} = {1})
⟺  F ∨ F
⟺  F
The only element of {{0}} is {0}. {0} = 0 is false because {0} is a set and 0 is a number. {0} = {1} is false because 0 ∈ {0} and 0 ∉ {1}, since 0 ≠ 1.
∴ ¬({{0}} ⊆ {0, {1}}).   EPf

Why? line: the only element of {{0}} is {0}, and {0} ∉ {0, {1}}.
