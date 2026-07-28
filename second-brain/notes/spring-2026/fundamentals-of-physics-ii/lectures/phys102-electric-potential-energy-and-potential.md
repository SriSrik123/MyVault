# Electric Potential Energy and Electric Potential

**Course**: PHYS 102 — Fundamentals of Physics II  
**Topic**: Potential Energy, Electric Potential, Equipotential Surfaces  
**Tags**: #phys102 #electricity #potential-energy #electric-potential

---

## 1. Electric Potential Energy

**Definition**: Potential energy is the work done by an external force to bring two charges together from an initially infinite separation.

- High potential energy → someone did work to bring those objects into that configuration
- Two positive charges placed near each other have high potential energy (they'd repel if released)
- A positive and negative charge near each other also have potential energy — they'd attract and accelerate together if released

$$U = k \frac{q_1 q_2}{r}$$

**Convention**: When charges are infinitely far apart, potential energy = 0.

### Multiple Charges

For a system of charges, potential energy is the **sum over all pairs**:

$$U_{total} = \sum_{\text{all pairs}} k \frac{q_i q_j}{r_{ij}}$$

For 3 charges → 3 pairs  
For 4 charges → 6 pairs

---

## 2. Work and Potential Energy

$$\Delta W_{\text{external}} = \Delta U \quad \text{(external force increases PE)}$$

$$W_{\text{field}} = -\Delta U \quad \text{(field doing work decreases PE)}$$

Key relationships:
- External force does **positive work** → PE **increases**
- Electric field does work → PE **decreases**, KE **increases**
- Conservation of energy: $KE_i + U_i = KE_f + U_f$

### Removing a Charge to Infinity

$$\Delta W_{\text{external}} = U_f - U_i$$

Where $U_f = 0$ (charges infinitely separated).

If the result is **negative**, the charge will push itself away on its own — you'd actually need to do negative work (hold it back), meaning the field does the work for you.

---

## 3. Electric Potential (V)

**Potential is NOT the same as potential energy.**

| | Potential Energy (U) | Potential (V) |
|---|---|---|
| Requires | Two charges | Single charge creating a field |
| Units | Joules (J) | Volts (V = J/C) |
| Formula | $U = kq_1q_2/r$ | $V = kq/r$ |

$$U = qV \quad \Rightarrow \quad \Delta U = q \cdot \Delta V$$

**Potential** is a scalar field created by a charge distribution. A second charge placed in that field has potential energy = $qV$.

### Relationship Between E and V

$$E = -\frac{dV}{dx} \quad \text{(in 1D)}$$

$$\Delta V = -\int E \cdot dr$$

---

## 4. Potential of Symmetric Charge Distributions

**Outside** a charged shell/sphere (conducting or non-conducting):

$$V(r) = \frac{kQ}{r} \quad (r \geq R)$$

Behaves like a point charge — no surprise.

**Inside** a conducting sphere:

- E = 0 inside
- Since $E = -dV/dr = 0$, potential must be **constant** inside
- $V_{\text{inside}} = V_{\text{surface}} = \frac{kQ}{R}$

**Physical meaning**: Inside a conductor, there's no force on a charge, so no work is needed to move it around → potential is constant (equipotential volume).

---

## 5. Equipotential Surfaces

A surface where the potential is constant is called an **equipotential surface** (or line in 2D).

- Moving along an equipotential: $\Delta U = q\Delta V = 0$ → **no work done**
- **Equipotential surfaces are always perpendicular to E field lines**
- This is because $W = F \cdot d\cos\theta = 0$ only when $\theta = 90°$

### Examples

- Point charge → equipotential surfaces are **concentric spheres**
- Uniform E field (e.g., between parallel plates) → equipotential surfaces are **planes perpendicular to E**

**E field lines are always 90° to equipotential surfaces** (and to the surface of a conductor).

> In lab: you trace equipotential lines with a probe (finding equal-voltage points), then draw E field lines perpendicular to them.

---

## 6. Finding V from an Expression

If potential is given as a function:

$$V(x) = 1500 + 10x + 2x^2 \quad \text{(example)}$$

- Find $V$ at $x = 1\,\text{m}$: plug in $x = 1$
- Find $V$ at $x = 2\,\text{m}$: plug in $x = 2$
- Find E: $E = -\frac{dV}{dx}$ → take derivative and negate

---

## 7. Example Problem (Textbook 23.1 style)

**Given**: $E = 2000 \, \text{V/m}$ in the $+x$ direction  
**Find**: $\Delta V$ between $x = 0$ and $x = 4\,\text{m}$, then $\Delta U$ for a $3\,\mu\text{C}$ charge

$$\Delta V = V(x=4) - V(x=0) = -E \cdot \Delta x = -(2000)(4) = -8000 \, \text{V} = -8 \, \text{kV}$$

$$\Delta U = q \cdot \Delta V = (3 \times 10^{-6})(-8000) = -24 \times 10^{-3} \, \text{J} = -24 \, \text{mJ}$$

**Interpretation**: The charge's PE decreased by 24 mJ → its KE increased by 24 mJ (it sped up in the direction of E).

---

## 8. Key Takeaways

1. Potential energy requires **two charges**; potential is created by **one charge**
2. Moving along an equipotential = **zero work done**
3. Equipotential surfaces are **always ⊥ to E field**
4. E fields are always **⊥ to conducting surfaces** (else free energy paradox)
5. Inside a conductor: $E = 0$, $V = \text{constant}$
6. Sign of work tells you the physics — don't ignore it
