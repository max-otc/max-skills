---
name: max-compress
description: Use when the user wants existing text made much shorter for a HUMAN to read — compressed, condensed, distilled, tightened — keeping every main point and cutting only what does not serve them. Triggers on "compress this", "condense", "shorten this", "make this shorter", "cut this down", "tighten this", "distill this", "boil it down", "trim this", "too long — shorten it", "TL;DR but keep what matters", "make this denser", "make it more concise", "summarize tightly", "halve this", "make it a third the length", and whenever a long answer must be made compact for a person to read. NOT for machine/token compression (LLMLingua, Sparse Priming Representations — those write for a model, not a reader). NOT for explaining one concept simply (use max-eli5). NOT for rewriting a whole docs set (use max-doc).
---

# Max Compress

## Overview

You take a long text and hand back a short one a person can read in a third of the time — and lose nothing that mattered. Not a chopped excerpt. Not the first paragraph with the rest deleted. A *judged* compression: you found the points the text exists to deliver, kept every one of them, and incinerated the filler around them.

The deliverable is the compressed text and nothing else — same meaning, same usable conclusions, a fraction of the words. The reader finishes it able to act, decide, or repeat the content exactly as they could from the original, only faster.

Compression is not truncation. Truncation keeps the start and drops the end. Compression keeps the *spine* and drops the *padding* — wherever in the text the padding happens to sit.

## Core Principle

**A weak shortening removes words. A real compression removes what the reader can live without, and keeps every load-bearing point untouched.**

Most "make it shorter" fails the same way: it cuts the end, or it thins every sentence evenly until the whole thing is vague. Both lose signal. The craft is to separate the load-bearing from the decorative — the claim from the example that illustrates it, the decision from the deliberation behind it, the fact from the three softening qualifiers around it — and to spend your word budget entirely on the load-bearing.

Keep what changes the reader's understanding. Cut what only decorates it.

## When to Use

- "Compress / condense / shorten / tighten / distill / trim this"
- "Cut this down" · "boil it down" · "make it denser" · "make it more concise"
- "Too long — shorten it" · "TL;DR but keep everything important"
- "Make it half the length" · "get it to ~150 words" · "fit this in a paragraph"
- When **your own** prior answer ran long and the user wants the compact version
- Tightening an article, report, transcript, thread, email, or spec for a human to skim

**Do NOT use for:**

- Token/prompt compression for a **machine** reader → LLMLingua-2, or David Shapiro's Sparse Priming Representations. Those deliberately write for a model and read as shorthand to a human. This skill is the opposite — readable prose for a person.
- Explaining **one** hard concept in plain words → `max-eli5`
- Rewriting a whole documentation set → `max-doc`
- Pulling **everything** out of a source (extraction, which expands) → not compression; say so and stop

This skill produces **one shorter readable text**, faithful to the source. It never adds new claims and never invents.

## Foundations — the canon

You stand on the named work of the people who already solved pieces of this. One line each.

**The engine:**

- **Chain of Density** (Griffin Adams, Alexander Fabbri, Faisal Ladhak, Eric Lehman, Noémie Elhadad — Salesforce AI / Columbia / MIT, 2023) — write a summary at a *fixed* length, then rewrite it denser and denser, each pass folding in the salient facts you missed and cutting filler to make room. The finding that governs this whole skill: **humans prefer the middle of the chain, not the end.** Pushed to maximum density, the text becomes a buzzword list and readability collapses. Stop where density and readability still meet.
- **Fabric** (Daniel Miessler) — the `summarize` and `create_micro_summary` patterns: a one-sentence core, a few tight main points, a few takeaways, in clean Markdown. The shape of a readable digest.

**The decision rules — what to cut:**

- **"Omit needless words"** (William Strunk & E. B. White, *The Elements of Style*) — the oldest law. Every word that can be removed without loss of meaning *must* be. Vigorous writing is concise.
- **Grice's Maxims** (Paul Grice) — Quantity: say exactly as much as is needed, no more. Relevance: drop what does not bear on the point. Manner: be brief and orderly, avoid obscurity. This is your filter for every sentence.
- **Signal and noise** (Claude Shannon, information theory) — compression keeps the *surprising* and drops the *predictable*. The words a reader could have guessed carry no information; spend nothing on them.

**The ordering rule — what comes first:**

- **The Pyramid Principle** (Barbara Minto, McKinsey) — answer first, support beneath. The main point leads; the reasons and detail follow, in descending order of weight. A compression that buries its conclusion has failed twice.
- **Progressive Summarization** (Tiago Forte, *Building a Second Brain*) — "a method for *forgetting* as much as possible." Keep only what earns its place; let the rest go.

**The boundary — what this is not:**

- **Sparse Priming Representations** (David Shapiro) — compresses ~10:1, but its own prompt says it writes "for another language model, not a human." That is the line. If the reader is a person, SPR is the wrong tool, and so is anything that reads as shorthand. You always produce readable prose.

## The method — eight laws

### 1. Find the spine first.

Before cutting a word, read the whole text and name the **load-bearing points** — the claims, facts, decisions, or instructions the text exists to deliver. Usually a handful. Write them in your head as a list. Everything that is not one of these, or directly required to understand one, is a candidate for deletion.

> You are not shortening the text. You are keeping the spine and dropping the flesh around it.

### 2. Rank everything against the spine.

For every sentence, ask one question: *does this carry a load-bearing point, or does it decorate one?* Decoration is the illustrating example, the second example, the restatement, the throat-clearing intro, the hedge, the aside, the "as we all know." Decoration goes. The point stays.

### 3. Cut by Grice, hard.

Delete, in this order: off-topic material (Relevance), repetition and restatement (Quantity), hedging and qualifiers that do not change the truth (Manner), filler phrases ("it is important to note that", "in order to", "the fact that"), and examples that only illustrate a point already clear. Strunk's law runs underneath all of it: if a word can go without loss, it goes.

### 4. Keep the surprising, drop the predictable.

A reader gains nothing from words they could have guessed. Generic openers, stock transitions, and ambient context the reader already holds carry no signal — cut them and spend the budget on the specific, the named, the numeric, the decisive. The fact `revenue fell 12% in Q3` survives; "the company faced some challenges" does not.

### 5. Densify at fixed length — fold, don't list.

Now rebuild within your word budget, Chain-of-Density style. Fuse related survivors into single sentences. Compress phrases to words ("at this point in time" → "now"). Pack the named facts in. The target is not a thinner version of every sentence — it is *fewer, fuller* sentences, each carrying more.

### 6. Stop at the readable middle.

Push density until one more turn of the screw would make it read like a telegram or a buzzword list — then back off one notch. This is the single most important law, and the one Chain of Density's research proved: maximum density is not the goal, maximum density *that still reads well* is. If a human would have to slow down and decode it, you went too far.

### 7. Answer first.

Lead with the main point, Minto-style. The conclusion, the headline fact, the decision — first sentence. Supporting detail descends from there by weight. Never make the reader hunt the bottom of the text for the thing it was about.

### 8. Verify nothing load-bearing died.

Final pass, with the spine list from law 1 in hand: is every load-bearing point still present and still true? Could the reader act, decide, or repeat the content the same way from your short version as from the original? If the loss of a cut fact would change what the reader does, it was load-bearing — restore it. Faithfulness outranks brevity. A shorter text that misleads is worse than a longer one that does not.

## How short, and what shape

**Default target: ~3× shorter** (keep roughly a third). Obey any explicit instruction the user gives — "halve it", "to 100 words", "to a tweet", "to three bullets", "as short as it can be without losing anything." When they name a budget, hit it; when they don't, aim for a third and let the spine decide — a dense source compresses less, a padded one compresses more.

**Shape is adaptive — read the source:**

- **Structured source** (headings, lists, a report) → return a lean structure: a one-line lead, then tight points. Skimmable.
- **Flowing prose** (an essay, an argument, a story) → return tight prose. Reads like a person wrote a short version, not an outline of one.
- **A conversation or transcript** → return the decisions and the open questions, not the back-and-forth.

When in doubt, prose. An outline is easy; readable compressed prose is the craft.

## The voice — before / after

> **Before (211 words):**
> *"I wanted to take a moment to reach out and provide you with an update on where things currently stand with the Henderson project, which as you know has been ongoing for several months now. After a great deal of internal discussion and back-and-forth among the various stakeholders involved, we have ultimately come to the decision that it would be in everyone's best interest to push the launch date back. The new target that we are now aiming for is the 15th of March. The primary reason behind this decision, to be completely transparent with you, is that the design team has unfortunately encountered a number of unexpected technical challenges relating to the mobile version of the product, and these are challenges that we feel really do need to be properly addressed before we move forward. We would of course much rather get this right than rush it out the door. On the budget side of things, I'm happy to report that we are still tracking within the range we originally set, so there are no concerns there at this time. I'll be sure to send along another update as soon as we have more to share. Please don't hesitate to reach out with any questions."*
>
> **After (~3.4× shorter, 41 words):**
> **Henderson launch moved to March 15.** The design team hit technical problems on the mobile version that we need to fix before shipping. Budget is still on track. More to come; ask if you have questions.

Answer first — the new date leads. The spine survives whole: new date, the reason, budget status. Gone: the throat-clearing, the "as you know", the "to be completely transparent", every doubled phrase. Nothing a reader would act on was lost.

## Process

1. **Read the whole thing.** Name the load-bearing points (law 1). Hold them as your target.
2. **Rank and cut** — decoration, repetition, hedging, predictable filler (laws 2–4).
3. **Densify** within the budget — fuse, compress phrases, pack the named facts (law 5).
4. **Find the readable edge** — push density, then back off one notch (law 6).
5. **Order it** — answer first, support by weight (law 7).
6. **Verify the spine** — every load-bearing point present and true; faithful action preserved (law 8).
7. **Deliver the result only** — no preamble, no "here is your compressed text." Offer a one-line *"want to see what I cut?"* only if the cuts were aggressive enough that the user might want to check.

## Output rules

- Deliver the compressed text and nothing else by default. No "Here's a shorter version:" wrapper.
- Match the source's shape (prose → prose, structured → lean structure).
- Lead with the main point. Always.
- Hit the requested length; default ~3× when none is given.
- Never add a claim, fact, or framing not in the source. Compression only removes and fuses — it does not invent.
- Keep the register of the source unless asked to change it. A compressed legal notice still reads as a legal notice.
- If the text is already tight and cannot lose a third without losing meaning, say so and compress only as far as is honest. Do not fabricate slack that isn't there.

## Strict rules

- Keep every load-bearing point. Faithfulness outranks brevity, always.
- Cut decoration, not conclusions. Never shorten by truncating the end.
- Answer first — the main point leads the result.
- Stop at the readable middle. Dense-but-readable beats maximally-dense.
- Readable prose for a human — never SPR-style shorthand or token-soup.
- Remove only; never invent. No new claims, no editorializing.
- Result only — no preamble, no meta-commentary unless asked.

## Common mistakes

| Mistake | What it looks like | Fix |
|---|---|---|
| **Truncation in disguise** | Keeps the first third verbatim, deletes the rest. The conclusion, often at the end, vanishes. | Compress across the *whole* text. Find the spine wherever it sits; the last line is often the most load-bearing. |
| **Even thinning** | Every sentence shaved 30%, so the whole thing goes vague and nothing is sharp. | Don't thin uniformly. Delete whole decorative sentences; keep load-bearing ones at full strength. |
| **Over-densification** | Pushed to the dense end — reads like a buzzword telegram, reader has to decode it. | Back off one notch from maximum. The readable middle is the target (Chain of Density). |
| **Lost a load-bearing fact** | A number, date, name, or caveat that changes the reader's decision got cut as "detail." | Run the law-8 fidelity check: would losing this change what the reader does? If yes, restore it. |
| **Buried lead** | The main point sits in sentence four; the result opens with context. | Minto: answer first. Conclusion leads, support descends. |
| **Invented to smooth** | Added a connective claim or framing not in the source to make it flow. | Remove and fuse only. If it wasn't in the source, it doesn't go in the compression. |

## Quality checks before finishing

- Did you name the spine first — and is every load-bearing point still in the result?
- Could the reader act, decide, or repeat the content the same way from your version as from the original?
- Does the main point lead the first sentence?
- Did you cut whole decorative sentences rather than thinning every sentence evenly?
- Is it dense but still *readable* — would a human read it at speed without decoding?
- Is it readable prose for a person, not shorthand for a machine?
- Did you only remove and fuse — adding nothing new?
- Did you hit the requested length (or ~3× by default)?

If any answer is no — compress again, more carefully, before delivering.
