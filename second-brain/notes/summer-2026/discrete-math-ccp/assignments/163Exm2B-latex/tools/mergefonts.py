#!/usr/bin/env python3
"""Fill 2B's Cambria subset's empty glyphs from 1B's subset (which has full
math-italic a/i/s coverage, confirmed by direct cmap check 2026-08-07 -- 2B's
own raw extraction lacks math-italic a (U+1D44E), i (U+1D456), s (U+1D460):
the blank exam prints them only inside tiny cross-reference labels like
"1a(i)" and inside 3c's own "s" variable, none of which happened to render
via a Cambria text run rich enough to pull those glyphs into the subset).

Same mechanism as 163Exm2A-latex/tools/mergefonts.py (PDF TrueType subsets
keep the source Cambria Math font's original glyph numbering, so donor and
target share GIDs for the same character even though each PDF only painted
some of them). Writes fonts/CambriaM.ttf / CambriaM_nokern.ttf. Run from the
replica root.
"""
import copy
from fontTools.ttLib import TTFont

DONOR = "../163Exm1B-latex/fonts/CambriaMath_22.ttf"
JOBS = [("fonts/CambriaMath_22.ttf", "fonts/CambriaM.ttf"),
        ("fonts/CambriaMath_nokern.ttf", "fonts/CambriaM_nokern.ttf")]
# math-italic a, i, s, plus plain digits 0 and 9 -- the latter two only
# surfaced once \FOLIO{} (preamble.tex, hardcoded through \CMT/CambriaM)
# started printing worksheet folio numbers like 5110/5120/9130 that
# happen to contain them; this exam's raw extraction has 1-8 but not 0/9,
# same "independently-subsetted, check don't assume" digit-gap class 2A
# hit for a different digit set.
NEEDED_CP = [0x1D44E, 0x1D456, 0x1D460, ord('0'), ord('9')]
EXTRA_CMAP = {}


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
        if g.isComposite():
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
        from fontTools.ttLib.tables._c_m_a_p import CmapSubtable
        full = dict(f.getBestCmap())
        full.update(additions)
        sub = CmapSubtable.newSubtableClass(12)(12)
        sub.platformID, sub.platEncID, sub.language = 3, 10, 0
        sub.cmap = full
        f['cmap'].tables.append(sub)
    f.save(dst)
    print(f"{dst}: filled {filled} glyphs, mapped {len(additions)} chars")
