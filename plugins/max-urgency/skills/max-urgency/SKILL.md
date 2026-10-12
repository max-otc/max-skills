---
name: max-urgency
description: Use for deadline-mode orchestration on a hard clock — "we ship in N hours", "accelerate", "we are late", "keep pushing".
---

# max-urgency

One orchestrator, zero work in chat. Built from the 2026-09-02 audit freeze: 3 hours, 4 tag moves, 3 builder deaths, delivered 30 minutes early.

## 0. Clock and critical path

- `date` first. The deadline in EDT opens every status message. Each lane's hard stop is 15–25 min before it.
- Name the critical path out loud: the ONE chain of machine-bound steps (compile → proof → push → tag). Everything else runs in parallel; nothing else may block it.

## 1. Question every requirement, then delete

The clock is the only requirement that survives this step, plus one rule: **never tag a tip whose pins disagree with its own source.** Everything else is negotiable against the clock.
- Ask of each queue item: "if we ship without it, what breaks?" Usually nothing. The tag needs green code and coherent pins. Docs, sweeps and re-ranks land AFTER the tag as docs-only pushes. The tag can move; a missed deadline cannot.
- One compile: if the tree has not changed in that language since the last green run, the run stands. "Optimize to not do 2 solc" — Max.

## 2. Ten agents, always

Fewer than ten live means the orchestrator is doing an agent's work. Every single point of failure gets a standby. All roles opus:

| Role | Count |
|---|---|
| Builder: one clone, one lock, serial builds, incremental pushes | 1 |
| **Standby builder**: watches four signals; takes over only on 7 min silence + no process + no push | 1 |
| Lane writers on DISJOINT files; each emits `patch-<x>.diff` + `patch-<x>.md` with integrity counts | 4–6 |
| Verifiers, one per landed patch, "assume it is wrong" | 2–3 |
| Fixers for the deliverables (edition, table), parameterized, armed on a `TAG.sha` file | 2 |
| Cold reader / fresh-clone smoke: the auditor's first hour, from a network clone | 1–2 |

- Only machine-bound work is serial (one docker ELF). Forge builds follow crx-deploy-speed: one forge lock; solc-par splits one compile over 6 solc. If only four agents are live, the doc queue is behind the builder: that is the mistake.
- Rate limits kill agents in batches. The standby exists for this. Relaunch every cut agent from disk state, on the model that still has budget (`model: opus`).
- The tool runs 20 live per session (nested counted) and queues the rest. Launch all orchestrators at once.

## 3. Patches, not edits

- Lanes never touch the builder's clone. They branch off a NAMED base sha, edit disjoint files, emit a diff. Before the builder sees any, the orchestrator `git apply`s all diffs TOGETHER in a throwaway clone and runs the doc gates. The builder applies with one command.
- A diff off the wrong base will not apply. Replay its judgements BY KEY (row id, symbol) onto the live file; never `-X theirs`, never drop.
- Stamp placeholders (`@TAGSHA@`). The builder substitutes them at commit time with the amend trick: commit → take sha → sed → `commit --amend --no-edit` → tag. Nothing is pushed before the amend.

## 4. Push on a cadence, not at the end

- A 45-minute gap reads as a stall. Push every green increment to main. Move the tag at the end, as often as needed: delete, re-push annotated, same name; never `--force` on main.
- Every push: `git fetch --prune` first, fast-forward only, a PROGRESS line with the sha. The orchestrator confirms on the remote (`git ls-remote`), never on the agent's word.
- One pusher; two is a race. The orchestrator may push a docs-only correction itself once the builder has stood down and the gate is green.

## 5. Verify the system

- Every claim is re-derived by someone who did not make it: a lens re-runs the check. A cited line is not a read line.
- Each landed patch gets a verifier before the builder applies it. Route each verdict the same minute: exact edits → the builder; owner calls → the sheet.
- After the tag, five lenses in one message: fresh-clone day-one (follow the readme literally, run everything), doc-rule sweep over every `.md`, register consistency across all deliverables, code residue hunt, vkey reproduction with docker. Any finding moves the tag once more.

## Rules around it

- Status to Max: three lines: where we are, what is left, what needs his word. Numbers on their own line. No narration of options.
- Two irreversible calls wait for his word even at 13:52: deleting a remote tag, pushing a repo that auto-deploys prod. Everything reversible proceeds.
- The day plan B starts, plan A is dead: when the builder dies, the standby IS the builder. No post-mortem in chat; the memory line carries it.
- Did we hit the wall fast enough? A first push after 45 minutes means no.

## Files

- `$S/PROGRESS.md`: the builder's timestamped truth; agents read, never write.
- `$S/TAG<N>.sha`: one per tag move; fixers key on it.
- `$S/patch-<lane>.diff` + `.md` per lane; `$S/VERIFY-<x>.md` per verifier.
- `$S/POST-TAG-CLEANUP.sh`: guarded (dirty, unmerged, running build, tag present, `DRY=1`); dry-run first.
- Memory: one line per push, tag and relaunch; a `feedback` file per rule Max states in the session.
