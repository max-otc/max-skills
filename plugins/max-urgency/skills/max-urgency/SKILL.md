---
name: max-urgency
description: Deadline-mode orchestration — a hard clock, ten or more subagents live at all times, the critical path found and starved of everything else, incremental pushes, a standby for every single point of failure. Use for "we ship in N hours", "accelerate", "we are late", "keep pushing".
---

# max-urgency

One orchestrator, zero work in chat. The clock is the only requirement that survives step 1. Built from the 2026-09-02 audit freeze: 3 hours, 4 tag moves, 3 builder deaths, delivered 30 minutes early.

## Step 0 — read the clock, write the clock

- `date` first. Deadline in EDT on the first line of every status message. Hard stops for every lane are 15–25 minutes before it.
- Say out loud what the critical path is: the ONE chain of machine-bound steps (compile → proof → push → tag). Everything not on it runs in parallel; nothing not on it is allowed to block it.

## Step 1 — question every requirement, then delete

- For each item in the queue: "if we ship without it, what breaks?" Usually nothing. The tag needs code green and pins coherent. Docs, sweeps, re-ranks land AFTER the tag as docs-only pushes. The tag can move; a missed deadline cannot.
- The rule that survives deletion: **never tag a tip whose pins disagree with its own source.** Everything else is negotiable against the clock.
- One compile. If the tree has not changed in that language since the last green run, the run stands. "Optimize to not do 2 solc" — Max.

## Step 2 — ten agents, always

Fewer than ten live means the orchestrator is doing something an agent should. Roles that filled the ten:

| Role | Count | Model |
|---|---|---|
| Builder (one clone, one lock, serial builds, incremental pushes) | 1 | opus |
| **Standby builder** — watches four signals, takes over only on 7 min silence + no process + no push | 1 | opus |
| Lane writers on DISJOINT files, each emits `patch-<x>.diff` + `patch-<x>.md` with integrity counts | 4–6 | opus |
| Verifiers, one per landed patch, "assume it is wrong" | 2–3 | opus |
| Fixers for the deliverables (edition, table), parameterized, armed on a `TAG.sha` file | 2 | fable |
| Cold reader / fresh-clone smoke — the auditor's first hour, from a network clone | 1–2 | opus |

- Machine-bound work does not parallelize (one solc, one docker ELF). Everything else does. If only four agents are live, the doc queue is behind the builder: that is the mistake.
- Rate limits kill agents in batches. Relaunch every cut agent from disk state, on the model that still has budget (`model: opus`). The standby exists for this.
- Subagent cap is 20. Fan-out inside lanes counts. Launch lean.

## Step 3 — patches, not edits

- Lanes never touch the builder's clone. They branch off a NAMED base sha, edit disjoint files, and emit a diff. The orchestrator tests every diff TOGETHER in a throwaway clone (`git apply` all, run the doc gates) before the builder sees any of them. The builder applies with one command.
- A lane that branched off the wrong base produces a diff that cannot apply. Replay its judgements BY KEY (row id, symbol) onto the live file; never `-X theirs`, never drop.
- Stamp placeholders (`@TAGSHA@`) and let the builder substitute at commit time with the amend trick: commit → take sha → sed → `commit --amend --no-edit` → tag. Nothing is pushed before the amend.

## Step 4 — push on a cadence, not at the end

- Max watches GitHub. A 45-minute gap reads as a stall. Push every green increment to main; move the tag at the end, as many times as needed (delete, re-push annotated, same name, never `--force` on main).
- Every push: `git fetch --prune` first, fast-forward only, PROGRESS line with the sha. The orchestrator confirms on the remote (`git ls-remote`), never from the agent's word.
- Two pushers is a race. One pusher. The orchestrator may push a docs-only correction itself when the builder has stood down and the gate is green.

## Step 5 — verify the system

- Every claim re-derived by someone who did not make it: a lens re-runs the check. A cited line is not a read line.
- Each landed patch gets a verifier before the builder applies it; each verifier verdict routes the same minute: exact edits → the builder; owner calls → the sheet.
- After the tag: fresh-clone day-one (follow the readme literally, run everything), doc-rule sweep over every `.md`, register consistency across all deliverables, code residue hunt, vkey reproduction with docker. Five lenses, one message, then the tag moves once more if they find anything.

## Rules around it

- Status to Max: three lines — where we are, what is left, what needs his word. Numbers on their own line. No narration of options.
- Two irreversible calls (delete a remote tag, push a repo that auto-deploys prod) wait for his word even at 13:52. Everything reversible proceeds.
- The day plan B starts, plan A is dead: when the builder dies, the standby IS the builder. No post-mortem in the chat; the memory line carries it.
- Did we hit the wall fast enough? If the first push came after 45 minutes, no.

## Files

- `$S/PROGRESS.md` — the builder's timestamped truth; agents read, never write.
- `$S/TAG<N>.sha` — one file per tag move; fixers key on it.
- `$S/patch-<lane>.diff` + `.md` — every lane's output; `$S/VERIFY-<x>.md` — every verifier's.
- `$S/POST-TAG-CLEANUP.sh` — guarded (dirty, unmerged, running build, tag present, `DRY=1`); dry-run before the real run.
- Memory: one line per push, per tag, per relaunch; a `feedback` file for every rule Max states in the session.
