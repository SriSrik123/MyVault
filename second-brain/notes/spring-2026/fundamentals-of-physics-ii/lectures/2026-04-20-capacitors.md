# Capacitors — PHYS-102
**Date:** 2026-04-20
**Source:** lecture recording (Voice 260420_090721)

## Overview
This lecture introduces capacitors — devices that store electrical energy by separating charge on two conducting plates. The professor covers how capacitors are charged, how capacitance is defined, the energy stored in a capacitor, and how geometry (plate area, separation, shape) determines capacitance.

## Key Concepts

### What is a Capacitor?
- A capacitor consists of **two conductors** (plates) separated by a gap
- The simplest form is the **parallel plate capacitor**: two metallic plates facing each other
- Capacitors appear in many forms: rolled foil (inside high-power electronics), spherical shells, cylindrical cables

### Charging a Capacitor
- Connect a capacitor to a **battery** (EMF source): the larger bar = positive terminal, smaller bar = negative
- Electrons from the negative plate flow to the battery; electrons accumulate on the other plate
- One plate becomes **positive** (+Q), the other **negative** (−Q)
- This separation creates an **electric field E** between the plates pointing from + to −
- Charging stops when the potential difference across the plates equals the battery voltage → capacitor is **fully charged**

### Capacitance (C)
**Definition:** Capacitance is the ability of a geometry to store charge per unit potential difference.

$$C = \frac{Q}{V}$$

- C is a **property of the geometry only** — it does not depend on Q or V individually
- Unit: **Farad (F)** = C/V (typical capacitors are μF or pF)
- Larger area → larger C; smaller separation → larger C

### Parallel Plate Capacitor
$$C = \frac{\varepsilon_0 A}{d}$$

| Symbol | Meaning |
|--------|---------|
| ε₀ | Permittivity of free space (8.85 × 10⁻¹² F/m) |
| A | Area of one plate |
| d | Separation between plates |

- Electric field between plates: **E = V/d** (uniform field)
- Surface charge density: σ = Q/A → E = σ/ε₀

### Energy Stored in a Capacitor
Three equivalent expressions (use whichever variables you're given):

$$U = \frac{Q^2}{2C} = \frac{1}{2}CV^2 = \frac{1}{2}QV$$

- Energy comes from the work done separating charges — analogous to raising a mass to height h in gravity

### Spherical Capacitor
Two concentric conducting shells with radii R₁ (inner) and R₂ (outer):

$$C = \frac{4\pi\varepsilon_0}{\frac{1}{R_1} - \frac{1}{R_2}}$$

- Potential difference: V = kQ(1/R₁ − 1/R₂)
- Outside the outer shell, acts like a point charge

### Cylindrical Capacitor
A wire (inner conductor) surrounded by a cylindrical shell — standard coaxial cable geometry. Capacitance per unit length derived from Gauss's law.

## Worked Scenarios

### Scenario 1 — Disconnect battery, then increase plate separation
- Charge Q is **constant** (nowhere to go)
- d increases → C = ε₀A/d **decreases**
- Since Q is fixed and C decreases: V = Q/C **increases**
- Energy U = Q²/2C **increases** (energy comes from the work you do pulling the plates apart)

### Scenario 2 — Keep battery connected, then increase plate separation
- Voltage V is **constant** (battery enforces it)
- d increases → C **decreases**
- Since V is fixed: Q = CV **decreases** (charge flows back to battery)
- Energy U = ½CV² **decreases**

## Important Formulas / Definitions

| Formula | Meaning |
|---------|---------|
| C = Q/V | Definition of capacitance |
| C = ε₀A/d | Parallel plate capacitor |
| E = V/d | Uniform field between parallel plates |
| U = Q²/2C = ½CV² = ½QV | Energy stored in capacitor |
| σ = Q/A | Surface charge density |
| E = σ/ε₀ | Field from surface charge |

## Summary
A capacitor stores energy by separating charge; its capacitance C is purely geometric. For parallel plates, C grows with area and shrinks with separation. The energy stored has three equivalent forms — pick based on what's given. When a capacitor is disconnected from a battery, Q is conserved; when connected, V is conserved. These two scenarios lead to opposite behaviors when you change the geometry, which is a common exam question.
