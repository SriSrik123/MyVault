#!/usr/bin/env python3
from common import T, Barred, VStack, gen

pieces = [
    ('5.0', VStack([
        (T('(a,b),(c,d),(e,f) ∈ ℕ×ℕ'), 0),
        (Barred(T('a+b = a+b'), T('(a,b)R(a,b)')), 8),
    ]), 4, 4),
    ('5.1', Barred(T('∀(a,b)∈ℕ×ℕ ((a,b)R(a,b))'), T('Rflx(R)')), 4, 6),
    ('5.2', Barred(T('(a,b)R(c,d)'), T('a+b = c+d')), 4, 6),
    ('5.3', Barred(T('a+b = c+d'), T('c+d = a+b')), 4, 6),
    ('5.4', Barred(T('c+d = a+b'), T('(c,d)R(a,b)')), 4, 6),
    ('5.5', Barred(T('∀(a,b),(c,d)∈ℕ×ℕ((a,b)R(c,d)/(c,d)R(a,b))'), T('Sym(R)')), 4, 6),
    ('5.6', Barred(T('(a,b)R(c,d)    (c,d)R(e,f)'), T('a+b=c+d    c+d=e+f')), 4, 6),
    ('5.7', Barred(T('a+b = c+d = e+f'), T('a+b = e+f')), 4, 6),
    ('5.8', Barred(T('a+b = e+f'), T('(a,b)R(e,f)')), 4, 6),
    ('5.9', Barred(T('∀(a,b),(c,d),(e,f)∈ℕ×ℕ(((a,b)R(c,d) (c,d)R(e,f))/(a,b)R(e,f))'), T('Trns(R)')), 4, 6),
    ('5.10', Barred(T('Rflx(R)    Sym(R)    Trns(R)'), T('Eqv(ℕ×ℕ,R)')), 4, 6),
    ('5.11', VStack([
        (T('k ≔ a+b.  EqvCl((a,b),R) = {(x,y)∈ℕ×ℕ ∣ x+y=k} = {(0,k),(1,k−1),…,(k,0)}, size k+1'), 0),
        (T('(ℕ×ℕ)/R = {{(0,k),…,(k,0)} ∣ k∈ℕ}'), 8),
    ]), 4, 4),
]

gen(10110, pieces)
