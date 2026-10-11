"""Simple full-width top-to-bottom piece stacking for work sheets.
Ported from 163Exm2A-latex/tools/pieces.py -- page geometry changed back
from 2A's US Letter (612x792) to A4 (595.32x841.92), matching 2B (same as
1B/1C), everything else unchanged. Styleguide sec.4 / page 401's own rule:
work for a problem on page n goes on blank (not ruled) sheets after it,
numbered n0,n1,n2..., each piece boxed and separated by ruler-straight
lines.
"""
import os
from atoms import fmt

# \PLBL (preamble.tex) always renders its label through \BA{9.5} (Book
# Antiqua) -- BA's subsetted font is missing digit 7 (confirmed via cmap:
# BookAntiqua_5.ttf has no U+0037), so any auto-numbered piece index that
# reaches 7 (piece .7, .17, ...) silently drops that digit. Wrap it in a
# scoped {\CMT{9.5}7} so just that character renders in CambriaM (which
# has the full digit set) and the group's closing brace reverts to BA for
# whatever follows -- matches \PLBL's own hardcoded 9.5pt size exactly.
def _label_tex(label):
    return label.replace('7', r'{\CMT{9.5}7}')


MARGIN_X = 42.0
PAGE_W = 595.32
PAGE_H = 841.92
TOP_Y = 34.0
BOTTOM_Y = 800.0  # leave room for folio box (2B's own folio sits at y=789.6)
CONTENT_W = PAGE_W - 2 * MARGIN_X


LABEL_BAND = 20.0   # vertical space reserved for the piece-label box itself
DIVIDER_GAP = 6.0    # gap between a divider line and the label band below it


def lay_pieces(pieces, content_x=None, top_y=None):
    """pieces: list of (label, atom, pad_top, pad_bottom).
    pad_top/pad_bottom are extra breathing room ABOVE the label band and
    BELOW the content, respectively. atom is placed with its own baseline
    at the row's baseline y. Returns a list of line-lists, one per physical
    sheet (new sheets opened automatically on overflow).

    top_y overrides the module default TOP_Y=34 -- safe for a synthetic
    \\worksheet{} page (blank, no chrome), but a real \\dopage{} page
    already carries \\ChromePage's own header text starting at y=45.6
    (preamble.tex), so a piece label box at the default TOP_Y overlaps it
    (confirmed by render: 1b(i)'s "1b.i.0" box sat directly on top of
    "Due by2359 hours..." once its work moved onto the real page 408).
    Callers writing to a chrome'd real page must pass a top_y clear of
    that header (e.g. 90.0, the same safe value already used elsewhere in
    this project for post-chrome content)."""
    if content_x is None:
        content_x = MARGIN_X + 14
    y0 = TOP_Y if top_y is None else top_y
    sheets = []
    cur = []
    y = y0
    first_on_sheet = True
    for label, atom, pad_top, pad_bottom in pieces:
        needed = pad_top + LABEL_BAND + atom.ht + atom.dp + pad_bottom
        if not first_on_sheet and y + needed > BOTTOM_Y:
            sheets.append(cur)
            cur = []
            y = y0
            first_on_sheet = True
        if not first_on_sheet:
            cur.append(f'\\DLINE{{{fmt(MARGIN_X)}}}{{{fmt(y)}}}'
                       f'{{{fmt(PAGE_W - MARGIN_X)}}}{{{fmt(y)}}}{{0.7}}')
            y += DIVIDER_GAP
        y += pad_top
        # piece label box: top-left corner at the top of this piece's band
        cur.append(f'\\PLBL{{{fmt(MARGIN_X)}}}{{{fmt(y)}}}{{{_label_tex(label)}}}')
        y += LABEL_BAND
        baseline_y = y + atom.ht
        cur += atom.emit(content_x, baseline_y)
        y = baseline_y + atom.dp + pad_bottom
        first_on_sheet = False
    sheets.append(cur)
    return sheets


def lay_grid(cells, ncols, content_pad_x=14.0, top_y=None, row_gap=10.0,
             border_w=0.7):
    """cells: list of (label, atom) in row-major order, filling an
    ncols-wide grid on a SINGLE sheet -- each cell gets its own full
    rectangle border plus a PLBL corner tag (styleguide's per-piece boxed
    convention, extended to 2D for a multi-cell grid problem like 3a's six
    Tlg/Cdn/Cng classifications, matching SOL2B-2024's own folio 5140
    layout exactly: one bordered+labelled box per cell, not one label per
    row). No overflow handling (unlike lay_pieces) -- callers with more
    cells than comfortably fit one page should pre-chunk into multiple
    lay_grid() calls/sheets themselves; a fixed small grid never needs it.
    """
    n = len(cells)
    nrows = -(-n // ncols)  # ceil
    col_w = CONTENT_W / ncols
    y0 = TOP_Y if top_y is None else top_y
    row_h = 0.0
    for label, atom in cells:
        needed = LABEL_BAND + atom.ht + atom.dp + row_gap
        row_h = max(row_h, needed)
    out = []
    for i, (label, atom) in enumerate(cells):
        r, c = divmod(i, ncols)
        x0c = MARGIN_X + c * col_w
        x1c = x0c + col_w
        y0c = y0 + r * row_h
        y1c = y0c + row_h
        out += [
            f'\\DLINE{{{fmt(x0c)}}}{{{fmt(y0c)}}}{{{fmt(x1c)}}}{{{fmt(y0c)}}}{{{fmt(border_w)}}}',
            f'\\DLINE{{{fmt(x0c)}}}{{{fmt(y1c)}}}{{{fmt(x1c)}}}{{{fmt(y1c)}}}{{{fmt(border_w)}}}',
            f'\\DLINE{{{fmt(x0c)}}}{{{fmt(y0c)}}}{{{fmt(x0c)}}}{{{fmt(y1c)}}}{{{fmt(border_w)}}}',
            f'\\DLINE{{{fmt(x1c)}}}{{{fmt(y0c)}}}{{{fmt(x1c)}}}{{{fmt(y1c)}}}{{{fmt(border_w)}}}',
        ]
        out.append(f'\\PLBL{{{fmt(x0c)}}}{{{fmt(y0c)}}}{{{_label_tex(label)}}}')
        content_y = y0c + LABEL_BAND + atom.ht
        out += atom.emit(x0c + content_pad_x, content_y)
    return [out]


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
