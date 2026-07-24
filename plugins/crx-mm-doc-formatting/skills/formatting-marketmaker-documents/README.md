# CRX MM document formatting skill (v4.2)

The design standard for formal CRX market-maker documents (Margin & Settlement, Collateral Overview, methodologies, one-pagers).

- `SKILL.md` — the full skill. Drop the whole folder into `~/.claude/skills/` (or read the file directly).
- `templates/crx-doc-template.html` — the locked canonical skeleton; every document starts as a copy of it.
- `templates/doc-qa.py` — mechanical conformance gate.
- `templates/_fixtures/` — regression fixtures (HTML + rendered PDF pairs).
- `reference/crx-margin-settlement-overview-v5.html` — the reference implementation. SKILL.md cites it at `~/Downloads/…` on Jake's machine; in this bundle it lives here. When a rule is ambiguous, this file is the tiebreaker.

Render on macOS (body face is system Times New Roman), headless Chrome HTML→PDF.
