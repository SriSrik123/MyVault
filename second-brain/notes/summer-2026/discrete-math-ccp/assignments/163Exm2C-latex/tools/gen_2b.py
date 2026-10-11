#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
from atoms import R, Chain
from gterms import G_formula, csop_terms

SZ = 12.96
out = []

g = G_formula(SZ)
out += g.emit(213.05 + R('=', SZ, font='c').w + 8, 112.94)

terms = csop_terms(SZ)
indent = R('+', SZ, font='c').w + 8
chain = Chain(terms[0], [('+', t) for t in terms[1:]], sz=SZ, rowgap=4.0,
              indent=indent)
out += chain.emit(216.05 + R('=', SZ, font='c').w + 8, 171.14)

with open('pages/answers614.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers614.tex')
