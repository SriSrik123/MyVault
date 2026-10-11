#!/usr/bin/env python3
"""503: J-number blank, J1..J8, My J-values/My C-values rows, My Connective
List C1..C8. J=00499317 (Sri's fixed personal ID, reused from 1B/1C/2A/2B
setup precedent). C-values via the exam's own printed table (0,4,8->OR;
1,5,9->AND; 2,6->IMP; 3,7->IFF).
"""
import sys
sys.path.insert(0, '.')
from atoms import R

J = [0, 0, 4, 9, 9, 3, 1, 7]
TABLE = {0: '∨', 1: '∧', 2: '⟶', 3: '⟷', 4: '∨', 5: '∧', 6: '⟶', 7: '⟷', 8: '∨', 9: '∧'}
C = [TABLE[d] for d in J]
out = []

# J-number blank
out += R('00499317', 12.0, font='b').emit(223.0, 114.02)

# J1..J8 "=" fills
j_slots_row1 = [(204.0, 168.26), (276.0, 168.26), (347.5, 168.26), (419.5, 168.26)]
j_slots_row2 = [(203.5, 218.90), (276.0, 218.90), (347.5, 218.90), (419.5, 218.90)]
for (x, y), v in zip(j_slots_row1 + j_slots_row2, J):
    out += R(str(v), 11.04, font='b').emit(x, y)

# My J-values row (y=440.30), same x's as the J-number header row (y=426.17)
jcol_x = [180.74, 225.65, 270.77, 315.79, 360.91, 406.03, 451.18, 496.18]
for x, v in zip(jcol_x, J):
    a = R(str(v), 11.04, font='b')
    out += a.emit(x - a.w / 2 + 2.1, 440.30)

# My C-values row (y=454.50), same x's
for x, c in zip(jcol_x, C):
    a = R(c, 11.04)
    out += a.emit(x - a.w / 2 + 2.1, 454.50)

# My Connective List: C1=.. C8=..
c_slots_row1 = [(205.0, 567.43), (277.0, 567.43), (349.0, 567.43), (421.0, 567.43)]
c_slots_row2 = [(205.0, 617.98), (277.0, 617.98), (349.0, 617.98), (421.0, 617.98)]
for (x, y), c in zip(c_slots_row1 + c_slots_row2, C):
    out += R(c, 11.04).emit(x, y)

with open('pages/answers503.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers503.tex; J={J} C={C}')
