#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
from atoms import R, HB, smart, circle_token
from gterms import sop_terms, msop_terms, plus_join

SZ = 12.96
out = []

# A := SOP(G(w,x,y,z)) =  (value)
sop = plus_join(sop_terms(SZ), SZ)
out += sop.emit(280.13 + R('=', SZ, font='c').w + 8, 114.02)

# B = MSOP(G(w,x,y,z)) =  (value)
msop = plus_join(msop_terms(SZ), SZ)
out += msop.emit(287.69 + R('=', SZ, font='c').w + 8, 144.14)

# A_S=5, A_L=11, B_S=4, B_L=9
vals = [(128.06, 229.10, '5'), (236.45, 229.10, '11'),
        (343.87, 229.10, '4'), (452.26, 229.10, '9')]
for x0, y0, v in vals:
    a = R(v, SZ, font='c')
    out += a.emit(x0 + R('=', SZ, font='c').w + 6, y0)

# circle Smplr(B,A) -- printed token spans roughly x=252.05..332 at y=286.25
out += circle_token(250.0, 335.0, 286.25, SZ)

# Why?
why = smart('  (𝐵𝐿=9<11=𝐴𝐿) and (𝐵𝑆=4≤5=𝐴𝑆), so 𝑆𝑚𝑝𝑙𝑟(𝐵,𝐴) holds by definition.',
            11.04, font='b')
out += why.emit(146.02, 314.90)

# psi(p,q,r,s) = version of G(w,x,y,z) in PC (w->p, x->q, y->r, z->s)
P, Q, R_, S = '𝑝', '𝑞', '𝑟', '𝑠'


def lit(name, comp=False):
    a = R(name, SZ, font='c')
    return a if not comp else HB(R('¬', SZ), a)


f1 = HB(R('(', SZ), lit(R_), R(' ∨ ', SZ, font='c'), lit(S, True), R(')', SZ))
f2 = HB(R('(', SZ), lit(P), R(' ∨ ', SZ, font='c'), lit(Q), R(' ∨ ', SZ, font='c'),
        lit(R_), R(' ∨ ', SZ, font='c'), lit(S), R(')', SZ))
f3 = HB(R('(', SZ), lit(P, True), R(' ∨ ', SZ, font='c'), lit(Q), R(' ∨ ', SZ, font='c'),
        lit(R_, True), R(' ∨ ', SZ, font='c'), lit(S), R(')', SZ))
psi = HB(f1, R('∧', SZ), f2, R('∧', SZ), f3)
out += psi.emit(108.02 + R('=', SZ, font='c').w + 8, 447.80)

with open('pages/answers618.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers618.tex')
