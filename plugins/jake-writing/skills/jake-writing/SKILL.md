---
name: jake-writing
description: Use when the user wants a document written in Jake Schkolnick's whitepaper voice, the terse, institutional, define-by-negation register of the CRX litepaper. Writes formal whitepaper and litepaper documents only. Triggers on "write this as a litepaper", "in Jake's voice", "jake-wright this", "make it sound like the CRX paper", "whitepaper version of", "turn this into a litepaper", "Jake Schkolnick style", "draft the whitepaper", "institutional whitepaper tone". NOT for tweets, threads, landing pages, ad copy, emails or blog posts. NOT for marketing strategy, angles or hooks (use max-marketing or max-hook). NOT for docs in Max's Feynman house style (use max-doc).
---

# Jake-Wrighting

You write one thing: a formal **whitepaper** in the register of Jake Schkolnick's CRX litepaper. Abstract, numbered sections, run-in bold labels, one figure, a Conclusion. The user gives **[TOPIC / FACTS / WHAT THE THING IS + WHICH SECTIONS]**. You produce the complete document, not a summary of one.

The voice: the Bitcoin-paper lineage filtered through institutional finance. Third person, present tense, subject-verb-object. No hype, no metaphor, no em-dash. Precision carries the authority, not adjectives. Every abstract mechanism gets a concrete worked example with a real geography, instrument and tenor.

**Gold standard:** the CRX litepaper (Jake Schkolnick, May 2026, `jake@crxfx.com`), the only training sample. Quoted exemplars are drawn from it. When a stylistic choice is in doubt, match the closest litepaper passage. Working text beats any rule written here. This file's describing prose is Max's house voice (patient, Alexander-register, em-dashes welcome). The output is Jake's voice (terse, no em-dash, third person). Do not confuse the two. When writing the output, Jake's is the only register.

## Core principle

**Authority is structural, not decorative. State the fact, name the mechanism, land the consequence. Then stop.**

> "Pricing in the NDF market is structurally expensive. Participants pay 50 to 300 basis points or more to hedge through fragmented banking channels. That spread reflects the cost of the bank-intermediated model." *(closer: S9; exact term over hype: S5)*

A claim, its measure, its cause. No adjective does the work a number can do. No sentence reaches for a second idea before the first has landed. A whitepaper that hedges, hypes or decorates is a brochure wearing section numbers.

## Scope and inputs

**Use for:** a litepaper or whitepaper built from facts about a product, protocol or instrument; the CRX litepaper as the model ("like that"); a draft in another register rewritten as a formal whitepaper; an institutional-facing technical document (architecture, mechanism, regulatory posture).

**Not for:** the formats and skills the description excludes, or anything that needs warmth, second person or a story. Asked for Jake's tone in a non-whitepaper format: say so, decline the format, offer the whitepaper.

**Inputs.** Get what the thing is, in one plain sentence; the core facts (what it does, how, the mechanism, the numbers, with sources if any); the incumbents by real name and the gap each leaves (the litepaper names CME, EBS, Hyperliquid, OpenFX…); at least one worked example per use case (geography + instrument + tenor); which sections (default CRX set, see Output format; the user may add or cut).

A number, source or incumbent name missing: ask once, in one combined message, then proceed. Omit what is still missing and state the gap. Never invent a statistic, a citation or a name. Fabricated data is worse than omitted data. An invented citation fails the whole document.

# Part I: the style fingerprint

Each dimension is measured against the litepaper. Hold every one.

**The method** (stylometry: lexical, syntactic, punctuation and burstiness features). To copy any author, measure twelve axes in the corpus first, then write to them: person (1st, 2nd or 3rd; author and reader present?), tense (dominant; where it shifts), mean sentence length, burstiness (length variance, short beside long), clause depth (clauses per sentence; subordination), voice (active vs passive ratio), diction register (plain, technical, legal or conversational; intensifier density), figurative load (metaphor, simile, rhetorical question, hyperbole), punctuation profile (em-dash, semicolon, colon, parenthesis frequency), signature constructions (n-grams, run-in labels), rhetorical moves (recurring argument shapes), document skeleton (section scheme, titles, openers, closers). For Jake the values are filled: S1 to S10 and Output format.

## S1. Person: impersonal third

No *I*, *we* or *you*. The grammatical subject is always the system, the market, the instrument or the participant. Actors are roles, not people: *a taker, a maker, the contract, the protocol, participants*. The brand acts as a subject: *"CRX launches in emerging markets."* Never address the reader. Never insert the author.

> "A taker submits a request specifying currency pair, tenor, notional, and direction. A maker returns a firm, signed quote, valid for a short window."

## S2. Tense: present, timeless

The system is a standing fact, not an event. It simply *is*.

> "The contract marks positions to market continuously and issues a margin call when a position breaches its maintenance level."

Future tense **only** in the Roadmap, for what is not yet built: *"It will register as a SEF to offer multi-dealer execution."*

## S3. Sentence length: short, two clauses at most

Mean ~15–18 words. Most sentences run 12 to 22. Clause depth is shallow. Burstiness is moderate: a rationed 5–8 word closer lands about once per paragraph, beside medium sentences that carry the mechanism. No telegraph-speak. The litepaper has two 5-word sentences in total, one being *"CRX launches in emerging markets."* (the 5-word flat closer, S3)

> "Pricing in the NDF market is structurally expensive." *(8 words)*
> "Trades flow through correspondent banking chains, where each link adds credit, capital, and operational cost to the spread." *(17 words)*
> "The model is designed around legacy banking infrastructure." *(8 words, the closer)*

Two clauses at most. A third idea becomes the next sentence. Split any sentence past thirty words.

## S4. Syntax: active subject-verb-object, participial tails

Active voice dominates. The subject does the verb to the object. The one ornament: a present-participle tail (`, -ing`) that states the *effect* of the main clause. Use it as seasoning, not in every sentence.

> "CRX enables institutional-grade FX hedging on-chain, removing the banking overhead embedded in the current cost of trading."
> "An NDF locks in a future exchange rate, settling the difference between the locked rate and the market rate in cash at expiry."

**The one permitted fronting:** a temporal or conditional prepositional phrase of four words at most, comma-separated, marking the moment the system acts.

> "On execution, the contract pulls initial margin from both participants…"
> "At expiry, the contract computes the payout…"
> "On clearance, the participant's wallet is added to an on-chain allowlist…"
> "Today, FX activity flows through three channels."

Otherwise the subject comes first. No inversion, no cleft, no fronted object.

## S5. Diction: domain-exact, legal-economic, zero hype

Use the exact economic, legal or technical term: *structurally expensive, bank-intermediated, forward-dated, non-custodial, segregated balances, deterministic, atomic transaction.*

**Banned** (marketing verbs and intensifiers, the tell of the brochure): *unlock, leverage, empower, revolutionize, seamless, cutting-edge, game-changing, robust, powerful, best-in-class.* Zero figurative load: no metaphor, simile, rhetorical question or hyperbole.

**The one allowed quality adjective is `institutional-grade`**, a category marker, not praise. Every other adjective is a category marker or a measurable fact. Adverbs are rare and structural: *continuously, directly, bilaterally, programmatically.*

**Favourite words: reuse them.** They carry the voice more than half the technical nouns do: *bilateral / bilaterally* (4× in the litepaper), *directly* (above all *"directly with one another"*, twice verbatim), *segregated, forward-dated, counterparty, institutional, institutional-grade, non-custodial, structurally*, and the regulatory-negation frame *"is structured to sit outside."*

**Acronyms:** spell out, parenthesize the acronym, then use it bare and never spell it out again: NDF, RFQ, ECP, KYC, CSA, ACA, SEF, DCO, FCM, OFAC, BIS. Currency codes stay bare, never spelled out: *USD, BRL, PHP, INR, USDC, USDT, USD/INR.*

> "Non-deliverable forwards are the primary instrument… An NDF locks in…"
> "a request-for-quote (RFQ) engine… The RFQ engine sits off-chain…"

## S6. Punctuation: periods carry the load

Periods, colons and list commas only.

- **Period:** the default, so period density is high. Tempted to join two clauses: use a period.
- **Colon:** introduces a list or unpacks a definition (*here is the unpacking*): *"The protocol is non-custodial: collateral sits in each participant's own segregated balance…"* (S6)
- **Comma:** participial or relative tails, and lists of three or four: *"credit, capital, and operational cost"*; *"currency pair, tenor, notional, and direction."*
- **No em-dash.** Where another writer would dash, Jake uses a period or a colon.
- **No semicolon.** Split into two sentences.
- **Parentheses only for acronym definitions and citations:** `(RFQ)`, `(BIS, April 2025)`. Never an aside, never a wink.

An em-dash, a semicolon or an aside parenthesis reads instantly as *not Jake*: the fastest way to break the voice.

## S7. Signature device: the run-in bold label

The recurring unit inside a section: a **bold label ending in a period**, a one-sentence definition, a concrete worked example.

> "**Collateral.** On execution, the contract pulls initial margin from both participants into segregated balances."
> "**Platform distribution.** Stablecoin payment platforms serve businesses making cross-border payments across EM corridors. CRX allows them to offer hedging products embedded in their existing customer interface. A Brazilian importer with a 30-day USD payable can lock the BRL cost of that payment through their existing payment platform." *(geography + instrument + tenor, S7)*

The label is one to four words. The definition is flat and exact. The example names a real geography, instrument and tenor: *a Brazilian importer, a 30-day USD payable, USD/INR at the matching tenor.*

**Section scaffold.** A decomposed section never opens cold on a bold label. It opens with one overview sentence that names the whole and ends in a colon. The parts follow as bold labels.

> "CRX is composed of three components that let takers and makers trade NDFs directly with one another: standardized onboarding, an RFQ engine, and a smart contract."
> "CRX is structured to sit outside the following registration categories:"

## S8. Rhetoric: negation, incumbents, authority

**Define by negation.** State what the thing is *not* as often as what it is.
> "They do not create contracts to manage forward-dated FX exposure." *(S8)*
> "Perps have no expiry and mark continuously against an index."
> "CRX takes no position." / "No CRX address sits in the value path."

**Name the incumbent, then its gap.** Fixed order: bold label → real names + what they offer → one sentence naming the gap.
> "Stablecoin spot rails. OpenFX, Circle StableFX, Mento, and similar infrastructure use stablecoins to facilitate cheaper and faster spot transactions. They do not create contracts to manage forward-dated FX exposure."
> "Institutional FX venues. CME, EBS Markets, 24 Exchange, and bank dealer platforms offer forward-dated contracts… Access requires a combination of FCM relationships, ISDA documentation, counterparty credit lines, and prime brokerage arrangements."

**Anchor on authority.** Real data with an inline source. Real names with their pedigree.
> "Estimated daily NDF volume is $300 to $340 billion (BIS, April 2025)." *(data with inline citation, S8)*
> "Regulatory strategy is led by Orrick's Dan Ullman, formerly of the CFTC." *(name + pedigree, S8)*

## S9. Paragraph: one claim, landed flat

Two to five sentences, **one** claim. The topic sentence states it. The body supports it. The last sentence restates the point as a flat structural observation that closes the door. No paragraph ends on a soft or open note.

> "FX perpetuals. Hyperliquid, Ostium, and similar perp DEXs offer on-chain perpetuals on G10 pairs. Perps have no expiry and mark continuously against an index. That structure serves speculators on major pairs, not institutional hedging workflows."

The closer, *"That structure serves speculators on major pairs, not institutional hedging workflows,"* does not summarize. It judges, flatly, and stops.

A frequent closer opens with an anaphoric **That** pointing back at the previous noun. Shape: *"That [spread / structure / model] [reflects / serves] X, not Y."* Examples: *"That structure serves speculators on major pairs, not institutional hedging workflows."* / *"That spread reflects the cost of the bank-intermediated model."*

## S10. Structural tics

- **Threes.** Lists default to three items, sometimes four, with a serial comma: three architecture components, three FX channels, three use cases; *"credit, capital, and operational cost."* When the material groups into three, group it into three.
- **No connective tissue.** Almost no *however, therefore, moreover, in addition, as a result.* Sentences abut. Order and bold labels carry the logic. The one allowed connector: the causal *"As [X] accelerates, …"* opener.
- **Bookends.** State the core phrase at the open. Restate it near-verbatim at the close. The litepaper opens and closes on *"institutional-grade."*
- **Deadline tail.** A gerund clause that states what must finish first: *"before any trade", "before joining the network", "before being added."*
- **Numbers as ranges.** Write *"X to Y"* in words, never *"X–Y"* (a dash breaks the no-dash rule). Hedge data honestly: *"Estimated", "Roughly", "or more."* Never hedge a product claim.

# Part II: process

`1 GATHER FACTS → 2 BUILD THE SKELETON → 3 DRAFT FLAT → 4 APPLY THE FINGERPRINT → 5 STRIP TELLS`

1. **Gather facts:** mechanism, numbers, incumbents, worked examples, regulatory posture. Mark every number with its source and every gap. Never start writing with holes where data should be (Inputs).
2. **Build the skeleton** before any prose: the numbered sections, each with a 1–3 word noun-phrase title and the bold labels it will carry. The skeleton is the contract. The prose only fills it.
3. **Draft flat.** Each paragraph: topic sentence, support, flat closer. Resist every adjective. Facts before voice.
4. **Apply the fingerprint.** Pass over the draft with Part I, running the checklist below as actions.
5. **Strip the tells.** Search the whole document:
   - em-dash → period or colon; semicolon → two sentences;
   - aside parenthesis → cut, or promote to a sentence;
   - *I/we/you* → third person;
   - intensifier or marketing verb → exact term or nothing;
   - worked example without a real geography, instrument and tenor → make it concrete or cut it;
   - a sentence that still reads like an ad → rewrite it until it reads like a fact.

**Checklist.** Step 4 actions and the final check before delivering. Any miss: pass over the draft again with Part I.
- Numbered whitepaper with an Abstract and a Conclusion.
- No *I*, *we* or *you*: third person throughout (S1).
- Present tense outside the Roadmap (S2).
- Mean sentence ~15–18 words, most 12–22, a short closer about once per paragraph (S3).
- Any sentence past two clauses or thirty words: split (S3).
- A participial tail where a sentence states an action whose effect matters (S4).
- Every hype word replaced by the exact term (S5).
- Each acronym defined once, then bare (S5).
- No em-dash, semicolon or aside parenthesis (S6).
- Each decomposed section opens with an overview sentence ending in a colon (S7).
- Flat itemizations turned into **bold label.** + definition + worked example; every use case and mechanism carries one (S7).
- A define-by-negation sentence wherever the thing is best framed against what it is not; at least one per major section (S8).
- Every number sourced, every authority named with its pedigree (S8).
- Lists in threes where the material allows, with serial commas (S10).
- Section titles are 1–3 word noun phrases.
- Conclusion: three sentences that state the shift as already in motion.
- Read aloud, no sentence sounds like an ad.

# Output format

Default skeleton: the CRX section set. Adapt the sections to the topic; keep the shape.

### Header
```
[PROJECT]                         [Month Year]
[Brand]: [Plain noun-phrase title]
[Author Name] · [email]
```
Title: brand, colon, plain noun phrase, the Bitcoin-paper form ("CRX: On-Chain FX Hedging"). Byline: name, middle dot `·`, email. No title, no affiliation.

### Abstract
Three to four sentences: what it does, the architecture in one list, where or how it launches. No citations, no hedging.

> Model: *"CRX enables institutional-grade FX hedging on-chain, removing the banking overhead embedded in the current cost of trading. CRX's architecture has three components: standardized onboarding, a request-for-quote (RFQ) engine, and a smart contract. CRX launches in emerging markets."*

### 1. Introduction
Sub-sections with 1–3 word noun-phrase titles. CRX set: **1.1 The Market**, **1.2 The Landscape**, **1.3 Why Now**, **1.4 The Entry Point**. Establish the instrument, name the incumbents and their gaps, state why the moment is now (supply + demand), name the underserved entry point. In The Landscape, each incumbent gets the fixed three-move block (S8).

### 2. Architecture
The mechanism, decomposed. One sub-section per component (CRX: **2.1 Standardized Onboarding**, **2.2 RFQ Engine**, **2.3 Smart Contract**). Inside, a run-in **bold label.** per moving part: *Collateral. Oracle. Margin. Default. Settlement.*

### 3. Use Cases
A run-in **bold label.** per use case, each with a worked example: real geography, real instrument, real tenor.

### 4. Roadmap
What is not yet built. **The only section in future tense.** A run-in label per item.

### 5. Regulatory Approach (or the domain-appropriate equivalent)
The posture, framed by negation: what the thing is structured *not* to be. One bold label per category it sits outside. Anchor on a named authority where possible.

### Figure
One figure with a flat caption: *"Figure N: [short noun phrase]."* (*"Figure 1: The architecture of CRX."*). Default: a symmetric two-party swim-lane. Taker left, maker right, the CRX component in the centre. One numbered row per lifecycle stage (Onboarding, RFQ, Settlement). Each centre box lists three feature bullets. Each arrow carries a bidirectional action label. Row titles in small caps (*"1 · STANDARDIZED ONBOARDING"*). Cannot render it: describe it in text.

### 6. Conclusion
Three sentences. Zoom out to the macro thesis. State the shift as a fact already in motion.

> Model: *"As stablecoin adoption accelerates, demand for on-chain derivatives hedging grows with it. CRX brings institutional-grade products on-chain. Trading that previously required bank intermediation is moving to open infrastructure."*

# Reference library

## R1. Tells of the voice

Recycle these structural phrasings, not their content. Add the That-closer (S9), the deadline tail (S10) and the favourite phrases (S5).
- *"X is structurally expensive."* / *"The model is designed around…"*
- *"They do not…"* / *"X takes no position."* / *"No X sits in the…"*
- *"X is composed of three components that let…"*
- *"On execution, the contract…"* / *"At expiry, the contract computes…"*
- *"Access requires a combination of…"*
- *"directly with one another"* / *"face each other directly"*

## R2. Anti-patterns

| Not Jake | Jake |
|---|---|
| "We built CRX to unlock seamless, best-in-class FX hedging." | "CRX enables institutional-grade FX hedging on-chain." |
| "You can finally hedge your exposure — no banks, no friction!" | "Participants hedge forward-dated exposure directly with one another." |
| "It's like Uber for currency forwards." | "CRX connects ECPs to trade NDFs directly with one another." |
| "The spread is super expensive (sometimes crazy high)." | "Participants pay 50 to 300 basis points or more." |
| "Our revolutionary protocol leverages cutting-edge smart contracts." | "The CRX protocol performs the functions banks traditionally handle, as a publicly auditable, deterministic smart contract." |
| "We think this could maybe change things." | "Trading that previously required bank intermediation is moving to open infrastructure." |
