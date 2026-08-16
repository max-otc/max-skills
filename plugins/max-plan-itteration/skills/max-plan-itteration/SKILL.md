---
name: max-plan-itteration
description: Use when a plan, report, audit finding, scout inventory, or agent-produced doc contains factual claims that will drive decisions or shipping — before trusting it, before building on it, or when the user says "verify", "check this", "is this true", "gate it".
---

# Verifying claims

## Overview

Claims are verified by fresh adversarial pairs until a full round adds nothing. A verifier that trusts the artifact, or its own prior CLEAN, is not verifying.

## The loop

1. **Dispatch 2 fresh verifiers in parallel, in ONE message** — distinct lenses (split by domain: e.g. on-chain vs guest/system; or claims vs premises). Both READ-ONLY: no writes, no fixes, no builds beyond what re-derivation needs.
2. **Prompt shape (each verifier):**
   - "ASSUME at least one claim is wrong and at least one defect is missing — hunt until found or exhausted."
   - Every claim gets a verdict: **CONFIRMED / WRONG / UNVERIFIABLE**, each with independently re-derived evidence (file:line, command output). Never accept the artifact's own citation as evidence — re-read the cited line.
   - For WRONG: state the correct fact.
   - End with a **MISSED DEFECTS** section: what the artifact should say but doesn't.
3. **Cross-verify from round 2:** each agent receives the OTHER's findings and attacks them — confirm, refute, or sharpen. Point at least one verifier at a PREMISE of the artifact, not only at what the last round added.
4. **Fix the artifact between rounds** — a dedicated FIXER subagent applies the consolidated fix list. The fixer re-verifies every cite at source before writing it, and must REPORT any brief item that turns out false (write the code-true version, flag the deviation). Warm continuation (SendMessage to the same agents) is fine for iterating fixes.
5. **Converge:** done only when a full round where BOTH agents add nothing new. Finding-rate decay in warm agents is NOT convergence. A zero-wrong-facts round is NOT convergence either — findings then shift from facts to silences/interactions; run the structural lenses (below) before declaring done.
6. **Cold close for high stakes** (audited, irreversible, money-adjacent): after warm convergence, dispatch a FRESH pair, cold context, full scope, prompted "this survived N rounds; assume a defect remains." Only after a full round where both agents add nothing of substance. If the cold pair finds nothing, done. If it finds things, iterate warm, close cold again.

## Lens rotation across rounds (newest = least verified)

- **R1-2:** repo-truth (re-derive every cite) vs premises.
- **R3+:** attack the FIXES from the last round hardest — a fix pass is the least-verified text in the doc.
- **Mid rounds:** territory nobody touched — first-hand chain probes (cast/RPC), ssh to boxes, external web (official docs), files no verifier opened (gate scripts, deploy manifests, untracked docs, foundry.toml).
- **Late rounds** (cheap findings gone, think structurally): the doc's SILENCES; interaction war-games (pairs of steps × concurrent actors/sessions); rollback audit (do the named rollbacks actually restore state?); worst-reader test (the persona who reads only one section); "would the owner call any ruled outcome wrong" pre-flight.
- **Every layer a claim crosses gets its own verification** — an arm-level check that passes can be inverted by the guest/fold layer (real case: frozen-seat exit "verified" at ArmLib, killed by guest NOT_WHITELISTED two rounds later).

## Rules that close known holes

- **Verify the system, not the process** — a verifier re-runs the check itself; the builder's word (or a green transcript) is not evidence.
- **Dedup against everything seen**, not against confirmed findings — else refuted findings reappear each round and the loop never converges.
- **A cited line is not a read line** — mis-citations have survived 19 rounds because every agent inherited the citation.
- **Ask "is the search complete?" again** — it has found a new candidate every time it was re-asked.
- **Agent liveness = git/ps evidence**, never transcript silence; a dead subagent's parent fabricates results.
- Report UNVERIFIABLE honestly — an unverifiable claim is not a confirmed one.
- **Verifier conflict** (two agents assert different facts): resolve by a third derivation at source — usually the next fixer re-derives on-chain/in-repo. Never pick by authority or recency.

## Live-environment rules

- If a live session shares the repo: sample git state at start AND end of every agent pass; a moving HEAD is a finding, record it.
- Verifiers re-probe chain/VPS facts FIRST-HAND — never inherit another agent's probe as evidence.
- Read-only verifiers leave no write-evidence; watchdog on runtime norms instead (these lenses run 4-14 min). Transcript stubs flush only at completion — stub mtime ≠ stall.
- Subagent dead on API error or stream stall: redispatch FRESH, trust nothing partial. Probe-heavy prompts must say "keep individual ssh/RPC commands short-timeout".

## Decision-sheet coupling

- Every decision the doc defers to the owner in prose gets a lettered sheet row (A/B + one-word rec), one ruling per row, answerable as "1A 2B". A body/sheet mismatch is a defect the verifiers must hunt.

## Red flags — the round is invalid

- A verifier returned only CONFIRMEDs on its first pass ("looks right overall")
- A resumed agent re-blessing its own earlier CLEAN as the closing gate
- Verdicts citing the artifact's own citations instead of re-derived evidence
- "Both agents agree" declared while one report is still pending
- A verifier that edited files

**Any of these: redispatch that verifier fresh.**

## Implementation phase (after the plan converges)

- The same loop runs on CODE: builder subagent(s) implement in isolated worktrees (cap 3) → 2 fresh verifiers per round, distinct lenses → fixer → repeat until a clean round → cold close BEFORE merge/push.
- Verifier evidence changes medium, not shape: a verifier RE-RUNS the build and the tests itself in its own worktree — a green transcript from the builder is not evidence. Plan-fidelity lens (diff vs the converged plan, byte-level where the plan carries code) pairs with an adversarial lens (break it: edge inputs, revert paths, gas/size limits).
- Every fix and every guard needs a POSITIVE CONTROL: flip the condition, watch the test go red, flip it back. A suite that cannot fail proves nothing (negatives lie).
- Builders pre-flight the toolchain before long work (forge/cargo --version + one trivial compile); builds run foreground; edits FIRST, full build LAST (builds outlast watchdogs).
- Cold close = 2 fresh agents, own worktrees, full re-run, prompted "assume a defect remains". Only after both come back clean: merge to the live branch, push, delete branch + worktrees in one motion.
- Deploy stays outside the loop: it fires only on the owner's explicit go, per the deploy-gate discipline.
