#!/usr/bin/env python3
"""Render orig & replica pages, save side-by-side and overlay-diff images.
Run from the replica root: python3 tools/compare.py 0 1 2 ...  (pdf page index)"""
import fitz, sys, os
from PIL import Image, ImageChops
orig = fitz.open("/Users/sri/Documents/MyVault/second-brain/notes/summer-2026/discrete-math-ccp/assignments/163Exm2C.pdf")
mine = fitz.open("main.pdf")
os.makedirs("cmp", exist_ok=True)
dpi = int(os.environ.get("DPI", "96"))
def topil(pix):
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
for pn in [int(a) for a in sys.argv[1:]]:
    po = topil(orig[pn].get_pixmap(dpi=dpi))
    pm = topil(mine[pn].get_pixmap(dpi=dpi))
    if pm.size != po.size: pm = pm.resize(po.size)
    w, h = po.size
    sbs = Image.new("RGB", (w*2+6, h), (128,128,128))
    sbs.paste(po, (0,0)); sbs.paste(pm, (w+6,0))
    sbs.save(f"cmp/sbs{pn:02d}.png")
    # overlay: original in RED channel, mine in BLUE channel -> black where both have ink,
    # red = only original, blue = only replica
    go, gm = po.convert("L"), pm.convert("L")
    ov = Image.merge("RGB", (gm, ImageChops.lighter(go, gm), go))
    ov.save(f"cmp/ov{pn:02d}.png")
    # numeric diff score
    diff = ImageChops.difference(go, gm)
    bbox = diff.getbbox()
    hist = diff.histogram()
    bad = sum(hist[32:])
    print(f"page {pn}: diff-pixels(>32)={bad} bbox={bbox}")
