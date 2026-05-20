# Java Review — CS-265
**Date:** 2026-03-31
**Source:** Java Review

## Overview
Opening lecture Java review for CS-265 (Advanced Programming Tools & Techniques), covering Java fundamentals for students with prior programming experience (Python). Topics include the Java ecosystem (JVM/JRE/JDK), type system, naming conventions, OOP visibility, and key method categories.

## Key Concepts

### Java Ecosystem
- **JVM** – Java Virtual Machine: converts bytecode to native machine code; handles memory management and garbage collection.
- **JRE** – Java Runtime Environment: JVM + standard libraries; needed to *run* programs.
- **JDK** – Java Development Kit: JRE + compiler; needed to *compile and develop* programs.

### Key Differences from Python
| Feature | Python | Java |
|---------|--------|------|
| Types | Dynamic | Static — every variable has a declared type |
| Visibility | Convention-based (`_name`) | Compiler-enforced (`private`, `public`, etc.) |
| Keywords | Mixed case | All **lowercase** (`public`, `void`, `int`) |
| Classes | PascalCase supported | PascalCase **required** |

### Naming Conventions
- **Classes:** PascalCase → `MyStack`, `LinkedList`
- **Methods & variables:** camelCase → `push()`, `stackSize`
- **Constants:** CAP_UNDERSCORE → `MAX_CAPACITY`
- **Test methods:** all_lowercase_underscore → `push_on_empty_returns_true()`

### Type System
**Primitives** (lowercase keywords):

| Type | Size | Description |
|------|------|-------------|
| `boolean` | 1 bit | true / false |
| `char` | 16 bit | single Unicode character |
| `byte` | 8 bit | signed integer |
| `short` | 16 bit | signed integer |
| `int` | 32 bit | signed integer |
| `long` | 64 bit | signed integer |
| `float` | 32 bit | floating-point |
| `double` | 64 bit | floating-point |

**Objects** are non-primitive types (PascalCase): `String`, `ArrayList`, `Scanner`, etc.

### OOP and Visibility
Four visibility modifiers in Java (strictly enforced by the compiler):

| Modifier | Scope |
|----------|-------|
| `public` | All code |
| `protected` | Package + subclasses |
| *(package-private)* | Same package |
| `private` | Only within the defining class |

**Best practice:** instance fields should always be `private`.

### Special Methods
- **Constructor:** initializes a new instance; shares the class name; no return type.
- **Getter (Accessor):** returns a private field's value.
- **Setter (Mutator):** modifies a private field; return type is `void`.
- **`this`:** refers to the current object — used to disambiguate when parameter names shadow field names.

## Important Formulas / Definitions

```java
public class Stack {
    private int[] data;
    private int top;

    public Stack(int capacity) {  // Constructor
        data = new int[capacity];
        top = -1;
    }

    public int peek() { return data[top]; }       // Getter
    public void setTop(int t) { this.top = t; }   // Setter using 'this'
}
```

Comments:
```java
// Single-line
/* Multi-line block comment */
```

## Summary
Java enforces structure that Python leaves to convention: static types catch errors at compile time, and visibility modifiers enforce encapsulation. Understanding these foundations—especially the difference between primitives and objects, and the four visibility levels—is essential for building the more complex data structures and tools covered in CS-265.


---

## Related Notes

[[second-brain/notes/advanced-prog-tools/syllabus|CS-265 Syllabus]]  [[2026-04-06-pass-by-value-vs-reference|Next: Pass-by-Value vs Reference]]  [[second-brain/notes/intro-software-eng/lectures/2026-03-31-java-review|Java Review (SE-201 — same topic)]]