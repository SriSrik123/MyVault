#!/usr/bin/env python3
"""1c printed-page answers (page 610): MSOP(E) restated, psi(p,q,r) = PC
version of MSOP(E), and the "prove phi=psi in PC" derivation -- the exact
same consensus/absorption reduction as 1b's E-chain, transliterated into
PC notation (no solved exhibit covers 1c specifically on this exam, same
gap class as every prior exam's "prove that" problems; this construction
mirrors the one demonstrated method available, 1b's own consensus chain,
symbol-for-symbol relettered x->p, y->q, z->r, BA-ops->PC-ops)."""
import sys
sys.path.insert(0, '.')
from atoms import R, HB, Chain, fmt

SZ = 11.04
out = []


def pclit(v, name):
    if v == 1:
        return R(name, SZ, font='c')
    return HB(R('(', SZ), R('¬', SZ), R(name, SZ, font='c'), R(')', SZ))


def conj(bits, names):
    parts = []
    for i, (v, n) in enumerate(zip(bits, names)):
        if i:
            parts.append(R('∧', SZ))
        parts.append(pclit(v, n))
    return HB(R('(', SZ), HB(*parts), R(')', SZ))


P, Q, R_ = '𝑝', '𝑞', '𝑟'

# ---- MSOP(E) restated at (1c)'s own "From (1b) MSOP(E) =" line ----
msop_atom = HB(R('𝑥', 12.96, font='c'), R(' + ', 12.96, font='c'), R('𝑦', 12.96, font='c'))
out += msop_atom.emit(231.65 + R('=', 12.96, font='c').w + 8, 84.50)

# ---- psi(p,q,r) = p v q ----
psi_atom = HB(R(P, 12.96, font='c'), R('∨', 12.96), R(Q, 12.96, font='c'))
out += psi_atom.emit(198.77 + R('=', 12.96, font='c').w + 8, 170.06)

# ---- proof: phi(p,q,r) = ... = psi(p,q,r), consensus/absorption chain ----
c1 = conj((1, 1, 1), (P, Q, R_))
c2 = conj((1, 1, 0), (P, Q, R_))
c3 = conj((1, 0, 1), (P, Q, R_))
c4 = conj((1, 0, 0), (P, Q, R_))
c5 = conj((0, 1, 1), (P, Q, R_))
c6 = conj((0, 1, 0), (P, Q, R_))
pq = HB(R('(', SZ), R(P, SZ, font='c'), R('∧', SZ), R(Q, SZ, font='c'), R(')', SZ))
pnq = HB(R('(', SZ), R(P, SZ, font='c'), R('∧', SZ), R('¬', SZ), R(Q, SZ, font='c'), R(')', SZ))
npq = HB(R('(', SZ), R('¬', SZ), R(P, SZ, font='c'), R('∧', SZ), R(Q, SZ, font='c'), R(')', SZ))
q_atom = R(Q, SZ, font='c')
p_atom = R(P, SZ, font='c')

steps = [
    [c1, c2, c3, c4, c5, c6],
    [c3, c4, c5, c6, pq],
    [c5, c6, pq, pnq],
    [pq, pnq, npq],
    [pnq, q_atom],
    [q_atom, p_atom],
]

MAXPER = 3


def pack(terms, sign_first):
    """Split `terms` into physical lines (<=MAXPER each); returns a list of
    (sign_or_None, row_atom). Only the first physical line carries the
    step's own relation sign; continuations carry None (Chain skips the
    sign glyph but keeps the same indent, so they still align under it)."""
    lines = [terms[i:i + MAXPER] for i in range(0, len(terms), MAXPER)]
    out_rows = []
    for i, ln in enumerate(lines):
        parts = [ln[0]]
        for t in ln[1:]:
            parts.append(R('∨', SZ))
            parts.append(t)
        atom = HB(*parts)
        sign = sign_first if i == 0 else None
        out_rows.append((sign, atom))
    return out_rows


phys_rows = []
phys_rows += pack(steps[0], None)
for st in steps[1:]:
    phys_rows += pack(st, '=')

phi_label = HB(R('𝜑(', SZ, font='c'), R(P, SZ, font='c'), R(',', SZ, font='c'),
               R(Q, SZ, font='c'), R(',', SZ, font='c'), R(R_, SZ, font='c'), R(')', SZ, font='c'))
out += phi_label.emit(144.02, 258.0)

chain_indent = R('=', SZ, font='c').w + 8
first_sign, first_atom = phys_rows[0]
chain = Chain(first_atom, [(s or ' ', a) for s, a in phys_rows[1:]], sz=SZ,
              rowgap=6.0, indent=chain_indent)
out += chain.emit(144.02, 284.0)

psi_label = HB(R('=', SZ, font='c'), R('  ', SZ), R(P, SZ, font='c'), R('∨', SZ),
               R(Q, SZ, font='c'), R('  =  ', SZ, font='c'), R('𝜓(', SZ, font='c'),
               R(P, SZ, font='c'), R(',', SZ, font='c'), R(Q, SZ, font='c'),
               R(',', SZ, font='c'), R(R_, SZ, font='c'), R(')', SZ, font='c'))
last_y = 284.0 + chain.ys[-1] + phys_rows[-1][1].dp + 16
out += psi_label.emit(144.02, last_y)

with open('pages/answers610.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers610.tex')
print('n physical rows:', len(phys_rows))
