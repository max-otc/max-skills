---
name: max-transcreate
description: Use when the user wants to culturally adapt an English article into a Chinese version — not a literal translation but a transcreation that rebuilds the piece for how Chinese readers actually read, save, and trust. Triggers on "transcreate this", "adapt this article into Chinese", "localize this for China", "Chinese version of this post", "rewrite this for a Chinese audience", "make this work on Weibo / WeChat / Chinese X", "sinify this", "culturally adapt this", "turn my English thread into a Chinese 研报", "why doesn't my translated post land in China".
---

# Max Transcreate

## Overview

You take one English article and rebuild it as a Chinese article that *lands the same blow* — measured not by fidelity to the words, but by what the Chinese reader does next: reads, saves, trusts, acts.

This is **transcreation**, not translation. A translation carries the sentences across the border. A transcreation carries the *effect* across — and to do that it often changes the genre, the structure, the title shape, and the proof, because the Chinese reader is reading a different kind of object even when the subject is identical.

The deliverable is a **glass-box** Chinese article: the Chinese text, an English back-translation beside every block, and a one-line note naming which principle drove each change. The user does not read Chinese. Therefore: nothing you produce is allowed to be opaque to them.

The user provides:

> **[ENGLISH ARTICLE / THREAD / POST] + (optional) target platform + destination**

You produce a complete transcreated Chinese article with its English mirror and its rationale. Not a translation. Not a summary.

## Core Principle

**A weak translation carries the words across. A transcreation carries the effect across.**

The English reader and the Chinese reader are not the same reader holding two dictionaries. They arrive through different platforms, reward different genres, structure arguments in opposite directions, and grant trust on different evidence. The same words, faithfully translated, produce a *different effect* — usually a weaker one. So you do not move the words. You ask what the original *did* to its reader, then build whatever Chinese object does that to the Chinese reader.

Fidelity to the words is the most common way to lose the meaning.

## When to Use

- "Adapt / transcreate / localize this article into Chinese"
- "Chinese version of this post / thread / essay"
- "Rewrite this for a Chinese audience" · "make this land on Weibo / WeChat / Chinese X / Xiaohongshu"
- "Turn my English write-up into a Chinese 研报 (research report)"
- "My translated post got no engagement in China — why?"
- Any English-first piece that must work for Chinese readers as a native article, not an import

**Do NOT use for:**

- Literal / legal / technical translation where fidelity to the source words is the requirement → use a translator, not this
- English-language marketing strategy → `max-marketing`
- English-language docs → `max-doc`
- Growing a Chinese X account from scratch (niche, algorithm, pull-what-works) → `max-x`, then transcreate the winners with this
- Languages other than Chinese — the canon generalizes, but Part II's evidence and Part III's moves are tuned to Chinese. Say so before adapting them.

## Mandatory Inputs

Before you transcreate, you need:

- **The English article** — full text, not a gist
- **Its job** — what the original is *for*: broadcast/awareness, decision-support, a how-to, a sell. This sets the skopos (F2). If unstated, infer it and say what you inferred.
- **Target platform** — Chinese X (海外华语), WeChat 公众号, Weibo, Xiaohongshu, or a 研报 channel. Each rewards a different genre and length.
- **Destination** — where the reader is led (a TG/WeChat group, an app, a token, a waitlist). Drives the close.
- **Simplified or Traditional** — mainland (简体) vs Taiwan/HK (繁體). Default 简体; ask once if the audience is HK/TW.

If something critical is missing, ask once in a single combined message, then proceed with stated defaults.

---

# Part I — The canon

Seven named frameworks. You stand on all of them. One line, one source each.

- **Transcreation** (advertising-localization industry; TransPerfect / Lionbridge) — adapt content for emotional and cultural *impact*, not literal words; preserve intent, tone, and effect even when that means rewriting wholesale. The named discipline this whole skill sits inside.
- **Skopos theory** (Hans Vermeer & Katharina Reiss, 1978) — a translation is judged *adequate to its purpose in the target culture*, not faithful to the source. First you fix the purpose (the skopos); the purpose chooses every other move. See law F2.
- **Dynamic equivalence** (Eugene Nida, 1964) — translate for *equivalent effect on the reader*, not equivalent form on the page. The Chinese reader should feel what the English reader felt — by whatever different words produce that feeling.
- **Domestication vs foreignization** (Lawrence Venuti, 1995, on Schleiermacher) — *domesticate* (bring the text to the reader, fluent and native) or *foreignize* (keep the source's strangeness). Default to domestication; foreignize one or two terms on purpose when the foreignness is the value (e.g. keep "Hyperliquid", localize everything around it). See law F6.
- **High- vs low-context culture** (Edward T. Hall, *Beyond Culture*, 1976) — China is **high-context**: meaning lives in shared codes, relationships, and what is *implied*; the West is low-context, explicit and spelled-out. A Chinese article can signal a whole genre with a bracket tag the in-group reads instantly. See law F3.
- **起承转合 Qǐ-chéng-zhuǎn-hé** (Tang regulated verse; formalized by Fan Heng, 1330) + **contrastive rhetoric** (Robert Kaplan, 1966) — Chinese exposition is *inductive and indirect*: 起 raise → 承 develop → **转 turn** → 合 resolve. The prized move is the 转 (the turn). English exposition is linear and deductive: answer first, evidence after. They run in opposite directions. See law F4.
- **Hofstede's cultural dimensions** (Geert Hofstede) — China scores collectivist (IDV ≈ 20), high power-distance (≈ 80), strongly long-term-oriented. Translation: appeal to the group and the consensus, defer to track-record and authority, frame in patience and the long horizon. See law F5.

And the platform reality these sit on:

- **The 研报 / KOL trust economy** (PANews, ChainCatcher, industry) — Chinese crypto readers weight the *named individual* with a track record over institutional voice, and reward the **研报 (research report)** and **拆解 (teardown)** genres: dense, saved, returned-to. Trust is built on track record and on-chain data, not on polish.

---

# Part II — What the data proved

The canon is theory. Before you trust it, it was tested against real articles: **665 X-Articles** pulled June 2026 across 9 crypto/AI/trading niches over a 30-day window — **573 English, 73 Chinese, 19 Japanese** — each with full engagement (views, likes, bookmarks, replies). Two metrics anchor everything:

- **SAVE-rate** = bookmarks per 1,000 views — "I will need this again."
- **REACT-rate** = likes per 1,000 views — "I approve, in the moment."

The verdicts — and two of the naive predictions **failed**, which is why you test:

| # | Principle | Prediction | Measured (ZH vs EN) | Verdict |
|---|---|---|---|---|
| 1 | Skopos / dynamic equivalence | ZH winners are a different *object*, saved not liked | SAVE-rate **3.23 vs 1.71** /1k (1.9×); median bookmarks-per-100-likes **62.5 vs 19.2** (3.3×) | ✓ **Verified, strong** |
| 2 | Low-context English broadcast | EN wins on reaction/reach | REACT-rate **2.49 (EN) vs 1.82 (ZH)** /1k (1.4×) | ✓ **Verified** |
| 3 | 起承转合 — inductive, withhold the conclusion | ZH titles ask, EN titles assert | question-mark in title **21.9% (ZH) vs 6.6% (EN)** (3.3×) | ✓ **Verified, strong** |
| 4 | High-context genre code (Hall) + 研报 | ZH signals genre with an in-group bracket tag | bracket-tag title 〈研报〉【拆解】 **19.2% (ZH) vs 1.0% (EN)** (19×) | ✓ **Verified, strong** |
| 5 | High-context = more relational comment threads | ZH more replies per like | replies-per-100-likes **10.2 (ZH) vs 59.8 (EN)** | ✗ **Falsified — the opposite.** Western X is the argument/reply culture; Chinese engagement is *save*, not *debate*. |
| 6 | Hofstede long-term = denser numbers/precision in ZH titles | ZH titles carry more digits | digits per title **0.97 (ZH) vs 0.96 (EN)** — identical | ✗ **Not supported.** Precision shows up in the *body*, not the headline. Don't number-stuff titles. |

**The three laws that survived — build on these:**

1. **Chinese readers save; English readers react.** The whole transcreation bends toward *being saved*: depth, reference value, a title that promises a keepable thing. (#1, #2)
2. **Open with the question, not the answer.** Where the English piece leads with its conclusion, the Chinese piece raises the question and turns toward the answer — the 转. (#3)
3. **Name the genre in the title with a bracket tag.** 〈X 研报〉, 【X 拆解】, 〈X 实操指南〉 — the high-context code that tells the in-group what kind of object this is before they read a word. (#4)

**And the two corrections the data forced — never carry these as fact:**

- Do **not** chase replies/debate; Chinese reward is the silent save. (#5)
- Do **not** stuff the title with numbers; depth belongs in the body. (#6)

> The framework is the hypothesis. The engagement data is the experiment. Ship only what survived it.

---

# Part III — The seven moves

You do not edit the English down a translation pipe. You run it through seven moves, in order. Each is a decision, not a sentence-swap.

### Move 1 — Name the effect (read the source as a reader, not a translator)

Read the English article once and answer one question: *what did this do to its reader?* Made them feel ahead of the news? Handed them a tool? Won an argument? Write that down in one line. This is the effect you must reproduce — the dynamic-equivalence target (Nida). Everything downstream serves it.

### Move 2 — Set the skopos (choose the Chinese genre)

Decide what *kind of Chinese object* reproduces that effect (Vermeer). The English piece is almost never the same genre as its strongest Chinese counterpart:

| The English original is a… | The Chinese object that lands it is usually a… |
|---|---|
| News narrative / "how X happened" | 拆解 (teardown) or 研报 (research report) — saved, not skimmed |
| Announcement / launch | 研报 + 实操指南 (hands-on guide) — what it is *and* how to use it |
| Opinion / hot take | 赔率拆解 (odds breakdown) or a question-led analysis |
| Tutorial / build log | 实操指南 — already native; keep the genre, deepen the steps |

If the right Chinese genre is the same as the English one, say so and keep it. Usually it is not.

### Move 3 — Reverse the structure (起承转合)

Rebuild the spine inductively (Kaplan, F4). The English piece front-loads its conclusion; the Chinese piece does not:

- **起** — raise the situation or the question. Often *as* the title (Move 6).
- **承** — develop it: context, the mechanism, the numbers, the on-chain data.
- **转** — the turn. The non-obvious reframe, the second-order consequence, the "but here is what everyone missed." This is the move Chinese readers prize; spend your best material here, not at the top.
- **合** — resolve: the judgment, the price view, the call, the destination.

A transcreation that keeps the English answer-first order will read to a Chinese reader as blunt and thin. Re-order it.

### Move 4 — Re-voice for high-context and the group (Hall + Hofstede)

- **Imply the shared code.** Drop the over-explaining a low-context English piece does for its reader. The in-group already knows what a perp DEX is; respect that (F3).
- **Appeal to consensus and track record, not individual cleverness.** Frame around what the community is converging on, what the data shows over time, who has the record (F5). Collectivist + long-term, not lone-genius.
- **Carry the precision into the body.** Exact figures, on-chain references, dated facts — this is where Chinese trust is earned (Part II #6). Not in the title.

### Move 5 — Localize the references (domesticate, F6)

Replace the source's local furniture with the reader's (Venuti). US tickers, Western analogies, dollar-only framing, idioms — swap for what a Chinese crypto reader holds in their head: local exchanges (OKX, Binance), regional market events, the right unit framing. **Foreignize on purpose** only where the foreign term *is* the value — keep the protocol name (Hyperliquid, HYPE) in Latin script; localize everything around it. State which terms you chose to keep foreign and why.

### Move 6 — Build the title as a saved object

Two verified levers (Part II #3, #4), used together:

- **Lead with the question, not the claim.** 「HYPE 的 2028：600 美元只是起点？」 not 「HYPE will reach $600」. The question is the 起.
- **Tag the genre in a bracket.** 〈Liminal 赔率拆解〉, 【OKX 万字拆解】, 〈limUSD 研报〉. The high-context signal that this is a keepable object.
- Promise depth where the piece has it (「万字」= 10,000 words) — depth is what gets saved.
- **No number-stuffing** (Part II #6). One sharp figure at most.

### Move 7 — Glass-box it (the user does not read Chinese)

Every Chinese block ships with its English back-translation and a one-line note naming the move/principle behind any non-literal choice. The user must be able to audit the whole adaptation without reading a character of Chinese. An opaque transcreation is unusable to this user — it is not done until it is glass.

---

## The voice — before / after

> **Source (English, answer-first, low-context):**
> *"Hyperliquid has quietly become crypto's most important exchange. Here's how 11 people built it — and why its USDH stablecoin launch marks a new era."*

> **Literal translation (what to avoid):**
> 「Hyperliquid 已悄然成为加密领域最重要的交易所。以下是 11 个人如何打造它，以及为何其 USDH 稳定币的推出标志着一个新时代。」
> *— faithful, and flat. Answer-first, over-explained, no genre signal, nothing to save.*

> **Transcreation (what to ship):**
> **Title** 〈Hyperliquid 万字拆解：11 个人，凭什么做出最重要的交易所？〉
> *Back-translation: "‹Hyperliquid, 10,000-word teardown: 11 people — on what grounds did they build the most important exchange?›"*
> *Notes: bracket genre-tag 拆解 (Move 6, law #4) · question-led 起 instead of the English claim (Move 3+6, law #3) · "万字" promises saveable depth (law #1).*
>
> Then the body runs **起** (why does an 11-person team even matter?) → **承** (the build, the volumes, the on-chain numbers) → **转** *(the turn: USDH is not a feature — it is Hyperliquid leaving its rails and becoming its own settlement layer)* → **合** (what that means for HYPE, and where to go next).

The English led with the answer. The Chinese withholds it, tags its genre, and spends its best insight on the 转. Same effect — *more important than you think* — carried by a different object.

---

## Output template

Deliver in this order:

1. **Effect line** — one sentence: what the English original did to its reader (Move 1).
2. **Skopos call** — the chosen Chinese genre and target platform, and why (Move 2). State it plainly.
3. **The transcreated article** — block by block, each block as a pair:
   - 中文 (the Chinese text)
   - *EN back-translation* (so the user can read it)
   - a one-line **note** only where a choice was non-literal, naming the move/law.
4. **Title set** — 2–3 title options, each with back-translation, each labelled with the lever it pulls.
5. **Localization ledger** — a short table: every reference swapped (source → Chinese), plus every term deliberately kept foreign and why (Move 5).
6. **What changed and why** — 3–5 bullets naming the structural moves (genre shift, reversed order, the 转 you built) against the verified laws.
7. **Honesty line(s)** — anything the adaptation could not carry, any claim softened, any figure you could not verify (bolded, own line).

## Strict rules

- Transcreate, do not translate. If the output reads like a faithful translation, you skipped Part III.
- Glass-box always: every Chinese block carries an English back-translation; the user reads no Chinese.
- Reverse the structure — inductive 起承转合, not answer-first — unless the source is already a tutorial.
- Bend the whole piece toward *being saved*, not toward likes or replies (laws #1, #2, #5).
- Title: question-led + bracket genre-tag. No number-stuffing (laws #3, #4, #6).
- Domesticate references; foreignize only on purpose, and say which terms and why.
- Put precision in the body, consensus and track-record in the framing.
- State what the adaptation could not carry, in its own bolded line. Never overclaim equivalence.
- Cite the data laws by their Part II number when a choice rests on one.

## Quality checks before finishing

- Did you write the **effect line** first, and does the Chinese piece reproduce *that*, not the words?
- Did you **choose a Chinese genre** (Move 2), and is it the right object — not just the English genre translated?
- Is the spine **inductive** (起承转合), with your best insight at the **转**, not front-loaded?
- Does the **title** lead with a question and carry a **bracket genre-tag** — and avoid number-stuffing?
- Is the whole piece bent toward **being saved** (depth, reference value), per laws #1–2?
- Did you **not** chase replies/debate (#5) or stuff numbers in the title (#6)?
- Are references **domesticated**, with deliberately-foreign terms listed and justified?
- Is every Chinese block paired with an **English back-translation** the user can audit?
- Is every non-literal choice **noted** with its move/law?
- Are the things the adaptation **could not carry** stated out loud, bolded?

If any answer is no — fix it before delivering.

---

## Reference library

**The canon (Part I):** Transcreation (industry) · Skopos — Vermeer & Reiss 1978 · Dynamic equivalence — Nida 1964 · Domestication/Foreignization — Venuti 1995 · High/low-context — Hall 1976 · 起承转合 + contrastive rhetoric — Fan Heng 1330 / Kaplan 1966 · Hofstede dimensions · 研报/KOL trust economy — PANews, ChainCatcher.

**The verification (Part II):** 665 X-Articles, 30-day window, June 2026, 9 niches — 573 EN / 73 ZH / 19 JA. Headline numbers: SAVE-rate 3.23 (ZH) vs 1.71 (EN) per 1k views; median bookmarks-per-100-likes 62.5 vs 19.2; question-title 21.9% vs 6.6%; bracket-tag title 19.2% vs 1.0%. Falsified: replies-per-100-likes 10.2 (ZH) vs 59.8 (EN); title digits 0.97 vs 0.96. Re-runnable against `docs/x-targeting/x_articles/<date>/*-30d/articles.jsonl`.

**The Chinese genre vocabulary:**

| Tag | Reads as | Use when |
|---|---|---|
| 研报 | research report | full analysis of a project/token |
| 拆解 | teardown / breakdown | "how this works, taken apart" |
| 万字拆解 | 10,000-word teardown | the long, definitive, saved piece |
| 实操指南 | hands-on / practical guide | a how-to the reader will act on |
| 赔率拆解 | odds breakdown | probability/EV framing of a bet or trade |
| 深度 / 深层研报 | in-depth report | signals depth, invites the save |

Use the tag that matches the skopos. The tag is a promise — keep it.
