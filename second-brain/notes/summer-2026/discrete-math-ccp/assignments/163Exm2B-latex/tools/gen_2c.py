#!/usr/bin/env python3
"""2c (p512): Vld((p C3 q)->p, (p C3 q)->q / (p C3 q)->(p C5 q)) via algebra
of propositions. C3=OR, C5=AND for Sri. Verified VALID (Y): premises both
true only at (p,q)=(0,0) and (1,1), and the conclusion holds at both.
"""
import sys
sys.path.insert(0, '.')
from atoms import R, center_in_gap, circle_token

C3, C5 = '∨', '∧'
out = []

# "My problem" numerator: two premises, each with one C3 gap
out += center_in_gap(200.63, 216.77, 346.44, C3, 11.52)
out += center_in_gap(299.15, 315.31, 346.44, C3, 11.52)

# "My problem" denominator: C3 then C5
out += center_in_gap(227.87, 249.05, 411.96, C3, 11.52)
out += center_in_gap(295.31, 313.99, 411.96, C5, 11.52)

# both Vld boxes: VALID -> Y + Pf
out += circle_token(396.07, 405.69, 208.94, 15.96)   # Y, box 1 (raw)
out += circle_token(468.10, 486.77, 208.94, 15.96)   # Pf, box 1
out += circle_token(396.07, 403.30, 380.93, 12.00)   # Y, box 2 ("My problem")
out += circle_token(468.10, 482.14, 380.93, 12.00)   # Pf, box 2

with open('pages/answers512.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers512.tex')
