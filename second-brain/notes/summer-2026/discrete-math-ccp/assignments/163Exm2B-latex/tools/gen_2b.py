#!/usr/bin/env python3
"""2b (p511): psi(p,q) DNF/CNF derivation + verification tables. Verified:
psi(p,q) := not((p C1 not-q) C2 (not-p C3 q)), C1=C2=C3=OR for Sri -- same
inner expression as 1a(i), which is a flat tautology (contains p and not-p
as bare disjuncts) -- so psi is identically a CONTRADICTION (always 0).
Per the printed page's own instruction, this means ALL FOUR canonical DNF
disjuncts and ALL FOUR CNF conjuncts get struck (matches SOL2B-2024's own
psi=bottom outcome for different C-values, same phenomenon).

Flagged (not silently guessed): the second verification table's own column
header is printed "phi_1a(ii)" but the governing prose two paragraphs above
it only ever says "(1a)(i)" -- filling both tables' final column with
phi_1a(i)'s value (=1 always), matching the prose instruction literally;
the printed header label itself is left exactly as traced (pixel-fidelity),
not silently corrected.
"""
import sys
sys.path.insert(0, '.')
from atoms import R, center_in_gap, fmt

C1 = C2 = C3 = '∨'
out = []


def strike_box(x0, x1, y, dp=4.0, ht=9.0, w=0.6):
    """Diagonal strike across a pre-printed token's bounding box (not an
    Atom -- these tokens are already on the page from gen2.py's trace)."""
    return [f'\\DLINE{{{fmt(x0)}}}{{{fmt(y + dp)}}}{{{fmt(x1)}}}{{{fmt(y - ht)}}}{{{fmt(w)}}}']


# ---- substituted definition line (y=334.37): 3 connective gaps ----
out += center_in_gap(210.45, 229.97, 334.37, C1, 11.04)
out += center_in_gap(270.70, 279.05, 334.37, C2, 11.04)
out += center_in_gap(309.43, 326.35, 334.37, C3, 11.04)

# ---- DNF line (y=388.25): strike all 4 terms (psi = bottom always) ----
dnf_terms = [(180.02, 230.14), (233.57, 298.78), (302.09, 367.08), (370.51, 453.03)]
for x0, x1 in dnf_terms:
    out += strike_box(x0, x1, 388.25)

# ---- CNF line (y=439.63): strike all 4 terms ----
cnf_terms = [(180.02, 230.14), (233.57, 298.78), (302.09, 367.08), (370.51, 453.03)]
for x0, x1 in cnf_terms:
    out += strike_box(x0, x1, 439.63)

# ---- verification tables: p,q,not-p,not-q columns are ALREADY pre-printed
# per-row (confirmed via findgaps -- e.g. row y=595.90 already shows
# "0,0,1,1" at the given-bit x-positions, matching (p,q)=(0,0)) -- only the
# working columns plus the psi(p,q) and phi_1a column need filling.
#
# FLAGGED, confirmed directly against the original PDF's own text (not a
# tracing artifact): both tables' header rows print FIVE conjunct/disjunct
# column labels, not four -- slot 2 and slot 4 are IDENTICAL printed labels
# ("p ∧(¬q)" / "p ∨(¬q)" both times), a genuine authoring duplicate in the
# source exam (verified same in both tables, so systematic, not a one-off
# typo). The true 4th canonical minterm ((¬p)∧(¬q) / (¬p)∨(¬q)) only
# appears in slot 5. Filled per what each slot's OWN printed label asks for
# (slot 2 and slot 4 get the SAME values, since they carry the same label)
# rather than silently relabeling/fixing the template.
def AND(a, b): return 1 if (a and b) else 0
def OR(a, b): return 1 if (a or b) else 0
def NOT(a): return 1 - a


rows2 = [(0, 0), (0, 1), (1, 0), (1, 1)]
slot_mid = [(173.18 + 208.37) / 2, (208.37 + 256.25) / 2,
            (256.25 + 305.45) / 2, (305.45 + 356.47) / 2,
            (356.47 + 404.47) / 2]
psi_mid = (429.55 + 457.06) / 2
phi_mid = (481.78 + 503.86) / 2

ys1 = [595.90, 607.50, 630.90, 642.60]
for (p, q), y in zip(rows2, ys1):
    pq, pnq, npq, npnq = AND(p, q), AND(p, NOT(q)), AND(NOT(p), q), AND(NOT(p), NOT(q))
    vals = [pq, pnq, npq, pnq, npnq]   # slot4 duplicates slot2's label+value
    for x, v in zip(slot_mid, vals):
        a = R(str(v), 9.0, font='b')
        out += a.emit(x - a.w / 2, y)
    a = R('0', 9.0, font='b')
    out += a.emit(psi_mid - a.w / 2, y)
    a = R('1', 9.0, font='b')
    out += a.emit(phi_mid - a.w / 2, y)

ys2 = [701.40, 713.00, 736.40, 750.00]
phi2_mid = (480.70 + 505.06) / 2
for (p, q), y in zip(rows2, ys2):
    pq, pnq, npq, npnq = OR(p, q), OR(p, NOT(q)), OR(NOT(p), q), OR(NOT(p), NOT(q))
    vals = [pq, pnq, npq, pnq, npnq]
    for x, v in zip(slot_mid, vals):
        a = R(str(v), 9.0, font='b')
        out += a.emit(x - a.w / 2, y)
    a = R('0', 9.0, font='b')
    out += a.emit(psi_mid - a.w / 2, y)
    a = R('1', 9.0, font='b')
    out += a.emit(phi2_mid - a.w / 2, y)

with open('pages/answers511.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers511.tex')
