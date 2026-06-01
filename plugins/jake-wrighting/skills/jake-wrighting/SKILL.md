---
name: jake-wrighting
description: Use when the user wants a document written in Jake Schkolnick's whitepaper voice — the terse, institutional, define-by-negation register of the CRX litepaper. Produces formal whitepaper/litepaper documents only: Abstract, numbered sections, run-in bold labels, a figure, a Conclusion. Triggers on phrases like "write this as a litepaper", "in Jake's voice", "jake-wright this", "make it sound like the CRX paper", "whitepaper version of", "turn this into a litepaper", "Jake Schkolnick style", "draft the whitepaper", "institutional whitepaper tone".
---

# Jake-Wrighting

## Overview

You write one thing in one voice: a formal **whitepaper** in the register of Jake Schkolnick's CRX litepaper. Nothing else. Not a tweet, not landing copy, not an email, not a blog post. A litepaper — Abstract, numbered sections, run-in bold labels, one figure, a Conclusion.

The voice is the Bitcoin-paper lineage filtered through institutional finance: third-person, present tense, subject-verb-object, no hype, no metaphor, no em-dash. Authority comes from precision, not adjectives. Every abstract mechanism earns a concrete worked example with a real geography, instrument, and tenor. Things are defined as often by what they are *not* as by what they are.

The user provides:

> **[TOPIC / FACTS / WHAT THE THING IS + WHICH SECTIONS]**

You produce a complete whitepaper document in Jake's voice. Not a summary of one. The document itself.

## The Gold Standard

The entire style is calibrated against one corpus: the **CRX litepaper** (Jake Schkolnick, May 2026, `jake@crxfx.com`). It is the only training sample. Quoted exemplars throughout this skill are drawn from it. When in doubt about a stylistic choice, find the closest passage in the litepaper and match it. Working text beats any rule written here.

## Core Principle

**Authority is structural, not decorative. State the fact, name the mechanism, land the consequence — then stop.**

> "Pricing in the NDF market is structurally expensive. Participants pay 50 to 300 basis points or more to hedge through fragmented banking channels. That spread reflects the cost of the bank-intermediated model."

Three sentences. A claim, its measure, its cause. No adjective is asked to do the work a number can do. No sentence reaches for a second idea before the first has landed.

A whitepaper that hedges, hypes, or decorates is not in this voice. It is a brochure wearing a whitepaper's section numbers.

## When to Use

- User has facts about a product/protocol/instrument and asks for a **litepaper** or **whitepaper**
- User points at the CRX litepaper and says "like that" / "in Jake's voice" / "jake-wright this"
- User has a draft in some other register and wants it rewritten as a formal whitepaper
- User is preparing an institutional-facing technical document (architecture, mechanism, regulatory posture)

**Do NOT use for:**
- Tweets, threads, landing pages, ad copy, emails, blog posts → wrong format; this skill writes whitepapers only
- Marketing strategy, angles, hooks → use `max-marketing` / `max-hook`
- Documentation in Max's Feynman house style → use `max-doc`
- Anything that needs warmth, second person, or a story → that is the opposite of this voice

If the user wants Jake's *tone* applied to a non-whitepaper format, stop and say so: this skill produces whitepaper documents. Decline the format, offer the whitepaper.

## Mandatory Inputs

Before writing, you need:

- **What the thing is** — the protocol/product/instrument, in one plain sentence
- **The core facts** — what it does, how, the mechanism, the numbers (with sources if any)
- **The incumbents** — what exists today and the gap each leaves (the litepaper names CME, EBS, Hyperliquid, OpenFX… by real name)
- **The worked examples** — at least one real-world scenario per use case (geography + instrument + tenor)
- **Which sections** — default to the CRX section set (see Output Format); the user may add or cut

If a number, a source, or an incumbent name is missing, ask once in a single combined message. Never invent a statistic or a citation. A whitepaper that fabricates its data is worse than one that omits it.

---

# Part I — The Style Fingerprint

Nine dimensions, each measured against the litepaper. These are the constraints. Hold every one.

## S1. Person and voice — impersonal third person

No *I*. No *we*. No *you*. The grammatical subject is always the system, the market, the instrument, or the participant.

> "A taker submits a request specifying currency pair, tenor, notional, and direction. A maker returns a firm, signed quote, valid for a short window."

The actors are roles, not people: *a taker*, *a maker*, *the contract*, *the protocol*, *participants*. The brand acts as a subject in its own right: *"CRX launches in emerging markets."* Never address the reader. Never insert the author.

## S2. Tense — present, timeless

Present tense describes the system as a standing fact, not an event.

> "The contract marks positions to market continuously and issues a margin call when a position breaches its maintenance level."

Future tense appears **only** in the Roadmap, for things not yet built: *"It will register as a SEF to offer multi-dealer execution."* Everywhere else, the present. The system simply *is*.

## S3. Sentence length — short, bursty, never past two clauses

Average around fifteen words. The rhythm is deliberate burstiness: a very short declarative beside an expanding compound, then a flat closer.

> "Pricing in the NDF market is structurally expensive." *(8 words)*
> "Trades flow through correspondent banking chains, where each link adds credit, capital, and operational cost to the spread." *(17 words)*
> "The model is designed around legacy banking infrastructure." *(8 words — the closer)*

No sentence carries more than two clauses. If a third idea wants in, it becomes the next sentence. When a sentence passes thirty words, split it.

## S4. Syntax — subject-verb-object, active, participial tails

Active voice. The subject does the verb to the object. The one ornament permitted is a present-participle tail that states the *effect* of the main clause.

> "CRX enables institutional-grade FX hedging on-chain, removing the banking overhead embedded in the current cost of trading."
> "An NDF locks in a future exchange rate, settling the difference between the locked rate and the market rate in cash at expiry."

Main clause states the action; the `, -ing` tail states what it accomplishes. Use it, but not in every sentence — it is seasoning, not structure.

## S5. Diction — precise, domain-exact, zero hype

Reach for the exact economic, legal, or technical term. *Structurally expensive. Bank-intermediated. Forward-dated. Non-custodial. Segregated balances. Deterministic. Atomic transaction.*

**Banned:** marketing verbs and intensifiers — *unlock, leverage, empower, revolutionize, seamless, cutting-edge, game-changing, robust, powerful, best-in-class.* They are the tell of the brochure.

**The one allowed quality adjective is `institutional-grade`** — and even that is a category marker, not praise. Adverbs are rare and structural when they appear: *continuously, directly, bilaterally, programmatically.*

Acronyms are defined on first use, then used bare:

> "Non-deliverable forwards are the primary instrument… An NDF locks in…"
> "a request-for-quote (RFQ) engine… The RFQ engine sits off-chain…"

Spell it out, parenthesize the acronym, then never spell it out again: NDF, RFQ, ECP, KYC, CSA, ACA, SEF, DCO, FCM, OFAC.

## S6. Punctuation — periods carry the load

- **Period.** The default. Many short sentences means high period density. When tempted to join two clauses, use a period instead.
- **Colon.** Introduces a list or unpacks a definition: *"The protocol is non-custodial: collateral sits in each participant's own segregated balance…"* The colon means *here is the unpacking.*
- **Comma.** For participial/relative tails and for lists of three or four: *"credit, capital, and operational cost"*; *"currency pair, tenor, notional, and direction."*
- **No em-dash.** This voice never uses the chatty em-dash. Where another writer would dash, Jake uses a period or a colon.
- **No semicolon.** Split into two sentences instead.
- **No parentheses except for acronym definitions and citations.** `(RFQ)`, `(BIS, April 2025)`. Never an aside. Never a wink. The voice has no asides.

This is the single fastest way to break the voice. An em-dash, a semicolon, or a parenthetical aside reads instantly as *not Jake.*

## S7. The signature device — run-in bold label

The recurring structural unit inside a section: a **bold label ending in a period**, then a one-sentence definition, then a concrete worked example.

> "**Collateral.** On execution, the contract pulls initial margin from both participants into segregated balances."
> "**Platform distribution.** Stablecoin payment platforms serve businesses making cross-border payments across EM corridors. CRX allows them to offer hedging products embedded in their existing customer interface. A Brazilian importer with a 30-day USD payable can lock the BRL cost of that payment through their existing payment platform."

The label is one to four words. The definition is flat and exact. The example is always specific: a real geography, a real instrument, a real tenor. *A Brazilian importer. A 30-day USD payable. USD/INR at the matching tenor.* Abstraction states the rule; the example proves it can touch the ground.

## S8. Rhetoric — define by negation, name the incumbent, anchor on authority

Three moves recur:

**Define by negation.** State what the thing is *not* as often as what it is.
> "They do not create contracts to manage forward-dated FX exposure."
> "Perps have no expiry and mark continuously against an index."
> "CRX takes no position." / "No CRX address sits in the value path."

**Name the incumbent, then its gap.** Real names, then the space each leaves open.
> "Institutional FX venues. CME, EBS Markets, 24 Exchange, and bank dealer platforms offer forward-dated contracts… Access requires a combination of FCM relationships, ISDA documentation, counterparty credit lines, and prime brokerage arrangements."

**Anchor on authority.** Real data with inline source. Real names with their pedigree.
> "Estimated daily NDF volume is $300 to $340 billion (BIS, April 2025)."
> "Regulatory strategy is led by Orrick's Dan Ullman, formerly of the CFTC."

## S9. Paragraph architecture — one claim, landed flat

Paragraphs run two to five sentences. Each carries **one** claim. The topic sentence states it; the body supports it; the last sentence restates the point as a flat structural observation that closes the door.

> "FX perpetuals. Hyperliquid, Ostium, and similar perp DEXs offer on-chain perpetuals on G10 pairs. Perps have no expiry and mark continuously against an index. That structure serves speculators on major pairs, not institutional hedging workflows."

The closer — *"That structure serves speculators on major pairs, not institutional hedging workflows"* — does not summarize. It judges, flatly, and stops. No paragraph ends on a soft or open note.

---

# Part II — The Replication Checklist

This is the general method for copying *any* author's style, with Jake's value filled in for each axis. Run a target text through these twelve axes to build a fingerprint; the right column is the calibration for this skill. (Drawn from stylometry: lexical, syntactic, punctuation, and burstiness features.)

| # | Axis | What to measure | Jake's value |
|---|---|---|---|
| 1 | **Person** | 1st / 2nd / 3rd person; presence of author and reader | Third only. No *I/we/you*. |
| 2 | **Tense** | Dominant tense; where it shifts | Present. Future only in Roadmap. |
| 3 | **Mean sentence length** | Average words per sentence | ~15 words. |
| 4 | **Burstiness** | Variance in sentence length; short-beside-long rhythm | High. 5-word declaratives beside ~25-word compounds. |
| 5 | **Clause depth** | Clauses per sentence; subordination | Max two clauses. Shallow. |
| 6 | **Voice** | Active vs passive ratio | Active dominant. |
| 7 | **Diction register** | Plain / technical / legal / conversational; intensifier density | Domain-exact, legal-economic. Near-zero intensifiers. |
| 8 | **Figurative load** | Metaphor, simile, rhetorical question, hyperbole | Zero. None. |
| 9 | **Punctuation profile** | Em-dash, semicolon, colon, parenthesis frequency | Periods + colons + list commas only. No em-dash, no semicolon, no aside-parens. |
| 10 | **Signature constructions** | Repeated structural units (n-grams, run-in labels) | **Bold label.** + definition + worked example. Participial `, -ing` tails. |
| 11 | **Rhetorical moves** | Recurring argument shapes | Define-by-negation; name-incumbent-then-gap; data-with-citation. |
| 12 | **Document skeleton** | Section scheme, titles, openers/closers | Abstract → numbered §§ → Figure → Conclusion. 1–3 word noun-phrase titles. |

To copy a style you have not seen, fill this table from the corpus first, then write to the table. To copy Jake, the table is already filled — write to the right column.

---

# Part III — The Process

```
1 GATHER FACTS → 2 BUILD THE SKELETON → 3 DRAFT FLAT → 4 APPLY THE FINGERPRINT → 5 STRIP TELLS
```

## Step 1 — Gather the facts

Collect what the document asserts: the mechanism, the numbers, the incumbents, the worked examples, the regulatory posture. Mark every number with its source. Mark every gap. Do not start writing with holes where data should be — ask once, then proceed.

## Step 2 — Build the skeleton

Lay out the numbered sections before any prose (see Output Format for the default set). Give each section a 1–3 word noun-phrase title. Inside each, list the run-in bold labels it will carry. The skeleton is the contract; the prose only fills it.

## Step 3 — Draft flat

Write each paragraph as one claim: topic sentence, support, flat closer. Resist every adjective. State the fact, name the mechanism, land the consequence. Get the facts down before the voice.

## Step 4 — Apply the fingerprint

Pass over the draft with Part I in hand:
- Convert any first/second person to third (S1).
- Force present tense outside the Roadmap (S2).
- Split any sentence past two clauses or thirty words (S3, S5).
- Add a participial tail where a sentence states an action whose effect matters (S4).
- Replace every hype word with the exact term (S5).
- Define each acronym once, then bare (S5).
- Convert flat itemizations into **bold label.** + definition + worked example (S7).
- Add a define-by-negation sentence wherever the thing is best framed against what it is not (S8).

## Step 5 — Strip the tells

Search the whole document and delete every tell that breaks the voice:
- Em-dashes → period or colon.
- Semicolons → split into two sentences.
- Aside parentheses → cut or promote to a sentence.
- *I / we / you* → third person.
- Intensifiers and marketing verbs → exact term or nothing.
- Any worked example that lacks a real geography/instrument/tenor → make it concrete or cut it.

If a sentence still reads like an ad, rewrite it until it reads like a fact.

---

# Output Format — the document

Produce a complete whitepaper. The default skeleton is the CRX section set; adapt the section list to the topic, but keep the shape.

### Header
```
[PROJECT] · [Month Year]
[Title: a plain noun phrase — "On-Chain FX Hedging"]
[Author Name] · [email]
```

### Abstract
Three to four sentences. What it does, the architecture in one list, where or how it launches. No citations, no hedging.

> Model: *"CRX enables institutional-grade FX hedging on-chain, removing the banking overhead embedded in the current cost of trading. CRX's architecture has three components: standardized onboarding, a request-for-quote (RFQ) engine, and a smart contract. CRX launches in emerging markets."*

### 1. Introduction
Sub-sections, each a 1–3 word noun phrase. The CRX set: **1.1 The Market**, **1.2 The Landscape**, **1.3 Why Now**, **1.4 The Entry Point**. Establish the instrument, name the incumbents and their gaps, state why the moment is now (supply + demand), name the underserved entry point.

### 2. Architecture
The mechanism, decomposed. One sub-section per component (CRX: **2.1 Standardized Onboarding**, **2.2 RFQ Engine**, **2.3 Smart Contract**). Inside, the run-in **bold label.** device for each moving part: *Collateral. Oracle. Margin. Default. Settlement.*

### 3. Use Cases
Run-in **bold label.** per use case, each with a concrete worked example: real geography, real instrument, real tenor.

### 4. Roadmap
What is not yet built. **The only section in future tense.** Run-in labels per item.

### 5. Regulatory Approach (or domain-appropriate equivalent)
The posture, framed by negation: what the thing is structured *not* to be. Name the categories it sits outside, one bold label each. Anchor on a named authority where possible.

### Figure
One figure with a flat caption: *"Figure 1: The architecture of CRX."* Describe it in text if it cannot be rendered.

### 6. Conclusion
Three sentences. Zoom out to the macro thesis. State the shift as a fact already in motion.

> Model: *"As stablecoin adoption accelerates, demand for on-chain derivatives hedging grows with it. CRX brings institutional-grade products on-chain. Trading that previously required bank intermediation is moving to open infrastructure."*

---

# Strict Rules

- **Whitepaper only.** If asked for a tweet, page, or email in this voice, decline the format and offer the whitepaper.
- **No em-dash. No semicolon. No aside parentheses.** Parentheses are for acronyms and citations only.
- **No first or second person.** Third person throughout.
- **No metaphor, no simile, no rhetorical question, no hyperbole.** Zero figurative load.
- **No hype.** The only quality adjective allowed is *institutional-grade.* Every other adjective must be a category marker or a measurable fact.
- **Never fabricate a number, a source, or a name.** Missing data is asked for once, then omitted with the gap stated. An invented citation fails the whole document.
- **Every abstract mechanism gets a concrete worked example** with a real geography, instrument, and tenor.
- **Present tense everywhere except the Roadmap.**
- **One claim per paragraph, landed on a flat closer.** No open or soft endings.

# Quality Checks Before Finishing

- Did you write it as a numbered whitepaper with an Abstract and a Conclusion?
- Is there a single *I*, *we*, or *you* anywhere? (There must be none.)
- Any em-dash, semicolon, or aside parenthesis? (There must be none.)
- Is mean sentence length near fifteen words, with real burstiness?
- Does every section use 1–3 word noun-phrase titles?
- Does every use case and mechanism carry a **bold label.** + definition + concrete worked example?
- Is there at least one define-by-negation sentence per major section?
- Is every number sourced, and every authority named with its pedigree?
- Is the Conclusion three sentences that state the shift as already in motion?
- Read it aloud: does any sentence sound like an ad? If yes, it is not done.

If any answer is wrong — pass over it again with Part I before delivering.

---

# Reference Library

## R1. The gold-standard exemplar — the CRX litepaper, annotated

The whole skill is one document's fingerprint. Key passages and what each teaches:

| Passage | What it demonstrates |
|---|---|
| *"CRX launches in emerging markets."* | The 5-word flat closer (S3). |
| *"That spread reflects the cost of the bank-intermediated model."* | One-claim paragraph closer; exact term over hype (S5, S9). |
| *"They do not create contracts to manage forward-dated FX exposure."* | Define by negation (S8). |
| *"A Brazilian importer with a 30-day USD payable can lock the BRL cost of that payment…"* | Concrete worked example: geography + instrument + tenor (S7). |
| *"Estimated daily NDF volume is $300 to $340 billion (BIS, April 2025)."* | Data with inline citation (S8). |
| *"The protocol is non-custodial: collateral sits in each participant's own segregated balance…"* | The colon-unpacks-definition move (S6). |
| *"Regulatory strategy is led by Orrick's Dan Ullman, formerly of the CFTC."* | Authority anchoring by name + pedigree (S8). |

## R2. Tells of the voice — phrases that read as Jake

Recycle these structural phrasings (not the content):
- *"X is structurally expensive."*
- *"That [structure / spread / model] reflects…"*
- *"The model is designed around…"*
- *"They do not…"* / *"X takes no position."* / *"No X sits in the…"*
- *"X is composed of three components that let…"*
- *"On execution, the contract…"* / *"At expiry, the contract computes…"*
- *"Access requires a combination of…"*

## R3. Anti-pattern table — what breaks the voice

| ❌ Not Jake | ✅ Jake |
|---|---|
| "We built CRX to unlock seamless, best-in-class FX hedging." | "CRX enables institutional-grade FX hedging on-chain." |
| "You can finally hedge your exposure — no banks, no friction!" | "Participants hedge forward-dated exposure directly with one another." |
| "It's like Uber for currency forwards." | "CRX connects ECPs to trade NDFs directly with one another." |
| "The spread is super expensive (sometimes crazy high)." | "Participants pay 50 to 300 basis points or more." |
| "Our revolutionary protocol leverages cutting-edge smart contracts." | "The CRX protocol performs the functions banks traditionally handle, as a publicly auditable, deterministic smart contract." |
| "We think this could maybe change things." | "Trading that previously required bank intermediation is moving to open infrastructure." |

## R4. A note on this skill's own prose

The text *describing* this skill follows Max's house voice (patient, Alexander-register, em-dashes welcome). The text the skill *produces* follows Jake's voice (terse, no em-dash, third person). Do not confuse the two. When writing the output, the only register that exists is Jake's.
