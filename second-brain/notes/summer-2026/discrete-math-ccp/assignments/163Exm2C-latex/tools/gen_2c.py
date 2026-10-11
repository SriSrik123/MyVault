#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
from atoms import R, HB, Chain, wrap
from gterms import G_formula, sop_terms, msop_terms, plus_join

SZ = 12.96
out = []

g = G_formula(SZ)
out += g.emit(213.05 + R('=', SZ, font='c').w + 8, 112.94)

sop = plus_join(sop_terms(SZ), SZ)
out += sop.emit(262.85 + R('=', SZ, font='c').w + 8, 197.78)

from gterms import csop_terms
csop = csop_terms(SZ)
# only ~57pt before the next label ("2(i) PI(G)=" at y=283.49) -- pack
# several terms/line instead of 2b's spacious one-per-line restatement.
csz = 10.0
csop_small = csop_terms(csz)
lines3 = [csop_small[i:i + 4] for i in range(0, len(csop_small), 4)]


def row_join(terms):
    parts = [terms[0]]
    for t in terms[1:]:
        parts.append(R(' + ', csz, font='c'))
        parts.append(t)
    return HB(*parts)


c_rows = [row_join(r) for r in lines3]
c_indent = R('+', csz, font='c').w + 6
csop_chain = Chain(c_rows[0], [('+', r) for r in c_rows[1:]], sz=csz, rowgap=2.0,
                    indent=c_indent)
out += csop_chain.emit(273.53 + R('=', SZ, font='c').w + 8, 226.34)

# PI(G) = {w'y, wy'z', xy, xz', yz}
def prod(*lits, sz=SZ):
    from atoms import cvar
    return HB(*[cvar(n, comp=c, sz=sz) for n, c in lits])


pi_w1y = prod(('𝑤', True), ('𝑦', False))
pi_wy1z1 = prod(('𝑤', False), ('𝑦', True), ('𝑧', True))
pi_xy = prod(('𝑥', False), ('𝑦', False))
pi_xz1 = prod(('𝑥', False), ('𝑧', True))
pi_yz = prod(('𝑦', False), ('𝑧', False))
pi_inner = HB(pi_w1y, R(', ', SZ, font='b'), pi_wy1z1, R(', ', SZ, font='b'),
              pi_xy, R(', ', SZ, font='b'), pi_xz1, R(', ', SZ, font='b'), pi_yz)
pi_atom = wrap(pi_inner, l='{', r='}', sz=SZ)
out += pi_atom.emit(252.29 + R('=', SZ, font='c').w + 8, 283.49)

msop = plus_join(msop_terms(SZ), SZ)
out += msop.emit(276.77 + R('=', SZ, font='c').w + 8, 340.73)

with open('pages/answers616.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers616.tex')
