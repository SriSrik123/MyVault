#!/usr/bin/env python3
"""3c (p517): Vld(p C2 q, q C4 r, r C6 s / p C8 q). C2=OR,C4=AND,C6=IFF,
C8=IFF for Sri. Verified INVALID (N): countermodel p=0,q=1,r=1,s=1 makes
all 3 premises true but the conclusion p<->q false.
"""
import sys
sys.path.insert(0, '.')
from atoms import center_in_gap, circle_token

C2, C4, C6, C8 = '∨', '∧', '⟷', '⟷'
out = []

# "My problem" premises (y=231.26): 3 gaps
out += center_in_gap(187.37, 208.01, 231.26, C2, 9.96)
out += center_in_gap(231.85, 250.49, 231.26, C4, 9.96)
out += center_in_gap(270.83, 291.53, 231.26, C6, 9.96)

# "My problem" conclusion (y=266.57): 1 gap
out += center_in_gap(227.36, 250.25, 266.57, C8, 9.96)

# both Vld boxes: INVALID -> N + Pf
out += circle_token(396.07, 406.35, 139.94, 14.04)   # N, box 1
out += circle_token(432.07, 448.50, 139.94, 14.04)   # Pf, box 1
out += circle_token(396.07, 406.35, 249.62, 14.04)   # N, box 2
out += circle_token(432.07, 448.50, 249.62, 14.04)   # Pf, box 2

with open('pages/answers517.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers517.tex')
