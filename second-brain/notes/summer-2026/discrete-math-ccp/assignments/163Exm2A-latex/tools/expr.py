"""Shared math-italic unicode building blocks (must match the exact
codepoints Word used in the source PDF's CambriaMath subset -- plain ASCII
letters are NOT the same glyphs as U+1D400-block math-italic letters)."""

NU = "\U0001D708"  # 𝜈 MATHEMATICAL ITALIC NU (plain Greek U+03BD is NOT in the font)
C_, P_ = "\U0001D436", "\U0001D443"          # 𝐶 𝑃
S_, T_, J_ = "\U0001D446", "\U0001D461", "\U0001D43D"   # 𝑆 𝑡 𝐽
M_, L_ = "\U0001D440", "\U0001D459"           # 𝑀 𝑙
N_, K_ = "\U0001D45B", "\U0001D458"           # 𝑛 𝑘
B_, SS = "\U0001D44F", "\U0001D460"           # 𝑏 𝑠  (SS = math-italic s)
RHO = "\U0001D70C"                             # 𝜌
X_, Y_ = "\U0001D465", "\U0001D466"           # 𝑥 𝑦
F_, G_ = "\U0001D439", "\U0001D43A"           # 𝐹 𝐺
W_, O_, RR_, AA_ = "\U0001D44A", "\U0001D442", "\U0001D445", "\U0001D434"  # 𝑊 𝑂 𝑅 𝐴
RLC_, DLC_ = "\U0001D45F", "\U0001D451"       # 𝑟 𝑑 (lowercase, for Wrd)
Wrd = f"{W_}{RLC_}{DLC_}"                      # 𝑊𝑟𝑑
OM = f"{O_}{M_}"
RA = f"{RR_}{AA_}"
BCAP_ = "\U0001D435"    # 𝐵 (capital, math-italic -- distinct from B_ = lowercase b)
MLC_, FLC_ = "\U0001D45A", "\U0001D453"        # 𝑚 𝑓 (lowercase)
BnmlCfn = f"{BCAP_}{N_}{MLC_}{L_}{C_}{FLC_}{N_}"          # 𝐵𝑛𝑚𝑙𝐶𝑓𝑛 -- printed literally on
MltnmlCfn = f"{M_}{L_}{T_}{N_}{MLC_}{L_}{C_}{FLC_}{N_}"   # 𝑀𝑙𝑡𝑛𝑚𝑙𝐶𝑓𝑛    the exam (styleguide sec.8 #3)
A_, D_ = "\U0001D44E", "\U0001D451"           # 𝑎 𝑑 (unused placeholders)
MINUS = "−"
DEF = "≔"          # ≔
NOTDIV = "∤"       # ∤
DIV = "|"          # divides -- font lacks U+2223; source materials use ASCII pipe U+007C

St_J = f"{S_}{T_}({J_})"
MltSt_J = f"{M_}{L_}{T_}{S_}{T_}({J_})"
nu_StJ = f"{NU}({St_J})"
nu_MltStJ = f"{NU}({MltSt_J})"
