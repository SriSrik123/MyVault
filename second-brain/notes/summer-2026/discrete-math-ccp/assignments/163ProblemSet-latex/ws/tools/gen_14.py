#!/usr/bin/env python3
from common import T, R, Barred, VStack, gen

table_hdr = T('n     β(n)=(n!)ⁿ        δ(n)=nⁿ!            γ(n)=(n!)!          α(n)=(nⁿ)!', sz=10.0)
table = T('3     216               729                 720                 27!\n', sz=10.0)

p1 = [
    ('14.0', VStack([
        (T('n=3:  β=216   δ=729   γ=720   α=27!    (γ,δ swapped; close: 720 vs 729)'), 0),
        (T('n=4:  β=331,776   δ=4²⁴≈2.81×10¹⁴   γ=24!≈6.20×10²³   α=256!'), 6),
        (T('n=5:  β≈2.49×10¹⁰   δ=5¹²⁰≈7.5×10⁸³   γ=120!≈6.7×10¹⁹⁸   α=3125!'), 6),
    ]), 4, 6),
    ('14.1', Barred(T('331,776 < 4²⁴ < 24! < 256!'), T('P(4)')), 4, 6),
    ('14.2', VStack([
        (T('β<δ (base n=4; other two below): a(n)≔ln β(n)=n∙ln(n!),  b(n)≔ln δ(n)=n!∙ln n'), 0),
        (Barred(T('a(n)<b(n)'), T('(n+1)ln(n!)+(n+1)ln(n+1) < (n+1)[n!/n∙ln n+ln(n+1)]')), 8),
    ]), 4, 6),
    ('14.3', Barred(T('n!/n ≤ n!−1'), T('a(n+1) < b(n+1)')), 4, 6),
    ('14.4', T('n ≤ n!(n−1), true ∀n≥4 since n!(n−1)≥24∙3=72≫n'), 4, 4),
]

p2 = [
    ('14.5', VStack([
        (T('δ<γ: ln n<ln(n!) (n≥2)'), 0),
        (Barred(T('ln n < ln(n!)  (n≥2)'), T('n!∙ln n < n!∙ln(n!) ≤ ln((n!)!) = ln γ(n)')), 8),
    ]), 4, 6),
    ('14.6', VStack([
        (T('γ<α: n! ≤ nⁿ (n≥2), each of n! factors is ≤n'), 0),
        (Barred(T('n! ≤ nⁿ  (n≥2)'), T('α(n) = (nⁿ)! ≥ (n!)! = γ(n)')), 8),
    ]), 4, 6),
    ('14.7', Barred(T('P(4)    14.2  14.3  14.5  14.6'), T('∀n∈ℕ(n≥4) (β(n)<δ(n)<γ(n)<α(n))')), 4, 4),
]

gen(10290, p1)
gen(10291, p2)
