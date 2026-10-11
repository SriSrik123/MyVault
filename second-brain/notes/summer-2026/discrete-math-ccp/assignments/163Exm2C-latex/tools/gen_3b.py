#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
from atoms import R, HB, sup

SZ = 12.96
out = []


def setlit(name, comp=False):
    a = R(name, SZ, font='c')
    if not comp:
        return a
    csup = sup(a, R('c', SZ * 0.72, font='b'))
    return HB(R('(', SZ), csup, R(')', SZ))


# H(A,B,C,D) = (C ∪ D^c) ∩ (A ∪ B ∪ C ∪ D) ∩ (A^c ∪ B ∪ C^c ∪ D)
f1 = HB(R('(', SZ), setlit('𝐶'), R(' ∪ ', SZ, font='c'), setlit('𝐷', True), R(')', SZ))
f2 = HB(R('(', SZ), setlit('𝐴'), R(' ∪ ', SZ, font='c'), setlit('𝐵'), R(' ∪ ', SZ, font='c'),
        setlit('𝐶'), R(' ∪ ', SZ, font='c'), setlit('𝐷'), R(')', SZ))
f3 = HB(R('(', SZ), setlit('𝐴', True), R(' ∪ ', SZ, font='c'), setlit('𝐵'), R(' ∪ ', SZ, font='c'),
        setlit('𝐶', True), R(' ∪ ', SZ, font='c'), setlit('𝐷'), R(')', SZ))
H_atom = HB(f1, R('∩', SZ), f2, R('∩', SZ), f3)
out += H_atom.emit(108.02 + R('=', SZ, font='c').w + 8, 228.90)

# K(A,B,C,D) = (A^c ∩ C) ∪ (C ∩ D) ∪ (B ∩ D^c) ∪ (A ∩ C^c ∩ D^c)
g1 = HB(R('(', SZ), setlit('𝐴', True), R('∩', SZ), setlit('𝐶'), R(')', SZ))
g2 = HB(R('(', SZ), setlit('𝐶'), R('∩', SZ), setlit('𝐷'), R(')', SZ))
g3 = HB(R('(', SZ), setlit('𝐵'), R('∩', SZ), setlit('𝐷', True), R(')', SZ))
g4 = HB(R('(', SZ), setlit('𝐴'), R('∩', SZ), setlit('𝐶', True), R('∩', SZ), setlit('𝐷', True), R(')', SZ))
K_atom = HB(g1, R(' ∪ ', SZ, font='c'), g2, R(' ∪ ', SZ, font='c'), g3,
            R(' ∪ ', SZ, font='c'), g4)
out += K_atom.emit(108.02 + R('=', SZ, font='c').w + 8, 371.80)

with open('pages/answers620.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers620.tex')
