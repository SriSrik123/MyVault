import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atoms import M, R, HB, Kern, wrap, VC, binom, mltnom, Chevrons, assign, Infer, Chain
from stack import Barred, VStack, Box
from pieces import lay_pieces, write_sheets

SZ = 11.04
OUT = os.path.join(os.path.dirname(__file__), '..', 'sheets')


def T(s, sz=SZ, font='c'):
    return M(s, sz, font=font)


def gen(basefolio, pieces):
    sheets = lay_pieces(pieces)
    folios = write_sheets(basefolio, sheets, OUT)
    print(basefolio, '->', folios)
    return folios
