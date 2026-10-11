#!/usr/bin/env python3
"""Layout engine for the 1C answer layer.

Everything is set as Cambria/Book Antiqua TEXT runs (styleguide §2) placed at
absolute page coordinates; fractions, coefficient stacks, inference bars,
chevron witnesses and tall delimiters are composed here with real font
metrics and emitted as \\TL/\\GD/\\DLINE/\\RECT primitives (preamble.tex).

Coordinates: bp from page top-left, y increasing downward, baseline anchored.
Every Atom has width w, height ht (ink above baseline), depth dp (below);
emit(x, y) returns TeX lines for baseline-left at (x, y).
"""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPM = 2048.0


class Face:
    """Format-agnostic (TrueType glyf OR CFF/OTF) glyph metrics via the
    generic fontTools glyphSet + BoundsPen API, instead of raw glyf table
    access (which only exists for TrueType-outline fonts)."""
    def __init__(self, path):
        f = TTFont(path)
        self.cmap = f.getBestCmap()
        self.gset = f.getGlyphSet()
        self.hmtx = f['hmtx']
        self.order = f.getGlyphOrder()
        self.upm = f['head'].unitsPerEm
        self._bounds_cache = {}

    def gname(self, ch):
        return self.cmap.get(ord(ch))

    def adv(self, ch):
        gn = self.gname(ch)
        return self.hmtx[gn][0] / self.upm if gn else 0.5

    def _bounds(self, gn):
        if gn not in self._bounds_cache:
            pen = BoundsPen(self.gset)
            self.gset[gn].draw(pen)
            self._bounds_cache[gn] = pen.bounds  # (xMin,yMin,xMax,yMax) or None
        return self._bounds_cache[gn]

    def extents(self, ch):
        gn = self.gname(ch)
        if not gn:
            return (0.0, 0.7, 0.0)
        b = self._bounds(gn)
        if b is None:
            return (self.hmtx[gn][0] / self.upm, 0.0, 0.0)
        _, yMin, _, yMax = b
        return (self.hmtx[gn][0] / self.upm,
                max(0.0, yMax / self.upm), max(0.0, -yMin / self.upm))

    def gid_metrics(self, gid):
        gn = self.order[gid]
        b = self._bounds(gn)
        yMin, yMax = (0, 0) if b is None else (b[1], b[3])
        return (self.hmtx[gn][0] / self.upm, yMax / self.upm, yMin / self.upm)


CAM = Face(os.path.join(ROOT, 'fonts', 'STIXTwoMath-Regular.otf'))
BA = Face(os.path.join(ROOT, 'fonts', 'STIXTwoText-Regular.otf'))
BAB = Face(os.path.join(ROOT, 'fonts', 'STIXTwoText-Bold.otf'))
FACES = {'c': (CAM, r'\CMT'), 'b': (BA, r'\BA'), 'bb': (BAB, r'\BAB')}

ESC = {'{': r'\{', '}': r'\}', '%': r'\%', '&': r'\&', '#': r'\#',
       '$': r'\$', '_': r'\_', '^': r'\textasciicircum{}',
       '~': r'\textasciitilde{}'}


def esc(s):
    return ''.join(ESC.get(c, c) for c in s)


_ITAL_LOWER_EXC = {'h': 0x210E}
_GREEK_ITAL = {  # standard lowercase Greek -> mathematical-italic Greek
    'α': 0x1D6FC, 'β': 0x1D6FD, 'γ': 0x1D6FE, 'δ': 0x1D6FF, 'ε': 0x1D700,
    'ζ': 0x1D701, 'η': 0x1D702, 'θ': 0x1D703, 'ι': 0x1D704, 'κ': 0x1D705,
    'λ': 0x1D706, 'μ': 0x1D707, 'ν': 0x1D708, 'ξ': 0x1D709, 'ο': 0x1D70A,
    'π': 0x1D70B, 'ρ': 0x1D70C, 'σ': 0x1D70E, 'τ': 0x1D70F, 'υ': 0x1D710,
    'φ': 0x1D711, 'χ': 0x1D712, 'ψ': 0x1D713, 'ω': 0x1D714,
}


def ital(ch):
    """Map a single ASCII/Greek letter to its Unicode mathematical-italic
    codepoint (standard math-variable convention), matching the older
    Cambria-based pipeline's own always-italic-variable rule -- STIX Two
    Math's plain-ASCII/plain-Greek cmap slots are the UPRIGHT glyphs, so
    variables must route through this to render as proper italic math
    letters (this matters most for ν, the cardinality symbol used
    throughout this course, and for φ/ψ/ρ/α/β/γ/δ function names)."""
    if ch in _ITAL_LOWER_EXC:
        return chr(_ITAL_LOWER_EXC[ch])
    if ch in _GREEK_ITAL:
        return chr(_GREEK_ITAL[ch])
    if 'a' <= ch <= 'z':
        return chr(0x1D44E + (ord(ch) - ord('a')))
    if 'A' <= ch <= 'Z':
        return chr(0x1D434 + (ord(ch) - ord('A')))
    return ch


def V(s, sz=11.04, font='c'):
    """A text run of one or more variable names, each letter italicized
    via ital(); non-letters (digits, punctuation, primes) pass through
    unchanged. Use for any math variable/identifier; use plain R() for
    function/predicate names that are printed upright (rare in this
    course) or for pure-digit/operator runs."""
    return R(''.join(ital(c) if c.isalpha() else c for c in s), sz, font)


# Multi-letter predicate/function/label names that stay UPRIGHT (roman) --
# course convention: single-letter variables are math-italic, named
# predicates/functions/operators are upright, matching the printed exam's
# own Book-Antiqua-vs-Cambria-italic distinction now folded into one font.
UPRIGHT_WORDS = [
    'Rflx', 'AntSym', 'Sym', 'Trns', 'Eqv', 'PO', 'EqvCl', 'EqvCls',
    'EqvClsss', 'HsDgrm', 'Fnc', 'Src', 'Tgt', 'Im', 'Gr', 'exp', 'ln',
    'Flr', 'Clg', 'Prm', 'Evn', 'Odd', 'mnm', 'mxm', 'Wrd', 'St', 'MltSt',
    'Lst', 'Tlg', 'Cdn', 'Cng', 'TT', 'Prp',
]
UPRIGHT_WORDS.sort(key=len, reverse=True)


def M(text, sz=11.04, font='c'):
    """Smart math-string tokenizer: scans left to right, matching known
    upright multi-letter words first (UPRIGHT_WORDS), then single ASCII
    letters get math-italicized via ital(), everything else (digits,
    operators, unicode symbols, parens, spaces) renders as-is. Returns one
    Atom (R if the whole string needed no italicizing, else HB of runs)."""
    i, n = 0, len(text)
    runs = []  # (text, italic?)
    while i < n:
        matched = None
        for w in UPRIGHT_WORDS:
            if text.startswith(w, i):
                matched = w
                break
        if matched:
            runs.append((matched, False))
            i += len(matched)
            continue
        ch = text[i]
        runs.append((ital(ch) if ch.isalpha() else ch, False))
        i += 1
    # merge adjacent runs (all are non-italic strings already, since ital()
    # was applied inline) into one string, since M itself doesn't need a
    # separate italic R-variant -- ital() already picked the right glyph.
    merged = ''.join(r[0] for r in runs)
    return R(merged, sz, font)


def fmt(v):
    return f'{v:.2f}'.rstrip('0').rstrip('.')


class Atom:
    w = 0.0
    ht = 0.0
    dp = 0.0

    def emit(self, x, y):
        return []


class R(Atom):
    """A text run in one face/size."""
    def __init__(self, text, sz=11.04, font='c'):
        self.text, self.sz, self.font = text, sz, font
        face, _ = FACES[font]
        self.w = sum(face.adv(c) for c in text) * sz
        hts = [face.extents(c)[1] for c in text if c != ' ']
        dps = [face.extents(c)[2] for c in text if c != ' ']
        self.ht = (max(hts) if hts else 0.7) * sz
        self.dp = (max(dps) if dps else 0.0) * sz

    def emit(self, x, y):
        _, cmd = FACES[self.font]
        return [f'\\TL{{{fmt(x)}}}{{{fmt(y)}}}{{{cmd}{{{fmt(self.sz)}}}'
                f'{esc(self.text)}}}']


class G(Atom):
    """A Cambria glyph by gid (variants, assembly pieces, arrows)."""
    def __init__(self, gid, sz=11.04, dy=0.0):
        self.gid, self.sz, self.dy = gid, sz, dy
        adv, ymax, ymin = CAM.gid_metrics(gid)
        self.w = adv * sz
        self.ht = ymax * sz - dy
        self.dp = -ymin * sz + dy

    def emit(self, x, y):
        return [f'\\GD{{{fmt(x)}}}{{{fmt(y + self.dy)}}}{{{fmt(self.sz)}}}'
                f'{{{self.gid}}}']


class Prime(Atom):
    """Boolean-complement prime mark (U+2032), via the STIX fallback font
    (see preamble.tex's \\PrimeFont note -- no Cambria subset in this whole
    project has this glyph). Metrics read from STIXTwoMath-Regular.otf's
    own bounds (advance 0.296em, ink 0.399-0.703em above baseline)."""
    def __init__(self, sz=11.04):
        self.sz = sz
        self.w = 0.296 * sz
        self.ht = 0.703 * sz
        self.dp = 0.0

    def emit(self, x, y):
        return [f'\\PRIME{{{fmt(x)}}}{{{fmt(y)}}}{{{fmt(self.sz)}}}']


def cvar(name, comp=False, sz=11.04):
    """A (possibly-complemented) BA math-italic variable run, e.g.
    cvar('w', True) -> w′. Complement is ALWAYS the STIX Prime atom, never
    a literal ′ inside an R() text run (CambriaM has no prime glyph at
    all -- see Prime's docstring)."""
    base = R(name, sz, font='c')
    return HB(base, Prime(sz)) if comp else base


class Kern(Atom):
    def __init__(self, w):
        self.w = w


class Raise(Atom):
    """Shift a child atom vertically (negative dy = up)."""
    def __init__(self, child, dy):
        self.child, self.dy = child, dy
        self.w = child.w
        self.ht = child.ht - dy
        self.dp = child.dp + dy

    def emit(self, x, y):
        return self.child.emit(x, y + self.dy)


class HB(Atom):
    """Horizontal box: atoms in sequence on one baseline."""
    def __init__(self, *atoms, sep=0.0):
        self.atoms = [a for a in atoms if a is not None]
        self.sep = sep
        self.w = sum(a.w for a in self.atoms) + sep * max(0, len(self.atoms) - 1)
        self.ht = max((a.ht for a in self.atoms), default=0.0)
        self.dp = max((a.dp for a in self.atoms), default=0.0)

    def emit(self, x, y):
        out, cx = [], x
        for i, a in enumerate(self.atoms):
            out += a.emit(cx, y)
            cx += a.w + (self.sep if i < len(self.atoms) - 1 else 0.0)
        return out


def smart(text, sz=11.04, font='b', mfont='c'):
    """Auto-split `text` into runs, routing each CHARACTER to whichever of
    `font`/`mfont` actually has that glyph (preferring `font`), and
    concatenating the runs via HB. Whitespace stays with the run it falls
    inside rather than forcing a split.

    Built after repeatedly hand-splitting individual English-prose-with-
    inline-math lines across gen_1b/2a/2b/3a/3b/1c_work.py (2026-08-01
    audit pass) and finding it too slow and error-prone at the volume
    this project needs -- Book Antiqua (font='b'/'bb') turns out to be
    missing far more than the earlier-known gaps (no digit 7 at all in
    'b', no 4/7/8/9 in 'bb'; missing capitals H,K,Q,U,V,W,X,Z in 'b' and
    D,J,K,Q,U,X,Z in 'bb' -- none of this was checked before adding
    prose to work sheets, only spot-checked per bug as each one surfaced)
    while Cambria (font='c', the math default) has no plain Latin letters
    at all. Checking actual glyph presence per character, rather than
    guessing "this looks like English" vs "this looks like math", is the
    only way that scales past a handful of lines.

    Use this in place of a plain `R(text, sz, font='b')` for ANY string
    that might contain a digit, a math-italic variable, or a symbol
    outside {.,:;!()'-space} -- i.e. by default, prefer this over a bare
    Book-Antiqua run unless the string is provably pure prose with no
    numerals."""
    face, _ = FACES[font]
    mface, _ = FACES[mfont]
    runs = []
    cur, cur_font = '', None
    for ch in text:
        if ch.isspace():
            if cur_font is None:
                cur_font = font
            cur += ch
            continue
        avail = font if face.gname(ch) is not None else (
            mfont if mface.gname(ch) is not None else font)
        if cur_font is None:
            cur_font = avail
        if avail != cur_font:
            runs.append((cur, cur_font))
            cur, cur_font = ch, avail
        else:
            cur += ch
    if cur:
        runs.append((cur, cur_font))
    atoms = [R(t, sz, font=f) for t, f in runs]
    return atoms[0] if len(atoms) == 1 else HB(*atoms)


class Rule(Atom):
    """Horizontal drawn line of width w at the baseline."""
    def __init__(self, w, thick=0.6):
        self.w, self.thick = w, thick
        self.ht = thick
        self.dp = 0.0

    def emit(self, x, y):
        return [f'\\DLINE{{{fmt(x)}}}{{{fmt(y)}}}{{{fmt(x + self.w)}}}'
                f'{{{fmt(y)}}}{{{fmt(self.thick)}}}']


class Frac(Atom):
    """num over den with a drawn bar; axis at -0.24*sz (Word-ish)."""
    def __init__(self, num, den, sz=11.04, pad=1.5):
        self.num, self.den, self.sz, self.pad = num, den, sz, pad
        self.bar = max(num.w, den.w) + 2 * pad
        self.w = self.bar
        axis = 0.24 * sz
        self.axis = axis
        self.num_y = -(axis + 1.8 + num.dp)      # relative baseline of num
        self.den_y = -axis + 1.8 + den.ht
        self.ht = -(self.num_y - num.ht)
        self.dp = self.den_y + den.dp

    def emit(self, x, y):
        out = []
        out += self.num.emit(x + (self.bar - self.num.w) / 2, y + self.num_y)
        out += self.den.emit(x + (self.bar - self.den.w) / 2, y + self.den_y)
        out.append(f'\\DLINE{{{fmt(x)}}}{{{fmt(y - self.axis)}}}'
                   f'{{{fmt(x + self.bar)}}}{{{fmt(y - self.axis)}}}{{0.55}}')
        return out


class VC(Atom):
    """Vertical stack of atoms, centered, whole box centered on math axis."""
    def __init__(self, rows, sz=11.04, gap=3.0):
        self.rows, self.gap = rows, gap
        self.w = max(r.w for r in rows)
        total = sum(r.ht + r.dp for r in rows) + gap * (len(rows) - 1)
        axis = 0.24 * sz
        self.ys = []
        cy = -(total / 2) - axis
        for r in rows:
            cy += r.ht
            self.ys.append(cy)
            cy += r.dp + gap
        self.ht = -(self.ys[0] - rows[0].ht)
        self.dp = self.ys[-1] + rows[-1].dp

    def emit(self, x, y):
        out = []
        for r, ry in zip(self.rows, self.ys):
            out += r.emit(x + (self.w - r.w) / 2, y + ry)
        return out


# ---- tall delimiters: variant ladders + assemblies (gid, height units) ----
LADDER = {
    '(': [(4666, 1897), (3435, 2474), (4672, 3378), (3436, 4046),
          (3437, 6052), (4684, 7612), (3438, 8880)],
    ')': [(4667, 1897), (3439, 2474), (4673, 3378), (3440, 4046),
          (3441, 6052), (4685, 7612), (3442, 8880)],
    '{': [(4668, 1907), (3421, 6083), (4688, 7546)],
    '}': [(4669, 1907), (3425, 6083), (4689, 7546)],
}
ASM = {'(': (1735, 1736, 1737), ')': (1738, 1739, 1740),
       '{': (1747, 1750, 1748, 1750, 1749), '}': (1751, 1750, 1752, 1750, 1753)}


class Delim(Atom):
    """Tall delimiter covering ink height h, centered on center offset yc
    (page-coords offset from baseline; negative = above). Rendered via
    \\TDEL (math-mode \\left/\\right sized to a forced strut) -- see the
    DELIM_CMD/emit note below for why, not via LADDER/ASM gid lookup.

    Width estimate: LaTeX's \\left...\\right AUTO-SCALES a delimiter's
    rendered WIDTH along with its forced height (a tall paren is visibly
    wider than a short one, same as Word's own tall parens) -- a plain
    single-glyph advance width badly underestimates this for any h much
    bigger than the base font size, which caused real, confirmed overlap
    (a wrap()'d bracket's true ink ran into whatever HB-sibling content
    was placed right after it, using the too-small nominal width to
    compute that sibling's x-offset). 0.30*h is an empirical fit, not a
    derivation -- re-check against a render if a future delimiter looks
    mis-spaced either direction."""
    def __init__(self, ch, h, yc, sz=11.04):
        self.ch, self.h, self.yc, self.sz = ch, h, yc, sz
        self.ht = -yc + h / 2
        self.dp = yc + h / 2
        base_w = R('(' if ch in ('(', ')') else ch, sz).w
        self.w = max(base_w, 0.45 * h)

    # DELIM_CMD/emit: 2A's font subset has a DIFFERENT internal glyph
    # ordering than 1C's -- the LADDER/ASM gids above were calibrated
    # against 1C's specific merged font and render as *wrong, unrelated
    # glyphs* (confirmed by render: produced readable-looking but bogus
    # text like stray "phi(n)9)" fragments in place of a plain tall paren)
    # when applied to 2A's font. Route through the same math-mode \TDEL
    # mechanism gen2.py already uses for the printed pages instead of a
    # hardcoded GID lookup -- \TDEL resolves via the loaded math font's own
    # MATH table (unicode-math), which is robust across different subsets.
    DELIM_CMD = {'(': '(', ')': ')', '{': r'\{', '}': r'\}', '|': r'\vert'}

    def emit(self, x, y):
        d = self.DELIM_CMD.get(self.ch, self.ch)
        half = self.h / 2
        return [f'\\TDEL{{{fmt(x)}}}{{{fmt(y + self.yc)}}}{{{fmt(self.sz)}}}'
                f'{{{fmt(half)}}}{{{fmt(half)}}}{{{d}}}']


def center_in_gap(left_end_x, right_start_x, y, text, sz, font='c',
                   pad=1.5, min_sz=6.0):
    """Center `text` in the horizontal gap between two already-printed
    tokens' measured edges -- for filling a connective/relation symbol into
    a blank whose neighbors are already traced from the source PDF, rather
    than computing a generic column layout. (2B answer layer, promoted here
    after 1a/1b both needed it.)

    Shrinks to fit if the requested size doesn't leave `pad` clearance on
    each side, down to `min_sz` -- found necessary because C8=IFF renders
    as a-double-headed arrow glyph (~13bp wide at 11.04pt) roughly TWICE
    the width of C1-C7's single-char AND/OR glyphs (~6.5bp), so a gap
    sized generously enough for one is not automatically enough for the
    other; confirmed by zooming actual rendered ink, not just checking the
    nominal gap width -- several C8 fills on 1b's table header/decision
    line were genuinely overlapping their neighbors at the naive size."""
    avail = right_start_x - left_end_x - 2 * pad
    a = R(text, sz, font=font)
    if a.w > avail and avail > 0:
        sz = max(min_sz, sz * avail / a.w)
        a = R(text, sz, font=font)
    x = left_end_x + (right_start_x - left_end_x - a.w) / 2
    return a.emit(x, y)


def circle_token(x0, x1, y, sz, rx_pad=2.0, ry=7.5):
    """Draw an answer-circle around an already-printed token spanning
    [x0,x1] at baseline y, sized sz -- for the Vld/Tlg/Cdn/Cng Y-N-Pf-W
    choice convention (circle exactly one of each independent pair)."""
    cx = (x0 + x1) / 2
    rx = (x1 - x0) / 2 + rx_pad
    cy = y - 0.30 * sz
    return [f'\\CIRC{{{fmt(cx)}}}{{{fmt(cy)}}}{{{fmt(rx)}}}{{{fmt(ry)}}}']


def wrap(content, l='(', r=')', sz=11.04, tight=1.0):
    """content flanked by tall delimiters sized to its ink."""
    h = content.ht + content.dp + 2 * tight
    yc = (content.dp - content.ht) / 2
    return HB(Delim(l, h, yc, sz), Kern(0.5), content, Kern(0.5),
              Delim(r, h, yc, sz))


class Drawn(Atom):
    """Free-drawn element: list of (x0,y0,x1,y1,w) segments and optional
    filled dots (x,y,r), coordinates relative to baseline-left."""
    def __init__(self, w, ht, dp, segs=(), dots=()):
        self.w, self.ht, self.dp = w, ht, dp
        self.segs, self.dots = segs, dots

    def emit(self, x, y):
        out = []
        for (x0, y0, x1, y1, lw) in self.segs:
            out.append(f'\\DLINE{{{fmt(x + x0)}}}{{{fmt(y + y0)}}}'
                       f'{{{fmt(x + x1)}}}{{{fmt(y + y1)}}}{{{fmt(lw)}}}')
        for (dx, dy, r) in self.dots:
            out.append(f'\\fill ($(current page.north west)+({fmt(x + dx)}bp,'
                       f'-{fmt(y + dy)}bp)$) circle [radius={fmt(r)}bp];')
        return out


def larrow(sz=11.04, ln=13.0):
    """drawn long-left-arrow (subset lacks U+27F5)."""
    a = 0.26 * sz
    return Drawn(ln, a + 1, a - 2,
                 segs=[(0.5, -a, ln, -a, 0.6),
                       (0.5, -a, 3.2, -a - 2.2, 0.6),
                       (0.5, -a, 3.2, -a + 2.2, 0.6)])


def cdots(sz=11.04):
    a = 0.24 * sz
    return Drawn(9.0, a + 1, 0,
                 dots=[(1.5, -a, 0.55), (4.5, -a, 0.55), (7.5, -a, 0.55)])


def notin(sz=11.04):
    base = R('∈', sz)
    slash = Drawn(0, 0, 0, segs=[(base.w * 0.78, -base.ht - 1.2,
                                  base.w * 0.2, base.dp + 1.8, 0.55)])
    return HB(HBover(base, slash))


class HBover(Atom):
    """Two atoms drawn at the same origin (overlay)."""
    def __init__(self, *atoms):
        self.atoms = atoms
        self.w = max(a.w for a in atoms)
        self.ht = max(a.ht for a in atoms)
        self.dp = max(a.dp for a in atoms)

    def emit(self, x, y):
        out = []
        for a in self.atoms:
            out += a.emit(x, y)
        return out


def sup(base, script):
    return HB(base, Kern(0.5), Raise(script, -0.42 * 11.04))


def subs(base, script):
    return HB(base, Kern(0.3), Raise(script, 0.18 * 11.04))


class Chevrons(Atom):
    """Substitution witness: stacked assignment rows inside drawn ⟨ ⟩."""
    def __init__(self, rows, gap=3.5):
        self.inner = rows[0] if len(rows) == 1 else VC(rows, gap=gap)
        h = self.inner.ht + self.inner.dp + 4
        self.h = h
        self.cw = 4.2
        self.w = self.cw + 2.5 + self.inner.w + 2.5 + self.cw
        self.ht = self.inner.ht + 2
        self.dp = self.inner.dp + 2

    def emit(self, x, y):
        yc = y + (self.dp - self.ht) / 2
        out = [f'\\DLINE{{{fmt(x + self.cw)}}}{{{fmt(yc - self.h / 2)}}}'
               f'{{{fmt(x)}}}{{{fmt(yc)}}}{{0.55}}',
               f'\\DLINE{{{fmt(x)}}}{{{fmt(yc)}}}'
               f'{{{fmt(x + self.cw)}}}{{{fmt(yc + self.h / 2)}}}{{0.55}}']
        out += self.inner.emit(x + self.cw + 2.5, y)
        xr = x + self.w
        out += [f'\\DLINE{{{fmt(xr - self.cw)}}}{{{fmt(yc - self.h / 2)}}}'
                f'{{{fmt(xr)}}}{{{fmt(yc)}}}{{0.55}}',
                f'\\DLINE{{{fmt(xr)}}}{{{fmt(yc)}}}'
                f'{{{fmt(xr - self.cw)}}}{{{fmt(yc + self.h / 2)}}}{{0.55}}']
        return out


def assign(var_atom, expr_atom, sz=11.04):
    return HB(var_atom, Kern(2.5), larrow(sz), Kern(2.5), expr_atom)


def ditto(sz=11.04):
    return Chevrons([R('"', sz)])


class Chain(Atom):
    """Aligned equality chain: first line bare, later lines lead with the
    relation sign, all signs in one left column."""
    def __init__(self, first, steps, sz=11.04, gap=7.0, rowgap=7.0,
                 rel='=', indent=None):
        eqw = R(rel, sz).w
        self.sz, self.gap = sz, gap
        self.rows = []          # (sign_atom|None, atom)
        self.rows.append((None, first))
        for s in steps:
            sign = rel if not isinstance(s, tuple) else s[0]
            atom = s if not isinstance(s, tuple) else s[1]
            self.rows.append((R(sign, sz), atom))
        self.x_expr = eqw + gap if indent is None else indent
        self.ys = []
        cy = 0.0
        prev_dp = None
        for sign, a in self.rows:
            if prev_dp is not None:
                cy += max(prev_dp + a.ht + rowgap, 16.0)
            self.ys.append(cy)
            prev_dp = a.dp
        self.w = max(self.x_expr + a.w for _, a in self.rows)
        self.ht = self.rows[0][1].ht
        self.dp = self.ys[-1] + self.rows[-1][1].dp

    def emit(self, x, y):
        out = []
        for (sign, a), ry in zip(self.rows, self.ys):
            if sign is not None:
                out += sign.emit(x, y + ry)
            out += a.emit(x + self.x_expr, y + ry)
        return out


class Infer(Atom):
    """premises over a bar over conclusion, witness chevron right of bar."""
    def __init__(self, premise, conclusion, witness=None, pad=4.0, gap=3.2):
        self.premise, self.conclusion, self.witness = premise, conclusion, witness
        self.bar = max(premise.w, conclusion.w) + 2 * pad
        self.gap = gap
        self.prem_y = -(gap + 0.8 + premise.dp)
        self.conc_y = gap + conclusion.ht
        self.w = self.bar + ((witness.w + 6) if witness else 0)
        self.ht = -(self.prem_y - premise.ht)
        self.dp = self.conc_y + conclusion.dp
        if witness:
            self.ht = max(self.ht, witness.ht)
            self.dp = max(self.dp, witness.dp)

    def emit(self, x, y):
        out = []
        out += self.premise.emit(x + (self.bar - self.premise.w) / 2,
                                 y + self.prem_y)
        out.append(f'\\DLINE{{{fmt(x)}}}{{{fmt(y)}}}'
                   f'{{{fmt(x + self.bar)}}}{{{fmt(y)}}}{{0.6}}')
        out += self.conclusion.emit(x + (self.bar - self.conclusion.w) / 2,
                                    y + self.conc_y)
        if self.witness:
            out += self.witness.emit(x + self.bar + 6, y)
        return out


class BarStack(Atom):
    """rows separated by bars (3a piece style): r0 / bar / r1 / bar / ..."""
    def __init__(self, rows, witnesses=None, pad=4.0, gap=3.2):
        self.rows = rows
        self.wit = witnesses or {}
        self.bar = max(r.w for r in rows) + 2 * pad
        self.ys, self.bys = [], []
        cy = 0.0
        for i, r in enumerate(rows):
            if i:
                cy += gap + 0.8 + r.ht
            self.ys.append(cy)
            if i < len(rows) - 1:
                cy += r.dp + gap
                self.bys.append(cy)
        self.w = self.bar + max([self.wit[k].w + 6 for k in self.wit], default=0)
        self.ht = rows[0].ht
        self.dp = self.ys[-1] + rows[-1].dp

    def emit(self, x, y):
        out = []
        for r, ry in zip(self.rows, self.ys):
            out += r.emit(x + (self.bar - r.w) / 2, y + ry)
        for i, by in enumerate(self.bys):
            out.append(f'\\DLINE{{{fmt(x)}}}{{{fmt(y + by)}}}'
                       f'{{{fmt(x + self.bar)}}}{{{fmt(y + by)}}}{{0.6}}')
            if i in self.wit:
                wa = self.wit[i]
                out += wa.emit(x + self.bar + 6, y + by)
        return out


def strike(atom, extend=1.2):
    """cancellation stroke through an atom (bottom-left to top-right)."""
    seg = (- extend, atom.dp * 0.4 + 1.5, atom.w + extend,
           -atom.ht * 0.75 - 1.0, 0.55)
    return HBover(atom, Drawn(atom.w, atom.ht, atom.dp, segs=[seg]))


def binom(top, bot, sz=11.04):
    """binomial coefficient: top over bot in tall parens, no bar."""
    if isinstance(top, str):
        top = R(top, sz)
    if isinstance(bot, str):
        bot = R(bot, sz)
    return wrap(VC([top, bot], sz=sz, gap=2.5), sz=sz)


def mltnom(top, bots, sz=11.04, bgap=6.0):
    """multinomial: top centered over a row of bottom entries."""
    if isinstance(top, str):
        top = R(top, sz)
    row = HB(*[R(b, sz) if isinstance(b, str) else b for b in bots], sep=bgap)
    return wrap(VC([top, row], sz=sz, gap=2.5), sz=sz)


def chain_vbar(chain, x, y, skip_first=1, x_offset=-8.0):
    """A single vertical DLINE spanning the given rows of a Chain (by
    index into chain.ys), matching the printed exam's own convention for
    a stack of OR'd/summed alternatives bracketed by one left-hand bar
    (e.g. phi = phi1 v ... v phi6, one term per row, bar spanning all of
    them). skip_first=1 starts the bar at the row after the chain's own
    opening line (index 1), which is the usual case."""
    y0 = y + chain.ys[skip_first] - chain.rows[skip_first][1].ht + 1.0
    y1 = y + chain.ys[-1] + chain.rows[-1][1].dp - 2.0
    bx = x + x_offset
    return [f'\\DLINE{{{fmt(bx)}}}{{{fmt(y0)}}}{{{fmt(bx)}}}{{{fmt(y1)}}}{{0.6}}']
