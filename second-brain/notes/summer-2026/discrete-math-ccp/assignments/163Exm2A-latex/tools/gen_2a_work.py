#!/usr/bin/env python3
"""2a work sheet (p417): the step-by-step unroll for alpha(0..3)/phi(0..3)
and the derivation of the parity-selector closed form. a=1,b=9,c=5,d=7
(gen_402.py).

REBUILT (2026-08-02, Sri: "no words ... exactly like the solution exam" +
"all the proofs need to be in proof format with the equal signs lineing
up"). Read SOL2A-2024's own folio 4160 directly, rendered to PNG: every
unroll step is bar-inference (general recurrence over a bar, instantiated
below, `<-` chevron witness) continuing into a plain aligned-`=` Chain --
zero English words anywhere. Rebuilt to that exact shape; the two-step
reduction and the final recombination now reuse gen_2a.py's own
closed_form() so the work sheet and the printed answer are the identical
object, not independently retyped.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import R, HB, Kern, Frac, sup, Infer, Chain, Chevrons, assign, fmt, Atom
from stack import VStack
from pieces import lay_pieces, write_sheets
from gen_2a import closed_form, FloorAtom

OUT_SHEETS = os.path.join(os.path.dirname(__file__), '..', 'sheets')
SZ = 10.5
N_ = "\U0001D45B"
A = "\U0001D6FC"
PH = "\U0001D711"
M = "−"


def w1(var_sym, val, sz=SZ):
    return Chevrons([assign(R(var_sym, sz), R(val, sz), sz=sz)])


pieces = []

# phi(0) := alpha(0)+c, the one seed that needs a step (alpha(0):=1 is a
# raw given, not derived -- no piece needed for it).
phi0 = Chain(R(f"{PH}(0)", SZ), [('=', R(f"{A}(0)+5", SZ)), ('=', R("1+5", SZ)), ('=', R("6", SZ))], sz=SZ, rowgap=8)
pieces.append(("2a.0", phi0, 6, 6))


def unroll_step(idx, lhs_name, gen_lhs, gen_rhs, n_val, inst_rhs, final_lhs, num_rhs, result):
    gen = R(f"{gen_lhs} = {gen_rhs}", SZ)
    inst = R(f"{lhs_name}({n_val}+1) = {inst_rhs}", SZ)
    tail = Chain(R(f"{final_lhs} = {num_rhs}", SZ), [('=', R(result, SZ))], sz=SZ, rowgap=8)
    block = VStack([(inst, 0), (tail, 10)])
    return Infer(gen, block, w1(N_, str(idx)))


steps = [
    unroll_step(0, A, f"{A}({N_}+1)", f"{PH}({N_})(9)", 0, f"{PH}(0)(9)", f"{A}(1)", "(6)(9)", "54"),
    unroll_step(0, PH, f"{PH}({N_}+1)", f"{A}({N_})(7)+1", 0, f"{A}(0)(7)+1", f"{PH}(1)", "(1)(7)+1", "8"),
    unroll_step(1, A, f"{A}({N_}+1)", f"{PH}({N_})(9)", 1, f"{PH}(1)(9)", f"{A}(2)", "(8)(9)", "72"),
    unroll_step(1, PH, f"{PH}({N_}+1)", f"{A}({N_})(7)+1", 1, f"{A}(1)(7)+1", f"{PH}(2)", "(54)(7)+1", "379"),
    unroll_step(2, A, f"{A}({N_}+1)", f"{PH}({N_})(9)", 2, f"{PH}(2)(9)", f"{A}(3)", "(379)(9)", "3411"),
    unroll_step(2, PH, f"{PH}({N_}+1)", f"{A}({N_})(7)+1", 2, f"{A}(2)(7)+1", f"{PH}(3)", "(72)(7)+1", "505"),
]
for i, blk in enumerate(steps):
    pieces.append((f"2a.{1+i}", blk, 8, 8))

# two-step reduction: alpha(n+2), phi(n+2) as bare aligned Chains
red_a = Chain(R(f"{A}({N_}+2)", SZ),
              [('=', R(f"{PH}({N_}+1)(9)", SZ)),
               ('=', R(f"({A}({N_})(7)+1)(9)", SZ)),
               ('=', R(f"(63){A}({N_})+9", SZ))], sz=SZ, rowgap=8)
red_p = Chain(R(f"{PH}({N_}+2)", SZ),
              [('=', R(f"{A}({N_}+1)(7)+1", SZ)),
               ('=', R(f"({PH}({N_})(9))(7)+1", SZ)),
               ('=', R(f"(63){PH}({N_})+1", SZ))], sz=SZ, rowgap=8)
pieces.append(("2a.7", HB(red_a, Kern(30), red_p), 8, 8))

# alpha(2m), alpha(2m+1) -- geometric-plus-constant closed form in m,
# seeded by alpha(0)=1 resp. alpha(1)=54, citing the same
# ratio-63/increment-9 two-step recurrence just derived above.
m_def = HB(R("𝑚 ≔ ", SZ), FloorAtom(Frac(R(N_, SZ), R("2", SZ), sz=SZ), SZ))
a_even = R(f"{A}(2𝑚) = (63)", SZ)
a_even_full = HB(a_even, sup(R(" ", SZ), R("𝑚", SZ)), R(f"(1 {M} (9÷62)) + (9÷62)", SZ))
a_odd_full = HB(R(f"{A}(2𝑚+1) = (63)", SZ), sup(R(" ", SZ), R("𝑚", SZ)),
                R(f"(54 {M} (9÷62)) + (9÷62)", SZ))
pieces.append(("2a.8", VStack([(m_def, 0), (a_even_full, 10), (a_odd_full, 8)]), 8, 8))

p_even_full = HB(R(f"{PH}(2𝑚) = (63)", SZ), sup(R(" ", SZ), R("𝑚", SZ)),
                 R(f"(6 {M} (1÷62)) + (1÷62)", SZ))
p_odd_full = HB(R(f"{PH}(2𝑚+1) = (63)", SZ), sup(R(" ", SZ), R("𝑚", SZ)),
                R(f"(8 {M} (1÷62)) + (1÷62)", SZ))
pieces.append(("2a.9", VStack([(p_even_full, 0), (p_odd_full, 8)]), 8, 8))

# final recombination -- reuses gen_2a.py's own closed_form() (the exact
# object placed on p417 as the answer), so the parity-selector unified
# formula that folds the 2m/2m+1 cases above into ONE expression is never
# retyped independently.
recomb_m = HB(R("𝑚 ≔ ", SZ), FloorAtom(Frac(R(N_, SZ), R("2", SZ), sz=SZ), SZ))
alpha_final = HB(R(f"{A}({N_}) = ", SZ), closed_form(1, 54, 63, 9, 62, sz=SZ))
phi_final = HB(R(f"{PH}({N_}) = ", SZ), closed_form(6, 8, 63, 1, 62, sz=SZ))
pieces.append(("2a.10", VStack([(recomb_m, 0), (alpha_final, 10), (phi_final, 10)]), 8, 8))

sheets = lay_pieces(pieces)
folios = write_sheets(4170, sheets, OUT_SHEETS)
print("2a work sheets:", folios)
