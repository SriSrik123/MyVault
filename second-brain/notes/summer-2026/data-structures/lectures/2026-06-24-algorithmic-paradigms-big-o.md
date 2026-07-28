# Algorithmic Paradigms & Big-O Notation — CS260
**Date:** 2026-06-24
**Source:** CS260 Day 2 handwritten notes

## Overview
Day 2 covered when to use linear vs binary search, introduced algorithmic paradigms (brute force and divide & conquer), and dove into time complexity analysis including Big-O notation and asymptotic bounds.

## Key Concepts

### Search Algorithms
- **Linear search**: use when data is unsorted or in a linked list
- **Binary search**: cannot be used on a linked list — there's no way to jump to the middle

### Algorithmic Paradigms
- **Brute force** → try all possible solutions
- **Divide and conquer** → recursively break down the problem until you can solve it
  - Example: `foo(5)` generates pairs (0,0)→(0,4), (1,1)→(1,4), (2,2)→(2,4), ... until (4,4)

### What Makes an Algorithm Work Well?
- Works correctly
- Uses processing efficiently ← most important
- Uses memory efficiently
- Uses network efficiently

**What to measure:** input size, compiler quality, **time complexity** (most important)

Efficiency depends on the goal — like walking vs bike vs car vs plane vs rocket; it depends on the distance.

### Runtime Notation
- $T(n)$ = time it takes to run an algorithm on input of size $n$, in terms of number of operations
- $T$ = running time of algorithm X
- $n$ = size/number of inputs

### Asymptotic Notation
| Notation | Meaning |
|----------|---------|
| $T(n) = O(g(n))$ | $g(n)$ is upper bound |
| $T(n) = \Omega(g(n))$ | $g(n)$ is lower bound |
| $T(n) = \Theta(g(n))$ | $g(n)$ is tight bound |
| $T(n) = \omega(g(n))$ | $g(n)$ is loose upper bound |
| $T(n) = o(g(n))$ | $g(n)$ is loose lower bound |

### Calculating Asymptotic Bounds
- Upper bound: $\lim_{n \to \infty} \frac{g(n)}{T(n)} = \infty$
- Lower bound: $\lim_{n \to \infty} \frac{g(n)}{T(n)} = 0$

**Example:** $g(n) = 2n^2 + 3n + 7$, $f(n) = 5n + 30$
$\lim_{n \to \infty} \frac{g(n)}{f(n)} = \infty$ → so $f(n)$ is upper bounded by $g(n)$

## Important Formulas / Definitions

### Big-O Formal Definition
$T(n) = O(g(n))$ if there exist positive constants $c$ and $n_0$ such that $0 \leq T(n) \leq cg(n)$ for all $n \geq n_0$

**Example — Prove $3n^3 + 2n^2 = O(n^3)$:**
Need: $0 \leq 3n^3 + 2n^2 \leq cn^3$ for all $n \geq n_0$

- Try $c=1, n_0=1$: $3n^3 + 2n^2 \leq n^3$ → $2n^2(n+1) \leq 0$ → not possible
- Try $c=4, n_0=2$: $3n^3 + 2n^2 \leq 4n^3$ → $2n^2 \leq n^3$ for all $n \geq 2$ ✓ **Proven**

Also: $3n^3 + 2n^2$ is $O(n^{200})$ → loose upper bound (will be higher/equal at some point)

### Sum Formula
$1 + 2 + 3 + \ldots + n = \frac{n(n+1)}{2}$

### Rules of Thumb
- Only keep the fastest growing term and drop coefficients
- Example: $f(n) = 3n^3 + 2n \Rightarrow O(n^3)$
- Assume worst case

## Summary
Moral: **KNOW YOUR TOOL SET.** Time complexity (Big-O) is the primary measure of algorithm efficiency. Keep only the dominant term, drop constants, and always analyze worst case.
