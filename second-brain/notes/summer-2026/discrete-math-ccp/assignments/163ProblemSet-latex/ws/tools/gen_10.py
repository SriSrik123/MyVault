#!/usr/bin/env python3
from common import T, Chain, Barred, VStack, gen

rcs_step1 = Barred(T('P(n)'), T('β(n+1) = (n+1)β(n) ≤ (n+1)γ(n)'))
rcs_step2 = Barred(T('n ≤ n+1'), T('γ(n) = nⁿ ≤ (n+1)ⁿ'))
rcs_tail = Chain(T('(n+1)γ(n)'), [T('(n+1)(n+1)ⁿ'), T('(n+1)ⁿ⁺¹'), T('γ(n+1)')])

rcs_block = Barred(VStack([
    (rcs_step1, 0),
    (rcs_step2, 8),
    (rcs_tail, 8),
]), T('P(n+1)'))

proof = VStack([
    (T('P(n) ≔ (γ(n) ≥ β(n))'), 0),
    (T('SPf'), 8),
    (T('BC'), 8),
    (Barred(T('γ(0) = 0⁰ = 1 = 0! = β(0)'), T('P(0)')), 6),
    (T('RcS'), 12),
    (rcs_block, 6),
    (T('EPf'), 10),
])

gen(10210, [('10.0', proof, 4, 4)])
