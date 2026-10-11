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
    (437.00, [(1, 2), (2, 4)]),                                   # 1a
    (454.90, [(1, 2), (2, 2), (3, 2)]),                           # 1b
    (472.70, [(1, 5)]),                                           # 1c
    (508.60, [(1, 6)]),                                           # 2a
    (526.50, [(1, 4), (2, 2)]),                                   # 2b
    (544.40, [(1, 5)]),                                           # 2c
    (580.20, [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)]),   # 3a
    (598.00, [(1, 6)]),                                           # 3b
    (616.00, [(1, 5)]),                                           # 3c
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

with open('pages/answers500.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers500.tex; total={total}')
