"""Shared G(w,x,y,z)-related term builders for 2a/2b/2c/3a/3b/3c.
All values independently verified via Quine-McCluskey (see project memory).
"""
import sys
sys.path.insert(0, '.')
from atoms import R, HB, cvar


def G_formula(sz=12.96):
    # G(w,x,y,z) = (y+z')(w+x+y+z)(w'+x+y'+z)
    f1 = HB(R('(', sz), cvar('𝑦', sz=sz), R(' + ', sz, font='c'),
            cvar('𝑧', True, sz), R(')', sz))
    f2 = HB(R('(', sz), cvar('𝑤', sz=sz), R(' + ', sz, font='c'),
            cvar('𝑥', sz=sz), R(' + ', sz, font='c'), cvar('𝑦', sz=sz),
            R(' + ', sz, font='c'), cvar('𝑧', sz=sz), R(')', sz))
    f3 = HB(R('(', sz), cvar('𝑤', True, sz), R(' + ', sz, font='c'),
            cvar('𝑥', sz=sz), R(' + ', sz, font='c'), cvar('𝑦', True, sz),
            R(' + ', sz, font='c'), cvar('𝑧', sz=sz), R(')', sz))
    return HB(f1, f2, f3)


def baterm4(bits, sz=12.96):
    """bits = (w,x,y,z) each 0/1 -> juxtaposed BA product term."""
    names = ['𝑤', '𝑥', '𝑦', '𝑧']
    return HB(*[cvar(n, comp=(b == 0), sz=sz) for b, n in zip(bits, names)])


# SOP(G) = wy'z' + w'y + xy + xz' + yz  (via the 3-tier distribution tree)
# CORRECTED (2026-08-14): t1 was w'y'z' (transcription error) -- the real
# distribution-tree output is "z'wy'" = wy'z' (w UNcomplemented). Verified
# against the independently-computed PI(G)/MSOP(G) below, which already
# had this term right (wy'z'), and against direct QM prime-implicant
# computation. This bug reached the printed pages (612/616/618) before
# being caught while building the 2b consensus worksheet -- see project
# memory for the full audit.
def sop_terms(sz=12.96):
    def prod(*lits):
        # lits: list of (name, comp)
        return HB(*[cvar(n, comp=c, sz=sz) for n, c in lits])
    t1 = prod(('𝑤', False), ('𝑦', True), ('𝑧', True))   # wy'z'
    t2 = prod(('𝑤', True), ('𝑦', False))                # w'y
    t3 = prod(('𝑥', False), ('𝑦', False))                # xy
    t4 = prod(('𝑥', False), ('𝑧', True))                 # xz'
    t5 = prod(('𝑦', False), ('𝑧', False))                # yz
    return [t1, t2, t3, t4, t5]


def msop_terms(sz=12.96):
    def prod(*lits):
        return HB(*[cvar(n, comp=c, sz=sz) for n, c in lits])
    t1 = prod(('𝑤', True), ('𝑦', False))                 # w'y
    t2 = prod(('𝑤', False), ('𝑦', True), ('𝑧', True))    # wy'z'
    t3 = prod(('𝑥', False), ('𝑧', True))                  # xz'
    t4 = prod(('𝑦', False), ('𝑧', False))                 # yz
    return [t1, t2, t3, t4]


CSOP_BITS = [
    (0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0), (0, 1, 1, 0), (0, 1, 1, 1),
    (1, 0, 0, 0), (1, 0, 1, 1), (1, 1, 0, 0), (1, 1, 1, 0), (1, 1, 1, 1),
]


def csop_terms(sz=12.96):
    return [baterm4(b, sz) for b in CSOP_BITS]


def plus_join(terms, sz=12.96):
    parts = [terms[0]]
    for t in terms[1:]:
        parts.append(R(' + ', sz, font='c'))
        parts.append(t)
    return HB(*parts)
