#!/usr/bin/env python3
"""2b facing-side trees (page 615): one small distribution tree per
SOP(G) term, expanding it to full canonical minterms by the variable(s)
missing from that term (matching the exhibit's "one tree per SOP-term"
convention for building CSOP from SOP). SOP(G)=w'y'z'+w'y+xy+xz'+yz.
"""
import sys
sys.path.insert(0, '.')
from tree import Node, Tree

ALLV = ['w', 'x', 'y', 'z']

TERMS = [
    [('w', True), ('y', True), ('z', True)],   # w'y'z' -- missing x
    [('w', True), ('y', False)],                # w'y -- missing x,z
    [('x', False), ('y', False)],               # xy -- missing w,z
    [('x', False), ('z', True)],                # xz' -- missing w,y
    [('y', False), ('z', False)],               # yz -- missing w,x
]


def term_label(lits):
    return ''.join((n + ("'" if c else '')) for n, c in lits)


def missing_vars(lits):
    present = {n for n, _ in lits}
    return [v for v in ALLV if v not in present]


def order_lits(full_lits):
    # full_lits: dict var->comp ; render in w,x,y,z order
    return ''.join(v + ("'" if full_lits[v] else '') for v in ALLV)


y = 100.0
out = []
for lits in TERMS:
    base = {n: c for n, c in lits}
    miss = missing_vars(lits)
    label = term_label(lits)

    # build a small distribution tree over the missing variable(s)
    def build_level(assigned, remaining):
        if not remaining:
            return None
        v = remaining[0]
        children = []
        for comp in (False, True):
            a2 = dict(assigned)
            a2[v] = comp
            if len(remaining) == 1:
                children.append(Node(order_lits(a2), []))
            else:
                sub = build_level(a2, remaining[1:])
                lbl = order_lits(a2) if False else (v + ("'" if comp else ''))
                children.append(Node(lbl, sub))
        return children

    top_nodes = build_level(base, miss) if miss else [Node(label, [])]
    depth = len(miss) if miss else 1
    t = Tree(depth=max(depth, 1), top_nodes=top_nodes, sz=8.5, col_w=44.0)
    out += t.emit(90.0, y, show_title=(lits == TERMS[0]), root_label=label)
    y += t.dp + 34.0

with open('pages/answers615.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers615.tex, final y={y}')
