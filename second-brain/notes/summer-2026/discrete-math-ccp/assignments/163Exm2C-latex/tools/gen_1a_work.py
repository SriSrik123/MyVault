#!/usr/bin/env python3
"""1a facing-side work (page 607): full parenthesized 6-term expansion of
phi(p,q,r) that the printed page's own budget couldn't fit (page 606 only
had room for the compact phi1 v phi2 v ... summary). Page 606's own
instruction licenses this: "...on the facing page and record the answers
on this page" -- 607 IS this problem's designated work area.
"""
import sys
sys.path.insert(0, '.')
from atoms import R, HB, Chain

SZ = 12.96
out = []


def pclit(v, name):
    if v == 1:
        return R(name, SZ, font='c')
    return HB(R('(', SZ), R('¬', SZ), R(name, SZ, font='c'), R(')', SZ))


def conj3(p, q, r):
    inner = HB(pclit(p, '𝑝'), R('∧', SZ), pclit(q, '𝑞'), R('∧', SZ), pclit(r, '𝑟'))
    return HB(R('(', SZ), inner, R(')', SZ))


PQR = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
       (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
true_rows = [8, 7, 6, 5, 4, 3]  # bottom-to-top true rows (phi1..phi6)

phi_label = HB(R('𝜑(', SZ, font='c'), R('𝑝,', SZ, font='c'), R('𝑞,', SZ, font='c'),
               R('𝑟)', SZ, font='c'))
out += phi_label.emit(108.02, 110.0)

terms = [conj3(*PQR[row - 1]) for row in true_rows]
chain_indent = R('∨', SZ, font='c').w + 8
chain = Chain(terms[0], [('∨', t) for t in terms[1:]], sz=SZ, rowgap=8.0,
              indent=chain_indent)
out += chain.emit(144.02, 138.0)

with open('pages/answers607.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers607.tex')
