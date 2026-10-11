#!/usr/bin/env python3
"""Replace \\TDEL forced-delimiter lines with exact glyph placements (\\GD).

\\left/\\right picks Cambria size variants from strut heights, which is
unstable when many nested delimiters sit close together (wrong size class,
gapped assemblies, fixdel mispairing).  Instead: read the ORIGINAL PDF's
delimiter chars — a size variant paints as '('/')'/... whose variant we
identify by measured ink height; an assembly paints as U+239B.. piece chars
with their own pen origins — and emit the same glyph ids at the same pen
positions via \\XeTeXglyph.  Same subset font file => identical rendering.

Run from the replica root:  python3 tools/fixglyph.py 302 303 304
"""
import fitz, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ORIG = "/Users/sri/Documents/MyVault/second-brain/notes/summer-2026/discrete-math-ccp/assignments/163Exm1C.pdf"
FOLIO0 = 300
UPM = 2048.0

# vertical variant ladders from CambriaMath_22.ttf's MATH table (glyph ids;
# empty-in-subset variants omitted).  Outline bboxes are read from the font.
LADDER = {
    '(': [4666, 3435, 4672, 3436, 3437, 4684, 3438],
    ')': [4667, 3439, 4673, 3440, 3441, 4685, 3442],
    '{': [4668, 3421, 4688],
    '}': [4669, 3425, 4689],
    '|': [513, 4698, 3629, 4718],
}


def load_bboxes():
    from fontTools.ttLib import TTFont
    f = TTFont(os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "fonts", "CambriaMath_22.ttf"))
    glyf, order = f['glyf'], f.getGlyphOrder()
    out = {}
    for gid in [g for gids in LADDER.values() for g in gids] + PIECE_GIDS:
        g = glyf[order[gid]]
        out[gid] = (g.yMin, g.yMax) if g.numberOfContours else (0, 0)
    return out


PIECE_GIDS = list(range(1735, 1741)) + list(range(1747, 1754))
BBOX = load_bboxes()

TPAT = re.compile(r"\\TDEL\{([\d.]+)\}\{([\d.]+)\}\{([\d.]+)\}"
                  r"\{([\d.-]+)\}\{([\d.-]+)\}\{(.+)\}$")
# previously-emitted variant \GD lines (re-derivable => script is idempotent)
GPAT = re.compile(r"\\GD\{([\d.]+)\}\{([\d.]+)\}\{[\d.]+\}\{\d+\}"
                  r"% (.) ink=\[([\d.-]+),([\d.-]+)\]$")
DNORM = {'vert': '|', 'lvert': '|', 'rvert': '|',
         'lbrace': '{', 'rbrace': '}'}


# which glyph ids count as tall-delimiter material (variants + assembly
# pieces; nominal-size base glyphs are set in the \CT text runs, not TDELs)
VARIANT_CH = {}
for _ch, _gids in LADDER.items():
    for _g in _gids[1:]:                 # skip the base (nominal) glyph
        VARIANT_CH[_g] = _ch
PIECE_CH = {1735: '(', 1736: '(', 1737: '(',
            1738: ')', 1739: ')', 1740: ')',
            1747: '{', 1748: '{', 1749: '{',
            1751: '}', 1752: '}', 1753: '}'}
# extender 1750 serves both braces — resolve by x-proximity when chaining
PIECE_ANY = {**PIECE_CH, 1750: None}


def clusters_for_page(page):
    """Original page's tall delimiters from texttrace glyph ids:
    [{'ch','x','yc','ytop','ybot','kind','runs':[(gid,x,y,size),..]}]"""
    raw = []
    for span in page.get_texttrace():
        if 'Cambria' not in span['font']:
            continue
        sz = span['size']
        for uni, gid, origin, bbox in span['chars']:
            if gid in VARIANT_CH:
                raw.append(('variant', VARIANT_CH[gid], gid,
                            origin[0], origin[1], sz))
            elif gid in PIECE_ANY:
                raw.append(('piece', PIECE_ANY[gid], gid,
                            origin[0], origin[1], sz))
    out = []
    for kind, ch, gid, x, y, sz in sorted(raw, key=lambda r: (round(r[3]), r[4])):
        ymin, ymax = BBOX[gid]
        ytop = y - ymax * sz / UPM
        ybot = y - ymin * sz / UPM
        if kind == 'variant':
            out.append({'ch': ch, 'x': x, 'ybase': y, 'ytop': ytop,
                        'ybot': ybot, 'yc': (ytop + ybot) / 2,
                        'size': sz, 'kind': 'variant', 'gid': gid})
            continue
        # chain pieces at the same x whose extents touch into one delimiter
        g = next((cl for cl in out if cl['kind'] == 'pieces'
                  and abs(cl['x'] - x) < 1.0 and ytop < cl['ybot'] + 3
                  and ybot > cl['ytop'] - 3
                  and (ch is None or cl['ch'] is None or cl['ch'] == ch)), None)
        if g is None:
            g = {'ch': ch, 'x': x, 'ytop': ytop, 'ybot': ybot,
                 'yc': (ytop + ybot) / 2, 'size': sz,
                 'kind': 'pieces', 'runs': []}
            out.append(g)
        g['runs'].append((gid, x, y, sz))
        g['ch'] = g['ch'] or ch
        g['ytop'] = min(g['ytop'], ytop)
        g['ybot'] = max(g['ybot'], ybot)
        g['yc'] = (g['ytop'] + g['ybot']) / 2
    return out


def main(folios):
    doc = fitz.open(ORIG)
    grand = 0
    for folio in folios:
        path = f"pages/page{folio}.tex"
        cl = clusters_for_page(doc[folio - FOLIO0])
        used = set()
        lines = open(path).read().splitlines()
        out, n_var, n_asm, warn = [], 0, 0, 0
        for ln in lines:
            m = TPAT.search(ln)
            g = GPAT.search(ln) if not m else None
            if not m and not g:
                out.append(ln)
                continue
            if m:
                x, y = float(m.group(1)), float(m.group(2))
                H, D = float(m.group(4)), float(m.group(5))
                delim = DNORM.get(m.group(6).lstrip('\\'),
                                  m.group(6).lstrip('\\'))
                yc_est = y - (H - D) / 2
            else:
                x, delim = float(g.group(1)), g.group(3)
                yc_est = (float(g.group(4)) + float(g.group(5))) / 2
            if delim not in LADDER:
                print(f"  {path}: unknown delimiter '{delim}' — left as is")
                out.append(ln)
                warn += 1
                continue
            cand = [(i, c) for i, c in enumerate(cl)
                    if i not in used and c['ch'] == delim
                    and abs(c['x'] - x) < 8 and abs(c['yc'] - yc_est) < 30]
            if not cand:
                print(f"  {path}: NO MATCH for TDEL x={x} y={y} '{delim}'")
                out.append(ln)
                warn += 1
                continue
            i, c = min(cand, key=lambda ic: abs(ic[1]['x'] - x)
                       + 0.3 * abs(ic[1]['yc'] - yc_est))
            used.add(i)
            if c['kind'] == 'variant':
                out.append(f"\\GD{{{c['x']:.2f}}}{{{c['ybase']:.2f}}}"
                           f"{{{c['size']:g}}}{{{c['gid']}}}"
                           f"% {delim} ink=[{c['ytop']:.1f},{c['ybot']:.1f}]")
                n_var += 1
            else:
                for gid, px, py, psz in c['runs']:
                    out.append(f"\\GD{{{px:.2f}}}{{{py:.2f}}}"
                               f"{{{psz:g}}}{{{gid}}}% {delim}-piece")
                n_asm += 1
        open(path, "w").write("\n".join(out) + "\n")
        unmatched = [c for i, c in enumerate(cl) if i not in used]
        print(f"page{folio}: {n_var} variants, {n_asm} assemblies, "
              f"{warn} warnings, {len(unmatched)} orig clusters unmatched")
        for c in unmatched:
            print(f"   unmatched orig {c['ch']} x={c['x']:.1f} yc={c['yc']:.1f}")
        grand += n_var + n_asm
    print("converted:", grand)


if __name__ == "__main__":
    main([int(a) for a in sys.argv[1:]] or [302, 303, 304])
