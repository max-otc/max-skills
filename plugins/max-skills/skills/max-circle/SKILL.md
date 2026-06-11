---
name: max-circle
description: Use when the user wants documentation rebuilt to the level of Circle's developer docs — page structure, choreography, and native corporate-technical prose. Triggers on "circle-quality", "circle-level refactor", "refactor the docs like Circle", "make our docs sound like Circle", "read like Stripe / Circle docs", "raise the level of English", "the docs sound choppy / clipped / translated", "the pass barely changed anything", "circleify this", "league of Circle", "our docs don't sound native", "the English isn't at their level".
---

# Max Circle

## Overview

You rebuild documentation to the standard of Circle's developer docs (developers.circle.com). The standard works at four tiers, and you apply all four:

0. **The page system** — which sections a page has and in what order, how titles and headings are grammared, how a paragraph wraps one idea.
1. **Sentence grammar** — complete, single-arc sentences: actor, verb, object, benefit.
2. **Section choreography** — how Circle moves a reader through a page: guide contracts, step openers, code introductions, outcome confirmations, recaps.
3. **The lexicon** — the workhorse phrases, tense rules, and the words that never appear.

The skill runs in one of two modes:

- **Refactor mode** (default): page by page, you rebuild each page from its mode's blueprint in tier 0 — section order, canonical headings, choreography — and write every paragraph fresh with tiers 1–3. The facts are the contract; the old structure and the old prose are not. A new page is the same refactor with the facts supplied as source material instead of an old page.
- **Pass mode** (only when the user explicitly asks for sentences-only — "don't restructure", "just polish the prose"): facts, structure, headings, fences, and tables survive exactly; you rewrite sentences and may add choreography lines. Tier 0 is used only to flag structural gaps.

**The magnitude rule.** A Circle-level result is visible at arm's length: headings renamed to the blueprint's grammar, sections reordered, every paragraph rewritten, the page at or under its old length. If the diff reads as the old page with smoother sentences, you ran a pass while the user asked for the level. Start over from the skeleton (method, step 3).

**Structure is half the level.** A page can match the blueprint perfectly and still fail in sentence texture — house cadence, punchlines, personification survive the rebuild by default. The register trial (method, step 6) is where the other half is reached; it is not optional.

**REQUIRED REFERENCE:** `circle-corpus.md`, shipped beside this file — the verbatim pattern library, mined from the Circle corpus and organized by page mode. Read the section matching the page you are rebuilding before you touch it.

## Core Principle

**A styled doc shows the reader the author. A Circle-grade doc is a pane of glass — the reader sees only the product.**

Fragments, aphorisms, and clipped rhythm read as *voice*. Institutional readers hear voice and price in risk. Complete, smooth, plain sentences read as *fluency*, and fluency is what the reader registers as quality. The writing disappears; the product remains.

## When to Use

- "Make our docs sound like Circle / Stripe" · "raise the level of English" · "circle-level refactor"
- "The docs sound choppy / clipped / like a translation" · "polish the prose"
- A register pass was already run and barely changed the pages — the level needs the structure rebuilt, not the sentences smoothed
- Pre-launch rebuild before institutional or developer readers see the handbook

**Do NOT use for:**

- Planning the page set — which pages exist, which question each answers → `max-doc`. The two compose: `max-doc` decides the set of pages; `max-circle` rebuilds each page. Refactor mode never splits, merges, creates, or deletes pages — it flags the need.
- Explaining one concept to a layperson → `max-eli5`
- The litepaper / whitepaper register → `jake-writing`. That register is deliberately terse and define-by-negation — the opposite move. Never circleify the litepaper.
- Marketing copy and landing pages → `max-marketing`

## Foundations — the canon

You stand on the plain-prose canon. Named, one line each.

- **Classic style** (Thomas & Turner, *Clear and Simple as the Truth*; Pinker, *The Sense of Style*) — prose as a window: the reader looks *through* the writing at the thing itself. Anything that draws attention to the writing is removed. Circle's register is classic style applied to developer docs.
- **Actors and actions, then concision** (Joseph Williams, *Style: Toward Clarity and Grace*) — make the main character the grammatical subject and its action the verb ("CCTP burns and mints", never "transfers are facilitated"); then make every word work — cut what the sentence already implies.
- **Minimalism** (John Carroll, *The Nurnberg Funnel*) — the reader came to do a task; every paragraph that is not their task is in their way.
- **Google Developer Documentation Style Guide** — second person, present tense, active voice, one idea per sentence.
- **Microsoft Writing Style Guide** — warmth through precision: bias to verbs, talk to "you", never sell.
- **Curse of Knowledge** (Pinker; Chip & Dan Heath) — the expert opens with the term; the reader needs the plain claim first. The disease every habit below treats.
- **The Circle corpus itself** — `circle-corpus.md`. The canon tells you why; the corpus shows you exactly how.

## Tier 0 — the page system

Full blueprints with verbatim models: `circle-corpus.md` → "Page blueprints", "Title, description, and heading grammar", "Paragraph shapes".

### The four blueprints

| Mode | Section order |
|---|---|
| **Product overview** | intro (definition + audience) → Key features → What you can build (or Products, for a family) → How it works → Get started → Related products |
| **Quickstart / tutorial** | guide contract → Prerequisites → Step 1…N (verb-first, decimal sub-steps) → Next steps |
| **Concept page** | governing fact → one section per aspect → practical guidance or boundary to the sibling concept |
| **What-is intro** | definition paragraph → problem/contrast narrative → action section routing each reader |

### Title and heading grammar

- Product titles are bare nouns ("Circle Wallets"). Quickstart titles are `Quickstart: <Imperative>`. Concept titles are noun phrases. Intro titles are "What is X?".
- Frontmatter descriptions are imperative benefit summaries, one or two sentences: *"Add secure, embedded wallets to your application with Circle's APIs and SDKs."*
- **Headings come from a fixed vocabulary**, sentence case: Key features · What you can build · Products · How it works · Get started · Prerequisites · Next steps · Related products · Supported `<X>`. Step headings are verb-first imperatives. Concept-page sections are noun phrases naming the aspect. Do not invent headings outside the vocabulary ("API changes", "Misc", "Notes") — find the canonical home for the fact class instead (integration facts → How it works or a routed quickstart; support matrices → Supported `<X>`).

### The opener rule

The page opens with **two clean sentences, never one overloaded one**: the definition (plain claim, precise term one clause later, ≤ ~25 words) and the audience named by firm type. Never stack appositives — one "— formally, …" clause is the maximum; a second nested gloss means you needed a second sentence.

### Section behavior

- **Key features**: 3–4 items, bold label + colon + imperative benefit phrase. Features may restate facts that also appear in How it works — Circle states each fact once as a scannable benefit and once inside the flow.
- **Get started routes, it never teaches.** A decision criterion ("The right X depends on…"), then links by role or product. The teaching lives in the quickstart it points to.
- **Related products** closes on a one-sentence-pair boundary to the sibling product, then the decision criterion.

### Paragraph shapes — how an idea is wrapped

One idea per paragraph; one to three sentences, almost always two. Five wrappers, all in the corpus: **claim + support**, **before/after contrast**, **You/Us split**, **governing fact** (one flat sentence that rules the page), and the **warning three-beat** (bold prohibition → reason → the right action: *"**Do not hardcode fee values.** Fees can change at any time. Always retrieve the current fee…"*).

## Tier 1 — sentence grammar, seven habits

Observed verbatim in the Circle corpus. Apply all seven to every prose sentence.

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

### 7. Spend no word twice.

Circle's pages are short because each idea is paid for once. Merge sentences that carry one idea; delete a paragraph that restates its neighbor; strike the modifier the noun already implies. The one licensed redundancy is structural: a fact may appear once as a scannable benefit (Key features) and once inside the flow (How it works) — never twice in prose.

- Before: *"Settlement is atomic. The trade settles in a single transaction, atomically, with no settlement risk between the legs."*
- After: *"The trade settles atomically in one transaction, so no settlement risk sits between the legs."*

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
- **Zero casual transitions.** Also banned: *under the hood, basically, in a nutshell, simply put, let's, now,* (sentence-initial), *as you can see, it's worth noting*. Circle states the mechanism; it never winks at it. Where a transition is needed, the heading or the governing fact is the transition.

## The house tells — what the register trial hunts

Structure can match the blueprint while every sentence still sounds like the house. These six tells are the house voice's signature; the trial (method, step 6) hunts them one by one, and a draft fails the trial while any remains.

- **Punchline grammar.** Aphorism, antithesis ("a round you sat out, not a round you lost"), negation-as-punchline ("reveals nothing", "it does not guess"). A section that ends on a turn of phrase fails. Replace it with a flat behavioral statement or the boundary cross-link.
- **Em-dash constructions.** Paired appositions ("— a *bitmap* —") and pivot dashes. Circle uses a parenthetical, a comma, or a second sentence. Em-dash count in body prose: effectively zero.
- **Personification and metaphor.** The machine never *lingers, guesses, betrays, drifts, touches, lives, looks stale*, and data is never a *fingerprint*. Literal verbs only: records, deletes, rejects, excludes, returns, maps, verifies.
- **Drum-and-cymbal cadence.** An 8-word punch followed by a 40-word sprawl is the house rhythm. Circle is unimodal: 15–25 words, gently varied; any sentence over 30 words gets split.
- **Term rotation.** *Picks / position / predictions* for one concept. Circle picks one term per concept and holds it for the whole page.
- **Idiom leak.** *and so on, in practice, behind the scenes, right after, right up to, all over again, a handful of, sat out.* Exact words or exact numbers instead.

### The lint — countable, so count

| Check | Target |
|---|---|
| Body-prose sentences over 30 words | 0 |
| Em-dash appositions or pivots in body prose | 0 |
| Fragments in body prose (outside fences, cells, labels) | 0 |
| Banned gush words, exclamation marks | 0 |
| Idiom-leak list hits | 0 |
| Personification verbs on the system | 0 |
| Terms per concept | 1 |
| Section closers that are aphorisms or antitheses | 0 |

### House invariants — never traded for the register

Some house rules outrank Circle cosmetics; the refactor keeps them even where Circle would not:

- Time estimates on links ("~4 min") stay — an accessibility rule from the operating manual.
- Summary, plain-words, tip, and see-also fences stay, in their own register.
- Front-loaded answers stay: the first sentence of a section answers it.

The register governs body prose; it never strips the house's reader aids.

## The method — the refactor

The method is a staircase with gates. Do not skip a gate because the draft "feels done" — the trial exists because finished-feeling drafts fail it.

1. **Inventory the facts.** Before touching the page, list every fact in the source: numbers, names, links, time estimates, caveats, limitation lines. This list is the contract; the work ends with every item intact and housed.
2. **Name the page mode.** Tutorial, how-to, concept, overview, or reference — then read that section of `circle-corpus.md`.
3. **Lay the skeleton — and gate it.** Take the mode's blueprint from tier 0 and assign every inventoried fact to its section. Headings follow the blueprint's grammar; order follows the blueprint. A fact with no obvious home goes in How it works (or the concept aspect it supports). A fact that belongs on a *different page* is flagged for `max-doc`, never silently moved or dropped. Gate: the skeleton matches the blueprint before you write a sentence.
4. **Write fresh, one section at a time.** Write each section from the skeleton and the fact inventory — never by editing the old prose; the old page is a fact source, not a template. Close each section by checking it against the seven habits and its mode's choreography before starting the next. Return to the old page once, at the end, for facts you missed.
5. **Compress.** Apply habit 7 across the draft: merge sentences that carry one idea, delete prose that restates its neighbor. Net of the choreography lines you added, the page comes out at or under the source's length. A page that grew is carrying padding — find it.
6. **The register trial.** Re-read the whole draft as a hostile Circle editor who has just read the corpus. Hunt the house tells (the list below) sentence by sentence. Every hit becomes a named gap — draft sentence, violated pattern, corpus model, fixed version — and you fix them all, then re-read. The trial ends when a full read finds zero hits. Texture failing behind a passing structure is the *default* outcome of step 4; the trial is where the register is actually reached. For a flagship page, dispatch a fresh judge who has read only the corpus and the draft.
7. **Run the lint.** The countable checks in the lint table below. Count, don't estimate.
8. **Calibrate rhythm.** Explanatory sentences run 15–25 words, gently varied — unimodal, never drum-and-cymbal. Keep at most **one** short load-bearing sentence per section.
9. **Rebuild the page's index artifacts.** House artifacts that mirror structure — summary fences, sidebar titles, frontmatter descriptions — are regenerated to match the new headings, in their own register (fragments allowed in fences).
10. **Close with the fact diff.** Reconcile the inventory item by item against the rewrite. A caveat that softened or a number that moved means the refactor failed — fix it before delivering. A fact that *should* change is flagged, never silently changed.

For a doc set: one page at a time, in reading order. Never batch-rewrite blind. With each page, deliver a one-line structure note: sections renamed, reordered, or merged, the trial's hit count per round, and any facts flagged for another page.

In pass mode, steps 3 and 9 collapse: the skeleton is the existing structure, untouched; missing sections ship as flagged ready-to-paste blocks. The trial and the lint still run in full.

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

Same facts, same code. The step gained its opener, the code its introduction, the output its confirmation — and the aphoristic closer became a completed arc. The growth here is all choreography; step 5 holds everything else flat. Prose that restates the source in more words is padding, not polish.

## Strict rules

- Never add, drop, soften, or "improve" a fact, number, link, code block, or caveat — in either mode. Blueprints shape pages, never claims.
- Refactor mode rebuilds one page at a time. Splitting, merging, creating, or deleting pages is `max-doc`'s work — flag it, never do it silently.
- Structure comes from tier 0's blueprints and heading grammar, never invented. Index artifacts (summary fences, sidebar titles) are regenerated to match.
- The magnitude rule holds: if the delivered page reads as the old page with smoother sentences, the refactor is not done.
- The register trial runs on every page, in both modes: zero house tells before delivery, lint all zeros.
- House invariants (link time estimates, house fences, front-loaded answers) survive the refactor — the register never strips reader aids.
- Pass mode only on explicit request, and there structure is untouched — headings, fences, tables, callouts, link targets; missing sections ship as flagged ready-to-paste blocks.
- Body prose is complete sentences. Fragments survive only in summary fences, table cells, bullet labels — and reference parameter descriptions.
- The page opener follows habit 1. Every code block gets an introduction and an outcome confirmation. Every table and diagram is announced.
- Present tense for the system; "you'll" only for the reader's future; imperative for the reader's actions.
- No banned gush words. No exclamation marks. No aphorisms.
- One short punch sentence per section, at most. Net of added choreography, the page never grows.
- Never circleify a register that is terse on purpose (litepaper, legal, summary fences, parameter tables).

## Common mistakes

| Mistake | What it looks like | Fix |
|---|---|---|
| **The timid refactor** | The old structure intact, a handful of sentences smoothed — a pass wearing the refactor's name. | Write from the skeleton (method 3–4), never from the old prose. The result must differ at arm's length: blueprint order, new headings, every paragraph fresh. |
| **Padding growth** | Every paragraph longer, the page half again its size, "because fluency". | Step 5 and habit 7. Choreography lines may add; everything else holds flat or shrinks. |
| **Texture fail behind a passing structure** | Blueprint order, noun-phrase headings — and every paragraph still closes on a punchline a Circle editor would flag. | The register trial (method 6). Architecture is half; loop the trial until zero house tells. |
| **Em-dash habit** | "— a *bitmap* —" appositions and pivot dashes through the page. | Parenthetical, comma, or a second sentence. Lint target: zero. |
| **Personified machine** | "the oracle does not guess", "bitmaps do not linger". | Literal verbs: rejects, deletes, excludes, returns. The machine acts; it never behaves. |
| **Register strips the house aids** | "(~4 min)" removed from links, fences flattened, "because Circle doesn't do that". | House invariants outrank cosmetics. The aids stay. |
| **Surface smoothing** | A few fragments joined, but the jargon-first opener and the negations survive. | Run all four tiers as a checklist per section. Habit 1 applies to the opener every time. |
| **Grammar without choreography** | Sentences are arcs, but code blocks still end in silence and steps open cold. | Tier 2 is half the register. Every code block: introduction before, confirmation after. |
| **Aphoristic closers kept** | "You read a live mark." ends the step. | Complete the arc: "If `volPct` prints, the relayer reached the live oracle and you've read your first live mark." |
| **New fragments while fixing old ones** | "Always CRX, never another firm." appears in the rewrite. | Every prose sentence gets a subject and a verb. Re-read for fragments before delivering. |
| **Gush creep** | "seamlessly settles", "powerful margin engine". | The banned list. Clarity is the warmth; adjectives are the tell. |
| **Fact drift** | "strangers" becomes "other participants" and a caveat quietly softens. | The fact inventory is the contract. Diff against it (method 8). |
| **Cross-page restructuring** | Two pages merged into one, a section exported to a new page. | Refactor mode is per page. Page-set changes are flagged for `max-doc`. |
| **Stale index artifacts** | New headings, but the summary fence still answers the old ones. | Method 7: regenerate fences, sidebar titles, and frontmatter descriptions against the new structure. |
| **Structure changes in pass mode** | The user said "sentences only", yet headings got renamed and a prerequisites section appeared. | Pass mode touches sentences. Structural gaps ship as flagged ready-to-paste blocks. |
| **Circleifying the punch** | Every short sentence inflated; the section loses its one load-bearing line. | Keep one punch per section. Fluency needs rhythm too. |
| **Wrong-mode choreography** | A concept page gets "In this step, you'll…"; a reference page gets benefit clauses on parameters. | Name the page mode first (method 2). Each mode has its own choreography. |
| **Overloaded opener** | A 50-word first sentence stacking two appositives ("— formally, a wrapper on the NDF, CRX's core instrument, which settles…"). | The opener rule: two clean sentences — definition, then audience. One "— formally" clause maximum. |
| **Invented headings** | "API changes", "Misc", "Notes" appear as sections. | The blueprint's heading grammar (tier 0). Find the canonical home for the fact class. |
| **Casual transitions** | "Under the hood, every forward carries two legs." | The banned transitions list. State the mechanism; the heading is the transition. |
| **Get started that teaches** | A paragraph of inline instructions where the routing belongs. | Get started routes by role to a quickstart. The teaching lives on the page it points to. |

## Quality checks before finishing

- Refactor mode: does the page follow its mode's blueprint — section order, heading grammar, sentence-case headings, frontmatter description as imperative benefit summary — and is the change visible at arm's length?
- Is the page at or under the source's length, net of added choreography lines? Does any paragraph merely restate its neighbor?
- Does the page open with two clean sentences — the plain claim (term one clause later, one "— formally" maximum), then the audience by firm type?
- Does every paragraph wrap one idea in one of the five shapes, one to three sentences?
- Does Get started route rather than teach?
- Is every body-prose sentence a complete single arc — actor, verb, object, benefit?
- Does every feature sentence carry its "so that" / "without", and every negation-led definition now lead with the action?
- Are mechanisms said with concrete paired verbs, in present tense?
- Tutorial pages: guide contract at the top, an opener on every step, an introduction on every code block, a confirmation after it, a recap at the end?
- Concept pages: flows narrated actor-by-actor, tables and diagrams announced, trade-offs carried by because-clauses?
- Reference prose: conditionals exact, durations concrete, parameters terse?
- Zero banned words, zero exclamation marks, zero aphorisms?
- Did the register trial run to zero house tells — no punchline closers, no em-dash constructions, no personification, one term per concept, no idiom leaks?
- Does the lint table read all zeros, counted rather than estimated?
- Are the house invariants intact — link time estimates, house fences, front-loaded answers?
- Facts, numbers, links, time estimates, caveats — unchanged in meaning everywhere? (Pass mode: structure too.)
- Index artifacts — summary fences, sidebar titles, descriptions — regenerated against the new headings?
- Does the fact inventory reconcile, item by item?
- Read the page aloud once: does any sentence make you stop? That sentence is not done.

If any answer is no — the page is not done.
