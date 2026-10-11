#!/usr/bin/env python3
"""3c: repeating/non-repeating decimal rational/irrational proofs.
b=9,c=5 (exam's global setup values, reused here since x/y are explicitly
DEFINED using them, unlike 1c which is a free-standing construction).

No solved exhibit covers 3c (styleguide sec.8 #8 / project memory); the
Rtl-predicate SYMBOL is confirmed from the exam's own p428/p430 gloss text,
but 3b's proof template (prime-divides-a-root contradiction) does NOT
apply here -- x/y are decimal-digit-defined, not roots, so this uses the
standard technique: rational <=> eventually-periodic decimal, cited as a
fact (no note PDF states it explicitly -- grepped, zero hits) rather than
a specific theorem number, same citation-level treatment 3a gives the
geometric series formula.
  x: constructive proof via the classic "multiply by 10^period, subtract"
     trick (100x - x kills the repeating part exactly).
  y: contrapositive on the same fact -- y's digit sequence has UNBOUNDED
     runs (n c's between the n-th and (n+1)-st d), which no finite period
     can produce, so y is not eventually periodic, hence not rational.

x := .(bc)-repeating = .(9)(5)-repeating. y's digit-position pattern (dd c
d cc d ccc d...) per the exam's own printed gloss ("for every n in N there
are n c's between the n-th d and the (n+1)-st d", 0-indexed n) -- position
of the n-th d (0-indexed) is the triangular number n(n+1)/2.

REBUILT (2026-08-02, Sri: "no words ... absolutely no words ... it should
just be numbers and equations EXACTLY LIKE THE SOLUTION EXAM"). This file
was the worst offender in the project: full English paragraphs for the BC/
RcS proofs AND a 6-line prose argument for y's irrationality. Rebuilt
throughout:
- The x digit-value conjecture ("9 if n even, 5 if n odd") is now ONE
  parity-selector formula, x_n = 9((1+(-1)^n)/2)+5((1+(-1)^(n+1))/2), the
  same unified-formula trick already used for 2a/2c instead of a worded
  case split -- no "if n even/odd" anywhere.
- y's irrationality argument is now a fully symbolic BarStack contradiction:
  Rtl(y) -> (cite: rational <=> eventually periodic) -> a bounded-gap
  fact about occurrences of digit d -> contradicts the already-proven
  p(n+1)-p(n)=n+1 (unbounded) -> struck-Rtl(y). Two standard facts are
  CITED (not re-derived from scratch), matching how 3a cites the geometric
  series formula and 1c(iii) cites the k-subset-count formula rather than
  proving them inline -- the citation itself is a bare implication arrow,
  no "so"/"since"/"because".
- "dig" (the k-th-decimal-digit function) and "gcd" both need Book-Antiqua
  routing like "prm" -- CambriaM's lowercase set is missing e,f,g,h,i,j,
  o,u,v,w,z, so "dig"/"gcd" can't be spelled in math-italic.

FONT CONSTRAINT: CambriaM.ttf's math-italic capitals are limited to
A,B,F,J,P,R,S; lowercase k,n,p,x,y (all used here) are present; digit/gcd
need Book Antiqua (see above). No exists-quantifier, double-arrow, or
infinity glyph in this font subset -- 'for some'/'->'(single arrow, IS in
the font)/'unbounded' as a defined predicate stand in, same substitutions
already used throughout 3b/1c. Proof-skeleton labels (SPf/BC/RcS/EPf/LS/
RS) are plain ASCII Book Antiqua, not math-italic.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import R, HB, Kern, Frac, sup, subs, strike, BarStack, cdots, Atom, fmt

OUT_PAGES = os.path.join(os.path.dirname(__file__), '..', 'pages')
M = "−"
N = "\U0001D45B"
X = "\U0001D465"
Y = "\U0001D466"
K = "\U0001D458"
RTL = "\U0001D445\U0001D461\U0001D459"  # 𝑅𝑡𝑙 - math-italic, matches p428/430
PSZ = 10.5


def bt(text, sz=PSZ):
    return R(text, sz, font='b')


def bbt(text, sz=PSZ):
    return R(text, sz, font='bb')


def fit_centered(text, x0, x1, y, max_sz=14.04, min_sz=6.0, inset=1.0):
    paren_w = R("(", max_sz).w
    ix0, ix1 = x0 + paren_w, x1
    avail = (ix1 - ix0) - 2 * inset
    sz = max_sz
    while sz > min_sz and R(text, sz).w > avail:
        sz -= 0.25
    a = R(text, sz)
    cx = ix0 + (ix1 - ix0 - a.w) / 2
    return a.emit(cx, y)


def rowtools(y0, x=90.0, rowgap=9.5, pad=2.5):
    y = [y0]
    prev_dp = [None]

    def emit_row(atom, xx=x):
        if prev_dp[0] is not None:
            y[0] += max(rowgap, prev_dp[0] + atom.ht + pad)
        out = atom.emit(xx, y[0])
        prev_dp[0] = atom.dp
        return out

    def get_y():
        return y[0]

    def set_y(v):
        y[0] = v

    return emit_row, get_y, set_y


def emit_rule_at(get_y, set_y, x, w, after_atom, rowgap=9.5, pad=2.5):
    """bar separator matching gen_3a.py's emit_rule -- adapted to this
    file's closure-based (get_y/set_y) row tracking instead of a module
    global, added 2026-08-03 (Sri: "make sure you have a conclusion line
    and have a LS = RS") so BC/RcS blocks here get the same
    premise-bar-derivation-bar-conclusion shape 3a already has. This
    file's `rowtools` emit_row is look-BEHIND (advances y on the NEXT
    call), so get_y() right after an emit_row call still sits at that
    row's own baseline -- must add the row's own depth+pad here or the
    rule draws straight through the text above it (confirmed by render
    on gen_2c.py's identical helper, same bug, same fix)."""
    yy = get_y() + after_atom.dp + pad
    out = [f"\\DLINE{{{x:.2f}}}{{{yy:.2f}}}{{{x + w:.2f}}}{{{yy:.2f}}}{{0.55}}"]
    set_y(yy + rowgap)
    return out


def parity(base_pow, sz=PSZ):
    """(1+(-1)^base_pow)/2 -- the even-selector; base_pow+1 gives odd."""
    return Frac(HB(R("1+", sz), sup(R(f"({M}1)", sz), R(base_pow, sz))), R("2", sz), sz=sz)


def x_closed_form(narg, sz=PSZ):
    return HB(subs(R(X, sz), R(narg, sz)), R(" = 9(", sz),
              parity(narg, sz), R(") + 5(", sz), parity(f"{narg}+1", sz), R(")", sz))


# ======================= 3c1: x := .(bc)-repeating (page 428/429) ========
lines428 = []

lines428 += fit_centered("(9)(5)", 437.23, 485.62, 170.30, max_sz=11.0)
lines428 += R(X, 14.04).emit(422.2, 264.29)

emit_row, get_y, set_y = rowtools(340.0, x=144.02)
lines428 += emit_row(HB(bbt("BC"), Kern(8), subs(R(X, PSZ), R("0", PSZ)), R("≔9,", PSZ), Kern(4),
                        subs(R(X, PSZ), R("1", PSZ)), R("≔5", PSZ)))
lines428 += emit_row(HB(bbt("RcS"), Kern(8), R(f"∀{N}∈ℕ", PSZ), Kern(3),
                        subs(R(X, PSZ), R(f"{N}+2", PSZ)), R("≔", PSZ), subs(R(X, PSZ), R(N, PSZ))))

with open(os.path.join(OUT_PAGES, 'answers428.tex'), 'w', encoding='utf-8') as f:
    f.write('%% ===== answers428.tex — generated by gen_3c.py =====\n')
    f.write('\n'.join(lines428) + '\n')
print(f"wrote pages/answers428.tex ({len(lines428)} lines)")

# ---- page 429: closed form for the digit definition + Rtl(x) proof ----
emit_row, get_y, set_y = rowtools(88.0, x=90.0)
lines429 = []
lines429 += emit_row(bt("(3c1) continued"), xx=72.02)
set_y(get_y() + 8)

lines429 += emit_row(bt("SPf"))
lines429 += emit_row(HB(R("𝑃(", PSZ), R(N, PSZ), R(") ≔ (", PSZ), x_closed_form(N), R(")", PSZ)))
set_y(get_y() + 3)
lines429 += emit_row(bbt("BC"))
lines429 += emit_row(HB(bt("LS"), Kern(6), R("=", PSZ), Kern(4), subs(R(X, PSZ), R("0", PSZ)), R(" = 9", PSZ)))
lines429 += emit_row(HB(bt("RS"), Kern(6), R("=", PSZ), Kern(4), R("9(", PSZ), parity("0"), R(") + 5(", PSZ), parity("1"), R(")", PSZ),
                        Kern(4), R("= 9(1)+5(0) = 9", PSZ)))
lines429 += emit_row(HB(bt("LS"), R(" = ", PSZ, font='b'), bt("RS")))
lines429 += emit_row(R("𝑃(0)", PSZ))
set_y(get_y() + 3)
lines429 += emit_row(HB(bt("LS"), Kern(6), R("=", PSZ), Kern(4), subs(R(X, PSZ), R("1", PSZ)), R(" = 5", PSZ)))
lines429 += emit_row(HB(bt("RS"), Kern(6), R("=", PSZ), Kern(4), R("9(", PSZ), parity("1"), R(") + 5(", PSZ), parity("2"), R(")", PSZ),
                        Kern(4), R("= 9(0)+5(1) = 5", PSZ)))
lines429 += emit_row(HB(bt("LS"), R(" = ", PSZ, font='b'), bt("RS")))
lines429 += emit_row(R("𝑃(1)", PSZ))
set_y(get_y() + 3)
lines429 += emit_row(bbt("RcS"))
hyp3c = HB(R("𝑃(0) 𝑃(1) ", PSZ), cdots(PSZ), Kern(2), R(f" 𝑃({N})", PSZ))
lines429 += emit_row(hyp3c)
lines429 += emit_rule_at(get_y, set_y, 90.0, 160, hyp3c)
lines429 += emit_row(bt("LS"))
lines429 += emit_row(HB(R("=", PSZ), Kern(4), subs(R(X, PSZ), R(f"{N}+2", PSZ))))
lines429 += emit_row(HB(R("=", PSZ), Kern(4), subs(R(X, PSZ), R(N, PSZ))))
lines429 += emit_row(HB(R("=", PSZ), Kern(4), R("9(", PSZ), parity(N), R(") + 5(", PSZ), parity(f"{N}+1"), R(")", PSZ)))
set_y(get_y() + 3)
lines429 += emit_row(HB(sup(R(f"({M}1)", PSZ), R(f"{N}+2", PSZ)), R(" = ", PSZ),
                        sup(R(f"({M}1)", PSZ), R(N, PSZ)), R("(", PSZ), sup(R(f"({M}1)", PSZ), R("2", PSZ)), R(") = ", PSZ),
                        sup(R(f"({M}1)", PSZ), R(N, PSZ))))
set_y(get_y() + 3)
lines429 += emit_row(HB(R("=", PSZ), Kern(4), R("9(", PSZ), parity(f"{N}+2"), R(") + 5(", PSZ), parity(f"{N}+3"), R(")", PSZ)))
rs3c = HB(R("=", PSZ), Kern(4), bt("RS"))
lines429 += emit_row(rs3c)
lines429 += emit_rule_at(get_y, set_y, 90.0, 80, rs3c)
lines429 += emit_row(R(f"𝑃({N}+2)", PSZ))
set_y(get_y() + 3)
lines429 += emit_row(R(f"𝑃(0)∧𝑃(1)∧∀{N}∈ℕ(𝑃({N})→𝑃({N}+2))   →   ∀{N}∈ℕ(𝑃({N}))", PSZ))
lines429 += emit_row(bt("EPf"))
set_y(get_y() + 14)

# Rtl(x): standard "multiply by 10^period, subtract" construction
lines429 += emit_row(bt("SPf"))
lines429 += emit_row(R("𝑥 = .959595...", PSZ))
lines429 += emit_row(R("(100)𝑥 = 95.959595...", PSZ))
lines429 += emit_row(R("(100)𝑥 − 𝑥 = 95", PSZ))
lines429 += emit_row(R("(99)𝑥 = 95", PSZ))
lines429 += emit_row(HB(R("𝑥", PSZ), Kern(4), R("=", PSZ), Kern(4), Frac(R("95", PSZ), R("99", PSZ), sz=PSZ)))
lines429 += emit_row(HB(R("95,99∈ℕ, 99≠0, ", PSZ), bt("gcd"), R("(95,99)=1", PSZ)))
lines429 += emit_row(R(f"{RTL}({X})", PSZ))
lines429 += emit_row(bt("EPf"))

with open(os.path.join(OUT_PAGES, 'answers429.tex'), 'w', encoding='utf-8') as f:
    f.write('%% ===== answers429.tex — generated by gen_3c.py =====\n')
    f.write('\n'.join(lines429) + '\n')
print(f"wrote pages/answers429.tex ({len(lines429)} lines), final y={get_y():.1f}")

# ================= 3c2: y := .ddcdccdccc...d (page 430/431) ==============
lines430 = []

xg, yg = R(X, 14.04), R(Y, 14.04)
mx0, my0 = 421.99, 265.97
mx1 = mx0 + max(xg.w, yg.w) + 1.5
mtop = my0 - max(xg.ht, yg.ht) - 1.3
mbot = my0 + max(xg.dp, yg.dp) + 1.3
lines430.append(f"\\fill[white] ($(current page.north west)+({mx0 - 1.3:.2f}bp,-{mtop:.2f}bp)$) "
                 f"rectangle ($(current page.north west)+({mx1:.2f}bp,-{mbot:.2f}bp)$);")
lines430 += R(Y, 14.04).emit(422.2, 265.97)

lines430 += R("0.77575575557…", 14.04).emit(375.0, 135.50)

emit_row, get_y, set_y = rowtools(320.0, x=144.02)
lines430 += emit_row(HB(bbt("BC"), Kern(8), R("𝑝(0)≔0", PSZ)))
lines430 += emit_row(HB(bbt("RcS"), Kern(8), R(f"∀{N}∈ℕ", PSZ), Kern(3),
                        R(f"𝑝({N}+1)≔𝑝({N})+({N}+1)", PSZ)))

with open(os.path.join(OUT_PAGES, 'answers430.tex'), 'w', encoding='utf-8') as f:
    f.write('%% ===== answers430.tex — generated by gen_3c.py =====\n')
    f.write('\n'.join(lines430) + '\n')
print(f"wrote pages/answers430.tex ({len(lines430)} lines)")

# ---- page 431: induction proof p(n)=n(n+1)/2 + irrationality proof ----
emit_row, get_y, set_y = rowtools(88.0, x=90.0)
lines431 = []
lines431 += emit_row(bt("(3c2) continued"), xx=72.02)
set_y(get_y() + 8)

lines431 += emit_row(bt("SPf"))
lines431 += emit_row(HB(R("𝑃(", PSZ), R(N, PSZ), R(") ≔ (𝑝(", PSZ), R(N, PSZ), R(") = (", PSZ),
                        Frac(HB(R(N, PSZ), R(f"({N}+1)", PSZ)), R("2", PSZ), sz=PSZ), R(")", PSZ), R(")", PSZ)))
set_y(get_y() + 3)
lines431 += emit_row(bbt("BC"))
lines431 += emit_row(HB(bt("LS"), Kern(6), R("=", PSZ), Kern(4), R("𝑝(0) = 0", PSZ)))
lines431 += emit_row(HB(bt("RS"), Kern(6), R("=", PSZ), Kern(4), R("(0)(1)÷2 = 0", PSZ)))
lines431 += emit_row(HB(bt("LS"), R(" = ", PSZ, font='b'), bt("RS")))
lines431 += emit_row(R("𝑃(0)", PSZ))
set_y(get_y() + 3)
lines431 += emit_row(bbt("RcS"))
lines431 += emit_row(HB(R("𝑃(0) 𝑃(1) ", PSZ), cdots(PSZ), Kern(2), R(f" 𝑃({N})", PSZ)))
lines431 += emit_row(bt("LS"))
lines431 += emit_row(HB(R("=", PSZ), Kern(4), R(f"𝑝({N}+1)", PSZ)))
lines431 += emit_row(HB(R("=", PSZ), Kern(4), R(f"𝑝({N})+({N}+1)", PSZ)))
lines431 += emit_row(HB(R("=", PSZ), Kern(4),
                        Frac(HB(R(N, PSZ), R(f"({N}+1)", PSZ)), R("2", PSZ), sz=PSZ), R(f"+({N}+1)", PSZ)))
lines431 += emit_row(HB(R("=", PSZ), Kern(4),
                        Frac(HB(R(N, PSZ), R(f"({N}+1)+2({N}+1)", PSZ)), R("2", PSZ), sz=PSZ)))
lines431 += emit_row(HB(R("=", PSZ), Kern(4),
                        Frac(HB(R(f"({N}+1)", PSZ), R(f"({N}+2)", PSZ)), R("2", PSZ), sz=PSZ)))
lines431 += emit_row(HB(R("=", PSZ), Kern(4), bt("RS")))
lines431 += emit_row(R(f"𝑃({N}+1)", PSZ))
set_y(get_y() + 3)
lines431 += emit_row(R(f"𝑃(0) ∧ ∀{N}∈ℕ(𝑃({N})→𝑃({N}+1))   →   ∀{N}∈ℕ(𝑃({N}))", PSZ))
lines431 += emit_row(bt("EPf"))
set_y(get_y() + 14)

# y is irrational: contrapositive on rational <=> eventually-periodic
# decimal, fully symbolic BarStack contradiction. "dig(k)" = the k-th
# decimal digit of y (0-indexed), a defined function label like gcd/prm.
rows_irr = [
    R(f"{RTL}(𝑦)", PSZ),
    HB(bt("for some "), R("𝑚∈ℕ (𝑚>0)", PSZ), Kern(6), bt("for some "),
       subs(R("𝑙", PSZ), R("0", PSZ)), R("∈ℕ", PSZ)),
    HB(R("∀𝑘≥", PSZ), subs(R("𝑙", PSZ), R("0", PSZ)), R(" (", PSZ),
       bt("dig"), R("(𝑘)=", PSZ), bt("dig"), R("(𝑘+𝑚))", PSZ)),
    HB(bt("for some "), R("𝐵∈ℕ  ∀", PSZ), R(f"{N}∈ℕ (𝑝({N}+1){M}𝑝({N})≤𝐵)", PSZ)),
    R(f"𝑝({N}+1){M}𝑝({N}) = {N}+1", PSZ),
    HB(bt("for some "), R("𝐵∈ℕ  ∀", PSZ), R(f"{N}∈ℕ ({N}+1≤𝐵)", PSZ)),
    R("⊥", PSZ),
    HB(R("¬", PSZ), R(f"{RTL}(𝑦)", PSZ)),
    strike(R(f"{RTL}(𝑦)", PSZ)),
]
emit_row, get_y, set_y = rowtools(get_y(), x=90.0)
lines431 += emit_row(bt("SPf"))
irr_stack = BarStack(rows_irr)
lines431 += irr_stack.emit(90.0, get_y() + irr_stack.ht)
set_y(get_y() + irr_stack.ht + irr_stack.dp + 3)
lines431 += emit_row(bt("EPf"))

with open(os.path.join(OUT_PAGES, 'answers431.tex'), 'w', encoding='utf-8') as f:
    f.write('%% ===== answers431.tex — generated by gen_3c.py =====\n')
    f.write('\n'.join(lines431) + '\n')
print(f"wrote pages/answers431.tex ({len(lines431)} lines), final y={get_y():.1f}")
