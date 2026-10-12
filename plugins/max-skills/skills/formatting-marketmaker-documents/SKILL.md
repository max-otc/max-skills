---
name: formatting-marketmaker-documents
description: Use when producing, formatting, or molding a formal CRX market-maker document — Margin and Settlement Overview, Collateral Overview, margin methodology, rules overview, mechanism memo, or any MM-facing one-pager/PDF. Also use when asked to format a CRX doc, match the CRX standard, or render a CRX HTML document to PDF. Not for LOIs, decks, emails, or web docs.
---

# Formatting Market-Maker Documents: CRX MM document standard (v4.2)

Scope: the formal CRX market-maker documents in the description, new or molded. This skill owns the page; [[writing-marketmaker-documents]] owns the prose. LOIs → [[drafting-legal-documents]] (a letter, not this standard); decks → [[building-powerpoints]]; web docs → [[writing-documentation]].

Skeleton and QA gate: `templates/` (this repo). Tiebreaker for ambiguous rules: the reference implementation `~/Downloads/crx-margin-settlement-overview-v5.html`, the first document fully on this standard. Last updated 2026-07-23 (v4.2); rulings in §13.

## 0. Document class

LaTeX *document class* model: the template is the class; documents carry content only.

- `templates/crx-doc-template.html` holds the entire `<style>` block. Copy it; edit only the content slots.
- No new fonts, sizes, colors, spacings or element types inside a document. No `style=` in content markup (sole exception: geometry attributes inside a figure's `<svg>`).
- §6 is closed. A new element goes into the template first: change it, version it, then use it.
- One self-contained HTML file (fonts and lockup inlined) is the source of truth; the PDF is a build artifact, rendered locally. Times New Roman is system, not embedded: render on macOS. Embedded Charter subsets are the fallback.

## 1. Register

Audience: trading desks and their risk officers. An institutional paper in the ISDA/clearinghouse-rulebook grammar: typeset conviction, zero marketing gloss, white page, one accent, the CRX mark quiet. Sheets are composed full, never left to flow.

[[writing-marketmaker-documents]] owns language: register (clearinghouse content, protocol diction) and flow (purpose before mechanism, given→new chaining, lifecycle openers, cadence, compression floor). Its pass (costume sweep → flow pass) runs BEFORE layout.

## 2. Page geometry (locked)

- Page: US Letter 8.5 × 11in, `@page` margin 0. Sheet padding 0.55in top, 1in sides, 0.75in bottom.
- One `.sheet` div per page: flex column, `page-break-after: always`.
- Masthead (every sheet): ink lockup (13pt) left, date right, 0.5px `#9aa19d` hairline datum beneath (10px clearance), 0.32in below.
- Bottom: `.footnotes` pinned at the padding boundary (`margin-top:auto`, `margin-bottom:0`), `.folio` 10px beneath; last ink ≈0.77in from the paper edge. No footnotes: the folio goes in `.footgroup`, which carries the `margin-top:auto`. No `footer` element.
- A full sheet (≥85% full) takes `.sheet.flush` (vertical justification); wrap head and foot furniture each in one plain div, so slack spreads only between content sections. Shorter sheets stay top-packed (spread slack reads as stretched gaps).
- `.sheet.tight`: continuation sheets that must hold more. `.sheet.dense`: one-page documents.
- Content must fit its sheet. A section MAY split across sheets when pagination demands it, between elements (prose completes; the exhibit floats to the top of the next sheet), never mid-paragraph or mid-exhibit. Full sheets beat self-contained sections; bottom voids are the worse failure.

Capacity budgets (one body line = 11pt × 1.5 ≈ 0.23in):

| Sheet | Content height | ≈ body lines |
|---|---|---|
| Sheet 1 (masthead + title) | ~8.5in | ~37 |
| Sheet 2+ (masthead only) | ~9.1in | ~39 |
| Sheet 1 `.dense` | ~8.6in | ~37 |
| Sheet 2+ `.tight` | ~9.1in (+~15% from tighter rhythm) | ~45 |
| Deductions | section head ≈ 0.32in · exhibit label ≈ 0.28in · table row ≈ 0.25in · figure ≈ its viewBox height · footnote line ≈ 0.16in + 0.35in block overhead | |

Above ~90% of budget: move content or take `.tight`. Never shrink type to fit.

## 3. Type system (locked)

Serif: **Times New Roman** (the reference's face; Charter fallback, §0). **Diatype** (embedded regular+bold subsets): small apparatus only (roles below). Diatype has no italic: never italicize sans. Wordmark outlined in the lockup SVG. No third font, no new size, ever.

Serif roles:
- **Body, run-in definitions:** 11pt/400, lh 1.5; **justified**, `hyphens:auto`, `hyphenate-limit-chars:8 3 3`, widows/orphans 2.
- **Document title:** 13.5pt/700, lh 1.3, ink; **centered**, sheet 1 only.
- **Section heads (h2):** 10.5pt/700, UPPERCASE, tracking 0.02em, ink; numeral with period via `<span class="no">1.</span>`, same color.
- **Exhibit labels:** 10pt italic, ink, `Exhibit N: Name` (colon).
- **Displayed formula:** 11pt italic, indented 24px, own line.
- **Footnotes:** 8.25pt/400, lh 1.45; hanging indent 11px; italic cited titles.
- **Table cells:** 9.75pt/400 (`wide`: 9.25pt), `tabular-nums`. **Headers:** 9.5pt/700, sentence case; never uppercase, never sans (reference manner).

Diatype roles:
- **Masthead date:** 7.5pt/400, UPPERCASE, tracking 0.14em, `--muted`. Drafts append `· DRAFT`, removed before external send.
- **Folio:** 7pt/400, centered, **ink**, tracking 0.12em, `tabular-nums`; bare page number only.
- **Figure labels:** 10 / 8.5 SVG units, UPPERCASE, letter-spacing 1 (SVG units), ink (secondary `--muted`).
- **Flags:** 6.5pt/400, UPPERCASE, `--flag`.

One heading level, numbered `1.`, `2.`, …. Subsections promote to sections or demote to run-in bold leads.

## 4. Color tokens (locked)

- `--ink` `#191b1a`: text, exhibit labels, folio, all figure strokes and labels.
- `--band` `#0D2026`: table rules (top/header/bottom/total). Never body text or backgrounds.
- `--teal` `#135F52`: sups only. Never heads, figures, body text, rules or backgrounds.
- `--muted` `#5a6663`: masthead date, tablenotes, figure secondary labels. Never body text.
- `--rowline` `#c9cdca`: `.tx` row hairlines. Never text.
- `--flag` `#8a6d00`: `[confirm: …]` flags. Never anything shipping.
- `.ph` `#c00000`: unresolved placeholders. Never anything shipping.
- Masthead hairline `#9aa19d`: the letterhead datum only.

`--teal` (deep forest-teal, the reference's green in CRX's hue family) is the one accent; all else is ink on white. No other hex. No bands, gradients, fills or background tints anywhere.

## 5. Masthead, title block, folio (locked)

- **Masthead (every sheet, geometry §2):** the monochrome ink lockup is the brand's one appearance per page: the canonical template asset, never substituted. Its asterisk is the three-capsule mark, not a fused star. The gradient asterisk is for digital/marketing surfaces only. Date (`MONTH YEAR`) is the running head. The hairline datum runs the full measure. No title, series label or navigation.
- **Title block (sheet 1 only, spec §3):** 30px below→content. It may drop a leading "CRX" (`Margin and Settlement Overview` under a CRX letterhead); the file's `<title>` keeps it. No date line, no rule. The document names itself only here; the letterhead carries the brand on every sheet.
- **Folio (every sheet, spec §2–§3):** nothing else at the foot: no footer strip, rule, running title, `Page X of Y`, © or entity line. Set folios by hand; verify in the PDF. One-page documents drop the folio.

## 6. Component inventory (closed)

**6.1 Sections.** `<section>` + `<h2><span class="no">N.</span>Name</h2>`, numbered continuously.

**6.2 Paragraphs.** Plain justified text. No bold lead-ins: the section's purpose clause opens the first paragraph as plain prose. `<b>` only per §6.7; `<i>` only for defined-term mentions and cited titles.

**6.3 Tables.** One exhibit counter across tables AND figures. Italic label above (`Exhibit N: Name`); optional muted-italic `.tablenote` beneath.

| Mode | Class | Width | Rules | Gutters |
|---|---|---|---|---|
| Numeric exhibit | (default) | auto (content-sized), indented 22px | booktabs: 1px top, 0.5px under header, 1px bottom; **no row lines** | 42px |
| Text matrix | `tx` | 100% | booktabs + 0.5px row hairlines (multi-line prose cells) | 14px |
| Full-measure numeric | `full` | 100% | booktabs, no row lines, 9.75pt | 42px |
| Wide numeric (5+ cols) | `wide` | 100% | booktabs, no row lines, 9.25pt | 24px |

- Numeric columns `class="n"`: right-aligned, consistent units down a column.
- `full`: a two-column exhibit spanning the measure, no indent (e.g. the Portfolio IM table).
- Paired columns: spanner row `tr.grp`, centered `th.g` colspans; the inner `<span>` draws a trimmed rule (margin-inset 22px left / 24px right, matching the gutters). Paired data columns take equal width utilities (`w12`, `w19`); `gl` (22px left pad) opens each group; `pr` (24px right pad) restores the trailing gutter `:last-child` strips from the final column. Without both, spanner rules sit off-center (three-round lesson, Exhibit 2, 2026-07-21).
- Sibling `tx` tables sharing a first column (e.g. the collateral-model definition table and its instantiation) take one width utility on it (`w34`); auto layout misaligns their dividers.
- No vertical rules, fills or zebra striping.

**6.4 Figures.** Inline `<svg>` in `.figure`, same label grammar. Monochrome ink: 1px strokes, Diatype labels. Grammar locked on the Margin & Settlement exhibits:

- Canvas: viewBox width always 640 units (one text size across figures); height fits content.
- Nodes: rectangles, ONE line of text. Labels 10 units (secondary 9.5), uppercase, `letter-spacing="1"`, ink. Flow-state boxes 170×34.
- Connectors: orthogonal (vertical/horizontal runs, right-angle `<path>` elbows). Diagonals only for a fan converging into an aggregator node. Arrowheads: shared `<marker>` def, filled triangle `M0,0.6 L7,4 L0,7.4 Z`, `refX 6.5`, marker size 6.5. Solid strokes carry funds. Message flows (an RFQ, a quote) may take `stroke-dasharray="5 4"`, keyed by a `.tablenote` beneath.
- Edge labels: 8.5 units. Short vertical arrow: right of the line, mid-run. Long rail: a **railroad gap** (break the stroke; center one or two stacked lines in it). Horizontal arrow: centered above/below its span.
- Flow: past ~4 states, a vertical spine beats horizontal. Left-align it at the measure's edge; hang branches and side rails right. Side-loop arrows short (~110 units); long reaches read as slack.

Banned in figures: shadows, gradients, rounded corners, fills, any second color, teal, two-line node labels, clip-art, icon fonts.

**6.5 Formulas.** `.formula`: serif italic, own line, indented. Variables italic, operators upright, thin spaces around relations.

**6.6 Clauses.** `.clauses`: indented `(a) (b) (c)` paragraphs, one sentence each. The only list form; no bullets anywhere.

**6.7 Run-in definitions.** `<b>Term.</b> Definition…` paragraphs, for asset lists and glossaries. The ONLY bold inside paragraphs. A definition-led section opens with its first run-in.

**6.8 Footnotes.** Pinned per §2; continuous numbering; teal sups inline; each on the sheet that references it. Citation: issuer, *italic title*, (date or `forthcoming`), bare domain. Nothing more: no publisher rosters, example lists or asides; category-level detail goes in the prose. Never `(here)` links in prose.

**6.9 Flags and placeholders.** `[confirm: …]` flags (gold), `.ph` placeholders (red): internal drafts only, like the `· DRAFT` date (§3); grep before external render.

**Banned (not in the inventory):** footer strips and running feet, bold lead-ins, bullet lists, block quotes, callout boxes, code blocks, images/photographs, second heading levels, horizontal rules in content, colored text, background tints, bands or color bars, links styled as links.

## 7. Link mechanics

Links show bare domains, inherit color, no underline, live URL in `href`. Cross-references to CRX companions are citations, never prose links. Superscripts `--teal` at 68% in body and footnotes; subscripts 68%, uncolored.

## 8. Content rules

- **Verify facts against `~/CRX Master Brain/company/overview.md` first.** Locked margin vocabulary: *margin account*, *margin engine*, *close-out netting*, portfolio-first VM, 48h cure window. Never publish non-public calibration fractions.
- Banned: "so"; sentence-initial "Because"; em dashes anywhere (exhibit labels use a colon: `Exhibit 1: Portfolio IM`).
- Regulatory care per [[drafting-legal-documents]]: no legal terms of art characterizing CRX.

## 9. Molding procedure

1. Inventory the source: every heading, paragraph, table, diagram, formula, list, note, citation, image.
2. Map to components:
   - H1 / title → title block. H2 → numbered section. H3+ → promote to section or demote to run-in; never a third level.
   - Emphasized/bold opener → plain prose. Bullet list → prose, or `.clauses` if genuinely enumerable.
   - Table → exhibit (default / `tx` / `wide`, `tr.grp` for paired columns). Over 6 columns: split or restructure; never shrink below spec.
   - Diagram / image → redrawn §6.4 figure. Formula → `.formula`. Callout / note box → body prose or footnote. Inline link → bare-domain link or footnote citation. Code block → not in this class; route to dev docs.
   - Never survive: bold lead-ins, bullets, boxes, photographs.

3. Language pass (§1) before the format pass: costume sweep, flow pass, facts frozen.
4. Plan pagination against the §2 budgets, before filling slots: each exhibit on its referencing sheet; distribute footnotes; assign folios.
5. Copy `templates/crx-doc-template.html` → `crx-<topic>-v1.html`; fill slots; delete the component shelf; never touch `<style>`.
6. Render and verify (§10).
7. Run the gate (§11). Class-level gaps: fix the template, then document them here.

## 10. Production pipeline

1. Render:
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
     --headless --disable-gpu --no-pdf-header-footer \
     --print-to-pdf="crx-<topic>-v1.pdf" crx-<topic>-v1.html
   ```
2. QA probe (`templates/doc-qa.py`, needs Pillow):
   ```bash
   python3 ~/jake-skills/templates/doc-qa.py crx-<topic>-v1.html
   ```
   It fails on page count ≠ sheet count (overflow past the page edge) OR any sheet's bottom clearance <0.7in (flex overflows into padding without splitting; the page count cannot see it).
   - Fallback count: `grep -ao '/Count [0-9]*' file.pdf | head -1`. Never `mdls` (null on unindexed paths).
   - Fallback clearance without Pillow: `pdftotext -bbox file.pdf -`; max `yMax` per page (camelCase attributes); clearance = (792 − max)/72.
3. Check the PDF by eye (§11).
4. A revision bumps `-vN` on both files; HTML and PDF ship as a pair.

## 11. Conformance gate (run before any send)

```bash
f=crx-<topic>-vN.html
# 1. no inline styling in content (svg geometry excepted)
grep -n 'style="' "$f" | grep -v '<svg\|<rect\|<line\|<path\|<text\|<circle'
# 2. no colors outside the locked set
grep -no '#[0-9a-fA-F]\{3,6\}' "$f" | grep -viv '191b1a\|0D2026\|135F52\|5a6663\|c9cdca\|8a918d\|9aa19d\|8a6d00\|c00000\|ffffff\|fff'
# 3. draft artifacts
grep -n 'class="ph"\|\[confirm\|&middot; Draft' "$f"
# 4. em dashes (banned everywhere; exhibit labels use a colon)
grep -n '&mdash;\|—' "$f" | grep -v '<!--'
# 5. banned furniture: footer strips, teal inside figures
grep -n '<footer' "$f"
awk '/<svg/,/<\/svg>/' "$f" | grep -n '135F52'
# 6. banned elements incl. bold lead-ins (any <b> opening a paragraph at length)
grep -n '<ul\|<ol\|<h3\|<blockquote\|<code\|<img ' "$f" | grep -v 'band'
grep -no '<p><b>[^<]\{26,\}' "$f"
```

Visual checklist, rendered PDF:

- [ ] Every page: ink lockup, date, hairline datum; no band, gradient or footer strip
- [ ] Title centered, 13.5pt bold, sheet 1 only; heads INK (a teal head = stale pre-v4.2 class); bold only in run-ins
- [ ] Serif faces render (Helvetica-looking = missed glyph or missing Times); nothing clipped
- [ ] Exhibits numbered continuously across tables and figures, each on its referencing sheet, in its §6.3 mode; headers bold serif sentence case; numeric exhibits content-sized and indented; spanners centered over equal columns
- [ ] Figures: monochrome ink, 640-unit canvas, orthogonal, one-line nodes
- [ ] Footnotes continuous and minimal; teal sups resolve; bare centered ink folios sequential
- [ ] `doc-qa.py` passes: count match AND every sheet ≥0.7in bottom clearance
- [ ] Facts verified against the brain; banned constructions swept; no flags, placeholders or DRAFT on external sends

## 12. Regression fixtures

`templates/_fixtures/`: `crx-fixture-methodology.html` (3 sheets: formulas, 6-col `wide` table, two figures, clauses, `tight`, draft flags) and `crx-fixture-one-pager.html` (`dense`, single sheet). After ANY template change: re-render both, run `doc-qa.py` on both (3 and 1), check them by eye against §3–§6 before committing.

The v4 run (2026-07-20/21) also molded the Margin & Settlement and Collateral Overviews and folded back: `wide` tables lost their tight gutters (col-1 wrap, right slack); run-in bolds must survive lead-in retirement (length-gated unwrap); figure emphasis had to follow the deepened accent. v4.1 (2026-07-21): both fixtures pass, clearance 0.77in per sheet; 0.90in on the folio-less dense one-pager.

## 13. Rulings and provenance

Version history:
- **v4, 2026-07-20, locked with Jake:** white-letterhead serif register after the house reference `crx-margin-settlement-rules-overview (7).pdf` (ISDA/clearinghouse paper: white letterhead, centered serif title, green serif heads, justified Times, indented example tables). Replaced banded v3 and the banded 04×05 gallery design (record: `~/Downloads/crx-doc-style-gallery.html`). No band or gradient (decided against the reference file); title 13.5pt (16.5pt read oversized); bold lead-ins retired (fought the paper register; the reference has none); sections may split.
- **v4.1, 2026-07-21,** off the shipped Margin & Settlement Overview v5. Jake ruled: bare centered ink folios, footer strips removed; figures fully monochrome ink, teal emphasis retired; minimal citations; colon exhibit labels. Also: footnotes at the padding boundary; the 640-unit orthogonal figure grammar (vertical account-states spine, railroad-gap labels); spanner gutters (`gl`/`pr`/width utilities); capsule-asterisk lockup (early v4 shipped a fused star).
- **v4.2, 2026-07-23:** heads ink, teal on sups only (Jake); dashed message connectors (Flow of Funds Overview).

Sources: LaTeX document class; booktabs doctrine (Butterick, CSE), restored in v4 for numeric exhibits; v3's exhibit numbering, molding and QA machinery.
