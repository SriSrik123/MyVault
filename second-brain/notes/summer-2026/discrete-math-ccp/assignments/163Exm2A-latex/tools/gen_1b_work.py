#!/usr/bin/env python3
"""1b work sheets: characteristic-equation solve + k1/k2 system solve for
both cases (p407 distinct-root, p410 repeated-root), plus the
substitution-verification p410 explicitly requires ("Prove by
substitution that your answer is correct"). a=1,b=9,c=5 (gen_402.py).

Case (i) distinct root: x^2-(b+c)x+(bc)=0 -> factors (x-b)(x-c) by
construction -> roots 9,5. k1+k2=1, 9k1+5k2=2 -> k1=-3/4, k2=7/4.
Case (ii) repeated root: a^2x^2-2acx+c^2=0 -> (ax-c)^2=0 -> x=c/a=5
(double). k1=1, 5(k1+k2)=2 -> k2=-3/5.

REBUILT (2026-08-02, Sri posted reference photos of SOL2A's own folio
4080/4110 and said "1b should look like this"). Matches that reference
exactly: every rearrangement is "boxed elimination algebra" (BarStack --
the recurrence over a subtract-both-sides annotation row, over the
rearranged result), every char-eq-to-general-solution derivation is a
bar-chain (rewrite/factor/case-split/root-pick, each its own bar-
separated row, ending in the general k1/k2 form), every k1/k2 system-
solve is bar-inference witness substitution + more boxed elimination
algebra, and case (ii)'s required "prove by substitution" is NOT a flat
algebraic identity check (the old approach) but the same BC/RcS bar-chain
apparatus used throughout this project for induction, minus the SPf/EPf
bookend labels -- p410 asks to verify the closed form solves the
recurrence, not to run a full named induction, so only BC(0)/BC(1)/RcS
are labeled (matching the reference precisely: it never writes "SPf" or
"EPf" here, only where a genuine SPf...EPf proof is being run elsewhere
in this exam). Case (i) has no printed "prove by substitution" text on
its own page (that instruction is p410-specific), so it stops at the
solved closed form -- same asymmetry the reference itself shows (folio
4080 has no BC/RcS section, folio 4110 does).

Every exponent uses atoms.sup() (a real raised atom), never the unicode
superscript-n/zero glyphs -- checked against this font's cmap, superscript
n (U+207F) doesn't exist here; sup() sidesteps it by raising an ordinary
digit/variable instead of depending on a dedicated superscript codepoint.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import R, HB, Kern, Frac, sup, BarStack, Infer, Chain, Chevrons, assign, cdots, fmt
from stack import VStack
from pieces import lay_pieces, write_sheets

OUT_PAGES = os.path.join(os.path.dirname(__file__), '..', 'pages')
OUT_SHEETS = os.path.join(os.path.dirname(__file__), '..', 'sheets')


def write_to_pages(page_numbers, sheets, outdir):
    """Like pieces.write_sheets(), but for REAL pre-numbered blank exam
    pages (408/409 here) rather than synthetic \\worksheet{} insertions --
    page 401's own "blank sheets that follow" already exist as real pages
    in this exam's fixed 32-page layout for 1b(i) specifically (confirmed
    by rendering the ORIGINAL 163Exm2A.pdf directly: pages 408/409 are
    blank in the source, unlike every other problem in this exam, which
    has no spare blank page before the next problem starts and needs
    synthetic \\worksheet{} folios instead). Writes to
    pages/answers{page}.tex, read by the already-existing \\dopage{} calls
    in main.tex -- no new macro, no \\FOLIO{} call needed (the page's own
    printed footer already shows its real page number)."""
    used = []
    if len(sheets) > len(page_numbers):
        raise ValueError(f"{len(sheets)} sheets don't fit in {len(page_numbers)} "
                          f"pre-allocated pages {page_numbers}")
    for page, lines in zip(page_numbers, sheets):
        used.append(page)
        path = os.path.join(outdir, f'answers{page}.tex')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f'%% ===== answers{page}.tex — generated =====\n')
            f.write('\n'.join(lines) + '\n')
        print(f'wrote {path} ({len(lines)} lines)')
    return used
SZ = 10.5
N_ = "\U0001D45B"
M = "−"


def wn(val, sz=SZ):
    return Chevrons([assign(R(N_, sz), R(val, sz), sz=sz)])


def elim_algebra(eq, sub, result, sz=SZ):
    """Boxed elimination algebra: the equation, a subtract-both-sides
    annotation row (the same expression written twice, once per side),
    over a bar, over the rearranged result -- matches the reference's own
    folio 4080/4110 rearrangement step exactly."""
    top = VStack([(R(eq, sz), 0), (HB(R(sub, sz), Kern(60), R(sub, sz)), 8)])
    return BarStack([top, R(result, sz)])


pieces_i = []
pieces = pieces_i  # legacy alias so the (i) block below needs no edits

# ============================================================ 1b (i) =====
pieces.append(("1b.i.0", elim_algebra(
    "𝜌(𝑛+2) − 14𝜌(𝑛+1) + 45𝜌(𝑛) = 0",
    "−(−14𝜌(𝑛+1)+45𝜌(𝑛))",
    "(1)(𝜌(𝑛+2)) = −(−14)(𝜌(𝑛+1)) − (45)(𝜌(𝑛))",
), 6, 6))

ce_rows = [
    R("(1)𝑛²+(−14)𝑛+45 = 0", SZ),
    R("(𝑛−9)(𝑛−5) = 0", SZ),
    R("(𝑛−9=0) ∨ (𝑛−5=0)", SZ),
    R("(𝑛=9) ∨ (𝑛=5)", SZ),
    R("(𝑟₁=5) ∧ (𝑟₂=9)", SZ),
    R("𝑟₁≠𝑟₂", SZ),
    HB(R("∀𝑛∈ℕ  𝜌(𝑛) = 𝑘₁", SZ), sup(R("(5)", SZ), R(N_, SZ)),
       R(" + 𝑘₂", SZ), sup(R("(9)", SZ), R(N_, SZ))),
]
pieces.append(("1b.i.1", BarStack(ce_rows), 6, 6))

sys_i0 = HB(R(f"𝜌({N_}) = 𝑘₁", SZ), sup(R("(5)", SZ), R(N_, SZ)),
            R(" + 𝑘₂", SZ), sup(R("(9)", SZ), R(N_, SZ)))
sys_i_bc0 = BarStack([
    Infer(sys_i0, R("𝜌(0) = 𝑘₁(5)⁰ + 𝑘₂(9)⁰", SZ), wn("0")),
    R("𝜌(0) = 𝑘₁(1) + 𝑘₂(1)", SZ),
])
sys_i_bc1 = BarStack([
    Infer(sys_i0, R("𝜌(1) = 𝑘₁(5)¹ + 𝑘₂(9)¹", SZ), wn("1")),
    R("𝜌(1) = 𝑘₁(5) + 𝑘₂(9)", SZ),
])
pieces.append(("1b.i.2", HB(sys_i_bc0, Kern(24), sys_i_bc1), 6, 6))

eqA = elim_algebra("1 = 𝑘₁ + 𝑘₂", "−𝑘₁", "𝑘₂ = 1 − 𝑘₁")
eqB_rows = [
    R("2 = 𝑘₁(5) + 𝑘₂(9)", SZ),
    R("2 = 𝑘₁(5) + (1−𝑘₁)(9)", SZ),
    R("2 = 5𝑘₁ + 9 − 9𝑘₁", SZ),
    R("2 = 9 − 4𝑘₁", SZ),
]
eqB = BarStack(eqB_rows)
pieces.append(("1b.i.3", HB(eqA, Kern(24), eqB), 6, 6))

solve_k1 = BarStack([
    HB(R("4𝑘₁ = 7", SZ)),
    HB(R("÷4", SZ), Kern(30), R("÷4", SZ)),
    HB(R("𝑘₁ =", SZ), Kern(4), Frac(R("7", SZ), R("4", SZ), sz=SZ)),
])
k2_chain = Chain(R("𝑘₂ = 1 − 𝑘₁", SZ),
                 [('=', HB(R("1 −", SZ), Kern(4), Frac(R("7", SZ), R("4", SZ), sz=SZ))),
                  ('=', Frac(R(f"{M}3", SZ), R("4", SZ), sz=SZ))], sz=SZ, rowgap=8)
pieces.append(("1b.i.4", HB(solve_k1, Kern(24), k2_chain), 6, 6))

final_i = Chain(R(f"∀{N_}∈ℕ    𝜌({N_})", SZ), [
    ('=', HB(R("(", SZ), Frac(R("7", SZ), R("4", SZ), sz=SZ), R(")(5)", SZ),
             sup(R(" ", SZ), R(N_, SZ)), R(" + (", SZ), Frac(R(f"{M}3", SZ), R("4", SZ), sz=SZ),
             R(")(9)", SZ), sup(R(" ", SZ), R(N_, SZ)))),
], sz=SZ, rowgap=8)
pieces.append(("1b.i.5", final_i, 6, 6))

# ============================================================ 1b (ii) ====
pieces_ii = []
pieces = pieces_ii  # legacy alias so the (ii) block below needs no edits
pieces.append(("1b.ii.0", elim_algebra(
    "(1)𝜌(𝑛+2) + (−10)𝜌(𝑛+1) + (25)𝜌(𝑛) = 0",
    "−((−10)𝜌(𝑛+1)+(25)𝜌(𝑛))",
    "(1)(𝜌(𝑛+2)) = (10)(𝜌(𝑛+1)) − (25)(𝜌(𝑛))",
), 6, 6))

ce2_rows = [
    R("(1)𝑛²+(−10)𝑛+25 = 0", SZ),
    R("(𝑛−5)² = 0", SZ),
    R("𝑛 = 5", SZ),
    R("𝑟₁ = 𝑛 = 𝑟₂", SZ),
    HB(R("∀𝑛∈ℕ  𝜌(𝑛) = 𝑘₁", SZ), sup(R("(5)", SZ), R(N_, SZ)),
       R(" + 𝑘₂", SZ), R(N_, SZ), sup(R("(5)", SZ), R(N_, SZ))),
]
pieces.append(("1b.ii.1", BarStack(ce2_rows), 6, 6))

sys_ii0 = HB(R(f"𝜌({N_}) = 𝑘₁", SZ), sup(R("(5)", SZ), R(N_, SZ)),
             R(f" + 𝑘₂{N_}", SZ), sup(R("(5)", SZ), R(N_, SZ)))
sys_ii_bc0 = BarStack([
    Infer(sys_ii0, R("𝜌(0) = 𝑘₁(5)⁰ + 𝑘₂(0)(5)⁰", SZ), wn("0")),
    R("𝜌(0) = 𝑘₁(1) + 𝑘₂(0)(1)", SZ),
])
sys_ii_bc1 = BarStack([
    Infer(sys_ii0, R("𝜌(1) = 𝑘₁(5)¹ + 𝑘₂(1)(5)¹", SZ), wn("1")),
    R("𝜌(1) = 𝑘₁(5) + 𝑘₂(1)(5)", SZ),
])
pieces.append(("1b.ii.2", HB(sys_ii_bc0, Kern(24), sys_ii_bc1), 6, 6))

k1_ii = BarStack([R("𝜌(0) = 𝑘₁(1) = 1", SZ), R("𝑘₁ = 1", SZ)])
k2_ii_rows = [
    R("2 = 𝑘₁(5) + 𝑘₂(1)(5)", SZ),
    R("2 = (1)(5) + 5𝑘₂", SZ),
    R("2 = 5 + 5𝑘₂", SZ),
]
k2_ii = BarStack(k2_ii_rows)
pieces.append(("1b.ii.3", HB(k1_ii, Kern(24), k2_ii), 6, 6))

solve_k2_ii = BarStack([
    HB(R("5𝑘₂ = −3", SZ)),
    HB(R("÷5", SZ), Kern(30), R("÷5", SZ)),
    HB(R("𝑘₂ =", SZ), Kern(4), Frac(R(f"{M}3", SZ), R("5", SZ), sz=SZ)),
])
pieces.append(("1b.ii.4", solve_k2_ii, 6, 6))

final_ii = Chain(R(f"∀{N_}∈ℕ    𝜌({N_})", SZ), [
    ('=', HB(R("(1)(5)", SZ), sup(R(" ", SZ), R(N_, SZ)), R(f" + (", SZ),
             Frac(R(f"{M}3", SZ), R("5", SZ), sz=SZ), R(f")", SZ), R(N_, SZ),
             R("(5)", SZ), sup(R(" ", SZ), R(N_, SZ)))),
], sz=SZ, rowgap=8)
pieces.append(("1b.ii.5", final_ii, 6, 6))

# ---- verification by substitution, required by p410's own text: same
# BC/RcS bar-chain apparatus as an induction proof elsewhere in this
# project, but with no SPf/EPf bookends -- p410 asks to VERIFY the closed
# form solves the recurrence, not to run a separately-named induction.
p_def = HB(R(f"∀{N_}∈ℕ  (  𝑃({N_})", SZ), Kern(4), R("≔", SZ), Kern(4),
           R("(  𝜌(", SZ), R(N_, SZ), R(") = (1)(5)", SZ), sup(R(" ", SZ), R(N_, SZ)),
           R(f" + (", SZ), Frac(R(f"{M}3", SZ), R("5", SZ), sz=SZ), R(f")", SZ), R(N_, SZ),
           R("(5)", SZ), sup(R(" ", SZ), R(N_, SZ)), R("  )  )", SZ))
pieces.append(("1b.ii.6", p_def, 6, 6))

bc0_witness = Infer(R(f"𝑃({N_})", SZ), R("𝑃(0)", SZ), wn("0"))
bc0_check = BarStack([R("𝜌(0) = (1)(5)⁰ + (−3÷5)(0)(5)⁰", SZ), R("𝜌(0) = 1", SZ)])
pieces.append(("1b.ii.7", HB(bc0_witness, Kern(20), bc0_check, Kern(10), R("BC(0)", SZ, font='b')), 6, 6))

bc1_witness = Infer(R(f"𝑃({N_})", SZ), R("𝑃(1)", SZ), wn("1"))
bc1_check = BarStack([R("𝜌(1) = (1)(5)¹ + (−3÷5)(1)(5)¹", SZ), R("𝜌(1) = 2", SZ)])
pieces.append(("1b.ii.8", HB(bc1_witness, Kern(20), bc1_check, Kern(10), R("BC(1)", SZ, font='b')), 6, 6))

rcs_premise = HB(R("𝑃(0) 𝑃(1) ", SZ), cdots(SZ), Kern(2), R(f" 𝑃({N_}) 𝑃({N_}+1)", SZ))
rcs_chain = Chain(R(f"𝜌({N_}+2)", SZ), [
    ('=', R(f"10𝜌({N_}+1) − 25𝜌({N_})", SZ)),
    ('=', HB(R("10((1)(5)", SZ), sup(R(" ", SZ), R(f"{N_}+1", SZ)),
             R(f" + (", SZ), Frac(R(f"{M}3", SZ), R("5", SZ), sz=SZ), R(")(", SZ), R(f"{N_}+1", SZ),
             R(")(5)", SZ), sup(R(" ", SZ), R(f"{N_}+1", SZ)), R(")", SZ))),
    ('=', HB(R(" ", SZ), Kern(0), R(f"− 25((1)(5)", SZ), sup(R(" ", SZ), R(N_, SZ)),
             R(f" + (", SZ), Frac(R(f"{M}3", SZ), R("5", SZ), sz=SZ), R(")", SZ), R(N_, SZ),
             R("(5)", SZ), sup(R(" ", SZ), R(N_, SZ)), R(")", SZ))),
    # distribute the 10/-25 and rewrite every term over the common (5)^n
    # base (10(5)^(n+1)=50(5)^n, -6(n+1)(5)^(n+1)=-30(n+1)(5)^n) so the
    # coefficients can be collected -- this jump (raw substitution straight
    # to the final closed form) was the one genuinely missing step here
    # (audit finding, 2026-08-03).
    ('=', HB(R("(50 − 30(", SZ), R(f"{N_}+1", SZ), R(") − 25 + 15", SZ), R(N_, SZ),
             R(")(5)", SZ), sup(R(" ", SZ), R(N_, SZ)))),
    ('=', HB(R("(−15", SZ), R(N_, SZ), R(" − 5)(5)", SZ), sup(R(" ", SZ), R(N_, SZ)))),
    ('=', HB(R("(−3", SZ), R(N_, SZ), R(" − 1)(5)", SZ), sup(R(" ", SZ), R(f"{N_}+1", SZ)))),
    ('=', HB(R("(1)(5)", SZ), sup(R(" ", SZ), R(f"{N_}+2", SZ)), R(f" + (", SZ),
             Frac(R(f"{M}3", SZ), R("5", SZ), sz=SZ), R(f")(", SZ), R(f"{N_}+2", SZ),
             R(")(5)", SZ), sup(R(" ", SZ), R(f"{N_}+2", SZ)))),
], sz=SZ, rowgap=8)
rcs_stack = BarStack([rcs_premise, rcs_chain, R(f"𝑃({N_}+2)", SZ)])
pieces.append(("1b.ii.9", HB(R("RcS", SZ, font='b'), Kern(20), rcs_stack), 6, 6))

closing = BarStack([
    R("𝑃(0)", SZ),
    HB(R("𝑃(0) 𝑃(1) ", SZ), cdots(SZ), Kern(2), R(f" 𝑃({N_}) 𝑃({N_}+1)", SZ)),
    R(f"𝑃({N_}+2)", SZ),
])
pieces.append(("1b.ii.10", VStack([(closing, 0), (R(f"∀{N_}∈ℕ(𝑃({N_}))", SZ), 10)]), 6, 6))

# 1b(i)'s work goes on the exam's own pre-existing blank pages 408/409
# (real \dopage{} pages, not synthetic worksheets); 1b(ii)'s work has no
# spare blank page left before p411 (1c) starts, so it stays synthetic,
# numbered 4100+ per page 401's own "blank sheets after page N, numbered
# N0,N1,..." convention (N=410 here).
sheets_i = lay_pieces(pieces_i, top_y=90.0)
pages_used = write_to_pages([408, 409], sheets_i, OUT_PAGES)
print("1b(i) work pages:", pages_used)

sheets_ii = lay_pieces(pieces_ii)
folios_ii = write_sheets(4100, sheets_ii, OUT_SHEETS)
print("1b(ii) work sheets:", folios_ii)
