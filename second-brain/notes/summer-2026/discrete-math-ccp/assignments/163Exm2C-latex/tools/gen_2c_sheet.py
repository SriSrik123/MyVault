#!/usr/bin/env python3
"""Worksheet 6160 (work for problem on page 616, tag '2c.i.0'): full
consensus-method reduction of CSOP(G)'s 10 canonical terms down to
PI(G)={w'y, wy'z', xy, xz', yz}, listed level-by-level with Cns(...)=...
citations (independently verified via Quine-McCluskey). Worksheet 6161
('2c.ii.0'..'2c.ii.4') then verifies MSOP(G) covers CSOP(G) via one small
expansion tree per MSOP term -- matches peer-reference structure (folios
6160/6161 of Math163AdityaRayapudi.pdf).
"""
import sys
sys.path.insert(0, '.')
from tree import Node, Tree, label_atom
from atoms import R, HB, wrap, strike, fmt
from gterms import sop_terms, plus_join
import itertools


def term_str(t, names=['w', 'x', 'y', 'z']):
    parts = []
    for v, n in zip(t, names):
        if v == '-':
            continue
        parts.append(n if v == 1 else n + "'")
    return ''.join(parts) if parts else '1'


def combine(a, b):
    diff = [i for i in range(4) if a[i] != b[i]]
    if len(diff) == 1:
        i = diff[0]
        new = list(a)
        new[i] = '-'
        return tuple(new)
    return None


mG = [(0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0), (0, 1, 1, 0), (0, 1, 1, 1),
      (1, 0, 0, 0), (1, 0, 1, 1), (1, 1, 0, 0), (1, 1, 1, 0), (1, 1, 1, 1)]
groups = {}
for m in mG:
    groups.setdefault(sum(m), set()).add(m)
current = {k: set(v) for k, v in groups.items()}
all_events = []
prime_terms = []
while True:
    next_groups = {}
    used = set()
    keys = sorted(current.keys())
    level_events = []
    for i in range(len(keys) - 1):
        for a in current[keys[i]]:
            for b in current[keys[i + 1]]:
                c = combine(a, b)
                if c:
                    level_events.append((term_str(a), term_str(b), term_str(c)))
                    ones = sum(1 for v in c if v == 1)
                    next_groups.setdefault(ones, set()).add(c)
                    used.add(a)
                    used.add(b)
    for v in current.values():
        for t in v:
            if t not in used:
                prime_terms.append(term_str(t))
    all_events.append(level_events)
    if not next_groups:
        break
    current = next_groups

out = []
out.append('\\PLBL{42}{38}{2c.i.0}')

# CORRECTED (2026-08-14, matched against peer-reference folio 6160): a
# restatement header belongs here first -- SOP(G) (already known from 2a)
# over a rule, then PI(G) asserted as the same term set (for this G, every
# SOP(G) term already happens to be irreducible -- confirmed by the
# consensus derivation below, which is the PROOF of this claim, not an
# independent assumption).
sop_label = R('𝑆𝑂𝑃(𝐺) = ', 12.96, font='c')
out += sop_label.emit(72.0, 60.0)
out += plus_join(sop_terms(12.96), 12.96).emit(72.0 + sop_label.w, 60.0)
out.append(f'\\DLINE{{72.0}}{{80.0}}{{460.0}}{{80.0}}{{0.5}}')
pi_hdr_label = R('𝑃𝐼(𝐺) = ', 12.96, font='c')
out += pi_hdr_label.emit(72.0, 100.0)
pi_hdr_terms = ["w'y", "wy'z'", "xy", "xz'", "yz"]
pi_hdr_set = wrap(HB(*sum(([label_atom(t, 12.96), R(', ', 12.96, font='b')] for t in pi_hdr_terms), [])[:-1]), l='{', r='}', sz=12.96)
out += pi_hdr_set.emit(72.0 + pi_hdr_label.w, 100.0)

out.append(f'\\DLINE{{72.0}}{{130.0}}{{540.0}}{{130.0}}{{0.5}}')
out.append('\\PLBL{42}{140}{2c.i.1}')
out += R('𝐶𝑆𝑂𝑃(𝐺)', 12.96, font='c').emit(72.0, 175.0)

SZ = 9.5
Y = 209.0
COLS = [72.0, 320.0]
for lvl_i, events in enumerate(all_events):
    for i, (a, b, c) in enumerate(events):
        col = COLS[i % 2]
        row_y = Y + (i // 2) * 16.0
        cite = HB(R('Cns(', SZ, font='b'), label_atom(a, SZ), R(',', SZ, font='c'),
                  label_atom(b, SZ), R(')=', SZ, font='c'), label_atom(c, SZ))
        out += cite.emit(col, row_y)
    Y += ((len(events) + 1) // 2) * 16.0 + 14.0

out.append(f'\\DLINE{{72.0}}{{{fmt(Y)}}}{{540.0}}{{{fmt(Y)}}}{{0.5}}')
Y += 20
pi_terms = sorted(set(prime_terms))
pi_label = R('𝑃𝐼(𝐺) = ', 12.96, font='c')
out += pi_label.emit(72.0, Y)
set_parts = []
for i, t in enumerate(pi_terms):
    set_parts.append(label_atom(t, 12.96))
    if i != len(pi_terms) - 1:
        set_parts.append(R(', ', 12.96, font='b'))
pi_set = wrap(HB(*set_parts), l='{', r='}', sz=12.96)
out += pi_set.emit(72.0 + pi_label.w, Y)

with open('sheets/ws6160.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to sheets/ws6160.tex; PI(G)={pi_terms}')

# ---------------- ws6161: pairwise not-subset check + Cns closure across PI(G) ----------------
# CORRECTED (2026-08-14, matched against peer-reference folio 6161): a
# third column belongs on every row -- attempt Cns(a,b) itself (not just
# the not-subset check). If a and b don't differ in exactly one variable
# (with every other shared variable agreeing), consensus isn't defined at
# all, shown as a struck-through "Cns(a,b)". If it IS defined, the
# resulting term must already be covered by (subset-or-equal-to, in the
# "more literals = more specific = smaller set" sense) some existing
# PI(G) term -- otherwise PI(G) would be missing a term -- cited as
# "Cns(a,b)<=covering_term". This is the actual completeness proof for
# PI(G); the not-subset columns alone only show non-redundancy, not that
# consensus closure was checked.
out1b = []
out1b.append('\\PLBL{42}{38}{2c.i.2}')


def notsubset(sz):
    return strike(R('⊆', sz, font='c'), extend=0.5)


def parse_term(term):
    d = {}
    i = 0
    while i < len(term):
        v = term[i]
        if i + 1 < len(term) and term[i + 1] == "'":
            d[v] = True
            i += 2
        else:
            d[v] = False
            i += 1
    return d


def term_to_str(d):
    return ''.join(v + ("'" if d[v] else '') for v in ['w', 'x', 'y', 'z'] if v in d)


def literal_set(d):
    return set(v + ("'" if c else '') for v, c in d.items())


def try_consensus(a, b):
    da, db = parse_term(a), parse_term(b)
    shared = set(da) & set(db)
    diffs = [v for v in shared if da[v] != db[v]]
    if len(diffs) != 1:
        return None
    rv = diffs[0]
    result = {}
    for v in da:
        if v != rv:
            result[v] = da[v]
    for v in db:
        if v != rv:
            result[v] = db[v]
    return result


pi_dicts = {t: parse_term(t) for t in pi_terms}
pi_pairs = list(itertools.combinations(pi_terms, 2))
PSZ = 10.5
CSZ2 = 9.0
Y1b = 90.0
COLS = [72.0, 250.0, 460.0]
for i, (a, b) in enumerate(pi_pairs):
    row_y = Y1b + i * 20.0
    at = HB(label_atom(a, PSZ), R(' ', PSZ), notsubset(PSZ), R(' ', PSZ), label_atom(b, PSZ))
    out1b += at.emit(COLS[0], row_y)
    bt = HB(label_atom(b, PSZ), R(' ', PSZ), notsubset(PSZ), R(' ', PSZ), label_atom(a, PSZ))
    out1b += bt.emit(COLS[1], row_y)

    cterm = try_consensus(a, b)
    if cterm is None:
        cite = strike(HB(R('Cns(', CSZ2, font='b'), label_atom(a, CSZ2), R(',', CSZ2, font='c'),
                          label_atom(b, CSZ2), R(')', CSZ2, font='c')), extend=0.8)
    else:
        clits = literal_set(cterm)
        covering = [t for t in pi_terms if literal_set(pi_dicts[t]) <= clits]
        cov = covering[0] if covering else term_to_str(cterm)
        cite = HB(R('Cns(', CSZ2, font='b'), label_atom(a, CSZ2), R(',', CSZ2, font='c'),
                  label_atom(b, CSZ2), R(') ⊆ ', CSZ2, font='c'), label_atom(cov, CSZ2))
    out1b += cite.emit(COLS[2], row_y)

Y1b += len(pi_pairs) * 20.0 + 30.0

out1b.append(f'\\DLINE{{72.0}}{{{fmt(Y1b-16)}}}{{540.0}}{{{fmt(Y1b-16)}}}{{0.5}}')
out1b.append('\\PLBL{42}{' + fmt(Y1b - 32) + '}{2c.i.3}')
pi_label2 = R('𝑃𝐼(𝐺) = ', 12.96, font='c')
out1b += pi_label2.emit(72.0, Y1b)
set_parts2 = []
for i, t in enumerate(pi_terms):
    set_parts2.append(label_atom(t, 12.96))
    if i != len(pi_terms) - 1:
        set_parts2.append(R(', ', 12.96, font='b'))
pi_set2 = wrap(HB(*set_parts2), l='{', r='}', sz=12.96)
out1b += pi_set2.emit(72.0 + pi_label2.w, Y1b)

with open('sheets/ws6161.tex', 'w') as f:
    f.write('\n'.join(out1b) + '\n')
print(f'wrote {len(out1b)} lines to sheets/ws6161.tex; pairs={len(pi_pairs)}')

# ---------------- ws6162: MSOP-covers-CSOP verification trees ----------------
MSOP_TERMS = [
    [('w', True), ('y', False)],                # w'y -- missing x,z
    [('w', False), ('y', True), ('z', True)],   # wy'z' -- missing x
    [('x', False), ('z', True)],                # xz' -- missing w,y
    [('y', False), ('z', False)],                # yz -- missing w,x
]
ALLV = ['w', 'x', 'y', 'z']


def term_label(lits):
    return ''.join((n + ("'" if c else '')) for n, c in lits)


def missing_vars(lits):
    present = {n for n, _ in lits}
    return [v for v in ALLV if v not in present]


def order_lits(full_lits):
    return ''.join(v + ("'" if full_lits[v] else '') for v in ALLV)


out2 = []
out2.append('\\PLBL{42}{38}{2c.ii.0}')
out2 += R('𝐺', 12.96, font='c').emit(72.0, 60.0)

col_data2 = []
overlap_tracker = {}
_next_id = [1]
_expansions_tmp = []
for lits in MSOP_TERMS:
    present = {v: c for v, c in lits}
    miss = missing_vars(lits)
    leaves = []
    import itertools as _it
    for combo in _it.product([False, True], repeat=len(miss)):
        d = dict(present)
        for v, c in zip(miss, combo):
            d[v] = c
        leaves.append(order_lits(d))
    _expansions_tmp.append(leaves)
from collections import defaultdict as _dd
_occ = _dd(list)
for i, lvs in enumerate(_expansions_tmp):
    for lf in lvs:
        _occ[lf].append(i)
_overlap_id = {}
for m, idxs in _occ.items():
    if len(idxs) > 1:
        _overlap_id[m] = _next_id[0]
        _next_id[0] += 1

SZ2 = 9.5
X2 = [72.0, 150.0, 230.0, 350.0, 500.0]
Y02 = 90.0
ROWH2 = 26.0

# pass 1: build every row's atoms first so column 5's x-position can be
# fixed from the WIDEST row's column-4 content, not each row's own --
# a per-row dynamic x here would put col5's '=' sign at a different
# place on every line, which is incompatible with a single vertical bar
# drawn once for the whole column (this is exactly the bug the previous
# version had: shorter rows' '=' landed on/behind the bar and read as
# missing).
rows_built = []
max_col4_w = 0.0
for i, lits in enumerate(MSOP_TERMS):
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
    leaves = _expansions_tmp[i]
    parts4 = []
    for j, lf in enumerate(leaves):
        parts4.append(label_atom(lf, SZ2))
        if lf in _overlap_id:
            parts4.append(R(f'({_overlap_id[lf]})', 7.0, font='b'))
        if j != len(leaves) - 1:
            parts4.append(R('+', SZ2, font='c'))
    col4_atom = HB(*parts4)
    max_col4_w = max(max_col4_w, col4_atom.w)
    rows_built.append((col1, col2, col3, col4_atom))

col5_x = X2[3] + max_col4_w + 20.0

for i, (col1, col2, col3, col4_atom) in enumerate(rows_built):
    y = Y02 + i * ROWH2
    lead = '= ' if i == 0 else '+ '
    lead_x = X2[0] - 16
    out2 += R(lead, SZ2, font='c').emit(lead_x, y)
    out2 += label_atom(col1, SZ2).emit(X2[0], y)
    out2 += R('=', SZ2, font='c').emit(X2[1] - 12, y)
    out2 += label_atom(col2, SZ2).emit(X2[1], y)
    out2 += R('=', SZ2, font='c').emit(X2[2] - 12, y)
    out2 += label_atom(col3, SZ2).emit(X2[2], y)
    out2 += R('=', SZ2, font='c').emit(X2[3] - 12, y)
    out2 += col4_atom.emit(X2[3], y)
    out2 += R('=', SZ2, font='c').emit(col5_x, y)
    out2 += label_atom(col1, SZ2).emit(col5_x + 14.0, y)
    if i == 0:
        out2 += R(' = 𝑀𝑆𝑂𝑃(𝐺)', SZ2, font='c').emit(col5_x + 14.0 + label_atom(col1, SZ2).w, y)

bar_xs = [X2[0] - 24.0, X2[1] - 20.0, X2[2] - 20.0, X2[3] - 20.0, col5_x - 8.0]
bar_y0 = Y02 - 2.0
bar_y1 = Y02 + (len(MSOP_TERMS) - 1) * ROWH2 - 6.0
for bx in bar_xs:
    out2.append(f'\\DLINE{{{fmt(bx)}}}{{{fmt(bar_y0)}}}{{{fmt(bx)}}}{{{fmt(bar_y1)}}}{{0.5}}')

Y2end = Y02 + len(MSOP_TERMS) * ROWH2 + 30.0
out2.append(f'\\DLINE{{72.0}}{{{fmt(Y2end-16)}}}{{540.0}}{{{fmt(Y2end-16)}}}{{0.5}}')

positions = [(72.0, Y2end + 20.0), (330.0, Y2end + 20.0), (72.0, Y2end + 170.0), (330.0, Y2end + 170.0)]
tags = ['2c.ii.1', '2c.ii.2', '2c.ii.3', '2c.ii.4']
for lits, (px, py), tag in zip(MSOP_TERMS, positions, tags):
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

with open('sheets/ws6162.tex', 'w') as f:
    f.write('\n'.join(out2) + '\n')
print(f'wrote {len(out2)} lines to sheets/ws6162.tex')
