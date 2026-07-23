# max-skills

A Claude Code plugin marketplace. Personal skills for research, creative, writing, docs, and content work.

## Install the marketplace

Once. From inside Claude Code:

```
/plugin marketplace add max-otc/max-skills
```

## Install everything in one shot

```
/plugin install max-skills@max-skills
```

That installs all seventeen skills below as a single bundle. Use this if you want the lot.

## Install a single skill

```
/plugin install <skill-name>@max-skills
```

Replace `<skill-name>` with one of the entries below.

## Skills

### max-persona-research

Deep qualitative Reddit research. Reconstructs a target persona for a brand or product from real Reddit discussions: pain points, language, objections, current solutions, journey, strategic gaps. Eleven sections, evidence-loaded. Refuses to summarize.

Invoke by asking Claude to do Reddit research on a brand, build a persona, or run voice-of-customer analysis.

### max-hook

Ten neurologically-engineered video ad hooks for TikTok / Reels / Shorts / Meta. Each hook creates a mental rupture in under two seconds — pattern interrupt, open loop, visual tension. Awareness-matched, sound-off readable. Includes a brief naming the best hook for cold traffic, warm traffic, viral potential, and safe bets.

Invoke with "write a hook", "give me scroll-stoppers", "first 2 seconds for my ad".

### max-explainer-video

Scene-by-scene scripts for stick-figure / whiteboard / Notion-style explainer videos — hand-drawn characters, emoji section headers, callout boxes, a "wait... what?" moment in scene one. Loop ladder: hook → key concept → mechanism → three pillars → examples → rules → conclusion.

Invoke with "write an explainer", "script a whiteboard video about X".

### max-video

One worked YouTube video end-to-end. Nine sequential phases — idea, research, angle, title & thumbnail, script, voice-over, edit, publish, statistics — one artifact per phase in `videos/<slug>/`. For long-form storytelling videos (15 minutes to an hour), not shorts. Method from What a Fail!'s *Comment faire des vidéos (travaillées)*.

Invoke with "make a YouTube video about X", "script a long-form video on Y".

### max-ai-video

An AI-tool / trading-creator YouTube script in the recent DaviddTech mould — hook-first cold open, stacked authority, an enemy, a buddy-talk demo, a funnel staircase, the sign-off jingle. Eleven-part anatomy, ten sentence laws. Built part by part, sentence by sentence.

Invoke with "write a video like DaviddTech", "script my AI tool video".

### max-x

Data-driven X / Twitter growth. Pull what already works in the niche via `twitterapi.io`, reverse-engineer *why*, recycle it with your angle, lead the reader to a CTA. Six laws of the algorithm, the creator-mining loop, the data-article "stock not flux" machine, a five-account angle-testing rig. Output is an eleven-section growth operating plan.

Invoke with "grow my Twitter", "what niche should I post in", "why aren't my bangers working".

### max-marketing

Full e-commerce creative strategy — angle portfolio, awareness × sophistication map, villain/hero arc, EPIC distribution, hook bank, Entity ID variants, Andromeda 2026 test plan. Distilled from the 0€→1M€/mois ecom playbook (Schwartz, Hormozi, Rogers).

Invoke with "build me a marketing strategy", "find angles for my product", "EPIC angles".

### max-doc

Write or rewrite documentation in Max's house style — learning paths per reader, Feynman Q&A, terse, no TL;DRs. From a product or codebase to a small set of pages that answer the reader's real questions.

Invoke with "write the docs", "rewrite this doc", "document this".

### max-circle

Refactor documentation page by page to the level of Circle's developer docs. Four tiers mined from the Circle corpus: the page system, seven sentence habits, per-mode section choreography, the Circle lexicon. Default mode rebuilds each page from its blueprint; an opt-in pass mode polishes sentences only. Every page survives a register trial before delivery.

Invoke with "circle-quality", "refactor the docs like Circle", "raise the level of English".

### max-eli5

Rewrite any concept "explain like I'm 5" — answer-first, one everyday analogy carried all the way, one mechanism, jargon defined on use, one repeatable takeaway. Built on Feynman, Curse of Knowledge, Hofstadter, Made to Stick.

Invoke with "ELI5", "explain this simply", "in plain English".

### max-compress

Hyper-compress any text for a human reader — keep every load-bearing point, incinerate the filler. Chain of Density held at its readable middle, output shaped like Fabric's digest. Roughly 3x by default, obeys explicit targets. Not token-soup for a model — readable prose for a person.

Invoke with "compress this", "cut this down", "make it a third the length".

### max-walkthrough

Annotated product screenshots and a step-by-step visual walkthrough, produced by running the real web app in a build-time mock mode, capturing clean shots, and baking arrows and callouts in. The visual companion to `max-doc` — a screenshot the build regenerates never lies.

Invoke with "screenshot every step", "redo the docs with screenshots", "product tour with arrows".

### max-video-walkthrough

An animated Remotion walkthrough video built from scratch — a faux browser holding real captured screen states, a bezier cursor that glides and clicks, typed inputs, rolling numbers, page-load bars, popup callouts, a wallet-approval popup, all driven by a beat timeline. The motion companion to `max-walkthrough`.

Invoke with "walkthrough video", "animated product demo", "cursor demo video".

### max-ux-flow

Design a UX flow finance-first (regulated, but modern) and general-capable — what the user sees first, what they click, screen by screen, what each table shows, how the data is structured, mobile versus desktop, and the money/approval/KYC safety layer. Twenty frameworks into an eleven-section flow spec.

Invoke with "design the flow", "map the screens", "what goes in this table".

### max-ch-article

Culturally adapt an English article into a Chinese one — cultural adaptation, not translation. Skopos, Nida, Venuti, Hall, 起承转合, Hofstede, the 研报 trust economy, verified against 665 real X-Articles. Rebuilt inductive, genre-tagged, bent toward being saved. Glass-box, with an English back-translation.

Invoke with "adapt this article for Chinese readers", "write the Chinese version".

### max-legal

A formal legal structuring memorandum — privileged-and-confidential opinion-letter register, letter header, decimal-numbered sections, case-cited rule-application, jurisdiction-by-jurisdiction analysis, "Things to Watch Out For" lists, a structure diagram, a step plan, a limitations footer.

Invoke with "structuring memorandum", "draft the memorandum", "legal opinion version of this".

### jake-writing

A formal whitepaper in Jake Schkolnick's CRX-litepaper voice — terse, third-person, present-tense, define-by-negation, run-in bold labels, no em-dash, no hype. Nine-dimension style fingerprint plus a twelve-axis replication checklist.

Invoke with "write the litepaper", "in Jake's voice", "whitepaper version".

## Update

```
/plugin marketplace update max-skills
```

## Uninstall

```
/plugin uninstall <skill-name>@max-skills
```

## Adding a new skill

1. Create `plugins/<skill-name>/.claude-plugin/plugin.json`
2. Add the skill body at `plugins/<skill-name>/skills/<skill-name>/SKILL.md`
3. Add an entry to `.claude-plugin/marketplace.json`
4. Run `plugins/max-skills/sync.sh` so the bundle picks it up
5. Add a section to this README
6. Run `./validate.py` — it fails if a manifest or the README names a skill that is not there, or omits one
7. Commit, push, bump

## License

MIT.
