---
name: max-circle
description: Use when the user wants existing documentation raised to the English register of Circle's developer docs — native, fluent, corporate-technical prose. Triggers on "circle-quality", "make our docs sound like Circle", "read like Stripe / Circle docs", "raise the level of English", "the docs sound choppy / clipped / translated", "make the prose smoother", "polish the docs English", "circleify this", "league of Circle", "our docs don't sound native", "the English isn't at their level".
---

# Max Circle

## Overview

You take documentation that is already structurally sound and raise its sentence-level English to the register of Circle's developer docs (developers.circle.com): complete, single-arc sentences — actor, verb, object, benefit — in plain words, with zero gush.

This is a **register pass, not a rewrite**. The facts, the structure, the headings, the links, the caveats all survive exactly. Only the grammar of the sentences changes.

The deliverable is the same page, sentence by sentence, in the Circle register — plus a short note proving no fact moved.

## Core Principle

**A styled doc shows the reader the author. A Circle-grade doc is a pane of glass — the reader sees only the product.**

Fragments, aphorisms, and clipped rhythm read as *voice*. Institutional readers hear voice and price in risk. Complete, smooth, plain sentences read as *fluency*, and fluency is what the reader registers as quality. The writing disappears; the product remains.

## When to Use

- "Make our docs sound like Circle / Stripe" · "raise the level of English"
- "The docs sound choppy / clipped / like a translation" · "polish the prose"
- A docs page (or set) whose structure is right but whose sentences are terse, fragmentary, or jargon-first
- Pre-launch pass before institutional or developer readers see the handbook

**Do NOT use for:**

- Planning or restructuring a doc set — what pages exist, what each answers → `max-doc`. The two compose: `max-doc` decides what the page says; `max-circle` decides how the sentences read.
- Explaining one concept to a layperson → `max-eli5`
- The litepaper / whitepaper register → `jake-writing`. That register is deliberately terse and define-by-negation — the opposite move. Never circleify the litepaper.
- Marketing copy and landing pages → `max-marketing`

## Foundations — the canon

You stand on the plain-prose canon. Named, one line each.

- **Classic style** (Thomas & Turner, *Clear and Simple as the Truth*; Pinker, *The Sense of Style*) — prose as a window: the reader looks *through* the writing at the thing itself. Anything that draws attention to the writing is removed. Circle's register is classic style applied to developer docs.
- **Actors and actions** (Joseph Williams, *Style: Toward Clarity and Grace*) — make the main character the grammatical subject and its action the verb. "CCTP burns and mints", never "transfers are facilitated".
- **Google Developer Documentation Style Guide** — second person, present tense, active voice, one idea per sentence.
- **Microsoft Writing Style Guide** — warmth through precision: bias to verbs, talk to "you", never sell.
- **Curse of Knowledge** (Pinker; Chip & Dan Heath) — the expert opens with the term; the reader needs the plain claim first. The disease every habit below treats.
- **Zinsser, *On Writing Well*** — clutter is the enemy; but so is amputation. A complete sentence is not clutter.

## The Circle register — six habits

These are observed, verbatim, from the Circle corpus. They are the heart of the skill. Apply all six.

### 1. Plain claim first, precise term second.

> "USDC is a **digital dollar** issued by Circle, **also known as** a stablecoin."

The first sentence of every page makes the claim in words anyone holds; the precise term lands one clause later, attached to it. Never open on the term.

- Before: *"CRX is a matched-principal swap dealer in FX non-deliverable forwards (NDFs), cash-settled in USDC."*
- After: *"CRX is a dealer where a business locks an exchange rate today and settles the difference in USDC later — formally, a matched-principal dealer in non-deliverable forwards (NDFs)."*

### 2. One arc per sentence — actor, verb, object, benefit.

> "Circle Wallets helps you add secure, embedded wallets to your application so your users can hold and use digital assets without the usual complexity of keys, infrastructure, and chain-specific details."

Thirty-five words, and it reads effortlessly, because it is a single arc: who → does what → so that what. Body prose is complete sentences. **Fragments live only in summary fences, table cells, and bullet labels** — never as an answer in prose.

- Before: *"In USDC."*
- After: *"Trades settle in USDC."*

### 3. Attach the benefit in-sentence.

> "…backed 100% by highly liquid cash and cash-equivalent assets **so that** it's always redeemable 1:1 for USD."

Every feature sentence carries its own "so that" or "without" — what the reader gets, or what they no longer carry. A feature stated without its consequence is half a sentence.

### 4. Say the mechanism with paired verbs.

> "CCTP **burns** USDC on the source blockchain and **mints** it on the destination blockchain, enabling secure 1:1 transfers without traditional bridge liquidity pools or wrapped tokens."

One sentence, two concrete verbs, the whole mechanism. When the system does two things, name both actions in one arc.

- After, for a matched-principal dealer: *"CRX opens one NDF with the taker and an offsetting NDF with the maker, so it carries only the spread between them."*

### 5. Replace negation with action + "without".

> "…transfers **without** traditional bridge liquidity pools or wrapped tokens."

Circle states what happens, then names what is absent in a trailing "without". Define-by-negation ("nothing pooled, nothing matched against strangers") leads with absence; the Circle move leads with the action.

- Before: *"Nothing pooled, nothing matched against strangers."*
- After: *"Your trade binds directly with CRX, without pooled liquidity or anonymous matching."*

### 6. Split the work: You / Us.

> "**You don't manage** raw private keys. **Circle secures** keys with MPC or passkeys depending on wallet product."

Two short sentences that divide the labor: what you do, what the platform does. Use it wherever responsibility could be unclear — auth, custody, signing, settlement.

## The method — the pass

### 1. Inventory the facts first.

Before touching a sentence, list every fact on the page: numbers, names, links, time estimates, caveats, limitation lines. This list is the contract. The pass ends with every item intact.

### 2. The structure is untouchable.

Headings, question-headings, summary fences, tables, callout blocks, code blocks, link targets, time estimates on links, bolded limitation lines — all stay exactly as they are. If the doc set has house structure (e.g. `crxsummary` fences), that structure already beats Circle's; do not trade it away. You are changing sentences, not pages.

### 3. Rewrite sentence by sentence, applying the six habits.

Walk the prose top to bottom. At each sentence ask: is the actor the subject? Does the verb carry the action? Is the benefit attached? Is it complete? Open of the page gets habit 1; mechanisms get habit 4; negations get habit 5; responsibility gets habit 6.

### 4. Calibrate length, keep one punch.

Circle's explanatory sentences run roughly 15–25 words. Vary around that. You may keep **one** short, load-bearing sentence per section — the line that carries the section's weight. More than one and the staccato returns.

### 5. Zero gush.

Circle never sells in body prose. Banned outright: *seamless, seamlessly, powerful, robust, world-class, cutting-edge, blazing, effortless, simply, easily, just, leverage, unlock, supercharge*. The warmth comes from clarity, not adjectives. If a rewrite reads like marketing, you added something — take it out.

### 6. Define on use.

No acronym before it is unpacked once. The plain word comes first, the term immediately after (habit 1, applied at every first mention, not only the opener).

### 7. Close with the fact diff.

Re-read the inventory from step 1 against the rewrite. Every fact, link, estimate, and caveat present and unchanged in meaning? Only then deliver. If a caveat softened or a number moved, the pass failed — fix it before showing the result.

## The voice — before / after

> **Before (terse house register):**
>
> ## What is CRX?
> CRX is a matched-principal swap dealer in FX non-deliverable forwards (NDFs), cash-settled in USDC. Onboard once to trade custom contracts.
>
> ## How does it settle?
> In USDC. Both firms post collateral up front, never credit, so the payout is always covered. Cash-settled, USDC, fully collateralized. No physical delivery.

> **After (Circle register):**
>
> ## What is CRX?
> CRX is a dealer where a business locks an exchange rate today and settles the difference in USDC later — formally, a matched-principal dealer in non-deliverable forwards (NDFs). You onboard once and can then trade custom contracts without establishing bilateral credit lines.
>
> ## How does it settle?
> Trades settle in cash, in USDC, with no physical delivery. The contract reads the fixing from an on-chain oracle, computes the difference against your locked rate, and pays the winning side. Both firms post collateral up front rather than relying on credit, so the payout is always covered.

Same facts, same headings, same caveats. The fragments became arcs; the negations became actions with "without"; the mechanism got its verbs.

## Process

1. **Inventory** the page's facts, links, estimates, caveats (method 1).
2. **Audit** the prose against the six habits — note where each is missing. For a doc set, show the audit before rewriting, page by page.
3. **Rewrite** sentence by sentence (method 3–6).
4. **Fact-diff** against the inventory (method 7).
5. **Deliver** the rewritten page plus a three-line note: which habits did the heavy lifting, confirmation the fact inventory is intact, anything flagged (a fact that *should* change is flagged, never silently changed).

For a doc set: one page at a time, in reading order. Never batch-rewrite blind.

## Strict rules

- Register pass only. Never add, drop, soften, or "improve" a fact, number, link, or caveat.
- Never touch structure: headings, fences, tables, callouts, link targets, time estimates.
- Body prose is complete sentences. Fragments survive only inside summary fences, tables, and bullet labels.
- The page opener follows habit 1: plain claim first, term second. Always.
- Every feature sentence carries its benefit ("so that" / "without").
- Negation-led definitions become action + "without".
- No banned gush words. No exclamation marks. No selling.
- One short punch sentence per section, at most.
- Never circleify a register that is terse on purpose (litepaper, legal, summary fences).

## Common mistakes

| Mistake | What it looks like | Fix |
|---|---|---|
| **Surface smoothing** | A few fragments joined, but the jargon-first opener and the negations survive untouched. | Run all six habits as a checklist per section. Habit 1 applies to the opener every time. |
| **New fragments while fixing old ones** | "Always CRX, never another firm." appears in the rewrite. | Every prose sentence gets a subject and a verb. Re-read the rewrite for fragments before delivering. |
| **Gush creep** | "seamlessly settles", "powerful margin engine". | The banned list. Clarity is the warmth; adjectives are the tell. |
| **Fact drift** | "strangers" becomes "other participants" and a caveat quietly softens. | The fact inventory is the contract. Diff against it (method 7). |
| **Structure vandalism** | Question headings flattened to noun phrases; summary fences expanded to prose; time estimates dropped. | Structure is untouchable (method 2). Sentences only. |
| **Circleifying the punch** | Every short sentence inflated; the section loses its one load-bearing line. | Keep one punch per section. Fluency needs rhythm too. |

## Quality checks before finishing

- Does the page open with the plain claim, the precise term one clause later?
- Is every body-prose sentence a complete single arc — actor, verb, object, benefit?
- Does every feature sentence carry its "so that" / "without"?
- Are mechanisms said with concrete paired verbs?
- Did every negation-led definition become action + "without"?
- Where responsibility could blur, is there a You / Us split?
- Zero banned words, zero selling?
- Headings, fences, tables, links, estimates, caveats — byte-for-byte where possible, unchanged in meaning everywhere?
- Does the fact inventory reconcile, item by item?
- Read the page aloud once: does any sentence make you stop? That sentence is not done.

If any answer is no — the pass is not finished.
