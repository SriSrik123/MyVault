#!/usr/bin/env python3
"""1c (p509): Vld(LS/RS) entailment check, reusing 1b's LS/RS formulas
(same C7=AND, C8=IFF). Verified: LS does NOT entail RS (counterexample
p,q,r=(0,1,0): LS=1, RS=0) -> N, with Pf (a completed check justifies it).
Two Vld boxes on this page: the raw-C-notation one (no fill, circle only)
and "My problem"'s own restated substituted version (fill + circle).
"""
import sys
sys.path.insert(0, '.')
from atoms import R, center_in_gap, circle_token

C7, C8 = '∧', '⟷'
out = []

# "My problem" numerator p_q_r (y=327.41) -- the C8 gap's left edge is the
# closing paren around "p C7 q" (TDEL at x=247.85, sz=12.96), not q's own
# end (247.86, nearly identical to the paren's own x and easy to mistake
# for it) -- paren width ~=0.45*(19.68+13.20)=14.8bp per atoms.Delim's own
# documented estimate, found by zooming in and seeing the arrow's left
# head swallowed by the paren ink.
out += center_in_gap(224.01, 243.53, 327.41, C7, 8.04)
# Genuinely tight slot: paren-end to r is only ~6.7bp total, narrower than
# IFF's glyph even at the usual min_sz floor -- relax pad/floor here rather
# than accept overlap; still centered, just smaller than every other C8
# fill on this page (a real, template-driven constraint, not a mistake).
out += center_in_gap(247.85 + 14.8, 269.33, 327.41, C8, 8.04, pad=0.4, min_sz=4.5)

# "My problem" denominator p_r_q_r (y=396.05) -- outer C7 gap bounded by
# the two group parens (TDEL close at 223.85, TDEL open at 250.73), not by
# r's/q's own token positions which sit further inside each paren.
out += center_in_gap(200.61, 220.01, 396.05, C8, 8.04)
out += center_in_gap(223.85 + 14.8, 250.73, 396.05, C7, 8.04)
out += center_in_gap(262.38, 285.41, 396.05, C8, 8.04)

# both Vld boxes: verdict N, justification Pf
out += circle_token(432.07, 443.76, 161.06, 15.96)   # N, box 1
out += circle_token(468.10, 486.77, 161.06, 15.96)   # Pf, box 1
out += circle_token(432.07, 443.76, 363.77, 15.96)   # N, box 2
out += circle_token(468.10, 486.77, 363.77, 15.96)   # Pf, box 2

with open('pages/answers509.tex', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} lines to pages/answers509.tex')
