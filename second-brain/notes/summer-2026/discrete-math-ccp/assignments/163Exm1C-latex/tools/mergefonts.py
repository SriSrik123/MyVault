#!/usr/bin/env python3
"""Fill the 1C Cambria subsets' empty glyphs from the 1B subset.

PDF TrueType subsets keep the source font's glyph numbering (empty outlines
for unpainted glyphs), so the 1B exam's subset can donate outlines the 1C
exam never painted (math-italic a/c, ∃, α, φ, …) at the SAME gids — existing
\\GD{…}{gid} calls and painted-page rendering are untouched.

Writes fonts/CambriaM.ttf (from CambriaMath_22) and fonts/CambriaM_nokern.ttf
(from CambriaMath_nokern).  Run from the replica root.
"""
import copy
from fontTools.ttLib import TTFont

DONOR = "../163Exm1B-latex/fonts/CambriaMath_22.ttf"
JOBS = [("fonts/CambriaMath_22.ttf", "fonts/CambriaM.ttf"),
        ("fonts/CambriaMath_nokern.ttf", "fonts/CambriaM_nokern.ttf")]
# chars the 1C answers need that only the 1B subset outlines
NEEDED_CP = [0x1D44E, 0x1D450, 0x1D6FC, 0x1D711, 0x2203]  # a c α φ ∃
# glyphs 1C paints but does not cmap — map them so text/math input works too
EXTRA_CMAP = {0x27F6: 3639, 0x27FC: 3645, 0x2236: 1527}


def empty(g):
    return g.numberOfContours == 0 and not g.isComposite()


donor = TTFont(DONOR)
d_glyf, d_hmtx = donor['glyf'], donor['hmtx']
d_order = donor.getGlyphOrder()
d_index = {gn: i for i, gn in enumerate(d_order)}
d_cmap = donor.getBestCmap()


def closure(gid, acc):
    if gid in acc:
        return
    acc.add(gid)
    g = d_glyf[d_order[gid]]
    if g.isComposite():
        for comp in g.components:
            closure(d_index[comp.glyphName], acc)


todo = set()
for cp in NEEDED_CP:
    gn = d_cmap.get(cp)
    if gn is None:
        print(f"donor lacks U+{cp:04X}")
        continue
    closure(d_index[gn], todo)

for src, dst in JOBS:
    f = TTFont(src)
    glyf, hmtx = f['glyf'], f['hmtx']
    order = f.getGlyphOrder()
    n = min(len(order), len(d_order))
    filled = 0
    for gid in sorted(todo):
        if gid >= n or not empty(glyf[order[gid]]):
            continue
        g = copy.deepcopy(d_glyf[d_order[gid]])
        if g.isComposite():          # component refs are by NAME — translate
            for comp in g.components:
                comp.glyphName = order[d_index[comp.glyphName]]
        glyf[order[gid]] = g
        hmtx[order[gid]] = d_hmtx[d_order[gid]]
        filled += 1
    additions = {}
    for cp in NEEDED_CP:
        gn = d_cmap.get(cp)
        if gn and d_index[gn] < n:
            additions[cp] = order[d_index[gn]]
    for cp, gid in EXTRA_CMAP.items():
        if gid < n:
            additions[cp] = order[gid]
    has12 = any(t.format == 12 for t in f['cmap'].tables)
    for table in f['cmap'].tables:
        if not table.isUnicode():
            continue
        for cp, gn in additions.items():
            if cp in table.cmap:
                continue
            if table.format == 12 or cp <= 0xFFFF:
                table.cmap[cp] = gn
    if not has12 and any(cp > 0xFFFF for cp in additions):
        # build a format-12 subtable carrying the full union mapping
        from fontTools.ttLib.tables._c_m_a_p import CmapSubtable
        full = dict(f.getBestCmap())
        full.update(additions)
        sub = CmapSubtable.newSubtableClass(12)(12)
        sub.platformID, sub.platEncID, sub.language = 3, 10, 0
        sub.cmap = full
        f['cmap'].tables.append(sub)
    f.save(dst)
    print(f"{dst}: filled {filled} glyphs, mapped {len(additions)} chars")
