---
name: max-circle
description: Use when the user wants existing documentation raised to the English register of Circle's developer docs — native, fluent, corporate-technical prose. Triggers on "circle-quality", "make our docs sound like Circle", "read like Stripe / Circle docs", "raise the level of English", "the docs sound choppy / clipped / translated", "make the prose smoother", "polish the docs English", "circleify this", "league of Circle", "our docs don't sound native", "the English isn't at their level".
---

# Max Circle

## Overview

You take documentation that is already structurally sound and raise its English to the register of Circle's developer docs (developers.circle.com). The register works at three tiers, and you apply all three:

1. **Sentence grammar** — complete, single-arc sentences: actor, verb, object, benefit.
2. **Section choreography** — how Circle moves a reader through a page: guide contracts, step openers, code introductions, outcome confirmations, recaps.
3. **The lexicon** — the workhorse phrases, tense rules, and the words that never appear.

This is a **register pass, not a rewrite**. Facts, numbers, links, time estimates, and caveats survive exactly. You may *add* choreography sentences (a step opener, an outcome confirmation) because those are sentences; you may not move, rename, or delete sections.

**REQUIRED REFERENCE:** `circle-corpus.md`, shipped beside this file — the verbatim pattern library, mined from the Circle corpus and organized by page mode. Read the section matching the page you are rewriting before you touch it.

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
- **The Circle corpus itself** — `circle-corpus.md`. The canon tells you why; the corpus shows you exactly how.

## Tier 1 — sentence grammar, six habits

Observed verbatim in the Circle corpus. Apply all six to every prose sentence.

### 1. Plain claim first, precise term second.

> "USDC is a **digital dollar** issued by Circle, **also known as** a stablecoin."

The first sentence of every page makes the claim in words anyone holds; the precise term lands one clause later, attached to it. Never open on the term. This applies again at every first mention of a term, not only the page opener.

- Before: *"CRX is a matched-principal swap dealer in FX non-deliverable forwards (NDFs), cash-settled in USDC."*
- After: *"CRX is a dealer where a business locks an exchange rate today and settles the difference in USDC later — formally, a matched-principal dealer in non-deliverable forwards (NDFs)."*

### 2. One arc per sentence — actor, verb, object, benefit.

> "Circle Wallets helps you add secure, embedded wallets to your application so your users can hold and use digital assets without the usual complexity of keys, infrastructure, and chain-specific details."

Thirty-five words, effortless, because it is a single arc: who → does what → so that what. Body prose is complete sentences. **Fragments live only in summary fences, table cells, and bullet labels** — never as an answer in prose.

- Before: *"In USDC."* → After: *"Trades settle in USDC."*

### 3. Attach the benefit in-sentence.

> "…backed 100% by highly liquid cash and cash-equivalent assets **so that** it's always redeemable 1:1 for USD."

Every feature sentence carries its own "so that" or "without" — what the reader gets, or what they no longer carry. A feature stated without its consequence is half a sentence.

### 4. Say the mechanism with paired verbs.

> "CCTP **burns** USDC on the source blockchain and **mints** it on the destination blockchain, enabling secure 1:1 transfers without traditional bridge liquidity pools or wrapped tokens."

One sentence, two concrete verbs, the whole mechanism. The system's verbs are always concrete: *returns, emits, mints, burns, locks, signs, issues*.

### 5. Replace negation with action + "without".

> "…transfers **without** traditional bridge liquidity pools or wrapped tokens."

State what happens, then name what is absent in a trailing "without". Define-by-negation ("nothing pooled, nothing matched against strangers") leads with absence; the Circle move leads with the action.

- After: *"Your trade binds directly with CRX, without pooled liquidity or anonymous matching."*

### 6. Split the work: You / Us.

> "**You don't manage** raw private keys. **Circle secures** keys with MPC or passkeys depending on wallet product."

Two short sentences dividing the labor: what you do, what the platform does. Use it wherever responsibility could blur — auth, custody, signing, settlement. Its callout form: *"The StableFX API handles both offchain and onchain steps, so you don't need to interact with smart contracts directly."*

## Tier 2 — section choreography, by page mode

Identify the page mode first (tutorial / how-to / concept / overview / reference), then apply its choreography. Verbatim models for every pattern: `circle-corpus.md`.

### Tutorials and quickstarts

- **The guide contract.** Open with two sentences: what this guide walks through, and what the reader will have built, naming the tools. *"This guide walks you through transferring USDC on EVM testnets using Viem and Node.js. You'll build a simple script that checks your balance and sends test transfers."*
- **Prerequisites stem.** *"Before you begin, ensure that you've:"* followed by completed states ("Installed…", "Funded…").
- **Step openers.** Each step starts with one sentence naming its goal: *"In this step, you'll build…"* / *"This step shows you how to…"*. Then the actions.
- **Code introductions.** Imperative + colon: *"Create a `tsconfig.json` file:"*, *"Run the script using the following command:"*. Never drop a code block in unannounced.
- **Outcome confirmations.** After every meaningful code block, one of: what the reader sees (*"You'll see output similar to the following:"*), how to verify (*"To verify the transfer, copy the transaction hash URL…"*), or the state reached (*"A trade is funded when the status is `taker_funded`."*). A code block whose result is never confirmed leaves the reader unsure they succeeded — this is the most common gap in terse docs.
- **Recap closer.** *"In this quickstart, you learned how to…"* plus the key points, then next steps.

### Concept and explanation pages

- **Flow narration.** Narrate the machine in present tense, one actor-verb sentence per step, numbered when sequential: *"The xReserve contract emits a deposit event and locks the funds, holding them in reserve."*
- **Trade-off sentences.** Causality in a because-clause, mitigation in the same sentence: *"Because of the faster finality time, Fast Transfers are subject to a global allowance to mitigate reorganization risks."*
- **Announce every table and diagram.** *"The table below shows…"* / *"The following diagram shows how…"*. Nothing visual arrives unintroduced.
- **Decision criteria as flat facts.** *"The right wallet product depends on who controls the wallet."*

### Product overviews

- **Audience named by firm type**, sentence two: *"…designed for financial institutions including payment service providers, fintechs, crypto OTC desks, and prime brokers."*
- **Key features** as bold label + colon + imperative benefit: *"**24/7 Settlement:** Trade and settle around the clock with sub-second finality on Arc"*.
- **What you can build** as imperative use-case sentences: *"Offer FX liquidity directly in your platform without building your own matching engine."*
- **Get started** closer routes by role; **related products** closer draws the boundary to the sibling product in one sentence pair.

### Reference pages

- **Parameter descriptions are terse noun phrases** — *"Source domain ID"* — no sentence ceremony. This is the one place fragments are correct.
- **Conditional behavior is exact**: trigger, consequence, numbers. *"If you exceed 35 requests per second, the service blocks all API requests for the next 5 minutes and returns an HTTP 429 response."*
- **Durations are honest and concrete**: *"typically in seconds"*, *"typically takes ~65 blocks (15-19 minutes)"*. Never vague, never falsely precise.

## Tier 3 — the lexicon

- **Tense rules.** Present tense for everything the system does ("the contract emits", "the API returns"). "You'll" only for the reader's future inside this guide ("You'll build", "You'll see output"). Present perfect for prerequisites ("ensure that you've: Installed…"). Imperative for every action the reader takes now ("Create", "Run", "Sign").
- **The workhorse phrases** — use them; they are the register's connective tissue: "walks you through", "the following", "the table below shows", "so you don't need to", "to verify", "similar to the following", "depends on whether". Full table in `circle-corpus.md`.
- **Zero gush.** Banned outright: *seamless, seamlessly, powerful, robust, world-class, cutting-edge, blazing, effortless, simply, easily, just, leverage, unlock, supercharge*. No exclamation marks. No jokes, no aphorisms. The warmth is structural: short clear arcs, burdens named and removed, exact numbers.

## The method — the pass

1. **Inventory the facts.** Before touching a sentence, list every fact on the page: numbers, names, links, time estimates, caveats, limitation lines. This list is the contract; the pass ends with every item intact.
2. **Name the page mode.** Tutorial, how-to, concept, overview, or reference — then read that section of `circle-corpus.md`.
3. **Audit against all three tiers.** Where are the six habits missing? Which choreography lines are absent (step openers, code intros, outcome confirmations)? Which lexicon rules are broken?
4. **Rewrite sentence by sentence**, applying tier 1 to every sentence, tier 2 to the section seams, tier 3 throughout. You may add choreography sentences where they are missing — they are sentences, not structure.
5. **Respect the structure line.** Headings, fences, tables, callout blocks, code blocks, link targets, time estimates, bolded limitation lines — unchanged. A missing *section* (prerequisites, recap) is a structural gap: deliver it as a flagged, ready-to-paste block in the note, never silently inserted.
6. **Calibrate length, keep one punch.** Explanatory sentences run 15–25 words; vary around that. Keep at most **one** short load-bearing sentence per section. More and the staccato returns.
7. **Close with the fact diff.** Reconcile the inventory item by item against the rewrite. A caveat that softened or a number that moved means the pass failed — fix it before delivering. A fact that *should* change is flagged, never silently changed.

For a doc set: one page at a time, in reading order. Never batch-rewrite blind.

## The voice — before / after

> **Before (terse house register):**
>
> A public read, no token needed. Ask the relayer for the live margin schedule. The numbers come from live volatility, so the response is real:
>
> ```bash
> curl -s "$RELAYER/margin?pair=$PAIR&notional=100000"
> ```
>
> `volPct` is the live daily volatility the schedule scaled from. If it printed, the relayer reached the live oracle. You read a live mark.

> **After (Circle register):**
>
> In this step, you'll read a live margin schedule — a public endpoint, so no token is needed. The relayer reads live volatility from the oracle and scales the schedule from it, so the response is real and moves with the market.
>
> Request the schedule using the following command:
>
> ```bash
> curl -s "$RELAYER/margin?pair=$PAIR&notional=100000"
> ```
>
> You'll see a response similar to the following, where `volPct` is the live daily volatility the schedule scaled from. If `volPct` prints, the relayer reached the live oracle and you've read your first live mark.

Same facts, same code. The step gained its opener, the code its introduction, the output its confirmation — and the aphoristic closer became a completed arc.

## Strict rules

- Register pass only. Never add, drop, soften, or "improve" a fact, number, link, or caveat.
- Structure unchanged: headings, fences, tables, callouts, link targets, time estimates. Missing sections are flagged with ready-to-paste blocks, never silently inserted.
- Body prose is complete sentences. Fragments survive only in summary fences, table cells, bullet labels — and reference parameter descriptions.
- The page opener follows habit 1. Every code block gets an introduction and an outcome confirmation. Every table and diagram is announced.
- Present tense for the system; "you'll" only for the reader's future; imperative for the reader's actions.
- No banned gush words. No exclamation marks. No aphorisms.
- One short punch sentence per section, at most.
- Never circleify a register that is terse on purpose (litepaper, legal, summary fences, parameter tables).

## Common mistakes

| Mistake | What it looks like | Fix |
|---|---|---|
| **Surface smoothing** | A few fragments joined, but the jargon-first opener and the negations survive. | Run all three tiers as a checklist per section. Habit 1 applies to the opener every time. |
| **Grammar without choreography** | Sentences are arcs, but code blocks still end in silence and steps open cold. | Tier 2 is half the register. Every code block: introduction before, confirmation after. |
| **Aphoristic closers kept** | "You read a live mark." ends the step. | Complete the arc: "If `volPct` prints, the relayer reached the live oracle and you've read your first live mark." |
| **New fragments while fixing old ones** | "Always CRX, never another firm." appears in the rewrite. | Every prose sentence gets a subject and a verb. Re-read for fragments before delivering. |
| **Gush creep** | "seamlessly settles", "powerful margin engine". | The banned list. Clarity is the warmth; adjectives are the tell. |
| **Fact drift** | "strangers" becomes "other participants" and a caveat quietly softens. | The fact inventory is the contract. Diff against it (method 7). |
| **Structure vandalism** | Question headings flattened; summary fences expanded to prose; a prerequisites section silently inserted. | Sentences only. Structural gaps ship as flagged ready-to-paste blocks. |
| **Circleifying the punch** | Every short sentence inflated; the section loses its one load-bearing line. | Keep one punch per section. Fluency needs rhythm too. |
| **Wrong-mode choreography** | A concept page gets "In this step, you'll…"; a reference page gets benefit clauses on parameters. | Name the page mode first (method 2). Each mode has its own choreography. |

## Quality checks before finishing

- Does the page open with the plain claim, the precise term one clause later?
- Is every body-prose sentence a complete single arc — actor, verb, object, benefit?
- Does every feature sentence carry its "so that" / "without", and every negation-led definition now lead with the action?
- Are mechanisms said with concrete paired verbs, in present tense?
- Tutorial pages: guide contract at the top, an opener on every step, an introduction on every code block, a confirmation after it, a recap at the end — and any missing section flagged, not inserted?
- Concept pages: flows narrated actor-by-actor, tables and diagrams announced, trade-offs carried by because-clauses?
- Reference prose: conditionals exact, durations concrete, parameters terse?
- Zero banned words, zero exclamation marks, zero aphorisms?
- Headings, fences, tables, links, estimates, caveats — unchanged in meaning everywhere?
- Does the fact inventory reconcile, item by item?
- Read the page aloud once: does any sentence make you stop? That sentence is not done.

If any answer is no — the pass is not finished.
