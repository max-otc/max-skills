---
name: max-audit-loop
description: Use to run a full security audit of a smart-contract + zk-guest codebase the way Max's deep audits run, optionally benchmarked against a named auditor's public findings (e.g. "audit against Quantstamp", "cross-map Trail of Bits / Spearbit / Cyfrin", "audit like you did"). Triggers on "audit against <auditor>", "do the audit loop", "run max-audit-loop", "check if things they flag we flag too".
---

# max-audit-loop

**Argument:** the benchmark source: a named auditor whose public reports set the finding standard (`quantstamp`, `trail of bits`, `spearbit`, `cyfrin`, `code4rena`, `openzeppelin`, …), or `deep` / nothing for a protocol-specific hunt with no external checklist. It only seeds the checklist; the value is the deep hunt + the false-positive gate.

You dispatch; never audit in the main chat. Every worker is READ-ONLY.

## Non-negotiables (pass to every subagent)

- READ-ONLY on the target repo; a live session usually owns it. NEVER write, edit, git-reset, commit or build in its tree. Findings as text only; scratch files in the scratchpad dir, never the repo.
- Audit a stated commit. Sample `git rev-parse HEAD` at start and end of every pass; record a moving HEAD as a finding.
- A cited line is not a read line: re-derive every claim at source; never inherit another agent's citation as evidence.
- Honest severity, no overclaim: downgrade your own lead once a neutralizing invariant appears (a lead chased to Low is a win). Report UNVERIFIABLE honestly.
- Static tools (Slither/Aderyn) often cannot compile a modern toolchain (transient-storage opcodes, osaka evm, pinned solc). On failure, say so and rely on the manual + specialist passes; never drop the coverage silently.
- Brevity (Max has AuDHD): one line per finding, file:line, cut hard.

## Phase 0: scope

`ls src/ prover/`; find the contracts and the zk guest (often `prover/program` + `prover/<engine>/src`). Identify the proof-verification entry (`verifyProof` / `applyState`), money-movement verbs, margin/settlement model, trust boundaries (owner, keeper, curator, oracle). Read `audit/`, `KNOWN-ISSUES*.md`, `THREAT-MODEL.md` if present: you must know what the team ALREADY flagged, so a gap is a real gap.

## Phase 1: benchmark checklist (skip for `deep`)

One research agent reads the auditor's PUBLIC reports (certificate site, PDFs, GitHub, blog), nearest protocol type to the target first (for a clearing/margin/perp venue: Marginly, DerivaDEX, GMX, SynFutures, dYdX, Perpetual). It writes to the scratchpad 30–70 concrete, checkable finding PATTERNS, not vague categories: `- [ ] Q-xx <one-line> — severity — which report`. Cover access-control/centralization, oracle staleness/manipulation, ERC20 quirks, reentrancy, EIP-712/replay, MEV/slippage, integer/rounding, DoS/griefing, upgradeability, pause/emergency, events/validation, and the protocol-specific class (liquidation-drain, max-heap order, funding/mark gaming, socialized-loss/ADL, cross-margin contagion, settlement-price gaming, RFQ quote-expiry/nonce/cancel).

## Phase 2: cross-map sweeps

Parallel READ-ONLY lenses, one per class, each given the team's prior-findings list so it does not re-report known items. Tag every hit `[KNOWN]` (in the team's docs), `[NEW]` (real gap), `[OK]` (defended; one line why). Lenses that map to the target: access-control/centralization, ERC20+oracle, reentrancy/CEI, signatures+rounding, derivatives-accounting (liquidation/leverage/heap/caps/shutdown), DoS+slippage+hygiene, input-validation+param-bounds. Systematic classes (missing events, missing zero-checks): ENUMERATE exhaustively as a setter matrix; never sample. Then check each `[NEW]` against the team's own audit docs + static baselines: documented, or genuinely missed?

## Phase 3: deep protocol-specific rounds

The benchmark finds the generic; the criticals are protocol-specific. One complex target per round, orchestrator-driven or via focused agents. Crown jewels for a zk-clearing venue:

- **Guest↔chain trust boundary.** Chain binds EVERY public value it trusts? Each committed root (scenario/registry/env) CONTENT-DERIVED from the same data that drives the computation, or echoed from unconstrained input? Input book CAS-bound to on-chain roots?
- **Per-op invariant completeness.** Every state mutation re-establishes the invariant (margin recompute on every position change) BEFORE the root advances? Gate-then-seat, or seat-then-check?
- **Freshness of what the gate reads.** A global freshness clock standing in for per-item freshness? (A fold fresh while one seat's leaf is stale: the mark-staleness class.)
- **Merkle/crank paths outside the proof.** Leaf binds type+index? Cursor prevents replay? Leaf vs node domain-separated?
- **Economic multi-step chains.** Novation/allocation coverage vs the ordinary-open gate (asymmetry = under-charge). Escape/withdraw vs closeout timing. Settlement-price selection determinism (cherry-pick).
- **Guest internals (SP1).** Dispatch `sp1-guest-auditor` on the guest repo: public-values binding, per-op completeness, 32-bit truncation, determinism (no HashMap/float/rand/time), vkey pinning.

Record per round: mechanism, neutralizing invariant if any, residual. Chase every lead to VERIFIED / DOWNGRADED / KILLED.

## Phase 4: specialist verification

Per surviving candidate, in parallel:
- `fp-check:exploitability-verifier`: TRUE/FALSE positive; attacker-control, math-bounds and race analysis; honest severity.
- `differential-review:adversarial-modeler`: the concrete exploit chain; walk EVERY on-chain escape and show whether it neutralizes.
- `fp-check:poc-builder`: pseudocode, a unit-test sketch (asserts mapped to the repo's own shipped tests where possible), a negative PoC (the precondition that flips it).
- A fresh bug-hunter on surfaces the deep rounds under-covered.

Confirmed only when ≥ 2 independent agents, each re-deriving, agree and it survives a self-refutation. Kill false positives before the report.

## Phase 5: false-positive gate and convergence

- Try HARD to refute every candidate yourself: name the guard that would neutralize it. It stands only if you cannot break it; name the single load-bearing fact.
- High or irreversible: cold close: invoke the `max-plan-itteration` loop on the finding set (FRESH pair, cold context, prompted "this survived N rounds; assume a defect remains").
- Watchdog: liveness = git/ps/output mtime, never transcript silence; passes run 4–14 min. A stalled agent (no output growth ~8 min) gets TaskStop + a fresh redispatch. Never fabricate its result.

## Phase 6: deliverables

- One report, `<repo>-audit-report.md`: result table (severity × finding × status); a section per finding: mechanism, file:line, PoC status, one-line fix, severity rationale incl. threat-model dependence; a "verified SOUND" section naming every surface that held; the benchmark cross-map ("do we flag what they flag"); an honest tooling/coverage note.
- Per High: a verification record (data-flow, exploitability, impact, PoC, devil's-advocate, gate review, verdict).
- Save a memory of findings + fixes. Deliver the files; relay the headline (confirmed count by severity) in prose.

## Scale and limits

- Scale rigor to the ask: "any bugs" → a few lenses + single-vote verify; "thorough audit" → full fan-out + adversarial multi-vote + cold close.
- Subagents hit a session/rate limit: do the work in-context yourself (own file reads still run), fan out when it resets, note the deferral; never skip.
- The honest headline is often "well-built, N findings"; say it plainly. Nothing found after a real hunt is a valid, reportable result.
