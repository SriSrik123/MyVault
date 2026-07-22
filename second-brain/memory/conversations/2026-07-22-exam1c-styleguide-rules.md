---
title: Exam 1C style sheet and rules tightening
last_updated: 2026-07-22
type: conversation
source: cowork
---

# 2026-07-22 — Exam 1C Style Sheet and Rules Tightening

## What Happened
Sri supplied two solved Math 163 Exam 1C PDFs (professor's own solves: 2020 "Cap'n Orangebeard", 2024 "Captain Yellowbeard"), his blank 2026 Exam 1C, and his `Rules.md`, asking for a style sheet capturing the solved exams' exact format (for a future LaTeX markup of the 2026 exam) plus a precision pass on Rules.md. All 31 sample pages were rendered (PyMuPDF; poppler not installed) and studied. Key discovery: the 2026 exam is question-for-question the 2024 exam with new J-number data, and both samples skip the three proof questions (1c/2c/3c — expected grade 36/50). Delivered `discrete-math-ccp/styleguide.md` (answer anchors A1–A8, work-sheet piece grammar, substitution-bar/⟨x ⟵ e⟩ witness, tables, trees, coefficient stacks, LaTeX macro plan on top of the 1B pipeline, flagged decisions) and a substantially tightened `~/Downloads/Rules.md`.

## Key Decisions Made
- Formatting conflicts between samples resolve to SOL-2024 (same generation as 2026); printed page-301 instructions outrank both.
- `∵` stays prohibited even though the 2024 sample uses it once (work piece 1a.i.3); replacement is a two-premise conclusion bar (styleguide §5.3).
- `My {s,b}` fills follow the sample's positional order (not re-sorted); all other listings increasing — flagged for Sri's sign-off.
- Answers in the LaTeX replica are typeset in the print's own Cambria Math (format, not pen, is what's replicated), via macros with a draft-tint switch.
- Solved exams copied into the vault (`exams/163Exam1C-Solutions-2020/2024.pdf`); Rules.md left in Downloads (move into vault suggested).

## Facts Learned About Sri
- Enrolled in Math 163 Discrete Mathematics I (CCP, Summer 2026, section 901 ONLAS 7N); Exam 1C due 2026-07-27 23:59, submission must be mechanical-pencil handwriting, single document, work sheets foliated n0/n1/….

## Tasks / Action Items Resulting
- Compile page locators for Counting / Binomial Theorem / Induction and Recursion notes (Rules.md marks them uncompiled).
- Resolve flagged decisions: general-formula name (`BnmlCfn` vs `BnmlCfnt`) against Binomial Theorem notes; 1c/2c/3c proof layouts from Induction and Recursion notes; `My {s,b}` fill order.
- Then: generate the 163Exm1C LaTeX replica with `tools/gen2.py` (1B pipeline) and typeset answers per styleguide — before the 2026-07-27 deadline.

## Follow-Up Questions / Gaps
- Whether Sri wants the exam solved collaboratively next session ("You may discuss with anyone" is printed on every page) or only the blank replica + format scaffolding.
- 2026 J-number edge cases (undefined `s`/`b`, collapsed `{s,b}` alphabet) may trigger "does not make sense" chains — data-dependent, unresolved until his J-number is entered.

---

## Related Notes
[[memory/entities/sri]]  [[memory/SCHEMA|Schema]]  [[memory/index|Memory Index]]  [[memory/log|Log]]  [[memory/conversations/2026-07-20-exam-pdf-latex-replica|1B replica session]]
