# Pass-by-Value vs Pass-by-Reference — CS-265
**Date:** 2026-04-06

## Overview
A fundamental concept in programming: how arguments are passed to functions/methods. The distinction determines whether changes made inside a function affect the original variable in the caller's scope.

## Key Concepts

### Pass-by-Value
The function receives a **copy** of the argument's value. Changes made inside the function have no effect on the original variable.

```java
void addTen(int x) {
    x = x + 10;  // only modifies the local copy
}

int n = 5;
addTen(n);
System.out.println(n);  // still 5 — original unchanged
```

### Pass-by-Reference
The function receives the **memory address** (reference) of the original variable. Changes inside the function **do** affect the original.

*(True pass-by-reference exists in C++ via `&` parameters; Java does not have this.)*

### Java's Model — "Pass-by-Value of the Reference"
Java is always **pass-by-value**, but the value passed for objects is the *reference* (memory address), not the object itself.

| Type | What gets copied | Can caller's data be changed? |
|------|-----------------|-------------------------------|
| Primitive (`int`, `double`, etc.) | The actual value | ❌ No — it's a copy |
| Object | A copy of the reference (address) | ✅ Fields yes, but reference itself no |

**Implication for objects:**
- You **can** mutate the object's fields from inside the method (because you hold a reference to the same object).
- You **cannot** reseat the reference itself (make the caller's variable point to a different object).

```java
void mutate(int[] arr) {
    arr[0] = 99;   // ✅ mutates the array — caller sees this change
}

void reseat(int[] arr) {
    arr = new int[]{1, 2, 3};  // ❌ only changes local copy of the reference
}
```

## Important Formulas / Definitions

- **Pass-by-value** — a copy of the value is passed; original is safe.
- **Pass-by-reference** — the address is passed; original can be modified.
- **Java rule** — primitives are always pass-by-value; objects pass a copy of the reference (fields are mutable, the reference itself is not reseatable).

## Summary
Java is always pass-by-value, but "value" for an object variable means the reference (address). This is why you can change an object's internal state from a method, but you cannot make the caller's variable point to a new object. Understanding this prevents common bugs where you expect a method to "swap" two variables but it has no effect.


---

## Related Notes

[[second-brain/notes/advanced-prog-tools/syllabus|CS-265 Syllabus]]  [[second-brain/notes/advanced-prog-tools/lectures/2026-03-31-java-review|Previous: Java Review]]