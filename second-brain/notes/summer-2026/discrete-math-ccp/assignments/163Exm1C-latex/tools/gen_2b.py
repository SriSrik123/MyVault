#!/usr/bin/env python3
"""Generate answers312.tex + work sheet(s) 3120... for problem 2b: distinct
4-digit numbers from St(J)={0,1,3,4,7,9} with digit1!=0, digit4=digit1,
digit3>digit2, sum of digits even (<=> digit2+digit3 even, since 2*digit1
is always even). Tree is staggered into 5 tiers, one per digit1 value
(styleguide sec.6.2: wide trees tile the sheet in tiers)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import R, fmt
from expr import St_J
from tree import Node, Tree
from stack import VStack
from pieces import lay_pieces, write_sheets

SZ = 11.04
OUT_PAGES = os.path.join(os.path.dirname(__file__), '..', 'pages')
OUT_SHEETS = os.path.join(os.path.dirname(__file__), '..', 'sheets')

StJ = [0, 1, 3, 4, 7, 9]


def valid23(d2, d3):
    return d3 > d2 and (d2 + d3) % 2 == 0


def build_subtree(d1):
    """digit2 (all 6 tried; dead w/ 2 dashes if no valid digit3, per
    styleguide sec.6.2) -> digit3 (only valid ones are real branches --
    an invalid digit3 was never tried as a slot value here, unlike digit2
    which is tried unconditionally, so it is omitted rather than shown
    dead, matching tree.build()'s leaf-level convention) -> leaf (digit4
    forced := d1, shown as its own completed-number row)."""
    d2_nodes = []
    for d2 in StJ:
        d3_nodes = [Node(f"{d1}{d2}{d3} _", [Node(f"{d1}{d2}{d3}{d1}", [])])
                    for d3 in StJ if valid23(d2, d3)]
        d2_nodes.append(Node(f"{d1}{d2} _ _", d3_nodes))
    return d2_nodes


subtrees = {d1: build_subtree(d1) for d1 in StJ if d1 != 0}


def leaves_of(nodes):
    out = []
    for n in nodes:
        if not n.children:
            if len(n.label) == 4 and n.label.isdigit():
                out.append(n.label)
        else:
            out += leaves_of(n.children)
    return out


numbers = sorted((n for v in subtrees.values() for n in leaves_of(v)), key=int)
assert len(numbers) == 35

# ---------------------------------------------------------------- packed forest
# One shared grand-root (all 4 digits still blank) with all 5 digit1
# subtrees fanned out from it by straight lines -- short to a nearby
# subtree, long-diagonal to one packed lower on the sheet -- instead of
# 5 independently-rooted mini-trees with no connection to a common root.
# A single column of 5 full-depth (digit1-digit2-digit3-leaf) subtrees
# doesn't fit one sheet height-wise, so they're packed 2-2-1 into 3 rows;
# columns are sized small enough (with a wide gutter) that even the
# widest dash-suffixed labels can't bridge the gap between them.
D1_ORDER = [1, 3, 4, 7, 9]
GRID = [[1, 3], [4, 7], [9]]


class PackedForest:
    def __init__(self, sz=8.0, col_w=24.0, col_gap=60.0, row_gap=26.0):
        self.sz = sz
        self.trees = {d1: Tree(3, subtrees[d1], sz=sz, col_w=col_w) for d1 in D1_ORDER}
        tw = col_w * 7   # every subtree has exactly 7 leaves (see leaf-count check)
        row_w = tw * 2 + col_gap
        self.w = row_w
        row_footprint = 20.0 + 34.0 * 3 + 14.0 + 14.0   # Tree's own ht+dp for depth=3

        title_y = 10.0
        groot_y = title_y + 26.0
        row0_y = groot_y + 34.0
        self.anchors = {}   # d1 -> (x, y)
        for r, row in enumerate(GRID):
            ry = row0_y + r * (row_footprint + row_gap)
            row_span = tw * len(row) + col_gap * (len(row) - 1)
            x0 = (row_w - row_span) / 2
            for c, d1 in enumerate(row):
                self.anchors[d1] = (x0 + c * (tw + col_gap), ry)
        self.groot_x, self.groot_y = row_w / 2, groot_y
        self.title_y = title_y
        self.ht = 14.0
        self.dp = row0_y + len(GRID) * row_footprint + (len(GRID) - 1) * row_gap + 10.0

    def emit(self, x, y):
        out = []
        title = "Tree"
        tw = R(title, self.sz + 1, font='b').w
        tx = x + self.w / 2 - tw / 2
        ty = y + self.title_y
        out += R(title, self.sz + 1, font='b').emit(tx, ty)
        out.append(f'\\DLINE{{{fmt(tx)}}}{{{fmt(ty + 3)}}}{{{fmt(tx + tw)}}}{{{fmt(ty + 3)}}}{{0.5}}')
        out.append(f'\\DLINE{{{fmt(tx)}}}{{{fmt(ty + 5)}}}{{{fmt(tx + tw)}}}{{{fmt(ty + 5)}}}{{0.5}}')

        grx, gry = x + self.groot_x, y + self.groot_y
        glabel = "_ _ _ _"
        gw = R(glabel, self.sz).w
        out += R(glabel, self.sz).emit(grx - gw / 2, gry)

        for d1, tr in self.trees.items():
            ax, ay = x + self.anchors[d1][0], y + self.anchors[d1][1]
            root_x, root_y = ax + tr.w / 2, ay + 28.0
            out.append(f'\\DLINE{{{fmt(grx)}}}{{{fmt(gry + 3)}}}'
                       f'{{{fmt(root_x)}}}{{{fmt(root_y - 9)}}}{{0.5}}')
            out += tr.emit(ax, ay, show_title=False, root_label=f"{d1} _ _ _")
        return out


tree_piece = PackedForest(sz=8.0, col_w=24.0)

listing_rows = [numbers[i:i + 7] for i in range(0, len(numbers), 7)]
rows = [(R(", ".join(row) + ("," if i < len(listing_rows) - 1 else ""), SZ), 5.0)
        for i, row in enumerate(listing_rows)]
listing_piece = VStack(rows)

pieces_all = [("2b.0", tree_piece, 4, 14), ("2b.1", listing_piece, 8, 8)]
sheets = lay_pieces(pieces_all)
folios = write_sheets(3120, sheets, OUT_SHEETS)
print("2b work sheets used:", folios)

# ---------------------------------------------------------------- printed page 312
# S = { } is a wide 5-piece assembled brace, x~[144,497] y~[284.45,336.77]
lines312 = []
rows7 = [numbers[i:i + 7] for i in range(0, len(numbers), 7)]
for i, row in enumerate(rows7):
    text = ", ".join(row) + ("," if i < len(rows7) - 1 else "")
    lines312 += R(text, 9.0).emit(152, 292.0 + i * 10.0)
with open(os.path.join(OUT_PAGES, 'answers312.tex'), 'w') as f:
    f.write('%% ===== answers312.tex — generated by gen_2b.py =====\n')
    f.write('\n'.join(lines312) + '\n')
print(f"wrote pages/answers312.tex ({len(lines312)} lines)")
