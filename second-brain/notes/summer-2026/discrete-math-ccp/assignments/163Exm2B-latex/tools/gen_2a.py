#!/usr/bin/env python3
"""2a (p510): T1..T8 truth-table fills, phi1..phi8 canonical-DNF indicator
columns, and the 6-line assembled DNF (LHS: phi_k(p,q,r) citations, RHS:
the actual minterms). T1..T8 = 0,0,1,1,1,1,1,1 (Sri's J-number 00499317 ->
keep 0s, replace nonzero with 1). True rows are a contiguous block from the
bottom (rows 3..8), so the exhibits' dynamic bottom-up phi-numbering and
the Logic Notes' own fixed reference table agree here (see Rules.md flag) --
phi1=row8(111) ... phi6=row3(010).
"""
import sys
sys.path.insert(0, '.')
from atoms import R, HB

T = [0, 0, 1, 1, 1, 1, 1, 1]
ROWS = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
        (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
NP, NQ = '¬𝑝', '¬𝑞'

out = []

# ---- Tk = value fills ----
t_ys = [186.38, 200.54, 228.86, 243.00, 271.37, 285.53, 313.97, 328.13]
for y, t in zip(t_ys, T):
    out += R(str(t), 11.04, font='b').emit(183.5, y)

# ---- phi1..phi8 indicator columns ----
# true rows scanning bottom-up: row8->phi1, row7->phi2, ..., row3->phi6
phi_col_x = {1: 220.97, 2: 259.25, 3: 295.25, 4: 333.67, 5: 371.83,
             6: 412.27, 7: 452.86, 8: 491.14}
active_phi_by_row = {8: 1, 7: 2, 6: 3, 5: 4, 4: 5, 3: 6}  # 1-based row -> phi#
row_ys = [186.38, 200.54, 228.86, 243.00, 271.37, 285.53, 313.97, 328.13]
for i, y in enumerate(row_ys):
    rn = i + 1
    active = active_phi_by_row.get(rn)
    for k in range(1, 9):
        val = 1 if k == active else 0
        a = R(str(val), 11.04, font='b')
        cx = phi_col_x[k] + 6.0  # roughly centered under the phi_k header
        out += a.emit(cx - a.w / 2, y)

# ---- assembled DNF, 6 lines (phi1..phi6 are the active ones) ----
def lit(varname, sign):
    return varname if sign else ('¬' + varname)


active_rows_bottom_up = [8, 7, 6, 5, 4, 3]  # phi1..phi6
row_bits = {1: (0, 0, 0), 2: (0, 0, 1), 3: (0, 1, 0), 4: (0, 1, 1),
            5: (1, 0, 0), 6: (1, 0, 1), 7: (1, 1, 0), 8: (1, 1, 1)}

# pre-printed "=" signs sit at (108.02,428.90)/(324.07,428.90) -- content
# must start AFTER them, not at the same x (first pass placed phi1 right on
# top of the "=", rendering as a stray overline through the glyph; caught
# by looking at the actual render, not just a clean xelatex exit).
lhs_eq_end = 108.02 + R('=', 15.96).w
rhs_eq_end = 324.07 + R('=', 15.96).w
lhs_content_x = lhs_eq_end + 4.0
rhs_content_x = rhs_eq_end + 4.0
or_w = R('∨', 11.04).w
y0 = 428.90
rowgap = 22.0
for i, rn in enumerate(active_rows_bottom_up):
    k = i + 1
    p, q, r = row_bits[rn]
    y = y0 + i * rowgap
    lhs = HB(R('𝜑', 11.04), R(str(k), 8.04), R('(𝑝,𝑞,𝑟)', 11.04))
    if i == 0:
        out += lhs.emit(lhs_content_x, y)
    else:
        out += R('∨', 11.04).emit(lhs_content_x - or_w - 2.0, y)
        out += lhs.emit(lhs_content_x, y)
    parts = [lit('𝑝', p), R('∧', 11.04), lit('𝑞', q), R('∧', 11.04), lit('𝑟', r)]
    inner = HB(*[R(t, 11.04) if isinstance(t, str) else t for t in parts])
    term = HB(R('(', 11.04), inner, R(')', 11.04))
    if i == 0:
        out += term.emit(rhs_content_x, y)
    else:
        out += R('∨', 11.04).emit(rhs_content_x - or_w - 2.0, y)
        out += term.emit(rhs_content_x, y)

with open('pages/answers510.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers510.tex')
