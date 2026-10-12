---
name: max-plan-itteration
description: Use when a plan, report, audit finding, scout inventory, or agent-produced doc contains factual claims that will drive decisions or shipping — before trusting it, before building on it, or when the user says "verify", "check this", "is this true", "gate it".
---

# max-plan-itteration

Fresh adversarial pairs verify every claim until a full round adds nothing. A verifier that trusts the artifact, or its own earlier CLEAN, is not verifying.

## Loop

1. Dispatch 2 fresh verifiers in ONE message, distinct lenses split by domain (e.g. on-chain vs guest/system; or claims vs premises). Both READ-ONLY: no writes, no fixes, no builds beyond what re-derivation needs.
2. From round 2, cross-verify: each gets the other's findings and attacks them: confirm, refute or sharpen. Aim at least one verifier at a PREMISE of the artifact, not only at the last round's additions.
3. Between rounds a dedicated FIXER subagent applies the consolidated fix list. It re-verifies every cite at source before writing it. A brief item false at source: it writes the code-true version and reports the deviation. Warm continuation (SendMessage to the same agents) is fine for iterating fixes.
4. Converge only on a full round where BOTH add nothing new. Not convergence: finding-rate decay in warm agents; a zero-wrong-facts round (findings shift to silences and interactions; run the late-round lenses first).
5. Cold close for audited, irreversible or money-adjacent work: after warm convergence, a FRESH pair, cold context, full scope, prompted "this survived N rounds; assume a defect remains." Close only after a full round where both add nothing of substance. Cold pair finds nothing: done. It finds things: iterate warm, close cold again.

## Verifier brief

- "ASSUME at least one claim is wrong and at least one defect is missing; hunt until found or exhausted."
- Every claim: **CONFIRMED / WRONG / UNVERIFIABLE**, with independently re-derived evidence (file:line, command output). WRONG states the correct fact. UNVERIFIABLE is reported honestly, never as CONFIRMED.
- Re-read every cited line; the artifact's own citation is not evidence. (Inherited mis-citations survived 19 rounds.)
- Verify the system, not the process: re-run the check yourself. A builder's word or green transcript is not evidence.
- Re-probe chain/VPS facts first-hand; never inherit another agent's probe.
- Hunt body/sheet mismatches (owner decisions deferred in prose vs sheet rows).
- End with **MISSED DEFECTS**: what the artifact should say but doesn't.

## Lens rotation (newest text = least verified)

- **R1–2:** repo-truth (re-derive every cite) vs premises.
- **R3+:** attack last round's fixes hardest.
- **Mid:** territory nobody touched: first-hand chain probes (cast/RPC), ssh to boxes, external web (official docs), files no verifier opened (gate scripts, deploy manifests, untracked docs, foundry.toml).
- **Late** (cheap findings gone): the doc's silences; interaction war-games (pairs of steps × concurrent actors/sessions); rollback audit (do the named rollbacks restore state?); worst-reader test (the persona who reads only one section); pre-flight "would the owner call any ruled outcome wrong?"
- Every layer a claim crosses gets its own verification: a guest or fold layer can invert a passing arm-level check. (Frozen-seat exit "verified" at ArmLib died two rounds later on guest NOT_WHITELISTED.)

## Orchestrator rules

- If a live session shares the repo: sample git state at the start and end of every agent pass; a moving HEAD is a finding; record it.
- Dedup against everything seen, not only confirmed findings; else refuted findings reappear and the loop never converges.
- Probe-heavy briefs must say "keep individual ssh/RPC commands short-timeout".
- Re-ask "is the search complete?"; it has found a new candidate every time.
- Verifier conflict: resolve by a third derivation at source (usually the next fixer, on-chain or in-repo). Never by authority or recency.
- Liveness = git/ps evidence, never transcript silence; a dead subagent's parent fabricates results. Read-only verifiers leave no write evidence: watchdog on runtime norms (these lenses run 4–14 min). Transcript stubs flush only at completion; stub mtime is not a stall.
- A subagent dead on an API error or stream stall: redispatch fresh; trust nothing partial.
- Cites inside the artifact use anchors, never line numbers (default since 2026-09-13). Rules and traps: `anchors.md` in this skill's dir (not the spec of record `anchors-spec.md`). Read it before any cite work or the cite gate; pass it to every fixer and verifier on any artifact with cites, the conversion round included.
- Each decision the doc defers to the owner in prose gets a lettered sheet row (A/B + one-word rec), one ruling per row, answerable as "1A 2B". A body/sheet mismatch is a defect the verifiers must hunt.

## Red flags: the round is invalid; redispatch that verifier fresh

- Only CONFIRMEDs on a first pass ("looks right overall").
- A resumed agent re-blessing its own earlier CLEAN as the closing gate.
- Verdicts citing the artifact's own citations, not re-derived evidence.
- "Both agents agree" while one report is pending.
- A verifier that edited files.

## Code phase (after the plan converges)

- Same loop on code: builders (cap 3) in isolated worktrees → 2 fresh verifiers per round, distinct lenses → fixer → repeat to a clean round → cold close before merge/push.
- Verifiers re-run the tests in the merged tree. Pair a plan-fidelity lens (diff vs the converged plan, byte-level where the plan carries code) with an adversarial lens (edge inputs, revert paths, gas/size limits).
- Every fix and guard needs a positive control: flip the condition, watch the test go red, flip it back. A suite that cannot fail proves nothing.
- Builders pre-flight the toolchain before long work (forge/cargo --version + one trivial compile). Short builds foreground; over ~10 min: background, read the log every 1–2 min. Edits first, full build last (builds outlast watchdogs).
- Cold close = 2 fresh agents, own worktrees, full re-run, "assume a defect remains". Both clean: merge to the live branch, push, delete branch + worktrees in one motion.
- Deploy stays outside the loop: only on the owner's explicit go, per the deploy-gate discipline.
