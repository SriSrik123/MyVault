#!/usr/bin/env python3
"""Fill 2A's Cambria subset's empty glyphs from 1B's subset (which has full
ASCII digit coverage, confirmed by direct cmap check 2026-07-30 -- 2A's own
raw extraction is missing 4,5,6,7,9 entirely, since the blank exam never
happens to print those digits anywhere in Cambria text runs).

Same mechanism as 163Exm1C-latex/tools/mergefonts.py (PDF TrueType subsets
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
# ASCII digits 2A's own subset never painted, needed for nearly every
# numeral answer (a,b,c,d values, coefficients, roots, ...), plus
# math-italic P (U+1D443) -- needed for induction-proof predicate P(n),
# never printed anywhere on the blank exam so never in the base extraction.
NEEDED_CP = [ord(c) for c in "456790"] + [0x1D443]
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

# ---- Book Antiqua: capital 'B' never printed anywhere on the blank exam
# (needed for the induction-proof label 'BC'), so it's missing from both
# the regular and bold subsets. Same donor-fill mechanism, separate donor
# font (Book Antiqua, not Cambria Math), writing back to the SAME
# filenames in place -- safe, since this only fills previously-EMPTY
# glyphs and never touches ones the printed page already paints.
BA_JOBS = [("fonts/BookAntiqua_5.ttf", "../163Exm1B-latex/fonts/BookAntiqua_5.ttf"),
           ("fonts/BookAntiqua-Bold_11.ttf", "../163Exm1B-latex/fonts/BookAntiqua-Bold_11.ttf")]
BA_NEEDED_CP = [ord('B')]

for dst_src, ba_donor_path in BA_JOBS:
    ba_donor = TTFont(ba_donor_path)
    bd_glyf = ba_donor['glyf']
    bd_order = ba_donor.getGlyphOrder()
    bd_index = {gn: i for i, gn in enumerate(bd_order)}
    bd_cmap = ba_donor.getBestCmap()
    ba_todo = set()
    for cp in BA_NEEDED_CP:
        gn = bd_cmap.get(cp)
        if gn is None:
            print(f"BA donor lacks U+{cp:04X}")
            continue
        acc = set()

        def bclosure(gid):
            if gid in acc:
                return
            acc.add(gid)
            g = bd_glyf[bd_order[gid]]
            if g.isComposite():
                for comp in g.components:
                    bclosure(bd_index[comp.glyphName])
        bclosure(bd_index[gn])
        ba_todo |= acc

    f = TTFont(dst_src)
    glyf, hmtx = f['glyf'], f['hmtx']
    order = f.getGlyphOrder()
    n = min(len(order), len(bd_order))
    filled = 0
    for gid in sorted(ba_todo):
        if gid >= n or not empty(glyf[order[gid]]):
            continue
        g = copy.deepcopy(bd_glyf[bd_order[gid]])
        if g.isComposite():
            for comp in g.components:
                comp.glyphName = order[bd_index[comp.glyphName]]
        glyf[order[gid]] = g
        hmtx[order[gid]] = ba_donor['hmtx'][bd_order[gid]]
        filled += 1
    additions = {}
    for cp in BA_NEEDED_CP:
        gn = bd_cmap.get(cp)
        if gn and bd_index[gn] < n:
            additions[cp] = order[bd_index[gn]]
    for table in f['cmap'].tables:
        if not table.isUnicode():
            continue
        for cp, gn in additions.items():
            if cp not in table.cmap:
                table.cmap[cp] = gn
    f.save(dst_src)
    print(f"{dst_src}: filled {filled} glyphs (Book Antiqua donor), mapped {len(additions)} chars")
