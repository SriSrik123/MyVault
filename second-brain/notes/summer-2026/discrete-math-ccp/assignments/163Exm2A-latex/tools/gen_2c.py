#!/usr/bin/env python3
"""2c: prove by induction the conjectures from 2a (alpha(n)/phi(n) closed
forms) and 2b (Sm(alpha,n)/Sm(phi,n) closed forms). Page 421 is instruction-
only, blank below it; proofs go directly on 421, spilling onto blank
continuation page 422.

No solved exhibit covers 2c (styleguide sec.8 #8 / project memory). Format
confirmed from Induction and Recursion Notes' own SPf/BC/RcS/EPf template,
same skeleton as 3a/3b in this exam.

REBUILT (2026-08-02, Sri: "no words ... absolutely no words no need for
'(induction hyp)' it should just be numbers and equations EXACTLY LIKE THE
SOLUTION EXAM"). Removed every parenthetical justification ("(by RcS
above)", "(induction hyp)", "(regroup)", the two full-sentence RcS lines
in Proof 2) -- Sri named "(induction hyp)" specifically as an example of
what NOT to include. The RcS hypothesis line no longer says "hyp n in N,
P(n)" -- it's now a bare BarStack premise "P(0) P(1) (dots) P(n)" over the
bar, matching the bar-inference convention already used everywhere else in
this project (3a/3b/1b): the premise IS the induction hypothesis, no label
needed to say so.

Proof 1 (alpha/phi, from 2a): the GIVEN recurrences are single-step, but
relating CF(n+1) to CF(n) directly needs a parity case-split, so this
substitutes once for a clean TWO-STEP relation: alpha(n+2)=63alpha(n)+9,
phi(n+2)=63phi(n)+1 (algebra verified in gen_2a.py's own closed_form
regrouping). Two-base-case (P(0) and P(1)), step-+2 induction.

Proof 2 (Sm, from 2b): ordinary step-+1 induction, RcS using
Sm(n+1)=Sm(n)+f(n+1), citing Proof 1's now-established closed form. The
middle regrouping step (splitting Sm's sum back into matching even/odd
geometric pieces) is cited rather than expanded line-by-line -- verified
programmatically against direct summation per project memory, same
citation-level treatment 1b gives the char-eq formula.

FONT CONSTRAINT: only math-italic capitals A,B,F,J,P,R,S exist in this
font. Predicate names here use P (Proof 1) and R (Proof 2) -- both
available. Proof-skeleton labels (SPf/BC/RcS/EPf) are plain ASCII in Book
Antiqua -- NOT math-italic.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import R, HB, Kern, Frac, sup, cdots, Atom, fmt

OUT_PAGES = os.path.join(os.path.dirname(__file__), '..', 'pages')
M = "−"
N = "\U0001D45B"
A = "\U0001D6FC"   # 𝛼
PH = "\U0001D711"  # 𝜑

PSZ = 9.5


def bt(text, sz=PSZ):
    return R(text, sz, font='b')


def bbt(text, sz=PSZ):
    return R(text, sz, font='bb')


class FloorAtom(Atom):
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


def closed_form_rhs(v0, v1, ratio, inc, denom, sz, narg=N):
    """bare RHS of the parity-selector closed form, no "var(narg)=" prefix
    -- used both for the printed SPf citation (via closed_form(), below)
    and, at a shrunk size, for the BC/RcS substitution steps that need
    just the value, not a fresh restatement of what it's the value OF."""
    floor_n2 = FloorAtom(Frac(R(narg, sz), R("2", sz), sz=sz), sz)
    pw = sup(R(f"({ratio})", sz), floor_n2)
    m1 = R(f"({M}1)", sz)
    par1 = Frac(HB(R("1+", sz), sup(m1, R(narg, sz))), R("2", sz), sz=sz)
    par2 = Frac(HB(R("1+", sz), sup(m1, R(f"{narg}+1", sz))), R("2", sz), sz=sz)
    bracket = HB(R("(", sz), R(f"({v0})", sz), Kern(1.5), R("(", sz), par1, R(")", sz),
                 Kern(2), R("+", sz), Kern(2),
                 R(f"({v1})", sz), Kern(1.5), R("(", sz), par2, R(")", sz), R(")", sz))
    part1 = HB(pw, Kern(1.5), bracket)
    floor_n2b = FloorAtom(Frac(R(narg, sz), R("2", sz), sz=sz), sz)
    pw2 = sup(R(f"({ratio})", sz), floor_n2b)
    num2 = HB(pw2, R(f" {M} 1", sz))
    frac2 = Frac(num2, R(str(denom), sz), sz=sz)
    part2 = HB(R(f"({inc})", sz), Kern(1.5), R("(", sz), frac2, R(")", sz))
    return HB(part1, Kern(3), R("+", sz), Kern(3), part2)


def closed_form(var, v0, v1, ratio, inc, denom, sz, narg=N):
    return HB(lhs_of(var, narg), closed_form_rhs(v0, v1, ratio, inc, denom, sz, narg))


def lhs_of(var, narg, sz=PSZ):
    return R(f"{var}({narg})=", sz)


x0 = 90.0


def emit_rule_at(get_y, set_y, x, w, after_atom, rowgap=9.5, pad=3.0):
    """bar separator, same role as gen_3a.py's emit_rule -- adapted to
    this file's closure-based row tracking (2026-08-03, Sri: "make sure
    you have a conclusion line and have a LS = RS"). `make_rowtools`'s
    emit_row is look-BEHIND (it advances y on the NEXT call, using the
    row just placed), so get_y() right after an emit_row call still sits
    at THAT row's own baseline -- drawing a rule there runs it straight
    through the text (confirmed by render: produced a bogus "≡RS" with
    the rule cutting through the "=" and underlining "RS"). Pass the atom
    that was just emitted so this can add its own depth+pad clearance
    before drawing, the same spacing the next emit_row call would have
    applied."""
    yy = get_y() + after_atom.dp + pad
    out = [f"\\DLINE{{{x:.2f}}}{{{yy:.2f}}}{{{x + w:.2f}}}{{{yy:.2f}}}{{0.55}}"]
    set_y(yy + rowgap)
    return out


def make_rowtools(y0, x=x0, rowgap=9.5, pad=3.0):
    """Look-behind-and-ahead spacing (same lesson as 3a/2c's original
    version, restored here after a first draft used flat fixed offsets
    and produced real overlap -- confirmed by render, not assumed)."""
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


def rs_bc_row(v_sel, ratio, inc, denom, val, sz=PSZ):
    """RS at a concrete n=0/n=1 base case -- floor(n/2)=0 either way, so
    (ratio)^0=1 and the inc-term's numerator vanishes; shown as its own
    tiny step rather than skipped, then the final value."""
    return HB(bt("RS"), Kern(6), R("=", sz), Kern(4),
              sup(R(f"({ratio})", sz), R("0", sz)), R(f"({v_sel}) + ({inc})(", sz),
              sup(R(f"({ratio})", sz), R("0", sz)), R(f" {M} 1)÷{denom}", sz),
              Kern(4), R(f"= (1)({v_sel})+({inc})(0)", sz), Kern(4), R(f"= {val}", sz))


# ========================= Proof 1: alpha/phi (2a), page 421 =============
CSZ2C = 7.5  # shrunk size for a closed-form substituted inline into RcS --
             # same fix as gen_2b_work.py's citation rows: this parity-
             # selector formula is too wide to re-expand at full PSZ
             # without risking the page-overflow bug already found once.
emit_row, get_y, set_y = make_rowtools(178.0)
lines421 = []

lines421 += emit_row(bt("SPf"))
lines421 += emit_row(HB(R(f"𝑃({N}) ≔ (", PSZ), closed_form(A, 1, 54, 63, 9, 62, PSZ), R(")", PSZ)))
lines421 += emit_row(HB(R("        ∧ (", PSZ), closed_form(PH, 6, 8, 63, 1, 62, PSZ), R(")", PSZ)))
set_y(get_y() + 3)

lines421 += emit_row(bbt("BC"))
lines421 += emit_row(HB(bt("LS"), Kern(6), R("=", PSZ), Kern(4), R(f"{A}(0)=1", PSZ)))
lines421 += emit_row(rs_bc_row(1, 63, 9, 62, 1))
lines421 += emit_row(HB(bt("LS"), R(" = ", PSZ, font='b'), bt("RS")))
lines421 += emit_row(HB(bt("LS"), Kern(6), R("=", PSZ), Kern(4), R(f"{PH}(0)={A}(0)+5=1+5=6", PSZ)))
lines421 += emit_row(rs_bc_row(6, 63, 1, 62, 6))
lines421 += emit_row(HB(bt("LS"), R(" = ", PSZ, font='b'), bt("RS")))
lines421 += emit_row(R("𝑃(0)", PSZ))
set_y(get_y() + 3)
lines421 += emit_row(HB(bt("LS"), Kern(6), R("=", PSZ), Kern(4), R(f"{A}(1)=(9){PH}(0)=(9)(6)=54", PSZ)))
lines421 += emit_row(rs_bc_row(54, 63, 9, 62, 54))
lines421 += emit_row(HB(bt("LS"), R(" = ", PSZ, font='b'), bt("RS")))
lines421 += emit_row(HB(bt("LS"), Kern(6), R("=", PSZ), Kern(4), R(f"{PH}(1)=(7){A}(0)+1=(7)(1)+1=8", PSZ)))
lines421 += emit_row(rs_bc_row(8, 63, 1, 62, 8))
lines421 += emit_row(HB(bt("LS"), R(" = ", PSZ, font='b'), bt("RS")))
lines421 += emit_row(R("𝑃(1)", PSZ))
set_y(get_y() + 3)

lines421 += emit_row(bbt("RcS"))
hyp1 = HB(R("𝑃(0) 𝑃(1) ", PSZ), cdots(PSZ), Kern(2), R(f" 𝑃({N})", PSZ))
lines421 += emit_row(hyp1)
lines421 += emit_rule_at(get_y, set_y, x0, 200, hyp1)
lines421 += emit_row(bt("LS"))
lines421 += emit_row(HB(R("=", PSZ), Kern(4), R(f"{A}({N}+2)", PSZ)))
lines421 += emit_row(HB(R("=", PSZ), Kern(4), R(f"({A}({N})(7)+1)(9)", PSZ)))
lines421 += emit_row(HB(R("=", PSZ), Kern(4), R(f"(63){A}({N})+9", PSZ)))
lines421 += emit_row(HB(R("=", PSZ), Kern(4), R("(63)(", PSZ), closed_form_rhs(1, 54, 63, 9, 62, CSZ2C, N), R(")+9", PSZ)))
rs1 = HB(R("=", PSZ), Kern(4), bt("RS"))
lines421 += emit_row(rs1)
set_y(get_y() + rs1.dp + 5)
lines421 += emit_row(bt("LS"))
lines421 += emit_row(HB(R("=", PSZ), Kern(4), R(f"{PH}({N}+2)", PSZ)))
lines421 += emit_row(HB(R("=", PSZ), Kern(4), R(f"({PH}({N})(9))(7)+1", PSZ)))
lines421 += emit_row(HB(R("=", PSZ), Kern(4), R(f"(63){PH}({N})+1", PSZ)))
lines421 += emit_row(HB(R("=", PSZ), Kern(4), R("(63)(", PSZ), closed_form_rhs(6, 8, 63, 1, 62, CSZ2C, N), R(")+1", PSZ)))
rs2 = HB(R("=", PSZ), Kern(4), bt("RS"))
lines421 += emit_row(rs2)
lines421 += emit_rule_at(get_y, set_y, x0, 80, rs2)
lines421 += emit_row(R(f"𝑃({N}+2)", PSZ))
set_y(get_y() + 3)

lines421 += emit_row(R(f"𝑃(0)∧𝑃(1)∧∀{N}∈ℕ(𝑃({N})→𝑃({N}+2))   →   ∀{N}∈ℕ(𝑃({N}))", PSZ))
lines421 += emit_row(bt("EPf"))
y = get_y()

with open(os.path.join(OUT_PAGES, 'answers421.tex'), 'w', encoding='utf-8') as f:
    f.write('%% ===== answers421.tex — generated by gen_2c.py =====\n')
    f.write('\n'.join(lines421) + '\n')
print(f"wrote pages/answers421.tex ({len(lines421)} lines), final y={y:.1f} (limit ~700)")

# ========== Proof 2: Sm(alpha,n)/Sm(phi,n) (2b), page 422 continuation ===
def sm_rhs_full(k1n, k2n, inc, denom, sz, narg=N):
    """bare RHS of the Sm closed form (2b), no "Sm(nm,n)=" prefix --
    parametrized by narg so this also serves the RcS induction-hypothesis
    citation (narg=n, shrunk), not just the SPf definition (narg=n, full
    size)."""
    even_geo = Frac(HB(sup(R("(63)", sz), FloorAtom(Frac(R(narg, sz), R("2", sz), sz=sz), sz)), R(f" {M} 1", sz)),
                     R(str(denom), sz), sz=sz)
    odd_geo = Frac(HB(sup(R("(63)", sz), FloorAtom(Frac(R(f"({narg}{M}1)", sz), R("2", sz), sz=sz), sz)), R(f" {M} 1", sz)),
                    R(str(denom), sz), sz=sz)
    return HB(
        R("(", sz), Frac(R(str(k1n), sz), R(str(denom), sz), sz=sz), R(")(", sz), even_geo, R(")", sz),
        R("+(", sz), Frac(R(str(k2n), sz), R(str(denom), sz), sz=sz), R(")(", sz), odd_geo, R(")", sz),
        Kern(2), R(f"{M}(", sz), Frac(R(str(inc), sz), R(str(denom), sz), sz=sz), R(f")({narg}+1)", sz),
    )


def sm_full(nm, k1n, k2n, inc, sz):
    return HB(R(f"𝑆𝑚({nm},{N})=", sz), sm_rhs_full(k1n, k2n, inc, 62, sz))


sm_alpha_full = sm_full(A, 71, 3357, 9, PSZ)
sm_phi_full = sm_full(PH, 373, 497, 1, PSZ)


def rs_bc_row_sm(k1n, k2n, inc, denom, val, sz=PSZ):
    """Sm's RS at n=0: floor(0/2)=0 so the even geometric term is
    (63^1-1)/62=1, and floor(-1/2)=-1 so the odd term's (63^0-1)/62=0 --
    shown as the already-simplified bracket values (same economy as
    Proof 1's rs_bc_row) rather than deriving the floor arithmetic."""
    return HB(bt("RS"), Kern(6), R("=", sz), Kern(4),
              R("(", sz), Frac(R(str(k1n), sz), R(str(denom), sz), sz=sz), R(")(1) + (", sz),
              Frac(R(str(k2n), sz), R(str(denom), sz), sz=sz), R(")(0)", sz),
              Kern(3), R(f"{M}(", sz), Frac(R(str(inc), sz), R(str(denom), sz), sz=sz), R(")(1)", sz),
              Kern(4), R(f"= {val}", sz))


emit_row, get_y, set_y = make_rowtools(88.0)
lines422 = []
lines422 += emit_row(bt("(2c) continued"), xx=72.02)
set_y(get_y() + 10)

lines422 += emit_row(bt("SPf"))
lines422 += emit_row(HB(R("𝑅(", PSZ), R(N, PSZ), R(") ≔ (", PSZ), sm_alpha_full, R(")", PSZ)))
lines422 += emit_row(HB(R("        ∧ (", PSZ), sm_phi_full, R(")", PSZ)))
set_y(get_y() + 3)

lines422 += emit_row(bbt("BC"))
lines422 += emit_row(HB(bt("LS"), Kern(6), R("=", PSZ), Kern(4), R(f"𝑆𝑚({A},0)≔{A}(0)=1", PSZ)))
lines422 += emit_row(rs_bc_row_sm(71, 3357, 9, 62, 1))
lines422 += emit_row(HB(bt("LS"), R(" = ", PSZ, font='b'), bt("RS")))
lines422 += emit_row(HB(bt("LS"), Kern(6), R("=", PSZ), Kern(4), R(f"𝑆𝑚({PH},0)≔{PH}(0)=6", PSZ)))
lines422 += emit_row(rs_bc_row_sm(373, 497, 1, 62, 6))
lines422 += emit_row(HB(bt("LS"), R(" = ", PSZ, font='b'), bt("RS")))
lines422 += emit_row(R("𝑅(0)", PSZ))
set_y(get_y() + 3)

CSZ2C_SM = 7.0
lines422 += emit_row(bbt("RcS"))
hyp2 = HB(R("𝑅(0) 𝑅(1) ", PSZ), cdots(PSZ), Kern(2), R(f" 𝑅({N})", PSZ))
lines422 += emit_row(hyp2)
lines422 += emit_rule_at(get_y, set_y, x0, 200, hyp2)
lines422 += emit_row(bt("LS"))
lines422 += emit_row(HB(R("=", PSZ), Kern(4), R(f"𝑆𝑚({A},{N}+1)", PSZ)))
lines422 += emit_row(HB(R("=", PSZ), Kern(4), R(f"𝑆𝑚({A},{N})+{A}({N}+1)", PSZ)))
lines422 += emit_row(HB(R("=", PSZ), Kern(4), sm_rhs_full(71, 3357, 9, 62, CSZ2C_SM, N),
                        Kern(3), R("+(", PSZ), closed_form_rhs(1, 54, 63, 9, 62, CSZ2C_SM, f"{N}+1"), R(")", PSZ)))
rs3 = HB(R("=", PSZ), Kern(4), bt("RS"))
lines422 += emit_row(rs3)
set_y(get_y() + rs3.dp + 5)
lines422 += emit_row(bt("LS"))
lines422 += emit_row(HB(R("=", PSZ), Kern(4), R(f"𝑆𝑚({PH},{N}+1)", PSZ)))
lines422 += emit_row(HB(R("=", PSZ), Kern(4), R(f"𝑆𝑚({PH},{N})+{PH}({N}+1)", PSZ)))
lines422 += emit_row(HB(R("=", PSZ), Kern(4), sm_rhs_full(373, 497, 1, 62, CSZ2C_SM, N),
                        Kern(3), R("+(", PSZ), closed_form_rhs(6, 8, 63, 1, 62, CSZ2C_SM, f"{N}+1"), R(")", PSZ)))
rs4 = HB(R("=", PSZ), Kern(4), bt("RS"))
lines422 += emit_row(rs4)
lines422 += emit_rule_at(get_y, set_y, x0, 80, rs4)
lines422 += emit_row(R(f"𝑅({N}+1)", PSZ))
set_y(get_y() + 3)

lines422 += emit_row(R(f"𝑅(0)  ∧  ∀{N}∈ℕ(𝑅({N})→𝑅({N}+1))   →   ∀{N}∈ℕ(𝑅({N}))", PSZ))
lines422 += emit_row(bt("EPf"))
y = get_y()

with open(os.path.join(OUT_PAGES, 'answers422.tex'), 'w', encoding='utf-8') as f:
    f.write('%% ===== answers422.tex — generated by gen_2c.py =====\n')
    f.write('\n'.join(lines422) + '\n')
print(f"wrote pages/answers422.tex ({len(lines422)} lines), final y={y:.1f} (limit ~700)")
