---
name: max-audit-loop
description: Use to run a full security audit of a smart-contract + zk-guest codebase the way Max's deep audits run — optionally benchmarked against a named auditor's public findings (e.g. "audit against Quantstamp", "cross-map Trail of Bits / Spearbit / Cyfrin", "audit like you did"). Cross-maps an external finding standard onto the repo, deep-hunts protocol-specific surfaces, fans out specialist auditors, and false-positive-gates every finding before it ships. Triggers on "audit against <auditor>", "do the audit loop", "run max-audit-loop", "check if things they flag we flag too".
---

# The audit loop

One argument: the **benchmark source** — a named auditor whose public reports set the finding standard (`quantstamp`, `trail of bits`, `spearbit`, `cyfrin`, `code4rena`, `openzeppelin`, …), or `deep` / nothing for a protocol-specific hunt with no external checklist. The source only *seeds* the checklist; the real value is the deep hunt + the false-positive gate.

The orchestrator NEVER audits in the main chat — it dispatches. Every worker is READ-ONLY.

## Non-negotiables (pass to every subagent)

- **READ-ONLY on the target repo.** A live session usually owns it. NEVER write/edit/git-reset/commit/build inside the target tree. Workers output findings as text only. Scratch files go to the scratchpad dir, never the repo.
- **Sample `git rev-parse HEAD` at the start and end of every worker pass.** A moving HEAD is itself a finding — record it. Audit a stated commit.
- **A cited line is not a read line.** Re-derive every claim at source; never inherit another agent's citation as evidence.
- **Honest severity, no overclaim.** Downgrade your own leads the moment a neutralizing invariant appears (a good lead chased to Low is a win, not a loss). Report UNVERIFIABLE honestly.
- **Toolchain reality.** Static tools (Slither/Aderyn) often can't compile a modern toolchain (transient-storage opcodes, osaka evm, pinned solc). If they fail, say so and rely on the manual + specialist passes — do NOT silently drop the coverage.
- **Brevity.** Max has AuDHD — one line per finding, file:line, cut hard. This binds every worker.

## Phase 0 — scope

Read the repo: `ls src/ prover/`, find the contracts and the zk guest (often `prover/program` + `prover/<engine>/src`). Identify the proof-verification entry (`verifyProof` / `applyState`), the money-movement verbs, the margin/settlement model, the trust boundaries (owner, keeper, curator, oracle). Read `audit/`, `KNOWN-ISSUES*.md`, `THREAT-MODEL.md` if present — you must know what the team ALREADY flagged, so a "gap" is a real gap.

## Phase 1 — benchmark checklist (skip if source = deep)

Dispatch one research agent: pull the named auditor's PUBLIC reports (their certificate site, PDFs, GitHub, blog), prioritizing the closest protocol type to the target (for a clearing/margin/perp venue: Marginly, DerivaDEX, GMX, SynFutures, dYdX, Perpetual). Extract 30–70 concrete, checkable finding PATTERNS (`- [ ] Q-xx <one-line> — severity — which report`), not vague categories. Cover access-control/centralization, oracle staleness/manipulation, ERC20 quirks, reentrancy, EIP-712/replay, MEV/slippage, integer/rounding, DoS/griefing, upgradeability, pause/emergency, events/validation, and the protocol-specific class (liquidation-drain, max-heap order, funding/mark gaming, socialized-loss/ADL, cross-margin contagion, settlement-price gaming, RFQ quote-expiry/nonce/cancel). Write to scratchpad.

## Phase 2 — cross-map sweeps (parallel lenses)

Dispatch READ-ONLY lens agents over the repo, one per class, each tagging every hit `[KNOWN]` (already in the team's docs), `[NEW]` (real gap), or `[OK]` (defended, one line why). Give each lens the team's prior-findings list so it doesn't re-report known items. Lenses that map to the target: access-control/centralization, ERC20+oracle, reentrancy/CEI, signatures+rounding, derivatives-accounting (liquidation/leverage/heap/caps/shutdown), DoS+slippage+hygiene, input-validation+param-bounds. For systematic classes (missing events, missing zero-checks) ENUMERATE exhaustively (a setter matrix), don't sample. Then cross-reference the `[NEW]` items against the team's own audit docs + static baselines: which did they already document, which are genuinely missed?

## Phase 3 — deep protocol-specific rounds (the real value)

The benchmark finds the generic; the criticals are protocol-specific. One complex target per round, orchestrator-driven or via focused agents. For a zk-clearing venue, the crown jewels:
- **Guest↔chain trust boundary.** Does the chain bind EVERY public value it trusts? Is each committed root (scenario/registry/env) CONTENT-DERIVED from the same data that drives the computation, or echoed from unconstrained input? Is the input book CAS-bound to on-chain roots?
- **Per-op invariant completeness.** Does every state mutation re-establish the invariant (margin recompute on every position change) BEFORE the root advances? Gate-then-seat, or seat-then-check?
- **Freshness of what the gate reads.** Does a global freshness clock stand in for per-item freshness? (A fold can be fresh while one seat's leaf is stale — the mark-staleness class.)
- **Merkle/crank paths outside the proof.** Leaf binds type+index? Cursor prevents replay? Domain-separated leaf vs node?
- **Economic multi-step chains.** Novation/allocation coverage vs the ordinary-open gate (asymmetry = under-charge). Escape/withdraw vs closeout timing. Settlement-price selection determinism (cherry-pick).
- **Guest internals** (SP1): dispatch `sp1-guest-auditor` on the guest repo — public-values binding, per-op completeness, 32-bit truncation, determinism (no HashMap/float/rand/time), vkey pinning.

Record each round: the mechanism, the neutralizing invariant if any, and the residual. Chase every lead to VERIFIED / DOWNGRADED / KILLED.

## Phase 4 — specialist fan-out (verify, don't just find)

For each surviving candidate, run independent verification in parallel:
- `fp-check:exploitability-verifier` — TRUE/FALSE positive with attacker-control + math-bounds + race analysis and honest severity.
- `differential-review:adversarial-modeler` — the concrete exploit chain; walk EVERY on-chain escape and show it does/doesn't neutralize.
- `fp-check:poc-builder` — pseudocode + a unit-test sketch (map asserts to the repo's own shipped tests where possible) + a negative PoC (the precondition that flips it).
- A fresh bug-hunter on the surfaces the deep rounds under-covered.

A finding is confirmed only when ≥2 independent agents (each re-deriving) agree, plus a self-refutation it survives. Kill false positives before they reach the report.

## Phase 5 — false-positive gate + convergence

- Every candidate: try HARD to REFUTE it yourself (name the guard that would neutralize it). It STANDS only if you cannot break it — name the single load-bearing fact.
- Cold close for anything High/irreversible: a FRESH pair, cold context, prompted "this survived N rounds; assume a defect remains." (This is the `max-plan-itteration` loop — invoke it on the finding set.)
- Watchdog the workers: liveness = git/ps/output-mtime, never transcript silence; these passes run 4–14 min. A stalled agent (no output growth ~8 min) gets TaskStop + redispatch fresh — never fabricate its result.

## Phase 6 — deliverables

- **One report** (`<repo>-audit-report.md`): result table (severity × finding × status), a section per finding (mechanism + file:line + PoC status + one-line fix + severity rationale incl. threat-model dependence), a "verified SOUND" section naming every surface that held, the benchmark cross-map result ("do we flag what they flag"), and an honest tooling/coverage note.
- **A per-finding verification record** for each High (data-flow, exploitability, impact, PoC, devil's-advocate, gate review, verdict).
- Save a memory of the findings + fixes. Deliver the files; relay the headline (confirmed count by severity) in prose.

## Cadence notes

- If subagents hit a session/rate limit, do the work in-context yourself (own file reads still run) and fan out when the limit resets; note the deferral, don't skip.
- Scale rigor to the ask: "any bugs" → a few lenses + single-vote verify; "thorough audit" → full fan-out + adversarial multi-vote + cold close.
- The honest headline is often "well-built, N findings" — say that plainly. Finding nothing after a real hunt is a valid, reportable result.
