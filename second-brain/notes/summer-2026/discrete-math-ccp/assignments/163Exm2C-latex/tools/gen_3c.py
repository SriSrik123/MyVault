#!/usr/bin/env python3
"""3c printed-page proof (page 621): H(A,B,C,D)=K(A,B,C,D) in Sets.
No solved exhibit covers 3c on this exam (same "prove that" gap class as
1c throughout this project). Proof strategy: BA and Sets are isomorphic
Boolean algebras under the correspondence w,x,y,z<->A,B,C,D (complement
<->complement, + <->union, juxtaposition<->intersection) -- H is exactly
this correspondence applied to G(w,x,y,z), and K is the same
correspondence applied to MSOP(G(w,x,y,z)). Since G=MSOP(G) was
established via the consensus method (2c), applying the SAME
correspondence to both sides of that BA identity gives H=K directly."""
import sys
sys.path.insert(0, '.')
from atoms import R, HB, smart

SZ = 12.96
out = []

lines = [
    'The correspondence 𝑤,𝑥,𝑦,𝑧 to 𝐴,𝐵,𝐶,𝐷 together with complement to',
    'complement, + to union, and juxtaposition to intersection is a',
    'Boolean-algebra isomorphism between BA and Sets (both are the free',
    'Boolean algebra on 4 generators). By definition, 𝐻(𝐴,𝐵,𝐶,𝐷) is',
    'exactly this isomorphism applied to 𝐺(𝑤,𝑥,𝑦,𝑧), and 𝐾(𝐴,𝐵,𝐶,𝐷) is',
    'the same isomorphism applied to 𝑀𝑆𝑂𝑃(𝐺(𝑤,𝑥,𝑦,𝑧)).',
    '',
    'In (2c), the consensus method established, in BA:',
]

y = 140.0
for ln in lines:
    a = smart(ln, SZ, font='b')
    out += a.emit(108.02, y)
    y += 22.0

from gterms import msop_terms, plus_join
lhs = HB(R('𝐺(𝑤,', SZ, font='c'), R('𝑥,', SZ, font='c'), R('𝑦,', SZ, font='c'),
         R('𝑧)', SZ, font='c'))
rhs = plus_join(msop_terms(SZ), SZ)
eq_atom = HB(lhs, R('  =  ', SZ, font='c'), rhs)
out += eq_atom.emit(144.02, y)
y += 32.0

more = [
    'A Boolean-algebra isomorphism preserves every identity, so applying',
    'the same correspondence to both sides of this identity gives, in Sets:',
]
for ln in more:
    a = smart(ln, SZ, font='b')
    out += a.emit(108.02, y)
    y += 22.0

Hlbl = HB(R('𝐻(𝐴,', SZ, font='c'), R('𝐵,', SZ, font='c'), R('𝐶,', SZ, font='c'), R('𝐷)', SZ, font='c'))
Klbl = HB(R('𝐾(𝐴,', SZ, font='c'), R('𝐵,', SZ, font='c'), R('𝐶,', SZ, font='c'), R('𝐷)', SZ, font='c'))
concl = HB(Hlbl, R('  =  ', SZ, font='c'), Klbl)
out += concl.emit(144.02, y)
y += 26.0
out += smart('as required.', SZ, font='b').emit(144.02, y)

with open('pages/answers621.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers621.tex')
