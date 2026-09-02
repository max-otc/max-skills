---
name: max-musk
description: Use when orchestrating subagents and the task must ship 10x faster or simpler — "max-musk", "run it Musk-style", "apply the algorithm", "this pipeline is bloated", "too many agents", "too many steps", a brief longer than a screen, a plan that inherits last session's pipeline, or a team of agents spread across several priorities.
---

# max-musk

Musk's five-step algorithm (as told by Karim Bousta, Tesla VP 2016–2018), applied to managing agents. Steps run in this order. Skipping a step or reordering them is the failure this skill exists to stop. Target is 10x, never 10%.

**Argument:** the task. Read it, then run the five steps BEFORE any dispatch.

## 1. Question every requirement

List every requirement the task carries: the owner's words, CONTRIBUTING/CLAUDE rules, the repo's rituals, last session's pipeline, your own additions.

For each line write: `req | owner (one human or one file:line) | what breaks if deleted`.

- No owner → not a requirement. Delete.
- Owner is a document, not a human → the document is the person to "call": read it for the reason, not the rule. No reason stated → delete.
- Owner is Max → keep, or put it on a decision sheet (`max-decisions`). Never "lightweight versions". Never satisfy a ritual halfway.
- A requirement that gives a human a veto (approvals, sign-off, review by a person) is owned by that human, not by the document that names it. Route it to them in one line. The orchestrator never deletes it and never stands in for the human.
- Your own additions (config flags, stores, monitoring, notes for later) → delete. Someone asks for them back later, that is the signal you went far enough.

## 2. Delete every part you can

The dispatch plan with the fewest agents and the fewest steps that still proves the change works. Then delete one more.

- Verification tiers exist for money, irreversibility, or an audit. A reversible change gets one builder and one green run.
- Delete scouts when the builder can read. Delete doc agents when the diff is the doc. Delete "fixer" rounds until a verifier fails.
- You went far enough when a verifier or Max asks for a step back. If nobody asks, cut again next time.

## 3. Simplify and optimize

Only now. Rebuild the plan from a blank sheet, not from last session's pipeline. Do not "trim" the old one. Write the new one in ≤ 10 lines.

## 4. Accelerate cycle time

Cycle = owner's ask → pushed and verified. Write the natural estimate, then divide by ten. That is the target. Not 4x.

- Put the clock in every brief: `target: <N> min`.
- Everything that does not shorten the cycle waits.
- Two or three subjects live at once, at full depth. Nothing else exists.

## 5. Automate, last

No scripts, hooks, cron, loops, or watchdog automation until the manual run has succeeded twice. Automating a step freezes it. Automate the simplified pipeline, never the inherited one.

## Briefs

Every agent prompt is three lines, then pointers:

```
Problem: <one line>
Why this fix: <one line>
The fix: <one line>
target: <N> min · files: <paths> · report: 3 lines, PASS/FAIL first
```

Paste rules files by path, not by content. Reports back are three lines. An agent that sends status essays is cut.

## Plan A / plan B

- Plan B exists and is invisible in every brief.
- The day B starts, A is dead: kill A's agents, delete A's worktree, never keep "5 agents on A, 5 on B".
- No post-mortem. One question, one line: did we hit the wall fast enough?

## Ideas have no rank

A verifier's fix is as valid as the builder's. A cheap model's finding is as valid as an expensive one's. Route by the fact, not by the agent.

## Two agent profiles

- Builders: ask questions after. "Try it, we will see."
- One or two verifiers: ask questions before. More than two paralyse the round.

## Rationalizations

| Excuse | Reality |
|---|---|
| "CONTRIBUTING says so, I'll do a light version" | A light version keeps the step. Find the reason or delete it. |
| "90 min vs 6 h is already fast" | 4x is optimization. The target is 10x. Divide again. |
| "A config flag / kill switch / Redis note costs nothing" | They are requirements you invented. Delete. |
| "A scout first, to be safe" | The builder reads. Delete the scout. |
| "Two approvals: Max is the only approver, so one verifier" | A human veto is the human's. One line to Max, then wait. |
| "Keep A running while B ramps" | Half-and-half is how projects die. Kill A. |
| "The prompt must be self-contained" | Three lines plus paths is self-contained. |
| "I'll automate the pipeline now, it's repeatable" | It has not run manually twice. Not yet. |

## Red flags

- A brief longer than a screen.
- A requirement whose owner is "the process".
- A plan that starts from last session's plan.
- A time target set by rounding, not by dividing by ten.
- Two plans alive at once.
- A post-mortem meeting.

Any of these: back to step 1.

Source: Karim Bousta on Silicon Carne, https://www.youtube.com/watch?v=LcGlqRYfX88
