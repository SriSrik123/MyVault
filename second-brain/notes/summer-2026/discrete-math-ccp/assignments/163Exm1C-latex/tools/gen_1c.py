#!/usr/bin/env python3
"""Generate answers308.tex + work sheet(s) 3080... for problem 1c: direct
(non-induction) proof that AforAll n in N (4 | rho(n)), rho(n)=2n(n+1).

No solved sample exists for this problem (styleguide sec.8 #6). Structure:
case-split on Evn(n)/Odd(n) (both exam-defined, p303), each case exhibits
the divisibility witness directly and closes with one bar citing the
formal definition a|b :<=> exists c in N (b=ca) (Relations Notes p.24) --
matching that note's OWN proof of 'AforAll n in N (n|0)', which goes
straight from the witnessing equation to the divisibility line with a
single bar, no intermediate exists-statement spelled out.
Bracket-per-case layout mirrors Relations Notes' Refl/AntSym/Trns proofs
(parenthesis-bracketed parallel sub-derivations combined by a final bar).
No Case label is introduced (Rules.md forbids inventing labels the exam
doesn't print) -- the bracket grouping alone carries the case structure.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import R, HB, VC, Infer, Chain, wrap, fmt
from expr import N_, RHO, MINUS
from stack import VStack, Box
from pieces import lay_pieces, write_sheets

SZ = 11.04
OUT_PAGES = os.path.join(os.path.dirname(__file__), '..', 'pages')
OUT_SHEETS = os.path.join(os.path.dirname(__file__), '..', 'sheets')

J_LC = "\U0001D45A"   # 𝑚 (witness for the Evn case -- font lacks math-italic j)
K_LC = "\U0001D458"   # 𝑘  (already K_ in expr, kept local for clarity)
EVN = "\U0001D438\U0001D463\U0001D45B"   # 𝐸𝑣𝑛
ODD = "\U0001D442\U0001D451\U0001D451"   # 𝑂𝑑𝑑
DIV = "|"


def bar(*rows, sz=SZ, pad=4.0, gap=5.0):
    """simple full-width-bar stack: rows separated by single bars."""
    atoms = [R(r, sz) if isinstance(r, str) else r for r in rows]
    from stack import VStack as VS

    class Barred:
        def __init__(self):
            self.w = max(a.w for a in atoms) + 2 * pad
            ys, cy, first = [], 0.0, True
            for a in atoms:
                if first:
                    cy = a.ht; first = False
                else:
                    cy += gap + 0.8 + a.ht
                ys.append(cy)
                cy += a.dp
            self.ys = ys
            self.ht = atoms[0].ht
            self.dp = ys[-1] + atoms[-1].dp

        def emit(self, x, y):
            out = []
            for i, (a, ry) in enumerate(zip(atoms, self.ys)):
                out += a.emit(x + (self.w - a.w) / 2, y + ry)
                if i < len(atoms) - 1:
                    by = y + ry + a.dp + gap
                    out.append(f'\\DLINE{{{fmt(x)}}}{{{fmt(by)}}}'
                               f'{{{fmt(x + self.w)}}}{{{fmt(by)}}}{{0.6}}')
            return out
    return Barred()


def case_block(hyp, witness_line, chain, sz=SZ):
    inner = bar(hyp, witness_line, chain, f"4{DIV}{RHO}({N_})", sz=sz)
    return Box(wrap(inner, l='(', r=')', sz=sz, tight=6.0))


# page-301's literal instruction ("signs of equality... aligned vertically,
# one below the other") applies to every multi-step equality, not just long
# ones -- each transformation gets its own row, first line bare.
chain_evn = Chain(R(f"{RHO}({N_})", SZ), [
    R(f"2{N_}({N_}+1)", SZ),
    R(f"2(2{J_LC})({N_}+1)", SZ),
    R(f"({J_LC}({N_}+1))(4)", SZ),
], sz=SZ)
chain_odd = Chain(R(f"{RHO}({N_})", SZ), [
    R(f"2{N_}({N_}+1)", SZ),
    R(f"2{N_}(2{K_LC})", SZ),
    R(f"({N_}{K_LC})(4)", SZ),
], sz=SZ)
case_evn = case_block(f"{EVN}({N_})", f"{N_}=2{J_LC}", chain_evn)
case_odd = case_block(f"{ODD}({N_})", f"{N_}+1=2{K_LC}", chain_odd)

premise = R(f"{EVN}({N_}) ∨ {ODD}({N_})", SZ)
final = Infer(premise, R(f"4{DIV}{RHO}({N_})", SZ))
epf_line = HB(R(f"∀{N_}∈ℕ(4{DIV}{RHO}({N_}))", SZ), R("    ", SZ),
              R("EPf", SZ, font='b'))
opening_bar = bar(R(f"{N_}∈ℕ", SZ), premise, sz=SZ)
SPF_H = 16.0   # room reserved above opening_bar for its own "SPf" label

# ---------------------------------------------------------------- fit-check
# "Begin your proof on this page and continue onto pages that follow" means
# fill 308 as much as it holds before spilling to a work sheet -- not stop
# after the opening bar just because a work sheet exists. Page 301's footer
# sits at y=789; stay clear of it. No piece-label boxes on the printed page
# (styleguide sec.4's numbered-piece grammar is for blank work sheets only,
# per page 301: "a blank page intended for the purpose").
PAGE_BOTTOM = 780.0
START_Y = 250.0
GAP = 22.0

# each block: (label_or_None, atom, x). label prints as a bold marker to
# the block's left/above only for SPf (a proof delimiter, not a piece).
blocks = [
    ("SPf", opening_bar, 160),
    (None, case_evn, 160),
    (None, case_odd, 160),
    (None, final, 160),
    (None, epf_line, 144.02),
]
y = START_Y
placements = []
for i, (label, blk, x) in enumerate(blocks):
    top = y if i == 0 else y + GAP
    label_h = SPF_H if label else 0.0
    bottom = top + label_h + blk.ht + blk.dp
    if bottom > PAGE_BOTTOM:
        break
    if label:
        placements.append(('label', label, x, top))
    placements.append(('atom', blk, x, top + label_h + blk.ht))
    y = bottom
n_fit = sum(1 for kind, *_ in placements if kind == 'atom')
print(f"1c: {n_fit}/{len(blocks)} blocks fit on printed page 308 "
      f"(last bottom={y:.1f}, limit={PAGE_BOTTOM})")

lines308 = []
# "Fill in the blank" is an inline continuation of the printed sentence
# (A2: matches page303's s:=/b:= precedent) -- must match the printed
# line's own size (14.04), not the SZ=11.04 work-area size used below.
lines308 += R(f"2{N_}({N_}+1)", 14.04).emit(372, 174.38)
for item in placements:
    if item[0] == 'label':
        _, label, x, top = item
        lines308 += R(label, SZ, font='b').emit(144.02, top + 11)
    else:
        _, blk, x, baseline_y = item
        lines308 += blk.emit(x, baseline_y)

overflow = blocks[n_fit:]
if overflow:
    # whatever didn't fit continues on the work sheet, pieces numbered to
    # their true position in the overall proof sequence (the printed-page
    # portion isn't itself a numbered "piece" per page 301's rule, which
    # only requires indexing on blank work sheets)
    names = ["1c.1", "1c.2", "1c.3", "1c.4"]
    pieces_all = [(names[n_fit - 1 + j], b, 4 if j == 0 else 10, 10)
                  for j, (_, b, _) in enumerate(overflow)]
    sheets = lay_pieces(pieces_all)
    folios = write_sheets(3080, sheets, OUT_SHEETS)
    print("1c work sheet(s) used:", folios)
else:
    folios = []
    print("1c: entire proof fits on page 308 -- no work sheet needed")

with open(os.path.join(OUT_PAGES, 'answers308.tex'), 'w') as f:
    f.write('%% ===== answers308.tex — generated by gen_1c.py =====\n')
    f.write('\n'.join(lines308) + '\n')
print(f"wrote pages/answers308.tex ({len(lines308)} lines)")

with open(os.path.join(os.path.dirname(__file__), '.gen_1c_folios'), 'w') as f:
    f.write(','.join(folios))
