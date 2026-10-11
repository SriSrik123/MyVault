#!/usr/bin/env python3
"""505: J-number restatement blank, T-number blank, T1..T8 fills.
Keep every 0 digit, replace every nonzero digit with 1.
"""
import sys
sys.path.insert(0, '.')
from atoms import R

J = [0, 0, 4, 9, 9, 3, 1, 7]
T = [0 if d == 0 else 1 for d in J]
out = []

out += R('00499317', 11.04, font='b').emit(292.0, 109.70)
out += R('00111111', 11.04, font='b').emit(292.0, 176.90)

t_ys = [272.57, 301.49, 330.29, 359.21, 388.01, 416.93, 445.87, 474.67]
for y, v in zip(t_ys, T):
    # digit 0 (U+0030) missing from CambriaM; other digit fills across this
    # project always route through Book Antiqua for exactly this reason.
    out += R(str(v), 14.04, font='b').emit(106.0, y)

with open('pages/answers505.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers505.tex; T={T}')
