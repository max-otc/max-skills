---
name: max-merge
description: Use when several branches, worktrees, or clones of one repo must be consolidated into a single clean main — "merge everything", "land all the branches", "one clean main", "consolidate the worktrees", "merge all outstanding work", "collapse the branches", zero parked branches — especially with a concurrent live session committing in the same tree.
---

# max-merge

Consolidate every branch, worktree and clone of one repo into one clean main, around the agents live in it. Subagents hand-pick and rebase each branch; one pusher pushes serially.

## Steps

0. **Roll call.** `ListAgents`. Ask the repo's pusher (ROUTES.tsv): "max-merge on <repo>: any push in flight, which trees are yours, are you the pusher?" Wait one survey-length. Silence is not consent for a tree with live evidence.
1. **Survey** (one read-only subagent): `git branch -vv`, `git worktree list`, clones under `~` and `~/Downloads`, each VPS (`ssh`, find `.git` dirs, match `origin`), other sessions' scratchpad worktrees (`find /private/tmp/claude-501 -maxdepth 4 -name .git`, rev-parse each HEAD), side branches (`git ls-remote --heads origin`). Per item: ahead/behind `origin/main`, dirty count, conflicts vs main, what it is. Sample the live checkout's HEAD + dirty at start and end; a moving HEAD is a finding.
2. **Classify** (below), E-active test first.
3. **Fan out** up to 10 subagents for independent branches, each in its own worktree. One build on the merged tree.
4. **Land** B first, C last, dependencies respected. Serial pushes, one pusher. Each next branch rebases onto the new tip.
5. **Prune** to one main, zero parked branches. Keep audit pins + the live checkout.
6. **Verify:** build the final `origin/main` tip; measure any size cap (EIP-170); only `main` + intended pins remain.

## Classes

- **A** on main (ancestor/merged): nothing to do.
- **B** clean (ahead, no conflict, coherent): rebase → build → push.
- **C** conflicts: rebase → resolve keep-both → build → verify → push.
- **D** do-not-merge: foreign branches (e.g. an outside contributor's port), old-commit audit pins, superseded doc branches. Leave or prune; never merge.
- **E-active**: an agent mid-work (moving HEAD, dirty files, running gates; full test below). Never commit its files; leave the tree.
- **F** finished handoff: another session's done, unpushed work (clean tree, gates green, agent idle/stopped), incl. unpushed amended commits and remote side branches of stopped sessions. Fetch the SHA into the primary clone at once (scratchpad GC risk), then land it as B. Clean tree + idle owner = F; ask the owner first when known.

**E-active test**, before any B/C/F. Peer sessions' subagents count, and so do your own still-writing builders and fixers. Any one makes a tree E-active, whatever its commits look like:
- a peer claims it (ask each busy peer from `ListAgents` which trees its subagents hold and whether it is already the pusher);
- a file mtime or reflog entry < 30 min old; `.git/index` or `.git/HEAD` moved < 15 min ago;
- a live process (`forge|solc|cargo|rustc|docker|git|claude`) with the path in its command line (`ps -axo pid,etime,command`) or as its cwd (`lsof -a -d cwd -p <pid>`);
- `rebase-merge`, `rebase-apply` or `MERGE_HEAD` present;
- HEAD or dirty count moved between survey start and end;
- a lock dir (e.g. `~/.forge-build.lock`) held by its owner.

Start landing without waiting for your own E-active subagent; never put a second writer in its tree.

**Maximum of each agent's work survives.** Two lanes on the same code: reconcile line by line, keep everything each side built, keep the whole coherent. Drop a hunk only when main carries an equivalent or newer form (cite the sha) or the owner ruled it out. An owner-ruled DELETE on main beats keep-both: grep the deleted names after the rebase; the result must be empty. "Too entangled" earns a dedicated line-by-line lane, never a drop.

**Entangled conflict in money, margin or guest code:** ABORT the branch and report; never guess (keep-both is safe only for disjoint hunks; a guess on margin logic ships a silent bug). After the serial lander finishes, each aborted branch gets a dedicated semantic-merge agent: it reads both sides, merges by meaning, runs the touched suites foreground, pushes. Not done while an abort has no lane.

**"Include all" means all.** When Max says include all or merge everything, every completed commit lands, whichever session made it: local branches, finished handoffs, remote side branches. Only exclusions, each named in the report with its reason: E-active, audit pins, `-parked` branches, entangled aborts. Never skip work because another session touched it.

## Non-negotiable rules (each earned by a real failure)

- One pusher per repo across all sessions, not per session. Find it at roll call; hand it SHAs. (Two sessions were ordered to merge one repo while a third was mid-land: two pushers race main and a re-rebase drops a peer's hunk.)
- `git fetch --prune` right before every push (peers push between your fetch and push); re-rebase if main moved. A fast-forward of your exact commit is fine; a divergence is not.
- A peer's word classifies its own trees; git evidence the rest. Ask the owner before landing its finished branch; re-ask right before the push (a survey SHA goes stale while the owner's subagent amends the branch).
- Re-resolve every SHA at land time (rev-parse the home checkout and other sessions' scratchpad worktrees); land the newest clean-tree commit. (`libmerge` advanced after the survey; its stale SHA nearly shipped.)
- `--no-verify` only for named, pre-existing hook reds your work did not touch. Never `--force` to main.
- Never touch the live tree: no `git add -A`, `reset` or `stash`. Commit only your own paths. (Committing everything snapshots a peer's half-finished refactor and pushes a red tree.)
- Build in worktrees under `~/wt-<name>`; recreate checkouts from SHAs. Other sessions' scratchpad worktrees get garbage-collected mid-task; commits survive in the shared object store.
- Short builds foreground. Builds over ~10 min: background, read the log every 1–2 min. (A backgrounded `forge build` agent exited "waiting for the monitor"; nothing landed.)
- Kill a dead agent's orphan `solc`/`forge` before re-dispatching (it holds 100 % CPU; a new build collides on `out/`).
- Before deleting a clone, grep cron, launchd, `~/bin` and env files for its path; idle tests miss scheduled readers. (2026-10-09: a clone idle 6 h fed the hourly gas top-up; its deletion failed the 23:09Z run.)
- Liveness = `ps` + git evidence, never transcript silence. A foreground via_ir build is quiet 10–20 min; the transcript flushes on the agent's next action. Check for live `solc`/`rustc` and moving refs.

## Other sessions pushing

- Several sessions told to push or merge one repo (e.g. Max broadcasts "merge"): agree on ONE pusher by message before any push. The others survey only, hand over the survey + SHAs rebased on the pusher's tip, and push nothing.
- A peer is the pusher, or answers "I am the pusher" / "X is the pusher": stop pushing; **prepare-and-hand-off**. Rebase each finished branch in your own worktree onto its tip; hand it the SHAs in order. Take the role only when the peer hands it over in words.
- `git fetch --prune` before and after a push. On a push race: re-rebase, re-gate, retry once. LANDING/LANDED messages only to sessions with a push in flight on that repo.

## Your own subagents in parallel (earned 2026-09-20, whole-book night)

- One writer per tree: lander, fixer and each verifier get their own worktree (`git worktree add`, then `rsync` the submodule dirs from the parent; new worktrees have empty submodules; never `git submodule update` in a linked worktree).
- A builder's sub-lanes never write in its tree: each takes its own worktree off the builder's tip and returns `git format-patch`; the builder applies serially. (2026-09-21: a sub-lane rewrote `var.rs` under the builder; an edit was lost.)
- Brief every subagent to end its progress file with `READY … <sha>`, `LANDING <sha>` or `LANDED <sha>`. Poll that line; never infer state from silence.
- Rebase in parallel, cherry-pick last: the lander branches from the fixer's last commit, rebases onto `origin/main` now, polls the fixer's `READY <sha>` line, cherry-picks only the new commits, re-gates, squashes, pushes.
- Rehearse the longest rebase early: the second lane rebases onto the first lane's branch tip while it gates, then replays onto `origin/main` once it lands.
- A cut subagent (rate limit, login switch): kill its orphan shells, relaunch from disk state (commits, dirty files via `git diff`, progress file). Never redo what `git log` shows landed.
- Owner says land now: verifiers may read on main; findings come back as follow-up commits. A red gate or an entangled money-file conflict still stops the push.
- `timeout` is `/opt/homebrew/bin/timeout` (coreutils). A SIGTERM'd cold forge build writes nothing. Under "no solc" orders the landing gate is cargo build + clippy + tests + doc gates; list forge legs OWED in the commit body; `--no-verify` for the hook's forge legs only.
- In a rebase `--ours` is upstream, `--theirs` your commit (reverse of a merge). Resolve by content; after each resolution re-run the count gate and grep for the lane's own rows.

## Fan-out brief (per branch subagent)

Own worktree, the branch SHA, the current `origin/main` to rebase onto. "Short builds foreground. Builds over ~10 min: background, read the log every 1–2 min." Keep-both on disjoint hunks; ABORT + report on entangled margin/guest conflicts. Build + touched tests green before push; `git fetch`, push `HEAD:main`, re-rebase on race. Never touch the live checkout; land committed commits only; leave dirty files. End the progress file with `READY`/`LANDING`/`LANDED <sha>`.

## Red flags: stop

- Final message "compiling" / "waiting for the monitor" / "I'll wait for the build": it backgrounded and died. Verify on disk (`origin/main` sha, `git branch`), kill orphans, re-dispatch.
- Two agents pushing main at once, or a peer answers "I am the pusher" / "X is the pusher": stop pushing; serialize or switch to prepare-and-hand-off.
- `origin/main` unchanged after a "completed" consolidation: nothing pushed. Re-derive ground truth before trusting any report.

## Done

`git ls-remote --heads origin` shows only `main` (+ intended pins); `git worktree list` has no parked feature worktrees; the final tip builds green; any size cap is measured and under; tell every peer session that answered roll call the final tip. Merging is not deploying: track deploy blockers (e.g. vkey reproof) separately.
