#!/usr/bin/env python3
"""Worksheet 6080 (work for problem on page 608, tag '1b.i.0'/'1b.ii.0'):
full consensus-method reduction chain with real Cns(...)=... citations,
then a second worksheet 6081 ('1b.ii.1'/'1b.ii.2') with the MSOP-covers-
CSOP verification trees for x and y (peer-reference style: each PI term
re-expanded to canonical minterms via the missing variable(s), matching
folio 6080/6081 of Math163AdityaRayapudi.pdf).
"""
import sys
sys.path.insert(0, '.')
from atoms import R, HB, Chain, cvar, wrap, fmt, strike, subs
from tree import Node, Tree

SZ = 12.96
CSZ = 10.0


def t(bits, sz=SZ):
    names = ['𝑥', '𝑦', '𝑧']
    return HB(*[cvar(n, comp=(b == 0), sz=sz) for n, b in zip(names, bits)])


def row(*terms):
    parts = [terms[0]]
    for x in terms[1:]:
        parts.append(R(' + ', SZ, font='c'))
        parts.append(x)
    return HB(*parts)


def xy_pair(a, b, sz=SZ):
    return HB(cvar('𝑥', comp=(a == 0), sz=sz), cvar('𝑦', comp=(b == 0), sz=sz))


xyz, xyz1, xy1z, xy1z1, x1yz, x1yz1 = t((1, 1, 1)), t((1, 1, 0)), t((1, 0, 1)), t((1, 0, 0)), t((0, 1, 1)), t((0, 1, 0))
xy, xy1, x1y = xy_pair(1, 1), xy_pair(1, 0), xy_pair(0, 1)
xatom, yatom = R('𝑥', SZ, font='c'), R('𝑦', SZ, font='c')

rows = [
    row(xyz, xyz1, xy1z, xy1z1, x1yz, x1yz1),
    row(xy1z, xy1z1, x1yz, x1yz1, xy),
    row(x1yz, x1yz1, xy, xy1),
    row(xy, xy1, x1y),
    row(xy1, yatom),
    row(yatom, xatom),
]


def cns(a, b, res):
    return HB(R('Cns(', CSZ, font='b'), a, R(',', CSZ, font='c'), b, R(')=', CSZ, font='c'), res)


cite_atoms = [
    None,
    cns(t((1, 1, 1), CSZ), t((1, 1, 0), CSZ), xy_pair(1, 1, CSZ)),
    cns(t((1, 0, 1), CSZ), t((1, 0, 0), CSZ), xy_pair(1, 0, CSZ)),
    cns(t((0, 1, 1), CSZ), t((0, 1, 0), CSZ), xy_pair(0, 1, CSZ)),
    cns(xy_pair(1, 1, CSZ), xy_pair(0, 1, CSZ), R('𝑦', CSZ, font='c')),
    cns(xy_pair(1, 0, CSZ), R('𝑦', CSZ, font='c'), R('𝑥', CSZ, font='c')),
]

out = []
out.append('\\PLBL{42}{38}{1b.i.0}')
out += R('𝐸', SZ, font='c').emit(72.0, 75.0)

chain = Chain(rows[0], [('=', r) for r in rows[1:]], sz=SZ, rowgap=10.0,
              indent=R('=', SZ, font='c').w + 8)
CX = 72.0
CY = 100.0
out += chain.emit(CX, CY)
for cy, ct in zip(chain.ys, cite_atoms):
    if ct:
        out += ct.emit(390.0, CY + cy)

y_after_chain = CY + chain.ys[-1] + rows[-1].dp + 30
out.append(f'\\DLINE{{72.0}}{{{fmt(y_after_chain-14)}}}{{500.0}}{{{fmt(y_after_chain-14)}}}{{0.5}}')
out.append('\\PLBL{42}{' + fmt(y_after_chain - 30) + '}{1b.i.1}')

# not-subset justification (real ⊄ glyph, built as ⊆ struck through --
# neither ⊆ nor ⊄ exist natively in this exam's font, ⊆ was donor-merged
# in from 163Exm1B-latex/fonts/CambriaMath_22.ttf) + a struck-through
# "Cns" (the printed convention for "consensus does not apply here") +
# PI(E) restated -- matches the peer-reference's own symbolic notation,
# no word substitutes.
def notsubset(sz):
    return strike(R('⊆', sz, font='c'), extend=0.6)


def struck_cns():
    return strike(R('Cns', SZ, font='b'), extend=0.8)


just = HB(R('(', SZ), xatom, R(' ', SZ), notsubset(SZ), R(' ', SZ), yatom, R(')   (', SZ, font='c'), yatom,
          R(' ', SZ), notsubset(SZ), R(' ', SZ), xatom, R(')   ', SZ, font='c'), struck_cns(),
          R('(', SZ, font='c'), xatom, R(',', SZ, font='c'), yatom, R(')', SZ, font='c'))
out += just.emit(90.0, y_after_chain)
pi_set = wrap(HB(xatom, R(', ', SZ, font='b'), yatom), l='{', r='}', sz=SZ)
pi_lbl = R('𝑃𝐼(𝐸) = ', SZ, font='c')
out += pi_lbl.emit(150.0, y_after_chain + 26)
out += pi_set.emit(150.0 + pi_lbl.w, y_after_chain + 26)

with open('sheets/ws6080.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to sheets/ws6080.tex')

# ---------------- ws6081: MSOP(E)-covers-E verification table + trees ----------------
out2 = []
out2.append('\\PLBL{42}{38}{1b.ii.0}')
TSZ = 9.0
out2 += R('𝐸', 12.96, font='c').emit(72.0, 60.0)

one = R('1', TSZ, font='b')


def lbl(text):
    return R(text, TSZ, font='b')


def term(bits, sub=None):
    names = ['𝑥', '𝑦', '𝑧']
    a = HB(*[cvar(n, comp=(b == 0), sz=TSZ) for n, b in zip(names, bits)])
    if sub:
        a = HB(a, R('(', TSZ, font='b'), lbl(sub), R(')', TSZ, font='b'))
    return a


# x-branch (row1) and y-branch (row2), 6 columns
col1 = (R('𝑥', TSZ, font='c'), HB(R('+', TSZ, font='c'), R('𝑦', TSZ, font='c')))
col2 = (HB(R('𝑥', TSZ, font='c'), R('(', TSZ, font='c'), one, R(')(', TSZ, font='c'), one, R(')', TSZ, font='c')),
        HB(R('+(', TSZ, font='c'), one, R(')𝑦(', TSZ, font='c'), one, R(')', TSZ, font='c')))
def yz_sum(v):
    return HB(R('(', TSZ, font='c'), cvar(v, sz=TSZ), R('+', TSZ, font='c'), cvar(v, comp=True, sz=TSZ), R(')', TSZ, font='c'))


col3 = (HB(R('𝑥', TSZ, font='c'), yz_sum('𝑦'), yz_sum('𝑧')),
        HB(R('+', TSZ, font='c'), yz_sum('𝑥'), R('𝑦', TSZ, font='c'), yz_sum('𝑧')))
col4 = (HB(term((1, 1, 1), '11'), R('+', TSZ, font='c'), term((1, 1, 0), '21'), R('+', TSZ, font='c'),
           term((1, 0, 1)), R('+', TSZ, font='c'), term((1, 0, 0))),
        HB(R('+', TSZ, font='c'), term((1, 1, 1), '12'), R('+', TSZ, font='c'), term((1, 1, 0), '22'),
           R('+', TSZ, font='c'), term((0, 1, 1)), R('+', TSZ, font='c'), term((0, 1, 0))))
col5 = (HB(R('𝑥𝑦', TSZ, font='c'), R('(11)', TSZ, font='b'), R('+𝑥', TSZ, font='c'), cvar('𝑦', comp=True, sz=TSZ)),
        HB(R('+𝑥𝑦', TSZ, font='c'), R('(12)', TSZ, font='b'), R('+', TSZ, font='c'), cvar('𝑥', comp=True, sz=TSZ), R('𝑦', TSZ, font='c')))
col6 = (R('𝑥', TSZ, font='c'), HB(R('+𝑦', TSZ, font='c')))
cols = [col1, col2, col3, col4, col5, col6]

x_cols = [72.0, 110.0, 155.0, 250.0, 420.0, 500.0]
Y1, Y2 = 90.0, 108.0
for i, (r1, r2) in enumerate(cols):
    if i > 0:
        out2 += R('=', TSZ, font='c').emit(x_cols[i] - 12, Y1)
    out2 += r1.emit(x_cols[i], Y1)
    out2 += r2.emit(x_cols[i], Y2)
    out2.append(f'\\DLINE{{{fmt(x_cols[i]-6)}}}{{{fmt(Y1+3)}}}{{{fmt(x_cols[i]-6)}}}{{{fmt(Y2+1)}}}{{0.5}}')
out2 += R('= 𝑀𝑆𝑂𝑃(𝐸)', 12.0, font='c').emit(x_cols[-1] + col6[0].w + 10, Y1)

out2.append('\\PLBL{42}{140}{1b.ii.1}')
out2.append('\\PLBL{310}{140}{1b.ii.2}')


def leaf3(bits):
    names = ['𝑥', '𝑦', '𝑧']
    return ''.join((n if b else n + "'") for n, b in zip(names, bits))


# tree for x: missing y,z -> 4 leaves
top_x = []
for yb in (1, 0):
    children = []
    for zb in (1, 0):
        children.append(Node(leaf3((1, yb, zb)), []))
    top_x.append(Node('y' if yb else "y'", children))
tx = Tree(depth=2, top_nodes=top_x, sz=10.5, col_w=70.0)
out2 += tx.emit(72.0, 170.0, show_title=True, root_label='x')

# tree for y: missing x,z -> 4 leaves
top_y = []
for xb in (1, 0):
    children = []
    for zb in (1, 0):
        children.append(Node(leaf3((xb, 1, zb)), []))
    top_y.append(Node('x' if xb else "x'", children))
ty = Tree(depth=2, top_nodes=top_y, sz=10.5, col_w=70.0)
out2 += ty.emit(340.0, 170.0, show_title=True, root_label='y')

with open('sheets/ws6081.tex', 'w') as f:
    f.write('\n'.join(out2) + '\n')
print(f'wrote {len(out2)} lines to sheets/ws6081.tex')
