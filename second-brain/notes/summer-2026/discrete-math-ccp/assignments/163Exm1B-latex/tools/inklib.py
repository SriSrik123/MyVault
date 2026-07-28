"""Shared ink-based tall-delimiter detection for original and replica PDFs."""
import fitz

ASSEMBLY = set(range(0x239B, 0x23AE))

def ink_extent(pix, scale, x0, x1, yc, size):
    w, h = pix.width, pix.height
    ix0, ix1 = max(0, int(x0*scale)), min(w-1, int(x1*scale))
    if ix1 <= ix0: return None
    samp = pix.samples
    ylo, yhi = max(0, int((yc-3.2*size)*scale)), min(h-1, int((yc+3.0*size)*scale))
    dark = []
    for iy in range(ylo, yhi):
        row = samp[iy*w + ix0: iy*w + ix1]
        dark.append(any(b < 128 for b in row))
    runs, start = [], None
    for i, d in enumerate(dark):
        if d and start is None: start = i
        if not d and start is not None:
            runs.append((start, i)); start = None
    if start is not None: runs.append((start, len(dark)))
    if not runs: return None
    ycpx = int(yc*scale) - ylo
    best = min(runs, key=lambda r: 0 if r[0] <= ycpx <= r[1]
               else min(abs(r[0]-ycpx), abs(r[1]-ycpx)))
    return ((ylo+best[0])/scale, (ylo+best[1])/scale)

def tall_groups(page, thresh=1.15):
    """[(x, ytop, ybot), ...] for delimiters whose painted ink is tall."""
    pix = page.get_pixmap(dpi=300, colorspace=fitz.csGRAY)
    scale = 300/72.0
    tall = []
    for b in page.get_text("rawdict")["blocks"]:
        if b["type"] != 0: continue
        for l in b["lines"]:
            for s in l["spans"]:
                for ch in s["chars"]:
                    c = ch["c"]
                    if not c.strip(): continue
                    if c not in "(){}[]|∣⎛⎜⎝⎞⎟⎠⎧⎨⎩⎪⎫⎬⎭": continue
                    x0, _, x1, _ = ch["bbox"]
                    ext = ink_extent(pix, scale, x0, x1, ch["origin"][1], s["size"])
                    if ext and (ext[1]-ext[0]) > thresh*s["size"]:
                        tall.append((round(ch["origin"][0],2),
                                     round(ext[0],2), round(ext[1],2)))
    groups = []
    for x, yt, yb in sorted(tall, key=lambda t: (round(t[0]), t[1])):
        g = next((gg for gg in groups
                  if abs(gg[0]-x) < 3.0 and not (yt > gg[2]+2 or yb < gg[1]-2)), None)
        if g:
            g[1] = min(g[1], yt); g[2] = max(g[2], yb)
        else:
            groups.append([x, yt, yb])
    return [g for g in groups if (g[2]-g[1]) < 80]
