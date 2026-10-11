#!/usr/bin/env python3
"""2c work sheet (folio 5120). FLAGGED: no solved exhibit exists for 2c in
either SOL2B-2020 or SOL2B-2024 (both leave 2c blank in their own grading
tables, same "no sample" gap class as 1C/2A's own unsolved sub-parts) --
built by analogy, not matched against a reference. Proves the general
identity (P->R)^(P->S) = P->(R^S) via algebra of propositions (-> unfolds
to not/or per page 511's own given identity, then distributes), then
instantiates P=(p v q), R=p, S=q to reach the printed page's own target.
Citation style (inline parenthetical identity) matches 2b's own confirmed
convention (minus the U+2235 "because" glyph, missing from both fonts --
see gen_2b_work.py's note).

Schema variables P/R/S (not A/B/C): this exam's own merged font's
math-italic CAPITAL coverage is only {C,J,L,N,P,R,S,T,V,W,Y} (checked via
fontTools, same per-exam-independent-subset gotcha this project has hit on
every prior exam) -- A and B aren't in it. Picked P/R/S deliberately
distinct from the exam's own lowercase p/q/r/s to avoid the meta-variable
being visually confused with the actual propositional variables it's
later instantiated with.
"""
import sys
sys.path.insert(0, '.')
from atoms import smart, HB, Kern
from stack import VStack
from pieces import lay_pieces, write_sheets

SZ = 11.04
CITESZ = 9.5


def cite(text):
    return HB(Kern(14.0), smart(f'({text})', CITESZ, font='c'))


def row(expr_text, citation=None):
    a = smart(expr_text, SZ, font='c')
    return HB(a, cite(citation)) if citation else a


rows = [
    (row('(𝑃→𝑅)∧(𝑃→𝑆)'), 9.0),
    (row('=((¬𝑃)∨𝑅)∧((¬𝑃)∨𝑆)', '𝑝→𝑞=(¬𝑝)∨𝑞'), 9.0),
    (row('=(¬𝑃)∨(𝑅∧𝑆)', '(¬𝑃∨𝑅)∧(¬𝑃∨𝑆)=¬𝑃∨(𝑅∧𝑆)'), 9.0),
    (row('=𝑃→(𝑅∧𝑆)', '(¬𝑝)∨𝑞=𝑝→𝑞'), 9.0),
    (row('𝑃≔(𝑝∨𝑞),𝑅≔𝑝,𝑆≔𝑞'), 6.0),
    (row('((𝑝∨𝑞)→𝑝)∧((𝑝∨𝑞)→𝑞)=(𝑝∨𝑞)→(𝑝∧𝑞)'), 9.0),
]
content = VStack(rows)

sheets = lay_pieces([('2c', content, 4.0, 4.0)])
write_sheets(5120, sheets, 'sheets')
