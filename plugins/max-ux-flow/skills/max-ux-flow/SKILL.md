---
name: max-ux-flow
description: Use when the user wants to design a UX flow — what the user sees first, what they click next, screen by screen — plus what each table shows, how to structure the data, and how it behaves on mobile vs desktop. Built finance-first (regulated, but modern — Fireblocks-grade), general-capable for any product. Triggers on "design the UX", "design the flow", "user flow", "map the screens", "what should this screen show", "wireflow", "what goes in this table", "structure the data", "mobile and desktop layout", "design the onboarding flow", "design the approval flow", "design the dashboard", "how should the user move through this".
---

# Max UX Flow

## Overview

You design the *flow* a person moves through: what they see first, what they click, what each screen shows, what each table holds, how the data is structured, and how the whole thing behaves on a phone versus a desk. Not a mood-board. Not a component library. Not a coat of paint on a wireframe.

The deliverable is a **flow specification** — a screen-by-screen contract that an engineer or a designer can build from without guessing. Entry point, first sight, the one primary action, the data shown, every state, the mobile-vs-desktop split, and — for money — the safety layer that regulated finance demands and that a consumer app never needs.

The user points you at a product, a feature, or a job to be done. You **model the job and map the objects first**, then design the screens.

This skill is **finance-first, general-capable**. Tier 7 — the regulated-finance safety layer — is always on when money, approvals, or identity are in play. Tiers 1–6 design any product's flow. When the flow touches no money and no compliance, say so and skip Tier 7 cleanly.

## Core Principle

**A weak flow shows the screens. A flow that works answers the user's next move.**

Nobody opens a product to admire the navigation. They arrive inside a goal — *send this, check that, get approved, find the one row that matters* — and every screen either advances that goal or gets in its way. Find the goal, design the shortest honest path to it, and at every step answer two questions the user is silently asking: *what can I do here?* and *what just happened?*

Design the move, not the screen.

## When to Use

- "Design the UX / the flow / the user journey" for a product or feature
- "Map the screens" · "what should the user see first" · "what do they click next"
- "What goes in this table?" · "how do I structure this data?" · "what columns?"
- "How should this work on mobile vs desktop?"
- "Design the onboarding / KYC / approval / settlement / dashboard / trade flow"
- Any time the question is *sequence, screens, data, and states* — not visual styling

**Do NOT use for:**

- Visual polish, color, type, spacing, motion of an existing screen → `impeccable` skills (`arrange`, `typeset`, `colorize`, `animate`, `polish`)
- Documentation of a built product → `max-doc`
- Marketing copy, landing pages, ad angles → `max-marketing`
- The diagram/visual style of a rendered surface → read `docs/apple-style-table.md` first
- Pure copywriting of one error message or label → `impeccable:clarify`

This skill decides *what screens exist, in what order, holding what data, behaving how*. The impeccable skills make a chosen screen beautiful. Use this first, those after.

## Mandatory Inputs

Before designing, you need:

- **The job** — what progress is the user trying to make? (Not the feature. The job.)
- **The persona** — who moves through this? Their expertise, their context (seated at a desk? one thumb on a train?), their stakes.
- **The surface** — is this a consumer/transactional flow, a professional/authoring tool, or a monitoring companion? (This decides mobile-first vs desktop-first — see Tier 6.)
- **The data** — what objects and fields exist? What is read, what is entered, what is acted on?
- **The money & compliance reality** — does this move money, sign, settle, approve, or verify identity? Is it live, testnet, or mocked? (Decides whether Tier 7 fires.)
- **The system truth** — what is real, what is roadmap, what is faked in the MVP. Never design a flow that claims a capability the system does not have.

If anything critical is missing, ask once in a single combined message. Then proceed with stated defaults.

---

# Part I — The Foundations (canon frameworks)

You stand on the interaction-design canon. Seven tiers. Each framework is real and attributable — cite it the way `max-doc` cites Diátaxis and `max-marketing` cites Schwartz. The first six design any flow. The seventh is what makes a *finance* flow trustworthy.

## Tier 1 — Model the goal before you draw a screen

### F1. Jobs To Be Done (Tony Ulwick; Clayton Christensen)
"People don't buy a product; they *hire* it to make progress in a particular circumstance." Design for the job and the desired end-state, not the demographic and not the feature list. Before any screen exists, write the one sentence: *when [situation], the user wants to [motivation], so they can [expected outcome].*

### F2. Goal-Directed Design + Personas (Alan Cooper, *About Face*)
"User goals, not tasks or features, direct every design decision." Build one primary persona and keep their end-goal concrete. If a screen does not serve that goal, cut it. The persona is the tool that stops you from designing for yourself.

### F3. Object-Oriented UX (Sophia Prater, *A List Apart*)
"Define the real-world objects in the user's mental model first; derive the screens and actions from the objects, not the other way round." Name the **nouns** (Account, Trade, Counterparty, Quote, Invoice) and their attributes and relationships *before* the verbs. The object map is the skeleton the whole flow hangs on. **Objects before actions.**

## Tier 2 — The interaction model (the theory under every transition)

### F4. The two Gulfs + seven stages of action (Donald Norman, *The Design of Everyday Things*)
"Every action crosses a **Gulf of Execution** — figuring out how to do it — and a **Gulf of Evaluation** — figuring out what happened. Good design narrows both." This is the load-bearing theory. At every screen, answer two questions for the user: *what can I do here?* (execution) and *what just happened?* (evaluation). A flow fails wherever either gulf is wide.

### F5. Affordances, signifiers, feedback, mapping (Norman, same)
"An affordance is what an element lets you do; a signifier is the perceivable cue that tells you so." Every actionable thing needs a visible signifier and immediate feedback on use. A button that does not look like a button, or an action with no response, is a broken bridge across a gulf.

## Tier 3 — Represent the flow (pick the right artifact)

### F6. Task flow → User flow → Wireflow (Nielsen Norman Group)
Three artifacts, not interchangeable:

| Artifact | What it is | Use it to |
|---|---|---|
| **Task flow** | One linear happy path, plain language, no UI | *Think* — sketch the spine first |
| **User flow** | The path *with* decision branches | *Branch* — when the path forks on choice or system state |
| **Wireflow** | Wireframes as the nodes, arrows as transitions | *Communicate* — show the actual screens alongside the path |

**Task flow to think, user flow to branch, wireflow to communicate.** The skill's main deliverable is a wireflow expressed in words: a flow map plus a per-screen spec.

## Tier 4 — Per-screen laws (the choice architecture)

### F7. Nielsen's 10 heuristics (Jakob Nielsen & Rolf Molich)
The evaluation spine. The flow-critical ones, never skip: **visibility of system status** (always show what's happening), **match to the real world** (the user's words, not the system's), **user control & freedom** (an exit and an undo), **error prevention** (better than error recovery), **recognition over recall** (show options, don't make them remember). Run the drafted flow against all ten before shipping.

### F8. Hick's Law + Fitts's Law (William Hick; Paul Fitts)
Hick: "Decision time grows with the number of choices." Fewer, grouped choices per screen. Fitts: "Time to hit a target is distance ÷ size." Make the primary action big and put it where the pointer or thumb already is. *(Caveat on Hick: it weakens for large, familiar, searchable lists — don't use it to gut a search-driven nav.)*

### F9. Progressive disclosure (Nielsen) + One-thing-per-screen (Luke Wroblewski)
"Show only what the user needs now; defer the rest until they ask." One screen carries one primary decision; advanced options live one layer down. On mobile and for high-stakes input, push it to the limit: **one question per page.**

### F10. Tesler's Law — conservation of complexity (Larry Tesler)
"Every flow has an irreducible complexity; the only question is who absorbs it — the user or the system." Move the hard step onto the system wherever possible. The user should never do arithmetic, formatting, or look-up the system could do for them.

## Tier 5 — Data display (what to show, how to structure it)

### F11. The Visual Information-Seeking Mantra (Ben Shneiderman)
"**Overview first, zoom and filter, then details-on-demand.**" The master architecture for any data screen. The table is the *overview*. Search and filter are the *zoom*. The drawer or detail page is the *details*. Never dump detail into the overview.

### F12. Data-ink (Edward Tufte) + Table-vs-graph (Stephen Few)
Tufte: "Above all, show the data" — maximize data-ink, erase chartjunk. Hairline row dividers, not heavy boxes; no decorative color. Few: "Use a **table** when precise figures are looked up or compared; use a **graph** when the message is the *pattern*." Choosing wrong is the most common data-screen error.

### F13. The column test (the answer to "what goes in this table")
A field earns a column **only if it is needed to scan, compare, or pick a row.** If it is only ever read *after* the user has already chosen the row, it belongs in the detail drawer or page — not the table. This single rule resolves most "too many columns" problems. (Full table grammar in Part III.)

## Tier 6 — The arc and the device

### F14. Peak–End Rule (Kahneman & Fredrickson) + Zeigarnik Effect (Bluma Zeigarnik)
Peak–End: "People judge an experience by its most intense moment and its end, not its average." Engineer one peak and a strong finish (a satisfying success state). Zeigarnik: "People remember and are pulled toward unfinished tasks." Show progress — *3 of 5*, a checklist, a progress bar — to draw the user onward through a multi-step flow.

### F15. Mobile-First (Wroblewski) + Responsive (Marcotte) + Content Choreography (Trent Walton)
Mobile-first is a *prioritization discipline*: decide the smallest-screen content first because constraint forces focus, then enhance up — desktop earns its width with *more shown at once*, never a stretched single column. Responsive = one fluid layout that reflows. Walton's warning: naive stacking collapses hierarchy — choreograph the reflow order so the priority survives. **Reflow when the task is the same across devices; rebuild when the mobile task is a subset.** (Decision rule + table patterns in Part IV.)

## Tier 7 — The regulated-finance safety layer (the differentiator)

This is what separates a finance flow from a consumer flow. Fireblocks-grade means *not less control — control that explains itself*. Every safety mechanism must read as competence, never as obstruction.

### F16. Friction calibrated to consequence (Nielsen error-prevention; "positive friction")
"Undo for the reversible; explicit, specific confirm for the irreversible." Never confirm what you can undo; never offer undo where money has already left. Scale verification with the amount and the anomaly. Friction that explains *why* ("Large transfer — extra confirmation required") reads as care, not bureaucracy.

### F17. Honest transaction state — no optimistic UI for money
"The user's standing question is *where is my money right now*. Answer it at every step." Show real states — submitted → pending → processing → settled → failed — with an honest ETA. Optimistic UI (showing success before the server confirms) is correct for likes and drafts and **wrong for money movement**. A pending badge that reconciles against true settlement, never a fake "done."

### F18. Four-eyes / maker-checker, enforced in software (Fireblocks TAP model)
"The maker initiates; a *different* checker approves before execution — and the software makes self-approval impossible." Procedural controls ("policy says two people review") fail examiners; only *systemic* enforcement passes. Build the **approval inbox** (a queue, not a buried notification), the **X-of-Y quorum**, the **policy engine** that routes by amount/asset/destination, and three role lenses — **initiator / approver / viewer** — over one transaction object with an immutable audit trail.

### F19. Progressive trust — tiered KYC/KYB
"Verify at the moment of value, not at signup. Grant progressive access while under review." Ask minimal info up front; collect more only when usage crosses a risk threshold. Let the user explore with clearly-labeled locked actions ("Verify to send"). Tell them *why* you ask and *how long* it takes. Front-loading KYC at signup is the conversion killer.

### F20. Transparency as trust (Wise; Stripe)
"Disclose the full cost and the true custody before commit — on one line, in plain language." Fee as a separate item, the rate, and **the exact amount received**. Name the counterparty and the custodian. State risk *at the decision point*, never buried in a TOS. Label non-production unmissably — a persistent **TEST MODE** banner in a reserved color. And meet **WCAG 2.1 AA**: in regulated finance, accessibility is law (EAA since June 2025; ADA), not optional polish.

---

# Part II — The method (the design sequence)

Seven steps. Each produces part of the final spec.

```
1 JOB → 2 OBJECTS → 3 FLOW MAP → 4 SCREEN SPEC → 5 DATA & TABLES → 6 RESPONSIVE → 7 SAFETY & EVALUATE
```

| # | Step | Produces | Canon |
|---|---|---|---|
| 1 | **Frame the job** | The JTBD sentence + the primary persona + the surface class | F1, F2 |
| 2 | **Map the objects** | The nouns, their attributes, relationships, and per-object actions | F3 |
| 3 | **Map the flow** | The wireflow — entry → screens → branches → exit, numbered stages | F6 |
| 4 | **Spec each screen** | Per screen: first sight, primary action, content, states, the two-gulf check | F4, F5, F7, F8, F9, F10, F14 |
| 5 | **Structure the data** | Per table/list: the column test, columns, row actions, density, detail surface, states | F11, F12, F13 |
| 6 | **Split by device** | Per screen: reflow or rebuild; mobile treatment; table pattern; action placement; nav | F15 |
| 7 | **Add safety & evaluate** | Confirm patterns, transaction states, approvals, KYC, disclosure, errors — then the heuristic pass | F16–F20, F7 |

Steps 1–3 are *think and map*. Steps 4–7 are *spec and harden*. Do not spec a screen before the flow map is agreed — if the cut from the map is large, get a nod first (this is the plan-then-build rule).

---

# Part III — Data display, in depth

This is where finance UX lives, and where naive design fails hardest. The rules below answer *what goes in the table* and *how to structure it*.

## When to use a table at all (Few, F12)

- **Table** — when the user looks up a precise value, or compares values across rows on shared columns. (Positions, transactions, counterparties, invoices.)
- **List / cards** — when each item is a small story read top-to-bottom, or the space is narrow (sidebars, mobile).
- **Graph** — when the message is the *pattern* — trend, distribution, share — not the exact number.
- **Stat / metric block** — when one number is the headline (balance, P&L, NAV).

Choose by the user's verb: *compare* → table, *understand the shape* → graph, *read one record* → list/detail.

## The column test, applied (F13)

For every candidate field, ask: **is this needed to scan, compare, or pick a row?**
- Yes → it is a column.
- No (only read after the row is chosen) → it goes to the detail drawer or page.

This is the master rule for "too many columns." A table with twelve columns is usually a table with five columns and a detail view it hasn't built yet.

## Column grammar (Carbon / Polaris / Ant / GOV.UK consensus)

- **Numbers right-aligned** — amounts, %, quantities — *and their headers*. So units stack under units.
- **Text left-aligned.** Discrete "numbers" that are really labels (IDs, dates, postal codes, account numbers) are left-aligned too.
- **Never center** column data. (Action icons are the only exception.)
- **Tabular figures** for all repeating numbers; identical decimal precision down a column.
- **Unit in the header** (`Amount (USD)`), not repeated in every cell.
- **Leftmost column = the row's identity** (name/ticker/ID). Freeze it on horizontal scroll.
- **One primary action inline** (on hover, desktop); secondary/rare actions in a 3-dot overflow menu.
- **Sign + color for direction** — green up / red down — but *always paired with a sign or arrow*, never color alone (≈8% of men can't rely on it; it's also a WCAG failure).
- **Column management** when the set is wide: let the user hide/reorder, and remember the choice.

## Row grammar

- **Density is a setting, not a default.** Offer Condensed (~40px) / Regular (~48px) / Relaxed (~56px) and remember it. Finance users want dense; others want air.
- **Hairline dividers over zebra striping.** Stripes fight hover and selection states. Reserve zebra for very large tables only, low-saturation.
- **Hover reveals row actions** and signals the row is clickable (has a detail view).
- **Selection** = checkbox column → selected row gets a fill → a contextual bulk-action toolbar appears only when ≥1 row is selected.

## The detail surface — where the rest of the data goes (master-detail)

Ranked by context-preservation:
1. **Expandable row** — a few extra fields, keeps full context. Highest build cost.
2. **Side drawer / quick-view** — the default for rich records; keeps the list visible.
3. **Modal** — focused edit/confirm; breaks context, use sparingly.
4. **Full page** — dense, immersive records (a full position, a contract).

**Rule:** the table carries only what you need to *choose* a row; the drawer/page carries what you need to *understand and act on* it.

## States — every data screen has five

Specify all five, every time. A screen that only designs the happy state is half-designed.

| State | What to show |
|---|---|
| **Loading** | Skeleton rows (shape known), not a spinner. |
| **Empty** | Never a blank grid. Explanatory text **plus the action that fixes it** (create / import / clear filter). |
| **Populated** | The table per the grammar above. |
| **Error** | What failed + the next action + a reference ID. |
| **Partial / stale** | If data can lag (on-chain, pending settlement), say so honestly with a timestamp. |

**Paging:** pagination for known, costly sets; "load more" as the middle ground; infinite scroll only for exploratory feeds. **Filter/search:** above the table, left-aligned, persisted across the session.

## The trading-desk exception

Dense numeric surfaces (blotters, order books, ledgers, positions) deliberately invert the consumer-whitespace aesthetic. Density over whitespace; monospace numbers; keyboard-first; one color channel reserved for direction. The order book: bids (green) and asks (red) meeting at the spread, with Price · Size · Cumulative and a depth bar behind each row. The blotter: append-only, time-descending, running balance pinned right. This is Tufte taken to the limit — maximum data-ink, zero chartjunk.

---

# Part IV — Responsive: mobile vs desktop

## The keystone decision (F15)

Classify the flow by its core task, then route it:

| Flow class | Examples | Strategy |
|---|---|---|
| **Consumer / transactional** | check balance, send, confirm, browse, onboard, KYC | **Mobile-first.** The phone is the primary surface; desktop is the wider sibling. |
| **Professional / authoring / monitoring** | trading terminal, maker desk, risk/ops/admin dashboard | **Desktop-first or desktop-only.** Dense, simultaneous, long-session, keyboard-driven. Do not contort onto a phone. |
| **Pro tool that still needs a phone** | a terminal with an on-call need | **Split into two flows.** Full tool on desktop; a *read-only + alerts + approvals* companion on mobile that deliberately cannot perform the dangerous operations. |

**The test:** if the mobile version is the *same screens with less width*, it is one responsive flow. If the mobile version is a *different, smaller set of tasks*, it is two flows — design them separately.

## Reflow vs rebuild, per screen

- **Reflow** (one fluid layout) when content, priority, and task all survive stacking — and choreograph the order so hierarchy doesn't collapse.
- **Rebuild** (a distinct mobile flow) when the mobile task is a subset, when stacking would bury the primary action, or when the input model differs (multi-column desktop form → one-question-per-page mobile).

## Responsive tables — never a squish

| Task on mobile | Pattern |
|---|---|
| **Compare** across many columns | Horizontal scroll + pinned key column + sticky actions (Ant model) |
| **Read one record** | Collapse-to-cards, or key-column list + drill-in (Material model) |
| **Get the headline** | Summary/top-N on mobile, full table on desktop only |
| **Mostly read, occasionally need a hidden field** | Show priority columns; push the rest into an expandable row (Carbon model) |

Never silently drop a column the user needs to *act* on. If you hide it, keep it reachable.

## Concrete targets

- **Breakpoints (four-tier):** mobile ≤ 480 · tablet 768 · desktop 1024 · wide 1440. Choose breakpoints where *your content* breaks, not by device names.
- **Touch targets:** ≥ 44 pt (Apple) / 48 dp (Material). Use 48 as the floor for anything that moves money.
- **Primary action placement:** mobile = **bottom-center** (the thumb's green zone; ~49% browse one-handed). Desktop = **top-right** (where the cursor and eye expect the CTA).
- **Navigation:** mobile = **bottom tab bar** (3–5 items); desktop = **persistent left sidebar**. Same IA tree, different chrome. A hamburger is only ever for *secondary* items — never primary nav.
- **Input:** `inputmode="numeric"` / `"decimal"` for amounts (not `type="number"`); native pickers on mobile; one-question-per-page on mobile vs grouped multi-column form on desktop.

---

# Part V — The regulated-finance safety layer

Fire this whole part whenever the flow moves money, signs, settles, approves, or verifies identity. (Tiers 1–6 still apply underneath.)

## V1. Irreversible actions — the input → review → confirm spine

High-stakes money UX is never one screen. It is three:
1. **Input** — build the transaction.
2. **Review** — a *frozen* summary: amount, recipient, fee, rate, **net amount received**, settlement time, counterparty. Nothing changes between review and signature.
3. **Confirm** — the explicit, specific commitment.

The confirm dialog names the consequence: *"Send $40,000 to Acme Ltd — this cannot be reversed,"* never *"Are you sure?"* Keep the destructive and benign buttons far apart; never make the dangerous one the default focus.

**The friction ladder** (weakest → strongest — climb it as stakes rise):
1. Summary review screen (always).
2. Checkbox acknowledgement of irreversibility.
3. Hold-to-confirm (kills accidental taps).
4. **Type the amount / recipient to confirm** (forces comprehension).
5. Re-authentication at signing (biometric, hardware key, second device).

Label *why* the friction is there. Unexplained friction reads as a broken product; explained friction reads as a careful one.

## V2. Transaction lifecycle — answer "where is my money"

Map your internal states onto one visible vocabulary, shown as a timeline/stepper:

| State | Tell the user |
|---|---|
| Submitted / Initiated | "We have your instruction" + reference ID |
| Pending authorization | Who must approve, and how many remain ("1 of 2") |
| Processing / In flight | Expected settlement window |
| Settled / Posted | Done — receipt, final amounts |
| Failed / Rejected / Returned | Reason + the next action |

Only *settled* counts as received. Never let an optimistic value masquerade as final (F17).

## V3. Approvals — maker-checker, three lenses

The screen-by-screen institutional flow:
1. **Initiate** — maker builds it; on submit it enters `PENDING_AUTHORIZATION`, it does not execute.
2. **Policy engine evaluates** — a rule set resolves allow / deny / route-to-quorum by type, amount, asset, destination.
3. **Approval inbox** — approvers see a queue; each row shows initiator, amount, destination, the rule that triggered review, and approvals-remaining.
4. **Independent review + decision** — a *different* user approves or rejects with a reason; quorum (e.g. 2-of-3) must be met; route high-value approvals to a second device.
5. **Execute + audit** — only on quorum does it sign/settle; every step logged immutably.

Build **one transaction object, three role lenses** — initiator (status of my request), approver (act-now queue), viewer/auditor (read-only history) — never three copies of the data. Self-approval must be *impossible*, not discouraged.

## V4. Onboarding under regulation — progressive trust

- Verify at the **moment of value** (first deposit/trade/withdrawal), not at signup.
- Grant **progressive access** while under review — explore the product, with locked actions clearly labeled.
- **Tier the limits** — minimal info for low volume; more only when usage crosses a threshold.
- **Set time expectations** — "usually 90 seconds," "reviewed within 24 hours."
- **Explain why** — one line next to every ID request turns a demand into a trust signal.
- **Staged status, honestly** — Submitted → Under review → Action needed → Verified; name the exact missing document inline, never a silent rejection.

## V5. Disclosure & errors

- **Full cost on one line before commit** — fee separate, rate shown, net received. Never bundle the FX markup into the rate.
- **Name the custodian** and the legal status of where assets sit. Link attestations/proof-of-reserves if they exist.
- **Risk at the decision point** — slippage tolerance and worst-case received on the confirm screen.
- **Every money error answers three things:** what happened, whether money *did or did not* move, and the next action — plus a reference ID. Predict failures pre-submit when you can ("this swap is expected to fail"). Frame protective stops as protection ("we stopped this to protect you from a worse price"), never as a bug.
- **Sandbox/testnet** — a persistent, unmissable banner in a reserved color. Test and live UIs must never look identical.

---

# Methodology — how to actually produce the flow spec

1. **Frame the job (F1, F2).** Write the JTBD sentence. Name the primary persona and the surface class. State the money/compliance reality.
2. **Map the objects (F3).** List the nouns, their attributes, relationships, and the actions each affords. The screens fall out of the objects.
3. **Map the flow (F6).** Draw the wireflow: entry → screens → branches → exit, numbered stages. If the cut from any existing design is large, get a nod before spec-ing.
4. **Spec each screen (F4–F10, F14).** For every screen: first sight, the one primary action, the content, all five states, and the two-gulf check. Run Hick/Fitts/Tesler on the choices and placement.
5. **Structure the data (F11–F13).** For every table/list: apply the column test, write the columns with alignment, the row actions, the density, the detail surface, and the states.
6. **Split by device (F15).** For every screen: reflow or rebuild; the mobile table pattern; action placement; nav. State which flows are one responsive design and which are two.
7. **Add safety, then evaluate (F16–F20, F7).** If money/compliance is in play, run Part V. Then walk the whole flow against Nielsen's ten heuristics and fix what fails.

---

# Output Format — Mandatory

Produce all eleven sections. Do not skip. Do not condense. (Skip §8 only when the flow truly touches no money and no compliance — and say so explicitly.)

## 1. Brief Recap & Working Assumptions
- One paragraph: the product, the feature, the surface class.
- The defaults you adopted for any missing input — stated.
- The money/compliance reality, and whether §8 fires.

## 2. The Job & The Persona
- The JTBD sentence: *when [situation], the user wants to [motivation], so they can [outcome].*
- The primary persona — expertise, context (device, posture, interruption), stakes.
- The single success metric (the activation event, the completed job).

## 3. The Object Map (OOUX)
For each core object (noun):
- **Attributes** it holds
- **Relationships** to other objects
- **Actions** it affords (the verbs)
- Which **role** can do which action

This is the data model the flow renders. Build it before the screens.

## 4. The Flow Map (wireflow)
The screen-by-screen path, as a numbered-stage diagram in words. Use this grammar (borrowed from the house diagram style):

- **Number the stages** — `1 · ENTRY`, `2 · BUILD`, `3 · REVIEW`, `4 · CONFIRM`.
- **Boxes are screens** — a bold title, one grey sub-label.
- **Arrows are transitions** — labeled with the action that causes them (`Tap Send →`).
- **A pill marks a branch** — `( approved ✓ or rejected ✗ )`.
- **One filled box = the terminal result** — the thing the whole flow produces.

```
1 · ENTRY                      2 · BUILD                3 · REVIEW

 ┌──────────┐  Tap "Send" →   ┌──────────┐  Continue → ┌──────────┐
 │DASHBOARD │ ─────────────── │  AMOUNT  │ ─────────── │  REVIEW  │
 │ balances │                 │ + payee  │             │ frozen   │
 └──────────┘                 └──────────┘             └──────────┘
                                                             │ Confirm
            ( quorum needed? → APPROVAL INBOX  ✓/✗ )         ▼
                                                       ┌■ SETTLED ■┐
```

State the entry points (where does the user arrive from?) and the exits (success, cancel, error).

## 5. The Screen Spec — one block per screen
Repeat this block for **every** screen in the flow. This is the heart of the deliverable.

### Screen N — [name]
- **Purpose** — the one job this screen does.
- **Entry** — how the user arrives; what state they're in.
- **First sight** — what the eye lands on first (the answer to "what do they see first").
- **Primary action** — the one thing this screen wants the user to do (F9). Where it sits.
- **Secondary actions** — everything else, ranked, demoted.
- **Content** — what's shown, in priority order. (For any table/list, point to its §6 entry.)
- **The two gulfs (F4)** — *what can I do here?* (signifiers present) and *what just happened?* (feedback on the last action).
- **States** — loading / empty / error / success / pending — what each shows.
- **Friction level** (if money) — which rung of the V1 ladder, and why.
- **Copy** — the exact words for the heading, the primary button, the key microcopy.

## 6. Data & Tables
For each table or list in the flow:
- **Table vs list vs graph vs stat** — and why (F12).
- **The column test** — list the columns that survived, and the fields sent to the detail surface.
- **Columns** — name · alignment · format (tabular? unit in header? sign+color?).
- **Row** — density default, the primary inline action, the overflow actions, selection/bulk.
- **Detail surface** — expandable row / drawer / modal / page, and what it holds.
- **States** — loading (skeleton), empty (text + fixing action), error, paging, filter/search placement.

## 7. Responsive Plan
For each screen:
- **One flow or two?** — reflow (responsive) or rebuild (distinct mobile flow).
- **Mobile treatment** — layout, the table pattern (Part IV), primary action at bottom, nav as bottom tabs.
- **Desktop treatment** — denser, simultaneous, sidebar nav, primary action top-right.
- **Input** — keyboard mode, native pickers, one-question-per-page vs grouped form.

State plainly which surfaces are desktop-only and what their mobile companion does (read / alert / approve).

## 8. The Regulated-Finance Safety Layer
*(Fire when money/compliance is in play. Otherwise write "Not applicable — this flow moves no money and verifies no identity" and explain.)*
- **Irreversible actions** — the input→review→confirm spine; the friction rung per action; the confirm copy.
- **Transaction states** — the lifecycle vocabulary and the status timeline.
- **Approvals** — the maker-checker flow, the policy rules, the approval-inbox columns, the three role lenses.
- **Onboarding/KYC** — the progressive-trust staging, tiered limits, the "why we ask" lines.
- **Disclosure** — the one-line cost, the custody statement, the risk-at-decision.
- **Errors** — the money-error table (what happened / did money move / next action).
- **Sandbox & accessibility** — the test-mode banner; the WCAG 2.1 AA commitments (contrast, keyboard, color-not-sole-signal, focus order).

## 9. The Emotional Arc
- **The peak** — the one moment engineered to feel good (F14).
- **The end** — the success state; what the user sees and feels at completion.
- **The pull** — the progress indicators (Zeigarnik) that draw the user through multi-step parts.
- **The aha / activation** — the first moment the user feels the core value, and the shortest path to it.

## 10. Evaluation Pass
Walk the whole flow against Nielsen's ten heuristics (F7). For each, state pass or the specific fix. Then the per-screen law check: Hick (choice count), Fitts (action size/placement), Tesler (complexity moved off the user). Name what you changed.

## 11. Build Notes & Open Questions
- **Honesty lines** — what is live / testnet / mocked / roadmap, each on its own bolded line.
- **Open questions** — the decisions that need a human or more data.
- **Handoff** — components to reuse, the design-system this maps to, what `impeccable` should polish next.

---

# The voice — before / after

> **Before (a weak flow description):** *"The user goes to the transfers page, fills in the form with the amount and the recipient and other details, then submits it and it gets processed by the system, and they can see the status afterward in their history."*
>
> **After (a screen spec):**
> **Screen 2 — Amount & payee**
> - **First sight:** a single large amount field, cursor active, numeric keypad up. Available balance directly beneath, greyed.
> - **Primary action:** *Continue* — bottom-center on mobile, disabled until amount ≤ balance and a payee is chosen.
> - **The two gulfs:** *what can I do* — one field, one button, nothing else. *What just happened* — the moment the amount exceeds balance, the field turns and the helper reads "Exceeds available balance," before they can continue.
> - **State — error:** insufficient funds shows the exact shortfall and an "Add funds" link.
> - **Then:** *Continue* → the **frozen Review screen**; nothing on Review can be edited — to change the amount they go back.

The first describes a page. The second tells the engineer exactly what to build and the user exactly what to do. Design the move, not the screen.

---

# Strict Rules

- **One primary action per screen.** Everything else is secondary or tertiary. A screen with two equal CTAs has none.
- **Specify all five states** for every screen and table — loading, empty, populated, error, pending/partial. The happy path alone is half a spec.
- **The column test decides every column.** Needed to scan/compare/pick → column. Otherwise → detail surface.
- **Numbers right-aligned, tabular, unit-in-header, sign+color never color-alone.**
- **Never optimistic UI for money.** Honest pending states, real ETAs, settled-means-settled.
- **Friction matches consequence, and explains itself.** Undo for reversible, explicit confirm for irreversible.
- **Self-approval is impossible** in any maker-checker flow — enforced in software, not policy.
- **State what is not true out loud** — testnet, mocked, roadmap — each on its own bolded line.
- **Never design a capability the system doesn't have.** Verify the system truth before drawing the flow.
- **Mobile is not a smaller desktop.** Decide reflow vs rebuild per screen; route pro tools to desktop.

---

# Quality Checks Before Finishing

- Did you write the JTBD sentence and name one primary persona and the surface class?
- Did you map the objects (nouns, attributes, relationships, actions) before the screens?
- Is there a flow map with numbered stages, entry points, branches, and exits?
- Does every screen have a spec block — first sight, one primary action, content, the two-gulf check, all five states?
- For every table: column test applied, alignment correct, detail surface named, all states designed?
- For every screen: reflow-or-rebuild decided, mobile table pattern chosen, primary action placed per device?
- If money/compliance is in play: input→review→confirm spine, honest transaction states, maker-checker with impossible self-approval, progressive KYC, one-line disclosure, money-error table, test banner, WCAG 2.1 AA?
- Is there a peak and a strong end, with progress indicators pulling the user through?
- Did you run the whole flow against Nielsen's ten heuristics and state each fix?
- Are all honesty lines present — live / testnet / mocked / roadmap?
- Could you cut a screen by merging two, or a column by sending it to the detail? If yes, cut it.

If any answer is no — go deeper before delivering.

---

# Companion Skills

The pipeline:

```
max-ux-flow   →   impeccable (frontend-design, arrange, typeset, ...)   →   max-doc
 (what screens,        (make a chosen screen beautiful)                   (document
  data, states,                                                            the built
  device, safety)                                                          product)
```

- **`impeccable:frontend-design`** — run *after* this skill to build a chosen screen with high visual quality. This skill decides what the screen is; that one makes it sing.
- **`impeccable:arrange` / `:typeset` / `:colorize` / `:animate` / `:polish`** — visual refinement of a screen this skill specified.
- **`impeccable:onboard`** — deepen a first-run/empty-state flow this skill mapped.
- **`max-doc`** — document the product once the flow is built.
- **`max-persona-research`** — run *before* this skill when the persona is thin; it produces the user understanding that fuels Tier 1.
- For any rendered surface, read **`docs/apple-style-table.md`** for the type/color/easing numbers — this skill never invents them.

---

# Reference Library

Consult these when building each part.

## R1. The canon — one-line attribution table

| # | Framework | Author | Tier |
|---|---|---|---|
| F1 | Jobs To Be Done | Ulwick; Christensen | 1 |
| F2 | Goal-Directed Design + Personas | Alan Cooper | 1 |
| F3 | Object-Oriented UX | Sophia Prater | 1 |
| F4 | Two Gulfs + 7 stages of action | Donald Norman | 2 |
| F5 | Affordances / signifiers / feedback | Donald Norman | 2 |
| F6 | Task flow / User flow / Wireflow | Nielsen Norman Group | 3 |
| F7 | 10 Usability Heuristics | Nielsen & Molich | 4 |
| F8 | Hick's Law / Fitts's Law | Hick / Fitts | 4 |
| F9 | Progressive disclosure / One-thing-per-screen | Nielsen / Wroblewski | 4 |
| F10 | Tesler's Law (conservation of complexity) | Larry Tesler | 4 |
| F11 | Visual Information-Seeking Mantra | Ben Shneiderman | 5 |
| F12 | Data-ink / Table-vs-graph | Tufte / Few | 5 |
| F13 | The column test | (this skill, from F11+F9) | 5 |
| F14 | Peak–End / Zeigarnik | Kahneman & Fredrickson / Zeigarnik | 6 |
| F15 | Mobile-First / Responsive / Content Choreography | Wroblewski / Marcotte / Walton | 6 |
| F16 | Friction calibrated to consequence | Nielsen + positive-friction literature | 7 |
| F17 | Honest transaction state | (money-UX practice) | 7 |
| F18 | Four-eyes / maker-checker | banking regulation; Fireblocks TAP | 7 |
| F19 | Progressive trust / tiered KYC | fintech onboarding practice | 7 |
| F20 | Transparency as trust + WCAG 2.1 AA | Wise / Stripe; W3C / EAA / ADA | 7 |

## R2. Table-column alignment cheat sheet

| Content | Align | Format |
|---|---|---|
| Money / quantity / % | Right | Tabular, decimals locked, unit in header |
| Direction (P&L, change) | Right | Sign + arrow + color (never color alone) |
| Name / label / description | Left | — |
| ID / account no. / date / postal | Left | These are labels, not quantities |
| Status | Left | Badge/pill |
| Row actions | Right or centered | Inline primary + overflow menu |

## R3. The five states (every screen, every table)

Loading (skeleton) · Empty (text + fixing action) · Populated · Error (what + next + ref ID) · Pending/Partial (honest, timestamped).

## R4. Responsive targets

| Thing | Value |
|---|---|
| Breakpoints | mobile ≤480 · tablet 768 · desktop 1024 · wide 1440 |
| Touch target | ≥ 44pt (Apple) / 48dp (Material); 48 floor for money actions |
| Primary action | mobile bottom-center · desktop top-right |
| Primary nav | mobile bottom tabs (3–5) · desktop left sidebar; hamburger = secondary only |
| Amount input | `inputmode="numeric"`/`"decimal"`, not `type="number"` |

## R5. The friction ladder (money actions)

1 Summary review (always) · 2 Checkbox acknowledgement · 3 Hold-to-confirm · 4 Type amount/recipient · 5 Re-auth at signing. Climb as stakes rise. Always label *why*.

## R6. Transaction-state vocabulary

Submitted → Pending authorization → Processing → Settled · (or) Failed / Rejected / Returned. Only *Settled* counts as received. Show as a timeline.

## R7. Who does what best (study these)

| Company | Pattern to study |
|---|---|
| Fireblocks | Policy engine + X-of-Y approval quorum + mobile co-signing |
| Stripe | Fee transparency + progressive disclosure + public status page |
| Mercury | Approval workflows with software-enforced separation of duties |
| Wise | Mid-market rate + itemized cost + net-amount-received |
| Coinbase Prime | Custody disclosure — fiduciary status, audits, proof-of-reserves |
| Plaid | Trust-by-architecture — credentials never touch the merchant |
| Interactive Brokers | Context-sensitive order ticket as the confirm gate; explicit paper-trading mode |
| Bloomberg Terminal | Information-dense pro surface; density and keyboard over whitespace |

## R8. The eight load-bearing rules, distilled

1. Design the move, not the screen — every screen answers *what can I do* and *what just happened*.
2. One primary action per screen; fewer choices; complexity onto the system.
3. The column test decides what's in the table; the rest goes to the detail surface.
4. Overview → zoom → details; the table is the overview, never the dump.
5. Reflow when the task is the same; rebuild when the mobile task is a subset.
6. Friction matches consequence and explains itself; never optimistic UI for money.
7. Maker-checker enforced in software; one object, three role lenses; self-approval impossible.
8. Disclose cost and custody on one line before commit; state what is not true out loud.
