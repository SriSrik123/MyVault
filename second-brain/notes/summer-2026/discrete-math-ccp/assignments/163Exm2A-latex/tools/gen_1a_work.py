#!/usr/bin/env python3
"""1a work sheets: coefficient-by-coefficient derivation for both the
binomial (p404) and multinomial (p405) expansions. Page 403's own rule:
"Show calculations for all coefficients that occur on pages that follow
and note only the answer on the page containing the problem."

Placement/format REBUILT (2026-08-02, Sri: "no words ... exactly like the
solution exam" + "put the work for 1a i in the page after 1ai and the work
for 1aii for the page after 1aii"). Read SOL2A-2024's own folios 4040
(after ITS p404) and 4050 (after ITS p405) directly, rendered to PNG: work
for each sub-part sits on its OWN sheet immediately after that sub-part's
own printed page, not bundled together after p406 -- p406 stays untouched
(the original exam's own blank filler page, no `\\worksheet` on it now).
Every row is bar-inference (Infer/BarStack, `<-` chevron witnesses) or a
vertically-aligned `=`/`+` Chain -- zero English words anywhere, matching
the exhibit exactly (it has none either).

Math, a=1,b=9,c=5 (gen_402.py):
  binomial: (9+(-1)x)^5, C(5,k) for k=0..5 = 1,5,10,10,5,1
  multinomial: (5+(-1)x+y)^2, terms (n1,n2,n3) with n1+n2+n3=2,
    coefficient 2!/(n1!n2!n3!)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import (R, HB, VC, Kern, Frac, sup, binom, Chevrons, assign,
                    strike, Infer, Chain, fmt)
from stack import VStack
from pieces import lay_pieces, write_sheets

OUT_SHEETS = os.path.join(os.path.dirname(__file__), '..', 'sheets')
SZ = 10.5
X = "\U0001D465"
Y = "\U0001D466"
M1 = "(−1)"
N_ = "\U0001D45B"
K_ = "\U0001D458"


def fact_frac(n, ks, sz=SZ):
    num = R(f"({n})!", sz)
    den = HB(*[R(f"({k})!", sz) for k in ks])
    return Frac(num, den, sz=sz)


def w1(var_sym, val, sz=SZ):
    return Chevrons([assign(R(var_sym, sz), R(val, sz), sz=sz)])


# ============================================================ 1a (i) ======
pieces_i = []

gen_formula = HB(R("(𝑎+𝑏)", SZ), sup(R(" ", SZ), R(N_, SZ)), R(" = ", SZ),
                  R("∑", SZ), sup(R(" ", SZ), R(N_, SZ)),
                  R("(", SZ), binom(N_, K_, sz=SZ), R(")", SZ),
                  R(" 𝑎", SZ), sup(R(" ", SZ), R(f"{N_}−{K_}", SZ)),
                  R(" 𝑏", SZ), sup(R(" ", SZ), R(K_, SZ)))
sub_i0 = HB(R(f"(9+{M1}𝑥)", SZ), sup(R(" ", SZ), R("5", SZ)), R(" = ∑ ", SZ),
            R("(", SZ), binom("5", K_, sz=SZ), R(")", SZ),
            R(" (9)", SZ), sup(R(" ", SZ), R(f"5−{K_}", SZ)),
            R(f" ({M1}𝑥)", SZ), sup(R(" ", SZ), R(K_, SZ)))
witness_i0 = Chevrons([
    assign(R(N_, SZ), R("5", SZ), sz=SZ),
    assign(R("𝑎", SZ), R("9", SZ), sz=SZ),
    assign(R("𝑏", SZ), R(f"{M1}𝑥", SZ), sz=SZ),
])
pieces_i.append(("1a.i.0", Infer(gen_formula, sub_i0, witness_i0), 8, 8))

terms_i = [(0, "59049", None), (1, f"{M1}32805{X}", None), (2, f"7290{X}", "2"),
           (3, f"{M1}810{X}", "3"), (4, f"45{X}", "4"), (5, f"{M1}{X}", "5")]


def sym_term_i(k):
    return HB(R("(", SZ), binom("5", str(k), sz=SZ), R(")", SZ),
              R(" (9)", SZ), sup(R(" ", SZ), R(str(5 - k), SZ)),
              R(f" ({M1}𝑥)", SZ), sup(R(" ", SZ), R(str(k), SZ)))


sum_first = HB(R("∑", SZ), sup(R(" ", SZ), R("5", SZ)),
               R("(", SZ), binom("5", K_, sz=SZ), R(")", SZ),
               R(" (9)", SZ), sup(R(" ", SZ), R(f"5−{K_}", SZ)),
               R(f" ({M1}𝑥)", SZ), sup(R(" ", SZ), R(K_, SZ)))
steps_i = [('=', sym_term_i(0))] + [('+', sym_term_i(k)) for k in range(1, 6)]
pieces_i.append(("1a.i.1", Chain(sum_first, steps_i, sz=SZ, rowgap=8), 8, 8))

coef_chains_i = {
    0: ("1", None),
    1: ("5", None),
    2: ("10", "cancel"),
    3: ("10", ('sym', 2)),
    4: ("5", ('sym', 1)),
    5: ("1", ('sym', 0)),
}
for k in range(6):
    val, mode = coef_chains_i[k]
    head = HB(R("(", SZ), binom("5", str(k), sz=SZ), R(")", SZ))
    if mode is None:
        chain = Chain(head, [('=', R(val, SZ))], sz=SZ, rowgap=8)
    elif mode == "cancel":
        num_cancel = HB(R("(5)(4)", SZ), Kern(3), strike(R("(3)", SZ)), Kern(3),
                         strike(R("(2)", SZ)), Kern(3), strike(R("(1)", SZ)))
        den_cancel = HB(strike(R("(3)", SZ)), Kern(3), strike(R("(2)", SZ)), Kern(3),
                         strike(R("(1)", SZ)))
        steps = [
            ('=', fact_frac(5, [2, 3])),
            ('=', Frac(num_cancel, den_cancel, sz=SZ)),
            ('=', Frac(R("(5)(4)", SZ), R("(2)(1)", SZ), sz=SZ)),
            ('=', Frac(R("20", SZ), R("2", SZ), sz=SZ)),
            ('=', R(val, SZ)),
        ]
        chain = Chain(head, steps, sz=SZ, rowgap=8)
    else:
        _, symk = mode
        steps = [('=', HB(R("(", SZ), binom("5", f"5−{k}", sz=SZ), R(")", SZ))),
                 ('=', HB(R("(", SZ), binom("5", str(symk), sz=SZ), R(")", SZ))),
                 ('=', R(val, SZ))]
        chain = Chain(head, steps, sz=SZ, rowgap=8)
    val_disp, exp_disp = terms_i[k][1], terms_i[k][2]
    val_atom = sup(R(val_disp, SZ), R(exp_disp, SZ)) if exp_disp else R(val_disp, SZ)
    term_steps = []
    if exp_disp:
        # raw repeated-multiplication form before cleaning up to exponent
        # notation (e.g. "7290xx" -> "7290x²") -- matches the exhibit's own
        # 3-column breakdown (folio 4040: col2 shows "1176xx" as its own
        # step, col3 cleans it up to "1176x²"), which my first pass here
        # skipped, going straight to the exponent form (audit finding,
        # 2026-08-03: Sri asked to show ALL the work in the solution exam).
        term_steps.append(('=', R(val_disp + X * (int(exp_disp) - 1), SZ)))
    term_steps.append(('=', val_atom))
    term_line = Chain(sym_term_i(k), term_steps, sz=SZ, rowgap=8)
    block = VStack([(chain, 0), (term_line, 10)])
    pieces_i.append((f"1a.i.{2+k}", block, 6, 6))

sheets_i = lay_pieces(pieces_i)
folios_i = write_sheets(4040, sheets_i, OUT_SHEETS)
print("1a(i) work sheets:", folios_i)

# ============================================================ 1a (ii) =====
pieces_ii = []

gen_formula2 = HB(R("(𝑎+𝑏+𝑐)", SZ), sup(R(" ", SZ), R(N_, SZ)), R(" = ∑ ", SZ),
                   R("(", SZ), R(f"{N_},{K_}₁,{K_}₂,{K_}₃", SZ), R(")", SZ),
                   R(" 𝑎", SZ), sup(R(" ", SZ), R(f"{K_}₁", SZ)),
                   R(" 𝑏", SZ), sup(R(" ", SZ), R(f"{K_}₂", SZ)),
                   R(" 𝑐", SZ), sup(R(" ", SZ), R(f"{K_}₃", SZ)))
sub_ii0 = HB(R(f"(5+{M1}𝑥+𝑦)", SZ), sup(R(" ", SZ), R("2", SZ)), R(" = ∑ ", SZ),
             R("(", SZ), R(f"2,{K_}₁,{K_}₂,{K_}₃", SZ), R(")", SZ),
             R(" (5)", SZ), sup(R(" ", SZ), R(f"{K_}₁", SZ)),
             R(f" ({M1}𝑥)", SZ), sup(R(" ", SZ), R(f"{K_}₂", SZ)),
             R(" (𝑦)", SZ), sup(R(" ", SZ), R(f"{K_}₃", SZ)))
witness_ii0 = Chevrons([
    assign(R(N_, SZ), R("2", SZ), sz=SZ),
    assign(R("𝑎", SZ), R("5", SZ), sz=SZ),
    assign(R("𝑏", SZ), R(f"{M1}𝑥", SZ), sz=SZ),
    assign(R("𝑐", SZ), R("𝑦", SZ), sz=SZ),
])
pieces_ii.append(("1a.ii.0", Infer(gen_formula2, sub_ii0, witness_ii0), 8, 8))

parts_ii = [(2, 0, 0), (0, 2, 0), (0, 0, 2), (1, 1, 0), (1, 0, 1), (0, 1, 1)]
part_first = R("2", SZ)
part_steps = [('=', R(f"{n1}+{n2}+{n3}", SZ)) for (n1, n2, n3) in parts_ii]
pieces_ii.append(("1a.ii.1", Chain(part_first, part_steps, sz=SZ, rowgap=8), 6, 6))


def sym_term_ii(n1, n2, n3):
    return HB(R("(", SZ), R(f"2,{n1},{n2},{n3}", SZ), R(")", SZ),
              R(" (5)", SZ), sup(R(" ", SZ), R(str(n1), SZ)),
              R(f" ({M1}𝑥)", SZ), sup(R(" ", SZ), R(str(n2), SZ)),
              R(" (𝑦)", SZ), sup(R(" ", SZ), R(str(n3), SZ)))


sum_first2 = HB(R("∑", SZ),
                R("(", SZ), R(f"2,{K_}₁,{K_}₂,{K_}₃", SZ), R(")", SZ),
                R(" (5)", SZ), sup(R(" ", SZ), R(f"{K_}₁", SZ)),
                R(f" ({M1}𝑥)", SZ), sup(R(" ", SZ), R(f"{K_}₂", SZ)),
                R(" (𝑦)", SZ), sup(R(" ", SZ), R(f"{K_}₃", SZ)))
steps_ii = [('=', sym_term_ii(*parts_ii[0]))] + [('+', sym_term_ii(*p)) for p in parts_ii[1:]]
pieces_ii.append(("1a.ii.2", Chain(sum_first2, steps_ii, sz=SZ, rowgap=8), 8, 8))

term_vals = {(2, 0, 0): "25", (1, 1, 0): f"{M1}10{X}", (0, 2, 0): f"{X}²",
             (0, 1, 1): f"{M1}2{X}{Y}", (1, 0, 1): f"10{Y}", (0, 0, 2): f"{Y}²"}
mcoef = {(2, 0, 0): 1, (1, 1, 0): 2, (0, 2, 0): 1,
         (0, 1, 1): 2, (1, 0, 1): 2, (0, 0, 2): 1}
for i, (n1, n2, n3) in enumerate(parts_ii):
    val = mcoef[(n1, n2, n3)]
    head = HB(R("(", SZ), R(f"2,{n1},{n2},{n3}", SZ), R(")", SZ))
    steps = [('=', fact_frac(2, [n1, n2, n3])), ('=', R(str(val), SZ))]
    chain = Chain(head, steps, sz=SZ, rowgap=8)
    final_val = term_vals[(n1, n2, n3)]
    term_steps2 = []
    # same raw-multiplication intermediate as part (i): (0,2,0) and (0,0,2)
    # are the only exponent-2 terms here (total degree 2), so only they get
    # an "xx"/"yy" step before the exponent-notation cleanup.
    if n2 >= 2:
        term_steps2.append(('=', R(X * n2, SZ)))
    elif n3 >= 2:
        term_steps2.append(('=', R(Y * n3, SZ)))
    term_steps2.append(('=', R(final_val, SZ)))
    term_line = Chain(sym_term_ii(n1, n2, n3), term_steps2, sz=SZ, rowgap=8)
    block = VStack([(chain, 0), (term_line, 10)])
    pieces_ii.append((f"1a.ii.{3+i}", block, 6, 6))

sheets_ii = lay_pieces(pieces_ii)
folios_ii = write_sheets(4050, sheets_ii, OUT_SHEETS)
print("1a(ii) work sheets:", folios_ii)

with open(os.path.join(os.path.dirname(__file__), '.gen_1a_work_folios'), 'w') as f:
    f.write(','.join(folios_i + folios_ii))
