#!/usr/bin/env python3
"""3b (p516): same validity question as 2c, via axioms/rules of inference
instead of algebra of propositions -- Vld((p C3 q)->p, (p C3 q)->q /
(p C3 q)->(p C5 q)), VALID (Y), agreeing with 2c per the page's own
cross-check requirement. Second Vld box genuinely has only Y/N printed on
the blank exam (no Pf/W pair) -- confirmed against the exam's own raw text
extraction, not a tracing gap.
"""
import sys
sys.path.insert(0, '.')
from atoms import R, center_in_gap, circle_token

C3, C5 = '∨', '∧'
out = []

out += center_in_gap(200.63, 216.77, 365.16, C3, 11.52)
out += center_in_gap(299.15, 315.31, 365.16, C3, 11.52)
out += center_in_gap(227.87, 249.05, 430.68, C3, 11.52)
out += center_in_gap(295.31, 313.99, 430.68, C5, 11.52)

out += circle_token(396.07, 403.30, 227.54, 12.00)   # Y, box 1
out += circle_token(468.10, 482.14, 227.54, 12.00)   # Pf, box 1
out += circle_token(396.07, 403.30, 399.53, 12.00)   # Y, box 2 (no Pf/W here)

with open('pages/answers516.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers516.tex')
