#!/usr/bin/env python3
"""1b facing-side work (page 609): consensus-method reduction chain from
E's canonical form down to PI(E)={x,y}/MSOP(E)=x+y. Verified independently
via Quine-McCluskey; chain mirrors SOL2C's own demonstrated grouping
(adjacent same-prefix pairs first)."""
import sys
sys.path.insert(0, '.')
from atoms import R, HB, Chain, cvar, smart, wrap

SZ = 12.96
out = []


def t(bits):
    names = ['𝑥', '𝑦', '𝑧']
    return HB(*[cvar(n, comp=(b == 0), sz=SZ) for n, b in zip(names, bits)])


def row(*terms):
    parts = [terms[0]]
    for x in terms[1:]:
        parts.append(R(' + ', SZ, font='c'))
        parts.append(x)
    return HB(*parts)


xyz, xyz1, xy1z, xy1z1, x1yz, x1yz1 = t((1,1,1)), t((1,1,0)), t((1,0,1)), t((1,0,0)), t((0,1,1)), t((0,1,0))
xy = HB(cvar('𝑥', sz=SZ), cvar('𝑦', sz=SZ))
xy1 = HB(cvar('𝑥', sz=SZ), cvar('𝑦', True, sz=SZ))
x1y = HB(cvar('𝑥', True, sz=SZ), cvar('𝑦', sz=SZ))
xatom, yatom = R('𝑥', SZ, font='c'), R('𝑦', SZ, font='c')

rows = [
    row(xyz, xyz1, xy1z, xy1z1, x1yz, x1yz1),
    row(xy1z, xy1z1, x1yz, x1yz1, xy),
    row(x1yz, x1yz1, xy, xy1),
    row(xy, xy1, x1y),
    row(xy1, yatom),
    row(yatom, xatom),
]
SM = 9.5
cites = [
    None,
    'consensus of terms 1,2',
    'consensus of terms 1,2 (new list)',
    'consensus of terms 1,2 (new list)',
    'consensus of terms 1,2; result absorbs both',
    'consensus of terms 1,2; result absorbs term 1',
]
cites = [smart('  (' + c + ')', SM, font='b') if c else None for c in cites]

label = smart('𝐸(𝑥,𝑦,𝑧)', SZ, font='c')
out += label.emit(108.02, 110.0)

indent = R('+', SZ, font='c').w + 8
chain = Chain(rows[0], [('=', r) for r in rows[1:]], sz=SZ, rowgap=8.0, indent=indent)
out += chain.emit(144.02, 138.0)

for cy, ct in zip(chain.ys, cites):
    if ct:
        out += ct.emit(400.0, 138.0 + cy)

final_y = 138.0 + chain.ys[-1] + rows[-1].dp + 20
pi_set = wrap(HB(xatom, R(', ', SZ, font='b'), yatom), l='{', r='}', sz=SZ)
concl1 = smart('So 𝑃𝐼(𝐸)=', SZ, font='b')
out += concl1.emit(108.02, final_y)
out += pi_set.emit(108.02 + concl1.w + 4, final_y)
concl2 = smart('  and 𝑀𝑆𝑂𝑃(𝐸)=', SZ, font='b')
concl2_x = 108.02 + concl1.w + 4 + pi_set.w
out += concl2.emit(concl2_x, final_y)
msop_atom = row(xatom, yatom)
out += msop_atom.emit(concl2_x + concl2.w, final_y)

with open('pages/answers609.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers609.tex')
