#!/usr/bin/env python3
"""2b work sheet (folio 5110, matching page 511's own n0 convention):
algebra-of-propositions derivation of psi(p,q) down to bottom. Sri's
C1=C2=C3=OR is IDENTICAL to SOL2B-2024's own Yellowbeard exhibit (folio
5110 there too) -- this derivation is reused close to verbatim, matching
that exact 9-line format: opening negated definition, De Morgan x2,
double-negation, associativity regroup, p-and-not-p collapse x2, final
bottom, then the DNF/CNF restatement lines. Every citation matches the
exhibit's own inline "(: identity)" placement -- first-step-only citation
convention confirmed by cross-checking all six 3a cells' citation pattern
too (see gen_3a_work.py).

Font notes (found only by building and reading the "Missing character"
log, not by inspection): plain ASCII p/q used in a first draft silently
fell back to CambriaM's default face, which has NO plain Latin letters at
all (confirmed via fontTools) -- fixed by using math-italic p/q (U+1D45D/
1D45E, both present in this exam's own merged font) throughout, matching
every other file in this project. Separately, U+2235 (the "because" tri-
dot symbol the source exhibit itself uses) is missing from BOTH CambriaM
and BookAntiqua entirely -- dropped rather than substituted with a lookalike,
since no drawn-glyph workaround exists for it yet in this project; the
citation still reads as a parenthetical identity, just without the symbol.
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
    if citation:
        return HB(a, cite(citation))
    return a


rows = [
    (row('¬((𝑝∨(¬𝑞))∨((¬𝑝)∨𝑞))'), 9.0),
    (row('=((¬(𝑝∨(¬𝑞)))∧(¬((¬𝑝)∨𝑞)))', '¬(𝑝∨𝑞)=(¬𝑝)∧(¬𝑞)'), 9.0),
    (row('=(((¬𝑝)∧(¬(¬𝑞)))∧((¬(¬𝑝))∧(¬𝑞)))', '¬(𝑝∨𝑞)=(¬𝑝)∧(¬𝑞)'), 9.0),
    (row('=(((¬𝑝)∧𝑞)∧(𝑝∧(¬𝑞)))', '¬(¬𝑝)=𝑝'), 9.0),
    (row('=((𝑝∧(¬𝑝))∧(𝑞∧(¬𝑞)))', '(𝑝∧𝑞)∧𝑟=𝑝∧(𝑞∧𝑟)'), 9.0),
    (row('=((⊥)∧(⊥))', '𝑝∧(¬𝑝)=⊥'), 9.0),
    (row('=⊥', '𝑝∧𝑝=𝑝'), 9.0),
    (row('=⊥ (DNF)'), 9.0),
    (row('=⊥ (CNF)'), 9.0),
]
content = VStack(rows)

sheets = lay_pieces([('2b', content, 4.0, 4.0)])
write_sheets(5110, sheets, 'sheets')
