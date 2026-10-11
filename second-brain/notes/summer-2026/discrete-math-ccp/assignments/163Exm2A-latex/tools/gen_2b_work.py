#!/usr/bin/env python3
"""2b work sheets (p418, p420): how the Sm(alpha,n)/Sm(phi,n) conjectures
were arrived at.

REBUILT (2026-08-03, Sri posted SOL2A-2024's own 2b.i/2b.ii exhibit pages
(folios 4190/4191) and said "make sure mine is similar"). Restructured to
match that reference's own approach: cite 2a's already-established general
parity-selector closed form, substitute the chosen parity variable under
an explicit "for all p, Evn(p)"/"for all q, Odd(q)" hypothesis, simplify
the parity selector at that specific parity, THEN sum term-by-term and
apply the geometric series formula, then combine the even/odd halves --
rather than the previous approach of asserting an already-simplified
per-parity closed form with no derivation shown at all.

This rebuild also fixes a REAL math bug the previous version had: its
per-parity closed forms showed (v0 - inc/denom)(ratio)^m + inc/denom
instead of the correct (v0 + inc/denom)(ratio)^m - inc/denom -- a sign
error in the fixed-point/particular-solution derivation (confirmed wrong
by direct computation against the actual recurrence: the old formula
gave alpha(2)=54, the real value is 72). The PRINTED page (gen_2b.py,
p419's "My Conjectures") was never affected by this -- it already,
independently, used the correct 71/3357/373/497 coefficients (verified
programmatically against direct summation for n=0..5) -- only this work
sheet's shown derivation was wrong, meaning the work shown didn't
actually arrive at the printed answer. Every formula below was
numerically re-verified against direct recurrence unrolling + direct
summation (fractions.Fraction, exact arithmetic) before typesetting.

a=1,b=9,c=5,d=7 (gen_402.py) -> alpha(0)=1,alpha(1)=54,
alpha(n+2)=63*alpha(n)+9 (ratio=bd=63,inc=ab=9); phi(0)=6,phi(1)=8,
phi(n+2)=63*phi(n)+1 (inc=a=1). Both denom=ratio-1=62.
  alpha even coef = 1+9/62  = 71/62     alpha odd coef = 54+9/62 = 3357/62
  phi   even coef = 6+1/62  = 373/62    phi   odd coef = 8+1/62  = 497/62
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import (R, HB, Kern, Frac, sup, Chain, BarStack, smart,
                    fmt, Atom)
from stack import VStack
from pieces import lay_pieces, write_sheets

OUT_SHEETS = os.path.join(os.path.dirname(__file__), '..', 'sheets')
SZ = 9.0
CSZ = 7.5   # citation-formula size -- matches 2a's own shrink for this exact wide formula
N_ = "\U0001D45B"
P_ = "\U0001D45D"
Q_ = "\U0001D45E"
M_ = "\U0001D45A"
A = "\U0001D6FC"
PH = "\U0001D711"
M = "−"


class FloorAtom(Atom):
    """floor(inner) via \\TDEL, both brackets. Width includes a
    height-proportional term (matching atoms.Delim's own documented fix)."""
    def __init__(self, inner, sz):
        self.inner, self.sz = inner, sz
        pad = 1.0
        self.ht = inner.ht + pad
        self.dp = inner.dp + pad
        self.gap = 3.5
        self.w = self.gap + inner.w + self.gap + 0.15 * (self.ht + self.dp)

    def emit(self, x, y):
        h = self.ht + self.dp
        half = h / 2
        yc = y - (self.ht - self.dp) / 2
        out = [f"\\TDEL{{{fmt(x)}}}{{{fmt(yc)}}}{{{self.sz:g}}}"
               f"{{{fmt(half)}}}{{{fmt(half)}}}{{\\lfloor}}"]
        out += self.inner.emit(x + self.gap, y)
        xr = x + self.gap + self.inner.w + self.gap
        out.append(f"\\TDEL{{{fmt(xr)}}}{{{fmt(yc)}}}{{{self.sz:g}}}"
                   f"{{{fmt(half)}}}{{{fmt(half)}}}{{\\rfloor}}")
        return out


def floor_bare(num_str, sz):
    return FloorAtom(Frac(R(num_str, sz), R("2", sz), sz=sz), sz)


def unified_cf(v0, v1, ratio, inc, denom, var, sz):
    """2a's own parity-selector closed form (gen_2a.py's closed_form()),
    cited verbatim with `var` substituted for n -- this is 2a's ALREADY
    VERIFIED formula (printed on p416/417), never re-derived here."""
    floor_v = floor_bare(var, sz)
    pw = sup(R(f"({ratio})", sz), floor_v)
    m1 = R(f"({M}1)", sz)
    par1 = Frac(HB(R("1+", sz), sup(m1, R(var, sz))), R("2", sz), sz=sz)
    par2 = Frac(HB(R("1+", sz), sup(m1, R(f"{var}+1", sz))), R("2", sz), sz=sz)
    bracket = HB(R("(", sz), R(f"({v0})", sz), Kern(2), R("(", sz), par1, R(")", sz),
                 Kern(3), R("+", sz), Kern(3),
                 R(f"({v1})", sz), Kern(2), R("(", sz), par2, R(")", sz), R(")", sz))
    part1 = HB(pw, Kern(2), bracket)
    floor_v2 = floor_bare(var, sz)
    pw2 = sup(R(f"({ratio})", sz), floor_v2)
    num2 = HB(pw2, R(f" {M} 1", sz))
    frac2 = Frac(num2, R(str(denom), sz), sz=sz)
    part2 = HB(R(f"({inc})", sz), Kern(2), R("(", sz), frac2, R(")", sz))
    return HB(part1, Kern(4), R("+", sz), Kern(4), part2)


def exp_frac(var, is_even, sz):
    """the (now floor-less) exponent once parity is fixed: p/2 (even) or
    (q-1)/2 (odd) -- both are exact integers once the parity is known, no
    floor needed."""
    if is_even:
        return Frac(R(var, sz), R("2", sz), sz=sz)
    return Frac(R(f"{var}{M}1", sz), R("2", sz), sz=sz)


def bracket_values(v0, v1, ratio, inc, denom, var, is_even, sz):
    """parity selector evaluated to literal 0/1 and the floor dropped --
    matches the exhibit's own "(6)(1)+(12)(0)" row exactly."""
    sel0, sel1 = ("1", "0") if is_even else ("0", "1")
    pw = sup(R(f"({ratio})", sz), exp_frac(var, is_even, sz))
    bracket = HB(R("(", sz), R(f"({v0})({sel0})", sz), Kern(3), R("+", sz), Kern(3),
                 R(f"({v1})({sel1})", sz), R(")", sz))
    part1 = HB(pw, Kern(2), bracket)
    pw2 = sup(R(f"({ratio})", sz), exp_frac(var, is_even, sz))
    num2 = HB(pw2, R(f" {M} 1", sz))
    frac2 = Frac(num2, R(str(denom), sz), sz=sz)
    part2 = HB(R(f"({inc})", sz), Kern(2), R("(", sz), frac2, R(")", sz))
    return HB(part1, Kern(4), R("+", sz), Kern(4), part2)


def bracket_distributed(v_sel, ratio, inc, denom, var, is_even, sz):
    """multiply the selector through and distribute the inc/denom term --
    lands on the per-term closed form actually used by the sum step."""
    pw = sup(R(f"({ratio})", sz), exp_frac(var, is_even, sz))
    term1 = HB(pw, Kern(2), R(f"({v_sel})", sz))
    incfrac = Frac(R(str(inc), sz), R(str(denom), sz), sz=sz)
    pw2 = sup(R(f"({ratio})", sz), exp_frac(var, is_even, sz))
    term2 = HB(R("(", sz), incfrac, R(")", sz), Kern(2), pw2)
    term3 = HB(R("(", sz), incfrac, R(")", sz))
    return HB(term1, Kern(3), R("+", sz), Kern(3), term2, Kern(3), R(f"{M}", sz), Kern(3), term3)


def citation_atom(func_sym, word, var, v0, v1, v_sel, ratio, inc, denom, is_even):
    hyp = smart(f"∀{var}∈ℕ({word}({var}))", SZ)
    general_var = HB(R(f"{func_sym}({var}) = ", CSZ), unified_cf(v0, v1, ratio, inc, denom, var, CSZ))
    citation_block = BarStack([hyp, general_var])
    simp_chain = Chain(R(f"{func_sym}({var})", SZ), [
        ('=', bracket_values(v0, v1, ratio, inc, denom, var, is_even, CSZ)),
        ('=', bracket_distributed(v_sel, ratio, inc, denom, var, is_even, CSZ)),
    ], sz=SZ, rowgap=8)
    return VStack([(citation_block, 0), (simp_chain, 10)])


def sigma(fl_atom, sz):
    return HB(R("∑", sz), sup(R(" ", sz), fl_atom))


def sum_atom(func_sym, v_sel, ratio, inc, denom, is_even, combined_num, m_reindex):
    """sum the per-term closed form (from citation_atom) over its index
    and apply the geometric series formula (cited in 2b.0). Compressed to
    3 steps, not 5 (2026-08-03, Sri: "i think you can combine some of the
    points") -- distribute-the-sum and evaluate-the-constant-subsum land
    in one row, and collect-the-coefficient and apply-the-geometric-
    formula land in another, matching the exhibit's own economy rather
    than showing every individual algebraic move as its own line."""
    sz = SZ
    fl_str = N_ if is_even else f"{N_}{M}1"
    incfrac = Frac(R(str(inc), sz), R(str(denom), sz), sz=sz)

    first = HB(sigma(floor_bare(fl_str, sz), sz), R(" ", sz), R(f"{func_sym}({m_reindex})", sz))

    per_term = HB(sup(R(f"({ratio})", sz), R(M_, sz)), Kern(2), R(f"({v_sel})", sz), Kern(3),
                  R("+", sz), Kern(3), R(f"({inc})", sz), Kern(2), R("(", sz),
                  Frac(HB(sup(R(f"({ratio})", sz), R(M_, sz)), R(f" {M} 1", sz)),
                       R(str(denom), sz), sz=sz), R(")", sz))
    step1 = HB(sigma(floor_bare(fl_str, sz), sz), Kern(2), R("(", sz), per_term, R(")", sz))

    # distribute the sum linearly AND evaluate the constant sub-sum
    # (a constant summed ⌊.⌋+1 times) in one step
    sumA = HB(R(f"({v_sel})", sz), sigma(floor_bare(fl_str, sz), sz), sup(R(f"({ratio})", sz), R(M_, sz)))
    sumB = HB(R("(", sz), incfrac, R(")(", sz), sigma(floor_bare(fl_str, sz), sz),
              sup(R(f"({ratio})", sz), R(M_, sz)), Kern(3), R(f"{M}", sz), Kern(3),
              R("(", sz), floor_bare(fl_str, sz), R("+1))", sz))
    step2 = HB(sumA, Kern(4), R("+", sz), Kern(4), sumB)

    # collect the (ratio)^m coefficient AND apply the geometric series
    # formula in one step
    geo = Frac(HB(sup(R(f"({ratio})", sz), HB(floor_bare(fl_str, sz), R("+1", sz))), R(f" {M} 1", sz)),
               R(str(denom), sz), sz=sz)
    combFrac = Frac(R(str(combined_num), sz), R(str(denom), sz), sz=sz)
    step3 = HB(R("(", sz), combFrac, R(")(", sz), geo, R(")", sz),
              Kern(4), R(f"{M}", sz), Kern(4), R("(", sz), incfrac, R(")", sz),
              R("(", sz), floor_bare(fl_str, sz), R("+1)", sz))

    ch = Chain(first, [('=', step1), ('=', step2), ('=', step3)], sz=sz, rowgap=8)
    return ch


def even_odd_atom(func_sym, word, var, v0, v1, v_sel, ratio, inc, denom, is_even,
                   combined_num, m_reindex):
    """citation+parity-simplify and sum+geometric-formula for one parity."""
    cite = citation_atom(func_sym, word, var, v0, v1, v_sel, ratio, inc, denom, is_even)
    summ = sum_atom(func_sym, v_sel, ratio, inc, denom, is_even, combined_num, m_reindex)
    return VStack([(cite, 0), (summ, 14)])


def combine_atom(func_sym, ratio, inc, denom, num_even, num_odd):
    sz = SZ
    fl_e = floor_bare(N_, sz)
    fl_o = floor_bare(f"{N_}{M}1", sz)
    geo_e = Frac(HB(sup(R(f"({ratio})", sz), HB(fl_e, R("+1", sz))), R(f" {M} 1", sz)), R(str(denom), sz), sz=sz)
    geo_o = Frac(HB(sup(R(f"({ratio})", sz), HB(fl_o, R("+1", sz))), R(f" {M} 1", sz)), R(str(denom), sz), sz=sz)
    coefE = Frac(R(str(num_even), sz), R(str(denom), sz), sz=sz)
    coefO = Frac(R(str(num_odd), sz), R(str(denom), sz), sz=sz)
    incfrac = Frac(R(str(inc), sz), R(str(denom), sz), sz=sz)

    first = R(f"𝑆𝑚({func_sym},{N_})", sz)
    step1 = HB(R("(", sz), coefE, R(")(", sz), geo_e, R(")", sz), Kern(3), R("+", sz), Kern(3),
              R("(", sz), coefO, R(")(", sz), geo_o, R(")", sz), Kern(3), R(f"{M}", sz), Kern(3),
              R("(", sz), incfrac, R(")(", sz), fl_e, R("+1)", sz), Kern(3), R(f"{M}", sz), Kern(3),
              R("(", sz), incfrac, R(")(", sz), fl_o, R("+1)", sz))
    step2 = HB(R("(", sz), coefE, R(")(", sz), geo_e, R(")", sz), Kern(3), R("+", sz), Kern(3),
              R("(", sz), coefO, R(")(", sz), geo_o, R(")", sz), Kern(3), R(f"{M}", sz), Kern(3),
              R("(", sz), incfrac, R(")(", sz), R(f"{N_}+1)", sz))
    return Chain(first, [('=', step1), ('=', step2)], sz=sz, rowgap=8)


def full_piece(label, func_sym, v0, v1, ratio, inc, denom, num_even, num_odd):
    """even + odd + combine, all under ONE label with no dividers between
    them (2026-08-03, Sri: "get rid of the extra lines... if you have 2
    2b.i.0 there should be no lines in the middle") -- the exhibit tags
    its entire alpha/phi derivation with a single "2b.i.0"/"2b.ii.0" box,
    not one label per even/odd/combine sub-step; splitting those into
    separate pieces was what put a `lay_pieces` divider line between them.
    One piece = one label = no dividers, matching that exactly."""
    even = even_odd_atom(func_sym, "Evn", P_, v0, v1, v0, ratio, inc, denom, True, num_even, f"2{M_}")
    odd = even_odd_atom(func_sym, "Odd", Q_, v0, v1, v1, ratio, inc, denom, False, num_odd, f"2{M_}+1")
    comb = combine_atom(func_sym, ratio, inc, denom, num_even, num_odd)
    return (label, VStack([(even, 0), (odd, 14), (comb, 14)]), 8, 8)


pieces = []

# No separate "2b.0" definitions/geometric-formula preamble (removed
# 2026-08-03, Sri: "what is the extra thing on 4180?") -- Sm(alpha,n)
# is already defined in the printed problem statement on p419 itself
# ("Sm(alpha,n):=S(alpha,n):=sum alpha(k)"), and the exhibit doesn't show
# the geometric series formula as its own preliminary box either, just
# uses it directly inside the derivation -- restating both here was
# redundant scaffolding and the reason worksheet 4180 was nearly blank.

# alpha ("2b.i.0", matching the exhibit's own single folio-4190 label):
# v0=1,v1=54,inc=9,denom=62,ratio=63 -> even coef 71, odd coef 3357
pieces.append(full_piece("2b.i.0", A, 1, 54, 63, 9, 62, 71, 3357))

# phi ("2b.ii.0", matching the exhibit's own single folio-4191 label):
# v0=6,v1=8,inc=1,denom=62,ratio=63 -> even coef 373, odd coef 497
pieces.append(full_piece("2b.ii.0", PH, 6, 8, 63, 1, 62, 373, 497))

sheets = lay_pieces(pieces)
folios = write_sheets(4180, sheets, OUT_SHEETS)
print("2b work sheets:", folios)
