#!/usr/bin/env python3
"""3c work sheet (folio 5170). FLAGGED: no solved exhibit for 3c either
(same gap as 2c). The inference is INVALID, so the required "work" is a
countermodel, not a derivation -- state the falsifying assignment, show
every premise evaluates true and the conclusion evaluates false under it.
C2=OR,C4=AND,C6=IFF,C8=IFF for Sri; countermodel p=0,q=1,r=1,s=1 already
verified programmatically (verify_2b.py) and by hand earlier this session.

CORRECTED 2026-08-08: an earlier draft narrated this in English ("Counter-
model:", "(premise 1, true)", "(conclusion, false)", a closing "invalid"
sentence) -- none of that is authorized notation (not in Rules.md's
Authorized Abbreviations list, not printed anywhere on this exam, not
shown in any solved exhibit), it was just scaffolding I added myself.
Stripped to bare symbolic content: the assignment line and the four
evaluation chains speak for themselves (0/1 already means false/true
throughout this exam, per the T-number convention on page 505), and the
verdict itself is the circled N already on the printed page (517), not
something this worksheet needs to restate. Pure math now, so `row()`
routes to CambriaM primarily instead of Book Antiqua.
"""
import sys
sys.path.insert(0, '.')
from atoms import smart
from stack import VStack
from pieces import lay_pieces, write_sheets

SZ = 11.04


def row(text):
    return smart(text, SZ, font='c', mfont='b')


rows = [
    (row('𝑝≔0,𝑞≔1,𝑟≔1,𝑠≔1'), 8.0),
    (row('𝑝∨𝑞=0∨1=1'), 7.0),
    (row('𝑞∧𝑟=1∧1=1'), 7.0),
    (row('𝑟⟷𝑠=1⟷1=1'), 7.0),
    (row('𝑝⟷𝑞=0⟷1=0'), 9.0),
]
content = VStack(rows)

sheets = lay_pieces([('3c', content, 4.0, 4.0)])
write_sheets(5170, sheets, 'sheets')
