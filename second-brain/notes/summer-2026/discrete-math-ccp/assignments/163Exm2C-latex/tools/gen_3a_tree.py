#!/usr/bin/env python3
"""3a facing-side formation tree (page 619) for
psi(p,q,r,s) = (r v ~s) ^ (p v q v r v s) ^ (~p v q v ~r v s)
Operator-parse tree: root=AND splits [factor1, AND(factor2,factor3)];
each OR-factor is a right-associative binary OR chain down to leaves;
negated leaves get a unary NOT node above the bare variable (matches
1C project's own "Basic Formation Trees" convention: root=outermost
connective, recurse into each side, leaves=atoms).
"""
import sys
sys.path.insert(0, '.')
from tree import Node
from atoms import R, HB, fmt as fmt_
from gterms import G_formula

# CORRECTED (2026-08-14, matched against peer-reference folio 6181): this
# page needs a restatement header -- G(w,x,y,z)'s own factored form over a
# rule, then Psi(p,q,r,s)'s PC translation -- BEFORE the formation tree,
# not just the bare tree by itself.
HSZ = 12.96
header_out = []
g_lbl = HB(R('𝐺(𝑤,𝑥,𝑦,𝑧) = ', HSZ, font='c'), G_formula(HSZ))
header_out += g_lbl.emit(108.0, 75.0)
header_out.append(f'\\DLINE{{90.0}}{{95.0}}{{460.0}}{{95.0}}{{0.5}}')
header_out += R('𝜓(𝑝,𝑞,𝑟,𝑠)', HSZ, font='c').emit(108.0, 115.0)


def lit(name, comp=False):
    return Node('¬', [Node(name, [])]) if comp else Node(name, [])


def or_chain(items):
    # items: list of (name, comp) pairs, right-associative OR
    if len(items) == 1:
        return lit(*items[0])
    return Node('∨', [lit(*items[0]), or_chain(items[1:])])


f1 = or_chain([('r', False), ('s', True)])
f2 = or_chain([('p', False), ('q', False), ('r', False), ('s', False)])
f3 = or_chain([('p', True), ('q', False), ('r', True), ('s', False)])

root = Node('∧', [f1, Node('∧', [f2, f3])])


def max_depth(n):
    if not n.children:
        return 1
    return 1 + max(max_depth(c) for c in n.children)


def collect_leaves(n, out):
    if not n.children:
        out.append(n)
    else:
        for c in n.children:
            collect_leaves(c, out)


depth = max_depth(root)
leaves = []
collect_leaves(root, leaves)

from tree import ROW_H, label_atom
from atoms import fmt

col_w = 46.0
sz = 10.0
W = max(col_w * len(leaves), col_w * 2)
Y0 = 195.0


def psi_atom():
    def orx(*items):
        parts = [items[0]]
        for it in items[1:]:
            parts.append(R('∨', HSZ, font='c'))
            parts.append(it)
        return HB(*parts)

    def lit_atom(name, comp):
        return HB(R('(', HSZ), R('¬', HSZ), R(name, HSZ, font='c'), R(')', HSZ)) if comp else R(name, HSZ, font='c')

    f1a = HB(R('(', HSZ), orx(lit_atom('𝑟', False), lit_atom('𝑠', True)), R(')', HSZ))
    f2a = HB(R('(', HSZ), orx(lit_atom('𝑝', False), lit_atom('𝑞', False), lit_atom('𝑟', False), lit_atom('𝑠', False)), R(')', HSZ))
    f3a = HB(R('(', HSZ), orx(lit_atom('𝑝', True), lit_atom('𝑞', False), lit_atom('𝑟', True), lit_atom('𝑠', False)), R(')', HSZ))
    return HB(R('= ', HSZ, font='c'), f1a, R(' ∧ ', HSZ, font='c'), f2a, R(' ∧ ', HSZ, font='c'), f3a)


header_out += psi_atom().emit(108.0, 140.0)

out = list(header_out)
title = 'Tree'
from atoms import R
tw = R(title, sz + 1, font='b').w
tx = 72.0 + W / 2 - tw / 2
out += R(title, sz + 1, font='b').emit(tx, Y0)
out.append(f'\\DLINE{{{fmt(tx)}}}{{{fmt(Y0 + 3)}}}{{{fmt(tx + tw)}}}{{{fmt(Y0 + 3)}}}{{0.5}}')
out.append(f'\\DLINE{{{fmt(tx)}}}{{{fmt(Y0 + 5)}}}{{{fmt(tx + tw)}}}{{{fmt(Y0 + 5)}}}{{0.5}}')

root_y = Y0 + 28.0
leaf_positions = {id(lf): 72.0 + col_w * (i + 0.5) for i, lf in enumerate(leaves)}


def layout(n, level):
    ny = root_y + ROW_H * level
    if not n.children:
        cx = leaf_positions[id(n)]
    else:
        child_xs = [layout(c, level + 1) for c in n.children]
        cx = sum(child_xs) / len(child_xs)
    latom = label_atom(n.label, sz)
    lw = latom.w
    out.extend(latom.emit(cx - lw / 2, ny))
    n._cx, n._cy = cx, ny
    return cx


root_cx = layout(root, 0)


def edges(n):
    for c in n.children:
        out.append(f'\\DLINE{{{fmt(n._cx)}}}{{{fmt(n._cy + 3)}}}'
                   f'{{{fmt(c._cx)}}}{{{fmt(c._cy - 9)}}}{{0.5}}')
        edges(c)


edges(root)

out.append('\\PLBL{42}{38}{3a.iii.0}')

with open('sheets/ws6181.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to sheets/ws6181.tex, depth={depth}, leaves={len(leaves)}')
