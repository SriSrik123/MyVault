#!/usr/bin/env python3
"""Setup pages 603-605: J-number/T-number fill-ins, then the alpha/beta/
gamma/G(w,x,y,z) derivation. J=00499317 (Sri's fixed personal ID, reused
from 1B/1C/2A precedent -- the field is blank on this exam too, matching
every prior exam in this project). T-number: keep every 0 digit, replace
every nonzero digit with 1 -> T=00111111 (T1=T2=0, T3..T8=1).
Coordinates read directly off pages/page603.tex, page604.tex, page605.tex
(the already-generated blank-template CT/TL/TDEL calls for those pages).
"""
import sys
sys.path.insert(0, '.')
from atoms import R, HB, Chain, cvar, wrap, fmt

J = [0, 0, 4, 9, 9, 3, 1, 7]
T = [0 if d == 0 else 1 for d in J]

# ---------------- page 603 ----------------
out603 = []
out603 += R('00499317', 11.04, font='b').emit(330.0, 100.3)
out603 += R('00111111', 11.04, font='b').emit(330.0, 151.7)

t_rows = [255.41, 284.33, 313.13, 342.05, 370.85, 399.77, 428.71, 457.51]
for y, v in zip(t_rows, T):
    out603 += R(str(v), 11.04, font='b').emit(116.0, y)

SZ = 14.04


def pc(v, name):
    return cvar(name, comp=(v == 0), sz=SZ)


w, x, y_, z = '𝑤', '𝑥', '𝑦', '𝑧'
alpha_num = HB(R('(', SZ), R(str(T[0]), SZ, font='b'), R(')(', SZ), R(w, SZ, font='c'), R(')', SZ),
               R(' + ', SZ, font='c'),
               R('(', SZ), R(str(T[1]), SZ, font='b'), R(')(', SZ), cvar(x, comp=True, sz=SZ), R(')', SZ),
               R(' + ', SZ, font='c'),
               R('(', SZ), R(str(T[2]), SZ, font='b'), R(')(', SZ), R(y_, SZ, font='c'), R(')', SZ),
               R(' + ', SZ, font='c'),
               R('(', SZ), R(str(T[3]), SZ, font='b'), R(')(', SZ), cvar(z, comp=True, sz=SZ), R(')', SZ))
alpha_final = HB(R(y_, SZ, font='c'), R(' + ', SZ, font='c'), cvar(z, comp=True, sz=SZ))
out603 += alpha_num.emit(108.02, 605.50)
out603 += alpha_final.emit(108.02, 665.50)

with open('pages/answers603.tex', 'w') as f:
    f.write('\n'.join(out603) + '\n')
print(f'wrote {len(out603)} lines to pages/answers603.tex')

# ---------------- page 604 ----------------
out604 = []


def prm(name):
    return cvar(name, comp=True, sz=SZ)


b1 = HB(R('(', SZ), R('(', SZ), R('1', SZ, font='b'), R(')', SZ), R(w, SZ, font='c'), R(')', SZ), R('′', SZ, font='c'))
# build beta rows via wrap()-safe primes using Prime atom through cvar; simpler: construct plain HB with cvar-based primes
from atoms import Prime


def group(varname, val):
    inner = HB(R('(', SZ), R(str(val), SZ, font='b'), R(')', SZ), R(varname, SZ, font='c'))
    return HB(R('(', SZ), inner, R(')', SZ), Prime(SZ))


# NOTE: y=122.9x is NOT a blank row -- it's the already-printed beta
# formula's own row (label "beta(T3,T4,T5,T6)" at y=85.34, its printed
# "(((T3)w)')..." expression sits right there at y~122.4-125.8). The
# real blank "=" rows for this problem's own work are 188.70/248.70/308.80
# (confirmed against page604.tex's own TL dump -- three rows, not four).
row1 = HB(group(w, T[2]), group(x, T[3]), group(y_, T[4]), group(z, T[5]), Prime(SZ))
row2 = HB(R('(', SZ), prm(w), R(')', SZ), R('(', SZ), prm(x), R(')', SZ),
          R('(', SZ), prm(y_), R(')', SZ), R('(', SZ), prm(z), R(')', SZ), Prime(SZ))
row4 = HB(R(w, SZ, font='c'), R(' + ', SZ, font='c'), R(x, SZ, font='c'), R(' + ', SZ, font='c'),
          R(y_, SZ, font='c'), R(' + ', SZ, font='c'), R(z, SZ, font='c'))

for yy, atom in zip([188.70, 248.70, 308.80], [row1, row2, row4]):
    out604 += atom.emit(108.02, yy)

# gamma rows
g1 = HB(R('(', SZ), R('1', SZ, font='b'), R(')(', SZ), prm(w), R(')', SZ),
        R(' + ', SZ, font='c'),
        R('(', SZ), R('1', SZ, font='b'), R(')(', SZ), R(x, SZ, font='c'), R(')', SZ),
        R(' + ', SZ, font='c'),
        R('(', SZ), R('1', SZ, font='b'), R(')(', SZ), prm(y_), R(')', SZ),
        R(' + ', SZ, font='c'),
        R('(', SZ), R('1', SZ, font='b'), R(')(', SZ), R(z, SZ, font='c'), R(')', SZ))
g2 = HB(prm(w), R(' + ', SZ, font='c'), R(x, SZ, font='c'), R(' + ', SZ, font='c'),
        prm(y_), R(' + ', SZ, font='c'), R(z, SZ, font='c'))
# same fix: y=487.6x is the already-printed gamma formula's own row
# (label at 458.71, printed expression at 487.15-490.51). Real blank
# rows are 547.80/607.80/667.80 -- only 2 genuine steps needed here
# (substitute, then final), so the 3rd stays blank per project precedent
# (leave unneeded printed slots blank rather than pad with a fake step).
out604 += g1.emit(108.02, 547.80)
out604 += g2.emit(108.02, 607.80)

with open('pages/answers604.tex', 'w') as f:
    f.write('\n'.join(out604) + '\n')
print(f'wrote {len(out604)} lines to pages/answers604.tex')

# ---------------- page 605 ----------------
out605 = []
alpha_f = wrap(HB(R(y_, SZ, font='c'), R(' + ', SZ, font='c'), pc(0, z)), l='(', r=')', sz=SZ)
beta_f = wrap(HB(R(w, SZ, font='c'), R(' + ', SZ, font='c'), R(x, SZ, font='c'), R(' + ', SZ, font='c'),
                  R(y_, SZ, font='c'), R(' + ', SZ, font='c'), R(z, SZ, font='c')), l='(', r=')', sz=SZ)
gamma_f = wrap(HB(prm(w), R(' + ', SZ, font='c'), R(x, SZ, font='c'), R(' + ', SZ, font='c'),
                   prm(y_), R(' + ', SZ, font='c'), R(z, SZ, font='c')), l='(', r=')', sz=SZ)
g_row = HB(alpha_f, beta_f, gamma_f)
out605 += g_row.emit(108.02, 205.90)

with open('pages/answers605.tex', 'w') as f:
    f.write('\n'.join(out605) + '\n')
print(f'wrote {len(out605)} lines to pages/answers605.tex')
