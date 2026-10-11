#!/usr/bin/env python3
from common import T, Chain, Barred, VStack, gen

rcs_chain = Chain(T('S(3,n+1)'), [
    T('(n(n+1)/2)² + (n+1)³'),
    ('=', T('(n+1)²∙[n²/4+(n+1)]')),
    ('=', T('(n+1)²∙(n+2)²/4')),
    ('=', T('((n+1)(n+2)/2)²')),
    ('=', T('(S(1,n+1))²')),
])

rcs_block = Barred(Barred(T('P(n)'), rcs_chain), T('P(n+1)'))

proof = VStack([
    (T('S(1,n) = n(n+1)/2.   P(n) ≔ (S(3,n) = (S(1,n))²)'), 0),
    (T('SPf'), 8),
    (T('BC'), 8),
    (Barred(T('S(3,0) = 0 = (S(1,0))²'), T('P(0)')), 6),
    (T('RcS'), 12),
    (rcs_block, 6),
    (T('EPf'), 10),
])

gen(10190, [('9.0', proof, 4, 4)])
