---
name: max-hard-audit
description: Use when a repo needs a hard audit run in rounds until Max says stop, with fixes built and pushed — "audit X hard", "keep auditing in loops", "audit + fix + push to main".
---

# max-hard-audit

One orchestrator; never audit in chat; everything is a subagent. Rounds of twenty read-only lenses under five orchestrators until Max says stop.

**Argument:** repo + scope ("contracts only" etc.). Solidity/zk: read `~/.claude/audit-kit/INDEX.md` first.

## Files (`~/crx-scratch/<topic>/` unless the path starts `~/`)

- `COMMON-rN.md`: ≤ 40-line round brief: target clone + sha, scope, lens rules, rulings list, live facts. A new file each round (one growing COMMON.md hit 390 KB on 09-19; no lens could paste it).
- `prior-findings.md`: every report ever, verbatim. Lenses dedup against ALL of it, KILLED included, or refuted findings resurrect.
- `rN/lenses/<nn>-<slug>.md` per lens; `rN/ORCH-<X>.md` per orchestrator.
- `iter/RULES.md`: verifier rules: ASSUME a claim is wrong and a defect missing; CONFIRMED / WRONG / UNVERIFIABLE with re-derived evidence; MISSED DEFECTS last; ≤ 90 lines; READ-ONLY; write early, append as you go (rate limits kill agents).
- `~/<repo>-audit-consolidated-<date>.md`: THE table. One fixer at a time; back up `.rN.bak` before each.
- `~/<repo>-audit-round*-records/`: archive.
- `solutions/`: patches + README per fix owner (chain / guest / keeper / ops / docs); `VERIFY-*.md` beside them.
- `PROGRESS.md`: the builder's, one timestamped line per step; others only read.
- Memory: one `project` file per audit + index line; update after every round, push, sheet, relaunch.

**Binding lens rules** (in COMMON; pasted into every lens prompt): READ-ONLY on the target (a live session may own it: no edit/build/commit/reset); `git rev-parse HEAD` at start + end (a moving HEAD is a finding); re-derive every cite at source (a cited line is not a read line); tag `[NEW]` / `[KNOWN]` / `[OK]`; ≤ 60 lines; one line per finding: `sev | tag | claim | file:line | load-bearing fact | fix`; brevity (Max has AuDHD).

## Loop

1. **Twenty lenses, five orchestrators.**
   - Unopened territories (grep prior lens titles + `ls r*/lenses`). A new tip is new territory: re-open a paid one only on code moved since its last read.
   - 5 themes × 4 (e.g. Solidity delta · storage/upgrade/wire · live probe + static tools · guest/prover · rulings/docs/ops truth).
   - 5 orchestrators in one message (general-purpose, opus, never fable). Each pastes COMMON into 4 lens prompts, launches them in one message (general-purpose; `sp1-guest-auditor` for zk guests), waits, writes `rN/ORCH-<X>.md` (≤ 20 lines), replies ≤ 5 lines. Never 20 flat agents from the chat (Max 09-22: "agents of agents, 20 in parallel is too much").
   - Lens prompt = COMMON + territory + what is KNOWN there + "write ONLY `rN/lenses/…`". No two lenses share a file set; each names ONE question answered by a defect or a named check.
   - Territories that paid: one lane read linearly end to end; guest↔chain↔keeper mirror parity; storage layout by hand-count; EIP-712 parity across repos; gates/allowlists; register vs tree; test truth (positive controls real?); deleted-guard forensics; live-state probes (cast, read-only); static tools on a scratch copy (slither/aderyn/semgrep, triaged vs the baseline); new code written tonight (adversarial); the plan/runbook as a security change; newest fix commits as fix-closure (CLOSED / PARTIAL / NEW-HOLE).
   - **Blind Watsons** once coverage saturates: 4 lenses barred from `prior-findings.md` and the table until their `## Dedup` section. Only KNOWN = coverage proof; `KNOWN-BUT-BURIED` = readability fix for the fixer; NEW = the prize. (Round 44 caught a register "Fixed" row that was not fixed.)
2. **Append** each report to `prior-findings.md` the moment it lands; archive it.
3. **Fixer** (one agent, one file) folds the round into the table: re-verifies each cite before writing, reports brief items FALSE at source, recounts by the table's stated rule with arithmetic. Never two fixers at once: gate the second on the file's mtime.
4. **Verifier pair** on the table every round: the warm pair attacks the fix pass (least-verified text) + a structural lens (premises, silences, interactions, rollback, worst-reader). Fresh agents each round; cross-verify from round 2.
5. **Cold close** any HIGH: fresh pair, cold context, "survived N rounds; assume a defect remains". Colds found real defects through round nine; continue until a full pair adds nothing of substance.
   - Off-tree facts decide severity. A cold that says "HIGH if the publisher does X" is not done: the same minute, a scout on the off-tree service (price publisher, Pyth calendar, fxempire page) + a LIVE read (WebFetch twice, cast). (Severity flipped twice in one hour on such facts.)
   - **MED cold sweep** before the audit (as on audit eve, rounds 40-45): one division, waves of 4, every OPEN money MED no cold has verified. (~40 % fell to LOW; the rest gained a USD figure; one, dust-leg IM release, became a lane-conditional HIGH over three cold rounds.)
6. **Solutions** in parallel: one designer per fix owner, patches on a scratch copy (`git apply --check` on a fresh clone; cargo in scratch only; NEVER solc/forge in the tree without Max's go). Two verifiers per patch set (adversarial + apply-check); a cold pair before anything ships.
7. **Decision sheets** (`max-decisions`, published to the hub) for every owner call: ≤ 12 decisions, money examples, one word each; ratifications in one row. Serve as soon as the first owner call appears (5–6 cards); add cards by republishing the same id, `data-d` stable. The fixer tags those rows OWNER-CALL with the card number.
8. **Design notes** per build lane → Max validates → build.

## Build (after "go")

- ONE builder, own clone in a worktree under `~/wt-<name>`, never the live tree; lanes fan out for code WRITING only. Lock file; a `PROGRESS.md` line per step; no Co-Authored-By; never `--force`.
- Pre-flight before any long build: forge/cargo/cargo prove versions, pinned rustc present. Short builds foreground; over ~10 min: background, read the log every 1–2 min. Forge builds follow `crx-deploy-speed`: one forge lock; solc-par splits one compile over 6 solc.
- Land lanes in dependency order. 0 `.orig`/`.rej` in any commit (grep case-insensitively: BSD patch prints lowercase "failed"). Re-run wire generators from the spec; regenerate fixtures with emitters; never hand-edit generated blocks or fixtures. Storage tail-append only; freed slots renamed in place; lens pins for every new slot.
- **Fidelity verify** each range before push, read-only: commit vs patch/note/ruling; trailers; strays; storage hand-count; wire copies; role gates; deleted selectors vs the ruled list. Verdict PUSHABLE / NOT YET.
- **Push incrementally** to main when Max rules so: forge green modulo the named pre-existing reds + cargo green on the range; fast-forward only; `PUSHED <sha> → origin/main` in PROGRESS.
- Re-stamp the table's auditor edition at each freeze sha (every cite re-derived at origin/main; no lane/scratchpad cites). Before ship: a verifier pair on it, then a cold on the delta. (VE-A/VE-B/VE-C found 13 + 9 wrong rows in an edition whose pins were all correct.)

## Running agents

- The Agent tool runs 20 live per session (nested counted) and queues the rest. Launch all orchestrators at once. Every response requests every item that does not wait on another's result; nothing else.
- The table lies about status: re-derive every OPEN HIGH on main before telling Max a number. (VB81 read "11 open HIGH"; two colds on origin/main found 10 fixed, 1 process-only.)
- Route each finding the minute it lands: code defects → builder/lane; doc defects → fixer; owner calls → next sheet.
- Liveness = file mtimes, `git log` in lane clones, `ps` for solc/cargo; never transcript silence. A 9-minute background sleep re-arms the pull; task output files stay 135 B until completion.
- Rate limits kill batches: when Max says the limit is back, relaunch every cut agent in RESUME mode from its on-disk state (clone, PROGRESS, partial report). Trust the disk, not the summary.
- Login cuts kill whole batches: relaunch the orchestrators in RESUME mode (lens files overwrite their header stubs). Tell every division to `sleep 120` and retry on the concurrency-cap error.
- Verifiers without the Write tool return text: save it yourself.
- Look-alike ids get misaddressed: keep a launch-order list of ids and roles.
- Foreign builds in other sessions' worktrees contend for CPU: report them to Max; never kill another session's process.
