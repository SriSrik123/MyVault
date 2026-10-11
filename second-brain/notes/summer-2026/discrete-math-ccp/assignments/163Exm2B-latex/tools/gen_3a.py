#!/usr/bin/env python3
"""3a (p513): six Tlg/Cdn/Cng classifications. Each row's RHS (after "=")
has 2 connective blanks; verdict circled below. Hand+programmatically
verified (verify_2b.py): alpha=Tlg, beta=Tlg, gamma=Cng, delta=Cdn,
zeta=Cdn, eta=Cng.
"""
import sys
sys.path.insert(0, '.')
from atoms import center_in_gap, circle_token

V, A, IFF = '∨', '∧', '⟷'
out = []

# alpha: C1=OR, C3=OR
out += center_in_gap(239.92, 255.89, 162.50, V, 12.00)
out += center_in_gap(267.56, 281.57, 162.50, V, 12.00)
out += circle_token(324.07, 359.50, 202.10, 12.00)   # Tlg

# beta: C2=OR (outer), C4=AND (inner)
out += center_in_gap(235.30, 251.21, 267.77, V, 12.00)
out += center_in_gap(262.88, 279.65, 267.77, A, 12.00)
out += circle_token(324.07, 359.58, 307.49, 12.00)   # Tlg

# gamma: C3=OR (inner), C5=AND (outer)
out += center_in_gap(235.83, 252.41, 374.09, V, 12.00)
out += center_in_gap(264.08, 280.13, 374.09, A, 12.00)
out += circle_token(468.10, 505.75, 413.69, 12.00)   # Cng

# delta: C4=AND (outer), C6=IFF (inner)
out += center_in_gap(237.09, 250.97, 479.47, A, 12.00)
out += center_in_gap(262.64, 278.69, 479.47, IFF, 12.00)
out += circle_token(396.07, 433.33, 519.07, 12.00)   # Cdn

# zeta: C5=AND (outer), C7=AND (inner)
out += center_in_gap(233.86, 249.77, 585.67, A, 12.00)
out += center_in_gap(261.44, 275.45, 585.67, A, 12.00)
out += circle_token(396.07, 432.73, 625.42, 12.00)   # Cdn

# eta: C6=IFF (inner), C8=IFF (outer)
out += center_in_gap(230.98, 246.89, 691.18, IFF, 12.00)
out += center_in_gap(258.71, 277.85, 691.18, IFF, 12.00)
out += circle_token(468.10, 506.32, 730.90, 12.00)   # Cng

with open('pages/answers513.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers513.tex')
