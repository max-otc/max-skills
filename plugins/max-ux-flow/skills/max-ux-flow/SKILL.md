---
name: max-ux-flow
description: Use when the user wants to design a UX flow — what the user sees first, what they click next, screen by screen — plus what each table shows, how to structure the data, and how it behaves on mobile vs desktop; any question about sequence, screens, data and states, not visual styling. Finance-first (regulated, but modern — Fireblocks-grade), general-capable for any product. Triggers on "design the UX", "design the flow", "user flow", "user journey", "map the screens", "what should the user see first", "what do they click next", "what should this screen show", "wireflow", "what goes in this table", "how do I structure this data?", "what columns", "structure the data", "mobile and desktop layout", "how should this work on mobile vs desktop", "design the onboarding flow", "design the approval flow", "design the dashboard", "design the onboarding / KYC / approval / settlement / dashboard / trade flow", "how should the user move through this".
---

# Max UX Flow

You design the *flow* a person moves through and deliver it as a **flow specification**: a screen-by-screen contract an engineer or designer builds from without guessing. Entry point, what they see first, what they click, the one primary action, what each table holds, how the data is structured, every state, phone vs desk and, for money, the safety layer regulated finance demands. Not a mood-board, a component library, or paint on a wireframe. **Model the job and map the objects first**, then design the screens.

Finance-first, general-capable. Tiers 1–6 design any product's flow. Tier 7, the regulated-finance safety layer, is always on when money, approvals or identity are in play. No money and no compliance: say so and skip Tier 7 cleanly.

## Core principle

**A weak flow shows the screens. A flow that works answers the user's next move. Design the move, not the screen.**

The user arrives inside a goal: *send this, check that, get approved, find the one row that matters*. Every screen advances that goal or blocks it. Design the shortest honest path to it. At every step answer the user's two silent questions: *what can I do here?* and *what just happened?*

## Not for, and the pipeline

- Visual polish, color, type, spacing, motion of an existing screen → `impeccable` skills (`arrange`, `typeset`, `colorize`, `animate`, `polish`).
- Copy for one error message or label → `impeccable:clarify`.
- Docs of a built product → `max-doc`.
- Marketing copy, landing pages, ad angles → `max-marketing`.
- Diagram or visual style of a rendered surface → read `docs/apple-style-table.md` first.

Pipeline: `max-persona-research` (before, when the persona is thin; feeds Tier 1) → **this skill** (*what screens exist, in what order, holding what data, behaving how*) → `impeccable:frontend-design` (build a chosen screen at high visual quality), then `:arrange` / `:typeset` / `:colorize` / `:animate` / `:polish` (refine it) and `impeccable:onboard` (deepen a first-run or empty-state flow mapped here) → `max-doc` (document the built product). Take the type, color and easing numbers for any rendered surface from `docs/apple-style-table.md`; this skill never invents them.

## Mandatory inputs

Before designing, you need:

- **The job**: the progress the user is trying to make. Not the feature.
- **The persona**: expertise, context (at a desk? one thumb on a train?), stakes.
- **The surface**: consumer/transactional, professional/authoring, or monitoring companion. It decides mobile-first vs desktop-first (Part IV).
- **The data**: which objects and fields exist; what is read, entered, acted on.
- **The money and compliance reality**: does it move money, sign, settle, approve or verify identity? Live, testnet or mocked? It decides whether Tier 7 fires.
- **The system truth**: what is real, what is roadmap, what the MVP fakes. Never design a flow that claims a capability the system lacks.

If anything critical is missing, ask via the max-ask skill (one sheet). Then proceed with stated defaults.

---

# Part I — The canon: seven tiers

Each framework is real and attributable — cite it the way `max-doc` cites Diátaxis and `max-marketing` cites Schwartz. Tiers 1–6 design any flow. Tier 7 makes a *finance* flow trustworthy. Tier 5 (F11–F13) opens Part III, F15 Part IV, Tier 7 (F16–F20) Part V.

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

## Tier 1 — Model the goal before you draw a screen

**F1. Jobs To Be Done** (Tony Ulwick; Clayton Christensen). "People don't buy a product; they *hire* it to make progress in a particular circumstance." Design for the job and its end-state, not the demographic or the feature list. Before any screen, write: *when [situation], the user wants to [motivation], so they can [expected outcome].*

**F2. Goal-Directed Design + Personas** (Alan Cooper, *About Face*). "User goals, not tasks or features, direct every design decision." Build one primary persona with a concrete end-goal; it stops you designing for yourself. Cut any screen that does not serve that goal.

**F3. Object-Oriented UX** (Sophia Prater, *A List Apart*). Define the real-world objects in the user's mental model first; derive screens and actions from the objects. Name the **nouns** (Account, Trade, Counterparty, Quote, Invoice), their attributes and relationships, before the verbs. **Objects before actions.**

## Tier 2 — The interaction model

**F4. The two Gulfs + seven stages of action** (Donald Norman, *The Design of Everyday Things*). The load-bearing theory. Every action crosses a **Gulf of Execution** (*what can I do here?*) and a **Gulf of Evaluation** (*what just happened?*). Answer both at every screen. A flow fails wherever either gulf is wide.

**F5. Affordances, signifiers, feedback, mapping** (Norman, same). An affordance is what an element lets you do; a signifier is the visible cue that says so. Every actionable thing needs a visible signifier and immediate feedback.

## Tier 3 — Represent the flow

**F6. Task flow → User flow → Wireflow** (Nielsen Norman Group). Three artifacts, not interchangeable:

| Artifact | What it is | Use it to |
|---|---|---|
| **Task flow** | One linear happy path, plain language, no UI | *Think*: sketch the spine first |
| **User flow** | The path *with* decision branches | *Branch*: the path forks on choice or system state |
| **Wireflow** | Wireframes as nodes, arrows as transitions | *Communicate*: the actual screens alongside the path |

Your main deliverable is a wireflow in words: a flow map plus a per-screen spec.

## Tier 4 — Per-screen laws

**F7. Nielsen's 10 heuristics** (Jakob Nielsen & Rolf Molich). The evaluation spine. Never skip the flow-critical five: **visibility of system status** (always show what is happening), **match to the real world** (the user's words, not the system's), **user control and freedom** (an exit and an undo), **error prevention** (beats error recovery), **recognition over recall** (show options).

**F8. Hick's Law + Fitts's Law** (William Hick; Paul Fitts). Hick: decision time grows with the number of choices; use fewer, grouped choices per screen. It weakens for large, familiar, searchable lists; do not use it to gut a search-driven nav. Fitts: time to hit a target is distance ÷ size; make the primary action big and put it where the pointer or thumb already is.

**F9. Progressive disclosure** (Nielsen) **+ One-thing-per-screen** (Luke Wroblewski). Show only what the user needs now; the rest waits until they ask. One screen, one primary decision; advanced options one layer down. On mobile and for high-stakes input: **one question per page.**

**F10. Tesler's Law, conservation of complexity** (Larry Tesler). Every flow has an irreducible complexity; the user or the system absorbs it. Move the hard step onto the system wherever possible. The user never does arithmetic, formatting or look-up the system could do.

## Tier 6 — The arc and the device

**F14. Peak–End Rule** (Kahneman & Fredrickson) **+ Zeigarnik Effect** (Bluma Zeigarnik). People judge an experience by its most intense moment and its end, not its average: engineer one peak and a strong finish (a satisfying success state). People remember and are pulled toward unfinished tasks: show progress (*3 of 5*, a checklist, a progress bar) through a multi-step flow.

---

# Part II — The method

| # | Step | Produces | Canon |
|---|---|---|---|
| 1 | **Frame the job** | The JTBD sentence, the primary persona, the surface class; state the money/compliance reality | F1, F2 |
| 2 | **Map the objects** | The nouns, their attributes, relationships and per-object actions. The screens fall out of the objects | F3 |
| 3 | **Map the flow** | The wireflow: entry → screens → branches → exit, numbered stages | F6 |
| 4 | **Spec each screen** | Per screen: first sight, the one primary action, content, all five states, the two-gulf check. Run Hick, Fitts and Tesler on choices and placement | F4, F5, F7, F8, F9, F10, F14 |
| 5 | **Structure the data** | Per table/list: the column test, columns with alignment, row actions, density, detail surface, states | F11, F12, F13 |
| 6 | **Split by device** | Per screen: reflow or rebuild; mobile table pattern; action placement; nav. State which flows are one responsive design and which are two | F15 |
| 7 | **Add safety & evaluate** | If money/compliance is in play, run Part V: confirm patterns, transaction states, approvals, KYC, disclosure, errors. Then walk the whole flow against Nielsen's ten heuristics and fix what fails | F16–F20, F7 |

Do not spec a screen before the flow map is agreed. If the map cuts deep into an existing design, get a nod before you spec (the plan-then-build rule).

---

# Part III — Data display (Tier 5)

**F11. The Visual Information-Seeking Mantra** (Ben Shneiderman). "**Overview first, zoom and filter, then details-on-demand.**" The master architecture for any data screen. The table is the *overview*. Search and filter are the *zoom*. The drawer or detail page holds the *details*. Never dump detail into the overview.

**F12. Data-ink** (Edward Tufte) **+ Table-vs-graph** (Stephen Few). Tufte: "Above all, show the data." Maximize data-ink, erase chartjunk: hairline row dividers, not heavy boxes; no decorative color. Few: pick table or graph by the list below. Choosing wrong is the most common data-screen error.

- **Table**: look up a precise value, or compare values across rows on shared columns (positions, transactions, counterparties, invoices).
- **List / cards**: each item is a small story read top to bottom, or the space is narrow (sidebars, mobile).
- **Graph**: the message is the pattern (trend, distribution, share), not the exact number.
- **Stat / metric block**: one number is the headline (balance, P&L, NAV).

*Compare* → table. *Understand the shape* → graph. *Read one record* → list/detail.

## F13. The column test (this skill's rule, from F11 + F9)

A field earns a column **only if it is needed to scan, compare, or pick a row.** A field read only after the row is chosen goes to the detail drawer or page. This is the master rule for "too many columns": a twelve-column table is usually a five-column table plus a detail view nobody built yet.

## Column grammar (Carbon / Polaris / Ant / GOV.UK consensus)

| Content | Align | Format |
|---|---|---|
| Money, quantity, % | Right, header too | Tabular figures for all repeating numbers; identical decimal precision down the column; unit in the header (`Amount (USD)`), not in every cell |
| Direction (P&L, change) | Right | Sign + arrow + color (sign or arrow at minimum; green up, red down). Never color alone: ≈8% of men cannot rely on it, and it fails WCAG |
| Name, label, description | Left | — |
| ID, account no., date, postal code | Left | Labels, not quantities |
| Status | Left | Badge/pill |
| Row actions | Right or centered | One primary action inline (on hover, desktop); secondary and rare actions in a 3-dot overflow menu |

- **Never center column data.** Action icons are the only exception.
- **Leftmost column = the row's identity** (name, ticker, ID). Freeze it on horizontal scroll.
- **Wide set:** let the user hide and reorder columns; remember the choice.

## Row grammar

- **Density is a setting, not a default.** Condensed (~40px) / Regular (~48px) / Relaxed (~56px); remember the choice. Finance users want dense; others want air.
- **Hairline dividers over zebra striping.** Stripes fight hover and selection states. Zebra only for very large tables, low-saturation.
- **Hover reveals row actions** and signals the row opens a detail view.
- **Selection:** checkbox column → the selected row gets a fill → a contextual bulk-action toolbar appears only when ≥1 row is selected.

## The detail surface (master-detail)

Ranked by context preservation:
1. **Expandable row**: a few extra fields; keeps full context; highest build cost.
2. **Side drawer / quick-view**: the default for rich records; the list stays visible.
3. **Modal**: focused edit or confirm; breaks context; use sparingly.
4. **Full page**: dense, immersive records (a full position, a contract).

The table carries only what the user needs to *choose* a row. The drawer or page carries what they need to *understand and act on* it.

## The five states (every screen, every table)

| State | Show |
|---|---|
| **Loading** | Skeleton rows (shape known), not a spinner |
| **Empty** | Never a blank grid. Explanatory text **plus the action that fixes it** (create / import / clear filter) |
| **Populated** | The table per the grammar above |
| **Error** | What failed + the next action + a reference ID |
| **Pending / partial / stale** | If data can lag (on-chain, pending settlement), say so honestly, with a timestamp |

**Paging:** pagination for known, costly sets; "load more" as the middle ground; infinite scroll only for exploratory feeds. **Filter and search:** above the table, left-aligned, persisted across the session.

## The trading-desk exception

Dense numeric surfaces (blotters, order books, ledgers, positions) invert the consumer-whitespace aesthetic: density over whitespace, monospace numbers, keyboard-first, one color channel reserved for direction, maximum data-ink, zero chartjunk. Order book: bids (green) and asks (red) meet at the spread; Price · Size · Cumulative, a depth bar behind each row. Blotter: append-only, time-descending, running balance pinned right.

---

# Part IV — Responsive: mobile vs desktop (F15, Tier 6)

**F15. Mobile-First** (Luke Wroblewski) **+ Responsive** (Marcotte) **+ Content Choreography** (Trent Walton). Mobile-first is a *prioritization discipline*: decide the smallest-screen content first, because constraint forces focus, then enhance up. Desktop earns its width by *showing more at once*, never a stretched single column. Responsive = one fluid layout that reflows. Walton: naive stacking collapses hierarchy; choreograph the reflow order so the priority survives.

## The keystone decision

Classify by the core task:

| Flow class | Examples | Strategy |
|---|---|---|
| **Consumer / transactional** | check balance, send, confirm, browse, onboard, KYC | **Mobile-first.** The phone is the primary surface; desktop is the wider sibling |
| **Professional / authoring / monitoring** | trading terminal, maker desk, risk/ops/admin dashboard | **Desktop-first or desktop-only.** Dense, simultaneous, long-session, keyboard-driven. Do not contort it onto a phone |
| **Pro tool that still needs a phone** | a terminal with an on-call need | **Two flows.** Full tool on desktop; a *read-only + alerts + approvals* companion on mobile that cannot perform the dangerous operations |

**The test:** mobile is the *same screens with less width* → one responsive flow. Mobile is a *different, smaller set of tasks* → two flows; design them separately.

## Reflow vs rebuild, per screen

- **Reflow** (one fluid layout) when content, priority and task all survive stacking, in a choreographed order.
- **Rebuild** (a distinct mobile flow) when the mobile task is a subset, when stacking would bury the primary action, or when the input model differs (multi-column desktop form → one-question-per-page mobile).

## Responsive tables: never a squish

| Task on mobile | Pattern |
|---|---|
| **Compare** across many columns | Horizontal scroll + pinned key column + sticky actions (Ant model) |
| **Read one record** | Collapse to cards, or key-column list + drill-in (Material model) |
| **Get the headline** | Summary/top-N on mobile; full table on desktop only |
| **Mostly read, sometimes need a hidden field** | Priority columns; the rest in an expandable row (Carbon model) |

Never silently drop a column the user needs to *act* on. If you hide it, keep it reachable.

## Concrete targets

| Thing | Value |
|---|---|
| Breakpoints (four-tier) | mobile ≤ 480 · tablet 768 · desktop 1024 · wide 1440. Set them where *your content* breaks, not by device name |
| Touch target | ≥ 44 pt (Apple) / 48 dp (Material). 48 is the floor for anything that moves money |
| Primary action | Mobile: **bottom-center** (the thumb's green zone; ~49% browse one-handed). Desktop: **top-right** |
| Navigation | Mobile: **bottom tab bar** (3–5 items). Desktop: **persistent left sidebar**. Same IA tree, different chrome. A hamburger holds *secondary* items only, never primary nav |
| Input | `inputmode="numeric"` / `"decimal"` for amounts, not `type="number"`. Native pickers on mobile. One question per page on mobile; grouped multi-column form on desktop |

---

# Part V — The regulated-finance safety layer (Tier 7)

Fireblocks-grade means *not less control, control that explains itself*: every safety mechanism reads as competence, never as obstruction. Fire all of Part V whenever the flow moves money, signs, settles, approves or verifies identity. Tiers 1–6 still apply underneath.

## V1. Irreversible actions (F16)

**Undo for the reversible; an explicit, specific confirm for the irreversible.** Never confirm what you can undo. Never offer undo once money has left. Scale verification with the amount and the anomaly.

High-stakes money UX is three screens, never one:
1. **Input**: build the transaction.
2. **Review**: a *frozen* summary: amount, recipient, fee, rate, **net amount received**, settlement time, counterparty. Nothing changes between review and signature.
3. **Confirm**: the explicit commitment. Name the consequence: *"Send $40,000 to Acme Ltd — this cannot be reversed,"* never *"Are you sure?"* Destructive and benign buttons far apart; the dangerous one never has default focus.

**The friction ladder**, weakest → strongest; climb as stakes rise: 1 summary review screen (always) · 2 checkbox acknowledgement of irreversibility · 3 hold-to-confirm (kills accidental taps) · 4 **type the amount / recipient to confirm** (forces comprehension) · 5 re-authentication at signing (biometric, hardware key, second device).

Label *why* the friction is there ("Large transfer — extra confirmation required"). Explained friction reads as care; unexplained friction reads as a broken product.

## V2. Transaction lifecycle (F17)

The user's standing question: *where is my money right now?* Answer it at every step. Map internal states onto one visible vocabulary, shown as a timeline/stepper, with an honest ETA:

| State | Tell the user |
|---|---|
| Submitted / Initiated | "We have your instruction" + reference ID |
| Pending authorization | Who must approve, and how many remain ("1 of 2") |
| Processing / In flight | Expected settlement window |
| Settled / Posted | Done: receipt, final amounts |
| Failed / Rejected / Returned | Reason + the next action |

**No optimistic UI for money.** Showing success before the server confirms is right for likes and drafts, wrong for money movement. Use a pending badge that reconciles against true settlement, never a fake "done". Only *Settled* counts as received.

## V3. Approvals (F18)

The maker initiates; a *different* checker approves before execution. The software makes self-approval *impossible*, not discouraged. Procedural controls ("policy says two people review") fail examiners; only *systemic* enforcement passes.

1. **Initiate**: the maker builds it. On submit it enters `PENDING_AUTHORIZATION`; it does not execute.
2. **Policy engine evaluates**: a rule set resolves allow / deny / route-to-quorum by type, amount, asset, destination.
3. **Approval inbox**: a queue, not a buried notification. Each row shows initiator, amount, destination, the rule that triggered review, approvals remaining.
4. **Independent review + decision**: a different user approves or rejects with a reason. The X-of-Y quorum (e.g. 2-of-3) must be met. Route high-value approvals to a second device.
5. **Execute + audit**: only on quorum does it sign/settle. Every step is logged in an immutable audit trail.

Build **one transaction object, three role lenses**: initiator (status of my request), approver (act-now queue), viewer/auditor (read-only history). Never three copies of the data.

## V4. Onboarding under regulation (F19, tiered KYC/KYB)

- Verify at the **moment of value** (first deposit, trade or withdrawal), not at signup. Front-loading KYC at signup is the conversion killer.
- Grant **progressive access** while under review: the user explores, with locked actions clearly labeled ("Verify to send").
- **Tier the limits**: minimal info for low volume; more only when usage crosses a risk threshold.
- **Set time expectations**: "usually 90 seconds", "reviewed within 24 hours".
- **Explain why**: one line next to every ID request turns a demand into a trust signal.
- **Staged status, honestly**: Submitted → Under review → Action needed → Verified. Name the exact missing document inline; never a silent rejection.

## V5. Disclosure and errors (F20)

- **Full cost and true custody before commit, on one line, in plain language**: fee as a separate item, the rate, the **exact amount received**. Never bundle the FX markup into the rate.
- **Name the counterparty and the custodian**, and the legal status of where assets sit. Link attestations or proof-of-reserves if they exist.
- **Risk at the decision point**, never buried in a TOS: slippage tolerance and worst-case received on the confirm screen.
- **Every money error** states what happened, whether money *did or did not* move, the next action, and a reference ID. Predict failures pre-submit when you can ("this swap is expected to fail"). Frame protective stops as protection ("we stopped this to protect you from a worse price"), never as a bug.
- **Sandbox/testnet**: a persistent, unmissable **TEST MODE** banner in a reserved color. Test and live UIs never look identical.
- **WCAG 2.1 AA**: in regulated finance, accessibility is law (EAA since June 2025; ADA).

---

# Output format (mandatory)

Produce all eleven sections. Do not skip. Do not condense. Skip §8 only when the flow truly touches no money and no compliance, and say so explicitly.

## 1. Brief recap and working assumptions
- One paragraph: the product, the feature, the surface class.
- The defaults you adopted for any missing input, stated.
- The money/compliance reality, and whether §8 fires.

## 2. The job and the persona
- The JTBD sentence (F1).
- The primary persona: expertise, context (device, posture, interruption), stakes.
- The single success metric (the activation event, the completed job).

## 3. The object map (OOUX)
Build it before the screens. Per core object (noun): **attributes**, **relationships** to other objects, **actions** it affords (verbs), and which **role** can do which action.

## 4. The flow map (wireflow)
The screen-by-screen path as a numbered-stage diagram in words, in the house diagram grammar:

- **Number the stages**: `1 · ENTRY`, `2 · BUILD`, `3 · REVIEW`, `4 · CONFIRM`.
- **Boxes are screens**: a bold title, one grey sub-label.
- **Arrows are transitions**, labeled with the action that causes them (`Tap Send →`).
- **A pill marks a branch**: `( approved ✓ or rejected ✗ )`.
- **One filled box = the terminal result**, the thing the whole flow produces.

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

State the entry points (where the user arrives from) and the exits (success, cancel, error).

## 5. The screen spec: one block per screen
Repeat for **every** screen.

### Screen N — [name]
- **Purpose**: the one job this screen does.
- **Entry**: how the user arrives; what state they are in.
- **First sight**: what the eye lands on first.
- **Primary action**: the one thing the screen wants the user to do (F9), and where it sits.
- **Secondary actions**: everything else, ranked, demoted.
- **Content**: what is shown, in priority order. Point any table or list to its §6 entry.
- **The two gulfs (F4)**: *what can I do here?* (signifiers present) and *what just happened?* (feedback on the last action).
- **States**: loading / empty / error / success / pending: what each shows.
- **Friction level** (if money): which V1 rung, and why.
- **Copy**: the exact words for the heading, the primary button, the key microcopy.

## 6. Data and tables
Per table or list:
- **Table vs list vs graph vs stat**, and why (F12).
- **The column test**: the columns that survived; the fields sent to the detail surface.
- **Columns**: name · alignment · format (tabular? unit in header? sign + color?).
- **Row**: density default, the primary inline action, overflow actions, selection/bulk.
- **Detail surface**: expandable row / drawer / modal / page, and what it holds.
- **States**: loading (skeleton), empty (text + fixing action), error, paging, filter/search placement.

## 7. Responsive plan
Per screen:
- **One flow or two?** Reflow or rebuild.
- **Mobile**: layout, the table pattern (Part IV), primary action at bottom, nav as bottom tabs.
- **Desktop**: denser, simultaneous, sidebar nav, primary action top-right.
- **Input**: keyboard mode, native pickers, one-question-per-page vs grouped form.

State plainly which surfaces are desktop-only and what their mobile companion does (read / alert / approve).

## 8. The regulated-finance safety layer
Fire when money or compliance is in play. Otherwise write "Not applicable — this flow moves no money and verifies no identity" and explain why. Cover:
- **Irreversible actions** (V1): the input → review → confirm spine; the friction rung per action; the confirm copy.
- **Transaction states** (V2): the lifecycle vocabulary and the status timeline.
- **Approvals** (V3): the maker-checker flow, policy rules, approval-inbox columns, three role lenses.
- **Onboarding/KYC** (V4): progressive-trust staging, tiered limits, the "why we ask" lines.
- **Disclosure** (V5): the one-line cost, the custody statement, the risk at decision.
- **Errors** (V5): the money-error table (what happened / did money move / next action).
- **Sandbox & accessibility** (V5): the test-mode banner; the WCAG 2.1 AA commitments (contrast, keyboard, color-not-sole-signal, focus order).

## 9. The emotional arc (F14)
- **The peak**: the one moment engineered to feel good.
- **The end**: the success state; what the user sees and feels at completion.
- **The pull**: the progress indicators (Zeigarnik) that draw the user through multi-step parts.
- **The aha / activation**: the first moment the user feels the core value, and the shortest path to it.

## 10. Evaluation pass
Walk the whole flow against Nielsen's ten heuristics (F7); for each, state pass or the specific fix. Then the per-screen law check: Hick (choice count), Fitts (action size and placement), Tesler (complexity moved off the user). Name what you changed.

## 11. Build notes and open questions
- **Honesty lines**: what is live / testnet / mocked / roadmap, each on its own bolded line.
- **Open questions**: the decisions that need a human or more data.
- **Handoff**: components to reuse, the design system this maps to, what `impeccable` should polish next.

## Worked example: weak vs spec

> **Weak:** *"The user goes to the transfers page, fills in the form with the amount and the recipient and other details, then submits it and it gets processed by the system, and they can see the status afterward in their history."*
>
> **Spec:**
> **Screen 2 — Amount & payee**
> - **First sight:** a single large amount field, cursor active, numeric keypad up. Available balance directly beneath, greyed.
> - **Primary action:** *Continue*, bottom-center on mobile, disabled until amount ≤ balance and a payee is chosen.
> - **The two gulfs:** *what can I do*: one field, one button, nothing else. *What just happened*: the moment the amount exceeds balance, the field turns and the helper reads "Exceeds available balance," before they can continue.
> - **State — error:** insufficient funds shows the exact shortfall and an "Add funds" link.
> - **Then:** *Continue* → the **frozen Review screen**. Nothing on Review can be edited; to change the amount they go back.

---

# Strict rules

- **One primary action per screen.** Two equal CTAs = none. Fewer choices; complexity onto the system.
- **All five states** for every screen and table. The happy path alone is half a spec.
- **The column test decides every column.** The table is the overview, never the dump.
- **Numbers right-aligned, tabular, unit in header; sign + color, never color alone.**
- **Never optimistic UI for money.** Honest pending states, real ETAs, settled means settled.
- **Friction matches consequence and explains itself.**
- **Self-approval is impossible**, enforced in software, not policy. One object, three role lenses.
- **Disclose cost and custody on one line before commit.**
- **State what is not true out loud**: testnet, mocked, roadmap, each on its own bolded line.
- **Never design a capability the system does not have.** Verify the system truth first.
- **Mobile is not a smaller desktop.** Reflow vs rebuild per screen; pro tools to desktop.

# Before you deliver

- JTBD sentence, one primary persona and the surface class; objects (nouns, attributes, relationships, actions) mapped before screens; a flow map with numbered stages, entry points, branches and exits.
- Every screen has a spec block: first sight, one primary action, content, the two-gulf check, all five states.
- Every table: column test applied, alignment correct, detail surface named, all states designed.
- Every screen: reflow-or-rebuild decided, mobile table pattern chosen, primary action placed per device.
- Money or compliance in play: input → review → confirm spine, honest transaction states, maker-checker with impossible self-approval, progressive KYC, one-line disclosure, money-error table, test banner, WCAG 2.1 AA.
- A peak and a strong end, with progress indicators pulling the user through; all ten heuristics run, each fix stated; every honesty line (live / testnet / mocked / roadmap).
- Can you merge two screens, or send a column to the detail? Then cut it.

Any "no": go deeper before you deliver.

# Reference: who does what best

| Company | Pattern to study |
|---|---|
| Fireblocks | Policy engine + X-of-Y approval quorum + mobile co-signing |
| Stripe | Fee transparency + progressive disclosure + public status page |
| Mercury | Approval workflows with software-enforced separation of duties |
| Wise | Mid-market rate + itemized cost + net amount received |
| Coinbase Prime | Custody disclosure: fiduciary status, audits, proof-of-reserves |
| Plaid | Trust by architecture: credentials never touch the merchant |
| Interactive Brokers | Context-sensitive order ticket as the confirm gate; explicit paper-trading mode |
| Bloomberg Terminal | Information-dense pro surface; density and keyboard over whitespace |
