#!/usr/bin/env python3
"""1b (p507): connective fills on the two setup lines (2i/2ii), the combined
LS/RS truth table's substituted header row, all 6 working columns x 8 rows,
and the closing LS<->RS decision line + its Y/N/Pf/W circles. Every gap's
(x0,x1) is read off tools/findgaps.py's report against pages/page507.tex,
not guessed. C7=AND, C8=IFF for Sri's J-number.
"""
import sys
sys.path.insert(0, '.')
from atoms import R, center_in_gap, circle_token, fmt

C7, C8 = '∧', '⟷'


def AND(a, b): return 1 if (a and b) else 0
def IFF(a, b): return 1 if (a == b) else 0


def box(x0, y0, x1, y1, w=0.7):
    """Ruler-straight rectangle outline (4 DLINEs), matching the course's
    ruled-line requirement -- used per SOL2B-2024's own '(See the boxed
    ones)' convention: box the LS<=>RS answer column to call out the
    tautology-counterexample rows the verdict rests on."""
    return [
        f'\\DLINE{{{fmt(x0)}}}{{{fmt(y0)}}}{{{fmt(x1)}}}{{{fmt(y0)}}}{{{fmt(w)}}}',
        f'\\DLINE{{{fmt(x0)}}}{{{fmt(y1)}}}{{{fmt(x1)}}}{{{fmt(y1)}}}{{{fmt(w)}}}',
        f'\\DLINE{{{fmt(x0)}}}{{{fmt(y0)}}}{{{fmt(x0)}}}{{{fmt(y1)}}}{{{fmt(w)}}}',
        f'\\DLINE{{{fmt(x1)}}}{{{fmt(y0)}}}{{{fmt(x1)}}}{{{fmt(y1)}}}{{{fmt(w)}}}',
    ]


out = []

# ---- 2(i) LS setup line (y=215.06, sz=11.04) ----
out += center_in_gap(255.93, 282.65, 215.06, C7, 11.04)
out += center_in_gap(288.60, 316.87, 215.06, C8, 11.04)

# ---- 2(ii) RS setup line (y=292.25, sz=11.04) ----
out += center_in_gap(286.41, 313.15, 292.25, C8, 11.04)
out += center_in_gap(318.40, 360.55, 292.25, C7, 11.04)
out += center_in_gap(366.50, 398.23, 292.25, C8, 11.04)

# ---- table substituted header row (y=478.87, sz=11.04) ----
out += center_in_gap(141.54, 153.74, 478.87, C7, 11.04)   # col1 p_q
out += center_in_gap(188.12, 197.93, 478.87, C7, 11.04)   # col2 inner (p_q)
out += center_in_gap(208.46, 223.25, 478.87, C8, 11.04)   # col2 outer _r
out += center_in_gap(261.45, 273.65, 478.87, C8, 11.04)   # col3 p_r
out += center_in_gap(315.72, 328.15, 478.87, C8, 11.04)   # col4 q_r
out += center_in_gap(372.25, 389.35, 478.87, C8, 11.04)   # col5 inner-left
out += center_in_gap(399.18, 413.95, 478.87, C7, 11.04)   # col5 outer
out += center_in_gap(424.48, 441.70, 478.87, C8, 11.04)   # col5 inner-right

# ---- value columns, 8 rows, col mids from the header spans ----
rows = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
        (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
ys = [503.70, 517.90, 546.20, 560.30, 588.70, 602.80, 631.30, 645.50]
mid = {
    'c1': (134.66 + 160.41) / 2,     # pC7q
    'c2': (178.46 + 227.54) / 2,     # (pC7q)C8r = LS
    'c3': (255.89 + 278.54) / 2,     # pC8r
    'c4': (310.25 + 332.92) / 2,     # qC8r
    'c5': (369.31 + 443.94) / 2,     # (pC8r)C7(qC8r) = RS
    'c6': (473.02 + 525.98) / 2,     # LS<=>RS
}
for (p, q, r), y in zip(rows, ys):
    c1 = AND(p, q)
    c2 = IFF(c1, r)          # LS
    c3 = IFF(p, r)
    c4 = IFF(q, r)
    c5 = AND(c3, c4)         # RS
    c6 = IFF(c2, c5)         # LS<=>RS
    for key, val in [('c1', c1), ('c2', c2), ('c3', c3), ('c4', c4),
                      ('c5', c5), ('c6', c6)]:
        a = R(str(val), 11.04, font='b')
        out += a.emit(mid[key] - a.w / 2, y)

# box the LS<=>RS answer column (SOL2B-2024's own convention, "See the boxed
# ones" written directly on its page 507) -- outer grid-line coordinates
# measured directly off 163Exm2B.pdf via a 300dpi ink-scan (dark-fraction
# >0.8 across the column band), not estimated from the value-centering mid[]
# above: left/right column border at x=464.52/534.36, top of the first row
# to bottom of the last row (spanning the 3 blank separator rows too, same
# as the exhibit's own box) at y=495.72/651.48.
out += box(464.52, 495.72, 534.36, 651.48)

# ---- closing decision line (y=712.90) ----
out += center_in_gap(124.26, 136.46, 712.90, C7, 11.04)    # LS inner
out += center_in_gap(142.41, 160.94, 712.90, C8, 11.04)    # LS outer
out += center_in_gap(224.13, 233.93, 712.90, C8, 11.04)    # RS inner-left
out += center_in_gap(239.18, 271.61, 712.90, C7, 11.04)    # RS outer
out += center_in_gap(277.56, 292.37, 712.90, C8, 11.04)    # RS inner-right

# verdict: LS<=>RS is NOT a tautology (verified: counterexamples at
# (p,q,r)=(0,1,0) and (1,0,0)) -> circle N; Pf always circled alongside
# whichever of Y/N holds (a completed truth table is the Pf), per the
# Y-N-Pf-W convention confirmed from both solved exhibits.
out += circle_token(396.07, 406.35, 712.90, 14.04)   # N
out += circle_token(432.07, 448.50, 712.90, 14.04)   # Pf

with open('pages/answers507.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers507.tex')
