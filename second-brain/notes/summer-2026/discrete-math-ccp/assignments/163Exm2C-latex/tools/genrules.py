#!/usr/bin/env python3
"""Extract the original PDF's vector fill rectangles (table rules, underlines,
strikethroughs) into pages/rulesNNN.tex as \\RECT lines.  Non-rectangle items
are emitted as comments for manual attention.  Run from the replica root."""
import fitz, os

SRC = "/Users/sri/Documents/MyVault/second-brain/notes/summer-2026/discrete-math-ccp/assignments/163Exm2C.pdf"
OUT = "pages"
FOLIO0 = 600
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(SRC)

for pn in range(len(doc)):
    folio = FOLIO0 + pn
    lines = []
    for dr in doc[pn].get_drawings():
        if dr["type"] not in ("f", "fs"):
            lines.append(f"% NON-FILL drawing type={dr['type']} rect={dr['rect']}")
            continue
        for it in dr["items"]:
            if it[0] == "re":
                r = it[1]
                lines.append(f"\\RECT{{{r.x0:.2f}}}{{{r.y0:.2f}}}{{{r.x1:.2f}}}{{{r.y1:.2f}}}")
            elif it[0] == "qu":
                q = it[1]
                r = q.rect
                lines.append(f"\\RECT{{{r.x0:.2f}}}{{{r.y0:.2f}}}{{{r.x1:.2f}}}{{{r.y1:.2f}}}")
            else:
                lines.append(f"% NON-RECT item {it[0]} {it[1:]}")
    if lines:
        with open(f"{OUT}/rules{folio}.tex", "w") as f:
            f.write("\n".join(lines) + "\n")
        print(f"rules{folio}.tex: {len(lines)} entries")
print("rules generated")
