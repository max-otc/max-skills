---
name: max-doc
description: Use when the user wants to write or rewrite documentation — a docs site, a docs page, a README, help content, an explainer — in Max's house style, AND when writing or revising a formal CRX market-maker document (the Margin and Settlement Overview, the Collateral Overview, companion IM/VM/closeout/collateral methodologies). Now carries the CRX market-maker document register as its priority layer — clearinghouse content in Hyperliquid-grade plain English, given→new flow, lifecycle order. Triggers on "write the docs", "rewrite this doc", "docs page", "document this", "make a docs site", "plan the docs", "help page", "the docs are too verbose / too long", "turn this into docs", plus "the tone is off", "too legal", "reads like fake legal prose", "fix the flow", "reads choppy", "make it read professional", "MM doc language", "Margin Overview", "Collateral Overview".
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

## Two layers

This skill has two layers, and they do not fight.

- **Architecture** — which pages exist, which reader owns each, which mode each is in. The eleven laws below. This layer governs every document type.
- **The CRX market-maker document register** — the sentence-level register and flow for one document class: the formal documents CRX hands to desks. This layer is **priority**. For those documents it governs every sentence and *overrides the general voice below wherever they differ.*

When the document in front of you is a formal CRX market-maker document, read the register first. Otherwise, the general voice holds.

## When to Use

- "Write / rewrite the docs" for a product or feature
- "Document this" · "make a docs site" · "help page" · "README"
- "These docs are too long / too verbose / full of fluff"
- "Plan the docs" — what pages, for whom, in what order
- Any rendered explainer the reader chose to read
- **A formal CRX market-maker document** — the Margin and Settlement Overview, the Collateral Overview, or a companion methodology; or a request to fix its tone ("too legal", "reads choppy", "make it read professional")

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

---

# The CRX market-maker document register

**Priority layer.** When the document is a formal CRX market-maker document — the Margin and Settlement Overview, the Collateral Overview, or a companion methodology (IM, VM, closeout, collateral curation) — this register governs every sentence. Where it differs from the general voice and the eleven laws below, **this register wins**. The architecture laws still apply — which pages exist, MECE coverage, honesty lines, resolving every reference. The voice is this register's.

## The genre

A rules document is read by a desk deciding whether to trust a venue. It is not a spec (nobody implements from it), not marketing (nobody is persuaded by it), not a handbook page (nobody lands mid-stream). The reader goes start to finish once, testing whether the system is *designed* — whether each mechanism exists for a reason and hands off cleanly to the next. The prose must do two things at once: state rules exactly, and carry the reader through them as one connected system.

## The register: clearinghouse content, protocol diction

One lens governs every sentence: **a clearinghouse risk engineer explaining the live system to a desk, on the record.** Authority comes from precision and mechanism, never from diction. A sentence earns trust by being checkable, not by sounding like a rulebook.

The register blends two sources, and the blend is asymmetric — we take the *content discipline* of one and the *voice* of the other.

**Take from LCH / CME** — the content layer:

- Defined terms introduced once, then used verbatim: IM, VM, MM, cure window, closeout mark, election. Precise vocabulary is not costume — *novate*, *haircut*, *netting* are the exact names of mechanisms and stay.
- Exact parameters: windows, thresholds, calibration targets, asset lists stated with numbers and dates.
- Completeness: every state the system can enter has a stated outcome. No mechanism trails off.
- Lifecycle structure: numbered sections that walk trade → margin → marks → cure → closeout → settlement.
- Neutral temperature: the document never sells, reassures, or dramatizes.

**Refuse from LCH / CME** — the costume:

- Ceremonial grammar: *shall*, *hereby*, *herein*, *thereof*, *pursuant to*, *absent* as a preposition, *in the event that*, legal *where* as a conditional.
- Inversions for gravitas: "The default terms bind no account."
- Decree voice about the document itself: "This document sets out…", "governs", "binds". The document describes the system; it does not ordain.
- Synonym doublets ("terms and conditions"-style pairs that add words, not meaning).

**Take from Hyperliquid / Ostium** — the diction layer:

- Plain declarative sentences with the mechanism as subject and a working verb. The anchor exemplar, from Hyperliquid's margining page: *"The maintenance margin is currently set to half of the initial margin at max leverage."* A parameter, stated flat, checkable in one read.
- Verbs that are things the system does: posts, nets, settles, auctions, enters, releases, converts, triggers.
- Conditions in spoken grammar: *when*, *if*, *by default* — not *where*, *absent*, *in circumstances where*.

**Refuse from Hyperliquid / Ostium** — the casualness:

- Second person. CRX rules documents are third person, always.
- Marketing superlatives ("tightest spreads", "deepest liquidity"), feature-selling, *simply*, *just*, exclamation, emoji.
- Hedge-casual qualifiers ("basically", "essentially", "roughly") — a rules doc states the rule or states that the rule is forthcoming.

## The sentence test

Every sentence in the document passes all five. Apply to new sentences as written and to existing sentences on any edit pass.

1. **Concrete subject.** The grammatical subject is a thing in the system — a position, an account, collateral, the mark, a maker, CRX — not an abstraction about the document or an empty frame ("It is the case that…").
2. **Working verb.** The main verb is an action the system performs or a state it holds. Kill decree verbs and being-verb stacks that describe the document rather than the machine.
3. **Sayable on a call.** The strongest anti-costume test: if Jake would not say the phrase out loud to a desk head, rewrite it. "Absent any election" fails; "By default" passes. "In one of two circumstances" fails; "Two events trigger closeout" passes.
4. **Exact where it counts.** Numbers, windows, thresholds, and defined terms survive verbatim. Plainness never rounds off precision — a plain sentence with a soft number is a worse sentence, not a friendlier one.
5. **Neutral temperature.** No reassurance adverbs (*robustly*, *securely*, *seamlessly*), no drama, no aphorism or seesaw constructions ("tighten immediately, loosen only with review" — split it into two plain sentences).

## The costume sweep

Replacements to apply on sight. Left column = what has appeared in our own drafts.

| Costume | Plain |
|---|---|
| Absent any election | By default |
| The default terms bind no account | No account is locked into the default terms |
| in one of two circumstances: | Two events trigger closeout: |
| where the receiving account has elected to accept it | when the receiving account has opted in |
| where elections are compatible | when both sides' elections match |
| This document sets out… | (delete the frame; state the first rule) |
| shall settle / shall post | settles / posts |
| pursuant to / hereunder / herein | name the document, or drop |
| may [do X] (permission-flavored) | can [do X], or state who decides |

The sweep targets grammar, not vocabulary. *Election*, *novation*, *cure*, *haircut*, *closeout mark* are mechanism names and stay; the costume is conjugating them ceremonially.

## Passive voice

Allowed when the actor is system-obvious and the sentence stays short: "IM is released to each participant's margin account." Banned when it hides who acts at a decision point — anywhere discretion, election, or governance is involved, name the actor. "Risk parameters are tightened" hides the hand; "CRX tightens risk parameters" shows it.

## The seven flow principles

Register makes sentences right; flow makes them read as one system. Maximum compression is the standing failure mode — a document distilled to perfect isolated sentences reads as an index of rules, not a designed system. Tightness is kept at the sentence level; flow is built between sentences.

### 1. Purpose before mechanism

Every section opens with one clause naming what the mechanism protects, guarantees, or achieves — then defines how it works. One clause. If the purpose needs a paragraph, it belongs in a methodology doc.

> *Initial margin (IM) is the collateral that protects participants against counterparty default. Both sides post it at trade…*

### 2. Given → new

The flow engine. Begin each sentence with information the reader already holds (usually from the previous sentence); place the new fact at the end. Chain: the object of one sentence becomes the subject of the next. When a paragraph reads choppy, the diagnosis is almost always sentences that each open with new material — the reader restarts at every period.

### 3. Walk the lifecycle

The document's deep structure is time: trade → margin posted → marks move → VM flows → cure → closeout → expiry. Let sentence openers carry it: *at trade, while a position is open, upon breach, at expiry.* Temporal and conditional scaffolding is the genre's native connective tissue.

### 4. One paragraph, one movement

A paragraph is rule → mechanism → consequence, in that order. Never a stack of parallel atoms sharing a topic. If two rules do not develop each other, they are two paragraphs (or one belongs to an exhibit).

### 5. Deliberate cadence

Vary sentence length inside every paragraph. A short sentence lands only when its neighbors are longer; three consecutive sentences of equal weight read as staccato regardless of content. The standard pattern: a long establishing sentence, then the short rule.

### 6. Anaphoric stitches

Demonstrative back-references — *this requirement, that mark, the same window* — knit sentences into paragraphs. A stitch points at a specific antecedent; filler ("in addition", "moreover") points at nothing. When a transition is needed and no stitch is available, the information order is wrong (see principle 2).

### 7. The compression budget

Two new facts per sentence. A third fact gets its own sentence or moves to an exhibit. Overloaded sentences are decoded, not read — the reader's parse effort is the tell, participle stacks the usual culprit.

The budget has a floor as well as a ceiling. Connective tissue — a purpose clause, a stitch, a subordinated consequence — carries zero facts and never counts against the budget; cutting it is what produces the too-tight read. The hard trigger: **three consecutive sentences that each open with a brand-new subject read as an index, regardless of their individual quality.** The fix is rarely deleting facts. It is merging a rule with its consequence into one subordinated sentence (*if the window expires unmet, closeout begins*), opening with time (*while a position is open…*), and letting the previous sentence's object become the next sentence's subject.

## Standing bans

Never "so" in any form. Never a sentence opening with "Because". No em dashes in document body prose. No participle trailers ("with X-ing"). No aphorisms or seesaw constructions. Third person, present tense throughout.

## Bench: before → after

Real lines from our drafts, rewritten in register. Study the moves, not just the outputs.

**Legal conditional → spoken conditional**

> Before: *Absent any election, an account posts, accepts, and settles in USDC alone.*
> After: *By default, an account posts, accepts, and settles in USDC only.*

The triplet stays — each verb is a distinct mechanism. Only the ceremonial opener changes.

**Inversion → direct statement with the actor visible**

> Before: *The default terms bind no account. An account may adopt alternative collateral terms, or publish and capitalize its own, certified against the network's standard terms.*
> After: *No account is locked into the default terms. An account can adopt alternative collateral terms, or publish and capitalize its own; new terms are certified against the network's standard framework.*

**Seesaw → two plain sentences**

> Before: *Risk parameters tighten immediately, loosen only with independent review.*
> After: *CRX can tighten risk parameters immediately. Loosening them requires independent review.*

The mechanism (asymmetric governance) survives intact; the aphorism shape goes, and the actor becomes visible.

**Circumstance frame → trigger statement**

> Before: *Closeout occurs in one of two circumstances: the cure window expires unmet, or the account's balance falls to the MM threshold.*
> After: *Two events trigger closeout: a cure window expires unmet, or the account's balance falls to the MM threshold.*

**Index → system (a flow rewrite, not a register one)**

> Before: *Positions on CRX are collateralized on-chain. Both sides of every trade post collateral to smart contracts. Initial margin (IM) and variation margin (VM) are computed continuously and netted across each participant's full portfolio. Margin accounts unable to meet VM requirements enter cure windows. Unmet cure windows or breaches of maintenance margin (MM) trigger closeout. Positions settle against institutional benchmarks.*
> After: *Every position on CRX is collateralized on-chain: both sides of a trade post collateral to smart contracts. While a position is open, initial margin (IM) and variation margin (VM) are computed continuously and netted across each participant's full portfolio. A margin account that cannot meet its VM requirement enters a cure window; if the window expires unmet, or the account breaches maintenance margin (MM), closeout begins. At expiry, positions settle against institutional benchmarks.*

Every sentence in the before passes the sentence test; the paragraph still fails, six same-weight declaratives each opening on a new subject. The after merges rule with consequence, hands the lifecycle to the openers, and varies cadence — same facts, four sentences, one system.

## Revision procedure

Per section, in order:

1. **Costume sweep** — run the replacement table and the five-check sentence test on every sentence. Register before flow: there is no point chaining sentences that will be rewritten.
2. **Purpose check** — does sentence one say what the mechanism is for? If not, write the purpose clause first.
3. **Chain check** — for each sentence, underline its opening noun phrase. Is it given (held by the reader) or new? Reorder until openings are given.
4. **Lifecycle check** — do openers carry time where the content is sequential?
5. **Cadence check** — read aloud; mark three consecutive sentences of equal length and split or merge one.
6. **Budget check** — count new facts per sentence; offload thirds.
7. **Ban sweep** — so / sentence-initial Because / em dashes / participle trailers / seesaws.

Facts are frozen during any register or flow pass: every number, term, and rule survives verbatim unless the user approves a change. These passes reword and reorder; they do not re-litigate content.

## Self-review

Three reads, in order. As a desk head with thirty seconds: does it read as one designed system, start to finish, with no sentence that forces a restart? As a Hyperliquid docs reader: is any sentence wearing a costume — would this phrase survive being said out loud? As an LCH reviewer: is every parameter exact, every term defined-then-used, every state accounted for?

---

# The method — eleven laws

These laws govern architecture and hold for every document type. For a formal CRX market-maker document, the register above owns the sentence-level voice; where a law and the register differ, the register wins.

### 1. Plan the learning paths before writing a word.

List each party who will read — each role or persona. For each, write the ordered questions they actually have. Cut every topic no one asks. The page set is the union of those questions, and nothing more. Each cluster becomes one page in one mode (law 11).

Then run the page map against two tests — this is MECE, applied:

- **No overlap** (mutually exclusive): no question is answered on two pages. Two pages that answer the same question are one page split in half — merge them, and point every other page at the single home.
- **No gap** (collectively exhaustive): every real reader question has exactly one page that owns it. A question with no home is a missing page. A page with no question behind it is an invented page — cut it.

This is also how you refactor an existing doc set. Don't read it page by page. List its current pages, list the reader's real questions beside them, then map one to the other: questions that share a page split out, pages that share a question fold together, orphan pages (no question) get cut, orphan questions (no page) get written. The map drives the edits — not the order the old docs happened to be in.

> A doc set is the questions a reader asks, in order — each with one home, none missing.

### 2. Every heading is a question.

Phrase each `##` as the reader's question, in their words: *"Where is my money held?"*, *"What if I run out?"*. The first sentence answers it. Mechanism after.

**Exception — MM documents.** A formal CRX market-maker document is lifecycle-ordered, not question-headed. Its sections walk trade → margin → marks → cure → closeout → settlement (see the register). Question-headings are for reader-facing docs, help pages, and explainers.

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

**Exception — MM documents.** A formal CRX market-maker document is its own genre — a rules document read start to finish once — and sits outside the four modes. The register governs it.

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

**This voice is for reader-facing docs.** It is second person and question-headed by design. A formal CRX market-maker document is third person and lifecycle-ordered — use the register, not this example.

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
2. **Write.** One page at a time. Question headings, answer-first, terse (laws 2–7). For an MM document, lifecycle-ordered sections in the register instead.
3. **Cut.** Merge duplicates. Delete pages no reader needs. Fewer pages, each load-bearing.
4. **Validate.** No TL;DR blocks. Every link resolves. Every diagram and asset id exists. Frontmatter complete. Honesty lines present. For an MM document, run the register's revision procedure and self-review.

## Page template

- **Frontmatter:** title (a question or a short noun phrase), one-line description, **mode** (tutorial / how-to / reference / explanation), order, group.
- **Body:** question sections only. No TL;DR.
- A short **`Next:`** link line at the end, with a time estimate.
- A glossary only if the page introduces more than 3 new terms.

## Strict rules

- No TL;DR. No closing aphorisms. No analogy where the literal claim works.
- Short sentences. Vital facts only. Cut anything that does not teach.
- Every heading is the reader's real question — except in an MM document, which is lifecycle-ordered.
- Plan the per-reader question list before writing.
- State every limitation in its own bolded line.
- Verify every link and asset id against the source before shipping.
- For a formal CRX market-maker document, the register is priority: third person, present tense, no costume, no em dashes, no seesaws.

## Quality checks before finishing

- Did you plan the per-reader question list, and cut topics no one asks?
- Is the page map MECE — no question answered on two pages (overlap → merge), no real question without a page (gap → write it)?
- Is every `##` a real reader question, answered in the first sentence? (MM documents excepted — lifecycle-ordered.)
- Is each page exactly one Diátaxis mode (tutorial / how-to / reference / explanation), obeying its contract? (MM documents excepted — their own genre.)
- Zero TL;DR blocks?
- Short sentences, no flourish, no "explaining life"?
- Every link and diagram id resolves?
- Every limitation stated out loud, bolded, never buried?
- For any how-to: context set, the click-path given, the outcome and its branch stated?
- For any diagram: numbered stages, simple boxes, every arrow a verb, one accent, the terminal box filled — and does it earn its place over prose?
- For an MM document: does it pass the register's self-review — one designed system, no costume, every parameter exact?
- Could you cut another page by merging two? If yes, cut it.

If any answer is no — tighten before delivering.
