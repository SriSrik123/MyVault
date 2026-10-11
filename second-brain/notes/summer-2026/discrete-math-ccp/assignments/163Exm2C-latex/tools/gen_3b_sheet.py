#!/usr/bin/env python3
"""Worksheet 6200 (work for problem on page 620, tags '3b.i'/'3b.ii'):
minimal over/under restatement of G->H and MSOP(G)->K, matching the
peer-reference's own minimal-restatement style for this problem (folio
6200 of Math163AdityaRayapudi.pdf shows no further derivation beyond
this -- H/K's Sets translation is a direct term-by-term substitution,
not something with intermediate algebra to show).
"""
import sys
sys.path.insert(0, '.')
from atoms import R, HB, sup, fmt
from gterms import G_formula, msop_terms, plus_join

SZ = 12.96
out = []


def setlit(name, comp=False):
    a = R(name, SZ, font='c')
    if not comp:
        return a
    csup = sup(a, R('c', SZ * 0.72, font='b'))
    return HB(R('(', SZ), csup, R(')', SZ))


f1 = HB(R('(', SZ), setlit('𝐶'), R(' ∪ ', SZ, font='c'), setlit('𝐷', True), R(')', SZ))
f2 = HB(R('(', SZ), setlit('𝐴'), R(' ∪ ', SZ, font='c'), setlit('𝐵'), R(' ∪ ', SZ, font='c'),
        setlit('𝐶'), R(' ∪ ', SZ, font='c'), setlit('𝐷'), R(')', SZ))
f3 = HB(R('(', SZ), setlit('𝐴', True), R(' ∪ ', SZ, font='c'), setlit('𝐵'), R(' ∪ ', SZ, font='c'),
        setlit('𝐶', True), R(' ∪ ', SZ, font='c'), setlit('𝐷'), R(')', SZ))
H_atom = HB(f1, R('∩', SZ), f2, R('∩', SZ), f3)

g1 = HB(R('(', SZ), setlit('𝐴', True), R('∩', SZ), setlit('𝐶'), R(')', SZ))
g2 = HB(R('(', SZ), setlit('𝐶'), R('∩', SZ), setlit('𝐷'), R(')', SZ))
g3 = HB(R('(', SZ), setlit('𝐵'), R('∩', SZ), setlit('𝐷', True), R(')', SZ))
g4 = HB(R('(', SZ), setlit('𝐴'), R('∩', SZ), setlit('𝐶', True), R('∩', SZ), setlit('𝐷', True), R(')', SZ))
K_atom = HB(g1, R(' ∪ ', SZ, font='c'), g2, R(' ∪ ', SZ, font='c'), g3,
            R(' ∪ ', SZ, font='c'), g4)


def centered(atom, y):
    x = 72.0 + (462.0 - atom.w) / 2
    return atom.emit(x, y)


Y = 75.0
out.append('\\PLBL{42}{38}{3b.i}')
g_lbl = HB(R('𝐺(𝑤,𝑥,𝑦,𝑧) = ', SZ, font='c'), G_formula(SZ))
out += centered(g_lbl, Y)
Y += g_lbl.dp + 16
out.append(f'\\DLINE{{72.0}}{{{fmt(Y)}}}{{534.0}}{{{fmt(Y)}}}{{0.5}}')
Y += 20
h_lbl = HB(R('𝐻(𝐴,𝐵,𝐶,𝐷) = ', SZ, font='c'), H_atom)
out += centered(h_lbl, Y)
Y += h_lbl.dp + 40

out.append(f'\\PLBL{{42}}{{{fmt(Y-24)}}}{{3b.ii}}')
msop_lbl = HB(R('𝑀𝑆𝑂𝑃(𝐺(𝑤,𝑥,𝑦,𝑧)) = ', SZ, font='c'), plus_join(msop_terms(SZ), SZ))
out += centered(msop_lbl, Y)
Y += msop_lbl.dp + 16
out.append(f'\\DLINE{{72.0}}{{{fmt(Y)}}}{{534.0}}{{{fmt(Y)}}}{{0.5}}')
Y += 20
k_lbl = HB(R('𝐾(𝐴,𝐵,𝐶,𝐷) = ', SZ, font='c'), K_atom)
out += centered(k_lbl, Y)

with open('sheets/ws6200.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to sheets/ws6200.tex')
