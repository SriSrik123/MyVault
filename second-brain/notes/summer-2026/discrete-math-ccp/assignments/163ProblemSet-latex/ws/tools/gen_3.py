#!/usr/bin/env python3
from common import T, Barred, VStack, gen

pieces = [
    ('3.0', VStack([
        (T('a,b,c ∈ ℕ'), 0),
        (Barred(T('a = 1a'), T('a∣a')), 8),
    ]), 4, 4),
    ('3.1', Barred(T('∀a∈ℕ (a∣a)'), T('Rflx(∣)')), 4, 6),
    ('3.2', Barred(T('a=0    a∣b'), T('b = c∙0 = 0 = a')), 4, 6),
    ('3.3', Barred(T('a≠0    a∣b    b∣a'), T('b=ca    a=db')), 4, 6),
    ('3.4', Barred(T('a = db = d(ca) = (dc)a'), T('dc = 1')), 4, 6),
    ('3.5', Barred(T('dc = 1'), T('d=1    c=1')), 4, 6),
    ('3.6', Barred(T('d=1    c=1'), T('b = ca = 1a = a')), 4, 6),
    ('3.7', Barred(T('∀a,b∈ℕ((a∣b  b∣a)/(a=b))'), T('AntSym(∣)')), 4, 6),
    ('3.8', Barred(T('a∣b    b∣c'), T("b=c′a    c=bd′")), 4, 6),
    ('3.9', Barred(T("c = bd′ = (c′a)d′ = (c′d′)a"), T('a∣c')), 4, 6),
    ('3.10', Barred(T('∀a,b,c∈ℕ((a∣b  b∣c)/(a∣c))'), T('Trns(∣)')), 4, 6),
    ('3.11', Barred(T('Rflx(R)    AntSym(R)    Trns(R)'), T('PO(R,ℕ)')), 4, 4),
]

gen(10070, pieces)
