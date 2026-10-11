#!/usr/bin/env python3
"""Worksheet 6180 (work for problem on page 618, tags '3a.i.0'..'3a.ii'):
A_S/A_L/B_S/B_L shown via explicit Smnd()/MSLtr() set and multiset
notation, then the Smplr(B,A) justification bar -- matches peer-reference
structure (folio 6180). Worksheet 6181 ('3a.iii.0') carries the PC version
of G and its formation-tree (moved off the literal facing page 619, same
convention the reference submission uses for every tree in this exam).
"""
import sys
sys.path.insert(0, '.')
from atoms import R, HB, wrap, fmt
from tree import Node, label_atom

SZ = 12.96
out = []

SOP_TERMS = [('wy′z′', 3), ('w′y', 2), ('xy', 2), ('xz′', 2), ('yz', 2)]
MSOP_TERMS = [('w′y', 2), ('wy′z′', 3), ('xz′', 2), ('yz', 2)]


def box(tag, x, y):
    return f'\\PLBL{{{fmt(x)}}}{{{fmt(y)}}}{{{tag}}}'


def term_set_atom(terms, sz=SZ):
    parts = []
    for i, (t, _) in enumerate(terms):
        parts.append(label_atom(t.replace('′', "'"), sz))
        if i != len(terms) - 1:
            parts.append(R(', ', sz, font='b'))
    return wrap(HB(*parts), l='{', r='}', sz=sz)


def multiset_atom(terms, sz=SZ):
    # {var:count, ...} aggregated across all terms
    from collections import Counter
    counts = Counter()
    for t, _ in terms:
        s = t.replace('′', "'")
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i + 1] == "'":
                counts[s[i:i + 2]] += 1
                i += 2
            else:
                counts[s[i]] += 1
                i += 1
    parts = []
    items = sorted(counts.items())
    for i, (lit, c) in enumerate(items):
        parts.append(label_atom(lit, sz))
        parts.append(R(f':{c}', sz, font='b'))
        if i != len(items) - 1:
            parts.append(R(', ', sz, font='b'))
    return wrap(HB(*parts), l='{', r='}', sz=sz)


cells = [
    ('3a.i.0', '𝐴', 'S', 'Smnd', term_set_atom(SOP_TERMS), sum(1 for _ in SOP_TERMS)),
    ('3a.i.1', '𝐴', 'L', 'MSLtr', multiset_atom(SOP_TERMS), sum(n for _, n in SOP_TERMS)),
    ('3a.i.2', '𝐵', 'S', 'Smnd', term_set_atom(MSOP_TERMS), sum(1 for _ in MSOP_TERMS)),
    ('3a.i.3', '𝐵', 'L', 'MSLtr', multiset_atom(MSOP_TERMS), sum(n for _, n in MSOP_TERMS)),
]
positions = [(72.0, 100.0), (320.0, 100.0), (72.0, 220.0), (320.0, 220.0)]
for (tag, var, sub, fn, setatom, val), (px, py) in zip(cells, positions):
    out.append(box(tag, px - 30, py - 24))
    lbl = HB(R(var, SZ, font='c'), R(sub, 9.0, font='b'))
    out += lbl.emit(px, py)
    y2 = py + 24
    l2 = HB(R('= v(', SZ, font='b'), R(fn, SZ, font='b'), R('(', SZ, font='c'), R(var, SZ, font='c'), R('))', SZ, font='c'))
    out += l2.emit(px, y2)
    y2 += 24
    l3 = HB(R('= v(', SZ, font='b'), setatom, R(')', SZ, font='c'))
    out += l3.emit(px, y2)
    y2 += 24
    out += R(f'= {val}', SZ, font='c').emit(px, y2)

Y = 350.0
out.append(box('3a.ii', 42, Y - 24))
just = HB(
    R('¬((', SZ, font='c'), R('𝐴', SZ, font='c'), R('𝐿', 9.0, font='c'), R('=11<9=', SZ, font='c'),
    R('𝐵', SZ, font='c'), R('𝐿', 9.0, font='c'), R(')∧(', SZ, font='c'),
    R('𝐴', SZ, font='c'), R('𝑆', 9.0, font='c'), R('=5≤4=', SZ, font='c'),
    R('𝐵', SZ, font='c'), R('𝑆', 9.0, font='c'), R('))', SZ, font='c'))
out += just.emit(90.0, Y)
Y += 22
just2 = HB(
    R('¬((', SZ, font='c'), R('𝐵', SZ, font='c'), R('𝐿', 9.0, font='c'), R('=9<11=', SZ, font='c'),
    R('𝐴', SZ, font='c'), R('𝐿', 9.0, font='c'), R(')∧(', SZ, font='c'),
    R('𝐵', SZ, font='c'), R('𝑆', 9.0, font='c'), R('=4≤5=', SZ, font='c'),
    R('𝐴', SZ, font='c'), R('𝑆', 9.0, font='c'), R('))', SZ, font='c'))
out += just2.emit(90.0, Y)
Y += 30
out.append(f'\\DLINE{{90.0}}{{{fmt(Y)}}}{{460.0}}{{{fmt(Y)}}}{{0.5}}')
Y += 20
out += R('𝑆𝑚𝑝𝑙𝑟(𝐵,𝐴)', SZ, font='c').emit(150.0, Y)

with open('sheets/ws6180.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to sheets/ws6180.tex')
