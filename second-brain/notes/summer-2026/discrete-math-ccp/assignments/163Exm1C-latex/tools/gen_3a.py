#!/usr/bin/env python3
"""Generate answers316.tex + work sheet 3160 for problem 3a.
s=2, b=0, b+s=2. The (v)/(vi) identity (all four coefficients equal, and
that fact holds for ANY s,b -- symmetry of C(n,k) + multinomial-with-2-
parts-is-binomial) is a general algebraic fact, not data-dependent, so the
vi.0-3 pieces are legitimately the same symbolic content SOL-2024 used."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import R, HB, Kern, Chevrons, assign, ditto, binom, mltnom, Chain, BarStack, Frac, sup, subs, fmt
from expr import B_, SS, X_, Y_, N_, K_, MINUS, BnmlCfn, MltnmlCfn
from stack import VStack, Barred
from pieces import lay_pieces, write_sheets

SZ = 11.04
OUT_PAGES = os.path.join(os.path.dirname(__file__), '..', 'pages')
OUT_SHEETS = os.path.join(os.path.dirname(__file__), '..', 'sheets')

s_val, b_val, n_val = 2, 0, 2   # n = b+s

A_ = "\U0001D44E"   # generic dummy 'a' in the abstract BnmlCfn(a^(n-k)b^k,(a+b)^n) fact
# SOL-2024 reuses B_ as BOTH the problem's data value b AND the generic
# formula's second base (⟨...,b<-y⟩) -- same overload, kept for fidelity.
X1 = X_ + "₁"; X2 = X_ + "₂"; N1 = N_ + "₁"; N2 = N_ + "₂"

# ---------------------------------------------------------------- preliminary "3a": derive n=b+s
prelim = BarStack([
    R(f"{SS}={s_val}  {B_}={b_val}  {K_}={SS}  {N_}{MINUS}{K_}={B_}", SZ),
    R(f"{N_}{MINUS}{SS}={B_}", SZ),
    R(f"{N_}={B_}+{SS}", SZ),
    R(f"{N_}={b_val}+{s_val}", SZ),
    R(f"{N_}={n_val}", SZ),
])

def xp(base, exp, sz=SZ):
    """base^exp as a real raised superscript (text mode has no '^')."""
    b = R(base, sz) if isinstance(base, str) else base
    return sup(b, R(exp, sz * 0.72))


def sb(base, script, sz=SZ):
    b = R(base, sz) if isinstance(base, str) else base
    return subs(b, R(script, sz * 0.72))


GEN_BNML = HB(R(f"{BnmlCfn}(", SZ), xp(A_, f"{N_}{MINUS}{K_}"), xp(B_, K_),
              R(",", SZ), xp(f"({A_}+{B_})", N_), R(")", SZ))

_x1, _x2 = sb(X_, "1"), sb(X_, "2")
GEN_MLTNM = HB(R(f"{MltnmlCfn}((", SZ), xp(_x1, N1), R(")(", SZ), xp(_x2, N2), R("),(", SZ),
               _x1, R("+", SZ), _x2, xp(")", N_))


def bnml_piece(xexp_sym, yexp_sym, k_num):
    first = HB(R(f"{BnmlCfn}(", SZ), xp(X_, xexp_sym), R(" ", SZ), xp(Y_, yexp_sym), R(",", SZ),
               xp(f"({X_}+{Y_})", f"{xexp_sym}+{yexp_sym}"), R(")", SZ))
    step1 = HB(R(f"{BnmlCfn}(", SZ), xp(X_, f"{n_val}{MINUS}{k_num}"), R(" ", SZ), xp(Y_, str(k_num)),
               R(",", SZ), xp(f"({X_}+{Y_})", str(n_val)), R(")", SZ))
    step2 = HB(R("(", SZ), GEN_BNML, R(")", SZ),
               Chevrons([assign(R(N_, SZ), R(str(n_val), SZ)), assign(R(K_, SZ), R(str(k_num), SZ)),
                         assign(R(A_, SZ), R(X_, SZ)), assign(R(B_, SZ), R(Y_, SZ))]))
    step3 = HB(binom(N_, K_, sz=SZ),
               Chevrons([assign(R(N_, SZ), R(str(n_val), SZ)), assign(R(K_, SZ), R(str(k_num), SZ))]))
    step4 = binom(str(n_val), str(k_num), sz=SZ)
    return Chain(first, [step1, step2, step3, step4], sz=SZ)


def mltnm_piece(xexp_sym, yexp_sym, n1_num, n2_num):
    first = HB(R(f"{MltnmlCfn}(", SZ), xp(X_, xexp_sym), R(" ", SZ), xp(Y_, yexp_sym), R(",", SZ),
               xp(f"({X_}+{Y_})", f"{xexp_sym}+{yexp_sym}"), R(")", SZ))
    step1 = HB(R("(", SZ), GEN_MLTNM, R(")", SZ),
               Chevrons([assign(R(N_, SZ), R(str(n_val), SZ)),
                         assign(R(N1, SZ), R(str(n1_num), SZ)), assign(R(N2, SZ), R(str(n2_num), SZ)),
                         assign(sb(X_, "1"), R(X_, SZ)), assign(sb(X_, "2"), R(Y_, SZ))]))
    step2 = HB(mltnom(N_, [N1, N2], sz=SZ), ditto(SZ))
    step3 = mltnom(str(n_val), [str(n1_num), str(n2_num)], sz=SZ)
    return Chain(first, [step1, step2, step3], sz=SZ)


def fr(num, den, sz=SZ):
    return Frac(R(num, sz), R(den, sz), sz=sz)


piece_i = bnml_piece(B_, SS, s_val)      # BnmlCfn(x^b y^s,...) -> k=s
piece_ii = bnml_piece(SS, B_, b_val)     # BnmlCfn(x^s y^b,...) -> k=b
piece_iii = mltnm_piece(B_, SS, b_val, s_val)
piece_iv = mltnm_piece(SS, B_, s_val, b_val)

# ---------------------------------------------------------------- v.0-3: numeric equivalence chain
v0 = Chain(binom(str(n_val), str(s_val), sz=SZ),
           [fr(f"({n_val}!)", f"(({s_val}!)(({n_val}{MINUS}{s_val})!))"),
            fr(f"({n_val}!)", f"(({s_val}!)({b_val}!))")], sz=SZ)
v1 = Chain(binom(str(n_val), str(b_val), sz=SZ),
           [fr(f"({n_val}!)", f"(({b_val}!)(({n_val}{MINUS}{b_val})!))"),
            fr(f"({n_val}!)", f"(({b_val}!)({s_val}!))")], sz=SZ)
v2 = Chain(mltnom(str(n_val), [str(b_val), str(s_val)], sz=SZ),
           [mltnom(str(n_val), [str(s_val), str(b_val)], sz=SZ),
            fr(f"({n_val}!)", f"(({b_val}!)({s_val}!))")], sz=SZ)
v3 = Chain(binom(str(n_val), str(s_val), sz=SZ),
           [binom(str(n_val), str(b_val), sz=SZ),
            mltnom(str(n_val), [str(b_val), str(s_val)], sz=SZ),
            mltnom(str(n_val), [str(s_val), str(b_val)], sz=SZ)], sz=SZ)

# ---------------------------------------------------------------- vi.0-3: SYMBOLIC (general s,b) proof
vi0 = Chain(binom(f"{B_}+{SS}", B_, sz=SZ),
            [fr(f"({B_}+{SS})!", f"(({B_}!)((({B_}+{SS})){MINUS}{B_})!)"),
             fr(f"({B_}+{SS})!", f"(({B_}!)({SS}!))")], sz=SZ)
vi1 = Chain(binom(f"{B_}+{SS}", SS, sz=SZ),
            [fr(f"({B_}+{SS})!", f"(({SS}!)((({B_}+{SS})){MINUS}{SS})!)"),
             fr(f"({B_}+{SS})!", f"(({SS}!)({B_}!))")], sz=SZ)
vi2 = Chain(mltnom(f"{B_}+{SS}", [B_, SS], sz=SZ),
            [mltnom(f"{B_}+{SS}", [SS, B_], sz=SZ),
             fr(f"({B_}+{SS})!", f"(({B_}!)({SS}!))")], sz=SZ)
vi3 = Chain(binom(f"{B_}+{SS}", SS, sz=SZ),
            [binom(f"{B_}+{SS}", B_, sz=SZ),
             mltnom(f"{B_}+{SS}", [B_, SS], sz=SZ),
             mltnom(f"{B_}+{SS}", [SS, B_], sz=SZ)], sz=SZ)

pieces_all = [
    ("3a", prelim, 4, 12),
    ("3a.i", piece_i, 4, 10), ("3a.ii", piece_ii, 8, 10),
    ("3a.iii", piece_iii, 8, 10), ("3a.iv", piece_iv, 8, 10),
    ("3a.v.0", v0, 8, 10), ("3a.v.1", v1, 8, 10),
    ("3a.v.2", v2, 8, 10), ("3a.v.3", v3, 8, 10),
    ("3a.vi.0", vi0, 8, 10), ("3a.vi.1", vi1, 8, 10),
    ("3a.vi.2", vi2, 8, 10), ("3a.vi.3", vi3, 8, 8),
]
sheets = lay_pieces(pieces_all)
folios = write_sheets(3160, sheets, OUT_SHEETS)
print("3a work sheets used:", folios)

# ---------------------------------------------------------------- printed page 316
def centered(text, sz, x0, x1, y, inset=3.2):
    """emit text baseline-centered in the printed blank [x0,x1] at baseline y,
    shrinking the font until it fits if needed. inset accounts for the
    printed parens' own ink eating into the nominal gap on both sides."""
    x0, x1 = x0 + inset, x1 - inset
    while R(text, sz).w > (x1 - x0 - 0.5) and sz > 4.0:
        sz -= 0.5
    w = R(text, sz).w
    return R(text, sz).emit(x0 + (x1 - x0 - w) / 2, y)


lines316 = []
lines316 += R(str(s_val), SZ).emit(200, 135.38)
lines316 += R(str(b_val), SZ).emit(273, 135.38)
lines316 += R(str(n_val), SZ).emit(370, 135.38)
# The symbolic "b+s"/"s+b" exponent fill is 3 glyphs, not 1 -- the default
# inset=3.2 (tuned for single-numeral fills) starves it down to the sz>4.0
# floor, rendering as an illegible speck. SOL-2024's own fill runs nearly
# edge-to-edge in that bracket (verified by direct pixel comparison against
# the solved sample); inset=0.2 lets the shrink-loop land near sz~7, matching.
# (i): gaps at y=205.70, sz 9.96
lines316 += centered(f"{B_}+{SS}", 9.96, 219.65, 232.85, 205.70, inset=0.2)
lines316 += centered(str(b_val), 9.96, 341.35, 354.55, 205.70)
lines316 += centered(str(s_val), 9.96, 367.87, 381.07, 205.70)
lines316 += centered(str(n_val), 9.96, 435.43, 448.66, 205.70)
lines316 += binom(str(n_val), str(s_val), sz=SZ).emit(490, 214)
# (ii): gaps at y=296.93, sz 9.96
lines316 += centered(f"{SS}+{B_}", 9.96, 219.65, 232.85, 296.93, inset=0.2)
lines316 += centered(str(s_val), 9.96, 341.35, 354.55, 296.93)
lines316 += centered(str(b_val), 9.96, 367.87, 381.07, 296.93)
lines316 += centered(str(n_val), 9.96, 435.43, 448.66, 296.93)
lines316 += binom(str(n_val), str(b_val), sz=SZ).emit(490, 305.5)
# (iii): gaps at y=386.45, sz 9
lines316 += centered(f"{B_}+{SS}", 9, 220.49, 232.49, 386.45, inset=0.2)
lines316 += centered(str(b_val), 9, 344.71, 356.71, 386.45)
lines316 += centered(str(s_val), 9, 368.95, 380.95, 386.45)
lines316 += centered(str(n_val), 9, 431.11, 443.14, 386.45)
lines316 += mltnom(str(n_val), [str(b_val), str(s_val)], sz=SZ).emit(470, 394)
# (iv): gaps at y=473.71, sz 9
lines316 += centered(f"{SS}+{B_}", 9, 220.49, 232.49, 473.71, inset=0.2)
lines316 += centered(str(s_val), 9, 344.71, 356.71, 473.71)
lines316 += centered(str(b_val), 9, 368.95, 380.95, 473.71)
lines316 += centered(str(n_val), 9, 431.11, 443.14, 473.71)
lines316 += mltnom(str(n_val), [str(s_val), str(b_val)], sz=SZ).emit(470, 481)
# (v): circle Y and Pf ; (vi): circle N and Pf
lines316.append(f'\\CIRC{{402}}{{586}}{{9}}{{9}}')
lines316.append(f'\\CIRC{{478}}{{586}}{{15}}{{9}}')
lines316.append(f'\\CIRC{{438}}{{696.4}}{{9}}{{9}}')
lines316.append(f'\\CIRC{{478}}{{696.4}}{{15}}{{9}}')
with open(os.path.join(OUT_PAGES, 'answers316.tex'), 'w') as f:
    f.write('%% ===== answers316.tex — generated by gen_3a.py =====\n')
    f.write('\n'.join(lines316) + '\n')
print(f"wrote pages/answers316.tex ({len(lines316)} lines)")
