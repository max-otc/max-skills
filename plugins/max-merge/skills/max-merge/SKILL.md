---
name: max-merge
description: Use when several branches, worktrees, or clones of one repo must be consolidated into a single clean main — "merge everything", "land all the branches", "one clean main", "consolidate the worktrees", "merge all outstanding work", "collapse the branches", zero parked branches — especially with a concurrent live session committing in the same tree. Fans out subagents to hand-pick and rebase each branch; pushes serially.
---

# max-merge

Consolidate every outstanding branch/worktree/clone of one repo into **one clean main**, respecting other agents live in the tree. Survey → classify → fan out to rebase → push serially → prune → verify.

## The shape

1. **Survey (read-only, one subagent).** Map everything: `git branch -vv`, `git worktree list`, every clone under `~`, `~/Downloads`, and each VPS (`ssh`, find `.git` dirs, match `origin`). ALSO: every OTHER session's scratchpad worktrees (`find /private/tmp/claude-501 -maxdepth 4 -name .git`, rev-parse each HEAD), and `git ls-remote --heads origin` side branches. Per item: ahead/behind `origin/main`, dirty count, conflicts vs main, what it is. Sample the live checkout's HEAD + dirty at start AND end — a moving HEAD is a finding.
2. **Classify** every item:
   - **A already on main** (ancestor/merged) — nothing to do.
   - **B clean land** (ahead, no conflict, coherent) — rebase → build → push.
   - **C conflicts** — rebase → resolve keep-both → build → **verify** → push.
   - **D do-not-merge** — foreign branches (e.g. an outside contributor's port), old-commit audit pins, superseded doc branches. Leave or prune, never merge.
   - **E-active** — another agent MID-WORK: moving HEAD, dirty files, running gates. NEVER commit its files; leave the tree.
   - **F finished handoff** — another session's DONE-but-unpushed work: clean tree, gates green, agent idle/stopped. This is class B, not E — fetch the SHA into the primary clone immediately (scratchpad GC risk), then land it. Includes unpushed amended commits and remote side branches whose owning session has stopped.

   **Merge doctrine: maximum of each agent's work survives.** When two lanes touch the same code, the goal is not "pick a winner" — it is line-by-line reconciliation that keeps everything each side built, as long as the whole stays coherent. Drop a side's hunk only when it is provably superseded (main carries an equivalent or newer form — cite the sha) or the owner ruled it out. "Too entangled" earns a dedicated line-by-line lane, not a drop.

   An entangled-conflict abort is a HANDOFF, not a drop: after the serial lander finishes, dispatch a dedicated semantic-merge agent per aborted branch — it reads both sides, merges by meaning, runs the touched suites foreground, then pushes. The consolidation is not done while an aborted branch has no dedicated lane.

   **"Include all" means ALL.** When Max says include all / merge everything, every completed commit lands regardless of which session produced it — local branches, other sessions' finished handoffs, remote side branches. The ONLY exclusions: mid-work trees (E-active), audit pins, `-parked` branches, and entangled-conflict aborts — each named in the report with its reason. Never silently skip work because another session touched it.
3. **Fan out** up to 10 subagents when branches are independent — each in **its own worktree** — for parallel rebase+build. Independent builds parallelize; **pushes to main are serial (one pusher)**.
4. **Order:** clean (B) first, conflicts (C) last, dependencies respected. Each lands, then the next rebases onto the **new** tip.
5. **Prune:** collapse to one clean main, zero parked branches. Keep audit pins + the live checkout.
6. **Final verify:** build the final `origin/main` tip; measure any size cap (EIP-170). Confirm only `main` + intended pins remain.

## Non-negotiable rules (each earned by a real failure)

| Rule | The failure it prevents |
|---|---|
| **Builds run FOREGROUND; the agent waits for the exit code.** No backgrounding, no "a monitor will notify me". | An agent backgrounded its `forge build`, said "compiling, waiting for the monitor", and **exited — nothing landed**. Foreground-only is the fix. |
| **One pusher to main.** `git fetch --prune` right before every push; re-rebase if it moved. | Concurrent sessions push between your fetch and push. A fast-forward of your exact commit is fine; a divergence is not — re-rebase. |
| **Never touch the live session's working tree.** No `git add -A`, no `reset`, no `stash`. Commit only your own paths. | Committing "everything" snapshots another agent's half-finished refactor and pushes a red tree. |
| **Build in YOUR OWN scratchpad, recreate checkouts from SHAs.** | Other-session scratchpad worktrees are **garbage-collected mid-task** — `.git` and source vanished under a live build. The commit survives in the shared object store; recreate from the SHA. |
| **Kill orphan `solc`/`forge` from a dead agent before re-dispatching.** | A killed agent leaves solc at 100% CPU writing into a worktree; a new build collides on `out/`. |
| **Liveness = ps + git evidence, never transcript silence.** | A foreground via_ir build goes quiet for 10-20 min; the transcript only flushes on the agent's next action. Silence ≠ stall — check for live `solc`/`rustc` and moving refs. |
| **`--no-verify` ONLY for known pre-existing hook reds** (name them). Never `--force` to main. | Pre-push clippy/forge gates red on failures untouched by your work; bypass only those, documented. |
| **On an entangled conflict in money/margin/guest code: ABORT that branch and report — do not guess.** | "Keep both" is safe for disjoint hunks; guessing on margin logic ships a silent bug. |
| **Re-resolve every SHA right before landing it.** Survey SHAs go stale: rev-parse the branch's home checkout (and other sessions' scratchpad worktrees) again at land time; land the newest clean-tree commit. | A concurrent session amended/advanced `libmerge` after the survey; the lander nearly pushed the stale SHA and dropped the finished work. |

## Fan-out prompt shape (per branch subagent)

- Its own worktree; the branch's SHA; the current `origin/main` to rebase onto.
- "Build FOREGROUND, wait for exit; do NOT background or rely on a monitor."
- "Rebase onto `origin/main`; keep-both on disjoint hunks; ABORT + report on entangled margin/guest conflicts."
- "Build + run the touched tests green BEFORE push; `git fetch` then push `HEAD:main`; re-rebase on race."
- "Never touch the live checkout; land committed commits only, leave dirty files."

## Red flags — stop

- An agent's final message is "compiling / waiting for the monitor / I'll wait for the build" → it backgrounded and died. Verify on disk (`origin/main` sha, `git branch`), kill orphans, re-dispatch foreground.
- `origin/main` unchanged after a "completed" consolidation → nothing pushed. Re-derive ground truth before trusting any report.
- Two agents pushing main at once → serialize.

## Done means

`git ls-remote --heads origin` shows only `main` (+ intended pins), `git worktree list` has no parked feature worktrees, the final tip builds green, and any size cap is measured and under limit. Merging is not deploying — deploy blockers (e.g. vkey reproof) are tracked separately.
