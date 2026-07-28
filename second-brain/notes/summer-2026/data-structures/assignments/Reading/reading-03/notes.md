# CS260 Reading 3 (Week 3)
Worth 5 pts, graded on effort
File: [[reading-03.pdf|Reading 3 PDF]]

## What I need to do
- read 12.1, 12.2, 12.3
- take notes
- answer the 2 questions
- upload notes + answers pic/pdf to gradescope

## Notes

### 12.1 Supported Operations
- hash table = a dictionary
- 3 ops: Lookup (find by key), Insert (add), Delete (remove by key)
- all 3 typically O(1) time... but only if table is set up right + data isn't pathological (that's what the little asterisk means in the book)
- space used = O(|S|) (proportional to # objects actually stored), way better than a giant array sized for the whole universe of possible keys
- rule of thumb: fast lookups + set of objects keeps changing = use a hash table

### 12.2 Applications
- de-duplication
  - stream of data comes in one at a time
  - for each new key: Lookup first, if not found then Insert
  - end result: exactly one entry per distinct key
  - examples: distinct IPs hitting a site, distinct visitors, big log files
- symbol tables in compilers (tracking variable/function names) — this is literally why hash tables were invented back in the 1950s
- 2-SUM problem
  - given array + target t, is there x + y = t?
  - brute force = O(n^2)
  - better way: throw all numbers into a hash table, then for each x check if (t - x) is in the table → O(n) instead
- basically: anytime you're doing repeated lookups, hash table should come to mind

### 12.3 Implementation — High Level Ideas
- universe U = all possible keys (huge)
- set S = keys actually being stored (small compared to U)
- two straightforward but bad solutions:
  - big array sized to |U| → fast but insane amount of wasted space
  - linked list → good space but slow O(|S|) lookups
  - hash table = best of both worlds, O(|S|) space AND ~O(1) ops

- hash function h: maps every key in U to a position {0, 1, ..., n-1} in the array
- n is usually picked to be roughly proportional to |S| (like 2x)

- collisions
  - when two different keys hash to the same spot
  - literally unavoidable once |U| > n (pigeonhole principle)
  - even worse than that because of the birthday paradox — collisions start showing up way sooner than you'd think, even when the table is mostly empty
  - example from book: n = 10,000 slots, but inserting just 200 random objects is already likely to cause a collision

- collision resolution, two main ways:
  1. chaining
     - each bucket holds a linked list
     - insert = O(1) (just stick it at the front)
     - lookup/delete = O(length of that bucket's list)
     - buckets need to stay short for this to actually be fast
  2. open addressing
     - each slot holds 0 or 1 objects (no lists)
     - each key gets a probe sequence — an ordered list of positions to try
     - insert = walk the sequence, drop it in first empty slot
     - lookup = walk the sequence until you find the key or hit an empty slot
     - linear probing = simplest version, just try h(k), h(k)+1, h(k)+2... wrapping around
     - double hashing = use 2 hash functions, one for start position, one for the step/offset between tries

- what makes a hash function good
  - cheap to evaluate (ideally O(1))
  - cheap to store (ideally O(1) memory, not some huge lookup structure)
  - spreads out normal/non-pathological data pretty evenly across slots (mimics what a truly random function would do)
  - bad example: h(k) = 0 for every key → everything collides, basically turns the table into one giant linked list
  - simple real example: h(k) = k mod n
    - cheap, easy, but breaks if keys share patterns in their low digits (like everything ending in 000)
  - better: h(k) = (ak + b) mod n — scrambles the key first, harder to accidentally break

- pathological data sets
  - for literally any hash function you pick, someone could construct a nasty data set that makes everything collide
  - so hash tables can't guarantee O(1) for every possible input — only for "non-pathological" (realistic/normal) data
  - this is basically why every running-time claim in this chapter has that little asterisk next to it

## Answers

**Q1 (notes):** see above — that's the reading notes.

**Q2:**

(a) what makes a hash function "good"?
- spreads keys around pretty evenly/unpredictably so no one bucket gets overloaded
- cheap to compute and cheap to store
- keeps lookup/insert/delete close to O(1) for normal data

(b) what are collisions?
- when two different keys hash to the same slot/position in the table

(c) two main collision resolution methods:
- chaining — stick a linked list in every bucket, colliding keys just get added to that bucket's list
- open addressing — no lists, each key has a probe sequence of positions to try in order until it finds an empty one (or finds the key, for lookup)

(d) U = {xy | x in {a,b,c,d,e}, y in {1,2,3,4,5}}
- |U| = 5 * 5 = 25 = n
- sqrt(n) = 5
- hash function idea: h(xy) = index of x (a=0, b=1, c=2, d=3, e=4)
- only uses 5 slots total, each slot ends up with at most 5 keys in it (one per y value)
- since 5 = sqrt(25) = sqrt(n), this fits the sqrt(n) slot requirement

## Status
- [ ] not submitted yet — no exact due date printed on the sheet, double check gradescope
