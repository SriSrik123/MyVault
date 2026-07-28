#!/usr/bin/env python3
"""Generate answers304.tex + work sheets 3040/3041 for problem 1a.
J-number 00499317: nu(St(J))=6, nu(MltSt(J))=8 (invariant for every student).
Run from the replica root: python3 tools/gen_1a.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import R, HB, Kern, VC, Frac, Infer, Chain, Chevrons, assign, binom, notin, wrap
from expr import NU, C_, P_, N_, K_, MINUS, St_J, MltSt_J, nu_StJ, nu_MltStJ
from pieces import lay_pieces, write_sheets

SZ = 11.04
OUT_PAGES = os.path.join(os.path.dirname(__file__), '..', 'pages')
OUT_SHEETS = os.path.join(os.path.dirname(__file__), '..', 'sheets')
os.makedirs(OUT_SHEETS, exist_ok=True)

n_val, m_val = "6", "8"   # nu(St(J)), nu(MltSt(J)) for THIS J-number


def Cof(inner, sz=SZ):
    """C(...) with the paren pair TALL-SIZED to inner's actual ink height --
    plain-text '(' ')' around a two-line Frac() leaves the closing paren
    at baseline height, floating away from what it's supposed to enclose."""
    return HB(R(C_, sz), wrap(inner, l='(', r=')', sz=sz, tight=2.0))

# ---------------------------------------------------------------- 2(i)
premise_i0 = R(f"{C_}({N_},{N_}) = 1", SZ)
concl_i0 = R(f"{C_}({nu_StJ},{nu_StJ}) = 1", SZ)
wit_i0 = Chevrons([assign(R(N_, SZ), R(nu_StJ, SZ))])
piece_i0 = Infer(premise_i0, concl_i0, wit_i0)

premise_i1 = R(f"{P_}({N_},{N_}) = {N_}!", SZ)
concl_i1 = R(f"{P_}({nu_MltStJ},{nu_MltStJ}) = ({nu_MltStJ})!", SZ)
wit_i1 = Chevrons([assign(R(N_, SZ), R(nu_MltStJ, SZ))])
piece_i1 = Infer(premise_i1, concl_i1, wit_i1)

first_i2 = R(f"{C_}({C_}({nu_StJ},{nu_StJ}), {P_}({nu_MltStJ},{nu_MltStJ}))", SZ)
step_i2a = R(f"{C_}(1, (({nu_MltStJ})!))", SZ)
step_i2b = R(f"{C_}(1, {m_val}!)", SZ)
step_i2c = binom("1", f"({m_val}!)", sz=SZ)
piece_i2 = Chain(first_i2, [step_i2a, step_i2b, step_i2c], sz=SZ)

dom_premise = HB(R(f"∀{N_}∈ℕ ∀{K_}∈0..{N_} ", SZ), binom(N_, K_, sz=SZ))
notin_premise = HB(R(f"({m_val}!) ", SZ), notin(SZ), R(" 0..1", SZ))
premise_i3 = HB(dom_premise, Kern(20), notin_premise)
concl_i3 = HB(binom("1", f"({m_val}!)", sz=SZ), R(" does not make sense", sz=SZ, font='b'))
piece_i3 = Infer(premise_i3, concl_i3)

# ---------------------------------------------------------------- 2(ii)
premise_ii0 = HB(R(f"{P_}({N_},{K_}) = ", SZ),
                 Frac(R(f"({N_}!)", SZ), R(f"(({N_}{MINUS}{K_})!)", SZ), sz=SZ))
concl_ii0 = HB(R(f"{P_}({nu_MltStJ}, {nu_StJ}) = ", SZ),
               Frac(R(f"({nu_MltStJ})!", SZ),
                    R(f"(({nu_MltStJ}){MINUS}({nu_StJ}))!", SZ), sz=SZ))
wit_ii0 = Chevrons([assign(R(N_, SZ), R(nu_MltStJ, SZ)),
                    assign(R(K_, SZ), R(nu_StJ, SZ))])
piece_ii0 = Infer(premise_ii0, concl_ii0, wit_ii0)

piece_ii1 = piece_i1  # P(n,n)=n! <n<-nu(St(J))> -- reuse i1's SHAPE, but witness differs
premise_ii1 = R(f"{P_}({N_},{N_}) = {N_}!", SZ)
concl_ii1 = R(f"{P_}({nu_StJ},{nu_StJ}) = ({nu_StJ})!", SZ)
wit_ii1 = Chevrons([assign(R(N_, SZ), R(nu_StJ, SZ))])
piece_ii1 = Infer(premise_ii1, concl_ii1, wit_ii1)

first_ii2 = R(f"{C_}({P_}({nu_MltStJ}, {nu_StJ}), {P_}({nu_StJ}, {nu_StJ}))", SZ)
step_ii2a = Cof(HB(Frac(R(f"({nu_MltStJ})!", SZ),
                        R(f"(({nu_MltStJ}){MINUS}({nu_StJ}))!", SZ), sz=SZ),
                    R(f", ({nu_StJ})!", SZ)))
step_ii2b = Cof(HB(Frac(R(f"({m_val}!)", SZ), R(f"(({m_val}{MINUS}{n_val})!)", SZ), sz=SZ),
                    R(f", ({n_val}!)", SZ)))
step_ii2c = Cof(HB(Frac(R(f"({m_val}!)", SZ), R("(2!)", SZ), sz=SZ),
                    R(f", ({n_val}!)", SZ)))
step_ii2d = binom(Frac(R(f"({m_val}!)", SZ), R("(2!)", SZ), sz=SZ), f"({n_val}!)", sz=SZ)
piece_ii2 = Chain(first_ii2, [step_ii2a, step_ii2b, step_ii2c, step_ii2d], sz=SZ)

# ---------------------------------------------------------------- 2(iii)
premise_iii0 = R(f"{P_}({N_},{N_}) = {N_}!", SZ)
concl_iii0 = R(f"{P_}({nu_MltStJ},{nu_MltStJ}) = ({nu_MltStJ})!", SZ)
wit_iii0 = Chevrons([assign(R(N_, SZ), R(nu_MltStJ, SZ))])
piece_iii0 = Infer(premise_iii0, concl_iii0, wit_iii0)

piece_iii1 = piece_i0  # same shape as i0, reused fresh below with its own label

first_iii2 = R(f"{C_}({P_}({nu_MltStJ},{nu_MltStJ}), {P_}({nu_StJ},{nu_StJ}))", SZ)
step_iii2a = R(f"{C_}(({nu_MltStJ})!, ({nu_StJ})!)", SZ)
step_iii2b = R(f"{C_}(({m_val}!), ({n_val}!))", SZ)
step_iii2c = binom(f"({m_val}!)", f"({n_val}!)", sz=SZ)
piece_iii2 = Chain(first_iii2, [step_iii2a, step_iii2b, step_iii2c], sz=SZ)

# ---------------------------------------------------------------- lay out sheets
pieces_all = [
    ("1a.i.0", piece_i0, 6, 8), ("1a.i.1", piece_i1, 10, 8),
    ("1a.i.2", piece_i2, 10, 8), ("1a.i.3", piece_i3, 10, 8),
    ("1a.ii.0", piece_ii0, 10, 8), ("1a.ii.1", piece_ii1, 10, 8),
    ("1a.ii.2", piece_ii2, 10, 8),
    ("1a.iii.0", piece_iii0, 10, 8), ("1a.iii.1", piece_i0, 10, 8),
    ("1a.iii.2", piece_iii2, 10, 8),
]
sheets = lay_pieces(pieces_all)
folios = write_sheets(3040, sheets, OUT_SHEETS)
print("1a work sheets used:", folios)

# ---------------------------------------------------------------- printed page 304
BA_EQ_W_AT_1596 = 13.5   # approx width of the printed "=" glyph (BookAntiqua 15.96bp)
X0 = 108.02 + BA_EQ_W_AT_1596 + 6
lines304 = []
lines304 += HB(binom("1", f"({m_val}!)", sz=SZ), R(" does not make sense", sz=SZ, font='b')
               ).emit(X0, 298.80)
lines304 += binom(Frac(R(f"({m_val}!)", SZ), R("(2!)", SZ), sz=SZ), f"({n_val}!)", sz=SZ
                  ).emit(X0, 472.10)
lines304 += binom(f"({m_val}!)", f"({n_val}!)", sz=SZ).emit(X0, 645.50)
with open(os.path.join(OUT_PAGES, 'answers304.tex'), 'w') as f:
    f.write('%% ===== answers304.tex — generated by gen_1a.py =====\n')
    f.write('\n'.join(lines304) + '\n')
print(f"wrote pages/answers304.tex ({len(lines304)} lines)")
