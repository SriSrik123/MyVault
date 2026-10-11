#!/usr/bin/env python3
"""1b printed-page answers (page 608): restate E(x,y,z), then PI(E) and
MSOP(E) via the consensus method (full chain lives on worksheet 6080).
Verified independently via Quine-McCluskey: PI(E)={x,y}, MSOP(E)=x+y.
"""
import sys
sys.path.insert(0, '.')
from atoms import R, HB, cvar, wrap

SZ = 12.96
out = []

E_terms_bits = [(1, 1, 1), (1, 1, 0), (1, 0, 1), (1, 0, 0), (0, 1, 1), (0, 1, 0)]


def baterm(p, q, r):
    return HB(cvar('𝑥', comp=(p == 0), sz=SZ), cvar('𝑦', comp=(q == 0), sz=SZ),
              cvar('𝑧', comp=(r == 0), sz=SZ))


parts = [baterm(*E_terms_bits[0])]
for bits in E_terms_bits[1:]:
    parts.append(R(' + ', SZ, font='c'))
    parts.append(baterm(*bits))
E_atom = HB(*parts)
out += E_atom.emit(216.05 + R('=', SZ, font='c').w + 8, 113.06)

# PI(E) = {x, y}  (braces have no plain-cmap glyph in this font -- route
# through wrap()'s math-mode \TDEL like every other delimiter in this project)
pi_inner = HB(cvar('𝑥', sz=SZ), R(', ', SZ, font='b'), cvar('𝑦', sz=SZ))
pi_atom = wrap(pi_inner, l='{', r='}', sz=SZ)
out += pi_atom.emit(398.95 + R('=', SZ, font='c').w + 8, 141.62)

# MSOP(E) = x + y
msop_atom = HB(cvar('𝑥', sz=SZ), R(' + ', SZ, font='c'), cvar('𝑦', sz=SZ))
out += msop_atom.emit(420.67 + R('=', SZ, font='c').w + 8, 170.18)

with open('pages/answers608.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers608.tex')
