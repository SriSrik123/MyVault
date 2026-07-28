#!/usr/bin/env python3
"""Feedback pass: compare rendered TDEL/bigcup ink in build/main.pdf with the
original, then rewrite the lines (anchor x/y + strut) to close the gap."""
import fitz, re, glob
from inklib import tall_groups

ORIG = "/Users/sri/Documents/MyVault/second-brain/notes/summer-2026/discrete-math-ccp/assignments/163Exm1B.pdf"
MINE = "build/main.pdf"

def ink_xstart(pix, scale, x, ylo, yhi):
    """First dark column at or right of x-6, within rows [ylo,yhi]."""
    w, h = pix.width, pix.height
    iy0, iy1 = max(0, int(ylo*scale)), min(h-1, int(yhi*scale))
    for ix in range(max(0, int((x-6)*scale)), min(w-1, int((x+10)*scale))):
        for iy in range(iy0, iy1):
            if pix.samples[iy*w + ix] < 128:
                return ix/scale
    return None

def uni_extent(pix, scale, x, y, sz):
    """Vertical ink extent of the big-union glyph near (x, y)."""
    from inklib import ink_extent
    return ink_extent(pix, scale, x+1, x+sz*1.15, y, sz)

o_doc, m_doc = fitz.open(ORIG), fitz.open(MINE)
tpat = re.compile(r"\\TDEL\{([\d.]+)\}\{([\d.]+)\}\{([\d.]+)\}\{([\d.-]+)\}\{([\d.-]+)\}\{(.+)\}$")
upat = re.compile(r"\\MT\{([\d.]+)\}\{([\d.]+)\}\{([\d.]+)\}\{(\\displaystyle|\\textstyle)\\bigcup\}$")
total = 0
for path in sorted(glob.glob("build/pages/page*.tex")):
    folio = int(re.search(r"page(\d+)", path).group(1))
    pn = folio - 200
    lines = open(path).read().splitlines()
    if not any(tpat.search(ln) or upat.search(ln) for ln in lines):
        continue
    og = tall_groups(o_doc[pn])
    mg = tall_groups(m_doc[pn])
    opix = o_doc[pn].get_pixmap(dpi=300, colorspace=fitz.csGRAY)
    mpix = m_doc[pn].get_pixmap(dpi=300, colorspace=fitz.csGRAY)
    S = 300/72.0
    out = []
    for ln in lines:
        tm = tpat.search(ln)
        um = upat.search(ln)
        if tm:
            x, y, sz, H, D, delim = (float(tm.group(1)), float(tm.group(2)),
                                     float(tm.group(3)), float(tm.group(4)),
                                     float(tm.group(5)), tm.group(6))
            tgt = min(og, key=lambda g: abs(g[0]-x) + 0.5*abs((g[1]+g[2])/2 - y),
                      default=None)
            ren = min(mg, key=lambda g: abs(g[0]-x) + 0.5*abs((g[1]+g[2])/2 - y),
                      default=None)
            if (not tgt or not ren or abs(tgt[0]-x) > 5
                    or abs((tgt[1]+tgt[2])/2 - y) > 30
                    or abs((ren[1]+ren[2])/2 - y) > 30):
                out.append(ln); continue
            tc, tmid = (tgt[1]+tgt[2])/2, (tgt[2]-tgt[1])/2
            rc, rmid = (ren[1]+ren[2])/2, (ren[2]-ren[1])/2
            dy, dm = tc - rc, tmid - rmid
            # horizontal: align first ink column
            ox = ink_xstart(opix, S, tgt[0], tc-tmid*0.5, tc+tmid*0.5)
            mx = ink_xstart(mpix, S, ren[0], rc-rmid*0.5, rc+rmid*0.5)
            dx = (ox - mx) if (ox is not None and mx is not None) else 0.0
            if abs(dy) < 0.6 and abs(dm) < 0.8 and abs(dx) < 0.6:
                out.append(ln); continue
            dm = max(-3.0, min(3.0, dm)); dy = max(-6, min(6, dy)); dx = max(-1.5, min(1.5, dx))
            out.append(f"\\TDEL{{{x+dx:.2f}}}{{{y+dy:.2f}}}{{{sz:g}}}"
                       f"{{{H+dm:.2f}}}{{{D+dm:.2f}}}{{{delim}}}")
            total += 1
        elif um:
            x, y, sz, style = (float(um.group(1)), float(um.group(2)),
                               float(um.group(3)), um.group(4))
            oe = uni_extent(opix, S, x, y, sz)
            me = uni_extent(mpix, S, x, y, sz)
            if not oe or not me:
                out.append(ln); continue
            dy = (oe[0]+oe[1])/2 - (me[0]+me[1])/2
            if abs(dy) < 0.6:
                out.append(ln); continue
            out.append(f"\\MT{{{x:.2f}}}{{{y+max(-6,min(6,dy)):.2f}}}{{{sz:g}}}{{{style}\\bigcup}}")
            total += 1
        else:
            out.append(ln)
    open(path, "w").write("\n".join(out) + "\n")
print("adjusted:", total)
