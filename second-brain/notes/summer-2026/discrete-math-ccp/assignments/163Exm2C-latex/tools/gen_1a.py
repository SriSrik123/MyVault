#!/usr/bin/env python3
"""1a printed-page answers (page 606): T1..T8 fills, phi1..phi8 indicator
grid, and the three canonical-sum formulas phi(p,q,r)/F(A,B,C)/E(x,y,z).

T-number from Sri's fixed J-number 00499317: keep 0-digits, replace every
nonzero digit with 1 -> T = 0,0,1,1,1,1,1,1 (T1=T2=0, T3..T8=1).

phi_k numbering follows SOL2C-2020/2024's own demonstrated convention
(confirmed by direct read of the solved worksheet, folio 6060): dynamic,
assigned only to the TRUE rows, bottom-to-top (phi1 = bottommost true row
p=q=r=1, ... up through the topmost true row) -- NOT the notes' abstract
"phi_l = fixed row l" table. False rows (T1,T2) get no phi label at all.
"""
import sys
sys.path.insert(0, '.')
from atoms import R, HB, Chain, cvar, sup, fmt

SZ = 12.96

# ---------------------------------------------------------------- setup --
J = [0, 0, 4, 9, 9, 3, 1, 7]
T = [0 if d == 0 else 1 for d in J]
PQR = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
       (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

true_rows = [i for i in range(8, 0, -1) if T[i - 1] == 1]  # 1-indexed rows, bottom-up
phi_of_row = {row: k + 1 for k, row in enumerate(true_rows)}

out = []

# ---- T1..T8 value fills ----
T_Y = [180.62, 197.42, 228.62, 245.42, 276.53, 293.45, 324.53, 341.45]
T_EQ_X = [168.98, 169.22, 169.22, 168.86, 169.22, 169.22, 169.22, 169.22]
for i in range(8):
    eq_end = T_EQ_X[i] + R('=', 14.04, font='c').w
    a = R(str(T[i]), 14.04, font='c')
    out += a.emit(eq_end + 6, T_Y[i])

# ---- phi1..phi8 indicator grid ----
PHI_COL_X = [222.29, 263.69, 310.25, 356.47, 400.03, 441.43, 480.34, 519.46]
for row0 in range(8):
    y = T_Y[row0]
    row_n = row0 + 1
    active_phi = phi_of_row.get(row_n)
    for col0 in range(8):
        val = 1 if (active_phi is not None and col0 + 1 == active_phi) else 0
        a = R(str(val), 11.04, font='b')
        cx = PHI_COL_X[col0]
        out += a.emit(cx - a.w / 2 + 6, y - 3)


# ---------------------------------------------------------- phi(p,q,r) ---
def pclit(v, name):
    if v == 1:
        return R(name, SZ, font='c')
    return HB(R('(', SZ), R('¬', SZ), R(name, SZ, font='c'), R(')', SZ))


def conj3(p, q, r):
    inner = HB(pclit(p, '𝑝'), R('∧', SZ), pclit(q, '𝑞'), R('∧', SZ), pclit(r, '𝑟'))
    return HB(R('(', SZ), inner, R(')', SZ))


# CORRECTED (2026-08-14, matched against peer-reference submission
# Math163AdityaRayapudi.pdf's own page 606): the printed page shows the
# FULL raw disjunction for phi(p,q,r), same treatment as F(A,B,C) and
# E(x,y,z) below it -- not a compact phi1-v-...-v-phi6 summary. Wrapped
# 3 terms/line (2 lines) at the same reduced size F(A,B,C) already uses,
# to fit the ~70pt gap before the printed "1(ii)" label.
phi_terms = [conj3(*PQR[row - 1]) for row in true_rows]
phi_lines = [phi_terms[i:i + 3] for i in range(0, len(phi_terms), 3)]


def phi_row_atom(row):
    atoms = [row[0]]
    for t in row[1:]:
        atoms.append(R(' ∨ ', SZ, font='c'))
        atoms.append(t)
    return HB(*atoms)


phi_rows = [phi_row_atom(r) for r in phi_lines]
eq_x = 108.02 + R('=', SZ, font='c').w + 8
phi_indent = R('∨', SZ).w + 8
phi_chain = Chain(phi_rows[0], [('∨', r) for r in phi_rows[1:]], sz=SZ, rowgap=2.0,
                   indent=phi_indent)
out += phi_chain.emit(eq_x, 458.95)


# --------------------------------------------------------- F(A,B,C) -----
def setlit(v, name):
    if v == 1:
        return R(name, SZ, font='c')
    csup = sup(R(name, SZ, font='c'), R('c', SZ * 0.72, font='b'))
    return HB(R('(', SZ), csup, R(')', SZ))


def fconj3(p, q, r):
    inner = HB(setlit(p, '𝐴'), R('∩', SZ), setlit(q, '𝐵'), R('∩', SZ), setlit(r, '𝐶'))
    return HB(R('(', SZ), inner, R(')', SZ))


F_terms = [fconj3(*PQR[row - 1]) for row in true_rows]

# F's own "=" (579.31) to the next label "1(iii)" (628.42) is only ~49pt --
# tighter than it looks (628.42 is the NEXT problem's label, not more room
# for F) -- needs 3 terms/line (2 lines) to fit, not 2/line.
f_lines = [F_terms[i:i + 3] for i in range(0, len(F_terms), 3)]


def row_atom(row):
    atoms = [row[0]]
    for t in row[1:]:
        atoms.append(R('∪', SZ))
        atoms.append(t)
    return HB(*atoms)


f_rows = [row_atom(r) for r in f_lines]
# Chain's default x_expr is sized off rel='=' -- '∪' (union) is wider,
# so an un-indented Chain here lets the sign glyph bleed into the content
# start (confirmed by render: looked like a mangled first paren). Force
# indent to the actual union-glyph width + gap.
f_indent = R('∪', SZ).w + 8
F_chain = Chain(f_rows[0], [('∪', r) for r in f_rows[1:]], sz=SZ, rowgap=2.0,
                 indent=f_indent)
out += F_chain.emit(eq_x, 579.31)


# --------------------------------------------------------- E(x,y,z) -----
def baterm(p, q, r):
    return HB(cvar('𝑥', comp=(p == 0), sz=SZ), cvar('𝑦', comp=(q == 0), sz=SZ),
              cvar('𝑧', comp=(r == 0), sz=SZ))


E_terms = [baterm(*PQR[row - 1]) for row in true_rows]
parts = [E_terms[0]]
for t in E_terms[1:]:
    parts.append(R(' + ', SZ, font='c'))
    parts.append(t)
E_row_atom = HB(*parts)
eq_x_e = 108.02 + R('=', 12, font='c').w + 8
out += E_row_atom.emit(eq_x_e, 685.54)

with open('pages/answers606.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers606.tex')
print('phi_of_row:', phi_of_row)
print('E width:', E_row_atom.w)
