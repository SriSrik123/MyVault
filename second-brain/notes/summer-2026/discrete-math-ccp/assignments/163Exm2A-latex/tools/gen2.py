#!/usr/bin/env python3
"""Generator v2 (163Exm1C): text lines (justified) + every Cambria math run
placed as a text-mode segment at its exact coordinates; tall delimiters emitted
as forced \\left-variants; big unions as display operators.
Run from the replica root; writes pages/pageNNN.tex (folios 300-320)."""
import fitz, os

SRC = "/Users/sri/Documents/MyVault/second-brain/notes/summer-2026/discrete-math-ccp/assignments/163Exm2A.pdf"
OUT = "pages"
FOLIO0 = 400
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(SRC)

AXIS = 0.25  # Cambria math axis height (em)
ASSEMBLY = set(range(0x239B, 0x23AE))
DELMAP = {"(": "(", ")": ")", "{": r"\{", "}": r"\}", "[": "[", "]": "]",
          "|": r"\vert",
          "⎛": "(", "⎜": "(", "⎝": "(",
          "⎞": ")", "⎟": ")", "⎠": ")",
          "⎧": r"\{", "⎨": r"\{", "⎩": r"\{", "⎪": r"\{",
          "⎫": r"\}", "⎬": r"\}", "⎭": r"\}",
          # 2A: floor/ceiling — the extracted font's cmap has no reachable
          # glyph for these at plain-text (\CT) shaping, so they must go
          # through math-mode \left/\right like the tall parens do.
          "⌊": r"\lfloor", "⌋": r"\rfloor", "⌈": r"\lceil", "⌉": r"\rceil"}
DELCHARS = "(){}[]|∣⌊⌋⌈⌉"

def esc_text(t):
    t = t.replace("\\", r"\textbackslash{}")
    for c in "&%$#_{}":
        t = t.replace(c, "\\" + c)
    t = t.replace("~", r"\textasciitilde{}").replace("^", r"\textasciicircum{}")
    t = t.replace("'", '\\symbol{"27}')
    return t

def fcmd(font, size):
    s = f"{size:.2f}".rstrip("0").rstrip(".")
    return {"BookAntiqua": r"\BA", "BookAntiqua-Bold": r"\BAB", "Calibri": r"\CAL",
            "SymbolMT": r"\SYM", "Helvetica": r"\HEL"}.get(font), s

def ink_extent(pix, scale, x0, x1, yc, size):
    """Vertical extent (in bp) of contiguous ink at column band [x0,x1]
    around page-y yc. Returns (ytop, ybot) or None."""
    w, h = pix.width, pix.height
    ix0, ix1 = max(0, int(x0*scale)), min(w-1, int(x1*scale))
    if ix1 <= ix0: return None
    samp = pix.samples
    dark = []
    ylo, yhi = max(0, int((yc-3.2*size)*scale)), min(h-1, int((yc+3.0*size)*scale))
    for iy in range(ylo, yhi):
        row = samp[iy*w + ix0: iy*w + ix1]
        dark.append(any(b < 128 for b in row))
    # contiguous runs
    runs, start = [], None
    for i, d in enumerate(dark):
        if d and start is None: start = i
        if not d and start is not None:
            runs.append((start, i)); start = None
    if start is not None: runs.append((start, len(dark)))
    if not runs: return None
    ycpx = int(yc*scale) - ylo
    best = min(runs, key=lambda r: 0 if r[0] <= ycpx <= r[1] else min(abs(r[0]-ycpx), abs(r[1]-ycpx)))
    return ((ylo+best[0])/scale, (ylo+best[1])/scale)

for pn in range(len(doc)):
    pg = doc[pn]
    folio = FOLIO0 + pn
    raw = pg.get_text("rawdict")
    inkpix = pg.get_pixmap(dpi=300, colorspace=fitz.csGRAY)
    SCALE = 300/72.0
    tex = [f"%% ===== page {folio} (pdf page {pn+1}) — generated; edit freely =====",
           f"\\ChromePage{{{folio}}}"]

    allchars = []   # [font, size, c, x0, y_origin, x1, ytop, ybot]
    for b in raw["blocks"]:
        if b["type"] != 0: continue
        for l in b["lines"]:
            for s in l["spans"]:
                for ch in s["chars"]:
                    x0, y0, x1, y1 = ch["bbox"]
                    allchars.append([s["font"], round(s["size"],2), ch["c"],
                                     round(ch["origin"][0],2), round(ch["origin"][1],2),
                                     round(x1,2), round(y0,2), round(y1,2)])
    allchars = [c for c in allchars
                if not (abs(c[4]-45.6) < 2 or abs(c[4]-714.5) < 2)]

    cam = [c for c in allchars if c[0] == "CambriaMath"]

    # ink-based tall-delimiter detection: PDF metadata reports variant and
    # assembly glyphs at nominal size, so measure the painted ink instead
    tall, linear = [], []
    for c in cam:
        cp = ord(c[2]) if c[2] else 0
        if c[2] in DELCHARS or cp in ASSEMBLY:
            ext = ink_extent(inkpix, SCALE, c[3], c[5], c[4], c[1])
            if ext and (ext[1]-ext[0]) > 1.15*c[1]:
                tall.append([c[0], c[1], c[2], c[3], c[4], c[5], ext[0], ext[1]])
                continue
            linear.append(c)
        elif c[2] == "⋃":
            ext = ink_extent(inkpix, SCALE, c[3], c[5], c[4], c[1])
            big = ext and (ext[1]-ext[0]) > 1.15*c[1]
            style = "\\displaystyle" if big else "\\textstyle"
            tex.append(f"\\MT{{{c[3]:.2f}}}{{{c[4]:.2f}}}{{{c[1]:g}}}{{{style}\\bigcup}}")
        else:
            linear.append(c)

    # ---- linear Cambria runs: split at spaces / size / baseline changes ----
    linear.sort(key=lambda c: (round(c[4]/3)*3, c[3]))
    runs, cur = [], None
    for c in linear:
        if not c[2].strip():
            cur = None
            continue
        if (cur and abs(c[4]-cur["y"]) < 1.0 and c[1] == cur["sz"]
                and -1.0 < c[3] - cur["xend"] < 1.2):
            cur["t"] += c[2]
            cur["xend"] = max(cur["xend"], c[5])
        else:
            cur = {"x": c[3], "y": c[4], "sz": c[1], "t": c[2], "xend": c[5]}
            runs.append(cur)
    for r in runs:
        tex.append(f"\\CT{{{r['x']:.2f}}}{{{r['y']:.2f}}}{{{r['sz']:g}}}{{{esc_text(r['t'])}}}")

    # ---- tall delimiters: merge pieces only when their ink runs overlap ----
    tall.sort(key=lambda c: (round(c[3]), c[6]))
    groups = []
    for c in tall:
        g = next((gg for gg in groups
                  if abs(gg["x"]-c[3]) < 2.5
                  and not (c[6] > gg["ybot"]+2 or c[7] < gg["ytop"]-2)), None)
        if g:
            g["ytop"] = min(g["ytop"], c[6]); g["ybot"] = max(g["ybot"], c[7])
            g["ch"] = g["ch"] or c[2].strip(); g["sz"] = max(g["sz"], c[1])
        else:
            groups.append({"x": c[3], "ytop": c[6], "ybot": c[7],
                           "ch": c[2].strip(), "sz": c[1]})
    groups = [g for g in groups if (g["ybot"]-g["ytop"]) < 80]
    for g in groups:
        d = DELMAP.get(g["ch"])
        if not d:
            tex.append(f"% TALL-UNKNOWN {g}")
            continue
        ymid = (g["ytop"]+g["ybot"])/2
        M = (g["ybot"]-g["ytop"])/2
        a = AXIS*g["sz"]
        tex.append(f"\\TDEL{{{g['x']:.2f}}}{{{ymid+a:.2f}}}{{{g['sz']:g}}}"
                   f"{{{M+a:.2f}}}{{{M-a:.2f}}}{{{d}}}")

    # ---- non-Cambria lines, organized by visual row ----
    d = pg.get_text("dict")
    RIGHT_EDGE = 500.0
    txlines = []
    for b in d["blocks"]:
        if b["type"] != 0: continue
        for l in b["lines"]:
            spans = [s for s in l["spans"] if s["text"].strip()]
            if not spans: continue
            y = spans[0]["origin"][1]
            if abs(y-45.6) < 2 or abs(y-714.5) < 2: continue
            txlines.append((round(y,1), spans))
    # rows that contain any Cambria (or SymbolMT — its subset has no usable
    # space/bullet metrics) get word-exact treatment once
    rows = {}
    for y, spans in txlines:
        key = round(y/2)*2
        rows.setdefault(key, []).append((y, spans))
    handled_y = []
    for key, entries in sorted(rows.items()):
        has_cam = any(s["font"] in ("CambriaMath", "SymbolMT")
                      for _, spans in entries for s in spans)
        if has_cam:
            y0 = entries[0][0]
            if any(abs(y0-h) < 3.0 for h in handled_y): continue
            handled_y.append(y0)
            rowc = [c for c in allchars if c[0] != "CambriaMath"
                    and abs(c[4]-y0) < 3.6]
            rowc.sort(key=lambda c: c[3])
            wruns, cur = [], None
            for c in rowc:
                if not c[2].strip():
                    cur = None; continue
                if (cur and c[0] == cur["f"] and c[1] == cur["sz"]
                        and -1.0 < c[3]-cur["xend"] < 1.2):
                    cur["t"] += c[2]; cur["xend"] = max(cur["xend"], c[5])
                else:
                    cur = {"f": c[0], "sz": c[1], "x": c[3], "y": c[4],
                           "t": c[2], "xend": c[5]}
                    wruns.append(cur)
            for r in wruns:
                base, sz = fcmd(r["f"], r["sz"])
                if base is None: continue
                t = esc_text(r["t"]).replace("•", "\\SymBullet{}")
                tex.append(f"\\TL{{{r['x']:.2f}}}{{{r['y']:.2f}}}{{{base}{{{sz}}}{t}}}")
            continue
        for y, spans in entries:
            # pure text line: justified block placement; ink end limited to
            # this line's own horizontal extent
            x0 = spans[0]["bbox"][0]
            xmax = spans[-1]["bbox"][2] + 1.0
            rowc = [c for c in allchars if abs(c[4]-y) < 1.5 and c[2].strip()
                    and x0 - 1.0 <= c[3] <= xmax]
            x1 = max((c[5] for c in rowc), default=spans[-1]["bbox"][2])
            parts, ok, prev = [], True, None
            for s in spans:
                base, sz = fcmd(s["font"], s["size"])
                if base is None: ok = False; break
                t = s["text"]
                if s is spans[-1]: t = t.rstrip()
                if prev is not None:
                    gap = s["bbox"][0] - prev["bbox"][2]
                    if gap > 1.2 and not prev["text"].endswith(" ") and not t.startswith(" "):
                        parts.append(" ")
                parts.append(f"{base}{{{sz}}}{esc_text(t)}")
                prev = s
            if not ok: continue
            body = "".join(parts).replace("•", "\\SymBullet{}")
            ink = x1 - x0
            if x1 > RIGHT_EDGE and " " in body:
                tex.append(f"\\JL{{{x0:.2f}}}{{{y:.2f}}}{{{ink:.2f}}}{{{body}}}")
            else:
                tex.append(f"\\TL{{{x0:.2f}}}{{{y:.2f}}}{{{body}}}")

    with open(f"{OUT}/page{folio}.tex", "w") as f:
        f.write("\n".join(tex) + "\n")
print("v2 generated")
