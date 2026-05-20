# Invalid Arguments — CS-270
**Date:** 2026-04-14
**Source:** https://logic.boady.net/content/001_boolean/005_invalid.html

## Overview
An argument is **invalid** when it's possible for all premises to be true while the conclusion is false. This is the opposite of validity, which requires that true premises always guarantee a true conclusion.

## Key Definition
> An argument is invalid if: the premises can be true **and** the conclusion can be false at the same time.

## How to Prove Invalidity: The Counterexample Method
- Find **one** variable assignment where all premises are true but the conclusion is false.
- You only need **one** counterexample — invalidity doesn't require exhaustive checking.
- Proving **validity**, by contrast, requires exhaustive formal proof (no counterexample can exist).

## Examples

### Example 1: A ∨ B ∴ A ∧ B
| Variable | Value |
|----------|-------|
| A | True |
| B | False |

- Premise `A ∨ B` = True ✓
- Conclusion `A ∧ B` = False ✗
- **Invalid** — disjunction (OR) does not guarantee conjunction (AND).

### Example 2: A → B, B ∴ A  (Affirming the Consequent)
| Variable | Value |
|----------|-------|
| A | False |
| B | True |

- Premise `A → B` = True ✓  (False → True is True)
- Premise `B` = True ✓
- Conclusion `A` = False ✗
- **Invalid** — this is the classic *affirming the consequent* fallacy.

### Example 3: A, A → B ∴ ¬B
| Variable | Value |
|----------|-------|
| A | True |
| B | True |

- Premise `A` = True ✓
- Premise `A → B` = True ✓
- Conclusion `¬B` = False ✗
- **Invalid** — demonstrates an incorrect inference pattern.

## Key Asymmetry
| | Validity | Invalidity |
|---|---|---|
| What's required | Exhaustive proof (no counterexample possible) | Just one counterexample |
| Difficulty | Harder — must cover all cases | Easier — find one failing case |

## Summary
To disprove an argument, just find one assignment of truth values that makes all premises true and the conclusion false. This is much easier than proving validity, which requires showing the argument holds in every possible case.
