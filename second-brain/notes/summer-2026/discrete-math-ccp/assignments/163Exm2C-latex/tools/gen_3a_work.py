#!/usr/bin/env python3
"""3a work sheet (folio 5130, matching page 513's n0 convention): six
boxed cells (alpha..eta), each a 2-step reduction chain over a bar over a
Tlg/Cdn/Cng citation naming the FULL substituted expression (not the greek
letter) -- exact format confirmed from SOL2B-2024's own folio 5140 (all
six cells), same 2-row x 3-col grid, same "cite only the first/inner
simplification step, leave the final collapse uncited" convention (holds
across all six of Yellowbeard's own cells, cross-checked one by one before
trusting it as a real rule and not a coincidence).

Greek-letter and Tlg/Cdn/Cng codepoints copied directly from page513.tex's
OWN already-working trace, not retyped: a first draft used plain Greek
(U+03B1 etc) and plain ASCII "Tlg"/"Cdn"/"Cng", both silently missing from
CambriaM even though they LOOK identical to what's on the printed page --
the printed page actually uses MATH-ITALIC alpha/beta/gamma/zeta/eta
(U+1D6FC/FD/FE/701/702) and PLAIN Greek delta (U+03B4, an inconsistency in
the source exam's own Word typesetting, traced faithfully rather than
"corrected"), plus math-italic T/l/g/C/d/n (U+1D447 etc, matching the
printed page's own "Tlg(alpha)" citations exactly) -- found only by
grep'ing the actual bytes out of the working trace after the exhibit-
identical-looking glyphs still threw "Missing character".
"""
import sys
sys.path.insert(0, '.')
from atoms import smart, HB, Kern
from stack import VStack, Barred
from pieces import lay_grid, write_sheets

SZ = 10.0
CITESZ = 8.5

ALPHA, BETA, GAMMA = chr(0x1D6FC), chr(0x1D6FD), chr(0x1D6FE)
DELTA, ZETA, ETA = chr(0x03B4), chr(0x1D701), chr(0x1D702)
Tt, ll, gg = chr(0x1D447), chr(0x1D459), chr(0x1D454)
Cc, dd, nn = chr(0x1D436), chr(0x1D451), chr(0x1D45B)
TLG = Tt + ll + gg
CDN = Cc + dd + nn
CNG = Cc + nn + gg


def cite(text):
    return HB(Kern(10.0), smart(f'({text})', CITESZ, font='c'))


def cell(def_line, step1, step1_cite, final, citation_arg, verdict):
    rows = [
        (smart(def_line, SZ, font='c'), 7.0),
        (HB(smart(step1, SZ, font='c'), cite(step1_cite)), 7.0),
        (smart(final, SZ, font='c'), 7.0),
    ]
    chain = VStack(rows)
    citeline = smart(f'{verdict}({citation_arg})', SZ, font='c')
    return Barred(chain, citeline, pad=3.0, gap=5.0)


c_alpha = cell(f'{ALPHA}≔(⊺∨𝑝)∨⊥', '=⊺∨⊥', '⊺∨𝑝=⊺', '=⊺', '(⊺∨𝑝)∨⊥', TLG)
c_beta = cell(f'{BETA}≔⊺∨(𝑝∧⊥)', '=⊺∨⊥', '𝑝∧⊥=⊥', '=⊺', '⊺∨(𝑝∧⊥)', TLG)
c_gamma = cell(f'{GAMMA}≔(⊥∨𝑝)∧⊺', '=𝑝∧⊺', '⊥∨𝑝=𝑝', '=𝑝', '(⊥∨𝑝)∧⊺', CNG)
c_delta = cell(f'{DELTA}≔⊥∧(𝑝⟷⊺)', '=⊥∧𝑝', '𝑝⟷⊺=𝑝', '=⊥', '⊥∧(𝑝⟷⊺)', CDN)
c_zeta = cell(f'{ZETA}≔⊺∧(𝑝∧⊥)', '=⊺∧⊥', '𝑝∧⊥=⊥', '=⊥', '⊺∧(𝑝∧⊥)', CDN)
c_eta = cell(f'{ETA}≔(⊺⟷𝑝)⟷⊥', '=𝑝⟷⊥', '⊺⟷𝑝=𝑝', '=¬𝑝', '(⊺⟷𝑝)⟷⊥', CNG)

# Six independently bordered+labelled cells (3a.i..3a.vi), matching
# SOL2B-2024's own folio 5140 layout exactly -- lay_grid (pieces.py) added
# this session specifically for this problem, replacing an earlier
# per-row-only labeling workaround once the real per-cell grid convention
# was confirmed directly against the exhibit's own image.
sheets = lay_grid([
    ('3a.i', c_alpha), ('3a.ii', c_beta), ('3a.iii', c_gamma),
    ('3a.iv', c_delta), ('3a.v', c_zeta), ('3a.vi', c_eta),
], ncols=3)
write_sheets(5130, sheets, 'sheets')
