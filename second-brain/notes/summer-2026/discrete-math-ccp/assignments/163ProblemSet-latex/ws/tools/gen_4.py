#!/usr/bin/env python3
from common import T, Barred, VStack, gen

pieces = [
    ('4.0', VStack([
        (T('x,y,z ∈ ℤ'), 0),
        (Barred(T('x² = x²'), T('xRx')), 8),
    ]), 4, 4),
    ('4.1', Barred(T('∀x∈ℤ (xRx)'), T('Rflx(R)')), 4, 6),
    ('4.2', Barred(T('xRy'), T('x² = y²')), 4, 6),
    ('4.3', Barred(T('x² = y²'), T('y² = x²')), 4, 6),
    ('4.4', Barred(T('y² = x²'), T('yRx')), 4, 6),
    ('4.5', Barred(T('∀x,y∈ℤ (xRy / yRx)'), T('Sym(R)')), 4, 6),
    ('4.6', Barred(T('xRy    yRz'), T('x²=y²    y²=z²')), 4, 6),
    ('4.7', Barred(T('x² = y² = z²'), T('x² = z²')), 4, 6),
    ('4.8', Barred(T('x² = z²'), T('xRz')), 4, 6),
    ('4.9', Barred(T('∀x,y,z∈ℤ((xRy  yRz)/(xRz))'), T('Trns(R)')), 4, 6),
    ('4.10', Barred(T('Rflx(R)    Sym(R)    Trns(R)'), T('Eqv(ℤ,R)')), 4, 6),
    ('4.11', VStack([
        (T('EqvCl(x,R) = {t∈ℤ ∣ t² = x²} = {x,−x}'), 0),
        (T('x=0: EqvCl(0,R)={0}     x≠0: EqvCl(x,R)={x,−x}=EqvCl(−x,R)'), 8),
        (T('ℤ/R = {{0}} ∪ {{−n,n} ∣ n∈ℕ,n≥1}'), 8),
    ]), 4, 4),
]

gen(10090, pieces)
