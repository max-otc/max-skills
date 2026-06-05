---
name: max-doc
description: Use when the user wants to write or rewrite documentation — a docs site, a docs page, a README, help content, an explainer — in Max's house style. Triggers on "write the docs", "rewrite this doc", "docs page", "document this", "make a docs site", "plan the docs", "help page", "the docs are too verbose / too long", "turn this into docs", "explain this in the docs".
---

# Max Doc

## Overview

You write documentation the way Max reads it: a set of real questions a real reader asks, each answered in the fewest words that teach. Not a tour of the system. Not a brochure. Not an essay.

The deliverable is a small set of pages, each built around one reader and the questions that reader actually has — terse, front-loaded, and honest about what is not true yet.

The user points you at a product, a codebase, or an existing doc set. You **plan the learning paths first**, then write.

## Core Principle

**A weak doc explains the system. A doc that teaches answers the reader's next question.**

Nobody opens the docs to admire the architecture. They open them stuck on one question. Find the question, answer it, stop. Then the next question.

State the fact and stop. Do not explain life.

## When to Use

- "Write / rewrite the docs" for a product or feature
- "Document this" · "make a docs site" · "help page" · "README"
- "These docs are too long / too verbose / full of fluff"
- "Plan the docs" — what pages, for whom, in what order
- Any rendered explainer the reader chose to read

**Do NOT use for:**

- Marketing copy, ad angles, landing pages → `max-marketing`
- Video scripts → `max-video` / `max-explainer-video`
- Code comments — those stay conventional and live next to the code

## Foundations — the canon

You stand on the documentation canon. Six frameworks, one line each:

- **Diátaxis** (Daniele Procida) — docs come in four modes: **tutorial** (learning by doing), **how-to** (a task), **reference** (look-up), **explanation** (understanding why). Each serves a different need; one page never mixes two. See law 11.
- **Feynman Technique** (Richard Feynman) — explain it to a novice in plain words. The moment you reach for jargon, you have found the gap you don't actually understand. Close it, then write.
- **Every Page Is Page One** (Mark Baker) — readers arrive mid-stream from search, not from page one. Every page stands alone, sets its own context, and links out.
- **Minimalism** (John Carroll, *The Nurnberg Funnel*) — start from the reader's real task, cut everything that isn't it, and help them recover from errors. Less is more.
- **Pyramid Principle** (Barbara Minto) — lead with the answer, then the supporting points grouped beneath it. Never make the reader wait for the conclusion.
- **Curse of Knowledge** (Pinker; Heath brothers) — the expert forgets what the novice doesn't know. It is the disease every law below treats. Re-read your draft as the reader who knows nothing.

## The method — eleven laws

### 1. Plan the learning paths before writing a word.

List each party who will read — each role or persona. For each, write the ordered questions they actually have. Cut every topic no one asks. The page set is the union of those questions, and nothing more. Each cluster becomes one page in one mode (law 11).

Then run the page map against two tests — this is MECE, applied:

- **No overlap** (mutually exclusive): no question is answered on two pages. Two pages that answer the same question are one page split in half — merge them, and point every other page at the single home.
- **No gap** (collectively exhaustive): every real reader question has exactly one page that owns it. A question with no home is a missing page. A page with no question behind it is an invented page — cut it.

This is also how you refactor an existing doc set. Don't read it page by page. List its current pages, list the reader's real questions beside them, then map one to the other: questions that share a page split out, pages that share a question fold together, orphan pages (no question) get cut, orphan questions (no page) get written. The map drives the edits — not the order the old docs happened to be in.

> A doc set is the questions a reader asks, in order — each with one home, none missing.

### 2. Every heading is a question.

Phrase each `##` as the reader's question, in their words: *"Where is my money held?"*, *"What if I run out?"*. The first sentence answers it. Mechanism after.

### 3. Build from the simplest idea up.

Define each term the moment you use it, in plain words. No acronym before it is unpacked once. No leap the reader cannot follow. Teach the thing the thing depends on, first. That is the Feynman move.

### 4. Terse. Vital facts only.

Short sentences. No analogy where the literal claim works. No scene-setting, no storytelling, no closing aphorism, no "explaining life." Cut every sentence that does not teach.

### 5. No TL;DR.

The answer is already the first sentence of each section. A summary block on top only repeats it. Delete it.

### 6. Structure carries the meaning.

- Front-load: conclusion first, evidence after.
- Bullets for any list of 3+ items.
- Tables for any comparison of ≥ 3 rows.
- A time estimate on every internal link: `[Margin](/docs/margin) (~4 min)`.
- One register per section. Closed endings — a fact or a next link, never a trail-off.

### 7. State what is not true, out loud.

Every limitation gets its own bolded line, never buried mid-paragraph: **testnet only**, **mocked in the MVP**, **roadmap, not live**. Never overclaim. A reader who catches one buried caveat distrusts the whole page.

### 8. One true story.

Every page agrees with the canonical source. When a page contradicts the truth, fix it — do not preserve a comfortable simplification because it reads well.

### 9. Every reference must resolve.

Any link, diagram id, or asset you cite must exist. Verify against the real registry or source. A fabricated id renders broken, and silently. Grep before you cite.

### 10. Answer a how-to as a path, not a paragraph.

For anything the reader *does*, set the context first, then give the concrete steps — *click here, then do this* — then state what happens, including the branch — *it binds, or it expires*. A procedure buried in prose, or missing its outcome, leaves the reader unsure they did it right.

### 11. One page, one mode (Diátaxis).

Every page is exactly one of four modes. Declare it in the frontmatter (`mode:`) and obey its contract:

| Mode | Answers | Contract |
|---|---|---|
| **Tutorial** | "take me through it the first time" | a guided run that always works — no choices, no theory |
| **How-to** | "how do I do X?" | numbered steps to a goal; the click-path and the outcome (law 10) |
| **Reference** | "what exactly is X?" | dry, complete, scannable; no teaching, no opinion |
| **Explanation** | "why does it work this way?" | the reasoning and trade-offs; no steps |

A how-to that drifts into theory, or a reference that starts teaching, is two half-pages. Split it.

## The voice — before / after

> **Before:** *"You manage inventory the way an FX desk always has: you shade the one number you quote. Long the pair already? Skew the rate to quote away the side that adds to your position and toward the side that flattens it. You do this on demand, one RFQ at a time…"*
>
> **After:**
> **## How do I quote to manage inventory?**
> An RFQ lands on your desk. Before you send a rate:
> 1. Check your position on the pair — top-right of the desk.
> 2. Already long? Quote a worse rate on the side that adds to your position, a better one on the side that flattens it.
> 3. Send the quote, or click **Decline** to pass.
>
> Then one of two things happens: the taker accepts and the position binds, moving you toward flat — or the quote expires and nothing changes.

Context, then the click-path, then the outcome and its branch. Not a paragraph about how desks "always" work.

## Diagrams — the visual grammar

Add a diagram only where a visual carries what a sentence can't — a flow, a sequence, a branch, a hierarchy. If the prose already shows it, skip it. When one earns its place, build it in this grammar:

- **Number the stages.** Each stage gets a tracked-caps kicker: `1 · REQUEST FOR QUOTE`, `2 · ON TRADE ACCEPTANCE`. The number gives the order at a glance.
- **Keep boxes simple.** A bold title (`CRX`) and one small grey sub-label (`RFQ system`). Nothing else inside.
- **Every arrow is a verb.** Left to right, labeled with the action it carries: `Request quote`, `Broadcast`. Use a return arrow for the response — `Request quote →` / `← Quotes returned`.
- **One accent, one meaning.** White boxes, thin borders, for steps. One accent colour to mark the reader's own actor. A single dark-filled box for the terminal result — the thing the whole flow produces. No decorative colour.
- **A pill marks a branch.** Put a fork in a rounded pill between stages: `Aspora accepts ✓ or rejects ✗`.
- **Let it breathe.** 3–5 boxes per row, a thin divider between stages, generous whitespace.

Every box is a noun the reader recognises; every arrow is a verb. Read left to right, top to bottom — the numbered stages are the spine.

Reference shape (the CRX Trade Flow):

```
1 · REQUEST FOR QUOTE

 ┌─────────┐   Request quote →    ┌─────────┐   Broadcast →    ┌ Maker A ┐
 │ ASPORA  │ ───────────────────  │   CRX   │ ───────────────  │ Maker B │
 │  Taker  │   ← Quotes returned  │ RFQ sys │   ← Quotes        └ Maker C ┘
 └─────────┘                      └─────────┘

              ( Aspora accepts ✓   or rejects ✗ )

2 · ON TRADE ACCEPTANCE

 ┌ Margin posted ┐ →  ┌ Margined daily ┐ →  ┌■ Settles in USDC ■┐
   CRX Core opens       variation margin       at maturity, vs fixing
```

The reader's actor (`ASPORA`) is accented; the result (`Settles in USDC`) is the one filled box.

Implementation: build it as one small static SVG or component — no runtime data, no JS. In a registry-based docs system, add it once and reference it by id, then verify the id resolves (law 9). A diagram that renders "unknown" is worse than no diagram.

## Process

1. **Plan.** Per reader, the ordered questions (law 1). Show the page map — survive / merge / cut. If the cut is large, get a nod before writing.
2. **Write.** One page at a time. Question headings, answer-first, terse (laws 2–7).
3. **Cut.** Merge duplicates. Delete pages no reader needs. Fewer pages, each load-bearing.
4. **Validate.** No TL;DR blocks. Every link resolves. Every diagram and asset id exists. Frontmatter complete. Honesty lines present.

## Page template

- **Frontmatter:** title (a question or a short noun phrase), one-line description, **mode** (tutorial / how-to / reference / explanation), order, group.
- **Body:** question sections only. No TL;DR.
- A short **`Next:`** link line at the end, with a time estimate.
- A glossary only if the page introduces more than 3 new terms.

## Strict rules

- No TL;DR. No closing aphorisms. No analogy where the literal claim works.
- Short sentences. Vital facts only. Cut anything that does not teach.
- Every heading is the reader's real question.
- Plan the per-reader question list before writing.
- State every limitation in its own bolded line.
- Verify every link and asset id against the source before shipping.

## Quality checks before finishing

- Did you plan the per-reader question list, and cut topics no one asks?
- Is the page map MECE — no question answered on two pages (overlap → merge), no real question without a page (gap → write it)?
- Is every `##` a real reader question, answered in the first sentence?
- Is each page exactly one Diátaxis mode (tutorial / how-to / reference / explanation), obeying its contract?
- Zero TL;DR blocks?
- Short sentences, no flourish, no "explaining life"?
- Every link and diagram id resolves?
- Every limitation stated out loud, bolded, never buried?
- For any how-to: context set, the click-path given, the outcome and its branch stated?
- For any diagram: numbered stages, simple boxes, every arrow a verb, one accent, the terminal box filled — and does it earn its place over prose?
- Could you cut another page by merging two? If yes, cut it.

If any answer is no — tighten before delivering.
