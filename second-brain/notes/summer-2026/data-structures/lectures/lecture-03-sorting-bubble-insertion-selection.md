# Week 2 Lecture 1 — Sorting: Bubble, Insertion, Selection
**Date:** 6/30/26  
**Course:** CS-260 Data Structures

---

## Overview

Sorting covered today: **Bubble, Insertion, Selection** — all slower O(n²) algorithms.

- Searching is the main benefit of sorting data
- There is no perfect sorting algorithm
- Interviews may not ask you to sort directly, but sorting often helps you solve problems faster

---

## How Sorting Works: Pairwise Comparison

The heart of sorting is **compare then switch**:
- **True:** elements are in correct order → leave them
- **False:** elements are in wrong order → swap them

### Extra Info = Specialized Algorithms
If you know something extra about the data, you can sort faster:
- Sort numbers 0–50 with **no duplicates** → just place each number at its respective index
- Sort an array of non-negative numbers with duplicates up to 10³ → use **counting sort**

---

## Comparison-Based Sorting

Works on Array A of size n. Operators used: `<`, `>`

**Swapping** requires a temp variable → costs **3 memory operations** per swap:
```
temp = A[i]      // 1
A[i] = A[j]     // 2
A[j] = temp     // 3
```

- **Best case:** Already sorted list → 0 swaps
- **Worst case:** Inversely sorted list → swap every time

---

## Bubble Sort

**Idea:** Let elements "float" into place. Look at two adjacent elements and swap if needed. Repeat until sorted.

**Optimization:** After each outer loop pass, the largest unsorted element bubbles to the top — so we can decrement `stop` each pass.

```cpp
void BubbleSort(int* A, int n) {
    bool swapped = 1;
    int stop = n;
    while (swapped == 1) {
        swapped = 0;
        for (int i = 1; i < stop; i++) {
            if (A[i - 1] > A[i]) {
                swap(A, i-1, i);
                swapped = 1;
            }
        }
        stop = stop - 1;
    }
}
```

**Example walkthrough** (worst case: `5 4 3 2 1`):
```
5 4 3 2 1  →  4 3 2 1 | 5   (4 ops = n-1, costs 3 per swap)
4 3 2 1 5  →  3 2 1 | 4 5   (3 ops = 3(n-2))
...
```

**Cost analysis:**
- Memory writes: 3n(n+1)/2
- Comparisons: n(n-1)/2

**Memory need:** O(1) — only 4 extra variables:
| Variable | Space |
|----------|-------|
| Size of array | O(1) |
| Counter `i` | O(1) |
| `swapped` var | O(1) |
| `temp` var | O(1) |

---

## Insertion Sort

**Goal:** Minimize number of swaps → trade memory for time.

**Key idea:** Instead of swapping, **shift** elements and slide the target into place.
- **No temp variable needed** → saves memory
- Shift = **1 operation** per shift (vs swap = 3 ops)
- Same number of comparisons as Bubble Sort

```cpp
void InsertionSort(int* A, int n) {
    for (int i = 0; i < n; i++) {
        int key = A[i];
        for (int j = i; j > 0; j--) {
            if (A[j - 1] > key)
                A[j] = A[j-1];   // shift right to open space
            else
                break;
        }
        A[j] = key;   // place key in opened spot
    }
}
```

- Outer loop stores next unsorted number as `key`, then places it in the new space opened by the inner loop
- Inner loop shifts elements in the sorted region to make room

**Runtime:** O(n²) | **Memory writes:** n(n-1)/2 → **3× fewer** memory operations than Bubble Sort

---

## Selection Sort

**Idea:** Split list into sorted vs unsorted halves. Repeatedly pick the **minimum** of the unsorted portion and move it to the sorted portion.

- **Worst case:** n-1 swaps → O(n) swaps
- Still takes O(n) to find the min each pass
- **# of comparisons is still n(n-1)/2**
- **No early termination** — always O(n²) regardless of initial order

```cpp
void SelectionSort(int* A, int n) {
    for (int i = 1; i < n; i++) {
        minIndex = i;
        for (int j = i+1; j < n; j++) {
            if (A[j] < A[minIndex])
                minIndex = j;
        }
        swap(A, i, minIndex);   // put min in its proper place
    }
}
```

The heart of the algorithm is **finding the minimum**.

`find_min` is always **O(n)** runtime.

---

## Algorithm Comparison

All three have the **same worst-case runtime: O(n²)**, but actual performance differs:

|  | Best Case Comparisons | Best Case Memory Writes | Worst Case Comparisons | Worst Case Memory Writes |
|---|---|---|---|---|
| **Bubble Sort** | n | 0 | n²/2 | 3n²/2 |
| **Insertion Sort** | n | 2n | n²/2 | ~2n |
| **Selection Sort** | n²/2 | 3n | n²/2 | n(n-1)/2 |

**Key takeaways:**
- **Insertion vs Bubble:** Insertion wins on memory writes — shifting instead of repetitive swapping
- **Selection vs Insertion:** Selection wins on worst-case memory writes — single swap of the min instead of shifting
- Selection Sort has **no early termination** — always O(n²) even on an already-sorted list
