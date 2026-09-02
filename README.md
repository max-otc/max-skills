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

That installs all sixteen skills below as a single bundle. Use this if you want the lot.

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


### max-x

Data-driven X / Twitter growth. Pull what already works in the niche via `twitterapi.io`, reverse-engineer *why*, recycle it with your angle, lead the reader to a CTA. Six laws of the algorithm, the creator-mining loop, the data-article "stock not flux" machine, a five-account angle-testing rig. Output is an eleven-section growth operating plan.

Invoke with "grow my Twitter", "what niche should I post in", "why aren't my bangers working".

### max-marketing

Full e-commerce creative strategy — angle portfolio, awareness × sophistication map, villain/hero arc, EPIC distribution, hook bank, Entity ID variants, Andromeda 2026 test plan. Distilled from the 0€→1M€/mois ecom playbook (Schwartz, Hormozi, Rogers).

Invoke with "build me a marketing strategy", "find angles for my product", "EPIC angles".

### max-doc

Write or rewrite documentation in Max's house style — learning paths per reader, Feynman Q&A, terse, no TL;DRs. From a product or codebase to a small set of pages that answer the reader's real questions.

Invoke with "write the docs", "rewrite this doc", "document this".

### max-compress

Hyper-compress any text for a human reader — keep every load-bearing point, incinerate the filler. Chain of Density held at its readable middle, output shaped like Fabric's digest. Roughly 3x by default, obeys explicit targets. Not token-soup for a model — readable prose for a person.

Invoke with "compress this", "cut this down", "make it a third the length".

### max-ux-flow

Design a UX flow finance-first (regulated, but modern) and general-capable — what the user sees first, what they click, screen by screen, what each table shows, how the data is structured, mobile versus desktop, and the money/approval/KYC safety layer. Twenty frameworks into an eleven-section flow spec.

Invoke with "design the flow", "map the screens", "what goes in this table".


### jake-writing

A formal whitepaper in Jake Schkolnick's CRX-litepaper voice — terse, third-person, present-tense, define-by-negation, run-in bold labels, no em-dash, no hype. Nine-dimension style fingerprint plus a twelve-axis replication checklist.

Invoke with "write the litepaper", "in Jake's voice", "whitepaper version".

### formatting-marketmaker-documents

Format and render formal CRX market-maker documents to the CRX document standard — Margin and Settlement Overview, Collateral Overview, methodologies, mechanism memos. One locked LaTeX-style document class with a conformance gate that renders HTML to PDF locally.

Invoke with "format this CRX doc", "match the CRX standard", "render to PDF".

### max-decisions

Every open decision as one clickable HTML sheet — question, zero-context explanation, options with pros/cons, one recommendation, one verdict line per card. Answer inside the page, press Send.

Invoke with "what decisions are needed", "make a decisions file", "what do I need to rule on".

### max-plan-itteration

Verify a plan, report, or agent-produced doc by fresh adversarial verifier pairs until a full round adds nothing.

Invoke with "verify", "check this", "is this true", "gate it".

### max-blacklist

The ban-word and anti-AI-slop blacklist — banned words, phrases, and 26 measured sentence-structure pattern rules, matched by a Python linter, never by the model. Ships ste-lint.py, ste-lint-code.py, md-structure.py, words.txt.

Invoke with "run the blacklist", "slop check", "AI tells", "banned words".

### max-audit-loop

Full security audit of a smart-contract + zk-guest codebase, optionally benchmarked against a named auditor's public findings. Cross-maps the standard onto the repo, deep-hunts protocol surfaces, fans out specialist auditors, false-positive-gates every finding before it ships.

Invoke with "audit against <auditor>", "do the audit loop", "check if things they flag we flag too".

### max-hard-audit

The 10-agent parallel audit loop — read-only lenses in rounds, a dedup file, verifier pairs plus a fixer on one consolidated table, cold closes, solutions per fix owner, decision sheets, one serial builder, incremental pushes.

Invoke with "audit X hard", "keep auditing in loops", "audit + fix + push to main".

### max-merge

Consolidate branches, worktrees, or clones of one repo into a single clean main. Subagents hand-pick and rebase each branch; pushes go out serially; zero parked branches remain.

Invoke with "merge everything", "one clean main", "collapse the branches".

### max-clean-computer

Free disk on a Mac while builds run. Finds regenerable storage — caches, build targets, temp — and cleans only what is safe.

Invoke with "clean storage", "free disk", "disk full", "ENOSPC".

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
