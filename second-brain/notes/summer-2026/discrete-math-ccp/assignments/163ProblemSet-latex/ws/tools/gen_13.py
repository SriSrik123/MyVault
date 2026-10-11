#!/usr/bin/env python3
from common import T, Barred, VStack, gen

p1 = [
    ('13.0', VStack([
        (T('p,q,r ∈ Prp'), 0),
        (Barred(T('p↔p (tautology)'), T('pQp')), 8),
    ]), 4, 4),
    ('13.1', Barred(T('∀p∈Prp (pQp)'), T('Rflx(Q)')), 4, 6),
    ('13.2', Barred(T('pQq'), T('p↔q')), 4, 6),
    ('13.3', Barred(T('p↔q'), T('q↔p')), 4, 6),
    ('13.4', Barred(T('q↔p'), T('qQp')), 4, 6),
    ('13.5', Barred(T('∀p,q∈Prp (pQq/qQp)'), T('Sym(Q)')), 4, 6),
    ('13.6', Barred(T('pQq    qQr'), T('p↔q    q↔r')), 4, 6),
    ('13.7', Barred(T('p↔q↔r'), T('p↔r')), 4, 6),
    ('13.8', Barred(T('p↔r'), T('pQr')), 4, 6),
    ('13.9', Barred(T('∀p,q,r∈Prp((pQq  qQr)/pQr)'), T('Trns(Q)')), 4, 6),
    ('13.10', Barred(T('Rflx(Q)    Sym(Q)    Trns(Q)'), T('Eqv(Q)')), 4, 6),
    ('13.11', T('𝔽 ≔ Prp/Q ≔ {EqvCl(p,Q) ∣ p∈Prp}'), 4, 6),
    ('13.12', VStack([
        (T('pQq, p→r, rQs given.'), 0),
        (Barred(T('pQq'), T('p↔q')), 6),
    ]), 4, 6),
    ('13.13', Barred(T('p↔q'), T('q→p')), 4, 6),
    ('13.14', Barred(T('rQs'), T('r↔s')), 4, 6),
    ('13.15', Barred(T('r↔s'), T('r→s')), 4, 6),
    ('13.16', Barred(T('q→p    p→r    r→s'), T('q→s')), 4, 4),
]

p2 = [
    ('13.17', T('FℰG ≔ (F⟹G): well-defined by (ii) (independent of representatives p∈F,r∈G)'), 4, 6),
    ('13.18', VStack([
        (T('F,G,H ∈ 𝔽'), 0),
        (Barred(T('p,p′∈F'), T('pQp′')), 8),
    ]), 4, 6),
    ('13.19', Barred(T('pQp′'), T('p↔p′')), 4, 6),
    ('13.20', Barred(T('p↔p′'), T('p→p′')), 4, 6),
    ('13.21', Barred(T('∀F∈𝔽 (FℰF)'), T('Rflx(ℰ)')), 4, 6),
    ('13.22', Barred(T('FℰG    GℰF'), T('p₀→q₀    q₀→p₀')), 4, 6),
    ('13.23', Barred(T('p₀→q₀    q₀→p₀'), T('p₀↔q₀')), 4, 6),
    ('13.24', Barred(T('p₀↔q₀'), T('p₀Qq₀')), 4, 6),
    ('13.25', Barred(T('p₀Qq₀'), T('F=G')), 4, 6),
    ('13.26', Barred(T('∀F,G∈𝔽((FℰG  GℰF)/(F=G))'), T('AntSym(ℰ)')), 4, 6),
    ('13.27', Barred(T('FℰG    GℰH'), T('∀p∈F,q∈G(p→q)    ∀q∈G,r∈H(q→r)')), 4, 6),
    ('13.28', Barred(T('∀p∈F,q∈G(p→q)    ∀q∈G,r∈H(q→r)'), T('∀p∈F,r∈H(p→r)')), 4, 6),
    ('13.29', Barred(T('∀p∈F,r∈H(p→r)'), T('FℰH')), 4, 6),
    ('13.30', Barred(T('∀F,G,H∈𝔽((FℰG  GℰH)/FℰH)'), T('Trns(ℰ)')), 4, 6),
    ('13.31', Barred(T('Rflx(ℰ)    AntSym(ℰ)    Trns(ℰ)'), T('PO(ℰ,𝔽)')), 4, 4),
]

gen(10270, p1)
gen(10272, p2)
