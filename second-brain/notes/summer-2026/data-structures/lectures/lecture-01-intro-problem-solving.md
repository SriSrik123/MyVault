# Lecture 1 — Intro to Problem Solving
**Date:** 6/22/26  
**Course:** CS-260 Data Structures

---

## Algorithm vs Program

| Algorithm | Program |
|-----------|---------|
| Not tied to a language | Tied to a language |
| Formal method / instructions (conceptual) | Implementing the actual solution to solve the problem |

---

## What We Care About

- **Does it work?**
- **Is it efficient?**

---

## Peak Finding Problem

A **peak price** is when it is **NOT smaller than its neighbours**.

- **Inputs:** list of date, time, price
- **Output:** the peak price
- **Type:** Search
- **Representation:** Sliding window
- **How to solve:** Search through a list
- **Time:** O(n)

→ Search sorted arrays

**Correct vs Efficient Algorithm**

- **Correct** = it will find the value
- **Linear search** → look page one by one
- **Binary search** → look at middle and eliminate 50% of values

---

## Best vs Worst Case

- **Best case:** you find it on the first search
- **Worst case:** you look through everything and it's either last or not there

> ⭐ We are interested in the **worst case** for our algorithm.

**Binary Search → O(log n)**
