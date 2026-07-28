# Java Review — SE-201
**Date:** 2026-03-31
**Source:** Java ReviewSE201

## Overview
Week 1 lecture for SE-201 reviews the Java programming language for students coming from Python. Java is the primary language for this course and is used to learn Test-Driven Development (TDD) and software engineering principles. The lecture covers Java's core characteristics, type system, OOP model, and visibility rules.

## Key Concepts

### What Is Java?
- Released in 1995; general-purpose, object-oriented, concurrent, multi-platform.
- Compiled to **bytecode**, run on the **JVM** (Java Virtual Machine).
- Key components:
  - **JVM** – Java Virtual Machine: converts bytecode to machine code; handles memory and garbage collection.
  - **JRE** – Java Runtime Environment: JVM + libraries; required to *run* Java.
  - **JDK** – Java Development Kit: JRE + compiler tools; required to *compile* Java.

### Java vs. Python
| Feature | Python | Java |
|---------|--------|------|
| Typing | Dynamic | Static (explicit types) |
| Visibility | By convention only | Strictly enforced |
| Structure | Flexible | Strongly structured |
| OOP | Supported | Everything is a class |

### Naming Conventions
| Context | Convention | Example |
|---------|-----------|---------|
| Classes | PascalCase | `MyClass`, `Scanner` |
| Methods & variables | camelCase | `getAge()`, `firstName` |
| Constants | CAP_UNDERSCORE | `MAX_SIZE` |
| Test method names | all_lowercase_underscore | `one_plus_one_equals_two()` |

### Types
Two categories of types in Java:
1. **Primitives** (lowercase): `boolean`, `char`, `byte`, `short`, `int`, `long`, `float`, `double`
2. **Objects/Classes** (PascalCase): `String`, `Scanner`, `Math`, etc.

### Object-Oriented Programming (OOP)
- Everything is an object — a unit responsible for its own data and behavior.
- A **class** is a blueprint; an **instance** (object) is a realization of that blueprint.
- Three views of an object:
  - *Conceptual:* a set of responsibilities
  - *Specification:* a set of methods
  - *Implementation:* code + data

### Visibility Modifiers
| Modifier | Accessible From |
|----------|----------------|
| `public` | Everywhere |
| `protected` | Same package + subclasses |
| *(no modifier)* | Same package only |
| `private` | Only within the same class |

**Rule of thumb:** Fields (instance variables) should always be `private`.

### Special Method Types
- **Constructor** – initializes a new object; same name as class.
- **Getter (Accessor)** – returns the value of a private field.
- **Setter (Mutator)** – changes the value of a private field; return type `void`.
- **`this`** keyword – refers to the current object instance; used to distinguish instance variables from local parameters.

## Important Formulas / Definitions

```java
public class Student {
    private String name;  // private field

    public Student(String name) {  // constructor
        this.name = name;          // 'this' refers to the object
    }

    public String getName() { return name; }   // getter
    public void setName(String n) { name = n; } // setter
}
```

**Comments:**
```java
// Single line comment
/* Block
   comment */
```

## Summary
Java's strict typing, enforced visibility, and class-based OOP make it ideal for teaching software engineering principles. The key shift from Python is moving from convention-based to compiler-enforced visibility and from dynamic to static typing. This course uses Java 17 with IntelliJ IDE and requires GitLab for CI/CD workflows in TDD assignments.


---

## Related Notes

[[second-brain/notes/intro-software-eng/syllabus|SE-201 Syllabus]]  [[second-brain/notes/advanced-prog-tools/lectures/2026-03-31-java-review|Java Review (CS-265 — same topic)]]