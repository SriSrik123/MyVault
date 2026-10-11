#!/usr/bin/env python3
"""Parse a traced pages/pageNNN.tex and report, per visual row (tokens
clustered by y within a tolerance), each token's text/x/width and the GAP
between consecutive tokens -- so a blank's fill coordinates can be read off
directly instead of hand-computing them from the raw \\CT/\\TL call list.
Usage: python3 findgaps.py <folio> [--miny Y] [--maxy Y]
"""
import re
import sys
sys.path.insert(0, '.')
from atoms import R

CT_RE = re.compile(r'\\CT\{([-\d.]+)\}\{([-\d.]+)\}\{([-\d.]+)\}\{(.*?)\}$')
TL_RE = re.compile(r'\\TL\{([-\d.]+)\}\{([-\d.]+)\}\{\\[A-Z]+\{([-\d.]+)\}(.*?)\}$')
TDEL_RE = re.compile(
    r'\\TDEL\{([-\d.]+)\}\{([-\d.]+)\}\{([-\d.]+)\}\{([-\d.]+)\}\{([-\d.]+)\}\{(.*?)\}$')


def load(folio):
    toks = []
    with open(f'pages/page{folio}.tex', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            m = TDEL_RE.match(line)
            if m:
                x, y, sz, sh, sd, delim = (float(m.group(1)), float(m.group(2)),
                                            float(m.group(3)), float(m.group(4)),
                                            float(m.group(5)), m.group(6))
                # width estimate per atoms.Delim's own documented formula
                w = max(R('(', sz).w, 0.45 * (sh + sd))
                toks.append((x, y, sz, f'TDEL{delim}', w, 'delim'))
                continue
            m = CT_RE.match(line)
            font = 'c'
            if not m:
                m = TL_RE.match(line)
                font = 'b'
            if not m:
                continue
            x, y, sz, text = float(m.group(1)), float(m.group(2)), float(m.group(3)), m.group(4)
            text = text.replace(r'\{', '{').replace(r'\}', '}')
            w = R(text, sz, font=font).w if text.strip() else 0.0
            toks.append((x, y, sz, text, w, font))
    return toks


def main():
    folio = sys.argv[1]
    miny = float(sys.argv[sys.argv.index('--miny') + 1]) if '--miny' in sys.argv else 0
    maxy = float(sys.argv[sys.argv.index('--maxy') + 1]) if '--maxy' in sys.argv else 9999
    toks = [t for t in load(folio) if miny <= t[1] <= maxy]
    # cluster into rows by y (tolerance 3bp)
    toks.sort(key=lambda t: (t[1], t[0]))
    rows = []
    for t in toks:
        placed = False
        for row in rows:
            if abs(row[0][1] - t[1]) < 3.0:
                row.append(t)
                placed = True
                break
        if not placed:
            rows.append([t])
    for row in rows:
        row.sort(key=lambda t: t[0])
        y = row[0][1]
        print(f'--- row y={y:.2f} ---')
        prev_end = None
        for (x, ty, sz, text, w, font) in row:
            gap = f'  [GAP {prev_end:.2f}->{x:.2f} = {x - prev_end:.2f}bp]' if prev_end is not None and x - prev_end > 3 else ''
            print(f'  x={x:7.2f} end={x+w:7.2f} sz={sz:5.2f} font={font} {text!r}{gap}')
            prev_end = x + w


if __name__ == '__main__':
    main()
