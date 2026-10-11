#!/usr/bin/env python3
from common import T, Chain, Barred, VStack, gen

rcs_chain = Chain(T('S(2,n+1)'), [
    T('n(n+1)(2n+1)/6 + (n+1)²'),
    ('=', T('(n+1)∙[n(2n+1)+6(n+1)]/6')),
    ('=', T('(n+1)∙(2n²+7n+6)/6')),
    ('=', T('(n+1)(n+2)(2n+3)/6')),
])

rcs_block = Barred(Barred(T('P(n)'), rcs_chain), T('P(n+1)'))

proof = VStack([
    (T('P(n) ≔ (S(2,n) = n(n+1)(2n+1)/6)'), 0),
    (T('SPf'), 8),
    (T('BC'), 8),
    (Barred(T('S(2,0) = 0² = 0'), T('P(0)')), 6),
    (T('RcS'), 12),
    (rcs_block, 6),
    (T('EPf'), 10),
])

gen(10170, [('8.0', proof, 4, 4)])
