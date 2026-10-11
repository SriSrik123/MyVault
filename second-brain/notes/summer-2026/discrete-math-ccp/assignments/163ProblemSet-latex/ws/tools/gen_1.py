#!/usr/bin/env python3
from common import T, HB, Kern, Chain, Barred, VStack, gen

SZ = 11.04

bc_phi = Chain(T('φ(4)'), [T('4!'), T('24')])
bc_psi = Chain(T('ψ(4)'), [T('2⁴'), T('16')])

rcs_chain = Chain(T('φ(n+5)'), [
    T('(n+5)φ(n+4)'),
    ('≥', T('(n+5)ψ(n+4)')),
    ('≥', T('2ψ(n+4)')),
    ('=', T('ψ(n+5)')),
])

rcs_block = Barred(Barred(T('P(n)'), rcs_chain), T('P(n+1)'))

proof = VStack([
    (T('P(n) ≔ (φ(n+4) ≥ ψ(n+4))'), 0),
    (T('SPf'), 8),
    (T('BC'), 8),
    (HB(bc_phi, Kern(28), bc_psi), 6),
    (Barred(T('24 ≥ 16'), T('P(0)')), 10),
    (T('RcS'), 12),
    (rcs_block, 6),
    (T('EPf'), 10),
])

pieces = [('1.0', proof, 4, 4)]

gen(10030, pieces)
