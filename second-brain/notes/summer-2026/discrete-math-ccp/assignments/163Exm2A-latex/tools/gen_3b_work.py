#!/usr/bin/env python3
"""3b work: the actual Rtl contradiction proof (styleguide sec.6.6).

REBUILT (audit finding, 2026-08-01, Sri: "3b isn't done right"). The first
pass built a mathematically-correct but STRUCTURALLY wrong proof -- flowing
prose sentences ("By definition of Rtl: for some p,q...") instead of the
formal bar-step (premise / bar / conclusion) skeleton the styleguide's own
sec.6.6 specifies, sourced from the professor's OWN solved 3b exhibit.

Went back to 163Exam2A-Solutions-2024.pdf pages 19-20 (piece "3b.i",
folio 4260) and read the actual proof directly rather than trusting my own
paraphrased styleguide note blindly -- found the note's step 6 ordering was
slightly off (there are actually TWO double-negation moves: one right after
SPf, simplifying the awkward hypothesis "~(struck-goal)" down to plain
"Rtl(expr)" so the rest of the proof can work with it; a second one at the
very end, going from the derived contradiction back up through
"~~(struck-goal)" to the plain "struck-goal" conclusion -- confirmed by
reading the exhibit's own last 5 lines, not assumed).

CONFIRMED PROFESSOR MATH ERROR in the exhibit (project memory: "solved
exhibits -- correct FORMAT, unreliable MATH, never copy answers"): after
concluding p=2r, the exhibit substitutes back into a line reading
"2q^281=(2r)^281" -- should be "280q^281=(2r)^281" (280 was the coefficient
throughout, not 2). Followed the exhibit's STRUCTURE (factor out one prime,
prm() bar step, substitute, simplify, repeat for the other variable) but
used correct arithmetic throughout for my own numbers.

abcd = (1)(9)(5)(7) = 315 = 3^2 x 5 x 7, abcd+1 = 316. 315 has 3^2 (the
exhibit's 280=2^3x5x7 has 3 factors of its prime; mine has only 2) -- one
extra division-by-9 bookkeeping step before the second prm(3) call,
already correctly worked out in the first pass's math, just needed to be
wired into the new bar-step format.

FONT: no exists-quantifier or radical sign in this subset (checked directly
via fontTools, not assumed) -- "for some" replaces the exhibit's
exists-unique; kept the fractional-exponent form (315)^(1/316) throughout
rather than switching to the exhibit's root-sign notation, since the
radical glyph doesn't exist here and the printed problem statement itself
already uses the fractional-exponent form. RTL is math-italic (matches the
exam's own printed convention, confirmed in gen_3c.py). "prm" is a plain
Book-Antiqua proof-skeleton label, same convention as SPf/BC/RcS/EPf
elsewhere in this project -- not math-italic (that would be a mathematical
variable name, which this isn't).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import smart, R, HB, Kern, Frac, sup, strike, BarStack, fmt
from stack import VStack
from pieces import lay_pieces, write_sheets

OUT_PAGES = os.path.join(os.path.dirname(__file__), '..', 'pages')
OUT_SHEETS = os.path.join(os.path.dirname(__file__), '..', 'sheets')
PSZ = 9.0
RTL = "\U0001D445\U0001D461\U0001D459"  # 𝑅𝑡𝑙, math-italic (see gen_3c.py)


def bt(text, sz=PSZ):
    return smart(text, sz, font='b')


def p316(sz=PSZ):
    """the exponent (1/316) as a real stacked Frac, one size down."""
    return Frac(R("1", sz - 1), R("316", sz - 1), sz=sz - 1)


def expr(sz=PSZ):
    """(315)^(1/316), unstruck."""
    return HB(R("(315)", sz), sup(R(" ", sz), p316(sz)))


def rtl_of_expr(sz=PSZ):
    return HB(R(RTL, sz), R("(", sz), expr(sz), R(")", sz))


def struck_rtl_of_expr(sz=PSZ):
    return strike(rtl_of_expr(sz))


def pw(base_str, exponent, sz=PSZ):
    """base_str raised to a plain-text exponent, e.g. pw('315𝑞', '316')."""
    return HB(R(base_str, sz), sup(R(" ", sz), R(exponent, sz)))


def gcd_of(args_str, sz=PSZ):
    """gcd(args_str) -- "gcd" is a plain Book-Antiqua label (like prm),
    not math-italic: CambriaM has no math-italic 'g' at all (checked via
    fontTools, not assumed), so a bare R("𝑔𝑐𝑑...", sz) call silently drops
    the g. Matches gen_3c.py's own already-working bt(" gcd") precedent."""
    return HB(bt("gcd", sz), R(f"({args_str})", sz))


# ============================================================ page 426 ====
# Starts at y=350 -- page426.tex's own printed instruction ("Start proof on
# this side and continue on pages that follow...") is two BA{14.04} lines
# ending around y=321; 350 clears it with room to spare (matches the
# first pass's already-verified clearance).
rows426 = [
    HB(R("¬(", PSZ), struck_rtl_of_expr(PSZ), R(")", PSZ)),
    rtl_of_expr(PSZ),
    HB(bt("for some "), R("𝑝,𝑞∈ℕ ((", PSZ), gcd_of("𝑝,𝑞"), R("=1) ∧ (", PSZ), expr(PSZ), R(" = 𝑝÷𝑞))", PSZ)),
    HB(R("(", PSZ), gcd_of("𝑝,𝑞"), R("=1)", PSZ), Kern(30), R("(", PSZ), expr(PSZ), R(" = 𝑝÷𝑞)", PSZ)),
    HB(expr(PSZ), R(" = 𝑝÷𝑞", PSZ)),
]
stack426 = BarStack(rows426)

label_sz = 11.04
spf_label = R("SPf", label_sz, font='b')
lines426 = []
lines426 += spf_label.emit(144.02, 350.0)
lines426 += stack426.emit(144.02 + spf_label.w + 14, 350.0 + stack426.ht)

# Idempotent: read gen_3b.py's own (already-generated) substitution-line
# content fresh each run and rewrite the whole file, rather than
# appending -- appending would duplicate this proof on every re-run.
# Strip from WHICHEVER marker appears first -- the original prose-proof
# pass used a different marker string than this rebuild; splitting only
# on the new one left the old marker's block in place on the first rerun
# after the rewrite, rendering both proofs stacked on top of each other
# (caught by render: two overlapping "SPf" blocks). Check both so re-runs
# are safe regardless of which pass last wrote the file.
base_path = os.path.join(OUT_PAGES, 'answers426.tex')
base = open(base_path, encoding='utf-8').read()
marker = '%% ----- proof (rebuilt 2026-08-01, bar-step format) -----'
old_marker = '%% ----- proof (added 2026-08-01 audit fix) -----'
for m in (old_marker, marker):
    if m in base:
        base = base.split(m)[0]
        break
base = base.rstrip('\n')
with open(base_path, 'w', encoding='utf-8') as f:
    f.write(base + '\n\n' + marker + '\n')
    f.write('\n'.join(lines426) + '\n')
print(f"wrote pages/answers426.tex, stack bottom_y={350.0 + stack426.ht + stack426.dp:.1f} (limit ~714)")

# ============================================================ page 427 ====
rows427a = [
    HB(R("(", PSZ), expr(PSZ), R(")", PSZ), sup(R(" ", PSZ), R("316", PSZ)),
       R(" = (𝑝÷𝑞)", PSZ), sup(R(" ", PSZ), R("316", PSZ))),
    pw("315 = 𝑝", "316"),
    HB(pw("315 = 𝑝", "316"), R("÷𝑞", PSZ), sup(R(" ", PSZ), R("316", PSZ))),
    HB(pw("315𝑞", "316"), R(" = 𝑝", PSZ), sup(R(" ", PSZ), R("316", PSZ))),
    HB(R("(3)(3)(5)(7)(𝑞", PSZ), sup(R(" ", PSZ), R("316", PSZ)), R(") = 𝑝", PSZ), sup(R(" ", PSZ), R("316", PSZ))),
    HB(bt("prm(3)"), Kern(20), R("3|𝑝", PSZ), sup(R(" ", PSZ), R("316", PSZ))),
    R("3|𝑝", PSZ),
    HB(bt("for some "), R("𝑟∈ℕ (𝑝=3𝑟)", PSZ)),
    HB(pw("315𝑞", "316"), R(" = (3𝑟)", PSZ), sup(R(" ", PSZ), R("316", PSZ))),
    HB(pw("315𝑞", "316"), R(" = 3", PSZ), sup(R(" ", PSZ), R("316", PSZ)), R("𝑟", PSZ), sup(R(" ", PSZ), R("316", PSZ))),
]
stack427a = BarStack(rows427a)

title427 = HB(bt("(3b) continued - proof that "), expr(PSZ), bt(" is irrational"))
lines427 = []
lines427 += title427.emit(72.02, 100.0)
lines427 += stack427a.emit(90.0, 140.0 + stack427a.ht)
stack427a_bottom = 140.0 + stack427a.ht + stack427a.dp

# 315 = 9x35: divide both sides by 9, then the second prm(3) call. Own
# BarStack (own bar width) right below the first, with a small citation on
# the divide step instead of the exhibit's floating "÷9  ÷9" sub-
# annotation -- same simplification already used for the raise-to-power/
# multiply steps above.
rows427b = [
    HB(R("35𝑞", PSZ), sup(R(" ", PSZ), R("316", PSZ)), R(" = 3", PSZ), sup(R(" ", PSZ), R("314", PSZ)),
       R("𝑟", PSZ), sup(R(" ", PSZ), R("316", PSZ)), Kern(10), bt("(÷9)")),
    HB(bt("prm(3)"), Kern(20), R("3|35𝑞", PSZ), sup(R(" ", PSZ), R("316", PSZ))),
    HB(R("3|𝑞", PSZ), sup(R(" ", PSZ), R("316", PSZ)), Kern(10), R("(", PSZ), gcd_of("3,35"), R("=1)", PSZ)),
    R("3|𝑞", PSZ),
]
stack427b = BarStack(rows427b)
y427b = stack427a_bottom + 24.0
lines427 += stack427b.emit(90.0, y427b + stack427b.ht)
stack427b_bottom = y427b + stack427b.ht + stack427b.dp

with open(os.path.join(OUT_PAGES, 'answers427.tex'), 'w', encoding='utf-8') as f:
    f.write('%% ===== answers427.tex — generated by gen_3b_work.py =====\n')
    f.write('\n'.join(lines427) + '\n')
print(f"wrote pages/answers427.tex, ends at y={stack427b_bottom:.1f} (limit ~714)")

# ============================================================ ws4260 ======
# Final steps overflow to a work sheet, matching the SOLVED EXHIBIT's own
# choice (its "3b.i" piece, this exact continuation, lives on folio 4260 --
# confirmed by reading it directly, not guessed). lay_pieces()/
# write_sheets() (not a hand-rolled layout) for the same auto-pagination
# and \PLBL digit-7 safety every other work sheet gets.
rows4260 = [
    HB(R("3|𝑝", PSZ), Kern(20), R("3|𝑞", PSZ)),
    HB(R("3|", PSZ), gcd_of("𝑝,𝑞")),
    HB(R("3|", PSZ), gcd_of("𝑝,𝑞"), Kern(20), gcd_of("𝑝,𝑞"), R("=1", PSZ)),
    R("3|1", PSZ),
    R("⊥", PSZ),
    HB(R("¬(¬(", PSZ), struck_rtl_of_expr(PSZ), R("))", PSZ)),
    struck_rtl_of_expr(PSZ),
]
stack4260 = BarStack(rows4260)
epf_label = R("EPf", label_sz, font='b')
block4260 = VStack([(stack4260, 0), (epf_label, 16)])

pieces = [("3b.i", block4260, 4, 10)]
sheets = lay_pieces(pieces)
folios = write_sheets(4260, sheets, OUT_SHEETS)
print("3b overflow work sheet:", folios)
