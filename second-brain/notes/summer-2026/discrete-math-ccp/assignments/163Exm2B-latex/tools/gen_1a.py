#!/usr/bin/env python3
"""1a printed-page answers: connective-symbol fills (Ck -> actual glyph) and
truth-table value fills, both sub-parts (i) and (ii). Every blank's gap is
computed from the neighboring already-printed tokens' own measured x/width
(read off gen2.py's trace of page506.tex), not eyeballed -- same discipline
as 1C/1B's fit_centered(). Sri's connectives: C1=C2=C3=OR, C4=C5=AND,
C6=IFF -- so 1a(i) is a flat tautology (contains p and not-p as bare
disjuncts) by construction, not an error.
"""
import sys
sys.path.insert(0, '.')
from atoms import R


def center_in_gap(left_end_x, right_start_x, y, text, sz, font='c'):
    a = R(text, sz, font=font)
    x = left_end_x + (right_start_x - left_end_x - a.w) / 2
    return a.emit(x, y)


def OR(a, b): return 1 if (a or b) else 0
def AND(a, b): return 1 if (a and b) else 0
def IFF(a, b): return 1 if (a == b) else 0
def NOT(a): return 1 - a


C1 = C2 = C3 = '∨'
C4 = C5 = '∧'
C6 = '⟷'

out = []

# ============================================================== 1a(i) =====
# top summary line, RHS of "=" (y=130.46/130.10 mixed by token)
p_end = 344.95 + R('𝑝', 14.04).w
out += center_in_gap(p_end, 377.47, 130.46, C1, 14.04)              # C1
g2r_end = 409.39 + R(')', 12.96).w
out += center_in_gap(g2r_end, 438.82, 130.10, C2, 14.04)            # C2
g3l_end = 471.34 + R(')', 12.96).w
out += center_in_gap(g3l_end, 498.46, 130.46, C3, 14.04)            # C3

# header row 2, sub-columns (y=249.50/249.14)
p2_end = 202.85 + R('𝑝', 11.04).w
out += center_in_gap(p2_end, 226.01, 249.50, C1, 11.04)             # left subcol
np_end = 283.61 + R('(¬𝑝)', 11.04).w
out += center_in_gap(np_end, 329.11, 249.50, C3, 11.04)             # right subcol

# header row 2, combined column (y=250.10/250.46) -- 3 gaps
p3_end = 371.59 + R('𝑝', 11.04).w
out += center_in_gap(p3_end, 394.75, 250.10, C1, 11.04)
nq3_end = 394.75 + R('(¬𝑞)', 11.04).w
out += center_in_gap(nq3_end, 450.10, 250.10, C2, 11.04)
np3_end = 450.10 + R('(¬𝑝)', 11.04).w
out += center_in_gap(np3_end, 490.66, 250.46, C3, 11.04)

# value columns: rows (p,q) in printed order, y-positions from the already-
# printed p/q/not-p/not-q value columns on this page.
rows_i = [(0, 0), (0, 1), (1, 0), (1, 1)]
ys_i = [279.20, 293.30, 321.60, 335.80]
mid_left = (204.77 + 281.93) / 2     # under header span "p C1(not q)"
mid_right = (287.81 + 400.87) / 2    # under header span "(not p)C3 q"
mid_comb = (400.15 + 466.18) / 2     # under the combined-column parens
for (p, q), y in zip(rows_i, ys_i):
    left = OR(p, NOT(q))
    right = OR(NOT(p), q)
    comb = OR(left, right)
    for mid, val in [(mid_left, left), (mid_right, right), (mid_comb, comb)]:
        a = R(str(val), 11.04, font='b')
        out += a.emit(mid - a.w / 2, y)

# ============================================================= 1a(ii) =====
# top summary line RHS (y=425.09/424.61)
p4_end = 248.45 + R('𝑝', 14.04).w
out += center_in_gap(p4_end, 273.41, 425.09, C4, 14.04)
g1_end = 281.45 + R(')', 14.04).w
out += center_in_gap(g1_end, 313.99, 425.09, C5, 14.04)
q6_end = 322.51 + R('𝑞', 14.04).w
out += center_in_gap(q6_end, 349.87, 425.09, C6, 14.04)

# header row 2, sub-columns (y=522.19/521.83)
p5_end = 204.53 + R('𝑝', 11.04).w
out += center_in_gap(p5_end, 232.61, 522.19, C4, 11.04)
q5_end = 277.13 + R('𝑞', 11.04).w
out += center_in_gap(q5_end, 300.29, 522.19, C6, 11.04)

# combined column (y=521.83/522.19) -- 2 gaps
p6_end = 355.03 + R('(𝑝', 11.04).w
out += center_in_gap(p6_end, 380.47, 521.83, C4, 11.04)
q6c_end = 380.47 + R('𝑞)', 11.04).w
out += center_in_gap(q6c_end, 410.59, 522.19, C5, 11.04)
q7_end = 410.59 + R('(𝑞', 11.04).w
out += center_in_gap(q7_end, 438.46, 521.83, C6, 11.04)

rows_ii = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
           (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
ys_ii = [549.80, 563.90, 592.30, 606.50, 634.90, 649.10, 677.40, 691.50]
mid_left2 = (209.93 + 227.33 + R('𝑞', 11.04).w) / 2 + 8
mid_right2 = (280.13 + 297.41 + R('𝑟', 11.04).w) / 2 + 8
mid_comb2 = (364.03 + 429.67 + R('𝑟)', 11.04).w) / 2
for (p, q, r), y in zip(rows_ii, ys_ii):
    left = AND(p, q)
    right = IFF(q, r)
    comb = AND(left, right)
    for mid, val in [(mid_left2, left), (mid_right2, right), (mid_comb2, comb)]:
        a = R(str(val), 11.04, font='b')
        out += a.emit(mid - a.w / 2, y)

with open('pages/answers506.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers506.tex')
