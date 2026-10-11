"""Shared layout helpers: top-to-bottom LEFT-aligned stacking of
heterogeneous Atom-protocol objects (unlike atoms.VC, which centers)."""


class VStack:
    def __init__(self, rows):
        """rows: list of (atom, gap_before_this_row)."""
        self.rows = rows
        self.w = max(a.w for a, _ in rows)
        ys, cy = [], 0.0
        first = True
        for a, gap in rows:
            if first:
                cy = a.ht
                first = False
            else:
                cy += gap + a.ht
            ys.append(cy)
            cy += a.dp
        self.ys = ys
        self.ht = rows[0][0].ht
        self.dp = ys[-1] + rows[-1][0].dp

    def emit(self, x, y):
        out = []
        for (a, _), ry in zip(self.rows, self.ys):
            out += a.emit(x, y + ry)
        return out


class Box:
    """Wrap a raw (w, ht, dp, emit) object that isn't an Atom subclass so
    it composes with HB/VC/VStack/pieces.py the same way."""
    def __init__(self, atom):
        self.atom = atom
        self.w, self.ht, self.dp = atom.w, atom.ht, atom.dp

    def emit(self, x, y):
        return self.atom.emit(x, y)


class Barred:
    """`top` atom, a full-width conclusion bar, then `bottom` atom below."""
    def __init__(self, top, bottom, pad=4.0, gap=6.0):
        from atoms import fmt
        self._fmt = fmt
        self.top, self.bottom, self.gap = top, bottom, gap
        self.bar = max(top.w, bottom.w) + 2 * pad
        self.w = self.bar
        self.ht = top.ht
        self.dp = top.dp + gap * 2 + 0.8 + bottom.ht + bottom.dp

    def emit(self, x, y):
        fmt = self._fmt
        out = self.top.emit(x, y)
        by = y + self.top.dp + self.gap
        out.append(f'\\DLINE{{{fmt(x)}}}{{{fmt(by)}}}'
                   f'{{{fmt(x + self.bar)}}}{{{fmt(by)}}}{{0.6}}')
        out += self.bottom.emit(x + (self.bar - self.bottom.w) / 2,
                                 by + self.gap + self.bottom.ht)
        return out
