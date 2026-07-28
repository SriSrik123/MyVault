---
tags:
  - phys102
  - lab
  - electric-fields
  - electric-potentials
  - equipotential
  - physics
  - lab-report
  - spring-2026
type: lab
course: PHYS 102
date: 2026-04-14
partners:
  - Eamon Browne
  - Drishya Manda
  - Srinarayan Srikanth
conversation: "[[2026-04-14-claude-chat-phys102-lab1]]"
---

# Electric Fields and Electric Potentials — PHYS 102 Lab
**Date:** 2026-04-14
**Type:** Lab Report + Worksheet
**Partners:** Eamon Browne, Drishya Manda, Srinarayan Srikanth
**Source:** Lab session + Claude chat writeup → [[2026-04-14-claude-chat-phys102-lab1]]

---

## Overview
Mapped equipotential lines and electric field lines in two electrode configurations using a shallow tray of distilled water as the conducting medium and a digital multimeter. Compared field geometry between a two-ring setup and a ring-strip setup.

**Key equation:**
$$E_{avg} = -\frac{\Delta V}{\Delta r}$$

Where $\Delta V = 2\,V$ for every adjacent equipotential pair in this lab, so field strength depends entirely on how tightly the lines are packed.

---

## Part A: Two Ring Electrode Configuration

- Left ring at **(2, 9)** → 10 V; Right ring at **(22, 9)** → 0 V
- Equipotentials traced at 1, 3, 5, 7, 9 V

### Calculated E-field values (centerline, y = 9)
| Equipotential Pair | Distance (m) | E (N/C) |
|--------------------|-------------|---------|
| 3 V – 5 V          | 0.07        | 28.6    |
| 1 V – 3 V          | 0.05        | 20.0    |
| At (13, 7)         | 1           | 4.0     |

### Observations
- Equipotentials were **bilaterally symmetric** about the midpoint
- Lines curve concentrically near each ring, nearly vertical and straight at the center (~x = 12–13)
- **Strongest field:** center between the two rings (equipotentials most tightly packed)
- **Weakest field:** near/far from center where lines spread out
- **Inside ring electrodes:** potential is constant (10 V left, 0 V right), E-field = 0 (conductor)

---

## Part B: One Ring – One Strip Electrode Configuration

- Ring at **(2, 9)** → 10 V; Vertical strip at x = 22 → 0 V
- Same mapping procedure, equipotentials at 1, 3, 5, 7, 9 V

### Calculated E-field values (centerline)
| Equipotential Pair | Distance (m) | E (N/C) |
|--------------------|-------------|---------|
| 3 V – 5 V          | 0.07        | 28.0    |
| 1 V – 3 V          | 0.08        | 25.0    |
| 7 V – 9 V          | 0.02        | **100.0** |
| At (13, 7)         | 0.02        | 3.5     |

### Observations
- Symmetry is **broken** by the strip
- Near the ring: equipotentials tight and circular → strongest field (100 N/C near 7–9 V pair)
- Near the strip: equipotentials flatten and run parallel to the electrode (like parallel plates)
- Field weakens steadily moving toward the strip
- **Inside ring:** potential uniform at 10 V, E-field = 0

---

## Comparison: Two Rings vs. Ring-Strip

| Feature | Two Rings | Ring + Strip |
|---|---|---|
| Symmetry | Bilateral | Asymmetric |
| Equipotential shape | Curved/circular at rings, straight at center | Circular near ring, planar near strip |
| Strongest field location | Center between rings | Near the ring (~7–9 V region) |
| Max E measured | ~28.6 N/C | 100 N/C |
| Inside conductors | E = 0, V = constant | E = 0, V = constant |

---

## Key Concepts / Takeaways

- **Equipotential lines** are always ⊥ to **electric field lines**
- A charge moving along an equipotential does **no work** (ΔPE = 0)
- **Conductors are equipotential surfaces** — E = 0 inside
- More tightly packed equipotentials → **stronger E-field**
- Geometry of electrodes directly determines field distribution

---

## Sources of Error
- **Probe positioning** (~0.5 cm uncertainty) → up to **25% error** for closely spaced pairs (e.g., 7–9 V pair in Part B where spacing ≈ 2 cm)
- Uneven water depth from tray tilting → shifts current density
- Imperfect electrode contact at tray surface
- Off-axis measurements at (13,7) give lower E because field is weaker and oblique there

---

## Files
- [[2026-04-14-lab-electric-fields-potentials-report.docx]] — full written lab report
- [[2026-04-14-lab-electric-fields-potentials-worksheet.pdf]] — in-class worksheet with raw answers
- [[39298534.pdf]] — original lab instruction sheet
- Figures: hand-drawn equipotential + E-field maps (photographed, attached in report)
