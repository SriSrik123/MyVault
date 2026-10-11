"""6x6 (or NxN) divisibility-style table atom: corner cell, row/col headers,
one vertical + one horizontal rule, every cell holds '(x,y)', qualifying
cells get a drawn ellipse. Compatible with the Atom protocol (w/ht/dp/emit)
used by pieces.py and atoms.py's HB/VC/etc.
"""
from atoms import R, fmt


class DivTable:
    def __init__(self, xs, ys, qualifying, corner_label, sz=10.0,
                 cell_w=42.0, cell_h=24.0, label_w=30.0):
        self.xs, self.ys = xs, ys
        self.qualifying = set(qualifying)
        self.corner_label = corner_label
        self.sz = sz
        self.cell_w, self.cell_h, self.label_w = cell_w, cell_h, label_w
        self.n_rows, self.n_cols = len(xs), len(ys)
        self.w = label_w + cell_w * self.n_cols
        header_h = cell_h
        body_h = cell_h * self.n_rows
        self.ht = header_h * 0.35   # baseline given ~ near top of header row
        self.dp = header_h * 0.65 + body_h

    def emit(self, x, y):
        """(x, y) = baseline of the header row's corner cell (top-left area)."""
        out = []
        top = y - self.ht
        header_h, cell_w, cell_h, label_w = self.cell_h, self.cell_w, self.cell_h, self.label_w
        # corner cell label, centered in the label column x header row
        cx = x + label_w / 2
        cy = top + header_h * 0.68
        out += R(self.corner_label, self.sz, font='c').emit(
            cx - R(self.corner_label, self.sz, font='c').w / 2, cy)
        # column headers (y-values), centered over each column
        for j, yv in enumerate(self.ys):
            t = str(yv)
            tw = R(t, self.sz, font='c').w
            hx = x + label_w + cell_w * j + cell_w / 2 - tw / 2
            out += R(t, self.sz, font='c').emit(hx, cy)
        # row headers (x-values), centered in the label column for each row
        for i, xv in enumerate(self.xs):
            t = str(xv)
            tw = R(t, self.sz, font='c').w
            ry = top + header_h + cell_h * i + cell_h * 0.68
            out += R(t, self.sz, font='c').emit(x + label_w / 2 - tw / 2, ry)
        # vertical rule after the row-header column (full table height)
        vx = x + label_w
        out.append(f'\\DLINE{{{fmt(vx)}}}{{{fmt(top)}}}'
                   f'{{{fmt(vx)}}}{{{fmt(top + header_h + cell_h * self.n_rows)}}}{{0.6}}')
        # horizontal rule under the header row (full table width)
        hy = top + header_h
        out.append(f'\\DLINE{{{fmt(x)}}}{{{fmt(hy)}}}'
                   f'{{{fmt(x + self.w)}}}{{{fmt(hy)}}}{{0.6}}')
        # body cells
        for i, xv in enumerate(self.xs):
            for j, yv in enumerate(self.ys):
                t = f'({xv},{yv})'
                tw = R(t, self.sz, font='c').w
                px = x + label_w + cell_w * j + cell_w / 2 - tw / 2
                py = top + header_h + cell_h * i + cell_h * 0.68
                out += R(t, self.sz, font='c').emit(px, py)
                if (xv, yv) in self.qualifying:
                    ccx = x + label_w + cell_w * j + cell_w / 2
                    ccy = py - self.sz * 0.32
                    out.append(f'\\CIRC{{{fmt(ccx)}}}{{{fmt(ccy)}}}'
                               f'{{{fmt(cell_w * 0.42)}}}{{{fmt(cell_h * 0.38)}}}')
        return out
