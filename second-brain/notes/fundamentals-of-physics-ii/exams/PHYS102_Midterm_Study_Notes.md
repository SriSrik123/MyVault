# PHYS-102 Midterm-I — Comprehensive Study Notes
*Electric Charges · Electric Fields · Gauss's Law · Conductors · Charge Distributions*

---

## 1. Electric Charges & Coulomb's Law

### 1.1 The Basics of Charge
- Two types: positive (+) and negative (−)
- Like charges **repel**; opposite charges **attract**
- Charge is conserved — cannot be created or destroyed
- Elementary unit: **e = 1.6 × 10⁻¹⁹ C**
- Unit conversions: **1 nC = 10⁻⁹ C** · **1 μC = 10⁻⁶ C**

### 1.2 Coulomb's Law
The electrostatic force between two point charges q₁ and q₂ separated by distance r:

$$F = \frac{kq_1 q_2}{r^2} \qquad k = 9 \times 10^9 \ \text{N·m}^2/\text{C}^2$$

- Force is along the line connecting the two charges
- Positive result = repulsion; negative = attraction
- Newton's 3rd Law applies: F₁₂ = −F₂₁

> **Exam Tip:** With multiple charges, find each force separately as a vector and add components (x and y) separately.

---

## 2. Electric Field (E-Field)

### 2.1 Definition

$$\vec{E} = \frac{\vec{F}}{q} \qquad \Rightarrow \qquad \vec{F} = q\vec{E}$$

- E is a vector with units **N/C**
- Points **away** from positive charges, **toward** negative charges

### 2.2 E-Field from a Point Charge

$$E = \frac{kQ}{r^2}$$

### 2.3 Finding Where E = 0 Between Two Charges
- **Same-sign charges:** zero point is **between** them, closer to the smaller charge
- **Opposite-sign charges:** zero point is **outside** the pair, on the side of the smaller-magnitude charge
- Strategy: set k|Q₁|/x² = k|Q₂|/(d − x)² and solve for x

> **Exam Tip:** For charges −4Q and +Q (as on the midterm), the zero point is to the **right** of +Q (Region C), not between them.

### 2.4 Superposition
$$\vec{E}_{net} = \vec{E}_1 + \vec{E}_2 + \vec{E}_3 + \cdots \quad \text{(vector addition)}$$

Resolve into components, sum x and y separately, then find magnitude with √(Ex² + Ey²).

---

## 3. Charge Distributions

### 3.1 Types of Charge Density

| Symbol | Formula | Meaning |
|--------|---------|---------|
| λ | q / L | Linear (C/m) — along a wire |
| σ | q / A | Surface (C/m²) — on a surface |
| ρ | q / V | Volume (C/m³) — throughout a volume |

### 3.2 E-Field Formulas by Geometry

| Situation | Formula |
|-----------|---------|
| Point charge (outside) | E = kQ/r² |
| Inside uniform insulating sphere (r < R) | E = kQr/R³ *(grows linearly with r)* |
| Infinite line of charge | E = 2kλ/r |
| Near one infinite sheet | E = σ/(2ε₀) |
| Between two parallel opposite plates | E = σ/ε₀ |
| Inside any conductor | E = 0 *(always)* |

> **Exam Tip:** Know when to use E = kQr/R³ (inside a sphere) vs E = kQ/r² (outside). The inside formula gives E = 0 at the center and grows linearly to kQ/R² at the surface.

---

## 4. Gauss's Law

### 4.1 Statement

$$\oint \vec{E} \cdot d\vec{A} = \frac{q_{\text{enclosed}}}{\varepsilon_0} \qquad \varepsilon_0 = 8.85 \times 10^{-12} \ \text{C}^2/(\text{N·m}^2)$$

- Flux through a closed surface depends **only** on enclosed charge
- Moving a charge inside the surface changes the local E-field but **not** the total flux

### 4.2 Step-by-Step Method
1. Identify symmetry (spherical, cylindrical, planar)
2. Draw a Gaussian surface matching the symmetry
3. Calculate q_enclosed
4. Simplify: `∮ E·dA = E × (surface area)`
5. Set equal to q_enc/ε₀ and solve for E

### 4.3 Spherical Symmetry

$$E \times (4\pi r^2) = \frac{q_{\text{enclosed}}}{\varepsilon_0}$$

For a solid insulating sphere (charge Q, radius R):

| Region | q_enclosed | E-field |
|--------|-----------|---------|
| r < R (inside) | Q(r/R)³ | E = kQr/R³ |
| r = R (surface) | Q | E = kQ/R² |
| r > R (outside) | Q | E = kQ/r² |

### 4.4 Concentric Sphere Problems (Midterm Prob. 2)

Work region by region, tracking enclosed charge carefully:

| Region | E-field |
|--------|---------|
| r < R₁ (inside insulator) | E = kQr/R₁³ |
| R₁ < r < R₂ (gap) | E = kQ/r² |
| R₂ < r < R₃ (inside conductor) | **E = 0** |
| r > R₃ (outside everything) | E = k(Q + q_shell)/r² |

**Induced charges on the shell:**
- Inner surface: **−Q** (equal and opposite to the enclosed charge)
- Outer surface: **q_shell + Q** (remainder of shell's own charge)

> **Watch Out:** When finding the outer surface charge, don't forget to add Q to the shell's own charge. The midterm had q_shell = −12.25 nC and Q = +10 nC → outer surface = 10 − 12.25 = **−2.25 nC**.

### 4.5 Key Conceptual Points
- Flux depends **only** on enclosed charge — not on shape of surface or charges outside
- Moving a charge inside: **flux stays the same**, local E changes
- E = 0 everywhere inside a conductor in electrostatic equilibrium

---

## 5. Conductors in Electrostatic Equilibrium

### 5.1 Key Properties
- E-field inside a conductor is **always zero**
- Net charge resides entirely on the **outer surface**
- E-field just outside a conductor is perpendicular to the surface
- Cavity with charge Q inside → inner surface gets **−Q**, outer surface gets **+Q** (plus any original charge)

### 5.2 Conductor in an External Field
- Charges redistribute to cancel the external field inside
- **E_int = 0** regardless of the external field's strength
- The field outside is distorted; inside is always zero

> **Exam Tip:** The midterm asked about E_int for a conducting sphere in external field E⃗. The answer is always **E_int = 0**, not E⃗, not −E⃗.

---

## 6. Infinite Sheets & Parallel Plates

### 6.1 One Infinite Sheet

$$E = \frac{\sigma}{2\varepsilon_0}$$

- Uniform field at every distance from the sheet
- Perpendicular to the sheet; away from positive, toward negative

### 6.2 Two Parallel Opposite Plates

$$E = \frac{\sigma}{\varepsilon_0}$$

- Fields from both sheets **add** between them and **cancel** outside
- Field between plates is uniform

### 6.3 Particle Accelerating Between Plates
A charge q (mass m) released from rest travels distance d between plates:

$$\Delta W = qEd = \frac{q\sigma d}{\varepsilon_0} = \frac{1}{2}mv^2$$

$$\boxed{v = \sqrt{\frac{2q\sigma d}{m\varepsilon_0}}}$$

> **Exam Tip:** For the extra-credit problem, just set work = kinetic energy (qEd = ½mv²) and solve for v. The particle starts from rest so all work goes into KE.

---

## 7. Charged Particle in Equilibrium (FBD Problems)

### 7.1 Setup
A charged particle (charge q, mass m) hangs from a thread at angle θ near a large charged sheet. Three forces act on it:

| Force | Direction |
|-------|-----------|
| Tension T | Along the thread (angle θ from vertical) |
| Gravity mg | Straight down |
| Electric force qE | Horizontal (toward/away from sheet) |

### 7.2 Equations of Equilibrium

**Vertical:** 
$$T\cos\theta = mg \qquad \Rightarrow \qquad T = \frac{mg}{\cos\theta}$$

**Horizontal:** 
$$T\sin\theta = qE = \frac{q\sigma}{2\varepsilon_0} \qquad \Rightarrow \qquad \sigma = \frac{2\varepsilon_0 T\sin\theta}{q}$$

> **Exam Tip:** Find T from the vertical equation **first**, then plug into the horizontal equation to find σ. You need T before you can solve for σ.

> **Watch Out:** If the particle is negatively charged, the electric force points **opposite** to the E-field direction. Check the sign carefully.

---

## 8. Quick-Reference Equation Sheet

| Equation | What It Means |
|----------|--------------|
| k = 9 × 10⁹ N·m²/C² | Coulomb's constant |
| ε₀ = 8.85 × 10⁻¹² C²/(N·m²) | Permittivity of free space |
| k = 1/(4πε₀) | Relationship between k and ε₀ |
| F = kq₁q₂/r² | Coulomb's Law |
| E = kQ/r² | E-field from a point charge |
| E = kQr/R³ (r < R) | E inside a uniform insulating sphere |
| ∮E·dA = q_enc/ε₀ | Gauss's Law |
| E = σ/(2ε₀) | One infinite sheet |
| E = σ/ε₀ | Between two parallel opposite plates |
| qEd = ½mv² | Work-energy: particle between plates |
| T cosθ = mg | Equilibrium, vertical |
| T sinθ = qE | Equilibrium, horizontal |
| λ = q/L · σ = q/A · ρ = q/V | Charge density definitions |
| 1 μC = 10⁻⁶ C · 1 nC = 10⁻⁹ C | Unit conversions |

---

## 9. Exam Strategy & Common Mistakes

### Common Mistakes
- Forgetting to **square** r in E = kQ/r²
- Using E = kQ/r² **inside** a sphere instead of E = kQr/R³
- Mixing up E = σ/(2ε₀) (one sheet) with E = σ/ε₀ (between two plates)
- Forgetting the **−Q** induced on the inner surface of a conducting shell
- Not accounting for the shell's own charge when finding outer surface charge
- Saying E_int = E_external for a conductor — it's **always zero**
- Swapping sin and cos in FBD problems

### 50-Minute Time Plan
- **Problem 1** (30 pts, 6 multiple choice) → ~12 min
- **Problem 2** (40 pts, concentric spheres) → ~22 min — find Q in part [a] first, use it in all later parts
- **Problem 3** (30 pts, FBD) → ~12 min — draw FBD first, label all forces
- **Problem 4** (10 pts extra credit) → ~4 min — straightforward work-energy theorem

---

## Last-Minute Cheat Sheet

### E-Field Regions (Spherical)
| Location | E-field |
|----------|---------|
| r < R (insulating sphere) | E = kQr/R³ → grows from 0 at center |
| R₁ < r < R₂ (gap) | E = kQ/r² |
| Inside conductor | **E = 0** |
| r > R₃ (outside all) | E = k(Q_total)/r² |

### Induced Charges on Conducting Shell
- Inner surface: **−Q_inner**
- Outer surface: **q_shell + Q_inner**

### FBD
$$T = \frac{mg}{\cos\theta} \qquad \sigma = \frac{2\varepsilon_0 T\sin\theta}{q}$$

### Particle Between Plates
$$v = \sqrt{\frac{2q\sigma d}{m\varepsilon_0}}$$

### Conceptual Quick-Hits
- E inside any conductor = **0**
- Moving charge inside Gaussian surface → **flux same**, local E changes
- Zero E-field: **between** same-sign charges; **outside** opposite-sign charges (on small-charge side)
- Conductor in external field → **E_int = 0**
