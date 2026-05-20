# Racket Function Reference Sheet — CS270
**Date:** 2026-05-13
**Source:** Course reference sheet (Racket Functions.pdf)

> ⚠️ **Rule:** Functions in the "NEVER permitted" list will result in **penalties** if used. Functions in the "conditional" sections should only be used when **explicitly allowed** by the assignment.

---

## ✅ Core Functions — ALWAYS Permitted

| Function | Description | Example |
|----------|-------------|---------|
| `null` | The empty list (not a function). Prefer over `'()` for readability | `null` = `'()` |
| `null?` | Tests for empty list. Prefer over `equal?` for null checks | `(null? '(2 3))` = `#f`, `(null? null)` = `#t` |
| `integer?` | Tests if input is an integer | `(integer? 5)` = `#t`, `(integer? '(3 1))` = `#f` |
| `list?` | Tests if input is a list | `(list? 5)` = `#f`, `(list? '(3 1))` = `#t` |
| `equal?` | Checks equality of lists/any structure. Avoid using with null | `(equal? '(1 2) '(1 2))` = `#t` |
| `first` | Returns first element of a list. List CANNOT be null | `(first '(3 1 4))` = `3` |
| `rest` | Returns all but first element. Input cannot be null | `(rest '(a b c))` = `'(b c)` |
| `cons` | Constructs list with new first element. 2nd arg must be a list | `(cons 3 '(1 4))` = `'(3 1 4)` |
| `if` | Conditional output. **AVOID nesting if/cond** | `(if (= n 3) 4 5)` |
| `cond` | Equivalent to nested ifs. Use `[condition output]` format. Last case should be `else`. Use `if` when only 2 cases. **AVOID nesting** | `(cond [(= n 1) 2] [(= n 3) 7] [else 5])` |
| `define` | Creates an alias. Does NOT create functions/variables. Avoid nesting — helper functions go outside the mother function | `(define x 3)` |
| `lambda` | Function factory — takes params + expression, returns anonymous function. **Use sparingly** | `(λ (x y) (+ x y y))` |

---

## ⚠️ List Functions — Permitted Only If Explicitly Allowed

| Function | Description | Example |
|----------|-------------|---------|
| `length` | Returns number of members in a list | `(length '(5 1 2))` = `3` |
| `list` | Creates a list of the arguments | `(list 3 1)` = `'(3 1)` |
| `append` | Merges two lists together | `(append '(5 1) '(2 4))` = `'(5 1 2 4)` |
| `cons?` | Tests if input was result of a cons | `(cons? (cons 2 null))` = `#t`, `(cons? null)` = `#f` |
| `reverse` | Reverses a list. *If you think you need this, your recursive call is probably in the wrong place* | `(reverse '(3 1 4))` = `'(4 1 3)` |
| `second`, `third`, `fourth`, etc. | Returns member at that index. Prefer `(first (rest ...))` for equational reasoning | `(second '(3 1 4))` = `1` |
| `map` | Avoids direct recursion — maps a function over a list | `(map double '(3 1 4))` = `'(6 2 8)` |
| `foldr` / `foldl` | Avoids direct recursion — folds a function over a list with initial value | `(foldr + 0 '(3 1 4))` = `8` |

---

## ✅ Boolean Functions — ALWAYS Permitted (unless stated otherwise)

| Function | Description | Example |
|----------|-------------|---------|
| `and` | Conjunction — all inputs true | `(and #t #t)` = `#t`, `(and #t #f)` = `#f` |
| `or` | Disjunction — at least one input true | `(or #f #t)` = `#t`, `(or #f #f)` = `#f` |
| `not` | Negation — switches input | `(not #t)` = `#f`, `(not #f)` = `#t` |
| `xor` | Exclusive or. Note: NOT the same as "exactly one true" for 3+ inputs | `(xor #t #t)` = `#f`, `(xor #t #f)` = `#t` |

---

## 🚫 NEVER Permitted — Will Result in Penalties

```
set, let, list-ref, empty?, eq?, modulo, car, cdr, display, begin,
match, filter, flatten, do, apply, when, unless, for-each, andmap,
make-list, build-list
```

---

## ✅ Math Functions — ALWAYS Permitted

| Function | Description | Example |
|----------|-------------|---------|
| `+` | Addition — variadic (any number of inputs) | `(+ 2 3 4)` = `9`, `(+)` = `0` |
| `-` | Subtraction — variadic | `(- 9 7)` = `2` |
| `*` | Multiplication — variadic | `(* 2 3)` = `6` |
| `=` | Checks equality of numbers (not lists). Avoid using with 0 | `(= 3 3)` = `#t` |
| `>`, `<`, `>=`, `<=` | Comparison operators for numbers | `(< 3 7)` = `#t`, `(> 5 5)` = `#f` |
| `zero?` | Faster than `(= x 0)` | `(zero? 0)` = `#t`, `(zero? 3)` = `#f` |
| `remainder` | Remainder after division | `(remainder 20 3)` = `2` |
| `quotient` | Integer division | `(quotient 20 3)` = `6` |

---

## ⚠️ Math Functions — Permitted Only If Explicitly Allowed

| Function | Description | Example |
|----------|-------------|---------|
| `log` | Natural logarithm | `(log 10)` = `2.302...` |
| `expt` | Exponentiation | `(expt 2 3)` = `8` |
| `/` | Division | `(/ 10 5)` = `2` |
| `even?` / `odd?` | Parity predicate | `(even? 6)` = `#t`, `(even? 9)` = `#f` |
| `max` / `min` | Maximum or minimum | `(max 2 7 1)` = `7` |
| `sqrt` | Square root | `(sqrt 9)` = `3` |
