#!/usr/bin/env python3
from common import T, HB, Kern, Chain, Barred, VStack, gen

bc_chain = Chain(T('1^(p+1) − 0^(p+1)'), [T('1'), T('(0+1)^(p+1)')])

rcs_chain = Chain(T('Σ(k=0..n+1)[(k+1)^(p+1)−k^(p+1)]'), [
    T('Σ(k=0..n)[(k+1)^(p+1)−k^(p+1)] + [(n+2)^(p+1)−(n+1)^(p+1)]'),
    ('=', T('(n+1)^(p+1) + (n+2)^(p+1) − (n+1)^(p+1)')),
    ('=', T('(n+2)^(p+1)')),
    ('=', T('((n+1)+1)^(p+1)')),
])

rcs_block = Barred(Barred(T('Q(n)'), rcs_chain), T('Q(n+1)'))

proof = VStack([
    (T('Q(n) ≔ (Σ(k=0..n)[(k+1)^(p+1)−k^(p+1)] = (n+1)^(p+1))'), 0),
    (T('SPf'), 8),
    (T('BC'), 8),
    (Barred(bc_chain, T('Q(0)')), 6),
    (T('RcS'), 12),
    (rcs_block, 6),
    (T('EPf'), 10),
])

binom_id = T('(k+1)^(p+1) − k^(p+1) = Σ(j=0..p) C(p+1,j) k^j')

step2 = VStack([
    (binom_id, 0),
    (Barred(HB(binom_id, Kern(20), T('Q(n)')),
            T('Σ(j=0..p) C(p+1,j) S(j,n) = (n+1)^(p+1)')), 8),
])

formula = T('S(p,n) = 1/(p+1) ∙ [(n+1)^(p+1) − Σ(j=0..p−1) C(p+1,j) S(j,n)]')

check = Chain(T('p=2:  S(2,n)'), [
    T('⅓[(n+1)³−(n+1)−3∙n(n+1)/2]'),
    T('n(n+1)(2n+1)/6   ✓ (matches 2(8))'),
])

pieces = [
    ('15.0', proof, 4, 6),
    ('15.1', step2, 4, 6),
    ('15.2', formula, 4, 6),
    ('15.3', check, 4, 4),
]
gen(10320, pieces)
