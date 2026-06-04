# max-skills

A Claude Code plugin marketplace. Personal skills for research, creative, and content work.

## Install the marketplace

Once. From inside Claude Code:

```
/plugin marketplace add max-otc/max-skills
```

## Install everything in one shot

```
/plugin install max-skills@max-skills
```

That installs all nine skills below as a single bundle. Use this if you want the lot.

## Install a single skill

```
/plugin install <skill-name>@max-skills
```

Replace `<skill-name>` with one of the entries below.

## Skills

### max-persona-research

Deep qualitative Reddit research. Reconstructs a target persona for a brand or product from real Reddit discussions: pain points, language, objections, current solutions, journey, strategic gaps. Eleven sections, evidence-loaded. Refuses to summarize.

```
/plugin install max-persona-research@max-skills
```

Invoke by asking Claude to do Reddit research on a brand, build a persona, or run voice-of-customer analysis.

### max-hook

Generate ten neurologically-engineered video ad hooks for TikTok / Reels / Shorts / Meta. Each hook is engineered to create a mental rupture in under two seconds — pattern interrupt, open loop, visual tension. Awareness-matched, sound-off readable, algorithm-friendly. Includes a strategy brief naming the best hook for cold traffic, warm traffic, viral potential, and safe bets.

```
/plugin install max-hook@max-skills
```

Invoke by asking Claude to "write a hook", "give me scroll-stoppers", "open my video", "first 2 seconds for my ad", or any first-frame attention-capture task.

### max-explainer-video

Generate scene-by-scene scripts for stick-figure / whiteboard / Notion-style explainer videos — the kind with hand-drawn characters, emoji section headers, callout boxes, and a "wait... what?" moment in scene one. Structured as a loop ladder: hook → key concept → mechanism → three pillars → examples → rules → conclusion. Visual-first, sound-off readable.

```
/plugin install max-explainer-video@max-skills
```

Invoke by asking Claude to "write an explainer", "turn this into a stick-figure video", or "script a whiteboard video about X".

### max-video

Walk one worked YouTube video end-to-end. Nine sequential phases — idea, research, angle of attack, detailed plan & script, voice-over, edit, title & thumbnail, publish, statistics — with one artifact written to `videos/<slug>/` per phase. For long-form storytelling videos (15 min to an hour, 20–80 hours of work), not shorts or explainers. Method from What a Fail!'s *Comment faire des vidéos (travaillées)*.

```
/plugin install max-video@max-skills
```

Invoke by asking Claude to "make a YouTube video about X", "script a long-form video on Y", or "help me produce a worked video".

### max-ai-video

Write an AI-tool / trading-creator YouTube script in the recent DaviddTech mould — the "I let Claude build X, here's what happened" genre, with a free workbook for a comment, a community of hundreds, and a paid tier at the end. Hook-first cold open, stacked authority, an enemy, a buddy-talk demo, a funnel staircase, the sign-off jingle. Eleven-part anatomy and ten sentence laws (result first, land on a punch, one breath per sentence, plain word then gloss). Built part by part, sentence by sentence, to `scripts/<slug>/`.

```
/plugin install max-ai-video@max-skills
```

Invoke by asking Claude to "write a video like DaviddTech", "script my AI tool video", "sell my tool on YouTube", or "write the video sentence by sentence, part by part".

### max-x

Data-driven X / Twitter growth. You don't invent content — you pull what already works in the niche via `twitterapi.io`, reverse-engineer *why* it works, recycle it with your angle, and lead the reader to a CTA. Models the six laws of the X algorithm (niche-first distribution, the consistency law, the soccer-coach memory, the flux gate, the reply game, dead niches), runs the creator-mining loop, builds the data-article "stock not flux" machine, and stands up a 5-account angle-testing rig. Output is an eleven-section growth operating plan. Distilled from Max OTC's method (the source conversation ships with the skill).

```
/plugin install max-x@max-skills
```

Invoke by asking Claude to "grow my Twitter", "X growth strategy", "what niche should I post in", "pull top creators in my niche", "why aren't my bangers working", "build me a reply-game plan", or "set up a multi-account testing rig".

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
4. Commit, push, bump

## License

MIT.
