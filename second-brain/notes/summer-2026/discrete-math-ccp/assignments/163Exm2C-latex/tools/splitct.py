#!/usr/bin/env python3
"""Split multi-char \\CT Cambria text runs into per-char placements at the
original PDF's own pen positions (from texttrace).

Word shapes math runs with its own kerning; XeTeX's differs by up to a couple
bp over a run, and Word sometimes nudges individual chars off the run baseline
(e.g. nominal parens raised 0.36bp).  Placing every char at its measured pen
removes the whole error class.  When the original painted a char with a
size-variant glyph id, a \\GD line is emitted instead of a \\CT char.

Run from the replica root:  python3 tools/splitct.py 302 303 ...
"""
import fitz, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixglyph import VARIANT_CH, PIECE_ANY, ORIG, FOLIO0

CPAT = re.compile(r"^\\CT\{([\d.]+)\}\{([\d.]+)\}\{([\d.]+)\}\{(.*)\}$")
UNESC = {'\\{': '{', '\\}': '}', '\\%': '%', '\\&': '&', '\\#': '#',
         '\\$': '$', '\\_': '_'}
ESC = {v: k for k, v in UNESC.items()}


def untex(s):
    out, i = [], 0
    while i < len(s):
        if s[i] == '\\' and i + 1 < len(s) and s[i:i+2] in UNESC:
            out.append(UNESC[s[i:i+2]])
            i += 2
        else:
            out.append(s[i])
            i += 1
    return out


def chars_for_page(page):
    """All Cambria chars in paint order: (char, gid, x, y, size)."""
    out = []
    for span in page.get_texttrace():
        if 'Cambria' not in span['font']:
            continue
        for uni, gid, origin, bbox in span['chars']:
            out.append((chr(uni), gid, origin[0], origin[1], span['size']))
    return out


def main(folios):
    doc = fitz.open(ORIG)
    for folio in folios:
        path = f"pages/page{folio}.tex"
        if not os.path.exists(path):
            continue
        stream = chars_for_page(doc[folio - FOLIO0])
        lines = open(path).read().splitlines()
        out, n_split, n_gd, warn = [], 0, 0, 0
        for ln in lines:
            m = CPAT.match(ln)
            if not m:
                out.append(ln)
                continue
            x, y, sz = float(m.group(1)), float(m.group(2)), float(m.group(3))
            text = untex(m.group(4))
            if not text or any(c == '\\' for c in text):
                out.append(ln)      # macro content — leave alone
                continue
            # find the anchor char in the paint stream
            starts = [i for i, (c, g, cx, cy, cs) in enumerate(stream)
                      if c == text[0] and abs(cx - x) < 0.6
                      and abs(cy - y) < 0.6]
            seq = None
            for s0 in starts:
                cand, j = [], s0
                ok = True
                for tc in text:
                    if j >= len(stream) or stream[j][0] != tc:
                        ok = False
                        break
                    cand.append(stream[j])
                    j += 1
                if ok:
                    seq = cand
                    break
            if seq is None:
                print(f"  {path}: no stream match for \\CT x={x} y={y} "
                      f"{''.join(text)!r} — left as one run")
                out.append(ln)
                warn += 1
                continue
            for c, gid, cx, cy, cs in seq:
                if c == ' ':
                    continue
                out.append(f"\\GD{{{cx:.2f}}}{{{cy:.2f}}}{{{cs:g}}}"
                           f"{{{gid}}}% {c}")
                n_gd += 1
            n_split += 1
        open(path, "w").write("\n".join(out) + "\n")
        print(f"page{folio}: split {n_split} runs ({n_gd} chars -> \\GD), "
              f"{warn} left unmatched")


if __name__ == "__main__":
    main([int(a) for a in sys.argv[1:]])
