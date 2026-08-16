---
name: formatting-marketmaker-documents
description: Use when producing, formatting, or molding a formal CRX market-maker document — Margin and Settlement Overview, Collateral Overview, margin methodology, rules overview, mechanism memo, or any MM-facing one-pager/PDF. Also use when asked to format a CRX doc, match the CRX standard, or render a CRX HTML document to PDF. Not for LOIs, decks, emails, or web docs.
---

# Formatting Market-Maker Documents — the CRX MM document standard (v4.2)

> **Use this when…** producing any formal CRX market-maker document — the Margin and Settlement Overview, Collateral Overview, companion methodologies, rules overviews, mechanism memos, MM-facing one-pagers — or molding an existing document into the standard. Scoped to the MM document class, the same scope as [[writing-marketmaker-documents]]: that skill owns the prose of these documents, this one owns the page. Not for LOIs ([[drafting-legal-documents]]), decks ([[building-powerpoints]]), or web docs ([[writing-documentation]]).
> **What it does.** Locks one design system for all MM documents. Every document supplies content only; the look is decided once, here, and never per-document.
> **Canonical skeleton:** `templates/crx-doc-template.html` (this repo). Design v4 locked 2026-07-20 with Jake: the white-letterhead serif register, aligned to the house reference (`crx-margin-settlement-rules-overview (7).pdf` grammar — ISDA/rulebook paper), replacing the banded v3 look the same day. v4.1 furniture revision locked 2026-07-21 off the shipped Margin & Settlement Overview: footer strips removed (bare centered ink folio only), figures fully monochrome ink, minimal citations. QA gate: `templates/doc-qa.py`.
> **Reference implementation:** `~/Downloads/crx-margin-settlement-overview-v5.html` — the first document fully on this standard; when a rule here is ambiguous, that file is the tiebreaker.
> **Last updated:** 2026-07-23 (v4.2: section heads ink, teal on sups only; dashed-stroke message-connector convention added off the Flow of Funds Overview)

---

## 0. The governing principle: document class, not per-document styling

The pattern that makes LaTeX documents uniform across thousands of authors is the *document class*: one versioned style definition, and documents that carry only content. Steal it wholesale.

- **The template is the class.** `templates/crx-doc-template.html` holds the entire `<style>` block. A new document starts as a copy of the skeleton and edits only the content slots.
- **Documents never restyle.** No new fonts, sizes, colors, spacings, or element types inside a document. No `style=` attributes in content markup (sole exception: geometry attributes inside a figure's `<svg>`). A document that "needs" a new element is a signal to extend the template — make the change there, version it, then use it.
- **One source file.** Each document is a single self-contained HTML file (fonts and lockup inlined), rendered to PDF locally. The HTML is the source of truth; the PDF is a build artifact. One portability caveat: the primary serif is system Times New Roman (not embedded) — render on macOS; Charter subsets are embedded as the fallback.
- **The component inventory is closed.** Every element a document may contain is listed in §6. Content that cannot be expressed with those components extends the template first — never the document.

## 1. Register

The audience is trading desks and their risk officers. The document reads as an institutional paper — the ISDA/clearinghouse-rulebook grammar — carrying the CRX mark quietly: typeset conviction, zero marketing gloss, white page, one accent.

- Serif-led page: justified serif body, centered serif title, serif section heads. The brand sans (Diatype) survives only in small apparatus (masthead date, folio, flags, figure labels).
- Brand appears once per page: the monochrome ink lockup in the letterhead. **No band, no gradient anywhere** — the gradient asterisk belongs to digital/marketing surfaces; documents carry the ink lockup only (v4 reverses v3's banded masthead; Jake-decided 2026-07-20 against the reference file).
- **Color doctrine — one accent.** `--teal #135F52` (deep forest-teal, the reference's green in CRX's hue family) appears ONLY on superscript markers. Section heads are ink (teal heads retired, Jake 2026-07-23). Everything else is ink on white. Figures are entirely monochrome ink — the one-teal-emphasis-per-figure allowance is retired (Jake 2026-07-21).
- Density: the reference's paper set — 11pt/1.5 justified — composed as full sheets with footnotes and folio pinned to the bottom, never left to flow.
- **Minimal furniture.** No footer strip, no running title, no © line: the bottom of a sheet carries only the pinned footnotes (when the sheet has any) and a bare centered ink folio (Jake 2026-07-21). The document identifies itself once, in the title block; the letterhead carries the brand on every sheet.

**Language is owned by [[writing-marketmaker-documents]]** — register (clearinghouse content, protocol diction) and flow (purpose before mechanism, given→new chaining, lifecycle openers, cadence, compression floor). This skill owns how the page looks; that one owns how the prose reads. The purpose clause opening each section is a prose rule; on the page it sets in **plain text** — the bold lead-in was a v3 device and is retired (§6.2).

## 2. Page geometry (locked)

| Property | Value |
|---|---|
| Page | US Letter, 8.5 × 11in, `@page` margin 0 |
| Sheet padding | 0.55in top, 1in sides, 0.75in bottom |
| Sheet model | one `.sheet` div per page, flex column; `page-break-after: always` |
| Masthead | every sheet: ink lockup (13pt) left, date right, 0.5px `#9aa19d` hairline datum beneath (10px clearance), 0.32in below |
| Bottom anchoring | `.footnotes` pinned via `margin-top:auto` at the padding boundary (`margin-bottom:0`), the `.folio` 10px beneath — last ink naturally sits ≈0.77in from the paper edge; a sheet with no footnotes wraps its folio in `.footgroup` (which carries the `margin-top:auto`); a full sheet takes `.sheet.flush` (wrap head furniture and foot furniture each in one plain div so slack distributes only between content sections). There is no `footer` element in this class (removed 2026-07-21) |
| Variants | `.sheet.tight` (continuation sheets that must hold more), `.sheet.dense` (one-page documents) |
| Overflow discipline | content must fit its sheet. A section MAY split across sheets when pagination demands it (Jake relaxed atomicity 2026-07-20): the split point is between elements — prose completes on one sheet, the exhibit floats to the top of the next — never mid-paragraph, never mid-exhibit. Full sheets beat self-contained sections; bottom voids are the worse failure |

**Page capacity budgets** (plan pagination before filling slots; one body line = 11pt × 1.5 ≈ 0.23in):

| Sheet | Content height available | ≈ body lines |
|---|---|---|
| Sheet 1 (masthead + title) | ~8.5in | ~37 |
| Sheet 2+ (masthead only) | ~9.1in | ~39 |
| Sheet 1 `.dense` | ~8.6in | ~37 |
| Sheet 2+ `.tight` | ~9.1in (+~15% from tighter rhythm) | ~45 |
| Deductions | section head ≈ 0.32in · exhibit label ≈ 0.28in · table row ≈ 0.25in · figure ≈ its viewBox height · footnote line ≈ 0.16in + 0.35in block overhead | |

A sheet planned above ~90% of budget moves content or takes `.tight`. Never shrink type to fit.

**Flush rule:** `.sheet.flush` (vertical justification) only when the sheet is ≥85% full — on a short sheet the distributed slack reads as stretched gaps. Short sheets stay top-packed; the pinned footnotes/folio handle the bottom.

## 3. Type system (locked)

Primary serif is **Times New Roman** (system; the reference's face), falling back to embedded Charter. **Diatype** (embedded regular+bold subsets) carries only the small apparatus; it has no italic — nothing sans is ever italicized. The wordmark is outlined inside the lockup SVG. No third font ever, no new size ever.

| Role | Face | Size / weight | Treatment |
|---|---|---|---|
| Body, run-in definitions | Times/serif | 11pt / 400, lh 1.5 | **justified**, `hyphens:auto`, `hyphenate-limit-chars:8 3 3`, widows/orphans 2 |
| Document title | Times/serif | 13.5pt / 700 | **centered**, sheet 1 only, lh 1.3, ink. Modest by design — 16.5pt read oversized (Jake 2026-07-20) |
| Section heads (h2) | Times/serif | 10.5pt / 700 | UPPERCASE, tracking 0.02em, ink; numeral with period (`1.`) via `<span class="no">1.</span>`, same color |
| Exhibit labels | Times/serif | 10pt / italic | ink, `Exhibit N: Name` (colon separator — em dashes removed 2026-07-21, Jake) |
| Displayed formula | Times/serif | 11pt / italic | indented 24px, own line |
| Footnotes | Times/serif | 8.25pt / 400, lh 1.45 | hanging indent 11px; italic cited titles |
| Table cells | Times/serif | 9.75pt / 400 (`wide`: 9.25pt) | `tabular-nums` |
| Table headers | Times/serif | 9.5pt / 700 | sentence case — never uppercase, never sans (reference manner) |
| Masthead date | Diatype | 7.5pt / 400 | UPPERCASE, tracking 0.14em, `--muted`; drafts append `· DRAFT`, removed before external send |
| Folio | Diatype | 7pt / 400 | centered, **ink**, tracking 0.12em, `tabular-nums`; the bare page number alone — no rule, no running title |
| Figure labels | Diatype | 10 / 8.5 SVG units | UPPERCASE, letter-spacing 1 (SVG units), ink (secondary `--muted`) |
| Flags | Diatype | 6.5pt / 400 | UPPERCASE, `--flag` |

One heading level only, numbered sequentially with periods (`1.`, `2.`, …). Subsections promote to sections or demote to run-in bold leads.

## 4. Color tokens (locked)

| Token | Hex | Used for | Never used for |
|---|---|---|---|
| `--ink` | `#191b1a` | text, exhibit labels, folio, all figure strokes and labels | — |
| `--band` | `#0D2026` | table rules (top/header/bottom/total) | body text, backgrounds |
| `--teal` | `#135F52` | sups only | heads, figures, body text, rules, backgrounds |
| `--muted` | `#5a6663` | masthead date, tablenotes, figure secondary labels | body text |
| `--rowline` | `#c9cdca` | `.tx` row hairlines | text |
| `--flag` | `#8a6d00` | `[confirm: …]` flags | anything shipping |
| `.ph` | `#c00000` | unresolved placeholders | anything shipping |
| Masthead hairline | `#9aa19d` | the letterhead datum only | — |

No other hex may appear. No gradients, no fills, no background tints anywhere.

## 5. Masthead, title block, folio (locked)

- **Masthead (every sheet):** monochrome ink lockup (canonical asset baked into the template — never substitute; the asterisk is the three-capsule mark, not a fused star — the wrong glyph shipped in early v4 and was corrected 2026-07-21) at 13pt left; the date right (`MONTH YEAR`, masthead-date spec); a 0.5px hairline datum across the full measure beneath. The masthead never carries the document title, a series label, or navigation. The date lives here on every sheet — it is the running head's information.
- **Title block (sheet 1 only):** the document title centered, 13.5pt bold serif, 30px below→content. The rendered title may drop a leading "CRX" (`Margin and Settlement Overview` under a CRX letterhead); the file's `<title>` keeps it. No date line (it's in the masthead), no rule (whitespace separates). Sheets 2+ carry no title — the masthead alone runs.
- **Folio (every sheet):** the bare page number, centered, Diatype 7pt ink, 10px below the footnote block (or alone in `.footgroup` on a sheet without footnotes). Nothing else at the foot: no rule, no running title, no `Page X of Y`, no ©, no entity line (footer strip removed 2026-07-21, Jake). Folios by hand — verify in the rendered PDF. One-page documents drop the folio.

## 6. The component inventory (closed set)

### 6.1 Sections
`<section>` + `<h2><span class="no">N.</span>Name</h2>`. Numbered continuously.

### 6.2 Paragraphs
Plain text, justified. **No bold lead-ins** — the v3 bold purpose-opener is retired (Jake 2026-07-20: it fought the paper register; the reference has none). The section's purpose clause opens the first paragraph as plain prose. `<b>` in a paragraph is legal ONLY as a run-in definition (§6.7). `<i>` is for defined-term mentions and cited titles only.

### 6.3 Exhibits — tables (three modes)
One continuous exhibit counter across tables AND figures. Italic label above (`Exhibit N: Name`), optional muted-italic `.tablenote` beneath.

| Mode | Class | Width | Rules | Gutters |
|---|---|---|---|---|
| Numeric exhibit | (default) | auto (content-sized), indented 22px | booktabs three-rule: 1px top, 0.5px under header, 1px bottom — **no row lines** | 42px |
| Text matrix | `tx` | 100% | booktabs + 0.5px row hairlines (multi-line prose cells need row separation) | 14px |
| Full-measure numeric | `full` | 100% | booktabs three-rule, no row lines, 9.75pt (default type, spanning width) | 42px |
| Wide numeric (5+ cols) | `wide` | 100% | booktabs, no row lines, 9.25pt | 24px |

Numeric columns `class="n"` right-aligned, consistent units down a column. Headers bold serif sentence-case. A two-column exhibit that should span the measure takes `full` (100% width, no indent — the Portfolio IM table). Paired columns take a grouped-header spanner row: `tr.grp` + centered `th.g` colspans whose inner `<span>` draws a trimmed rule (margin-inset 22px left / 24px right, matching the gutters). Sibling `tx` tables sharing a first column (a definition table and its instantiation, like the collateral-model pair) take the same width utility on that column (`w34`) — auto layout would otherwise place their dividers at different positions and the mismatch reads as sloppiness once the tables sit near each other. Under a spanner, give the paired data columns equal width utilities (`w12`, `w19`) and group gutters: `gl` (22px left pad) opens each group, `pr` (24px right pad) restores the trailing gutter on the final column that `:last-child` strips — without both, the spanner rules sit asymmetrically over their columns (three-round lesson from Exhibit 2, 2026-07-21). Never vertical rules, fills, or zebra striping.

### 6.4 Exhibits — figures
Same label grammar, inline `<svg>` in `.figure`. **Entirely monochrome ink**: 1px strokes, no fills, square corners, Diatype labels — teal never appears in a figure (allowance retired 2026-07-21; the accent lives on sups alone). Grammar locked on the Margin & Settlement exhibits:

- **Canvas:** viewBox width 640 units, always — text then sets at a consistent size across every figure in the class; height sized to content.
- **Nodes:** rectangles carrying ONE line of text. Node labels 10 units (secondary node text 9.5), uppercase, `letter-spacing="1"`, ink. Flow-state boxes are 170×34.
- **Connectors:** orthogonal only — vertical/horizontal runs and right-angle `<path>` elbows, never diagonals (sole exception: a fan converging into an aggregator node). Arrowheads via a shared `<marker>` def: filled triangle `M0,0.6 L7,4 L0,7.4 Z`, `refX 6.5`, marker size 6.5. Solid strokes carry funds; message flows (an RFQ, a quote) may take a dashed stroke (`stroke-dasharray="5 4"`), keyed by a `.tablenote` beneath the figure — locked on the Flow of Funds Overview (2026-07-23).
- **Edge labels:** 8.5 units. Beside a short vertical arrow: offset right of the line, mid-run. On a long rail: set into a **railroad gap** — break the stroke and center the label (one or two stacked lines) in the gap. Above/below a horizontal arrow: centered on its span.
- **Flow direction:** vertical spine beats horizontal once states exceed ~4 — left-align the spine at the measure's edge, hang branches and side rails to the right. Keep side-loop arrows short (~110 units); long reaches read as slack.

Banned: shadows, gradients, rounded corners, fills, any second color, teal, two-line node labels, clip-art, icon fonts.

### 6.5 Formulas
`.formula`: serif italic on its own line, indented. Variables italic, operators upright, thin spaces around relations.

### 6.6 Clauses
`.clauses`: indented `(a) (b) (c)` paragraphs, one sentence each. The only list form — no bullets anywhere.

### 6.7 Run-in definitions
`<b>Term.</b> Definition…` as a paragraph — asset lists and glossaries. The ONLY bold allowed inside paragraphs. A definition-led section opens directly with its first run-in.

### 6.8 Footnotes
Page-bottom block pinned at the padding boundary (the folio sits beneath), continuous numbering, teal superscripts inline. Citation format: issuer, *italic title*, (date or `forthcoming`), bare domain — and nothing more. **Citations stay minimal**: no publisher rosters, example lists, or explanatory asides in a footnote (Jake 2026-07-21 — institutional papers cite, they don't elaborate; category-level detail belongs in the prose). Never `(here)` links-in-prose. A footnote appears on the sheet that references it.

### 6.9 Flags and placeholders
`[confirm: …]` flags (gold) and `.ph` placeholders (red) — internal drafts only; grep before external render. Draft state also shows in the masthead date (`· DRAFT`).

**Not in the inventory (banned):** footer strips and running feet, bold lead-ins, bullet lists, block quotes, callout boxes, code blocks, images/photographs, second heading levels, horizontal rules in content, colored text, background tints, bands or color bars, links styled as links.

## 7. Footnote/link mechanics

Links display as bare domains, inherit color, no underline, live URL in `href`. Cross-references to CRX companions are citations, never prose links. Superscripts render `--teal` at 68% in body and footnote block; subscripts 68% uncolored.

## 8. Content rules

- **Verify facts against `~/CRX Master Brain/company/overview.md` first.** Margin-model vocabulary locked: *margin account*, *margin engine*, *close-out netting*, portfolio-first VM, 48h cure window; never publish non-public calibration fractions.
- Prose passes through [[writing-marketmaker-documents]] (costume sweep → flow pass) BEFORE layout. Molding = language pass first, then format pass.
- Banned constructions: never "so"; never sentence-initial "Because"; em dashes nowhere — exhibit labels use a colon (`Exhibit 1: Portfolio IM`).
- Regulatory care per [[drafting-legal-documents]]: no legal terms of art characterizing CRX.

## 9. The molding procedure — any document → this standard

1. **Inventory the source**: every heading, paragraph, table, diagram, formula, list, note, citation, image.
2. **Map to components:**

| Source element | Becomes | If it doesn't fit |
|---|---|---|
| H1 / title | Title block | — |
| H2 | Numbered section | — |
| H3+ | Promote to section or demote to run-in | never a third level |
| Emphasized/bold opener | Plain prose | bold lead-ins never survive |
| Bullet list | Prose, or `.clauses` if genuinely enumerable | bullets never survive |
| Table | Exhibit (default / `tx` / `wide`, `tr.grp` for paired columns) | >6 columns: split or restructure, never shrink below spec |
| Diagram / image | Redraw as §6.4 figure | photographs don't survive |
| Formula | `.formula` | — |
| Callout / note box | Body prose or footnote | boxes never survive |
| Inline link | Bare-domain link or footnote citation | — |
| Code block | Not in this class | route to dev docs |

3. **Language pass** ([[writing-marketmaker-documents]]): costume sweep, flow pass, facts frozen.
4. **Plan pagination** against §2 budgets; place each exhibit on its referencing sheet; distribute footnotes; assign folios.
5. **Fill the skeleton**: copy `templates/crx-doc-template.html` → `crx-<topic>-v1.html`; fill slots; delete the component shelf; never touch `<style>`.
6. **Render and verify** (§10).
7. **Run the conformance gate** (§11). Class-level gaps fix the template, then get documented here.

## 10. Production pipeline

1. **Render:**
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
     --headless --disable-gpu --no-pdf-header-footer \
     --print-to-pdf="crx-<topic>-v1.pdf" crx-<topic>-v1.html
   ```
2. **Verify mechanically with the QA probe** (`templates/doc-qa.py`, needs Pillow):
   ```bash
   python3 ~/jake-skills/templates/doc-qa.py crx-<topic>-v1.html
   ```
   Both failure modes: page count ≠ sheet count (overflow past the page edge) AND per-sheet bottom clearance <0.7in (content silently eating the foot margin — flex overflows into padding without splitting; the page count alone cannot see it). The natural pinned position measures ≈0.77in. Fallback count check: `grep -ao '/Count [0-9]*' file.pdf | head -1` (never `mdls` — null on unindexed paths). Fallback clearance check when Pillow is unavailable: `pdftotext -bbox file.pdf -`, take max `yMax` per page (attributes are camelCase), clearance = (792 − max)/72.
3. **Visual verify in the PDF:** masthead + hairline + date on every page; title centered 13.5pt; serif faces render (a Helvetica-looking element = missed glyph or missing Times); tables in their correct mode; nothing clipped.
4. **Version:** revisions bump `-vN` on both files; HTML and PDF ship as a pair.

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

Visual checklist, in the rendered PDF:

- [ ] Ink lockup + date + hairline datum on every page; no band, no gradient anywhere
- [ ] Title centered, 13.5pt bold, sheet 1 only
- [ ] No bold in paragraphs except run-in definitions
- [ ] Exhibit numbering continuous across tables and figures; each on its referencing sheet; correct table mode per §6.3
- [ ] Table headers bold serif sentence-case; numeric exhibits content-sized and indented; grouped spanners centered over equal columns
- [ ] Figures entirely monochrome ink on a 640-unit canvas; orthogonal connectors; one-line node labels
- [ ] Section heads render INK (a teal head = stale pre-v4.2 class)
- [ ] Footnotes continuous and minimal, teal sups resolve; bare centered ink folios sequential; no footer strip anywhere
- [ ] `doc-qa.py` passes: count match AND every sheet ≥0.7in bottom clearance
- [ ] Facts verified against the brain; banned constructions swept; no flags/placeholders/DRAFT on external sends

## 12. Regression fixtures

`templates/_fixtures/` holds `crx-fixture-methodology.html` (3 sheets: formulas, 6-col `wide` table, two figures, clauses, `tight`, draft flags) and `crx-fixture-one-pager.html` (`dense` single sheet). After ANY template change: re-render both, run `doc-qa.py` on both (3 and 1), and eyeball against §3–§6 before committing. The v4 validation run (2026-07-20/21) additionally molded the Margin & Settlement Overview and Collateral Overview as live-content tests; defects found and folded back: `wide` tables lost their tight gutters in the redesign (col-1 wrap with right slack), run-in bolds must survive lead-in retirement (length-gated unwrap), figure emphasis had to follow the deepened accent. The v4.1 furniture revision (2026-07-21) re-validated both fixtures: counts match, clearance 0.77in per sheet (0.90in on the dense one-pager, which drops its folio — a one-page document numbers nothing).

## 13. Provenance

Distills: the LaTeX document-class model; booktabs doctrine (Butterick, CSE) — restored in v4 for numeric exhibits (row hairlines survive only in `tx` prose matrices); the ISDA/clearinghouse paper grammar via the house reference `crx-margin-settlement-rules-overview (7).pdf` (white letterhead, centered serif title, green serif heads, justified Times, indented example tables) — Jake-locked 2026-07-20, superseding the banded 04×05 gallery design the same day (gallery record: `~/Downloads/crx-doc-style-gallery.html`); the exhibit-numbering, molding, and QA machinery retained from v3. v4.1 (2026-07-21, off the shipped Margin & Settlement Overview v5): footer strips removed for bare centered ink folios, footnotes dropped to the padding boundary, figures locked to monochrome ink with the 640-unit orthogonal grammar (vertical account-states spine, railroad-gap rail labels), grouped-spanner gutter mechanics (`gl`/`pr`/width utilities), minimal citations, capsule-asterisk lockup correction.

Related skills: [[writing-marketmaker-documents]] (prose), [[building-powerpoints]] (decks), [[drafting-legal-documents]] (LOIs — a letter, not this standard), [[writing-documentation]] (web docs).
