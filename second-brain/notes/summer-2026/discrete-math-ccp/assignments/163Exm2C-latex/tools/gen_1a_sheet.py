#!/usr/bin/env python3
"""Worksheet 6060 (work for problem on page 606, tag '1a'): full raw
6-term expansions of phi(p,q,r), F(A,B,C), E(x,y,z), each preceded by its
compact phi1-v-...-v-phi6-style summary line and separated by double
underlines -- matches the peer-reference layout (Math163AdityaRayapudi.pdf,
folio 6060): compact line, then vertical-bar-braced full expansion, then
a double rule, repeated for each of the three target languages.
"""
import sys
sys.path.insert(0, '.')
from atoms import R, HB, Chain, wrap, fmt, chain_vbar, subs, sup, Prime, cvar

SZ = 12.96
out = []
out.append('\\PLBL{42}{38}{1a}')

PQR = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
true_rows = [3, 4, 5, 6, 7, 8]  # phi3..phi8 true (top-to-bottom exam order)


def dline2(x0, x1, y):
    return [f'\\DLINE{{{fmt(x0)}}}{{{fmt(y)}}}{{{fmt(x1)}}}{{{fmt(y)}}}{{0.5}}',
            f'\\DLINE{{{fmt(x0)}}}{{{fmt(y+2.2)}}}{{{fmt(x1)}}}{{{fmt(y+2.2)}}}{{0.5}}']


Y = 75.0
X = 62.0

# ---- phi(p,q,r) ----
out += R('𝜑(𝑝,𝑞,𝑟)', SZ, font='c').emit(X, Y)
Y += 26

def phi_i(i):
    return subs(R('𝜑', SZ, font='c'), R(str(i), 8.0, font='b'))


phi_syms = [phi_i(i) for i in range(1, 7)]
summary_parts = []
for i, p in enumerate(phi_syms):
    summary_parts.append(p)
    if i != len(phi_syms) - 1:
        summary_parts.append(R(' ∨ ', SZ, font='c'))
summary = HB(*summary_parts)
out += R('=', SZ).emit(X, Y)
out += summary.emit(X + 20, Y)
Y += 30


def pclit(v, name):
    if v == 1:
        return R(name, SZ, font='c')
    return HB(R('(', SZ), R('¬', SZ), R(name, SZ, font='c'), R(')', SZ))


def conj3(p, q, r):
    inner = HB(pclit(p, '𝑝'), R('∧', SZ), pclit(q, '𝑞'), R('∧', SZ), pclit(r, '𝑟'))
    return HB(R('(', SZ), inner, R(')', SZ))


phi_terms = [conj3(*PQR[row - 1]) for row in true_rows]
phi_chain = Chain(phi_terms[0], [('∨', t) for t in phi_terms[1:]], sz=SZ, rowgap=6.0,
                   indent=R('∨', SZ, font='c').w + 8)
out += R('=', SZ).emit(X, Y)
out += phi_chain.emit(X + 24, Y)
out += chain_vbar(phi_chain, X + 24, Y)
Y += phi_chain.ys[-1] + phi_terms[-1].dp + 18
out += dline2(X, 470, Y)
Y += 20

# ---- F(A,B,C) ----
out += R('𝐹(𝐴,𝐵,𝐶)', SZ, font='c').emit(X, Y)
Y += 24


def setlit(v, name):
    if v == 1:
        return R(name, SZ, font='c')
    csup = sup(R(name, SZ, font='c'), R('c', SZ * 0.72, font='b'))
    return HB(R('(', SZ), csup, R(')', SZ))


def inter3(p, q, r):
    inner = HB(setlit(p, '𝐴'), R('∩', SZ), setlit(q, '𝐵'), R('∩', SZ), setlit(r, '𝐶'))
    return HB(R('(', SZ), inner, R(')', SZ))


f_terms = [inter3(*PQR[row - 1]) for row in true_rows]
f_chain = Chain(f_terms[0], [('∪', t) for t in f_terms[1:]], sz=SZ, rowgap=6.0,
                indent=R('∪', SZ, font='c').w + 8)
out += R('=', SZ).emit(X, Y)
out += f_chain.emit(X + 24, Y)
out += chain_vbar(f_chain, X + 24, Y)
Y += f_chain.ys[-1] + f_terms[-1].dp + 18
out += dline2(X, 470, Y)
Y += 20

# ---- E(x,y,z) ----
out += R('𝐸(𝑥,𝑦,𝑧)', SZ, font='c').emit(X, Y)
Y += 24


def balit(v, name):
    return cvar(name, comp=(v == 0), sz=SZ)


def prod3(p, q, r):
    return HB(balit(p, '𝑥'), balit(q, '𝑦'), balit(r, '𝑧'))


e_terms = [prod3(*PQR[row - 1]) for row in true_rows]
e_chain = Chain(e_terms[0], [('+', t) for t in e_terms[1:]], sz=SZ, rowgap=6.0,
                indent=R('+', SZ, font='c').w + 8)
out += R('=', SZ).emit(X, Y)
out += e_chain.emit(X + 24, Y)
out += chain_vbar(e_chain, X + 24, Y)

with open('sheets/ws6060.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to sheets/ws6060.tex')
