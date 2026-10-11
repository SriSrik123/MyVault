#!/usr/bin/env python3
"""Worksheet 6120/6121 (work for problem on page 612, tags '2a.0'..'2a.3'):
the SOP(G) distribution tree, the raw 32-term distribution (all leaves,
including the dead/zero ones, on one dense line -- matches the printed
exam's own convention for showing every combinatorial term before
dropping zeros), the nonzero-only listing with absorbed terms underlined,
the final reduced SOP(G) with subset citations, then (6121) the exhaustive
pairwise not-subset check across all 5 final terms proving none of them
is redundant, and the final restatement -- matches peer-reference
structure (Math163AdityaRayapudi.pdf folios 6120/6121... this exam's own
'2a.2' section).
"""
import sys
sys.path.insert(0, '.')
from tree import Node, Tree, label_atom
from atoms import R, HB, strike, fmt

f1 = ['y', "z'"]
f2 = ['w', 'x', 'y', 'z']
f3 = ["w'", 'x', "y'", 'z']
ORDER = ['w', 'x', 'y', 'z']


def varname(lit):
    return lit[0]


def iscomp(lit):
    return lit.endswith("'")


def canon(d):
    return ''.join(v + ("'" if d[v] else '') for v in ORDER if v in d)


def combine_dict(d, lit):
    v, c = varname(lit), iscomp(lit)
    if v in d and d[v] != c:
        return None
    d2 = dict(d)
    d2[v] = c
    return d2


top_nodes = []
raw_with_zero = []
nonzero_terms = []
for d1 in f1:
    lvl1_children = []
    d1dict = {varname(d1): iscomp(d1)}
    for d2 in f2:
        acc2 = combine_dict(d1dict, d2)
        lvl2_label = canon(acc2) if acc2 else '0'
        leaves = []
        for d3 in f3:
            acc3 = combine_dict(acc2, d3) if acc2 else None
            term = canon(acc3) if acc3 else '0'
            leaves.append(Node(term, []))
            raw_with_zero.append(term)
            if acc3:
                nonzero_terms.append(term)
        lvl1_children.append(Node(lvl2_label, leaves))
    top_nodes.append(Node(d1, lvl1_children))

seen = set()
deduped = []
for t2 in nonzero_terms:
    if t2 not in seen:
        deduped.append(t2)
        seen.add(t2)


def literals_of(term):
    o, i = [], 0
    while i < len(term):
        if i + 1 < len(term) and term[i + 1] == "'":
            o.append(term[i:i + 2])
            i += 2
        else:
            o.append(term[i])
            i += 1
    return set(o)


lit_sets = {t: literals_of(t) for t in deduped}
final_terms = [t for t in deduped if not any(t != t2 and lit_sets[t2] < lit_sets[t] for t2 in deduped)]
absorbed_by = {t: t not in final_terms for t in deduped}

out = []
out.append('\\PLBL{42}{38}{2a.0}')
t = Tree(depth=3, top_nodes=top_nodes, sz=6.2, col_w=14.0)
out += t.emit(72.0, 90.0, show_title=True, root_label='_ _ _')

Y = 250.0
out.append(f'\\DLINE{{72.0}}{{{fmt(Y-16)}}}{{540.0}}{{{fmt(Y-16)}}}{{0.5}}')
out.append('\\PLBL{42}{' + fmt(Y - 32) + '}{2a.1}')
out += R('𝐺(𝑤,𝑥,𝑦,𝑧)', 12.96, font='c').emit(108.0, Y)
Y += 22

# raw 32-term distribution, tiny font, all zeros shown
RSZ = 5.6
parts = [R('=  ', RSZ, font='c')]
for i, term in enumerate(raw_with_zero):
    parts.append(label_atom(term, RSZ))
    if i != len(raw_with_zero) - 1:
        parts.append(R('+', RSZ, font='c'))
row_raw = HB(*parts)
out += row_raw.emit(108.0, Y)
Y += row_raw.dp + 16

# nonzero-only, absorbed terms underlined
USZ = 9.5
parts = [R('=  ', USZ, font='c')]
x = 108.0 + parts[0].w
underline_segs = []
for i, term in enumerate(deduped):
    a = label_atom(term, USZ)
    parts.append(a)
    if i != len(deduped) - 1:
        parts.append(R(' + ', USZ, font='c'))
row_nz = HB(*parts)
out += row_nz.emit(108.0, Y)
# underline the absorbed ones individually (re-walk x positions)
cx = 108.0 + R('=  ', USZ, font='c').w
for i, term in enumerate(deduped):
    a = label_atom(term, USZ)
    if absorbed_by[term]:
        out.append(f'\\DLINE{{{fmt(cx)}}}{{{fmt(Y + row_nz.dp - 1)}}}{{{fmt(cx + a.w)}}}{{{fmt(Y + row_nz.dp - 1)}}}{{0.4}}')
    cx += a.w
    if i != len(deduped) - 1:
        cx += R(' + ', USZ, font='c').w
Y += row_nz.dp + 22

# final SOP(G), with subset-justification citations to the right
FSZ = 12.96
parts = [R('=  ', FSZ, font='c')]
for i, term in enumerate(final_terms):
    parts.append(label_atom(term, FSZ))
    if i != len(final_terms) - 1:
        parts.append(R(' + ', FSZ, font='c'))
row_final = HB(*parts)
out += row_final.emit(108.0, Y)

cite_lines = []
for f in final_terms:
    absorbed = [t for t in deduped if t != f and lit_sets[f] < lit_sets[t]]
    for a in absorbed:
        cite_lines.append(f'{f}⊆{a}')
CSZ = 8.5
cx0 = 380.0


def cite_atom(pair_str):
    lhs, rhs = pair_str.split('⊆')
    return HB(label_atom(lhs, CSZ), R(' ⊆ ', CSZ, font='c'), label_atom(rhs, CSZ))


CHUNK = 4
cy = Y - 6
for i in range(0, len(cite_lines), CHUNK):
    chunk = cite_lines[i:i + CHUNK]
    parts_c = [R('(', CSZ, font='c')]
    for j, p in enumerate(chunk):
        parts_c.append(cite_atom(p))
        if j != len(chunk) - 1:
            parts_c.append(R(',  ', CSZ, font='c'))
    if i + CHUNK >= len(cite_lines):
        parts_c.append(R(')', CSZ, font='c'))
    row_c = HB(*parts_c)
    out += row_c.emit(cx0, cy)
    cy += 16

with open('sheets/ws6120.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to sheets/ws6120.tex; final_terms={final_terms}')

# ---------------- ws6121: pairwise not-subset check + final restate ----------------
out2 = []
out2.append('\\PLBL{42}{38}{2a.2}')


def notsubset(sz):
    return strike(R('⊆', sz, font='c'), extend=0.5)


import itertools
pairs = list(itertools.combinations(final_terms, 2))
PSZ = 10.5
Y2 = 90.0
COLS = [72.0, 250.0, 420.0]
for i, (a, b) in enumerate(pairs):
    col = COLS[i % 3]
    row_y = Y2 + (i // 3) * 30.0
    at = HB(label_atom(a, PSZ), R(' ', PSZ), notsubset(PSZ), R(' ', PSZ), label_atom(b, PSZ),
            R('   ', PSZ), label_atom(b, PSZ), R(' ', PSZ), notsubset(PSZ), R(' ', PSZ), label_atom(a, PSZ))
    out2 += at.emit(col, row_y)

Y2 += ((len(pairs) + 2) // 3) * 30.0 + 30.0
out2.append(f'\\DLINE{{72.0}}{{{fmt(Y2-16)}}}{{540.0}}{{{fmt(Y2-16)}}}{{0.5}}')
out2.append('\\PLBL{42}{' + fmt(Y2 - 32) + '}{2a.3}')
out2 += R('𝐺(𝑤,𝑥,𝑦,𝑧)', 12.96, font='c').emit(108.0, Y2)
Y2 += 26
sop_row2 = HB(R('= ', 12.96, font='c'), *sum(([label_atom(t2, 12.96)] if i == 0 else
              [R(' + ', 12.96, font='c'), label_atom(t2, 12.96)] for i, t2 in enumerate(final_terms)), []))
out2 += sop_row2.emit(108.0, Y2)
Y2 += sop_row2.dp + 22
out2 += R('= 𝑆𝑂𝑃(𝐺)', 12.96, font='c').emit(108.0, Y2)

with open('sheets/ws6121.tex', 'w') as f:
    f.write('\n'.join(out2) + '\n')
print(f'wrote {len(out2)} lines to sheets/ws6121.tex; pairs={len(pairs)}')
