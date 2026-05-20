# Proof by Contradiction — CS-270
**Date:** 2026-04-14
**Source:** https://logic.boady.net/content/001_boolean/003_contradictions.html

## Overview
Proof by contradiction exploits the principle that every statement must be either true or false. Instead of proving something is true directly, you show it *cannot* be false — thereby establishing its truth indirectly.

## Key Principle
If assuming ¬P leads to a contradiction (⊥), then P must be true.

## The Four Deduction Rules

### 1. Negative Elimination (¬E)
- Premises A and ¬A cannot both be true simultaneously.
- Combining them produces a contradiction: `A, ¬A ⊢ ⊥`
- Foundation for all other contradiction rules.

### 2. Negative Introduction (¬I)
- If a subproof starting with assumption P ends in contradiction, then ¬P is provable.
- Form: assume P → derive ⊥ → conclude ¬P

### 3. Indirect Proof (IP)
- Assume ¬P, derive a contradiction, conclude P.
- Effectively removes the negation from the assumption.
- Form: assume ¬P → derive ⊥ → conclude P

### 4. Principle of Explosion
- Once a contradiction exists inside a subproof, **any** statement can be derived within it.
- Useful for disjunction elimination when one branch leads to impossibility.
- Formally: `⊥ ⊢ Q` (for any Q)

## Classic Example: The Halting Problem
Alan Turing (1937) used proof by contradiction to show no program can detect all infinite loops:
- Assume a `codeHalts()` detector exists.
- Construct a `breakCode()` function that does the *opposite* of what `codeHalts()` predicts.
- This leads to a logical contradiction — so the detector cannot exist.
- A foundational result in computability theory.

## Summary
Proof by contradiction is a powerful proof technique. The key rules are ¬E (combining a statement and its negation gives ⊥), ¬I (subproof ending in ⊥ lets you conclude the negation of the assumption), IP (assume the negation, derive ⊥, conclude the original), and Explosion (⊥ justifies anything within that branch).
