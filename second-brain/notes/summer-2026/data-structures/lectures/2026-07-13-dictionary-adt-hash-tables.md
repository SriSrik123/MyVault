# Dictionary ADT & Hash Tables — CS260 (Day 7)
**Date:** 2026-07-13
**Source:** CS260 day 7.pdf (handwritten + slides)

## Overview
Covered the Dictionary ADT (key-value pairs) and its array-based implementations, then moved into hash tables as a faster alternative, including hash functions, collisions, and open hashing (separate chaining) with runtime analysis.

## Key Concepts

### Dictionary ADT
- Stores key-value pairs, e.g. (StudentID, Name) — key: StudentID, value: Name.
- Can be implemented with arrays (unsorted or sorted).

**Unsorted array runtimes:**
- `insert(x)` → O(n) — must search first since no duplicates allowed
- `isMember(x)` → O(n) — linear search
- `delete(x)` → O(n) — search + shift

**Sorted array runtimes:**
- `insert(x)` → O(n) — search/shift
- `isMember(x)` → O(log n) — binary search
- `delete(x)` → O(n) — remove then shift

Question raised: can we do better? → leads to hash tables.

### Hash Tables
- A hash table is simply an array of size N.
- A hash function takes two inputs: array size and a key, and outputs the exact location where the value is stored.
- Dictionaries can be efficiently implemented using hashing + an array.

### Hashing Strings
- Every character in a string maps to a number (ASCII).
- Example algorithm (`hashString`): iterate over characters, accumulate `total = total*101 + charValue`, then return `total % N`.
- The constant 101 was found experimentally ("the magic number 101").
- Example: hashing "abc" with N=100 → total = 100948894 → `% 100` = 94.

### Collisions
- A collision occurs when the hash function returns the same index for two unique keys.
- Good hash functions with even distribution reduce collisions, but collisions become unavoidable past a certain point (pigeonhole principle).

### Handling Collisions — Open Hash Tables (Separate Chaining)
- Each array position stores a linked list.
- All elements that collide at the same index are stored together in that list.
- Struct: `OpenHashTable` has `size` and a `Node **table` (array of linked list heads), initialized to all NULL.

**Operations:**
- **Insert:** compute hash position, walk the list checking for existing key (no duplicates allowed), then prepend/append new node.
- **isMember:** compute hash position, walk the list comparing keys; return 1 if found, 0 otherwise.
- **Delete:** same search pattern as isMember, then unlink the node.

### Open Hash Table Runtime
- Collision rate R = 1/S (where S = table size), assuming a good hash function.
- With N elements inserted: `insert`, `isMember`, `delete` are all O(N·R) = O(N/S).
- **Load Factor** = N / S (elements / table size) — measures how full the table is. Higher load factor → more collisions → slower performance.
- Example: table size S=100, N=2000 elements inserted, ideal even distribution → average linked list length = 2000/100 = 20.
- If table size is chosen as S = N/A for constant A, then insert/member/delete all become O(A) — i.e., constant time on average, given a good size-to-elements ratio.

## Summary
Hash tables improve on plain sorted/unsorted array dictionaries by using a hash function to jump near-directly to a key's storage location. Collisions are inevitable but manageable via separate chaining (linked lists per bucket); keeping the load factor (N/S) low and choosing table size proportional to N keeps insert/isMember/delete close to constant time on average.
