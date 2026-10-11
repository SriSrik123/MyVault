#!/usr/bin/env python3
"""Worksheet 6100 (work for problem on page 610, tag '1c.ii.0'): the
algebra-of-propositions proof that phi(p,q,r) = psi(p,q,r) = p v q, as a
double-underlined equivalence chain -- matches peer-reference style
(Math163AdityaRayapudi.pdf folio 6100): each step is a full restatement,
separated by a double rule, ending phi(p,q,r) = psi(p,q,r).
"""
import sys
sys.path.insert(0, '.')
from atoms import R, HB, fmt

SZ = 11.5
out = []
out.append('\\PLBL{42}{38}{1c.ii.0}')


def dline2(x0, x1, y):
    return [f'\\DLINE{{{fmt(x0)}}}{{{fmt(y)}}}{{{fmt(x1)}}}{{{fmt(y)}}}{{0.5}}',
            f'\\DLINE{{{fmt(x0)}}}{{{fmt(y+2.2)}}}{{{fmt(x1)}}}{{{fmt(y+2.2)}}}{{0.5}}']


def pc(v, name):
    if v == 1:
        return R(name, SZ, font='c')
    return HB(R('(', SZ), R('¬', SZ), R(name, SZ, font='c'), R(')', SZ))


def conj3(p, q, r):
    inner = HB(pc(p, '𝑝'), R('∧', SZ), pc(q, '𝑞'), R('∧', SZ), pc(r, '𝑟'))
    return HB(R('(', SZ), inner, R(')', SZ))


PQR = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
true_rows = [3, 4, 5, 6, 7, 8]


def centered(atom, y):
    x = 72.0 + (462.0 - atom.w) / 2
    return atom.emit(x, y)


Y = 75.0
out += centered(R('𝜑(𝑝,𝑞,𝑟)', SZ, font='c'), Y)
Y += 26
out += dline2(72.0, 534.0, Y)
Y += 16

terms = [conj3(*PQR[r - 1]) for r in true_rows]
row1 = HB(terms[0], R(' ∨ ', SZ, font='c'), terms[1], R(' ∨ ', SZ, font='c'), terms[2])
row1b = HB(R('∨ ', SZ, font='c'), terms[3], R(' ∨ ', SZ, font='c'), terms[4], R(' ∨ ', SZ, font='c'), terms[5])
out += centered(row1, Y)
Y += row1.dp + 20
out += centered(row1b, Y)
Y += row1b.dp + 24
out += dline2(72.0, 534.0, Y)
Y += 16

# group by r: (p^q^(r v ~r)) v (p^~q^(r v~r)) v (~p^q^(r v~r))
r_or = HB(R('(', SZ), R('𝑟', SZ, font='c'), R(' ∨ ', SZ, font='c'), R('¬', SZ), R('𝑟', SZ, font='c'), R(')', SZ))


def grp(p, q):
    inner = HB(pc(p, '𝑝'), R('∧', SZ), pc(q, '𝑞'), R('∧', SZ), r_or)
    return HB(R('(', SZ), inner, R(')', SZ))


row2 = HB(grp(1, 1), R(' ∨ ', SZ, font='c'), grp(1, 0), R(' ∨ ', SZ, font='c'), grp(0, 1))
out += centered(row2, Y)
Y += row2.dp + 24
out += dline2(72.0, 534.0, Y)
Y += 16

# (p^q) v (p^~q) v (~p^q)
row3 = HB(R('(', SZ), R('𝑝', SZ, font='c'), R('∧', SZ), R('𝑞', SZ, font='c'), R(')', SZ),
          R(' ∨ ', SZ, font='c'),
          R('(', SZ), R('𝑝', SZ, font='c'), R('∧', SZ), R('¬', SZ), R('𝑞', SZ, font='c'), R(')', SZ),
          R(' ∨ ', SZ, font='c'),
          R('(', SZ), R('¬', SZ), R('𝑝', SZ, font='c'), R('∧', SZ), R('𝑞', SZ, font='c'), R(')', SZ))
out += centered(row3, Y)
Y += row3.dp + 24
out += dline2(72.0, 534.0, Y)
Y += 16

# p^(q v ~q) v (~p^q)
row4 = HB(R('(', SZ), R('𝑝', SZ, font='c'), R('∧', SZ), R('(', SZ), R('𝑞', SZ, font='c'),
          R(' ∨ ', SZ, font='c'), R('¬', SZ), R('𝑞', SZ, font='c'), R(')', SZ), R(')', SZ),
          R(' ∨ ', SZ, font='c'),
          R('(', SZ), R('¬', SZ), R('𝑝', SZ, font='c'), R('∧', SZ), R('𝑞', SZ, font='c'), R(')', SZ))
out += centered(row4, Y)
Y += row4.dp + 24
out += dline2(72.0, 534.0, Y)
Y += 16

# p v (~p^q)
row5 = HB(R('𝑝', SZ, font='c'), R(' ∨ ', SZ, font='c'),
          R('(', SZ), R('¬', SZ), R('𝑝', SZ, font='c'), R('∧', SZ), R('𝑞', SZ, font='c'), R(')', SZ))
out += centered(row5, Y)
Y += row5.dp + 24
out += dline2(72.0, 534.0, Y)
Y += 16

# (p v ~p) ^ (p v q)
row6 = HB(R('(', SZ), R('𝑝', SZ, font='c'), R(' ∨ ', SZ, font='c'), R('¬', SZ), R('𝑝', SZ, font='c'), R(')', SZ),
          R('∧', SZ),
          R('(', SZ), R('𝑝', SZ, font='c'), R(' ∨ ', SZ, font='c'), R('𝑞', SZ, font='c'), R(')', SZ))
out += centered(row6, Y)
Y += row6.dp + 24
out += dline2(72.0, 534.0, Y)
Y += 16

row7 = HB(R('𝑝', SZ, font='c'), R(' ∨ ', SZ, font='c'), R('𝑞', SZ, font='c'))
out += centered(row7, Y)
Y += row7.dp + 24
out += dline2(72.0, 534.0, Y)
Y += 16

out += centered(R('𝜓(𝑝,𝑞,𝑟)', SZ, font='c'), Y)
Y += 26
out += dline2(72.0, 534.0, Y)
Y += 16

final = HB(R('𝜑(𝑝,𝑞,𝑟) = 𝜓(𝑝,𝑞,𝑟)', SZ, font='c'))
out += centered(final, Y)

with open('sheets/ws6100.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to sheets/ws6100.tex')
