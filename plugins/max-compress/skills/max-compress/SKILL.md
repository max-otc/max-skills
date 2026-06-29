---
name: max-compress
description: Use when the user wants existing text made dramatically shorter for a HUMAN to read — hyper-compressed, condensed, distilled, cut down hard — keeping the decisive core and deleting everything else. Default is aggressive: at least 3x shorter, often more. Triggers on "compress this", "condense", "shorten this", "make this much shorter", "cut this down", "cut most of this", "tighten this", "distill this", "boil it down", "trim this hard", "too long — cut it", "TL;DR", "make this denser", "make it way more concise", "summarize tightly", "halve this", "make it a third / a tenth the length", and whenever a long answer must be made compact for a person. NOT for machine/token compression (LLMLingua, Sparse Priming Representations — those write for a model). NOT for explaining one concept simply (use max-eli5). NOT for rewriting a whole docs set (use max-doc).
---

# Max Compress

## Overview

You take a long text and return a *much* shorter one — a third of the length, often less — that a person reads in a fraction of the time and loses nothing that decides anything. Not a reworded version of the same length. Not every point kept and lightly trimmed. A violent cut: you keep the decisive core and delete the rest — the elaboration, the justification, the examples, the second clause, the parenthetical, the restatement.

The deliverable is the compressed text and nothing else. If it is not dramatically shorter than the original, you have not compressed it — you have only edited it, and you must go back and cut.

Compression is destruction with judgment. Most of the words go. The few that carry the decision stay.

## Core Principle

**If the result is not at least three times shorter, you failed. The job is to delete, not to reword.**

The way this skill fails is always the same: it decides everything is important, keeps every point, rewords each sentence a little tighter, and hands back a text nearly as long as the original. That is the one outcome that is not allowed. Length reduction is not a side effect of this skill — it *is* the skill. You start from the assumption that most of the text can go, and you defend only the words that earn their place by changing what the reader knows or does.

Keep the load-bearing few. Delete the comfortable many.

## When to Use

- "Compress / condense / shorten / tighten / distill / trim this — hard"
- "Cut this down" · "cut most of this" · "boil it down" · "make it way shorter"
- "Too long — cut it" · "TL;DR" · "give me the short version"
- "Make it half / a third / a tenth the length" · "fit this in a paragraph / three bullets"
- When **your own** prior answer ran long and the user wants the compact version
- Cutting an article, report, spec, transcript, thread, or email down for a human to skim

**Do NOT use for:**

- Token/prompt compression for a **machine** reader → LLMLingua-2, or Sparse Priming Representations. Those write for a model and read as shorthand to a human. This skill produces readable prose for a person.
- Explaining **one** hard concept in plain words → `max-eli5`
- Rewriting a whole documentation set → `max-doc`
- Pulling **everything** out of a source (extraction, which expands) → not compression

This skill produces **one much shorter readable text**, faithful to the source. It never adds a claim and never invents.

## Foundations — the canon

The named work this stands on. One line each.

- **"Omit needless words"** (William Strunk & E. B. White, *The Elements of Style*) — the law under everything. Every word that can go without loss *must* go. Read it as a command, not advice.
- **Grice's Maxims** (Paul Grice) — Quantity: say exactly enough and no more. Relevance: cut what does not bear on the point. Manner: be brief. Your filter for every clause.
- **Signal and noise** (Claude Shannon) — words a reader could have predicted carry zero information. Generic openers, soft transitions, restated context — all noise. Spend nothing on them.
- **The Pyramid Principle** (Barbara Minto, McKinsey) — answer first, support beneath, in descending weight. The conclusion leads; most of the support gets cut.
- **Progressive Summarization** (Tiago Forte) — "a method for *forgetting* as much as possible." Keep only what earns its place; let the rest go.
- **Chain of Density** (Adams, Fabbri, Ladhak, Lehman, Elhadad — Salesforce / Columbia / MIT) — fuse the survivors into fewer, fuller sentences; pack the named facts in. But take its lesson at the *readable* edge: dense, not a telegram.
- **Sparse Priming Representations** (David Shapiro) — the boundary. It writes "for another language model, not a human." If the reader is a person, that is the wrong tool. You always produce readable prose — short, but read like writing.

## The method — the laws

### 1. Cut to the budget. This is the job.

Fix the target before you write: default **at least 3x shorter** (keep one third or less). When the user names a budget — half, 150 words, a tweet, three bullets — hit it exactly. When they don't, assume they want it *short*, and lean past a third, not short of it. If your draft isn't dramatically shorter than the source, you haven't done the task. Cut again.

> Compression is the deletion. Everything else is bookkeeping.

### 2. The core is smaller than it looks.

In real text the decisive content is a fraction of the words. Each bullet, each sentence usually carries **one** load-bearing fact — and around it: the reason it's true, an example, a parenthetical, a qualifier, a restatement, a transition. The fact is the core. **All the rest is expendable.** Keep the *what*; drop the *why* and the *how-we-know* unless the reader cannot act without them. When unsure whether something is core, it is not — cut it.

### 3. Collapse the structure.

Do not preserve the shape one-to-one. Ten bullets become three; a section becomes a sentence; flowing argument becomes one dense paragraph. Fuse related points into a single line. The original's outline is not sacred; the original's *meaning* is. A compression that keeps every heading and bullet has not compressed — it has reformatted. Collapse the *count*, not the form: when the survivors are still 2+ parallel items, keep them as a tight bullet list (see Output rules), not buried in prose — fewer bullets, never zero.

### 4. Delete by Grice, ruthlessly.

In order, cut: off-topic material, repetition and restatement, hedging and qualifiers that don't change the truth, filler phrases ("it is important to note", "in order to", "the fact that"), every example that only illustrates a point already made, and every word a reader could have guessed. Keep the specific, the named, the numeric, the decisive. `revenue fell 12% in Q3` survives; "the company faced some headwinds" dies.

### 5. Fuse and densify what survives.

Rebuild inside the budget, Chain-of-Density style: merge survivors into single sentences, compress phrases to words ("at this point in time" → "now"), pack the named facts together. The target is not thinner sentences — it is *far fewer, fuller* ones.

### 6. Run the halve-again test.

Look at your draft and ask: *could I cut this in half again and still keep every decision?* If yes — do it. Repeat until one more cut would remove a fact the reader acts on. Most first drafts of a "compression" are still twice as long as they need to be. The instinct to keep is the enemy; distrust it.

### 7. Answer first.

Lead with the main point — the conclusion, the headline fact, the decision. Minto. Never make the reader earn the point by reading to the end. After compression the lead is often the *only* thing that survives from a whole paragraph.

### 8. Keep it true, keep it readable.

Two floors, and only two. **True:** never invent, never reverse a claim, never let a surviving sentence mislead. Losing detail is the goal; losing *accuracy* is failure. **Readable:** what survives reads like writing, not telegram shorthand or token-soup — dense, but a human reads it at speed. Everything between these two floors is yours to delete, and you should.

## How short — the violence dial

Default hard. Read the request:

- **Default** — at least 3x shorter (keep ≤ 1/3). Use this whenever no level is given. Err toward more.
- **Brutal** — when they say "as short as possible", "just the gist", "one line", "ruthless", "a tenth": cut to the irreducible core, 5–10x, sometimes a single sentence. Keep only what the reader cannot act without.
- **Light** — *only* when they explicitly ask for a gentle trim ("tighten slightly", "trim 20%"). Then preserve more structure. This is the exception, never the default.

If the text is genuinely irreducible — code, a one-line definition, a list of bare facts with no prose around them — say so and cut only as far as is honest. But normal prose, specs, reports, and threads always carry far more slack than they appear to. Assume the slack is there and find it.

## The voice — before / after

> **Before (118 words):**
> *"I'm writing to let you know that, after what has been quite a long period of careful internal deliberation and a fair amount of discussion across the team, we have arrived at the conclusion that we will unfortunately need to make the difficult decision to sunset the legacy analytics dashboard. The date we are targeting for this is the 30th of September. The main driver behind all of this is that the underlying database it relies upon is being fully decommissioned, and as a result we simply won't be able to keep the dashboard running past that point. Customers who are currently still relying on it will be migrated over automatically, so no action is required on their part."*
>
> **After (~5x shorter, 24 words):**
> **Legacy analytics dashboard sunsets September 30** — its database is being decommissioned. Current users migrate automatically; no action needed.

The decision leads. Only the decisive facts survive: what, when, why, and what the reader must do. Everything else — the deliberation, the "difficult decision", every doubled phrase — is gone. Not reworded. *Gone.*

## Process

1. **Set the budget** (law 1) — default ≥3x, brutal if asked. Write the number down before you draft.
2. **Mark the core** (law 2) — the one decisive fact in each point. Everything unmarked is a deletion candidate, which means most of the text.
3. **Delete and collapse** (laws 3–4) — drop the expendable, fuse what's left, ignore the original's shape.
4. **Densify** (law 5) — fewer, fuller sentences; pack the named facts.
5. **Halve again** (law 6) — cut the draft in half once more if the decisions survive.
6. **Order and check** (laws 7–8) — answer first; true and readable; on budget.
7. **Deliver the result only** — no "here's a shorter version" wrapper. Offer a one-line *"want to see what I cut?"* only if the cut was deep enough that the user might want to check.

## Output rules

- Deliver the compressed text and nothing else by default. No preamble.
- Be dramatically shorter — ≥3x unless told otherwise. If it isn't, cut again before delivering.
- Collapse structure freely; do not mirror the original's bullets or headings.
- **Bullet every list.** When 2+ parallel items survive (options, steps, properties, facts of one kind), give each its own line, lead with the noun (the thing named — not "The" or a verb), and use no trailing punctuation. Continuous argument stays prose.
- Lead with the main point.
- Never add a claim, fact, or framing not in the source. Compression only removes and fuses — it never invents.
- Keep the register of the source (a compressed legal notice still reads as one) unless asked to change it.
- Readable prose, never machine shorthand.

## Strict rules

- At least 3x shorter by default. Reword-only at full length is the one forbidden outcome.
- Keep the decisive core; delete elaboration, justification, examples, restatement.
- Collapse structure — fuse many points into few.
- Bullet any list of 2+ parallel items — one per line, lead with the noun, no trailing punctuation.
- Answer first.
- True and readable are the only floors. Everything else is deletable.
- Remove and fuse only; never invent.
- Result only — no meta-commentary unless asked.

## Common mistakes

| Mistake | What it looks like | Fix |
|---|---|---|
| **The timid reword** | Every bullet kept, each lightly reworded, output nearly as long as the input. The cardinal failure. | Compression is deletion. Set a hard ≥3x budget, cut whole points, collapse the structure. If it's not much shorter, you didn't do it. |
| **Everything is "load-bearing"** | Treats every clause as essential, so nothing gets cut. | The core is one fact per point; the reasons, examples, and qualifiers around it are expendable. When unsure, cut. |
| **Structure preserved** | Ten bullets in, ten bullets out — reformatted, not compressed. | Collapse. Ten points become three or one paragraph. The outline isn't sacred. |
| **Stopped too early** | Shorter, but still twice as long as it needs to be. | Run the halve-again test. Cut the draft in half once more while the decisions survive. |
| **Over-cut into shorthand** | So terse it reads like a telegram or token-soup. | Back off to the readable edge. Dense prose a human reads at speed — not a keyword list. |
| **Lost a decisive fact** | A number, date, name, or caveat the reader acts on got cut. | Keep the facts that change what the reader does. Cut the prose around them, not them. |
| **Invented to smooth** | Added a connective claim to make it flow. | Remove and fuse only. If it wasn't in the source, it doesn't go in. |

## Quality checks before finishing

- Is it at least 3x shorter than the source? If not, cut again — this is non-negotiable.
- Did you delete whole points and collapse the structure, not just reword each line?
- Could you halve it again and still keep every decision? If yes, do it.
- Does the main point lead the first sentence?
- Did every decisive fact (numbers, dates, names, caveats) survive?
- Is it dense but still readable prose — not shorthand for a machine?
- Did you only remove and fuse, adding nothing?
- Is every list of 2+ parallel items bulleted — one per line, noun first, no trailing punctuation?

If any answer is no — cut harder before delivering.
