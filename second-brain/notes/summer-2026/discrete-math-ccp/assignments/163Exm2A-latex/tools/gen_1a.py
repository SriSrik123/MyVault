#!/usr/bin/env python3
"""1a: binomial expansion of (b-ax)^c (p404) and multinomial expansion of
(c-x+y)^(1+a) (p405), with a=1,b=9,c=5 (see gen_402.py).

Math (verified by hand, see project memory):
  (9-1x)^5 = 59049 + (-1)32805x + 7290x^2 + (-1)810x^3 + 45x^4 + (-1)x^5
  (5-x+y)^2 = 25 + (-1)10x + x^2 + (-1)2xy + 10y + y^2
Term ordering: page-403's rule -- numero-alphabetical within a term (numbers
before letters, letters alphabetical), terms ordered lexicographically on
their expanded (repeated-letter) word form, (-1) the only negative numeral.
Confirmed both expansions' natural generation order already matches this
(binomial descending in k = ascending word length in x; multinomial in
"",x,xx,xy,y,yy order) -- no re-sorting needed, verified by hand against
Binomial and Multinomial Theorem Notes' own worked example (p.7-8, the
(1-x+y)^2 case), which sorts to the identical shape.

Glyph note: the font only has the math-italic x/y (U+1D465/1D466) and the
U+2212 minus sign -- plain ASCII 'x','y','-' are NOT in the subset (same
class of gap as the missing digits, see gen_402.py/mergefonts.py). Every
string literal below uses the italic codepoints and U+2212 explicitly.

Only the printed-page template fills + final polynomial answer -- NOT the
full coefficient-by-coefficient work-sheet derivation (styleguide 5.1/5.4),
which is deferred (flagged in project memory)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import R, sup, fmt

OUT_PAGES = os.path.join(os.path.dirname(__file__), '..', 'pages')
SZ = 14.04
SSZ = 9.96  # exponent/superscript size, matches printed exponent slots

X = "\U0001D465"   # math-italic x
Y = "\U0001D466"   # math-italic y
M1 = "(−1)"   # "(-1)" with U+2212 minus


def fit_centered(text, x0, x1, y, max_sz=SZ, min_sz=7.0, inset=1.5):
    """Center `text` in the printed blank spanning [x0,x1] on baseline y,
    shrinking from max_sz until it fits inset from both edges. Narrow
    template slots (e.g. a signed '(-1)' in an ~19pt paren gap) need this --
    same class of fix as the 1C project's centered()/inset lesson.

    x0,x1 are the printed '(' / ')' glyphs' own origins, NOT their ink
    edges -- '(' ink extends rightward from x0 by its own width, so the
    real interior is [x0+paren_w, x1]. Missing this initially caused a
    real overlap in gen_1b.py's wider fills ('(45)' etc.) even though it
    happened not to show up here since these fills are all single digits,
    narrow enough to hide the miscalculation -- fixed here too for
    correctness, not just because it visibly broke."""
    paren_w = R("(", max_sz).w
    ix0, ix1 = x0 + paren_w, x1
    avail = (ix1 - ix0) - 2 * inset
    sz = max_sz
    while sz > min_sz and R(text, sz).w > avail:
        sz -= 0.5
    a = R(text, sz)
    cx = ix0 + (ix1 - ix0 - a.w) / 2
    return a.emit(cx, y)


def poly_stack(parts, x0, y0, sz=SZ, rowgap=26.0, bar_dx=-16.0, bar_pad=6.0):
    """parts: list of (body_str, exponent_str_or_None). Page 403's own rule
    ("writing the summands VERTICALLY") plus the solved exhibit's own p404
    (2020/2024, confirmed by rendering it): first term sits on the printed
    '=' row; every later term drops to its own row below, left-aligned
    under the first, prefixed with '+', with a single vertical rule drawn
    to their left connecting the whole run -- not the horizontal run-on
    this generator originally used (a real rule violation, caught auditing
    against page 403's "writing the summands VERTICALLY" + the exhibit's
    own vertical-bar-plus-'+'-prefix rendering of this exact problem type,
    not by guessing)."""
    out = []
    body0, exp0 = parts[0]
    a0 = R(body0, sz)
    atom0 = sup(a0, R(exp0, sz)) if exp0 else a0
    out += atom0.emit(x0, y0)
    y = y0
    for body, exp in parts[1:]:
        y += rowgap
        plus = R("+", sz)
        out += plus.emit(x0, y)
        a = R(body, sz)
        atom = sup(a, R(exp, sz)) if exp else a
        out += atom.emit(x0 + plus.w + 4.0, y)
    bar_x = x0 + bar_dx
    out.append(f'\\DLINE{{{fmt(bar_x)}}}{{{fmt(y0 + bar_pad)}}}'
               f'{{{fmt(bar_x)}}}{{{fmt(y + bar_pad)}}}{{0.7}}')
    return out


# ------------------------------------------------------------------ page404
lines404 = []
# line 1 "My problem:" -- positional fill, NOT simplified: (9)-(1)x)^(5)
lines404 += fit_centered("9", 260.57, 279.41, 165.50)         # b
lines404 += fit_centered("1", 301.73, 320.59, 165.50)         # a
lines404 += fit_centered("5", 342.79, 355.99, 141.38, SSZ)    # c (exponent)
# line 2 rewrite: = (9)+(-1)x)^(5) -- the blank here sits BETWEEN the
# template's own fixed "(" "..." ")" (page404.tex y=259.97), so the fill
# must be the bare signed digit "-1", not M1="(-1)" -- filling M1 doubled
# up the parens (fixed "(" + my own "(" ... ")" + fixed ")") and forced
# fit_centered's shrink loop down to an illegible subscript-sized "(-1)"
# (audit finding, 2026-08-01: caught by zooming a render, not visible at
# normal page-view zoom).
lines404 += fit_centered("9", 260.57, 279.41, 259.97)
lines404 += fit_centered("−1", 301.73, 320.59, 259.97)
lines404 += fit_centered("5", 342.79, 355.99, 235.82, SSZ)
# final answer line (y=334.13, after the printed '=')
parts404 = [("59049", None), (f"{M1}32805{X}", None), (f"7290{X}", "2"),
            (f"{M1}810{X}", "3"), (f"45{X}", "4"), (f"{M1}{X}", "5")]
lines404 += poly_stack(parts404, 240.0, 334.13)

with open(os.path.join(OUT_PAGES, 'answers404.tex'), 'w', encoding='utf-8') as f:
    f.write('%% ===== answers404.tex — generated by gen_1a.py =====\n')
    f.write('\n'.join(lines404) + '\n')
print(f"wrote pages/answers404.tex ({len(lines404)} lines)")

# ------------------------------------------------------------------ page405
lines405 = []
# line 1: (5)-(1)x+y)^(1+(1))  -- c=5; the x-coefficient blank is always 1
# (problem prints '-x', not '-ax' -- confirmed against SOL2A-2024's own
# filled sample, which also writes a literal '1' there); exponent a=1
lines405 += fit_centered("5", 260.57, 279.41, 165.50)
lines405 += fit_centered("1", 301.73, 320.59, 165.50)
lines405 += fit_centered("1", 382.39, 395.59, 141.74, SSZ)
# line 2 rewrite: = (5)+(-1)x+y)^(2)   [combined exponent 1+a=2] -- same
# double-paren fix as 404's rewrite line above (blank sits between the
# template's own fixed parens).
lines405 += fit_centered("5", 269.81, 288.65, 260.45)
lines405 += fit_centered("−1", 320.23, 339.07, 260.45)
lines405 += fit_centered("2", 385.87, 399.19, 236.30, SSZ)
# final answer (y=330.89)
parts405 = [("25", None), (f"{M1}10{X}", None), (X, "2"),
            (f"{M1}2{X}{Y}", None), (f"10{Y}", None), (Y, "2")]
lines405 += poly_stack(parts405, 240.0, 330.89)

with open(os.path.join(OUT_PAGES, 'answers405.tex'), 'w', encoding='utf-8') as f:
    f.write('%% ===== answers405.tex — generated by gen_1a.py =====\n')
    f.write('\n'.join(lines405) + '\n')
print(f"wrote pages/answers405.tex ({len(lines405)} lines)")
