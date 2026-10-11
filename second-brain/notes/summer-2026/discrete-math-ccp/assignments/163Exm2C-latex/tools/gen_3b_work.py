#!/usr/bin/env python3
"""3b work sheet (folio 5160, matching page 516's n0 convention): axioms/
rules-of-inference bar-chain proving Vld((p C3 q)->p, (p C3 q)->q /
(p C3 q)->(p C5 q)), C3=OR, C5=AND for Sri. Method (generalize from a
trivial Vld(r/r), substitute via chevron witnesses down to the target) and
opening two bars match SOL2B-2024's own folio 5170 exactly; Yellowbeard's
own C5=IFF continues two more bars past this to convert (p^q) into
(p<->q) -- Sri's C5=AND means the target IS (p^q) directly, so Sri's chain
correctly stops one bar earlier than Yellowbeard's, at the same
(p C3 q)->(p^q) shape already filled on the printed page.
"""
import sys
sys.path.insert(0, '.')
from atoms import R, HB, Frac, BarStack, Chevrons, assign
from pieces import lay_pieces, write_sheets

SZ = 10.5


def vld(num_text, den_text):
    num = R(num_text, SZ)
    den = R(den_text, SZ)
    return HB(R('𝑉𝑙𝑑(', SZ), Frac(num, den, sz=SZ, pad=3.0), R(')', SZ))


def witness(var, expr_text):
    return Chevrons([assign(R(var, SZ * 0.85), R(expr_text, SZ * 0.85), sz=SZ * 0.85)])


rows = [
    vld('𝑟', '𝑟'),
    vld('(𝑟→𝑝)∧(𝑟→𝑞)', '(𝑟→𝑝)∧(𝑟→𝑞)'),
    vld('(𝑟→𝑝)∧(𝑟→𝑞)', '𝑟→(𝑝∧𝑞)'),
    vld('((𝑝∨𝑞)→𝑝)∧((𝑝∨𝑞)→𝑞)', '(𝑝∨𝑞)→(𝑝∧𝑞)'),
]
witnesses = {
    0: witness('𝑟', '(𝑟→𝑝)∧(𝑟→𝑞)'),
    2: witness('𝑟', '(𝑝∨𝑞)'),
}
chain = BarStack(rows, witnesses=witnesses, pad=6.0, gap=5.0)

sheets = lay_pieces([('3b', chain, 6.0, 6.0)])
write_sheets(5160, sheets, 'sheets')
