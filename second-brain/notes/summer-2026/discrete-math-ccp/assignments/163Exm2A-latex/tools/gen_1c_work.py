#!/usr/bin/env python3
"""1c work: for each of the 4 parts, draw the formation tree for the
target expression, the formation tree for the constructed set expression,
and a short cardinality-equals proof -- p411's own directives.

"Formation tree" = operator/connective parse tree (Logic Notes pp.3-4,
19-20 -- see gen_1c.py's docstring for the full citation), NOT the
Sets/Counting Notes element-enumeration "Tree". A simple recursive
node-and-line layout is built here (FTree) since these are small
(root operator, at most 2 children, leaves are the named sets) --
nothing like the scale of 1C's word-generation trees.

Placed directly below "My expression:" on each of p412-415. The word-
problem paragraphs p411 also asks for were removed entirely (2026-08-02,
Sri: "Get rid of the paragraphs in 1c") -- p411's own instruction does
call for one, but this overrides that in favor of a fully symbols-only
page; flagged here in case the missing word problem costs points.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import smart, R, HB, VC, Kern, Atom, sup, binom, fmt

OUT_PAGES = os.path.join(os.path.dirname(__file__), '..', 'pages')
# Bumped up from 10.0/9.0 (audit finding, 2026-08-01: Sri read the built
# pages and found 1c's writing too small next to the rest of the exam) --
# matches the 10.5pt used by every other problem's work sheets this
# session, plus a bit more since 1c's content is proof/tree heavy rather
# than dense equation chains.
SZ = 11.5
PSZ = 10.5


class FTree(Atom):
    """('op', child, child, ...) or a leaf string. Root at top, children
    below connected by straight lines, matching Logic Notes' own
    formation-tree convention (root=outermost connective).

    Node labels route through smart() (math-primary, English fallback),
    not plain R() -- symbol operators (x,coprod,setminus,+,-) are all in
    CMT, but multi-letter word operators used where no single glyph
    exists (Fnc, choose, pow, subsets) have letters CMT lacks (choose:
    h,o,e; pow: p,o,w are all missing from CMT) and need the same
    per-character routing already used everywhere else in this file --
    this was the original gap that made "choose" look unbuildable in the
    first pass (audit finding, 2026-08-01: it isn't unbuildable, it just
    needs the same font-routing every other mixed word already gets)."""
    def __init__(self, node, sz=SZ, xgap=14.0, ygap=22.0):
        self.sz, self.xgap, self.ygap = sz, xgap, ygap
        if isinstance(node, str):
            self.label = smart(node, sz, font='c', mfont='b')
            self.kids = []
        else:
            self.label = smart(node[0], sz, font='c', mfont='b')
            self.kids = [FTree(c, sz, xgap, ygap) for c in node[1:]]
        if not self.kids:
            self.w = self.label.w
            self.ht = self.label.ht
            self.dp = self.label.dp
        else:
            kids_w = sum(k.w for k in self.kids) + xgap * (len(self.kids) - 1)
            self.w = max(self.label.w, kids_w)
            self.ht = self.label.ht
            self.dp = ygap + max(k.ht + k.dp for k in self.kids)

    def emit(self, x, y):
        out = self.label.emit(x + (self.w - self.label.w) / 2, y)
        if not self.kids:
            return out
        kids_w = sum(k.w for k in self.kids) + self.xgap * (len(self.kids) - 1)
        cx = x + (self.w - kids_w) / 2
        cy = y + self.ygap
        root_cx = x + self.label.w / 2 + (self.w - self.label.w) / 2
        for k in self.kids:
            kid_top_x = cx + k.w / 2
            out.append(f'\\DLINE{{{fmt(root_cx)}}}{{{fmt(y + 3)}}}'
                       f'{{{fmt(kid_top_x)}}}{{{fmt(cy - k.ht - 2)}}}{{0.5}}')
            out += k.emit(cx, cy)
            cx += k.w + self.xgap
        return out


def row_gap(row, nxt):
    """Baseline-to-baseline gap from `row` to the row that follows it
    (None if `row` is last). Most rows are one line of plain text, where a
    flat 12pt gap is plenty -- but proof/word rows sometimes hold a
    binom(), or even a binom-of-binoms (p415's nested C(C(..),C(..))),
    which are 2-4 text-lines tall. A flat 12pt only accounts for a normal
    row's own height; it ignores BOTH how far the current row hangs below
    its baseline (row.dp) and how tall the NEXT row rises above its own
    baseline (nxt.ht) -- confirmed by render: both dimensions caused real
    collisions (p414's word-problem binom into "without", p415's nested
    binom into the row above it). Account for both explicitly."""
    next_ht = nxt.ht if nxt is not None else 8.0
    return max(12, row.dp + next_ht + 4)


def write_page(folio, header_lines, trees, proof_lines, y0):
    """header_lines: list of bt()/smart() rows (usually empty now -- kept
    only for a bare witness line where the base page states nothing).
    trees: list of FTree, always [target, constructed-set] in that fixed
    order (no labels -- the fixed target-then-constructed-set order is the
    only disambiguator, same convention every part uses so it stays
    unambiguous without a caption). proof_lines: bare Chain/HB rows, no
    section label. No word-problem argument -- removed entirely."""
    lines = []
    y = y0
    for row in header_lines:
        lines += row.emit(144.02, y)
        y += 13
    y += 6
    for tree in trees:
        lines += tree.emit(144.02, y)
        y += tree.ht + tree.dp + 16
    y += 4
    for i, row in enumerate(proof_lines):
        lines += row.emit(144.02, y)
        y += row_gap(row, proof_lines[i + 1] if i + 1 < len(proof_lines) else None)
    # Idempotent (see gen_3b_work.py for the same pattern/rationale): strip
    # any previous run's block before appending, so re-running this script
    # doesn't duplicate content underneath gen_1c.py's own "My expression".
    marker = '%% ----- 1c formation trees/proof/word problem -----'
    path = os.path.join(OUT_PAGES, f'answers{folio}.tex')
    base = open(path, encoding='utf-8').read().split(marker)[0].rstrip('\n')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(base + '\n\n' + marker + '\n')
        f.write('\n'.join(lines) + '\n')
    print(f"wrote 1c work to pages/answers{folio}.tex ({len(lines)} lines), final y={y:.1f}")


# ---- (i) p412: S := (A co B) x (F \ J), target (a+b)(c-d) ----
write_page(
    412,
    [],
    [FTree(("×", ("+", "𝑎", "𝑏"), ("−", "𝑐", "𝑑"))),
     FTree(("×", ("∐", "𝐴", "𝐵"), ("∖", "𝐹", "𝐽")))],
    [smart("𝜈(𝐴∐𝐵) = 𝜈(𝐴)+𝜈(𝐵) = 𝑎+𝑏", PSZ),
     smart("𝜈(𝐹∖𝐽) = 𝜈(𝐹)−𝜈(𝐽) = 𝑐−𝑑", PSZ),
     smart("𝜈(𝑆) = 𝜈((𝐴∐𝐵)×(𝐹∖𝐽)) = 𝜈(𝐴∐𝐵)×𝜈(𝐹∖𝐽) = (𝑎+𝑏)(𝑐−𝑑)", PSZ)],
    200.0,
)

# ---- (ii) p413: S := Fnc(F co J, A co B), target (a+b)^(c+d) ----
write_page(
    413,
    [],
    [FTree(("pow", ("+", "𝑎", "𝑏"), ("+", "𝑐", "𝑑"))),
     FTree(("𝐹𝑛𝑐", ("∐", "𝐹", "𝐽"), ("∐", "𝐴", "𝐵")))],
    [smart("𝜈(𝐹∐𝐽) = 𝑐+𝑑, 𝜈(𝐴∐𝐵) = 𝑎+𝑏", PSZ),
     HB(smart("𝜈(𝐹𝑛𝑐(𝑃,𝑅)) = 𝜈(𝑅)", PSZ), sup(R(" ", PSZ), R("𝜈(𝑃)", PSZ))),
     HB(R("𝜈(𝑆) = 𝜈(𝐴∐𝐵)", PSZ), sup(R(" ", PSZ), R("𝜈(𝐹∐𝐽)", PSZ)),
        R(" = (𝑎+𝑏)", PSZ), sup(R(" ", PSZ), R("(𝑐+𝑑)", PSZ)))],
    227.0,
)

# ---- (iii) p414: S := (a-b)-subsets of (F co J), target C(c+d,a-b) ----
# "choose" is the target's own root operator (not a page-411 set-operation
# -- that list builds S, it doesn't have to be what labels the GIVEN
# expression's tree); "subsets" is the honest name for what the
# constructed-set root actually does (pick a size and a source set),
# since "k-element-subsets-of" isn't reducible to the 9 listed primitives
# in closed form either -- same standing as Fnc as a named construction.
write_page(
    414,
    [smart("𝐵∖𝐴={ }", PSZ)],
    [FTree(("choose", ("+", "𝑐", "𝑑"), ("−", "𝑎", "𝑏"))),
     FTree(("subsets", ("−", "𝑎", "𝑏"), ("∐", "𝐹", "𝐽")))],
    [smart("𝜈(𝐹∐𝐽) = 𝑐+𝑑", PSZ),
     HB(smart("𝜈(𝑃)=𝑛 → 𝜈(subsets(𝑘,𝑃)) = ", PSZ), binom("𝑛", "𝑘", sz=PSZ)),
     HB(smart("𝜈(𝑆) = ", PSZ), binom("𝑐+𝑑", "𝑎−𝑏", sz=PSZ))],
    211.0,
)

# ---- (iv) p415: nested choose, target C(C(p+q,r+s),C(a-b,c-d)) ----
# R's own source set was mistakenly written as F\J in the first pass --
# F\J already has cardinality c-d (from (i)/(iii)'s own setup, J inside
# F), so "(c-d)-subsets of F\J" would just be C(c-d,c-d)=1, not the
# C(a-b,c-d) the formula actually shows. The target's second choose needs
# a SIZE-(a-b) source, i.e. A\B (B inside A, same convention as (iii)) --
# fixed here (audit finding, 2026-08-01, caught while building the tree
# for this part, which is exactly the kind of check a formation tree
# forces that prose alone let slide).
write_page(
    415,
    [smart("𝑝≔𝑎,𝑞≔𝑏,𝑟≔𝑐,𝑠≔𝑑", PSZ)],
    [FTree(("choose",
            ("choose", ("+", "𝑝", "𝑞"), ("+", "𝑟", "𝑠")),
            ("choose", ("−", "𝑎", "𝑏"), ("−", "𝑐", "𝑑")))),
     FTree(("subsets", "𝜈(𝑅)",
            ("subsets", ("+", "𝑐", "𝑑"), ("∐", "𝐴", "𝐵"))))],
    [HB(smart("𝑃 ≔ subsets((𝑐+𝑑), 𝐴∐𝐵)", PSZ), Kern(10), R("𝜈(𝑃) = ", PSZ), binom("𝑎+𝑏", "𝑐+𝑑", sz=PSZ)),
     HB(smart("𝑅 ≔ subsets((𝑐−𝑑), 𝐴∖𝐵)", PSZ), Kern(10), R("𝜈(𝑅) = ", PSZ), binom("𝑎−𝑏", "𝑐−𝑑", sz=PSZ)),
     HB(smart("𝜈(𝑆) = ", PSZ), binom("𝜈(𝑃)", "𝜈(𝑅)", sz=PSZ))],
    262.0,
)
