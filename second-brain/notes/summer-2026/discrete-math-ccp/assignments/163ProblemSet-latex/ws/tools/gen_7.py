#!/usr/bin/env python3
from common import T, Infer, Chevrons, assign, gen

wit = Chevrons([
    assign(T('R₀'), T('0')),
    assign(T('R₁'), T('1')),
    assign(T('r'), T('1/2')),
    assign(T('s'), T('√5/2')),
])

formula = T('ρ(n) = [(R₀(r+s)−R₁)/2s](r−s)ⁿ + [(R₁−R₀(r−s))/2s](r+s)ⁿ')

pieces = [
    ('7.0', Infer(formula, T('ρ(n) = (−1/√5)((1−√5)/2)ⁿ + (1/√5)((1+√5)/2)ⁿ'), witness=wit), 4, 8),
    ('7.1', T('r−s = (1−√5)/2,   r+s = (1+√5)/2'), 4, 4),
    ('7.2', T('ρ(n) = (1/√5)[((1+√5)/2)ⁿ − ((1−√5)/2)ⁿ]'), 4, 4),
    ('7.3', T('n=0: (1/√5)(1−1) = 0 = ρ(0)      n=1: (1/√5)∙√5 = 1 = ρ(1)'), 4, 4),
]

gen(10150, pieces)
