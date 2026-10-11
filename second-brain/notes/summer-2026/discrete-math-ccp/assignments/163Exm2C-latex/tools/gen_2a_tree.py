#!/usr/bin/env python3
"""2a facing-side tree (page 613): 3-tier distribution tree for
G(w,x,y,z)=(y+z')(w+x+y+z)(w'+x+y'+z) -> SOP(G). Root = generic dashes,
tier1 = alpha's 2 disjuncts (y, z'), tier2 = beta's 4 disjuncts (w,x,y,z),
tier3 (leaves) = gamma's 4 disjuncts (w',x,y',z), each leaf labeled with
the fully-reduced running product (idempotent dupes collapsed, '0' shown
for a tautological w/w' or y/y' or z/z' clash -- dead branches stay
visible per styleguide sec.6.2, never omitted).
"""
import sys
sys.path.insert(0, '.')
from tree import Node, Tree

f1 = ['y', "z'"]
f2 = ['w', 'x', 'y', 'z']
f3 = ["w'", 'x', "y'", 'z']


def varname(lit):
    return lit[0]


def iscomp(lit):
    return lit.endswith("'")


def combine(lits):
    seen = {}
    for l in lits:
        v, c = varname(l), iscomp(l)
        if v in seen and seen[v] != c:
            return None
        seen[v] = c
    out, seenset = [], set()
    for l in lits:
        if l not in seenset:
            out.append(l)
            seenset.add(l)
    return out


top_nodes = []
for d1 in f1:
    lvl1_children = []
    for d2 in f2:
        acc2 = combine([d1, d2])
        lvl2_label = ''.join(acc2) if acc2 else '0'
        leaves = []
        for d3 in f3:
            acc3 = combine(acc2 + [d3]) if acc2 else None
            leaves.append(Node(''.join(acc3) if acc3 else '0', []))
        lvl1_children.append(Node(lvl2_label, leaves))
    top_nodes.append(Node(d1, lvl1_children))

t = Tree(depth=3, top_nodes=top_nodes, sz=6.2, col_w=14.0)
out = t.emit(72.0, 110.0, show_title=True, root_label='_ _ _')

with open('pages/answers613.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers613.tex, tree width={t.w}')
