#!/usr/bin/env python3
from common import T, Barred, VStack, gen

pieces = [
    ('6.0', VStack([
        (T('(a,b),(c,d),(e,f) ∈ ℕ×ℕ'), 0),
        (Barred(T('a²+b² = a²+b²'), T('(a,b)R(a,b)')), 8),
    ]), 4, 4),
    ('6.1', Barred(T('∀(a,b)∈ℕ×ℕ ((a,b)R(a,b))'), T('Rflx(R)')), 4, 6),
    ('6.2', Barred(T('(a,b)R(c,d)'), T('a²+b² = c²+d²')), 4, 6),
    ('6.3', Barred(T('a²+b² = c²+d²'), T('c²+d² = a²+b²')), 4, 6),
    ('6.4', Barred(T('c²+d² = a²+b²'), T('(c,d)R(a,b)')), 4, 6),
    ('6.5', Barred(T('∀(a,b),(c,d)∈ℕ×ℕ((a,b)R(c,d)/(c,d)R(a,b))'), T('Sym(R)')), 4, 6),
    ('6.6', Barred(T('(a,b)R(c,d)    (c,d)R(e,f)'), T('a²+b²=c²+d²    c²+d²=e²+f²')), 4, 6),
    ('6.7', Barred(T('a²+b² = c²+d² = e²+f²'), T('a²+b² = e²+f²')), 4, 6),
    ('6.8', Barred(T('a²+b² = e²+f²'), T('(a,b)R(e,f)')), 4, 6),
    ('6.9', Barred(T('∀(a,b),(c,d),(e,f)∈ℕ×ℕ(((a,b)R(c,d) (c,d)R(e,f))/(a,b)R(e,f))'), T('Trns(R)')), 4, 6),
    ('6.10', Barred(T('Rflx(R)    Sym(R)    Trns(R)'), T('Eqv(ℕ×ℕ,R)')), 4, 6),
    ('6.11', VStack([
        (T('n ≔ a²+b².  EqvCl((a,b),R) = {(x,y)∈ℕ×ℕ ∣ x²+y²=n}'), 0),
        (T('(ℕ×ℕ)/R = {{(x,y) ∣ x²+y²=n} ∣ n∈ℕ, ∃(x,y)(n=x²+y²)}'), 8),
    ]), 4, 4),
]

gen(10130, pieces)
