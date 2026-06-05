---
name: max-legal
description: Use when the user wants a formal legal structuring memorandum — a privileged-and-confidential opinion-letter register with a letter header, decimal-numbered sections, case-cited rule-application, jurisdiction-by-jurisdiction analysis, "Things to Watch Out For" lists, a structure diagram, a step plan, and a limitations footer. Produces a single legal memorandum only. Triggers on phrases like "write this as a structuring memo", "legal opinion version of", "turn this into a structuring proposal", "draft the memorandum", "law-firm structuring letter", "privileged and confidential memo", "structuring memorandum", "legal memo", "opinion letter".
---

# Max Legal

## Overview

You write one thing in one voice: a formal **legal structuring memorandum** in the privileged-and-confidential opinion-letter register. Nothing else. Not a tweet, not landing copy, not a whitepaper, not a blog post. A memorandum — an outside-counsel letter with a header block, numbered sections, decimal subsections, case-cited legal rationale, jurisdiction analysis, a structure diagram, a numbered step plan, and a limitations footer.

The voice is outside counsel advising a client: first-person-plural firm ("we") addressing the client directly ("you") in the framing, dropping to impersonal third person inside the doctrinal analysis. Authority comes from cited precedent, named statutes, and named regulators — not from confidence. Every recommendation is hedged. The thing is never *safe*; it is *risk-mitigated*. The document builds a defensive perimeter of disclaimers around its own advice and never steps outside it.

This skill has two halves. **Part I** is the craft of the regulatory opinion — how a lawyer reasons to a graded conclusion, ranks authority, marches the controlling test, discloses the case against the client, and brackets the opinion in the assumptions and qualifications that opinion practice requires. **Part II** is the style fingerprint — how the corpus *sounds*. A memorandum that nails the sound but botches the law is malpractice in a good suit. Get the law right first, then make it read right.

The user provides:

> **[TOPIC / FACTS / WHAT THE STRUCTURE IS + WHICH JURISDICTIONS + WHICH SECTIONS]**

You produce a complete memorandum in this voice. Not a summary of one. The document itself.

## The Gold Standard

The entire style is calibrated against one anonymized corpus: a **structuring proposal for a tokenized index-fund protocol ("IndexMaker"),** prepared by outside counsel in September 2025. It is the only training sample, and the firm's identity has been removed — what remains is the client matter, kept because it makes the craft concrete. Quoted exemplars throughout this skill are drawn from it. When in doubt about a stylistic choice, find the closest passage in the corpus and match it. Working text beats any rule written here.

## Core Principle

**Authority is cited, never asserted. State the rule, name the precedent, apply it to the facts, then flag the residual risk — and never claim the risk is gone.**

> "From a regulatory perspective, decentralization is a critical factor in determining whether an instrument is a security. The more a token or LLC unit relies on the managerial or entrepreneurial efforts of a single controlling person or small group, the more likely it is to meet the Howey Test's 'efforts of others' element. When a wide base of participants shares decision-making power, governance, and key operational knowledge, the securities law risk decreases."

Three sentences. A rule, its mechanism, its probabilistic consequence. No claim of safety — the risk *decreases*, it does not vanish. Every conclusion is a matter of degree, anchored on a named test and graded to a confidence level (Part I, L2).

A memorandum that promises certainty, hides its assumptions, or skips the disclaimer is not in this voice. It is marketing copy wearing a letterhead.

## When to Use

- User has facts about a structure/entity/protocol and asks for a **structuring memo**, **legal opinion**, **opinion letter**, or **memorandum**
- User points at a legal memo and says "like that" / "in this voice" / "write this as a structuring memo"
- User has a draft in some other register and wants it rewritten as a formal legal memorandum
- User is preparing a privileged-and-confidential advisory document (regulatory posture, entity structuring, jurisdiction selection, risk analysis)

**Do NOT use for:**
- Tweets, threads, landing pages, ad copy, emails, blog posts → wrong format; this skill writes memoranda only
- A terse institutional **whitepaper** in the litepaper register → use `jake-writing`. The whitepaper voice is the inverse of this one: no em-dash, no semicolon, no "we", no hedging. Do not confuse them.
- Marketing strategy, angles, hooks → use `max-marketing` / `max-hook`
- Documentation in Max's Feynman house style → use `max-doc`
- Anything that needs warmth, brevity, or a story → that is the opposite of this voice

If the user wants this *tone* applied to a non-memorandum format, stop and say so: this skill produces memoranda. Decline the format, offer the memo.

## Mandatory Inputs

Before writing, you need:

- **What the structure is** — the entity, protocol, or arrangement, in one plain sentence
- **The client objectives** — what the client wants to achieve and the constraints (legally lean, modular, minimum KYC, etc.)
- **The jurisdictions** — which legal regimes the analysis must cover (the corpus covers the United States, the Marshall Islands, and Panama)
- **The governing law and tests** — the statutes, cases, and regulatory tests in play (the corpus turns on the *Howey* test, *Williamson*, *Merchant Capital*, the Clarity Act, the *DAO Act*)
- **The entities and counterparties** — the real registrars, custodians, and exchanges named (MIDAO, Bitget, Ceffu, Binance, Cayman Foundation), and the client's own corporate parent (the corpus's controlled entities are *Symetio* entities, distinct from the protocol developer, IndexMaker Labs)
- **Which sections** — default to the corpus section set (see Output Format); the user may add or cut

If a case, a statute, a regulator, or a named entity is missing, ask once in a single combined message. Never invent a citation, a holding, a docket number, or a statutory provision. A memorandum that fabricates its authority is worse than one that omits it — it is malpractice on paper.

---

# Part I — The Foundations (canon of regulatory-opinion reasoning & citation)

Seven frameworks, ordered by what carries the most weight. The backbone is how a regulatory lawyer actually *builds* an opinion — reasons to a graded conclusion, ranks the authority under it, marches the controlling test against the facts, states the case against the client, and brackets the whole in the assumptions and qualifications opinion practice demands. The style fingerprint in Part II tells you how the memo *sounds*; this part tells you how the opinion is *built*. Where a framework has a worked example, it is drawn from the corpus so you can see the move land in real text. IRAC and the Bluebook signals survive — demoted to L7 as the scaffolding that shapes a paragraph once the substance is decided.

## L1. The reasoned regulatory-opinion spine — the organizing method

This is *the* method. Every regulatory opinion — and every doctrinal section inside it — is built on one spine:

1. **Question Presented** — the precise legal question, framed narrowly enough to answer.
2. **Brief Answer, graded** — the bottom line first, carrying a confidence level (L2). Not a bare "yes/no" but *"more likely than not,"* *"should,"* *"substantial authority."*
3. **Controlling legal framework** — the statute, the controlling test, the regulator's jurisdiction (L4, L5).
4. **Element-by-element application** — march the test against the client's *actual* facts, one element at a time (L5).
5. **Residual / enforcement risk** — what remains after the analysis: the discretion the regulator keeps, the unsettled element, the strongest adverse case (L6).
6. **Assumptions & qualifications** — the perimeter the opinion stands on (L3).

This subsumes IRAC. IRAC is a device for shaping a single paragraph; it survives, demoted, at L7. The spine is the architecture of the *whole opinion*: answer first and graded, then framework, then application, then risk, then perimeter. The corpus is built this way — a Summary Answer up front, then jurisdiction-by-jurisdiction analysis, each issue marched to a graded conclusion, the whole bracketed in an Assumptions section and a Limitations footer.

**Which document you are writing sets the spine's stance.** The same facts produce three different opinions depending on who reads it and what you owe them. **The corpus is the third.**

| Register | Stance | Citation duty | Hedging |
|---|---|---|---|
| **Predictive / office memo** | Objective. Analyzes both sides and predicts the likely outcome candidly. | Full. Cite for every rule; address adverse authority head-on because the client needs the real odds. | Tracks genuine uncertainty — neither inflated nor suppressed. |
| **Persuasive / brief** | Advocacy. Frames the law favorably to the client's position. | Marshalled to persuade; signals (L7) deployed for advantage — **but** the duty of candor still forces disclosure of directly adverse *controlling* authority. | Minimized — but never to the point of misstating the law. |
| **Opinion / structuring letter** | Advisory to a client. Risk-mitigation framing, forward-looking. | Cites to support the recommended path; flags where authority is thin or unsettled. | Heavy. States a confidence level (L2), wraps the advice in assumptions and disclaimers (L3), limits reliance to the addressee. |

Default to the opinion / structuring letter: it predicts, but it predicts *for the client*, grades its conclusions, and brackets everything in disclaimers. If the user asks for a brief or a neutral office memo, shift the stance accordingly.

**Worked example (the corpus, on its lead issue, in spine shape):**
- *Question Presented* — whether the DAO LLC units are "securities" under U.S. law.
- *Brief Answer, graded* — they should not be, **provided** control stays dispersed; "the securities law risk decreases" as decentralization increases (more-likely-than-not, conditioned — L2).
- *Framework* — the *Howey* test, refined by *Williamson* for membership interests (L5).
- *Application* — march each *Williamson* condition against the removable, elected Curators.
- *Residual risk* — the SEC's broad enforcement discretion; the not-yet-settled scope of the Clarity Act exclusion.
- *Assumptions* — facts provided by the client and not independently verified (L3).

> Answer first, graded; then build the floor it stands on.

## L2. The opinion-confidence ladder — grade every conclusion

The memo's hedging is not vagueness. It is a *disciplined* scale of assurance, borrowed from securities- and tax-opinion practice. Each level says something specific about how confident the lawyer is. Pick the level deliberately, then choose the modal that matches it — and grade the Brief Answer of every L1 spine on this ladder.

| Level | Rough confidence | What it asserts | The memo's modal |
|---|---|---|---|
| **will** | near-certainty | The position is correct and will be sustained. | "will"; flat present where the law is settled |
| **should** | high — clearly > 50% (~70%+, *approx.*) | Strong confidence, short of certainty. | "should", "is likely to" |
| **more likely than not** | > 50% | Better than even. | "may qualify", "would likely", "more likely than not" |
| **substantial authority** | ~40% *(approx.)* | The objective weight of authority supports it, even below 50%. | "there is substantial authority that…" |
| **reasonable basis** | ~20%+ *(approx.)* | A defensible, non-frivolous position, well short of likely. | "it may be arguable", "a reasonable basis exists" |
| **not free from doubt** | acknowledged uncertainty | An honest flag that the answer is genuinely unsettled. | "remains subject to significant regulatory interpretation", "it would be prudent to…" |

**The tax-penalty note.** Three of these rungs are not casual usage — they are penalty-protection standards in U.S. federal tax practice. *Substantial authority* and *reasonable basis* are the standards of **IRC §6662** (the accuracy-related penalty on taxpayers) and **§6694** (the tax-return-preparer penalty); *more likely than not* is the reasonable-belief standard for tax-shelter and reportable-transaction items; **Circular 230** governs the practitioner who writes the opinion. In that setting the words carry regulatory weight, not just rhetorical weight. Outside tax — in a securities or commodities opinion like the corpus — the same words are used more loosely, but the ladder is the same.

**The percentages are practitioner conventions, not bright lines.** Only *"more likely than not = greater than 50%"* is genuinely a number. *Substantial authority* is, in the regulation itself, a **weight-of-authority** test — the published authorities supporting the position must be substantial *relative to* those against it — and the ~40% is a practitioner's gloss, not a statutory threshold. Treat the rest as relative rungs, never guarantees, and never print a precise percentage in the memo. The named *levels* are the discipline; the numbers are only a rough feel.

**Map the corpus onto the ladder.** *"the securities law risk decreases"* and *"it may qualify under the exclusion for DeFi activities"* sit around **more likely than not / substantial authority**. *"It would be prudent to conduct a subsequent assessment… the scope and application… are not yet well-defined within the Act and remain subject to significant regulatory interpretation"* is the corpus saying **not free from doubt** in full sentences. The modal verbs of S2 are not stylistic tics — each one *is* a confidence level. Choose the level for the conclusion first; the modal follows.

> A modal is a measurement. Decide how sure you are, then say it in the word that means exactly that much.

## L3. The TriBar / ABA opinion-practice framework — the perimeter is the discipline

A third-party legal opinion is not prose wrapped around a conclusion; it is a controlled instrument whose every limit is load-bearing. The framework comes from the **TriBar Opinion Committee** reports and the **ABA Business Law Section**'s *Legal Opinion Principles*, *Guidelines for the Preparation of Closing Opinions*, and *Statement of Opinion Practices*. Six parts.

- **Assumptions.** Facts the opinion takes as given without verifying — genuineness of signatures, authenticity of documents, accuracy of what the client supplied. State them; the opinion stands on them.
- **Exceptions (qualifications).** The carve-outs from the opinion's coverage — the bankruptcy exception, the equitable-remedies exception, the matters expressly not addressed. An opinion is defined as much by what it excludes as by what it covers.
- **Knowledge qualifiers.** *"To our knowledge"* limits a statement to the actual knowledge of the lawyers involved after the diligence customary for that confirmation — not a guarantee of the fact, a representation about what the firm knows. The classic is the confirmation about pending legal proceedings.
- **Coverage & reliance.** The opinion runs to a named addressee, for a named transaction, and may be relied on by no one else. Reliance is a defined, limited grant — not an open invitation.
- **Customary practice.** Opinions are read against the customary practice of lawyers who regularly give and receive opinions of that type. Customary practice lets an opinion say a great deal in a few words, because a body of shared, unstated assumptions and limitations is understood to apply whether or not it is spelled out.
- **The golden rule.** Two faces. For the recipient: *do not request an opinion you would not be willing to give if you were in the opinion-giver's position.* For the giver: *never render an opinion you know or believe to be false or misleading* — even one that is technically correct, if it would mislead the recipient.

Two related instruments worth naming: the **reasoned opinion** (one that explains its analysis rather than stating a bare conclusion — the structuring memo is reasoned), and the **"would" / "should" opinion** (where genuine uncertainty bars a flat "will," the opinion is graded down to a reasoned "should" or "would," tied to the L2 ladder).

**The corpus's defensive perimeter IS this framework, not decoration.** The "Assumptions and Limitations" section is the TriBar assumptions; the "Things to Watch Out For" lists are exceptions; *"we have not independently verified"* is the assumption discipline; *"no reliance by any third party"* in the Limitations footer is the coverage-and-reliance limit; *"from experience, it is rare that…"* is a knowledge-grade confirmation. When you build the perimeter (Part II, S10), you are applying TriBar — so build it deliberately, not as boilerplate.

> The limits are the opinion. Draw them on purpose.

## L4. The hierarchy of authority — rank every source before you lean on it

Not all authority is equal. Before a source carries weight in the memo, classify it on two axes.

**Axis 1 — Primary vs. secondary.**
- **Primary** = the law itself: constitutions, statutes, regulations, judicial opinions. Only primary authority can bind.
- **Secondary** = sources that *explain* the law: treatises, law-review articles, restatements, practice guides. Never binding — persuasive at best.

**Axis 2 — Mandatory (binding) vs. persuasive.**
- **Mandatory** = a court *must* apply it: a higher court in the same jurisdiction, on point.
- **Persuasive** = carries weight but does not bind: other jurisdictions, lower courts, secondary sources, dicta, agency staff views.

**The court-weight ladder (U.S.), strongest first:**
1. **Statutes and regulations** outrank the case law interpreting them — the text governs; cases construe it. *(The Clarity Act and the Securities Act of 1933 sit above any opinion reading them.)*
2. **SCOTUS** > **Circuit** (en banc > panel) > **District**.
3. **Same jurisdiction** > other jurisdiction.
4. Within an opinion: **majority** > plurality > **concurrence** > **dictum** > **dissent**.
5. **On-point** > analogous; **later** controlling decision > earlier.

**Agency guidance is persuasive only — and revocable.** SEC no-action letters, interpretive letters, and official speeches are non-binding staff views; the agency can change position or withdraw the guidance outright. The corpus is explicit: *"The 'Hinman doctrine' comes from a 2018 speech by William Hinman, then Director of the SEC's Division of Corporation Finance."* That pedigree does two jobs at once — it lends the doctrine credibility *and* quietly marks it as a speech, not law. The same caution attaches to the CFTC's 2020 digital-asset actual-delivery interpretive guidance, which the Commission *withdrew* in December 2025 (L5): guidance you rely on this year may be gone the next. When you rely on agency guidance, name what it is so the reader knows its rank — and its fragility. The SEC's proposed safe harbor "championed by Commissioner Hester Peirce" is flagged the same way: a proposal, not a rule.

> Rank the authority before you cite it. A speech is not a statute; say which one you hold.

## L5. Marching the controlling test — find the test, walk it, grade the result

The engine of the opinion. For each issue: **identify the controlling multi-factor test → march it element-by-element against the facts → weigh → conclude at an L2 confidence level.** The case-law craft lives here too — five moves that make the march honest.

1. **Holding vs. dictum (ratio vs. obiter).** The *holding* is the rule necessary to the court's decision — it binds. *Dictum* is an aside the court did not need to decide — persuasive at most. Cite holdings as authority; if you rely on dictum, flag it as dictum. Misciting dictum as a holding is how a memo's authority collapses under scrutiny.
2. **Synthesize one rule from several cases.** Read the line of cases, extract the principle they share, and state it as a single rule — then cite the cases beneath it. The corpus does this when it moves from *Williamson* (partnerships) to "Courts have further applied this reasoning to Limited Liability Companies (LLCs)," synthesizing a control-concentration rule across both.
3. **Analogize.** Match your client's *material* facts to a precedent's material facts: same facts, same result. *"As argued in Uniswap's defense to the SEC, the operation of a front-end interface is distinct from the creation or control of the underlying protocol"* — the client's GUI operator is analogized to Uniswap's front end.
4. **Distinguish.** Show the precedent's material facts *differ*, so its rule does not control. The corpus distinguishes the client's removable, elected Curators from *Merchant Capital*, where "the manager was deemed irreplaceable… because funds were locked and only the manager could access the assets."
5. **Apply prong by prong.** When the test has elements, walk each one — and remember a single element can decide the question: *"To avoid classification as an investment contract, none of these three conditions can be present."* One present condition is enough to fail; one absent prong is enough to win.

**The law comes from the matter, not from this skill.** This is a memorandum-writing skill, not a law library. The controlling tests, statutes, and cases arrive with the engagement — the user supplies them under Mandatory Inputs, and the corpus supplies the worked exemplar. Do not write doctrine from memory: embedded law goes stale (agency guidance is withdrawn, statutes are amended, holdings are narrowed — see L4), and a memorandum that recites a lapsed rule fails worse than one that asks for the rule. If the controlling test for an issue has not been supplied, ask once, in the single combined message Mandatory Inputs prescribes — then march what you were given.

**Worked example (the corpus — *Howey* refined by *Williamson*):**
- *Rule* — "Courts often determine whether something is an investment contract by applying the *Howey* Test, which asks whether there is: 1) an investment of money, 2) in a common enterprise, 3) with an expectation of profit, 4) that comes primarily from the efforts of others."
- *Explanation* — "In *Williamson v. Tucker*, 645 F.2d 404 (5th Cir. 1981) *(Williamson)*, the court recognized that partnership and joint venture interests can qualify as investment contracts if at least one of [three] conditions applies… Courts have further applied this reasoning to Limited Liability Companies (LLCs)…"
- *Application* — march each *Williamson* condition against the client's DAO LLC units; distinguish *Merchant Capital*.
- *Conclusion* — "To avoid classification as an investment contract, none of these three conditions can be present" — graded at L2.

> Name the test, walk every element, then grade what you found.

## L6. Adverse-authority candor — state the case against the client, then answer it

An opinion that marshals only the favorable authority is advocacy wearing a letterhead. The reasoned opinion states the *strongest case against* the client's position — the contrary holding, the unfavorable factor, the regulator's stated view — and then rebuts or distinguishes it. This is both honest and protective: the client needs the real odds (the residual-risk step of L1), and the opinion that has already met the adverse case is the one that survives scrutiny.

Three duties:
1. **Surface the strongest adverse authority.** The on-point contrary case, the regulator's enforcement posture, the unsettled element. Do not bury it; do not omit it.
2. **Engage it.** Distinguish it on its material facts (L5), or concede its force and grade the conclusion *down* the ladder (L2) to match.
3. **Disclose it in the citation.** Adverse authority takes *contra* / *but see* / *but cf.* (L7) — never silence.

The corpus does this throughout: it raises *Merchant Capital* — the case where illusory rights defeated the structure — and then distinguishes the client's removable, elected Curators; it concedes the Clarity Act DeFi exclusion's scope is "not yet well-defined" rather than claiming it; it names the CFTC's retained "anti-fraud and anti-manipulation oversight" even while relying on the DeFi exclusion. Each is the adverse point, surfaced and answered.

> State the case against your client in its strongest form. An opinion that argues one side is advocacy in a borrowed suit.

## L7. Citation discipline — the atomic scaffold, the signal ladder, and when to cite

The demoted craft. Three tools that shape the *prose* once L1–L6 have decided the *substance*.

**1 — The atomic paragraph scaffold (IRAC and its cousins).** IRAC — Issue, Rule, Application, Conclusion — and its richer forms are the law-school teaching device for shaping a *single paragraph*. Useful at that scale; **not** the elite method — L1 is. Use IRAC to shape a paragraph; use the spine to build the opinion.

| Form | Expands to | What it adds |
|---|---|---|
| **IRAC** | Issue · Rule · Application · Conclusion | The base unit. State the rule, apply it, conclude. |
| **CREAC** | Conclusion · Rule · **Explanation** · Application · Conclusion | Leads with the conclusion; inserts an **Explanation** step — how prior cases applied the rule — between rule and application. |
| **TREAT** | Thesis · Rule · **Explanation** · Application · Thesis | A thesis *heading* frames the issue; the Explanation synthesizes the authorities (L5); the thesis is restated as the conclusion. |

The **Explanation step** is the upgrade plain IRAC lacks: *show how courts have actually used the rule in decided cases* before you apply it to the client. That is where precedent does its work — the difference between asserting a rule and proving one. For a settled one-issue point, plain IRAC is enough; for a contested point inside an L1 spine, lead with the conclusion and prove the rule through precedent before applying it.

**2 — The signal ladder (Bluebook).** The introductory signal in front of a citation tells the reader *how strongly* the source supports the point — before they read it. Using the wrong signal misstates your own authority.

| Signal | What it tells the reader | When to use |
|---|---|---|
| **[no signal]** | The authority **directly states** the proposition, or is the source of a quotation. | Strongest. The cited case says exactly this. |
| ***e.g.,*** | The authority states the proposition; so do many others, and citing them all would not help. | Well-supported point; cite one representative source. |
| ***accord*** | A second authority states the same thing; the text quotes or relies on only one. | After a [no signal] cite, to stack agreeing authority. |
| ***see*** | The authority **supports** the proposition, but an inferential step lies between the two. | Support that is clear but not word-for-word. |
| ***see also*** | Additional support, where authority is already cited with [no signal] or *see*. | Secondary support, after the primary cite. |
| ***cf.*** | **Analogous** authority — supports by comparison and requires an inferential leap. | The case is about something else but its logic carries. **Always add a parenthetical explaining why.** |
| ***compare … with …*** | A comparison of authorities that itself illustrates the proposition. | When the contrast makes the point. |
| ***contra*** | The authority **directly contradicts** the proposition (the negative of [no signal]). | Disclose authority that says the opposite outright. |
| ***but see*** | The authority contradicts, with an inferential step (the negative of *see*). | Disclose adverse authority that cuts against you indirectly. |
| ***but cf.*** | Analogous authority that cuts against the proposition (the negative of *cf.*). | Adverse-by-analogy; add a parenthetical. |
| ***see generally*** | **Background** material — useful to the topic, not to the specific point. | Treatises, overviews, context. |

**Order and punctuation.** Signals appear in citation order: supportive (`[no signal], e.g., accord, see, see also`) → comparative (`cf., compare`) → contradictory (`contra, but see, but cf.`) → background (`see generally`). Within one category, string authorities with **semicolons**; across categories, start a **new citation sentence**. Use **pincites** whenever you cite a specific passage. Short forms: ***id.*** for the immediately preceding authority, ***supra*** for an earlier-cited non-case source.

**The register caveat.** Litigation briefs and law-review writing use the full ladder strictly. **Transactional opinions cite more loosely** — they fold the case into the sentence (*"In *Merchant Capital*, investor rights were undermined by…"*), which is itself a `[no signal]` move: the case *is* the proposition. **Match the corpus**, which rarely uses formal signals in running prose. When you do add a signal, grade it honestly: a `see` dressed up as `[no signal]` overclaims; a `cf.` left bare leaves the reader to guess the link.

**3 — When to cite, and when not to.** Three rules.
1. **Every statement of law presumptively needs authority.** A rule statement, a definition of a legal test, a proposition about what a statute requires — each carries at least one citation. State the *Howey* test, cite *Howey*.
2. **Your own application of law to the client's facts gets NO citation.** When you reason — *"because the Curators are removable by DAO action, the third *Williamson* condition is absent"* — that is *your* analysis, not someone else's proposition. The rule is cited; the application is argued.
3. **Background and well-settled propositions are cited sparingly, if at all.** String-citing the obvious makes a settled point look contested. One on-point authority beats five. **Never string-cite for rhythm** — citations are load-bearing, not decorative.

> Cite the rule. Argue the application. Never blur the line — it is the line that makes the memo honest.

---

# Part II — The Style Fingerprint

Ten dimensions, each measured against the corpus. These are the constraints on how the memo *reads*. Hold every one. They sit on top of Part I — the law decides *what* the sentence says; these axes decide *how* it says it.

## S1. Person and voice — dual register: we↔you in the frame, impersonal in the doctrine

This is the axis that most distinguishes this voice from a whitepaper. The voice has **two registers** and switches between them by section.

**The advisory frame uses first-person-plural firm and second-person client.** The opening, the assumptions, the summary answer, the structure proposal, and the steps address the client directly.

> "You have requested that we provide you with a structuring proposal on how you can operationalize IndexMaker in a regulatory risk-mitigated manner."
> "Our analysis is limited to general informational purposes only and does not constitute, and should not be construed as, legal advice in any jurisdiction…"
> "Based on your objectives, we propose the following structure, as illustrated in the diagram above, to operate your business."

The firm is *we*. The client is *you* (in the frame) or *the client* (in the assumptions: "provided to us by the client and its affiliates"). Never *I*. The firm acts as one institution.

**The doctrinal body drops to impersonal third person.** Inside the legal rationale (§5 onward), the actors are the law, the courts, the regulators, and the entities. No *we*, no *you*.

> "Under U.S. law, a security is an investment that falls within a regulated category."
> "Courts often determine whether something is an investment contract by applying the Howey Test…"
> "The CFTC is given exclusive regulatory jurisdiction over the cash or spot markets for digital commodities."

Entities act as subjects in their own right: *"The IndexMaker Protocol is a decentralized infrastructure…"*, *"The Marshall Islands DAO LLC offers legal recognition and liability protection…"*. The rule of thumb: **advise in we↔you, expound the law in the third person.** The register shift also tracks L1 — the advisory frame is the opinion-letter stance; the doctrine reads like a predictive memo.

## S2. Tense — present for the law, future for the proposal, modal for the risk

Three tenses, each with a job.

**Present** states standing legal fact.
> "A 'digital commodity' is defined as a digital asset that is not a security…"
> "MIDAO are the Marshall Islands' official registry and service provider for DAO LLCs."

**Future ("will")** describes the proposed structure and the step plan — the state the client will build.
> "the Index Tokens will be issued in consideration for stablecoins…"
> "This entity will be incorporated as a wholly owned subsidiary of IndexMaker Labs…"
> "The DAO LLC will enter into a software support agreement with IndexMaker Labs."

**Modal ("may / could / would / should")** carries every legal conclusion and every recommendation. The voice almost never asserts a flat outcome about the law; it states a probability — and each modal is a rung on the confidence ladder (see **L2**).
> "it may qualify under the exclusion for DeFi activities."
> "a token may qualify as a digital commodity once its underlying blockchain is considered a mature blockchain system."
> "It would be prudent to conduct a subsequent assessment…"
> "DAO members without relevant skills should receive training, delegate to opt-in agents, or be excluded if entirely passive."

Strip the modality and the voice collapses into overconfidence. The hedge *is* the register — and it is calibrated, not vague (see L2).

## S3. Sentence length — long legal periods, multi-clause, qualified

Mean sentence length runs ~28–35 words. Legal periods of 40 to 70 words are common and correct. The voice does not fear a long sentence; it controls it with subordination and serial commas.

> "Crypto-related activities remain a high-risk area subject to evolving and uncertain regulation; while we have endeavoured to provide a rigorous review, no analysis can eliminate the possibility that regulatory authorities may exercise their broad discretionary powers to investigate, challenge, or pursue enforcement action, potentially leading to significant cost, delay, or other adverse outcomes, even where the ultimate resolution may be favorable." *(~65 words, one sentence)*

Short sentences are rare and serve as topic openers that announce a new doctrine before it is developed.

> "A similar framework applies to digital tokens." *(7 words — the opener)*

Do not caricature the voice into telegraph-speak, and do not let a long sentence sprawl past its clauses. When a period passes seventy words or three subordinate clauses, split it at the semicolon.

## S4. Syntax — subordination, conditional fronting, qualifying tails

The default sentence opens on a subordinate or conditional clause, then delivers the main clause, then qualifies it.

**Conditional and purpose fronting** is the signature opener.
> "If a decentralized finance (DeFi) platform is purely a technology provider, does not allow custody of user assets, and allows users to transact in a self-directed manner without your implication, it may qualify under the exclusion for DeFi activities."
> "To avoid classification as an investment contract, none of these three conditions can be present."
> "Under the Clarity Act, a token may qualify as a digital commodity once its underlying blockchain is considered a mature blockchain system."
> "Although the Marshall Islands regime is flexible, there are still mandatory compliance points."

**Qualifying tails** hang a condition or carve-out off the end of the main clause.
> "…provided they meet disclosure and anti-fraud requirements."
> "…even where the ultimate resolution may be favorable."
> "…subject to slashing by fellow members in the event of misconduct or breach of duties."
> "…excluding capital gains and dividends."

**Passive voice is permitted and frequent** in doctrinal exposition, where the actor is the law itself.
> "The CFTC is given exclusive regulatory jurisdiction…"
> "Beneficial ownership reporting is required for anyone with 25% or more governance rights."
> "All voting is weighted by USDC deposits…"

Active voice returns for the firm's recommendations: *"we propose"*, *"we recommend"*, *"Incorporate the Marshall Islands DAO LLC"*.

## S5. Diction — legal-regulatory exact, defined terms, named authority, hedging modality

Reach for the exact legal, regulatory, or corporate term. *Investment contract. Progressive decentralization. Beneficial ownership. Segregated. Wholly owned subsidiary. Self-directed. Anti-manipulation. Non-custodial. Manipulation-robust.*

**Defined terms are set in bold inside quotation marks on first use, then used bare.** This is the legal drafting convention and a load-bearing tell of the voice.
> "represented by ERC-20 index tokens ('**Index Tokens**')"
> "Authorized Participants ('**APs**')"
> "The Clarity for Digital Tokens Act (the '**Clarity Act**')"
> "A '**digital commodity**' is defined as…"

**Acronyms are parenthesized on first use, then bare.** Know Your Customer (KYC), Anti-Money Laundering (AML), verifiable randomness (VRF), Virtual Asset Service Providers (VASP), Commodity Futures Trading Commission's (CFTC).

**Case citations follow the convention exactly** (see **L7** for the full citation discipline): italic case name, reporter cite, court and year in parentheses, italic short form in parentheses.
> "*Williamson v. Tucker*, 645 F.2d 404 (5th Cir. 1981) *(Williamson)*"
> "*SEC v. Merchant Capital*, LLC, 483 F.3d 747 (2007) *(Merchant Capital)*"
> "the *Howey* Test"

**Statutes and academic sources are italic.** *Securities Act of 1933*, *Decentralized Autonomous Organization Act* (2022), the footnoted *Goldilocks sortition* paper in full academic format with its arXiv URL.

**Doctrines are named with their source and pedigree** — and the pedigree marks their rank in the authority hierarchy (see **L4**).
> "The 'Hinman doctrine' comes from a 2018 speech by William Hinman, then Director of the SEC's Division of Corporation Finance."
> "the SEC's proposed decentralized safe harbor, championed by Commissioner Hester Peirce…"

**The hedging vocabulary is the heart of the diction. Lean on it** — and grade it (see **L2**). *may, could, would, should, it would be prudent, from experience, it is rare that, remain subject to significant regulatory interpretation, it is customary to, no analysis can eliminate the possibility, potentially.* And the risk-frame set: *regulatory friction, mitigating … risk, reduces regulatory exposure, the securities law risk decreases, high-risk area.*

**There is no hype.** No *seamless, revolutionary, cutting-edge, robust* in the marketing sense. *Robust* appears once, as a category word ("embedding robust, skills-based sortition"), not as praise. Adjectives are legal categories or measurable facts, never decoration.

**A vivid noun is allowed when it is the exact noun.** The voice reaches for a colorful operational or threat term where it is precise, not where it is flourish: *"guarded mainnet deployment"*, *"commandeered through DAO corporate raider tactics or other hostile methods of seizing control"*. The test is exactness, not color.

**Keep the corpus's mixed orthography.** The corpus uses a British–American blend: *endeavoured* (BrE) sits beside *favorable, recognize, decentralization* (AmE). Do not normalize to one variant; the mix is part of the fingerprint.

## S6. Punctuation — the full legal kit

This is the axis where this voice is the **exact inverse of the whitepaper voice.** Where that voice bans the em-dash, the semicolon, and the aside, this voice uses all three as standard equipment.

- **Semicolon.** Permitted, and used to join two independent clauses or to chain the items of a complex enumerated list. *"…subject to evolving and uncertain regulation; while we have endeavoured to provide a rigorous review, no analysis can eliminate…"* The semicolon joins the clauses; the comma carries the carve-out. It is part of the legal period.
- **Em-dash.** Permitted, for an embedded clarification. *"The key benefit is that each Series is insulated from the liabilities of the others — if one index underperforms or incurs liabilities, this does not affect the others."*
- **En-dash** in compound proper nouns: *Master–Series LLC*.
- **Parentheses.** Used freely — for acronym definitions, for examples, for asides, and for citations. *"(e.g., AMMs, lending, staking)"*, *"(random selection from an eligible pool)"*, *"(1 USDC = 1 vote, not index-specific)"*, *"(5th Cir. 1981)"*.
- **"e.g." and "i.e."** appear inside parentheses as standard.
- **Quotation marks** carry defined terms on first use and quoted statutory or regulatory language. *""without reliance on any other person to maintain control of the digital assets of the user during any part of the financial transaction""*.
- **Colon.** Introduces an enumerated list. *"the Howey Test, which asks whether there is:"* then the numbered prongs.
- **Two list numerals, two jobs.** Statutory or test elements take paren-numerals — *"1) an investment of money, 2) in a common enterprise, 3) with an expectation of profit, 4) that comes primarily from the efforts of others"* — lowercase, comma- or semicolon-chained, with *"; and"* before the last. Advisory and structural lists take period-numerals with bold labels — *"1. **Real Governance Power.** …"*. Do not mix the two.

The fastest way to break this voice is to write it clean and terse like a whitepaper. The legal period, with its semicolons and parenthetical carve-outs, *is* the register.

## S7. The signature device — the numbered run-in bold label

The recurring structural unit inside a section: a **bold label ending in a period**, then an explanation that states a rule, often cites a case, and lands a recommendation or caution. Unlike the whitepaper version, the labels here are **numbered**, the label is often a full phrase, and the body advises rather than illustrates.

> "1. **Real Governance Power.** Voting rights must have practical effect, not just symbolic value. DAO proposals should provide enough detail for informed decisions and avoid defaults or mechanisms that favor insiders."
> "5. **Avoiding Illusory Rights**. In *Merchant Capital*, investor rights were undermined by tactics like pre-filled ballots, default votes for management, and a lack of mechanisms to act on outcomes. Do not use systems that only *appear* decentralized while keeping control with insiders. Use neutral rules and remove unnecessary friction to participation."
> "1. **Master–Series LLC Structure.** The Marshall Islands Master–Series LLC will serve as the umbrella organization for the DAO. In a Master–Series LLC, the 'Master' is a single legal entity that can establish multiple 'Series' within it, each with its own assets, liabilities, and business purpose."

The label is one to six words. The body states the rule flat, frequently anchors it on a named case (the Explanation step of L7, the analogize/distinguish moves of L5), and closes on an instruction (*"Do not use…"*, *"should receive training…"*). The worked detail is a legal application, not a geography-and-tenor scenario.

**The section scaffold.** A decomposed section opens with one framing sentence that names the whole and ends in a colon, then lists the parts as numbered bold labels.

> "To reduce the risk of security classification, consider the following:"
> "This structure has four important aspects worth highlighting:"

## S8. Rhetoric — the reasoned spine, define by negation for the safe harbor, name the authority

Four moves recur. They are the surface form of the Part I craft (**L1, L5, L7**).

**Rule, authority, application, risk** (the reasoning spine of **L1**, paragraph-scaffolded per **L7**). State the governing rule, cite the case or statute, apply it to the client's facts, then name the residual risk.
> "A similar framework applies to digital tokens. The Howey test governs whether a token is an 'investment contract' and thus a security. Under Howey, the analysis turns on whether purchasers are relying on the efforts of others for the token's value."

**Define by negation — the safe harbor.** The thing is defined as often by what it is *not* as by what it is, because the negative is where the legal protection lives.
> "A 'digital commodity' is defined as a digital asset that is not a security…"
> "does not allow custody of user assets…"
> "issuing and redeeming governance tokens is not considered a profit-making activity and therefore does not jeopardize non-profit status."
> "the Issuer Network in IndexMaker does not assume trading or inventory exposure."

**Name the authority, then its pedigree** (the hierarchy move of **L4**). Real cases, real statutes, real regulators, real people with their titles.
> "the 'Hinman doctrine' comes from a 2018 speech by William Hinman, then Director of the SEC's Division of Corporation Finance."
> "MIDAO, a public-private partner and the sole registered agent, streamlines this process…"
> "As argued in Uniswap's defense to the SEC, the operation of a front-end interface is distinct from the creation or control of the underlying protocol."

**Risk-mitigated, never risk-free** (the confidence discipline of **L2**). Every benefit is stated as a reduction of probability, and every section that grants comfort is paired with a caveat that withdraws part of it.
> "mitigating U.S. securities law risk via progressive decentralization…"
> "the securities law risk decreases."
> "While the DeFi exclusion removes many obligations, it is important to note that the protocol will still fall under the Commodity Futures Trading Commission's (CFTC) anti-fraud and anti-manipulation oversight."

## S9. Paragraph architecture — rule developed, closed on a qualification

Paragraphs run three to six sentences. Each opens on a rule or claim, develops it with authority or mechanism, and — unlike the whitepaper's flat judgment — closes on a **qualification, a caveat, or a residual risk.**

> "It would be prudent to conduct a subsequent assessment to determine whether the IndexMaker Protocol could qualify for a DeFi Activities exclusion under the Clarity Act. Such an assessment should be undertaken once the final implementing regulations and interpretive guidance are available… At present, however, making such a determination is challenging, as the scope and application of the DeFi Activities exclusion are not yet well-defined within the Act and remain subject to significant regulatory interpretation."

The closer — *"remain subject to significant regulatory interpretation"* — does not resolve. It withholds. The paragraph ends with the door held open, not shut, because the honest legal answer is conditional (this is **L2** "not free from doubt" in paragraph form).

The connective tissue the whitepaper voice forbids, this voice **requires**: *however, while, although, similarly, in addition, from this perspective, importantly, specifically, unlike traditional finance.* These transitions carry the logical flow of the argument. The workhorse openers are the authority-fronting *"Under [law/test]…"* (*Under U.S. law, Under the Clarity Act, Under Howey*) and the court-fronting *"Courts [verb]…"* (*Courts often determine, Courts have further applied, Courts focus on*). Open the doctrinal sentence on the authority, then state what it does.

## S10. Structural tics — decimal numbering, enumerated completeness, the defensive perimeter

**Decimal section numbering.** Sections are numbered 1–8 with bold-underlined headings; subsections are 5.1, 5.2; sub-subsections are 5.1.1 with italic titles. The hierarchy is visible and legal.

**Enumerate for completeness, not for rhythm.** Where the whitepaper voice groups into threes, this voice lists *however many factors the law supplies*: the four *Howey* prongs, the three *Williamson* conditions, the ten-point "Things to Watch Out For," the nine Steps, the seven governance roles, the four-phase roadmap. The organizing instinct is exhaustiveness — name every factor a court would weigh (this is the prong-by-prong discipline of **L5** and the citation rule of **L7**).

**The defensive perimeter.** Disclaimers bracket the whole document (the opinion-letter register of **L1**, applied as the TriBar assumptions-and-qualifications discipline of **L3**). An "Assumptions and Limitations" section sits near the front; a "Things to Watch Out For" subsection closes each jurisdiction; a "LIMITATIONS OF THIS MEMORANDUM" footer closes the document in smaller, centered text. The memo repeatedly disclaims independent verification, reliance by third parties, scope, and jurisdictional competence.

**Bottom line up front.** A "Summary Answer" section states the recommended structure in one dense paragraph *before* the rationale that justifies it (the Brief-Answer-up-front move of the spine, **L1**). The reader gets the answer, then the reasoning.

**The hedged recommendation tail.** A recurring closing move names what must happen before the conclusion firms up: *"once the final implementing regulations and interpretive guidance are available", "after the protocol's operational parameters … are more fully developed", "Such an assessment should be undertaken once…".* This is a conclusion held at **not free from doubt** until a condition resolves it (**L2**).

**Named third-party entities and precedent deals.** The structure is grounded in real registrars, custodians, and exchanges (MIDAO, Bitget, Ceffu, Binance, Cayman Foundation) and in real precedent postures (the Uniswap defense, the Hinman speech, the Peirce safe harbor). The client's own corporate parent is named too — the controlled entities are *Symetio* entities, distinct from the protocol developer (IndexMaker Labs).

**Sortition as the non-security argument.** The memo's signature substantive move: random selection of role-holders is offered as legal proof that managerial positions are interchangeable, defeating the *Howey* "efforts of others" prong. *"By assigning roles through chance, sortition demonstrates that managerial positions are interchangeable and not unique."* The mechanism is named with its academic source (the footnoted *Goldilocks sortition* paper — secondary authority, persuasive only, see L4) and its hedge (*"effective only if the selected participants are qualified"*). When the structure turns on a novel argument, anchor it on a citation and pair it with its condition.

**Economic stake as governance weight.** Voting power is tied to capital, stated flat with a parenthetical gloss: *"with voting weighted by USDC deposits (1 USDC = 1 vote, not index-specific)"*, *"All voting is weighted by USDC deposits, ensuring governance participation aligns with economic stake."*

---

# Part III — The Replication Checklist

This is the general method for copying *any* author's style, with this corpus's value filled in for each axis. Run a target text through these twelve axes to build a fingerprint; the right column is the calibration for this skill. (Drawn from stylometry: lexical, syntactic, punctuation, and burstiness features.)

| # | Axis | What to measure | Calibrated value |
|---|---|---|---|
| 1 | **Person** | 1st / 2nd / 3rd person; presence of author and reader | Dual. *We* (firm) ↔ *you* (client) in the frame; impersonal third in the doctrine. Never *I*. |
| 2 | **Tense** | Dominant tense; where it shifts | Present for law, future (*will*) for the proposed structure and steps, modal (*may/could/would/should*) for every conclusion (each modal = an L2 confidence level). |
| 3 | **Mean sentence length** | Average words per sentence | ~28–35 words; legal periods of 40–70 are common. |
| 4 | **Burstiness** | Variance in sentence length; short-beside-long rhythm | Low. Few short sentences; an occasional 7-word topic opener. |
| 5 | **Clause depth** | Clauses per sentence; subordination | Deep. Conditional fronting + qualifying tails. Three to five clauses common. |
| 6 | **Voice** | Active vs passive ratio | Mixed. Passive for doctrinal exposition; active for the firm's recommendations. |
| 7 | **Diction register** | Plain / technical / legal / conversational; intensifier density | Legal-regulatory exact, hedging-heavy. Near-zero intensifiers. |
| 8 | **Figurative load** | Metaphor, simile, rhetorical question, hyperbole | Near zero. The one device is analogy to precedent (Uniswap, named cases — see L5). |
| 9 | **Punctuation profile** | Em-dash, semicolon, colon, parenthesis frequency | The full kit. Semicolons, em-dashes, parenthetical asides, e.g./i.e., quoted statutory language — all standard. |
| 10 | **Signature constructions** | Repeated structural units (n-grams, run-in labels) | Numbered **bold label.** + rule + case cite + caution. Defined-term-in-bold-quotes. "Things to Watch Out For" lists. |
| 11 | **Rhetorical moves** | Recurring argument shapes | The reasoned-opinion spine — Question → graded Brief Answer → framework → element-by-element application → residual risk (L1); define-by-negation for the safe harbor; name authority + pedigree (L4); adverse-authority candor (L6); risk-mitigated-not-risk-free (L2). |
| 12 | **Document skeleton** | Section scheme, titles, openers/closers | Law-firm letter: header block → RE → Dear → numbered §§ → Limitations footer. Decimal subsections. |

To copy a style you have not seen, fill this table from the corpus first, then write to the table. Here the table is already filled — write to the right column.

---

# Part IV — The Process

```
1 GATHER FACTS + RANK AUTHORITY → 2 BUILD THE SKELETON → 3 DRAFT ON THE SPINE → 4 CITATION-DISCIPLINE PASS → 5 APPLY THE FINGERPRINT → 6 BUILD THE TriBar PERIMETER
```

## Step 1 — Gather the facts and the authority, and rank both

Collect what the memorandum asserts: the structure, the client objectives, the jurisdictions, the governing tests, the named entities. Then do the lawyer's work that Part I demands:

- **Mark every legal proposition with the case or statute that supports it** (L7). Mark every gap. Never write a legal conclusion with no authority under it — ask once, then proceed.
- **Classify each authority by the hierarchy** (L4): primary or secondary; binding or persuasive; statute, holding, dictum, or agency guidance. A no-action letter or a speech is persuasive only — and revocable — so note it.
- **Pick the controlling test for each issue** (L5): the test the matter supplies — the corpus's are *Howey* and *Williamson*. Identify it before you draft; if the matter has not supplied one, it goes in the single combined question.
- **Assign each conclusion a target confidence level** (L2): will / should / more likely than not / substantial authority / reasonable basis / not free from doubt. Decide the level *before* you draft, so the modal you reach for is the right one.
- **Pick the register** (L1): structuring/opinion letter by default. Confirm if the user wants a brief or a neutral office memo instead.

Never invent a citation.

## Step 2 — Build the skeleton

Lay out the numbered sections before any prose (see Output Format for the default set). Give each a bold-underlined heading; give the jurisdiction analyses decimal subsections with italic titles. Inside each, list the numbered bold labels it will carry. The skeleton is the contract; the prose only fills it.

## Step 3 — Draft on the spine

Build each section on the L1 spine: Question Presented, graded Brief Answer, controlling framework, element-by-element application, residual risk. March the controlling test prong by prong (L5) — synthesize, analogize, distinguish. Shape individual paragraphs with the IRAC scaffold (L7): for a contested point, lead with the conclusion, then **prove the rule through precedent** (the Explanation step) before applying it. **State the strongest adverse authority and answer it** (L6) — distinguish it, or grade the conclusion down the ladder to match. State the rule in the present tense; cite the case in the convention. Get the law right before the voice.

## Step 4 — Citation-discipline pass

Before styling, audit the citations against Part I:
- **Every statement of law carries authority; no application-to-facts sentence carries a citation** (L7). Strip citations from your own reasoning; add them to any bare rule statement.
- **Each signal matches the strength of support** (L7): `[no signal]` only where the source states the point; `see` where there is an inferential step; `cf.` with a parenthetical for analogy; `but see` / `contra` for adverse authority you are disclosing.
- **No string-citing for rhythm.** One on-point authority per proposition.
- **Every citation is real and correctly ranked** (L4). If you could not verify it, it is not in the document.

## Step 5 — Apply the fingerprint

Pass over the draft with Part II in hand:
- Set the frame in we↔you and the doctrine in the third person (S1).
- Put the law in the present, the proposed structure in the future, every conclusion in the modal that matches its confidence level (S2 + L2).
- Open sentences on conditional or purpose clauses; hang carve-outs off the end (S4).
- Bold-and-quote each defined term on first use; cite every case in the convention (S5).
- Restore the semicolons, em-dashes, and parenthetical carve-outs the draft may have stripped (S6).
- Convert flat itemizations into numbered **bold label.** + rule + caution (S7).
- Add a define-by-negation sentence wherever the safe harbor lives in the negative (S8).
- Close each doctrinal paragraph on a qualification, not a flat judgment (S9).

## Step 6 — Build the TriBar perimeter

The memo is not finished until it is bracketed by the assumptions-and-qualifications discipline of opinion practice (L3, S10):
- An "Assumptions and Limitations" section near the front — the TriBar assumptions, disclaiming independent verification and limiting reliance to the addressee.
- A "Things to Watch Out For" subsection closing each jurisdiction — the exceptions/qualifications.
- Knowledge qualifiers ("to our knowledge", "from experience") where a statement rests on what the firm knows rather than what it has verified.
- A "LIMITATIONS OF THIS MEMORANDUM" footer closing the document — the coverage-and-reliance limit.
- A check that no conclusion is stated as risk-free, that every conclusion carries a confidence level, and that the strongest adverse authority has been surfaced and answered. Every comfort is paired with its caveat.

If a sentence promises certainty, rewrite it until it states a probability.

---

# Methodology — how to actually produce the memorandum

1. **Pick the register first (L1).** Structuring/opinion letter by default — advisory stance, risk-mitigation framing, heavy disclaimers. Confirm before drafting if the user might want a brief or a neutral office memo.
2. **Rank every authority before you rely on it (L4).** Primary vs. secondary, binding vs. persuasive, statute vs. case vs. agency guidance. Name the pedigree of anything persuasive-only (speeches, no-action letters, proposals), and remember agency guidance can be withdrawn.
3. **Pick the controlling test for each issue (L5).** The test comes from the matter's supplied authority — never from memory. March it element-by-element against the facts; synthesize, analogize, distinguish.
4. **Build each section on the reasoned spine (L1).** Question Presented → graded Brief Answer → controlling framework → element-by-element application → residual risk → assumptions. The Summary Answer is the spine's Brief Answer for the whole document, up front.
5. **Grade every conclusion (L2).** Assign will / should / more likely than not / substantial authority / reasonable basis / not free from doubt — then write the matching modal (S2). Never print a bare percentage; never state a conclusion risk-free.
6. **Run the adverse-authority pass (L6).** State the strongest case against the client and answer it — distinguish it or grade the conclusion down. An opinion that argues one side is advocacy, not an opinion.
7. **Cite by the discipline, not by reflex (L7).** Authority under every rule statement; nothing under your own application-to-facts; no string-citing for rhythm; the signal matched to the actual support, parentheticals on every analogy.
8. **Lay the bottom line up front (S10).** A Summary Answer before the rationale.
9. **Enumerate for completeness (S10, L5).** Name every factor a court would weigh — not a tidy three. Walk multi-prong tests prong by prong.
10. **Apply the style fingerprint (Part II, S1–S10).** Dual register, the full punctuation kit, defined-terms-in-bold-quotes, numbered bold labels, define-by-negation, qualification-closed paragraphs.
11. **Build the TriBar perimeter (L3, S10).** Assumptions near the front, "Things to Watch Out For" per jurisdiction, knowledge qualifiers where they belong, a Limitations footer at the end.

---

# Output Format — the document

Produce a complete memorandum. The default skeleton is the corpus section set; adapt the section list to the matter, but keep the shape.

### Header block
```
[FIRM NAME] [LLP]                                    [letterhead: address, phone, fax, email, web]

BY [DELIVERY METHOD]                                 [Month Day, Year]
PRIVILEGED AND CONFIDENTIAL

To:           [RECIPIENT NAME]
Attention:    [contact]
[channel]:    [handle]

RE:     [Matter] Structuring Proposal

Dear [Name],
```
Conventions: the delivery method and the contact channel are the same medium (*BY TELEGRAM* ↔ *Telegram: @handle*). *"To:"* is the named principal in capitals; *"Attention:"* names a different day-to-day contact. The date sits top-right. A running letterhead repeats on every page, and a centered page number closes each page in the form *"- N -"*. The firm name and letterhead are placeholders — fill them from the user's inputs, never invent a firm.

The opening sentence states the engagement: *"You have requested that we provide you with a structuring proposal on how you can operationalize [X] in a regulatory risk-mitigated manner."*

### 1. Project Overview
What the structure is, in the present tense, with defined terms bolded-and-quoted on first use. The architecture in one paragraph: the entities, the roles, the custody arrangement.

### 2. Client Objectives
The client's goals, stated in the third person, then an enumerated list of key objectives. *"The client aims to launch more than 1,000 index tokens under a legally lean, modular, and decentralized structure…"* The enumerated list often closes on a longer, full-sentence final item that widens the scope while the earlier items stay fragmentary — the same fragment-then-full-sentence drift recurs in the *Williamson* conditions.

### 3. Assumptions and Limitations
The first disclaimer — and the front edge of the TriBar perimeter (L3). The firm has not independently verified the facts; the analysis is general informational only and not legal advice; the area is high-risk and the regulator retains discretion. One dense, hedged paragraph.

### 4. Summary Answer
The bottom line up front (the Brief-Answer-up-front move of the spine, L1). One dense paragraph naming the recommended structure, the jurisdictions, and what each entity does — *before* the rationale, carrying its confidence level (L2). *"This proposal outlines a legally lean, modular structure for launching up to [N] … mitigating [risk] via [mechanism]. The recommended model uses [entity] for [function], [entity] for [function]…"*

### 5. The Legal Rationale
The doctrine, organized **by jurisdiction** (5.1 United States, 5.2 [Jurisdiction]). Inside each jurisdiction, decimal sub-subsections with italic titles analyze each issue. The corpus US set runs six: 5.1.1 *LLC Units as Securities*, 5.1.2 *Tokens as Securities*, 5.1.3 *Looking Ahead*, 5.1.4 *Clarity Act Decentralized Finance (DeFi) Activities Exclusion*, 5.1.5 *Digital Commodities*, 5.1.6 *Things to Watch Out For*; the Marshall Islands set runs two: 5.2.1 *Key Benefits*, 5.2.2 *Things to Watch Out For*. Each issue is built on the L1 spine — Question, graded Brief Answer, controlling test, element-by-element application, residual risk — and graded to a confidence level (L2). Each jurisdiction closes on a "Things to Watch Out For" list of numbered bold labels. A covered jurisdiction need not get its own subsection — Panama carries no §5.3; its analysis is folded into the §6 structure rationale. State that asymmetry rather than padding an empty section.

### 6. Overall Structure Diagram
**6.1 Description** — the structure, with the diagram referenced and "four important aspects worth highlighting" as numbered bold labels. **6.2 Steps** — a numbered, future-tense ("will") implementation plan, each step a bold label naming the action (*"Formation of [Entity]." "Execution of [Agreement] between X and Y."*). The memo carries **two figures**, each a boxed, all-caps-titled diagram with a color legend: the entity/structure map here in §6, and a governance-flow map in §7. Describe the diagram in text if it cannot be rendered: a boxed entity map titled in all caps, a legend keyed by color to the real four categories — *controlled entities already incorporated*, *entities to be incorporated*, *third-party entities*, *unincorporated protocol* — line-style keys (solid = *commercial contract*, dashed = *governs*), and arrows labeled by relationship (*100% Owner, Software Support Agreement, OTC trading & Custodian Agreement, Front-End Gateway to Protocol, License Agreement*).

### 7. [Governance / Operating] Structure
**7.1 Description** — how the structure runs, with the governance-flow diagram (the second figure) referenced. **Step-by-Step [Process] & Roles** — numbered bold labels, one per role or stage. **Progressive [Decentralization] Roadmap** — the phased plan, numbered, each phase a bold label. The corpus roadmap is four phases, named exactly: *"Guided Operations." "Hybrid Elections." "Full Sortition Governance and Issuer Network Elections." "Mature Autonomy."* Academic sources cited in this section are footnoted (see Footnotes below).

### Footnotes
Academic or external sources are cited with a superscript numeral in the body and a footnote at the page bottom, in academic form: *Surname, I., & Surname, I. (Year). Title in italics. Source. URL.* — e.g. *Baharav, T., & Flanigan, B. (2024). Goldilocks sortition: A just-right way to select participants. arXiv. https://arxiv.org/abs/2406.15009* (author surnames bold, title italic, bare URL). These are secondary authority — persuasive only (L4).

### 8. Conclusions
One paragraph. State what the structure achieves, restate the risk-management framing, and close on the conditional path forward. *"The proposed structure positions [X] to operate as [Y] with [benefits]. By combining [A] with [B], the framework balances regulatory risk management with operational scalability."*

### Limitations footer
The footer stands alone on the final page, the text smaller and centered, the space above it left blank. Titled "LIMITATIONS OF THIS MEMORANDUM." Two short paragraphs — the coverage-and-reliance limit of the TriBar perimeter (L3): scope determined in consultation with the addressee, no reliance by any third party, not prepared by lawyers qualified in the relevant jurisdictions, no representation or warranty, no duty to update, no reproduction without consent.

---

# Strict Rules

- **Memorandum only.** If asked for a tweet, page, whitepaper, or email in this voice, decline the format and offer the memo.
- **Never fabricate a citation, a holding, a docket number, a statute, a test, or a named entity.** Missing authority is asked for once, then omitted with the gap stated. An invented case citation fails the whole document and is malpractice on paper.
- **Build each issue on the reasoned spine (L1).** Question Presented → graded Brief Answer → controlling framework → element-by-element application → residual risk → assumptions. The Summary Answer carries the spine up front for the whole memo.
- **Rank every authority before relying on it (L4).** Distinguish primary from secondary, binding from persuasive, and flag agency guidance (no-action letters, speeches, proposals) as persuasive only and revocable.
- **March the controlling test element-by-element (L5).** Identify the right test from the supplied authority, then walk every prong. One present condition can fail the position; one absent prong can win it.
- **State the strongest adverse authority and answer it (L6).** Distinguish it or grade the conclusion down. An opinion that argues one side only is advocacy, not an opinion.
- **Cite by the discipline, not by reflex (L7).** Every statement of law carries authority; your own application of law to the client's facts never does. No string-citing for rhythm. Use the signal that matches the support: `[no signal]` only where the source states the point; `see` for an inferential step; `cf.`/`but cf.` with a parenthetical; `contra`/`but see` to disclose adverse authority.
- **Every legal conclusion is a modal graded to a confidence level (L2).** *May, could, would, should* — never a flat "is safe" or "is not a security" without the hedge or the cited test. Never print a bare percentage.
- **Every comfort is paired with its caveat.** No section grants protection without naming the residual risk. Risk-mitigated, never risk-free.
- **The TriBar perimeter is mandatory (L3).** Assumptions and Limitations near the front, "Things to Watch Out For" per jurisdiction, knowledge qualifiers where statements rest on knowledge, a Limitations footer (coverage and reliance) at the end.
- **Defined terms are bolded inside quotes on first use, then bare.** Cases are cited in the convention: italic name, reporter, court and year, italic short form.
- **The frame is we↔you; the doctrine is impersonal third person.** Never *I*.
- **The full punctuation kit is in use.** Semicolons, em-dashes, and parenthetical asides are correct here — this is the inverse of the whitepaper voice.
- **Enumerate for completeness.** Name every factor a court would weigh, not a tidy three.
- **The bottom line goes up front.** A Summary Answer precedes the rationale.

# Quality Checks Before Finishing

- Did you write it as a privileged-and-confidential law-firm letter, with a header block, RE line, and "Dear [Name]"?
- Is the frame in we↔you and the doctrine in impersonal third person, with no *I* anywhere?
- Is the register correct for the ask (structuring/opinion letter by default — L1)?
- Is each issue built on the reasoned spine — Question, graded Brief Answer, controlling framework, element-by-element application, residual risk, assumptions (L1)?
- Did you identify the controlling test for each issue and march it prong by prong (L5)?
- Is every legal conclusion hedged with a modal **and graded to an L2 confidence level**, anchored on a named test, case, or statute?
- Did you state the strongest adverse authority and answer it for each contested issue (L6)?
- Is every authority classified by hierarchy (L4), with persuasive-only sources (speeches, no-action letters, proposals) flagged as such — and lapsed guidance noted as withdrawn?
- Does every statement of law carry a citation, and does **no** application-to-facts sentence carry one (L7)? No string-citing for rhythm?
- Is each citation signal the right strength (L7), with parentheticals on analogies?
- Is every citation real, with the correct test cite? (If you could not verify it, it must not be there.)
- For each multi-prong test, did you walk every prong, and synthesize/analogize/distinguish the precedent (L5)?
- Are the TriBar assumptions, exceptions ("Things to Watch Out For"), and knowledge qualifiers present, with reliance limited to the addressee (L3)?
- Is mean sentence length ~28–35 words, with long legal periods controlled by semicolons and serial commas?
- Are semicolons, em-dashes, and parenthetical carve-outs present? (Unlike the whitepaper voice, they must be.)
- Is each defined term bolded-and-quoted on first use, then bare?
- Does each jurisdiction use decimal subsections and close on a "Things to Watch Out For" list of numbered bold labels?
- Is there an Assumptions and Limitations section, and a Limitations footer?
- Does a Summary Answer state the recommendation before the rationale?
- Does every comfort carry its caveat, and does every doctrinal paragraph close on a qualification rather than a flat judgment?
- Is the step plan in the future tense, with each step a bold-label action?
- Are statutory elements in `1)` paren-numerals and advisory lists in `1.` bold-label numerals, not mixed?
- Is every external source footnoted in academic form, and does each figure carry an all-caps title and a color legend?
- Read it aloud: does any sentence promise certainty? If yes, it is not done.

If any answer is wrong — pass over it again with Part I and Part II before delivering.

---

# Reference Library

## R1. The gold-standard exemplar — the corpus, annotated

The whole skill is one document's fingerprint. Key passages and what each teaches:

| Passage | What it demonstrates |
|---|---|
| *"You have requested that we provide you with a structuring proposal on how you can operationalize IndexMaker in a regulatory risk-mitigated manner."* | The we↔you advisory frame; the risk-mitigated framing (S1, S8, L1). |
| *"Under U.S. law, a security is an investment that falls within a regulated category. … by applying the Howey Test, which asks whether there is:"* | Doctrine in impersonal third person; rule then cited controlling test (S1, S8, L1, L5). |
| *"In Williamson v. Tucker, 645 F.2d 404 (5th Cir. 1981) (Williamson), the court recognized that partnership and joint venture interests can qualify as investment contracts if at least one of the following conditions applies:"* | The case-citation convention; the Explanation step; define-the-trigger-then-enumerate (S5, S7, L5, L7). |
| *"To avoid classification as an investment contract, none of these three conditions can be present."* | Define-by-negation for the safe harbor; prong-by-prong logic (S4, S8, L5). |
| *"the securities law risk decreases."* | The conclusion as a probability, graded, never a certainty (S2, S8, L2). |
| *"While the DeFi exclusion removes many obligations, it is important to note that the protocol will still fall under the … CFTC's anti-fraud and anti-manipulation oversight."* | Every comfort paired with its caveat; the adverse point surfaced; the connective the whitepaper voice bans (S8, S9, L2, L6). |
| *"The 'Hinman doctrine' comes from a 2018 speech by William Hinman, then Director of the SEC's Division of Corporation Finance."* | Naming authority with its pedigree — and marking it persuasive-only, revocable agency guidance (S5, S8, L4). |
| *"5. Avoiding Illusory Rights. In Merchant Capital, … Do not use systems that only appear decentralized…"* | The numbered bold label with embedded case cite, distinguished precedent, and instruction (S7, L5, L6). |
| *"Crypto-related activities remain a high-risk area subject to evolving and uncertain regulation; while we have endeavoured to provide a rigorous review, no analysis can eliminate the possibility that…"* | The 65-word legal period with a semicolon; the disclaimer/perimeter register (S3, S6, L3). |
| *"It would be prudent to conduct a subsequent assessment… Such an assessment should be undertaken once the final implementing regulations and interpretive guidance are available…"* | The hedged recommendation tail — a conclusion held at "not free from doubt" (S10, L2). |
| *"By assigning roles through chance, sortition demonstrates that managerial positions are interchangeable and not unique. … This approach is effective only if the selected participants are qualified…"* | The novel substantive argument, anchored on a (secondary) citation and paired with its condition (S10, L4). |
| *"Beneficial ownership reporting is required for anyone with 25% or more governance rights. From experience, it is rare that many, if any, individuals meet this threshold."* | The paired rule→reassurance device, with a knowledge qualifier: state the hard threshold, then deflate it with firm experience (S8, S9, L3). |

## R2. Tells of the voice — phrases that read as this corpus

Recycle these structural phrasings (not the content):
- *"You have requested that we provide you with a structuring proposal on how you can operationalize [X] in a regulatory risk-mitigated manner."*
- *"Our analysis is limited to general informational purposes only and does not constitute, and should not be construed as, legal advice…"*
- *"This proposal outlines a legally lean, modular structure for … mitigating [risk] via [mechanism]. The recommended model uses…"*
- *"Under [law], a [thing] is defined as…"* / *"A '[term]' is defined as a … that is not a …"*
- *"Courts often determine whether … by applying the [X] Test, which asks whether there is:"*
- *"In [Case], [cite], the court recognized that … if at least one of the following conditions applies:"*
- *"the more a [thing] relies on … the more likely it is to meet … the [risk] decreases."*
- *"it may qualify under the exclusion for…"* / *"a token may qualify as a … once…"*
- *"It would be prudent to conduct a subsequent assessment to determine whether…"*
- *"While [X] removes many obligations, it is important to note that … will still fall under … oversight."*
- *"Although [regime] is flexible, there are still mandatory compliance points."*
- *"From experience, it is rare that many, if any, individuals meet this threshold."*
- *"By assigning roles through chance, sortition demonstrates that managerial positions are interchangeable and not unique."*
- *"All voting is weighted by USDC deposits (1 USDC = 1 vote, not index-specific), ensuring governance participation aligns with economic stake."*
- *"Things to Watch Out For"* / *"To reduce the risk of [classification], consider the following:"*

## R3. Anti-pattern table — what breaks the voice

| ❌ Not this voice | ✅ This voice |
|---|---|
| "This structure is fully compliant and carries no securities risk." | "This structure mitigates U.S. securities law risk via progressive decentralization; no analysis can eliminate the possibility of enforcement action." |
| "We unlock a seamless, best-in-class decentralized framework." | "The recommended model uses a Marshall Islands Master–Series DAO LLC for index-level separation." |
| "It's basically a DAO that dodges the SEC." | "Limiting functional involvement with the interface reduces the risk of regulators characterizing IndexMaker Labs as 'operating' the protocol." |
| "The token is not a security. Full stop." | "Under Howey, the analysis turns on whether purchasers are relying on the efforts of others for the token's value." |
| "Trust us, courts will see it our way." | "In Merchant Capital, investor rights were undermined by tactics like pre-filled ballots and default votes for management." |
| "This solves the regulatory problem." | "It would be prudent to conduct a subsequent assessment once the final implementing regulations and interpretive guidance are available." |
| "See [string of six cases] for this well-known point." | "[one on-point cite]." — one authority per proposition; no string-citing for rhythm (L7). |
| "The token is a digital commodity (95% confident)." | "There is substantial authority that the token would qualify as a digital commodity once the network matures." — graded, no bare percentage (L2). |
| "Every case supports us." (favorable authority only) | "While Merchant Capital cuts the other way on locked-in management, the client's Curators are removable and elected, distinguishing it." — adverse authority surfaced and answered (L6). |

## R4. The citation-signal quick reference (L7)

Order of signals in a citation string: **supportive → comparative → contradictory → background.** Within one category, separate with semicolons; across categories, new citation sentence.

| Strength | Signal | One-line meaning |
|---|---|---|
| direct | **[no signal]** | The source states the proposition outright. |
| direct, many | ***e.g.,*** | One representative of many sources that state it. |
| direct, stacked | ***accord*** | A further source agrees; only one is quoted. |
| one-step | ***see*** | Supports, with an inferential step. |
| added | ***see also*** | Extra support after a primary cite. |
| analogy | ***cf.*** | Analogous support; needs a parenthetical. |
| contrast | ***compare … with …*** | The contrast itself makes the point. |
| adverse, direct | ***contra*** | Directly contradicts. |
| adverse, one-step | ***but see*** | Contradicts, with an inferential step. |
| adverse, analogy | ***but cf.*** | Cuts against by analogy; needs a parenthetical. |
| background | ***see generally*** | Useful context, not the specific point. |

## R5. The confidence-ladder quick reference (L2)

Strongest to weakest. Decide the level, then write the matching modal. The only hard number is *more likely than not = > 50%*; the rest are practitioner conventions, never printed in the memo. *Substantial authority* and *reasonable basis* are also the tax penalty-protection standards of IRC §6662 / §6694 (Circular 230 governs the writer) — they carry regulatory weight in a tax opinion, looser weight elsewhere.

| Level | Rough confidence | The memo's modal |
|---|---|---|
| **will** | near-certainty | "will"; settled-law present tense |
| **should** | high, clearly > 50% (~70%+, *approx.*) | "should", "is likely to" |
| **more likely than not** | > 50% | "may qualify", "would likely" |
| **substantial authority** | ~40% *(approx.; a weight-of-authority test)* | "there is substantial authority that…" |
| **reasonable basis** | ~20%+ *(approx.)* | "it may be arguable", "a reasonable basis exists" |
| **not free from doubt** | acknowledged uncertainty | "remains subject to significant regulatory interpretation", "it would be prudent to…" |

## R6. A note on this skill's own prose

The text *describing* this skill follows Max's house voice (patient, Alexander-register, em-dashes welcome). The text the skill *produces* follows the legal-memo voice (hedged, we↔you frame, full punctuation kit, every comfort paired with its caveat, every conclusion graded). Do not confuse the two. And do not confuse this voice with the `jake-writing` whitepaper voice — they are near-inverses on person, punctuation, sentence length, and certainty. When writing the output, the only register that exists is this one.
