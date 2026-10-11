#!/usr/bin/env python3
"""3a work sheet (p425): the step-by-step unroll for phi(0..3) and the
derivation showing how the closed-form conjecture was arrived at. The
induction PROOF is on p424/425 itself; this sheet covers the earlier step
of finding the conjecture in the first place. b=9,c=5,d=7 (gen_402.py).

phi(0)=c=5, phi(n+1)=phi(n)(9)+7.
phi(1)=(5)(9)+7=52, phi(2)=(52)(9)+7=475, phi(3)=(475)(9)+7=4282.
Repeated substitution: phi(n) = 9^n phi(0) + 7(9^(n-1)+...+9+1)
                              = 5(9^n) + 7((9^n-1)/8)   [geometric sum, r=9]

REBUILT (2026-08-02, Sri: "no words ... exactly like the solution exam" +
"equal signs lineing up"). Unroll steps are now bar-inference (general
recurrence over a bar, instantiated below, chevron witness) matching 2a's
exhibit-derived shape; the repeated-substitution and geometric-sum-closing
derivations are genuine Chains (one running expression, `=` aligned in a
single column), replacing the old flat-HB VStacks. Zero English words --
the one connector word this sheet had ("so") is gone too.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import R, HB, Kern, Frac, sup, cdots, Infer, Chain, Chevrons, assign, fmt
from stack import VStack
from pieces import lay_pieces, write_sheets

OUT_SHEETS = os.path.join(os.path.dirname(__file__), '..', 'sheets')
SZ = 10.5
N_ = "\U0001D45B"
PH = "\U0001D711"
M = "−"


def w1(val, sz=SZ):
    return Chevrons([assign(R(N_, sz), R(val, sz), sz=sz)])


pieces = []

# ----------------------------------------------------------- unroll -------
def unroll_step(idx, n_val, num_rhs, result):
    gen = R(f"{PH}({N_}+1) = {PH}({N_})(9)+7", SZ)
    inst = R(f"{PH}({n_val}+1) = {PH}({n_val})(9)+7", SZ)
    tail = Chain(R(f"{PH}({idx}) = {num_rhs}", SZ), [('=', R(result, SZ))], sz=SZ, rowgap=8)
    return Infer(gen, VStack([(inst, 0), (tail, 10)]), w1(str(n_val)))


steps = [
    unroll_step(1, 0, "(5)(9)+7", "52"),
    unroll_step(2, 1, "(52)(9)+7", "475"),
    unroll_step(3, 2, "(475)(9)+7", "4282"),
]
for i, blk in enumerate(steps):
    pieces.append((f"3a.{i}", blk, 8, 8))

# ------------------------------------------------ repeated substitution ---
sub_first = R(f"{PH}({N_})", SZ)
sub_steps = [
    ('=', R(f"9{PH}({N_}−1)+7", SZ)),
    ('=', HB(R("9(9", SZ), R(f"{PH}({N_}−2)+7)+7", SZ))),
    ('=', HB(R("9", SZ), sup(R(" ", SZ), R("2", SZ)), R(f"{PH}({N_}−2) + (9)(7) + 7", SZ))),
    ('=', HB(R("9", SZ), sup(R(" ", SZ), R("2", SZ)), R(f"(9{PH}({N_}−3)+7) + (9)(7)+7", SZ))),
    ('=', HB(R("9", SZ), sup(R(" ", SZ), R("3", SZ)), R(f"{PH}({N_}−3) + 9", SZ),
             sup(R(" ", SZ), R("2", SZ)), R("(7)+(9)(7)+7", SZ))),
    ('=', HB(R("9", SZ), sup(R(" ", SZ), R(N_, SZ)), R(f"{PH}(0) + 7(9", SZ),
             sup(R(" ", SZ), R(f"{N_}−1", SZ)), R("+9", SZ), sup(R(" ", SZ), R(f"{N_}−2", SZ)),
             R("+", SZ), cdots(SZ), R("+9+1)", SZ))),
]
pieces.append(("3a.3", Chain(sub_first, sub_steps, sz=SZ, rowgap=8), 8, 8))

# ---------------------------------------------- geometric-sum closing -----
geo_first = HB(R("9", SZ), sup(R(" ", SZ), R(f"{N_}−1", SZ)), R("+", SZ), cdots(SZ), R("+9+1", SZ))
geo_steps = [
    ('=', HB(R("(9", SZ), sup(R(" ", SZ), R(N_, SZ)), R(f"{M}1) ÷ (9{M}1)", SZ))),
    ('=', HB(R("(9", SZ), sup(R(" ", SZ), R(N_, SZ)), R(f"{M}1) ÷ 8", SZ))),
]
pieces.append(("3a.4", Chain(geo_first, geo_steps, sz=SZ, rowgap=8), 8, 8))

final_first = R(f"{PH}({N_})", SZ)
final_steps = [
    ('=', HB(R("9", SZ), sup(R(" ", SZ), R(N_, SZ)), R("(5) + 7((9", SZ),
             sup(R(" ", SZ), R(N_, SZ)), R(f"{M}1) ÷ 8)", SZ))),
    ('=', HB(R("(5)(9)", SZ), sup(R(" ", SZ), R(N_, SZ)), R(" + (7)((9", SZ),
             sup(R(" ", SZ), R(N_, SZ)), R(f"{M}1) ÷ 8)", SZ))),
]
pieces.append(("3a.5", Chain(final_first, final_steps, sz=SZ, rowgap=8), 8, 8))

sheets = lay_pieces(pieces)
folios = write_sheets(4250, sheets, OUT_SHEETS)
print("3a work sheets:", folios)
