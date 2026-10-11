#!/usr/bin/env python3
"""500: cover grading table. Point values per part read directly off the
blank exam's own printed numeral prefixes (e.g. "6 (1a)", then "2(i)"/
"4(ii)" for its sub-parts) -- same extraction method as 2A's gen_400.py.
Filled with full expected credit on every part, matching this session's
actual completion state (all 9 problems' printed pages done and verified;
worksheets completed in the same pass -- see project memory).
"""
import sys
sys.path.insert(0, '.')
from atoms import R

# (row_y, [(part_col_x, points), ...])
part_x = {1: 130.0, 2: 159.5, 3: 188.5, 4: 217.7, 5: 246.9, 6: 276.1, 7: 305.3, 8: 334.5, 9: 366.0}
rows = [
    (437.00, [(1, 4), (2, 1), (3, 1)]),   # 1a: 4(i) phi, 1(ii) F(A,B,C), 1(iii) E(x,y,z)
    (454.90, [(1, 3), (2, 3)]),           # 1b: 3(i) PI(E), 3(i) MSOP(E) [exam labels both '(i)']
    (472.70, [(1, 1), (2, 4)]),           # 1c: 1(i) psi, 4(ii) prove phi=psi
    (508.60, [(1, 6)]),                   # 2a: single part, no sub-numbering on the page
    (526.50, [(1, 6)]),                   # 2b: single part, no sub-numbering on the page
    (544.40, [(1, 2), (2, 3)]),           # 2c: 2(i) PI(G), 3(ii) MSOP(G)
    (580.20, [(1, 1), (2, 1), (3, 4)]),   # 3a: 1(i) As/AL/Bs/BL, 1(ii) circle+why, 4(iii) PC+tree
    (598.00, [(1, 1), (2, 1)]),           # 3b: 1(i) H, 1(i) K [exam labels both '(i)']
    (616.00, [(1, 9)]),                   # 3c: single proof part
]
EXP_X = 423.0

out = []
total = 0
for y, parts in rows:
    row_total = sum(p for _, p in parts)
    total += row_total
    for col, pts in parts:
        a = R(str(pts), 11.04, font='b')
        out += a.emit(part_x[col] - a.w / 2, y)
    a = R(str(row_total), 14.04, font='b')
    out += a.emit(EXP_X - a.w / 2, y)

a = R(str(total), 14.04, font='b')
out += a.emit(EXP_X - a.w / 2, 651.80)

with open('pages/answers600.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers600.tex; total={total}')
