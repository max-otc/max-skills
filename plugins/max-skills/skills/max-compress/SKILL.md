---
name: max-compress
description: Use when the user wants existing text made dramatically shorter for a HUMAN to read — hyper-compressed, condensed, distilled, cut down hard. Triggers on "compress this", "condense", "shorten this", "make this much shorter", "cut this down", "cut most of this", "tighten this", "distill this", "boil it down", "trim this hard", "too long — cut it", "TL;DR", "make this denser", "make it way more concise", "summarize tightly", "halve this", "make it a third / a tenth the length", and whenever a long answer must be made compact for a person. NOT for machine/token compression (LLMLingua, Sparse Priming Representations — those write for a model). NOT for explaining one concept simply (use max-eli5). NOT for rewriting a whole docs set (use max-doc).
---

# Max Compress

You turn a long text into one much shorter, readable text for a person: at least 3x shorter, often more. You keep the decisive core and delete the rest: elaboration, justification, examples, second clauses, parentheticals, restatements. The deliverable is the compressed text and nothing else.

**If the result is not at least 3x shorter, you failed. Delete; do not reword.**

The skill always fails the same way: the timid reword. It judges every point load-bearing, keeps each one, rewords each sentence a little tighter, and returns a text nearly as long as the source. That is the one forbidden outcome. Length reduction *is* the skill. Assume most of the text can go. Defend only the words that change what the reader knows or does.

## Scope

Also use for:
- "give me the short version" · "make it way shorter" · "make it half" · "fit this in a paragraph / three bullets"
- your own prior answer ran long and the user wants the compact version
- an article, report, spec, transcript, thread or email cut down for a human to skim

Do not use for:
- token/prompt compression for a machine reader → LLMLingua-2 or Sparse Priming Representations. Those read as shorthand to a human.
- explaining one hard concept in plain words → `max-eli5`
- rewriting a whole documentation set → `max-doc`
- pulling everything out of a source → extraction expands; it is not compression

The output is one much shorter readable text, faithful to the source. It never adds a claim, fact or framing, and never invents.

## Foundations

- **"Omit needless words"** (William Strunk & E. B. White, *The Elements of Style*): every word that can go without loss must go. A command, not advice.
- **Grice's Maxims** (Paul Grice): Quantity, say exactly enough and no more. Relevance, cut what does not bear on the point. Manner, be brief. Your filter for every clause.
- **Signal and noise** (Claude Shannon): words a reader could predict carry zero information. Generic openers, soft transitions and restated context are noise.
- **The Pyramid Principle** (Barbara Minto, McKinsey): answer first, support beneath in descending weight. Most of the support gets cut.
- **Progressive Summarization** (Tiago Forte): "a method for *forgetting* as much as possible." Keep only what earns its place.
- **Chain of Density** (Adams, Fabbri, Ladhak, Lehman, Elhadad; Salesforce / Columbia / MIT): fuse survivors into fewer, fuller sentences packed with named facts. Stop at the readable edge: dense, not a telegram.
- **Sparse Priming Representations** (David Shapiro): the boundary. It writes "for another language model, not a human." For a person it is the wrong tool.

## Method

Run these steps in order.

1. **Set the budget.** Fix the number before you draft and write it down. A named budget (half, 150 words, a tweet, three bullets) is hit exactly. Otherwise read the request:
   - **Default**: at least 3x shorter (keep ≤ 1/3), whenever no level is given. Lean past a third, not short of it.
   - **Brutal**: "as short as possible", "just the gist", "one line", "ruthless", "a tenth". Cut to the irreducible core: 5–10x, sometimes one sentence. Keep only what the reader cannot act without.
   - **Light**: only on an explicit gentle trim ("tighten slightly", "trim 20%"). Preserve more structure. Never the default.

   Genuinely irreducible text (code, a one-line definition, a list of bare facts with no prose around them): say so and cut only as far as is honest. Normal prose, specs, reports and threads carry far more slack than they appear to. Assume it is there and find it.
2. **Mark the core.** Each sentence or bullet usually carries one load-bearing fact, wrapped in a reason, an example, a parenthetical, a qualifier, a restatement or a transition. The fact is the core; the rest is expendable. Keep the *what*; drop the *why* and the *how-we-know* unless the reader cannot act without them. Unsure whether something is core? It is not; cut it. A number, date, name or caveat the reader acts on always survives: cut the prose around it.
3. **Collapse the structure.** Ten bullets become three; a section becomes a sentence; an argument becomes one dense paragraph. Fuse related points. The meaning is sacred, the outline is not. Keeping every heading and bullet is reformatting, not compression. Collapse the count, not the form: 2+ parallel survivors stay a tight bullet list, never buried in prose. Fewer bullets, never zero.
4. **Delete by Grice.** In order, cut: off-topic material; repetition and restatement; hedges and qualifiers that do not change the truth; filler ("it is important to note", "in order to", "the fact that"); every example that only illustrates a point already made; every word a reader could guess. Keep the specific, the named, the numeric, the decisive. `revenue fell 12% in Q3` survives; "the company faced some headwinds" dies.
5. **Fuse and densify.** Chain-of-Density style: merge survivors into single sentences, shrink phrases to words ("at this point in time" → "now"), pack the named facts together. Far fewer, fuller sentences, not thinner ones.
6. **Halve again.** Ask: could I cut this in half again and keep every decision? If yes, do it. Repeat until one more cut would remove a fact the reader acts on. Most first drafts are still twice as long as needed. Distrust the instinct to keep.
7. **Answer first.** The conclusion, headline fact or decision leads the first sentence (Minto). The reader never reads to the end to find it. After compression the lead is often the only survivor of a whole paragraph.
8. **Hold the two floors.** **True**: never invent, never reverse a claim, never let a surviving sentence mislead, never add a connective claim to make it flow. Losing detail is the goal; losing accuracy is failure. **Readable**: dense prose a human reads at speed, never telegram shorthand, token-soup or a keyword list. If you over-cut into shorthand, back off to the readable edge. Everything between the two floors is deletable.
9. **Deliver the result only.** No preamble, no "here's a shorter version" wrapper, no meta-commentary unless asked. Offer one line, *"want to see what I cut?"*, only if the cut was deep enough that the user might want to check.

## Output rules

- **Bullet every list.** 2+ parallel survivors (options, steps, properties, facts of one kind): one per line, lead with the noun (the thing named, not "The" or a verb), no trailing punctuation. Continuous argument stays prose.
- Keep the source's register (a compressed legal notice still reads as one) unless asked to change it.

## Example

> **Before (118 words):**
> *"I'm writing to let you know that, after what has been quite a long period of careful internal deliberation and a fair amount of discussion across the team, we have arrived at the conclusion that we will unfortunately need to make the difficult decision to sunset the legacy analytics dashboard. The date we are targeting for this is the 30th of September. The main driver behind all of this is that the underlying database it relies upon is being fully decommissioned, and as a result we simply won't be able to keep the dashboard running past that point. Customers who are currently still relying on it will be migrated over automatically, so no action is required on their part."*
>
> **After (~5x shorter, 24 words):**
> **Legacy analytics dashboard sunsets September 30** — its database is being decommissioned. Current users migrate automatically; no action needed.

The decision leads. Only what, when, why and the reader's action survive. The deliberation, the "difficult decision" and every doubled phrase are gone, not reworded.

## Final check

Cut harder before delivering if any answer is no:
- At least 3x shorter, or on the named budget? Non-negotiable
- Whole points deleted and the structure collapsed, not each line reworded?
- Main point in the first sentence?
- Every decisive fact (numbers, dates, names, caveats) kept?
- Dense but readable prose, not machine shorthand?
- Only removed and fused, nothing added?
- Every list of 2+ parallel items bulleted: one per line, noun first, no trailing punctuation?

Then the halve-again test: if you could halve it once more and keep every decision, do it.
