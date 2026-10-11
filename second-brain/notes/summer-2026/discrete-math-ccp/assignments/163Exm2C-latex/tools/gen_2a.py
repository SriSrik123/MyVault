#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
from atoms import R, Chain
from gterms import G_formula, sop_terms, plus_join

SZ = 12.96
out = []

g = G_formula(SZ)
out += g.emit(213.05 + R('=', SZ, font='c').w + 8, 112.94)

terms = sop_terms(SZ)
sop = plus_join(terms, SZ)
out += sop.emit(216.05 + R('=', SZ, font='c').w + 8, 169.10)

with open('pages/answers612.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers612.tex')
