"""Simple full-width top-to-bottom piece stacking for work sheets.
Styleguide sec.4: pieces tile left->right, top->bottom, separated by
ruler-straight lines. We use the top-to-bottom-only degenerate case
throughout for reliability across many sheets.
"""
import os
from atoms import fmt

MARGIN_X = 40.0
PAGE_W = 595.32
PAGE_H = 841.92
TOP_Y = 34.0
BOTTOM_Y = 800.0  # leave room for folio box
CONTENT_W = PAGE_W - 2 * MARGIN_X


LABEL_BAND = 20.0   # vertical space reserved for the piece-label box itself
DIVIDER_GAP = 6.0    # gap between a divider line and the label band below it


def lay_pieces(pieces, content_x=None):
    """pieces: list of (label, atom, pad_top, pad_bottom).
    pad_top/pad_bottom are extra breathing room ABOVE the label band and
    BELOW the content, respectively. atom is placed with its own baseline
    at the row's baseline y. Returns a list of line-lists, one per physical
    sheet (new sheets opened automatically on overflow)."""
    if content_x is None:
        content_x = MARGIN_X + 14
    sheets = []
    cur = []
    y = TOP_Y
    first_on_sheet = True
    for label, atom, pad_top, pad_bottom in pieces:
        needed = pad_top + LABEL_BAND + atom.ht + atom.dp + pad_bottom
        if not first_on_sheet and y + needed > BOTTOM_Y:
            sheets.append(cur)
            cur = []
            y = TOP_Y
            first_on_sheet = True
        if not first_on_sheet:
            cur.append(f'\\DLINE{{{fmt(MARGIN_X)}}}{{{fmt(y)}}}'
                       f'{{{fmt(PAGE_W - MARGIN_X)}}}{{{fmt(y)}}}{{0.7}}')
            y += DIVIDER_GAP
        y += pad_top
        # piece label box: top-left corner at the top of this piece's band
        cur.append(f'\\PLBL{{{fmt(MARGIN_X)}}}{{{fmt(y)}}}{{{label}}}')
        y += LABEL_BAND
        baseline_y = y + atom.ht
        cur += atom.emit(content_x, baseline_y)
        y = baseline_y + atom.dp + pad_bottom
        first_on_sheet = False
    sheets.append(cur)
    return sheets


def write_sheets(basefolio, sheets, outdir):
    """basefolio e.g. 3040; writes ws3040.tex, ws3041.tex, ... and returns
    the list of folio numbers used (as strings)."""
    folios = []
    for i, lines in enumerate(sheets):
        folio = f'{basefolio + i}'
        folios.append(folio)
        path = os.path.join(outdir, f'ws{folio}.tex')
        with open(path, 'w') as f:
            f.write(f'%% ===== work sheet {folio} — generated =====\n')
            f.write('\n'.join(lines) + '\n')
        print(f'wrote {path} ({len(lines)} lines)')
    return folios
