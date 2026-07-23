---
name: max-walkthrough
description: Use when the user wants annotated product screenshots or a step-by-step visual walkthrough of an app — "screenshot every step", "document the flow with screenshots", "product tour with arrows", "mock the app and capture each step", "annotated screenshots for the docs", "walkthrough page", "show the UI flow", "redo the docs with screenshots". Produces real-UI screenshots driven by a build-time mock mode, with arrows + callouts baked in, woven into docs in the max-doc style. The visual companion to max-doc.
---

# Max Walkthrough

## Overview

You turn a real app into a set of annotated screenshots — one per step a user takes — and weave them into the docs. Not mock-ups. Not a Figma. The **production UI**, run in a mock mode so every screen renders deterministically with no backend, captured by a script, with an arrow and a caption pointing at the one control that matters.

The output is the same as a screen recording a human would make — but reproducible, versioned, and re-shot with one command when the UI changes.

This skill is the visual half of documentation. The prose half is `max-doc`; this produces the figures it hangs on, and follows `max-doc` for the page itself.

## Core Principle

**A screenshot that drifts is worse than no screenshot. A screenshot the build regenerates never lies.**

The trap is the hand-taken screenshot: captured once on a live account, stale within weeks, impossible to re-shoot the same way. Every choice here exists to kill drift — the shots are the real components, the data is fixtures, the arrows are a manifest, and the whole set re-renders from one script.

## When to Use

- "Redo the docs with screenshots" · "screenshot the whole flow"
- "Annotated screenshots" · "arrows pointing at the steps" · "product tour"
- "Show users how to do X in the app" with images
- "Mock the app so I can capture each state"
- A walkthrough page — the full click-path, start to finish, in order

**Do NOT use for:**

- Prose-only docs → `max-doc`
- Marketing creative / ad screenshots → `max-marketing`
- A motion video walkthrough (cursor, popups, transitions) → that's the Remotion engine, a different deliverable
- One throwaway screenshot — just take it; the system is for a *set* that must stay current

## The system — five parts

| Part | What it is | Why |
|---|---|---|
| **Mock mode** | a build-time flag that swaps the app's data seams for fixtures | every step renders with no wallet/backend, deterministically |
| **Shot manifest** | one entry per step: route, readiness gate, pre-clicks, annotations | the flow as data — the spine of the whole set |
| **Annotate overlay** | an injected SVG: ring + numbered chip + curved arrow + haloed caption | one consistent pointing language, one accent |
| **Capture runner** | playwright-core driving the **local** Chrome, screenshot at 2× | no browser download; re-shoots the whole set in one command |
| **Figure renderer** | the docs render an image as a captioned figure | the shot lands below the step it illustrates |

## The method — replicate it step by step

### 1. Map the flow.

List the screens a real user walks, in order. That ordered list IS the manifest's spine and the walkthrough page's outline. One screen = one step = one shot (sometimes two, for a modal). Cut any screen the reader never sees.

### 2. Add mock mode.

A single build-time flag — `NEXT_PUBLIC_MOCK_MODE=1` (or your framework's equivalent) — that swaps the **narrowest** data seams for fixtures. Find the seams; do not rewrite the UI:

- **Data hooks / query clients** — the functions that fetch (`usePositions`, `useMakers`, REST clients). Swap at the module boundary: `export const useX = MOCK_MODE ? useMockX : useLiveX`.
- **Auth / wallet / session guard** — the gate that redirects unauthenticated visitors. In mock mode, render through it (skip the bounce) and present a fixture identity.
- **Deep-link knobs** — URL params that force a specific UI state: `?step=4`, `?modal=open`. Seed them with **lazy `useState` initialisers, never effects** — an effect races async data and loops.

Write ONE coherent fixture story (one user, a believable set of balances/rows/rates) so no two screens contradict. Keep it all behind the flag: it must be dead code in production.

> Mock mode renders the real component. Only the data is fake.

### 3. Write the shot manifest.

One entry per step. Target elements by **visible text** wherever possible — it survives class-name churn:

```js
{
  name: "collateral",                 // output filename
  url: "/collateral",                 // route
  waitFor: "Collateral",              // text that gates readiness
  settle: 900,                        // ms for animations/data to land
  clicks: [{ text: "Select" }],       // optional pre-shot taps (open a modal, expand a row)
  annotations: [
    { text: "Deposit", side: "bottom", label: "Add collateral" },
    { contains: "Total", side: "left", label: "Haircut-adjusted total" },
  ],
}
```

Target resolvers, in priority: `css` (selector), `text` (exact), `contains` (substring). Pick `side` so the chip + caption land in **whitespace** — centered cards have wide side gutters (point left/right); full-bleed dashboards have none (point inward from an edge).

### 4. Build and run the capture runner.

`playwright-core` driving the **local system Chrome** (`executablePath` → the installed Chrome) so there is no browser download. Per step: `goto` → wait for `waitFor` → settle → run `clicks` → inject the annotate overlay → screenshot at `deviceScaleFactor: 2` into a **redirect-safe** public path. A target that fails to resolve logs a loud `⚠`, never fails silent.

One command re-shoots everything: `node scripts/docs-shots/capture.mjs`.

### 5. Verify visually, then iterate.

This is part of the method, not optional. Read every captured PNG. Flag: arrows pointing at nothing, captions clipped at the canvas edge, the ring on the wrong (or a hidden duplicate) element, a chip covering critical content. Re-aim the failing target's `side`/selector and re-run. Dispatch a review pass over the set if it is large.

### 6. Weave into the docs.

Each shot lands **below** the step it illustrates, caption = the image alt text, via a figure renderer (see below). Follow `max-doc` for the page itself — question/step headings, terse, time estimates, honesty lines. Optionally one dedicated **Walkthrough** page carrying the full click-path in order, plus single shots dropped into the concept pages they belong to.

## The annotation grammar

One accent colour, one meaning. Quiet weight — the UI stays the subject, the arrow only points.

- **Highlight ring** — a rounded rect around the target, hairline accent.
- **Numbered chip** — a filled accent circle, white number, offset on the chosen `side`.
- **Arrow** — a short curved path from chip to the target edge, with an arrowhead.
- **Caption** — beside the chip, in your brand font, with a **white halo** (`paint-order: stroke`) so it reads over any screenshot without a box.

Scale to the ask: one arrow per shot for a clean point; two when a step has two controls. Never three — split the step.

## Code templates

The overlay drawer, injected into the page before each shot (condense to your accent + fonts):

```js
// One function, handed to page.evaluate(fn, { annotations, accent }).
function draw({ annotations, accent }) {
  const NS = "http://www.w3.org/2000/svg";
  document.getElementById("annot")?.remove();
  const svg = document.createElementNS(NS, "svg");
  svg.id = "annot";
  Object.assign(svg.style, { position: "fixed", inset: 0, width: "100vw", height: "100vh", zIndex: 2147483647, pointerEvents: "none" });
  svg.setAttribute("viewBox", `0 0 ${innerWidth} ${innerHeight}`);

  // CRITICAL: prefer the VISIBLE, on-screen match. Apps keep hidden twins
  // (collapsed rows, per-row CTAs) and off-screen sr-only live regions (x≈1500).
  const visible = (el) => {
    if (!el.offsetWidth && !el.offsetHeight) return false;
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) return false;
    if (r.bottom <= 0 || r.top >= innerHeight) return false;   // off-screen Y
    if (r.right <= 0 || r.left >= innerWidth) return false;    // off-screen X
    const s = getComputedStyle(el);
    return s.visibility !== "hidden" && s.opacity !== "0";
  };
  const dist = (el) => { const r = el.getBoundingClientRect(); return Math.hypot(r.left + r.width/2 - innerWidth/2, r.top + r.height/2 - innerHeight/2); };
  // On a text-length tie, break toward the viewport CENTRE — the open modal's CTA
  // beats a hidden per-row duplicate with identical text.
  const smallest = (test) => { let b=null,bl=1/0,bd=1/0; for (const el of document.querySelectorAll("body *")) { const t=(el.textContent||"").trim(); if(!test(t)||!visible(el))continue; const l=(el.textContent||"").length, d=dist(el); if(l<bl||(l===bl&&d<bd)){b=el;bl=l;bd=d;} } return b; };
  const resolve = (a) => a.css ? document.querySelector(a.css) : a.text ? smallest(t=>t===a.text) : smallest(t=>t.includes(a.contains));

  let drawn = 0;
  annotations.forEach((a, i) => {
    const el = resolve(a); if (!el) return; const r = el.getBoundingClientRect(); drawn++;
    // ring around r, numbered chip + curved arrow on a.side, haloed caption = a.label
    // (port geometry per side: left/right/top/bottom head+tail+chip placement)
  });
  document.body.appendChild(svg);
  return drawn;   // runner warns when drawn < annotations.length
}
```

The runner, driving local Chrome:

```js
import { chromium } from "playwright-core";
const exe = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; // or detect
const browser = await chromium.launch({ executablePath: exe, headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
for (const shot of SHOTS) {
  const page = await ctx.newPage();
  await page.goto(`${BASE}${shot.url}`, { waitUntil: "domcontentloaded" });
  if (shot.waitFor) await page.getByText(shot.waitFor, { exact: false }).first().waitFor({ timeout: 12000 }).catch(()=>{});
  await page.waitForTimeout(shot.settle ?? 900);
  for (const c of shot.clicks ?? []) await (c.css ? page.locator(c.css).first() : page.getByText(c.text, {exact:true}).first()).click({timeout:4000}).catch(()=>{});
  const drawn = await page.evaluate(draw, { annotations: shot.annotations, accent: ACCENT });
  await page.screenshot({ path: `${OUT}/${shot.name}.png` });
  console.log(drawn < shot.annotations.length ? `✓ ${shot.name}  ⚠ ${drawn}/${shot.annotations.length}` : `✓ ${shot.name}`);
  await page.close();
}
```

The figure renderer (Markdown wraps a standalone image in a `<p>`, so a `<figure>` there is invalid HTML — use a span):

```tsx
img({ src, alt }) {
  return src ? (
    <span className="figure">
      <img src={src} alt={alt ?? ""} loading="lazy" />
      {alt ? <span className="figcaption">{alt}</span> : null}
    </span>
  ) : null;
}
```

```css
.figure { display: block }
.figure img { display: block; width: 100%; border: 1px solid var(--border); border-radius: 12px }
.figcaption { display: block; margin-top: 10px; font-size: 13.5px; color: var(--muted); text-align: center }
```

## State the gotchas out loud — each cost real debugging time

- **Asset path must dodge every rewrite/redirect.** Images served under a path a `:path*` redirect catches (e.g. a retired `/docs/*` → external host) 301 away and 404 — silently. Serve shots from a path no rewrite touches (`/shots/...`).
- **Reject off-screen on BOTH axes + centre-tiebreak.** Screen-reader-only live regions are parked far right (x≈1500); a left-of-it twin steals the target. And identical-text twins (modal CTA vs hidden row button) tie — break toward the viewport centre.
- **Mock mode exposes latent render loops.** Faster re-renders can surface a `ResizeObserver`/measure loop that re-sets a value every fire — commit measured state only on a real delta.
- **Seed deep-linked states with lazy `useState`, not effects.** An effect that seeds a step races the async data load and can loop; a lazy initialiser runs once.
- **Don't trust the runner's ✓ — look.** A shot can capture "successfully" with the arrow pointing at empty space. Read every PNG.

## Process

1. **Map** the flow → the ordered step list.
2. **Mock** the seams behind one build-time flag + deep-link knobs.
3. **Manifest** — one entry per step, targets by visible text, `side` into whitespace.
4. **Capture** — local Chrome, overlay injected, 2×, redirect-safe path.
5. **Verify** — read every PNG, re-aim, re-run.
6. **Weave** — figures below steps, caption = alt, page per `max-doc`.

## Quality checks before finishing

- Is the flow mapped to the real steps a user walks, in order — none invented, none missing?
- Is mock mode a build-time flag, swapping only the data seams, dead in production?
- Does every shot resolve every target (no `⚠`), and did you LOOK at each PNG?
- Does each arrow point at the one control that matters — not a hidden twin, not empty space?
- Are captions readable (white halo), unclipped, landing in whitespace?
- Are images on a redirect-safe path, rendered as captioned figures?
- Does the page follow `max-doc` — step/question headings, terse, time estimates, honesty lines?
- Can the whole set re-shoot from one command after a UI change?

If any answer is no — fix before delivering.
