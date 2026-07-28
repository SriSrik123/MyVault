#!/usr/bin/env python3
"""Generate answers317.tex + work sheet 3170 for problem 3b.
p+q=4 is FIXED on the exam itself (not J-number data) -- identical for
every student, so matching SOL-2024's own computed values here is a
mathematical necessity, not a copying concern (see styleguide sec.8 #7)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import R, HB, Kern, Chevrons, assign, ditto, mltnom, Chain, BarStack, Frac, wrap, fmt
from expr import N_, K_, MINUS
from stack import VStack
from pieces import lay_pieces, write_sheets

SZ = 11.04
OUT_PAGES = os.path.join(os.path.dirname(__file__), '..', 'pages')
OUT_SHEETS = os.path.join(os.path.dirname(__file__), '..', 'sheets')

N1_, N2_, N3_ = N_ + "₁", N_ + "₂", N_ + "₃"
P_, Q_ = "\U0001D45D", "\U0001D45E"   # 𝑝 𝑞

pairs = [(p, 4 - p) for p in range(5)]   # (0,4),(1,3),(2,2),(3,1),(4,0)


def fr(num, den, sz=SZ):
    return Frac(R(num, sz), R(den, sz), sz=sz)


# ---------------------------------------------------------------- 3b.0: derive n=4
piece0 = BarStack([
    HB(R(f"{N_}={N1_}+{N2_}+{N3_}", SZ),
       Chevrons([assign(R(N1_, SZ), R("0", SZ)), assign(R(N2_, SZ), R(P_, SZ))])),
    HB(R(f"{N_}=0+{P_}+{Q_}", SZ), Chevrons([assign(R(N3_, SZ), R(Q_, SZ))])),
    R(f"{N_}=0+({P_}+{Q_})", SZ),
    HB(R(f"{N_}=0+4", SZ), Chevrons([assign(R(f"({P_}+{Q_})", SZ), R("4", SZ))])),
    R(f"{N_}=4", SZ),
])

# ---------------------------------------------------------------- 3b.1: enumerate splits
piece1 = Chain(R("4", SZ), [R(f"0+{p}+{q}", SZ) for p, q in pairs], sz=SZ)

# ---------------------------------------------------------------- 3b.2: sum, term values, total
def coef(p, q):
    return mltnom("4", ["0", str(p), str(q)], sz=SZ)


sigma_expr = HB(R("∑", SZ + 4), R(f"  {P_}+{Q_}=4  ", SZ * 0.75), coef(P_, Q_))
term_rows = [coef(p, q) for p, q in pairs]
value_rows = [R("1", SZ), fr("4!", "3!"), R("3!", SZ), fr("4!", "3!"), R("1", SZ)]
total_full = HB(R("2+(3!)+(2)", SZ), wrap(fr("4!", "3!"), l='(', r=')', sz=SZ, tight=2.0))


class SumBlock:
    """coefficient column (=/+ prefixed, vertical rule under '=') beside a
    parallel value column, with the final total shown on the top row."""
    def __init__(self, header, terms, values, total, sz=SZ, rowgap=10.0, colgap=18.0):
        self.header, self.total = header, total
        self.rows = list(zip(terms, values))
        self.sz, self.rowgap, self.colgap = sz, rowgap, colgap
        self.term_col_w = max(t.w for t in terms)
        self.val_col_w = max(v.w for v in values)
        self.eq_w = R("=", sz).w
        row_h = max(terms[0].ht + terms[0].dp, values[0].ht) + rowgap
        self.w = self.eq_w + 6 + self.term_col_w + self.colgap + self.val_col_w + \
            self.colgap + total.w
        self.ht = header.ht
        self.dp = header.dp + 24.0 + sum(t.ht + t.dp + rowgap for t, _ in self.rows)

    def emit(self, x, y):
        out = self.header.emit(x, y)
        ty = y + self.header.dp + 24.0
        term_x = x + self.eq_w + 6
        val_x = term_x + self.term_col_w + self.colgap
        tot_x = val_x + self.val_col_w + self.colgap
        rule_top = ty - 2
        for i, (t, v) in enumerate(self.rows):
            ry = ty + t.ht
            sign = "=" if i == 0 else "+"
            out += R(sign, self.sz).emit(x, ry)
            out += t.emit(term_x, ry)
            vsign = "=" if i == 0 else "+"
            out += R(vsign, self.sz).emit(val_x - R(vsign, self.sz).w - 4, ry)
            out += v.emit(val_x, ry)
            if i == 0:
                out += R("=", self.sz).emit(tot_x - R("=", self.sz).w - 4, ry)
                out += self.total.emit(tot_x, ry)
            ty = ry + t.dp + self.rowgap
        rule_bottom = ty - self.rowgap + 2
        out.append(f'\\DLINE{{{fmt(x)}}}{{{fmt(rule_top)}}}{{{fmt(x)}}}{{{fmt(rule_bottom)}}}{{0.6}}')
        out.append(f'\\DLINE{{{fmt(val_x - self.colgap / 2)}}}{{{fmt(rule_top)}}}'
                   f'{{{fmt(val_x - self.colgap / 2)}}}{{{fmt(rule_bottom)}}}{{0.6}}')
        return out


piece2 = SumBlock(sigma_expr, term_rows, value_rows, total_full)

# ---------------------------------------------------------------- 3b.3-3b.5: individual expansions
piece3 = Chain(coef(0, 4), [coef(4, 0), fr("4!", "(0!)(0!)(4!)"), fr("4!", "(1)(1)(4!)"),
                             fr("4!", "4!"), R("1", SZ)], sz=SZ)
piece4 = Chain(coef(1, 3), [coef(3, 1), fr("4!", "(0!)(3!)(1!)"),
                             fr("4!", "(1)(3!)(1)"), fr("4!", "3!")], sz=SZ)
piece5 = Chain(coef(2, 2), [fr("4!", "(0!)(2!)(2!)"), fr("4!", "(1)(2)(2)"), R("3!", SZ)], sz=SZ)

pieces_all = [
    ("3b.0", piece0, 4, 12),
    ("3b.1", piece1, 8, 12),
    ("3b.2", piece2, 8, 14),
    ("3b.3", piece3, 8, 10), ("3b.4", piece4, 8, 10), ("3b.5", piece5, 8, 8),
]
sheets = lay_pieces(pieces_all)
folios = write_sheets(3170, sheets, OUT_SHEETS)
print("3b work sheets used:", folios)

# ---------------------------------------------------------------- printed page 317
lines317 = []
lines317 += R("4", 13).emit(310, 213)
big = HB(R("2+(3!)+(2)", SZ + 3),
         wrap(fr("4!", "3!", sz=SZ + 3), l='(', r=')', sz=SZ + 3, tight=2.0))
lines317 += big.emit(165, 304.70)
with open(os.path.join(OUT_PAGES, 'answers317.tex'), 'w') as f:
    f.write('%% ===== answers317.tex — generated by gen_3b.py =====\n')
    f.write('\n'.join(lines317) + '\n')
print(f"wrote pages/answers317.tex ({len(lines317)} lines)")
