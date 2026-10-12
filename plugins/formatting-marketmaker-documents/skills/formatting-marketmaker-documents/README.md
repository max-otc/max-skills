# CRX MM document formatting skill (v4.2)

Design standard for formal CRX market-maker documents (Margin & Settlement, Collateral Overview, methodologies, one-pagers).

- `SKILL.md`: the skill. Drop the folder into `~/.claude/skills/`, or read the file.
- `templates/crx-doc-template.html`: locked canonical skeleton; every document starts as a copy.
- `templates/doc-qa.py`: mechanical conformance gate.
- `templates/_fixtures/`: regression fixtures (HTML + rendered PDF pairs).
- `reference/crx-margin-settlement-overview-v5.html`: reference implementation, tiebreaker for ambiguous rules. SKILL.md cites it at `~/Downloads/…` (Jake's machine); in this bundle it lives here.

Render on macOS (body face: system Times New Roman), headless Chrome HTML→PDF.
