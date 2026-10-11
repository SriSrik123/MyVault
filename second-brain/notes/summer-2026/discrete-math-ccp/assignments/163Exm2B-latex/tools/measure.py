#!/usr/bin/env python3
"""Char-level comparison of original vs replica PDF.
Aligns glyph sequences per page and reports position deltas and
delimiter-height mismatches, so fixes can be applied numerically.
Run from the replica root: python3 tools/measure.py 0 1 2 ... (pdf page index)"""
import fitz, sys, difflib

ORIG = "/Users/sri/Documents/MyVault/second-brain/notes/summer-2026/discrete-math-ccp/assignments/163Exm2B.pdf"
MINE = "main.pdf"
FOLIO0 = 500

def chars(page):
    out = []
    for b in page.get_text("rawdict")["blocks"]:
        if b["type"] != 0: continue
        for l in b["lines"]:
            for s in l["spans"]:
                for ch in s["chars"]:
                    c = ch["c"]
                    if not c.strip(): continue
                    x0, y0, x1, y1 = ch["bbox"]
                    out.append((c, round(ch["origin"][0],2), round(ch["origin"][1],2),
                                round(y1-y0,2)))
    out.sort(key=lambda t: (round(t[2]/4)*4, t[1]))  # bucket rows by ~4bp
    return out

DELIMS = set("(){}[]|")
o_doc, m_doc = fitz.open(ORIG), fitz.open(MINE)
for pn in [int(a) for a in sys.argv[1:]]:
    oc, mc = chars(o_doc[pn]), chars(m_doc[pn])
    osq = "".join(t[0] for t in oc)
    msq = "".join(t[0] for t in mc)
    sm = difflib.SequenceMatcher(None, osq, msq, autojunk=False)
    print(f"========== page {pn} (folio {FOLIO0+pn}) ==========")
    issues = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            cluster = None
            for k in range(i2-i1):
                o, m = oc[i1+k], mc[j1+k]
                dx, dy = round(m[1]-o[1],2), round(m[2]-o[2],2)
                dh = round(m[3]-o[3],2)
                bad = abs(dx) > 1.6 or abs(dy) > 1.2 or (o[0] in DELIMS and abs(dh) > 2.5)
                if bad:
                    if cluster is None:
                        ctx = osq[max(0,i1+k-6):i1+k+8].replace("\n"," ")
                        print(f"  drift @'{o[0]}' ctx'{ctx}' orig=({o[1]},{o[2]}) dx={dx} dy={dy}"
                              + (f" dh={dh} (h {o[3]}->{m[3]})" if o[0] in DELIMS and abs(dh)>2.5 else ""))
                        issues += 1
                        cluster = True
                else:
                    cluster = None
        elif op in ("delete", "replace"):
            seg = osq[i1:i2][:40]
            if seg.strip():
                o = oc[i1]
                print(f"  MISSING-in-mine: {seg!r} at ({o[1]},{o[2]})")
                issues += 1
        if op in ("insert", "replace"):
            seg = msq[j1:j2][:40]
            if seg.strip():
                m = mc[j1]
                print(f"  EXTRA-in-mine:   {seg!r} at ({m[1]},{m[2]})")
                issues += 1
    if not issues:
        print("  clean")
