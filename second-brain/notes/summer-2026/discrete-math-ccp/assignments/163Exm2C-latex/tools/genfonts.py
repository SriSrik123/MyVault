#!/usr/bin/env python3
"""Extract the embedded font subsets from the original PDF into fonts/ and
produce CambriaMath_nokern.ttf: the Cambria Math subset with the MATH table's
MathKernInfo offset zeroed (disables cut-in kerning; Word's text shaping does
not apply it, so the replica must not either).  Run from the replica root."""
import fitz, struct, os

SRC = "/Users/sri/Documents/MyVault/second-brain/notes/summer-2026/discrete-math-ccp/assignments/163Exm2C.pdf"
OUT = "fonts"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(SRC)
seen = {}
for pn in range(len(doc)):
    for f in doc[pn].get_fonts():
        xref = f[0]
        if xref in seen:
            continue
        name, ext, _, content = doc.extract_font(xref)
        seen[xref] = None
        if not content:
            print(f"xref {xref} {f[3]}: not embedded, skipped")
            continue
        base = name.split("+")[-1]
        fn = f"{OUT}/{base}_{xref}.{ext}"
        with open(fn, "wb") as fh:
            fh.write(content)
        seen[xref] = fn
        print(fn, len(content))

# ---- nokern variant of the Cambria Math subset ----
cam = next(v for v in seen.values() if v and "CambriaMath" in v)
d = bytearray(open(cam, "rb").read())
ntab = struct.unpack(">H", d[4:6])[0]
math_off = None
for i in range(ntab):
    off = 12 + 16*i
    if d[off:off+4] == b"MATH":
        math_off = struct.unpack(">I", d[off+8:off+12])[0]
assert math_off, "no MATH table in Cambria subset"
mgi_rel = struct.unpack(">H", d[math_off+6:math_off+8])[0]   # MathGlyphInfo
mki_field = math_off + mgi_rel + 6                            # MathKernInfo offset field
old = struct.unpack(">H", d[mki_field:mki_field+2])[0]
d[mki_field:mki_field+2] = b"\x00\x00"
open(f"{OUT}/CambriaMath_nokern.ttf", "wb").write(d)
print(f"CambriaMath_nokern.ttf written (MathKernInfo {old} -> 0 at byte {mki_field})")
