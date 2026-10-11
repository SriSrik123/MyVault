#!/usr/bin/env python3
"""Worksheet 6140/6141 (work for problem on page 614, tags '2b.0'..'2b.5'):
2b.0 is the full per-term algebraic expansion (matching peer-reference
folio 6140 exactly): for each SOP(G) term, four aligned columns -- the
bare term, the term with "(1)" inserted at each missing variable's own
natural w/x/y/z position, the term with "(var+var')" inserted at the same
positions, and the fully distributed leaf terms -- followed by the
deduplicated CSOP(G). Worksheet 6141 then carries the per-term expansion
trees (2b.1..2b.5), same as before.
"""
import sys
sys.path.insert(0, '.')
from tree import Node, Tree, label_atom
from atoms import R, HB, Chain, fmt

ALLV = ['w', 'x', 'y', 'z']
TERMS = [
    [('x', False), ('y', False)],                # xy
    [('w', True), ('y', False)],                  # w'y
    [('y', False), ('z', False)],                 # yz
    [('w', False), ('y', True), ('z', True)],     # wy'z'
    [('x', False), ('z', True)],                  # xz'
]


def term_label(lits):
    return ''.join((n + ("'" if c else '')) for n, c in lits)


def missing_vars(lits):
    present = {n for n, _ in lits}
    return [v for v in ALLV if v not in present]


def order_lits(full_lits):
    return ''.join(v + ("'" if full_lits[v] else '') for v in ALLV)


SZ = 9.5
out = []
out.append('\\PLBL{42}{38}{2b.0}')
out += R('𝑆𝑂𝑃(𝐺)', 12.96, font='c').emit(72.0, 60.0)

all_csop = set()
col_data = []  # per term: (col1, col2, col3, col4_leaves)
for lits in TERMS:
    present = {v: c for v, c in lits}
    miss = missing_vars(lits)
    col1 = term_label(lits)
    col2_parts, col3_parts = [], []
    for v in ALLV:
        if v in present:
            lit = v + ("'" if present[v] else '')
            col2_parts.append(lit)
            col3_parts.append(lit)
        elif v in miss:
            col2_parts.append('(1)')
            col3_parts.append(f"({v}+{v}')")
    col2 = ''.join(col2_parts)
    col3 = ''.join(col3_parts)
    import itertools
    leaves = []
    for combo in itertools.product([False, True], repeat=len(miss)):
        d = dict(present)
        for v, c in zip(miss, combo):
            d[v] = c
        leaf = order_lits(d)
        leaves.append(leaf)
        all_csop.add(leaf)
    col_data.append((col1, col2, col3, leaves))

X = [72.0, 150.0, 230.0, 350.0]
Y0 = 90.0
ROWH = 20.0
for i, (c1, c2, c3, leaves) in enumerate(col_data):
    y = Y0 + i * ROWH
    lead = '= ' if i == 0 else '+ '
    out += R(lead, SZ, font='c').emit(X[0] - 16, y)
    out += label_atom(c1, SZ).emit(X[0], y)
    out += R('=', SZ, font='c').emit(X[1] - 12, y)
    out += label_atom(c2, SZ).emit(X[1], y)
    out += R('=', SZ, font='c').emit(X[2] - 12, y)
    out += label_atom(c3, SZ).emit(X[2], y)
    out += R('=', SZ, font='c').emit(X[3] - 12, y)
    parts4 = []
    for j, lf in enumerate(leaves):
        parts4.append(label_atom(lf, SZ))
        if j != len(leaves) - 1:
            parts4.append(R('+', SZ, font='c'))
    out += HB(*parts4).emit(X[3], y)

Y = Y0 + len(col_data) * ROWH + 24.0
out.append(f'\\DLINE{{72.0}}{{{fmt(Y-14)}}}{{540.0}}{{{fmt(Y-14)}}}{{0.5}}')
out += R('𝐶𝑆𝑂𝑃(𝐺)', 12.96, font='c').emit(72.0, Y)
Y += 24
csop_sorted = sorted(all_csop)
PER_ROW = 5
csop_rows = [csop_sorted[i:i + PER_ROW] for i in range(0, len(csop_sorted), PER_ROW)]


def row_atom(terms, lead):
    parts = [R(lead, 12.96, font='c')]
    for i, t2 in enumerate(terms):
        parts.append(label_atom(t2, 12.96))
        if i != len(terms) - 1:
            parts.append(R(' + ', 12.96, font='c'))
    return HB(*parts)


first = row_atom(csop_rows[0], '= ')
rest = [('+', row_atom(r, '')) for r in csop_rows[1:]]
csop_chain = Chain(first, rest, sz=12.96, rowgap=8.0, indent=30.0)
out += csop_chain.emit(72.0, Y)

with open('sheets/ws6140.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to sheets/ws6140.tex; csop terms={len(all_csop)}')

# ---------------- ws6141: per-term expansion trees ----------------
out2 = []
positions = [(72.0, 90.0), (330.0, 90.0), (72.0, 240.0), (330.0, 240.0), (72.0, 390.0)]
tags = ['2b.1', '2b.2', '2b.3', '2b.4', '2b.5']
for lits, (px, py), tag in zip(TERMS, positions, tags):
    base = {n: c for n, c in lits}
    miss = missing_vars(lits)
    label = term_label(lits)

    def build_level(assigned, remaining):
        children = []
        v = remaining[0]
        for comp in (False, True):
            a2 = dict(assigned)
            a2[v] = comp
            if len(remaining) == 1:
                children.append(Node(order_lits(a2), []))
            else:
                children.append(Node(v + ("'" if comp else ''), build_level(a2, remaining[1:])))
        return children

    top_nodes = build_level(base, miss) if miss else [Node(label, [])]
    depth = max(len(miss), 1)
    t = Tree(depth=depth, top_nodes=top_nodes, sz=9.0, col_w=48.0)
    out2.append(f'\\PLBL{{{fmt(px-30)}}}{{{fmt(py-24)}}}{{{tag}}}')
    out2 += t.emit(px, py, show_title=True, root_label=label)

with open('sheets/ws6141.tex', 'w') as f:
    f.write('\n'.join(out2) + '\n')
print(f'wrote {len(out2)} lines to sheets/ws6141.tex')
