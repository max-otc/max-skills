---
name: max-musk
description: Use when orchestrating subagents and the task must ship 10x faster or simpler — "max-musk", "run it Musk-style", "apply the algorithm", "this pipeline is bloated", "too many agents", "too many steps", a brief longer than a screen, a plan that inherits last session's pipeline, or a team of agents spread across several priorities.
---

# max-musk

Musk's five-step algorithm (as told by Karim Bousta, Tesla VP 2016–2018), applied to managing agents. **Argument:** the task. Read it, then run the five steps in order, BEFORE any dispatch; skipping or reordering one is the failure this skill stops. Target 10x, never 10%.

## 1. Question every requirement

List every requirement: the owner's words, CONTRIBUTING/CLAUDE rules, the repo's rituals, last session's pipeline, your own additions. Per line: `req | owner (one human or one file:line) | what breaks if deleted`.

- No owner → not a requirement. Delete.
- Owner is a document → it is the person to "call": read it for the reason, not the rule. No reason stated → delete. "CONTRIBUTING says so, I'll do a light version": a light version keeps the step. Find the reason or delete it.
- Owner is Max → keep, or put it on a decision sheet (`max-decisions`). Never lightweight versions. Never satisfy a ritual halfway.
- A human veto (approvals, sign-off, review by a person) is owned by that human, not by the document that names it. Route it to them on a max-ask sheet. Never delete it, never stand in for the human: "Two approvals: Max is the only approver, so one verifier" is that mistake; ask Max on a max-ask sheet, then wait.
- Your own additions (config flags, kill switches, stores, Redis notes, monitoring, notes for later) are requirements you invented, even when they "cost nothing". Delete. When someone asks for one back, you went far enough.

## 2. Delete every part you can

Plan the fewest agents and steps that still prove the change works. Then delete one more.

- Verification tiers are for money, irreversibility or an audit. A reversible change gets one builder and one green run.
- Delete scouts when the builder can read ("a scout first, to be safe" included), doc agents when the diff is the doc, "fixer" rounds until a verifier fails.
- You went far enough when a verifier or Max asks for a step back. If nobody asks, cut again next time.

## 3. Simplify and optimize

Only now. Rebuild the plan from a blank sheet, ≤ 10 lines. Never trim last session's pipeline.

## 4. Accelerate cycle time

Cycle = owner's ask → pushed and verified. Write the natural estimate, divide by ten: that is the target. Not 4x: 4x is optimization ("90 min vs 6 h is already fast" → divide again).

- Every brief carries the clock: `target: <N> min`.
- Everything that does not shorten the cycle waits.
- Two or three subjects live at once, at full depth. Nothing else exists.

## 5. Automate, last

No scripts, hooks, cron, loops or watchdog automation until the manual run has succeeded twice, however repeatable it looks. Automating a step freezes it. Automate the simplified pipeline, never the inherited one.

## Briefs

Every agent prompt is three lines, then pointers; that is self-contained:

```
Problem: <one line>
Why this fix: <one line>
The fix: <one line>
target: <N> min · files: <paths> · report: 3 lines, PASS/FAIL first
```

Paste rules files by path, not by content. Reports back: three lines. Cut an agent that sends status essays.

## Plan A / plan B

- Plan B exists, invisible in every brief.
- The day B starts, A is dead: kill A's agents, delete A's worktree. Never "5 agents on A, 5 on B", never A running while B ramps: half-and-half is how projects die.
- No post-mortem. One question, one line: did we hit the wall fast enough?

## Ideas have no rank

A verifier's fix counts as much as the builder's, a cheap model's finding as an expensive one's. Route by the fact, not the agent.

## Two agent profiles

- Builders ask questions after: "Try it, we will see."
- One or two verifiers ask questions before. More than two paralyse the round.

## Red flags: back to step 1

A brief longer than a screen. A requirement whose owner is "the process". A plan that starts from last session's plan. A time target set by rounding, not by dividing by ten. Two plans alive at once. A post-mortem meeting.

Source: Karim Bousta on Silicon Carne, https://www.youtube.com/watch?v=LcGlqRYfX88
