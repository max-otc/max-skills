---
name: max-decisions
description: Use when Max has several open decisions, rulings, or forks to make at once — "what decisions are needed", "make a decisions file", "what do I need to rule on", batch owner calls, design forks, confirm-or-overturn rulings — and the answer should be a single decision sheet he can answer in one line.
---

# max-decisions — the AuDHD decision sheet

One HTML file. Every open decision as a card grid: question, zero-context explanation, 2–4 options with pros/cons, one recommendation, one verdict line. **Max answers inside the page** — he clicks a card per decision and presses Send. He types nothing in the chat.

## Output contract

Copy `template.html` (same directory) and fill it. Write to `~/<topic>-decisions.html` (e.g. `~/crx-curator-decisions.html`). The file IS the deliverable. The chat message accompanying it is 1–2 lines.

Then run these four steps, in order. Never skip step 1.

**1. Close the stale tab.** Any Chrome tab already showing this sheet — a `file://` one, or an `http://127.0.0.1:PORT/` one from an earlier serve — is closed first. Match on the topic slug in the URL:

```bash
SLUG=<topic>-decisions   # e.g. crx-curator-decisions
osascript -e "tell application \"Google Chrome\"
  set slug to \"$SLUG\"
  repeat with w in windows
    repeat with t in (tabs of w)
      if (URL of t contains slug) or (title of t contains slug) then close t
    end repeat
  end repeat
end tell" 2>/dev/null
```

The `title of t` arm catches the served tab, whose URL is only `http://127.0.0.1:<port>/`. Put the slug in the `<title>` so it matches. This rule is general: **on every update of a sheet, the previous tab is closed** — never leave a stale render behind.

**2. Serve it.** `serve.py` binds a free port on `127.0.0.1` and prints `PORT=<n>` as its first line:

```bash
python3 ~/.claude/skills/max-decisions/serve.py ~/<topic>-decisions.html \
  > /tmp/<topic>-serve.log 2>&1 &
sleep 1
PORT=$(sed -n 's/^PORT=//p' /tmp/<topic>-serve.log | head -1)
```

Serving over HTTP is required. A `file://` page has an opaque origin and cannot POST to localhost.

**3. Open the served URL** — never the file path:

```bash
open -a "Google Chrome" "http://127.0.0.1:$PORT/"
```

**4. Watch for the answer — the agent is ALWAYS looking.** Max clicks in the page and presses Send. The server writes `~/<topic>-decisions-answers.json` and `~/<topic>-decisions-answers.md`, then exits. Waiting is layered — every layer runs, because polls get killed and Max's answers must never sit unread:

- **Layer 1 — Monitor (preferred).** If the `Monitor` tool is available (load via `ToolSearch "select:Monitor"`), start a monitor that fires when `~/<topic>-decisions-answers.json` exists. It survives turn ends and re-invokes the agent on its own.
- **Layer 2 — background poll (fallback).** If no Monitor, run the poll in the background (`run_in_background`, not foreground):

```bash
for i in $(seq 1 720); do
  [ -f ~/<topic>-decisions-answers.json ] && break
  sleep 60
done
cat ~/<topic>-decisions-answers.md 2>/dev/null || echo "NO ANSWER"
```

- **Layer 3 — the standing check (ALWAYS, regardless of layers 1-2).** While any sheet is outstanding, `cat` the answers file **at the start of every turn** — on every user message, every task notification, every wakeup — before doing anything else. A killed poll or dead monitor is NOT "no answer"; the file is the truth. The sheet is outstanding until the answers file is read or Max cancels it. If a watcher gets killed, do not treat that as a signal to stop watching — restart a layer or rely on layer 3, and say so in one line.

Do NOT ask Max to type `1A 2B` in the chat. Tell him the sheet is open and answerable in the page, then watch. If he answers in the chat anyway, take it and kill the server. If he says "I answered" and the file is missing, check `pgrep -f serve.py` — a dead server means the Send fell back to clipboard; ask him to paste.

The server stops itself 12 hours after start if no answer arrives, so nothing lingers.

## The zero-context rule (the point of the format)

Each decision's `ctx` paragraph must stand alone: a reader with **no chat history and no memory** understands it. That means:

- Define every verb, term, and codename inline the first time it appears (`escapeToUnclaimed` — the exit for a de-whitelisted seat…").
- Name concrete things: file paths, addresses, amounts, line numbers, dates.
- State what is at stake in one sentence — what breaks or what money moves.
- 2–4 sentences. If it needs more, the decision is really two decisions — split it.

## The worked-example rule (MANDATORY — every decision)

Max has AuDHD. A paragraph of symbol names and file paths is unreadable to him, and a decision he cannot read is a decision he cannot make. **Every decision carries a `<div class="eg">` block, placed directly after `ctx`, before the options.**

The example is one short paragraph of **business logic with real numbers**:

- A named actor doing an ordinary thing — "a maker sells $10m of 1-year USD/JPY", "a desk holds a position over the weekend".
- Round, concrete money. `$30,000`, not `30 bps of gross`. Convert every rate, bp, and ratio into dollars.
- What happens to that money, in sequence, ending in the consequence the decision is about.
- **Zero code identifiers.** No file paths, no function names, no constants, no line numbers. Those live in `ctx` and the residuals box, never in the example.
- 2–4 sentences. Past tense or present, plain verbs.

Where the options differ in outcome, end the example with the fork made concrete: "Option A refuses the trade. Option B lets it through and charges nothing."

**If a decision cannot be given a money example, it is not ready to be a decision** — either it is an implementation detail that should not be on the sheet, or it has not been understood well enough to ask about. Do not ship a decision with a hand-waved example.

## The mechanism rule (MANDATORY — every option card)

A label Max cannot picture is a decision he cannot make. Earned by a real failure: a card titled "O(1) barrier + span guard" forced him to ask what it was before he could rule.

- **Every option card opens with a `<p class="how">` line** — first element of the `.pc` block, before pros. One or two short sentences, plain words: what this option actually does. Shape: what exists today → what this option changes → what new rule guards it. The "None of these" card is exempt.
- **The option `h3` title names the mechanism in plain words** ("Two saved numbers replace the walk"), never a term of art ("O(1) barrier", "payee-consent variant"). Jargon may appear only in parentheses after its plain name.
- **Define every term the first time it appears anywhere on the sheet** — recut → "regenerating the proof key", guest → "the audited program that runs inside the proof", fixture → "the stored real proof the tests replay".
- **Never one wall of prose.** ctx carries the today-state and the stake (2–4 sentences); each card's `how` carries that option's mechanics; pros/cons carry the trade. Mechanics of all options crammed into one ctx paragraph is a defect — split them onto the cards.

## Structure, in order

1. `<h1>`: `{Topic} — the decisions you need to make`.
2. Lede: why these decisions exist now + the ranking (which are substantive, which batch-rulable).
3. Optional red banner: the ONE urgent fact (live risk, deadline). At most one. Delete if none.
4. Decision sections, numbered, in **answer-first order**: urgent (the banner's item, if any) → substantive → batch-rulable one-liners → teardown/timing. The `n` label carries the gating note: `only if 1=A`, `batch-rulable`, `confirm a ruling`, `act first`.
5. Residuals box: facts to carry that are NOT decisions (already ruled, owed pushes, standing warnings). Delete if none.
6. Footer: date · which decision to take first and why · answer-back example · sources.

## Per decision

- The `h2` is a question.
- A worked money example after `ctx`, per the rule above. No exceptions.
- A plain-language `how` line opening every option card, per the mechanism rule above. No exceptions.
- At most ONE `rec` card, always placed first, tag `Recommended`, letter `A`. When there is genuinely no recommendation (a pure cost/appetite call), no card gets `rec`: all cards tagged `Option`, and the verdict opens `Your call —` naming the number that decides it.
- The sheet's letters are canonical. Reletter freely so the rec is `A`; never reference the source material's original option letters or names ("option (b)") — Max answers with the sheet's letters only.
- 2–4 options. Two is fine. Never more than four.
- Every option has an `effort` line: `ZERO / TRIVIAL / SMALL / MED / LARGE` + a short qualifier.
- Pros and cons ≤4 bullets each, one line per bullet. **The recommended option gets honest cons too** — a rec with no cons reads as salesmanship and Max will distrust the whole sheet.
- Verdict line: `My pick: A — {one-line reason}`. When the call is genuinely the owner's (a business number, a risk appetite), the verdict says so: recommend, then name the number only Max can price.
- Dependencies between decisions go in the `n` label and the verdict, not in prose walls.

## Answer-back convention

Number everything. The page builds the answer string itself (`1A · 2B · 3none`) and sends it back. The markup carries the wiring:

- Each decision section is `<section class="q" data-d="1">` — `data-d` is the number.
- Each option is a `<label class="opt">` holding `<input class="pick" type="radio" value="A">`. The `value` is the letter. The script assigns the radio group name, so option letters only need to be unique within their section.
- Every decision keeps the `None of these` card (`value="none"`) as its LAST card, and the comment textarea under the grid. Both are verbatim in the template — do not delete them.
- Selections and comments persist to `localStorage` under the document title, so a reload loses nothing.

Opened as a plain file with no server, the Send button copies the answer to the clipboard instead.

## Common mistakes

| Mistake | Fix |
|---|---|
| ctx assumes chat context ("as discussed", "the r201 issue") | Re-explain from zero, inline |
| Rec card has no cons | Add the honest ones |
| Options that are the same choice restated | Cut to the real fork |
| Prose analysis outside the cards | Everything lives in ctx/pros/cons/verdict |
| Burying a decision inside another's cons | Promote it to its own numbered section |
| New CSS or layout | Use template.html verbatim — only content changes |
| ctx written in symbol names and file paths | That is the engineer's view. Put it in money, add the example |
| Example states a rate, a bp, or a ratio | Convert to dollars on a round notional |
| Example mentions a function or a file | Strip it. Identifiers belong in ctx, never in the example |
| No example because "this one is technical" | Then it is not a decision Max can make — rewrite it or cut it |
| Old tab left open on an updated sheet | Close the matching Chrome tab BEFORE opening the new one |
| Opening the `file://` path | Open `http://127.0.0.1:$PORT/` — a file page cannot post back |
| Asking Max to type `1A 2B` in the chat | He answers in the page; wait for the answers file |
| Dropping the `None of these` card or the comment box | Both stay on every decision |
| Option title is a term of art ("O(1) barrier") | Rename to the plain mechanism; jargon in parentheses only |
| Option card with no `how` line | Every card opens with one — what it does, today → change → guard |
| All options' mechanics crammed into ctx | ctx keeps today-state + stake; each card's `how` carries its own mechanics |
