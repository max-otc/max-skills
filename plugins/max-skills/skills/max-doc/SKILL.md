---
name: max-doc
description: Use when writing or rewriting documentation in Max's house style (a docs site, a docs page, a README, help content, an explainer, any rendered explainer the reader chose to read) or a formal CRX market-maker document (the Margin and Settlement Overview, the Collateral Overview, companion IM/VM/closeout/collateral methodologies). Triggers on "write the docs", "rewrite this doc", "docs page", "document this", "make a docs site", "plan the docs", "help page", "README", "the docs are too verbose / too long", "full of fluff", "turn this into docs", plus "the tone is off", "too legal", "reads like fake legal prose", "fix the flow", "reads choppy", "make it read professional", "MM doc language", "Margin Overview", "Collateral Overview". NOT for marketing copy, ad angles or landing pages (use max-marketing), video scripts (use max-launch-video), or code comments (they stay conventional, next to the code).
---

# Max Doc

Write docs as the real questions a real reader asks, each answered in the fewest words that teach. Not a system tour, a brochure or an essay. Deliver a small set of pages, one reader each: terse, front-loaded, honest about what is not true yet. Given a product, codebase or doc set, plan the learning paths first, then write.

**Core principle.** A weak doc explains the system. A doc that teaches answers the reader's next question: find it, answer it, stop. Then the next question. State the fact and stop. Do not explain life.

## Two layers

- **Architecture: the eleven laws (Part 2).** Which pages exist, which reader owns each, which mode each is in. Governs every document type.
- **The CRX market-maker document register (Part 1).** Sentence register and flow for the formal documents CRX hands to desks ("MM documents"): the Margin and Settlement Overview, the Collateral Overview, companion methodologies (IM, VM, closeout, collateral curation). **Priority**: there it governs every sentence and wins wherever it differs from the general voice or a law. The architecture still applies: which pages exist, MECE coverage, honesty lines, every reference resolves.

For an MM document, read the register first. Otherwise the general voice holds.

## Foundations

- **Diátaxis** (Daniele Procida): four modes, tutorial (learning by doing), how-to (a task), reference (look-up), explanation (understanding why). One page never mixes two (law 11).
- **Feynman Technique** (Richard Feynman): explain it to a novice in plain words. Jargon marks a gap you don't understand; close it, then write.
- **Every Page Is Page One** (Mark Baker): readers arrive mid-stream from search. Every page stands alone, sets its own context, links out.
- **Minimalism** (John Carroll, *The Nurnberg Funnel*): start from the reader's real task, cut the rest, help them recover from errors.
- **Pyramid Principle** (Barbara Minto): answer first, supporting points beneath. Never make the reader wait for the conclusion.
- **Curse of Knowledge** (Pinker; Heath brothers): the expert forgets what the novice doesn't know. Re-read your draft as a reader who knows nothing.

---

# Part 1: The CRX market-maker document register

## The genre

A desk deciding whether to trust a venue reads the rules document once, start to finish. Not a spec (nobody implements from it), not marketing (nobody is persuaded by it), not a handbook page (nobody lands mid-stream). The desk tests whether the system is *designed*: each mechanism exists for a reason and hands off cleanly to the next. The prose must do two things at once: state rules exactly, and carry the reader through them as one connected system.

## The register

One lens: **a clearinghouse risk engineer explaining the live system to a desk, on the record.** Authority comes from precision and mechanism, never diction; a sentence earns trust by being checkable. Take the *content discipline* of LCH / CME and the *voice* of Hyperliquid / Ostium.

**Take from LCH / CME:**
- Defined terms introduced once, then used verbatim: IM, VM, MM, cure window, closeout mark, election. *Novate*, *haircut*, *netting* are exact mechanism names, not costume; they stay.
- Exact parameters: windows, thresholds, calibration targets, asset lists, with numbers and dates.
- Completeness: every state the system can enter has a stated outcome. No mechanism trails off.
- Lifecycle structure: numbered sections walking trade → margin → marks → cure → closeout → settlement.
- Neutral temperature: never sell, reassure or dramatize.

**Refuse from LCH / CME (costume):** ceremonial grammar (*shall*, *hereby*, *herein*, *thereof*, *pursuant to*, *absent* as a preposition, *in the event that*, legal *where* as a conditional); inversions for gravitas; decree voice about the document ("This document sets out…", "governs", "binds": the document describes the system, it does not ordain); synonym doublets ("terms and conditions" pairs that add words, not meaning).

**Take from Hyperliquid / Ostium:**
- Plain declaratives: the mechanism as subject, a working verb. Anchor, from Hyperliquid's margining page: *"The maintenance margin is currently set to half of the initial margin at max leverage."* A parameter, stated flat, checkable in one read.
- System verbs: posts, nets, settles, auctions, enters, releases, converts, triggers.
- Spoken conditions: *when*, *if*, *by default*. Not *where*, *absent*, *in circumstances where*.

**Refuse from Hyperliquid / Ostium (casualness):** second person (MM documents are third person, always); marketing superlatives ("tightest spreads", "deepest liquidity"), feature-selling, *simply*, *just*, exclamation, emoji; hedge qualifiers ("basically", "essentially", "roughly"). State the rule, or state that it is forthcoming.

## The sentence test

Every sentence passes all five: new ones as written, existing ones on any edit pass.

1. **Concrete subject**: a thing in the system (a position, an account, collateral, the mark, a maker, CRX). Never an abstraction about the document or an empty frame ("It is the case that…").
2. **Working verb**: an action the system performs or a state it holds. Kill decree verbs and being-verb stacks that describe the document, not the machine.
3. **Sayable on a call**, the strongest anti-costume test: if Jake would not say it out loud to a desk head, rewrite it. "Absent any election" fails; "By default" passes.
4. **Exact where it counts**: numbers, windows, thresholds and defined terms survive verbatim. A plain sentence with a soft number is worse, not friendlier.
5. **Neutral temperature**: no reassurance adverbs (*robustly*, *securely*, *seamlessly*), no drama, no aphorism or seesaw ("tighten immediately, loosen only with review": split into two plain sentences).

## The costume sweep

Apply on sight. The left column comes from our own drafts.

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

The sweep targets grammar, not vocabulary. *Election*, *novation*, *cure*, *haircut*, *closeout mark* stay; the costume is conjugating them ceremonially.

**Passive voice** is allowed when the actor is system-obvious and the sentence short: "IM is released to each participant's margin account." It is banned where it hides who acts at a decision point: wherever discretion, election or governance is involved, name the actor. "Risk parameters are tightened" hides the hand; "CRX tightens risk parameters" shows it.

## The seven flow principles

Register makes sentences right; flow makes them read as one system. Maximum compression is the standing failure: perfect isolated sentences read as an index of rules. Keep sentences tight; build flow between them.

1. **Purpose before mechanism.** Open every section with one clause naming what the mechanism protects, guarantees or achieves; then how it works. A purpose that needs a paragraph belongs in a methodology doc. *Initial margin (IM) is the collateral that protects participants against counterparty default. Both sides post it at trade…*
2. **Given → new**, the flow engine. Open each sentence with what the reader already holds, usually from the previous sentence; end on the new fact. One sentence's object becomes the next one's subject. A choppy paragraph almost always opens each sentence on new material.
3. **Walk the lifecycle.** The deep structure is time: trade → margin posted → marks move → VM flows → cure → closeout → expiry. Openers carry it: *at trade, while a position is open, upon breach, at expiry.* Temporal and conditional scaffolding is the genre's native connective tissue.
4. **One paragraph, one movement**: rule → mechanism → consequence, in that order. Never a stack of parallel atoms sharing a topic. Two rules that do not develop each other are two paragraphs, or one goes to an exhibit.
5. **Deliberate cadence.** Vary sentence length in every paragraph. A short sentence lands only when its neighbors are longer; three consecutive sentences of equal weight read as staccato. Standard: a long establishing sentence, then the short rule.
6. **Anaphoric stitches.** Demonstrative back-references (*this requirement, that mark, the same window*) knit sentences into paragraphs. A stitch points at a specific antecedent; filler ("in addition", "moreover") points at nothing. A needed transition with no stitch available means the information order is wrong (principle 2).
7. **The compression budget.** Two new facts per sentence; a third gets its own sentence or moves to an exhibit. Overloaded sentences are decoded, not read: parse effort is the tell, participle stacks the usual culprit. The budget has a floor too: connective tissue (a purpose clause, a stitch, a subordinated consequence) carries zero facts and never counts; cutting it produces the too-tight read. Hard trigger: **three consecutive sentences that each open with a brand-new subject read as an index, however good each one is.** The fix is rarely deleting facts: merge a rule with its consequence into one subordinated sentence (*if the window expires unmet, closeout begins*), open with time (*while a position is open…*), and let the previous object become the next subject.

## Standing bans

Never "so" in any form. Never a sentence opening with "Because". No em dashes in document body prose. No participle trailers ("with X-ing"). No aphorisms or seesaw constructions. Third person, present tense throughout.

## Bench: before → after

Real lines from our drafts. Study the moves, not just the outputs.

**Legal conditional → spoken conditional.** *Absent any election, an account posts, accepts, and settles in USDC alone* → *By default, an account posts, accepts, and settles in USDC only.* The triplet stays: each verb is a distinct mechanism. Only the ceremonial opener changes.

**Inversion → direct statement, actor visible.** *The default terms bind no account. An account may adopt alternative collateral terms, or publish and capitalize its own, certified against the network's standard terms* → *No account is locked into the default terms. An account can adopt alternative collateral terms, or publish and capitalize its own; new terms are certified against the network's standard framework.*

**Circumstance frame → trigger statement.** *Closeout occurs in one of two circumstances: the cure window expires unmet, or the account's balance falls to the MM threshold* → *Two events trigger closeout: a cure window expires unmet, or the account's balance falls to the MM threshold.*

**Seesaw → two plain sentences.** *Risk parameters tighten immediately, loosen only with independent review* → *CRX can tighten risk parameters immediately. Loosening them requires independent review.* The mechanism (asymmetric governance) survives; the aphorism shape goes; the actor becomes visible.

**Index → system (a flow rewrite, not a register one)**
> Before: *Positions on CRX are collateralized on-chain. Both sides of every trade post collateral to smart contracts. Initial margin (IM) and variation margin (VM) are computed continuously and netted across each participant's full portfolio. Margin accounts unable to meet VM requirements enter cure windows. Unmet cure windows or breaches of maintenance margin (MM) trigger closeout. Positions settle against institutional benchmarks.*
> After: *Every position on CRX is collateralized on-chain: both sides of a trade post collateral to smart contracts. While a position is open, initial margin (IM) and variation margin (VM) are computed continuously and netted across each participant's full portfolio. A margin account that cannot meet its VM requirement enters a cure window; if the window expires unmet, or the account breaches maintenance margin (MM), closeout begins. At expiry, positions settle against institutional benchmarks.*

Each before sentence passes the sentence test; the paragraph fails: six same-weight declaratives, each on a new subject. The after merges rule with consequence, gives the lifecycle to the openers, varies cadence. Same facts, four sentences.

## Revision procedure

Per section, in order. Register before flow: never chain sentences you will rewrite.

1. **Costume sweep**: the table and the sentence test on every sentence.
2. **Purpose** (flow 1): if sentence one does not say what the mechanism is for, write that clause first.
3. **Chain** (flow 2): underline each opening noun phrase; reorder until openings are given.
4. **Lifecycle** (flow 3): openers carry time where content is sequential.
5. **Cadence** (flow 5): read aloud; split or merge one of any three consecutive equal-length sentences.
6. **Budget** (flow 7): count new facts per sentence; offload thirds.
7. **Ban sweep**: so / sentence-initial Because / em dashes / participle trailers / seesaws.

Facts are frozen in every register or flow pass: every number, term and rule survives verbatim unless the user approves a change. Reword and reorder; never re-litigate content.

**Self-review**, three reads in order: a desk head with thirty seconds (one designed system, no sentence that forces a restart?); a Hyperliquid docs reader (any costume? would each phrase survive being said out loud?); an LCH reviewer (every parameter exact, every term defined then used, every state accounted for?).

---

# Part 2: The eleven laws

### 1. Plan the learning paths before writing a word.

List each reader (role or persona) and, for each, the ordered questions they actually have. Cut every topic no one asks. The page set is the union of those questions, nothing more; each cluster becomes one page in one mode (law 11). Test the page map MECE:

- **No overlap**: no question answered on two pages. Two such pages are one page split in half: merge them; point every other page at the single home.
- **No gap**: every real reader question has exactly one owning page. A question with no home is a missing page; write it. A page with no question behind it is invented; cut it.

Refactor an existing doc set the same way, not page by page: list its pages beside the reader's real questions and map one to the other. Questions sharing a page split out; pages sharing a question fold together. Orphan pages (no question) get cut; orphan questions (no page) get written. The map drives the edits, not the old page order.

> A doc set is the questions a reader asks, in order — each with one home, none missing.

### 2. Every heading is a question.

Phrase each `##` as the reader's question, in their words: *"Where is my money held?"*, *"What if I run out?"*. The first sentence answers it; mechanism after. **Exception:** MM documents are lifecycle-ordered (trade → margin → marks → cure → closeout → settlement), not question-headed.

### 3. Build from the simplest idea up.

Define each term in plain words the moment you use it. Unpack every acronym once before using it. No leap the reader cannot follow. Teach what the thing depends on first: the Feynman move.

### 4. Terse. Vital facts only.

Short sentences. No analogy where the literal claim works. No scene-setting, storytelling, closing aphorism or "explaining life". Cut every sentence that does not teach.

### 5. No TL;DR.

Each section's first sentence is already the answer; a summary block on top only repeats it. Delete it.

### 6. Structure carries the meaning.

- Front-load: conclusion first, evidence after.
- Bullets for any list of 3+ items. Tables for any comparison of ≥ 3 rows.
- A time estimate on every internal link: `[Margin](/docs/margin) (~4 min)`.
- One register per section. Closed endings: a fact or a next link, never a trail-off.

### 7. State what is not true, out loud.

Every limitation gets its own bolded line, never buried mid-paragraph: **testnet only**, **mocked in the MVP**, **roadmap, not live**. Never overclaim: one buried caveat costs the whole page its trust.

### 8. One true story.

Every page agrees with the canonical source. When a page contradicts it, fix the page, even when the simplification reads well.

### 9. Every reference must resolve.

Any link, diagram id or asset you cite must exist: verify against the real registry or source. A fabricated id renders broken, silently. Grep before you cite.

### 10. Answer a how-to as a path, not a paragraph.

For anything the reader *does*: context, then concrete steps (*click here, then do this*), then what happens, including the branch (*it binds, or it expires*). A procedure buried in prose, or missing its outcome, leaves the reader unsure they did it right.

### 11. One page, one mode (Diátaxis).

Declare each page's mode in the frontmatter (`mode:`) and obey its contract:

| Mode | Answers | Contract |
|---|---|---|
| **Tutorial** | "take me through it the first time" | a guided run that always works: no choices, no theory |
| **How-to** | "how do I do X?" | numbered steps to a goal; the click-path and the outcome (law 10) |
| **Reference** | "what exactly is X?" | dry, complete, scannable; no teaching, no opinion |
| **Explanation** | "why does it work this way?" | the reasoning and trade-offs; no steps |

A how-to that drifts into theory, or a reference that starts teaching, is two half-pages: split it. **Exception:** an MM document is its own genre (a rules document read start to finish once), outside the four modes; the register governs it.

## The voice: before / after

For reader-facing docs, help pages and explainers: second person, question-headed. An MM document uses the register instead.

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

Context, click-path, outcome and its branch. Not a paragraph about how desks "always" work.

## Diagrams

Add one only where a visual carries what a sentence can't (a flow, a sequence, a branch, a hierarchy) and the prose does not already show it. Grammar:

- **Numbered stages**, each with a tracked-caps kicker: `1 · REQUEST FOR QUOTE`. Read left to right, top to bottom; the stages are the spine.
- **Simple boxes**: a bold title (`CRX`) and one small grey sub-label (`RFQ system`), nothing else. Every box is a noun the reader recognises.
- **Every arrow is a verb**, left to right, labeled with its action (`Request quote`, `Broadcast`). A return arrow carries the response: `← Quotes returned`.
- **One accent, one meaning**: white, thin-bordered boxes for steps; one accent colour for the reader's own actor; one dark-filled box for the terminal result. No decorative colour.
- **A pill marks a branch**: a rounded pill between stages, `Aspora accepts ✓ or rejects ✗`.
- **Let it breathe**: 3–5 boxes per row, a thin divider between stages, generous whitespace.

Reference shape, the CRX Trade Flow (`ASPORA` accented, `Settles in USDC` the one filled box):

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

Build it as one small static SVG or component: no runtime data, no JS. In a registry-based docs system, add it once, reference it by id, verify the id resolves (law 9). A diagram that renders "unknown" is worse than none.

## Process

1. **Plan**: per reader, the ordered questions (law 1). Show the page map: survive / merge / cut. If the cut is large, get a nod before writing.
2. **Write**: one page at a time. Question headings, answer-first, terse (laws 2–7); an MM document in lifecycle-ordered sections in the register.
3. **Cut**: merge duplicates; delete pages no reader needs. Fewer pages, each load-bearing.
4. **Validate**: no TL;DR blocks; every link resolves; every diagram and asset id exists; frontmatter complete; honesty lines present. For an MM document, run the revision procedure and self-review.

**Page template.** Frontmatter: title (a question or a short noun phrase), one-line description, **mode** (tutorial / how-to / reference / explanation), order, group. Body: question sections only, no TL;DR. End on a short **`Next:`** link line with a time estimate. A glossary only if the page introduces more than 3 new terms.

## Strict rules

- No TL;DR. No closing aphorisms. No analogy where the literal claim works.
- Short sentences. Vital facts only. Cut anything that does not teach.
- Every heading is the reader's real question, except in an MM document (lifecycle-ordered).
- Plan the per-reader question list before writing.
- State every limitation in its own bolded line.
- Verify every link and asset id against the source before shipping.
- MM document: the register is priority. Third person, present tense, no costume, no em dashes, no seesaws.

## Checks before delivery

- Per-reader question list planned; topics no one asks cut?
- Page map MECE: no question on two pages (overlap → merge), no real question without a page (gap → write it)?
- Every `##` a real reader question, answered in the first sentence? (MM documents excepted: lifecycle-ordered.)
- Each page exactly one Diátaxis mode (tutorial / how-to / reference / explanation), obeying its contract? (MM documents excepted: their own genre.)
- Zero TL;DR blocks?
- Short sentences, no flourish, no "explaining life"?
- Every link and diagram id resolves?
- Every limitation stated out loud, bolded, never buried?
- Any how-to: context set, click-path given, outcome and its branch stated?
- Any diagram: numbered stages, simple boxes, every arrow a verb, one accent, the terminal box filled? Does it earn its place over prose?
- MM document: passes the register's self-review (one designed system, no costume, every parameter exact)?
- Could you cut another page by merging two? If yes, cut it.

Any no: tighten before delivering.
