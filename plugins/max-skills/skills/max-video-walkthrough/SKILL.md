---
name: max-video-walkthrough
description: Use when the user wants an animated product-demo video built from real app screenshots — "walkthrough video", "animated product demo", "screen recording from screenshots", "remotion walkthrough", "make a video walkthrough of the app", "cursor demo video", "video onboarding". Builds a Remotion walkthrough FROM SCRATCH — a faux browser holding real captured screen states, a cursor that glides on a bezier and clicks, typed inputs, rolling numbers, page-load bars, popup callouts, and a wallet-approval popup, all driven by a beat timeline. The motion companion to max-walkthrough.
---

# Max Video Walkthrough

## Overview

You turn a real app into an animated walkthrough video — a faux browser window holding real screenshots, a cursor that glides to a control and clicks, the screen state changing, fields typed, numbers rolling, a page-load bar sweeping, callouts springing in, a wallet popup approving — all timed to a **beat timeline** and rendered with Remotion.

Not a screen recording. Not After Effects. The **production UI**, captured in mock mode as a set of clean screen *states*, then choreographed in code so the demo is reproducible, versioned, and re-rendered with one command when the UI changes.

This skill is the motion half of the walkthrough family. The still half is `max-walkthrough` — annotated screenshots for docs. This builds the **engine from zero**: there is no pre-existing player. You write the geometry, the primitives, the beat model, and the player, and you LOOK at the render until it is right.

## Core Principle

**The click only reads as "it did something" if the screen state changes. Capture before AND after.**

A cursor that clicks a button over an unchanged screen looks broken. The illusion of a live app is: cursor arrives → clicks → page-load bar sweeps → the screenshot underneath *swaps* to the next state. Every device in this skill exists to sell that one beat: the cursor never teleports, overlays wear the screenshot's own font, the number lands exactly on the printed figure, the bar sweeps on every navigation.

## When to Use

- "Make a walkthrough video of the app" · "animated product demo"
- "Screen recording from screenshots" · "cursor demo video" · "video onboarding"
- "Remotion walkthrough" · "turn the click-path into a video"
- A motion product tour — cursor, typing, popups, transitions, a wallet approval

**Do NOT use for:**

- Annotated STILL screenshots for docs → `max-walkthrough` (the still companion; reuse its mock mode + capture)
- Prose docs → `max-doc`
- A talking-head edit, data-viz reel, or reference replica → those are the other Remotion engines in `video/`
- A real screen recording of a human clicking — that drifts; this skill exists for a reproducible *set*

## The system — seven parts

| Part | What it is | Why |
|---|---|---|
| **Mock mode + multi-state capture** | the app run with fixtures, captured per step as several screen STATES + named target rects + computed styles | a click can visibly change the screen; overlays inherit the real glyphs |
| **Geometry** | one module: image px → canvas px, window placement with side gutters | one source of truth; primitives never see the manifest |
| **Primitives** | Cursor, Callout, TypingField, NumberRoll, NavLoadingBar, ClickPulse, WalletModal, BrowserChrome | the frame-driven vocabulary of the demo |
| **Beat model** | a choreography DSL (`RawBeat`) resolved into canvas-space, frame-timed beats | the heart — the flow as data, hand-authored against the manifest |
| **Player** | one `<Sequence>` per beat; screen swaps on hard cuts; overlays per beat; synced caption | plays the resolved beats back-to-back |
| **Render + verify** | render stills at key beats, LOOK, iterate; then full MP4 | the engine lies on a green ✓ — only the eye confirms |
| **Registration** | the finished video at the ROOT of `Root.tsx` with `calculateMetadata` = summed beat frames | house rule; the video appears at the top of Studio |

## The method — replicate it for ANY app

### 1. Capture the app's states in mock mode.

Reuse `max-walkthrough`'s mock mode (one build-time flag swapping the narrowest data seams for fixtures, deep-link knobs seeded by lazy `useState`). This skill adds two things the still pipeline doesn't need:

- **Multi-state per step.** A step groups several SCREEN STATES so a click can visibly change the screen — `hedge-empty` and `hedge-filled`, `cp-list` → `cp-confirm` → `cp-live`. Capture each as its own clean PNG (no overlay).
- **Computed-style capture.** For any element you will animate (a field you type into, a figure you roll), capture its computed `font / size / weight / color / letterSpacing / background` so the overlay renders in the screenshot's own glyphs — not pasted on.

The shot list groups screens under steps. Each screen names the target rects the engine will choreograph against (resolved by visible text where possible — it survives class churn):

```js
// shots-video.mjs — richer than the still manifest: steps group screen STATES.
// resolver = { text } (exact) | { contains } (substring) | { css }
export const VIDEO_STEPS = [
  { name: "collateral", screens: [
    { id: "collateral", url: "/collateral", waitFor: "Collateral",
      targets: { total: { contains: "36,371" }, deposit: { text: "Deposit" } } },
  ]},
  { name: "counterparty", screens: [
    { id: "cp-list",    url: "/counterparties", waitFor: "No ranking",
      targets: { select: { text: "Select" } } },
    { id: "cp-confirm", url: "/counterparties", waitFor: "Select",
      clicks: [{ text: "Select" }],                 // pre-shot tap opens the modal
      targets: { confirm: { text: "Select counterparty" }, noMoney: { contains: "No funds move" } } },
    { id: "cp-live",    url: "/counterparties?mockAlloc=1", waitFor: "Release",
      targets: { locked: { contains: "$30,000" } } },   // ← deep-link knob = the AFTER state
  ]},
  { name: "amount", screens: [
    { id: "hedge-empty",  url: "/desk/taker/hedge?mockStep=0&mockFill=0", waitFor: "USD/INR",
      targets: { amount: { css: "input[inputmode='numeric']" } } },
    { id: "hedge-filled", url: "/desk/taker/hedge?mockStep=0", waitFor: "USD/INR",
      targets: { hero: { contains: "₹" }, next: { text: "Next" }, amount: { css: "input[inputmode='numeric']" } } },
  ]},
];
```

The capture runner drives **local Chrome** (no browser download), screenshots each state clean, and resolves rects + styles with the same visibility rules as the still overlay (skip off-screen and hidden twins; break text ties toward the viewport centre):

```js
// capture-video.mjs — run with the mock dev server up:
//   NEXT_PUBLIC_MOCK_MODE=1 PORT=3457 npm run dev
//   node scripts/docs-shots/capture-video.mjs   → walkthrough-video.json + clean PNGs
import { chromium } from "playwright-core";
import { VIDEO_STEPS } from "./shots-video.mjs";

const exe = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const browser = await chromium.launch({ executablePath: exe, headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });

// In-page: resolve a name→rect map AND the computed style of each target.
function resolveTargets(targets) {
  const visible = (el) => {
    const r = el.getBoundingClientRect();
    if (!r.width || !r.height) return false;
    if (r.bottom <= 0 || r.top >= innerHeight || r.right <= 0 || r.left >= innerWidth) return false;
    const s = getComputedStyle(el);
    return s.visibility !== "hidden" && s.opacity !== "0";
  };
  const dist = (el) => { const r = el.getBoundingClientRect();
    return Math.hypot(r.left + r.width/2 - innerWidth/2, r.top + r.height/2 - innerHeight/2); };
  const smallest = (test) => { let b=null,bl=1/0,bd=1/0;
    for (const el of document.querySelectorAll("body *")) {
      const t=(el.textContent||"").trim(); if(!test(t)||!visible(el)) continue;
      const l=(el.textContent||"").length, d=dist(el);
      if(l<bl||(l===bl&&d<bd)){b=el;bl=l;bd=d;} } return b; };
  const find = (q) => q.css ? [...document.querySelectorAll(q.css)].filter(visible)[0] ?? null
    : q.text ? smallest(t=>t===q.text) : smallest(t=>t.includes(q.contains));
  const out = {};
  for (const name in targets) {
    const el = find(targets[name]); if (!el) continue;
    const r = el.getBoundingClientRect();
    const s = getComputedStyle(el);
    out[name] = {
      x: Math.round(r.left), y: Math.round(r.top), w: Math.round(r.width), h: Math.round(r.height),
      style: { fontFamily: s.fontFamily, fontSize: parseFloat(s.fontSize), fontWeight: s.fontWeight,
               color: s.color, letterSpacing: s.letterSpacing, textAlign: s.textAlign,
               background: s.backgroundColor },   // ← the seam that makes overlays native
    };
  }
  return out;
}

const steps = [];
for (const step of VIDEO_STEPS) {
  const screens = [];
  for (const sc of step.screens) {
    const page = await ctx.newPage();
    await page.goto(`${BASE}${sc.url}`, { waitUntil: "domcontentloaded" });
    if (sc.waitFor) await page.getByText(sc.waitFor, { exact: false }).first().waitFor({ timeout: 12000 }).catch(()=>{});
    await page.waitForTimeout(sc.settle ?? 900);
    for (const c of sc.clicks ?? []) { await (c.css ? page.locator(c.css).first() : page.getByText(c.text,{exact:true}).first()).click({timeout:4000}).catch(()=>{}); await page.waitForTimeout(500); }
    const targets = await page.evaluate(resolveTargets, sc.targets ?? {});
    await page.screenshot({ path: `${OUT}/${sc.id}.png` });
    const want = Object.keys(sc.targets ?? {}).length, got = Object.keys(targets).length;
    console.log(got < want ? `✓ ${sc.id}  ⚠ ${got}/${want}` : `✓ ${sc.id}`);   // loud miss, never silent
    screens.push({ id: sc.id, image: `walkthrough/taker/${sc.id}.png`, targets });
    await page.close();
  }
  steps.push({ name: step.name, screens });
}
await browser.close();
// → public/walkthrough/taker/walkthrough-video.json: { viewport, scale, steps:[{ name, screens:[{ id, image, targets }] }] }
```

> Mock mode renders the real component. Only the data is fake. The video reads the JSON the engine never sees the app.

### 2. Geometry — one transform module.

One module owns the mapping from manifest image space (the 1440×900 capture) into canvas space (1920×1080), and where the window sits. Every primitive imports it; none ever touches the raw manifest. Place the window centred with side gutters wide enough that left/right callouts never clip.

```ts
// geometry.ts — the single source for the image→canvas transform.
export type Rect = { x: number; y: number; w: number; h: number };
export type Point = { x: number; y: number };

export const VIEWPORT = { width: 1440, height: 900 };  // the capture size
export const CANVAS_W = 1920, CANVAS_H = 1080;
export const CHROME_BAR_HEIGHT = 44, WINDOW_RADIUS = 16;

export const SCREEN_SCALE = 1.0;
export const SCREEN_W = VIEWPORT.width  * SCREEN_SCALE;   // 1440
export const SCREEN_H = VIEWPORT.height * SCREEN_SCALE;   // 900
export const WINDOW_LEFT = Math.round((CANVAS_W - SCREEN_W) / 2);  // 240 — the side gutter
export const WINDOW_TOP = 56;
export const SCREEN_LEFT = WINDOW_LEFT;
export const SCREEN_TOP = WINDOW_TOP + CHROME_BAR_HEIGHT;          // 100

export const toCanvas = (r: Rect): Rect => ({
  x: SCREEN_LEFT + r.x * SCREEN_SCALE, y: SCREEN_TOP + r.y * SCREEN_SCALE,
  w: r.w * SCREEN_SCALE, h: r.h * SCREEN_SCALE,
});
export const toCanvasPoint = (r: Rect): Point => { const c = toCanvas(r); return { x: c.x + c.w/2, y: c.y + c.h/2 }; };
export const WINDOW_CENTER: Point = { x: SCREEN_LEFT + SCREEN_W/2, y: SCREEN_TOP + SCREEN_H/2 };  // cursor's rest before beat 0
```

### 3. Primitives — the frame-driven vocabulary.

Every primitive computes its picture from `useCurrentFrame()`. **Never** a CSS `@keyframe` or `transition` — those do not render headless. House tokens: accent GM Electric `#2D5BFF`, ink `#1D1D1F`, the house spring `{mass:0.6, damping:16, stiffness:120}` over 26f, `EASE.out = bezier(0.16,1,0.3,1)`, the main move `bezier(0.87,0,0.13,1)`. Fonts: Bricolage Grotesque (`font`), Commit Mono (`monoFont`).

**Cursor** — glides `from`→`to` along a bowed bezier with the eased main move, dips on the press, emits one fading ring:

```ts
// cursorPath.ts — a real hand swings; bow the path perpendicular to from→to.
export function bezierArc(from: Point, to: Point, t: number): Point {
  const dx = to.x-from.x, dy = to.y-from.y, d = Math.hypot(dx,dy) || 1;
  const nx = -dy/d, ny = dx/d;                       // perpendicular unit vector
  const bow = Math.min(d * 0.18, 150);               // scales with distance, capped
  const mx = (from.x+to.x)/2 + nx*bow, my = (from.y+to.y)/2 + ny*bow;  // control point
  const u = 1-t; return { x: u*u*from.x + 2*u*t*mx + t*t*to.x, y: u*u*from.y + 2*u*t*my + t*t*to.y };
}
```

```tsx
// Cursor.tsx
const MOVE_EASE = Easing.bezier(0.87, 0, 0.13, 1);   // house "main move"
export const Cursor: React.FC<{ from: Point; to: Point; startFrame: number; moveDuration: number; clickFrame?: number }> =
({ from, to, startFrame, moveDuration, clickFrame }) => {
  const frame = useCurrentFrame();
  const pos = frame <= startFrame ? from
    : frame >= startFrame + moveDuration ? to
    : bezierArc(from, to, MOVE_EASE((frame - startFrame) / moveDuration));
  const d = clickFrame === undefined ? -1 : frame - clickFrame;
  const dip  = d >= 0 && d <= 6  ? interpolate(d, [0,6],  [0.85,1], { easing: Easing.out(Easing.quad), extrapolateRight:"clamp" }) : 1;
  const ring = d >= 0 && d <= 12 ? { size: interpolate(d/12,[0,1],[10,64],{easing:Easing.out(Easing.cubic)}),
                                     opacity: interpolate(d/12,[0,1],[0.55,0]) } : null;
  return (
    <div style={{ position:"absolute", left:pos.x, top:pos.y, zIndex:9000, pointerEvents:"none" }}>
      {ring && <div style={{ position:"absolute", width:ring.size, height:ring.size, marginLeft:-ring.size/2, marginTop:-ring.size/2,
                             borderRadius:"50%", border:`2px solid #2D5BFF`, opacity:ring.opacity }} />}
      <svg width={40} height={40} viewBox="0 0 24 24" style={{ transform:`scale(${dip})`, transformOrigin:"5px 3px",
           filter:"drop-shadow(0 2px 5px rgba(0,0,0,.35))" }}>
        <path d="M5 3L19 12L12 13L9 20L5 3Z" fill="#FFF" stroke="#1D1D1F" strokeWidth="1.5" strokeLinejoin="round" />
      </svg>
    </div>
  );
};
```

**Callout** — ring + numbered chip + curved arrow + haloed caption, springing in from the chip; the arrow draws on via `strokeDashoffset`. Geometry per `side` (head sits just off the target edge, tail = chip a fixed REACH further out, arrowhead from the end tangent). Caption uses `paint-order: stroke` for a white halo so it reads over any screenshot.

```tsx
// Callout.tsx (condensed: the per-side head/tail + draw-on are the load-bearing parts)
const GAP = 18, REACH = 104, CHIP_R = 20, ACCENT = "#2D5BFF";
const s = spring({ fps, frame: local, config:{mass:0.6,damping:16,stiffness:120}, durationInFrames:26 });
const scale = interpolate(s,[0,1],[0.9,1]), rise = interpolate(s,[0,1],[8,0]);
const drawn = interpolate(local,[3,16],[0,1],{ easing: Easing.bezier(0.16,1,0.3,1), extrapolateLeft:"clamp", extrapolateRight:"clamp" });
// head/tail by side: e.g. left → head=[rx-GAP, cy], tail=[rx-GAP-REACH, cy]; bend perpendicular; arrowPath = `M tail Q bend head`.
// <g transform translateY(rise) scale(scale) transformOrigin=chip>: ring rect, path (dasharray=len, dashoffset=len*(1-drawn)),
//   arrowhead polygon (opacity ramps in at local 14→18), chip circle + mono number, haloed caption:
<text fontFamily={font} fontSize={26} fontWeight={600} fill="#FFF"
      stroke="rgba(10,15,32,0.85)" strokeWidth={5} paintOrder="stroke" strokeLinejoin="round">{label}</text>
```

**TypingField** — types into the screenshot's empty input, character by character, with a blinking caret. Overlays ON TOP with no background fill, left-aligned at a fixed origin so a comma never shoves the value sideways. Pass the **captured computed style** so the value matches the field's own glyphs:

```tsx
// TypingField.tsx
export const TypingField: React.FC<{ rect: Rect; value: string; startFrame: number; durationFrames: number;
  prefix?: string; padLeft?: number; style?: CapturedStyle }> = ({ rect, value, startFrame, durationFrames, prefix="", padLeft, style }) => {
  const frame = useCurrentFrame(), local = frame - startFrame;
  const revealed = local <= 0 ? 0 : local >= durationFrames ? value.length : Math.floor(local/durationFrames * value.length);
  const typing = local > 0 && local < durationFrames;
  const caretOn = typing && frame % 30 < 15;
  const fs = style?.fontSize ?? Math.round(rect.h * 0.52);     // captured style WINS; this is the fallback
  return (
    <div style={{ position:"absolute", left:rect.x, top:rect.y, width:rect.w, height:rect.h, display:"flex",
      alignItems:"center", paddingLeft: padLeft ?? 30, boxSizing:"border-box", zIndex:8500, whiteSpace:"pre", overflow:"hidden",
      fontFamily: style?.fontFamily ?? monoFont, fontSize: fs, fontWeight: style?.fontWeight ?? 500,
      color: style?.color ?? "#1D1D1F", letterSpacing: style?.letterSpacing }}>
      <span>{prefix}{value.slice(0, revealed)}</span>
      <span style={{ display:"inline-block", width:2, height:fs, marginLeft:1, background: style?.color ?? "#1D1D1F", opacity: caretOn ? 1 : 0 }} />
    </div>
  );
};
```

**NumberRoll** — counts up to the target and **masks the static figure** so the roll lands seamlessly. A solid mask rect = the card's own captured `background`, bled out a few px on every side so no static digit peeks; the rolling value clamped so it never overshoots; ends EXACTLY on `to` so the overlay matches the screenshot and can unmount:

```tsx
// NumberRoll.tsx
const OUT_EASE = Easing.bezier(0.16, 1, 0.3, 1);
export const NumberRoll: React.FC<{ rect: Rect; to: number; from?: number; startFrame: number; durationFrames: number;
  prefix?: string; suffix?: string; decimals?: number; fontSize?: number; bgInset?: number; style?: CapturedStyle }> =
({ rect, to, from=0, startFrame, durationFrames, prefix="", suffix="", decimals=0, fontSize, bgInset=3, style }) => {
  const frame = useCurrentFrame(), local = frame - startFrame;
  let v = local <= 0 ? from : local >= durationFrames ? to
    : interpolate(local, [0, durationFrames], [from, to], { easing: OUT_EASE, extrapolateLeft:"clamp", extrapolateRight:"clamp" });
  v = to >= from ? Math.min(v, to) : Math.max(v, to);                 // never overshoot
  const fmt = v.toLocaleString("en-US", { minimumFractionDigits: decimals, maximumFractionDigits: decimals });
  const mask = style?.background ?? "#FFF";
  return (<>
    {/* mask: the card's OWN bg, bled by bgInset so static digits never peek */}
    <div style={{ position:"absolute", left:rect.x-bgInset, top:rect.y-bgInset, width:rect.w+bgInset*2, height:rect.h+bgInset*2, background:mask, zIndex:8500 }} />
    <div style={{ position:"absolute", left:rect.x, top:rect.y, width:rect.w, height:rect.h, display:"flex", alignItems:"center",
      justifyContent: (style?.textAlign ?? "left")==="right" ? "flex-end" : "flex-start", zIndex:8501, whiteSpace:"pre",
      fontVariantNumeric:"tabular-nums", fontFamily: style?.fontFamily ?? monoFont,
      fontSize: style?.fontSize ?? fontSize ?? 38, fontWeight: style?.fontWeight ?? 700, color: style?.color ?? "#1D1D1F" }}>
      {prefix}{fmt}{suffix}
    </div>
  </>);
};
```

**NavLoadingBar** — the thin Chrome page-load sliver across the window top, so a cut between two screenshots reads as a real navigation. Surges fast to ~90%, creeps, completes to 100%, fades over the last ~4f:

```tsx
// NavLoadingBar.tsx
export const NavLoadingBar: React.FC<{ top:number; left:number; width:number; startFrame:number; durationFrames:number }> =
({ top, left, width, startFrame, durationFrames }) => {
  const local = useCurrentFrame() - startFrame;
  if (local < 0 || local > durationFrames) return null;
  const completeAt = Math.max(0, durationFrames - 4), surge = completeAt * 0.7;
  const progress = local <= surge ? interpolate(local,[0,surge],[0.02,0.9],{ easing: Easing.bezier(0.16,1,0.3,1) })
    : local <= completeAt ? interpolate(local,[surge,completeAt],[0.9,0.98])
    : interpolate(local,[completeAt,durationFrames],[0.98,1]);
  const opacity = interpolate(local,[completeAt,durationFrames],[1,0],{ extrapolateLeft:"clamp" });
  return <div style={{ position:"absolute", left, top, width: width*progress, height:3, background:"#2D5BFF",
    boxShadow:"0 0 8px #2D5BFF", opacity, zIndex:8700 }} />;
};
```

**ClickPulse** — a brief tint flash + expanding outline over the *target* (the cursor ring flashes the hand; this flashes what it hit). Returns null outside its short window.

**WalletModal** — a WalletConnect→Fireblocks approval popup. Two phases that **slide** (never fade): a Connect picker (header, a tab row whose indicator slides Recent/Browser/QR, a wallet list with a highlighted Fireblocks row) → the Fireblocks approve panel (institutional navy, shield + wordmark, an inner tab row that slides, the transaction rows, Reject | Approve). Press Approve → spinner `Confirming…` → green `Approved ✓`. Critically, export the **cursor target points** derived from the *same* layout constants the component renders with, so the cursor lands exactly on the Approve button:

```tsx
// WalletModal.tsx — geometry lives at module level so the cursor target stays in lockstep.
export const MODAL_W = 440, MODAL_H = 560;
export const MODAL_LEFT = Math.round((CANVAS_W - MODAL_W) / 2);
export const MODAL_TOP  = Math.round((CANVAS_H - MODAL_H) / 2);
// ...Approve button is the right footer button; its center derived from PAD/BTN_W/BTN_GAP/BTN_H:
export const WALLET_APPROVE_POINT = { x: MODAL_LEFT + APPROVE_CX_REL, y: MODAL_TOP + APPROVE_CY_REL };

// Phase slide: connect exits left, approve enters right (frame-driven, both panels mounted):
const p = interpolate(frame - pick, [0, 8], [0,1], { easing: EASE_OUT, extrapolateLeft:"clamp", extrapolateRight:"clamp" });
const connectX = -p * MODAL_W, approveX = (1-p) * MODAL_W;
// Approve states: pressed (scale dip) → confirming (frame-rotated spinner) → confirmed (bg → success-green, pop).
```

**BrowserChrome + Screen** — the faux window. A rounded white surface with three traffic-light dots, back/forward/reload glyphs, a pill address bar (lock + muted scheme + dark host in mono), a kebab. It does NOT own placement — `Screen` feeds it the exact canvas geometry from `geometry.ts` and drops the screenshot flush below the chrome bar:

```tsx
// Screen.tsx
export const Screen: React.FC<{ image: string; url?: string }> = ({ image, url }) => (
  <BrowserChrome width={SCREEN_W} height={SCREEN_H} left={WINDOW_LEFT} top={WINDOW_TOP} url={url}>
    <Img src={staticFile(image)} style={{ width: SCREEN_W, height: SCREEN_H, display:"block", objectFit:"cover" }} />
  </BrowserChrome>
);
```

### 4. The beat model — the centerpiece.

A walkthrough is a list of STEPS, each a list of BEATS. A beat is one micro-action: glide to a control, click, swap the screen, type, roll, pop a callout, approve a wallet. You author beats in a terse DSL against the captured manifest; a resolver turns each into a canvas-space, frame-timed `ResolvedBeat`. Two things the resolver owns make the motion feel alive:

- **Cursor chaining.** A module-level `prevPoint` carries the cursor's resting position across beats, so each beat's `from` = where the last beat left the hand. The cursor never teleports.
- **Per-click page-load bar.** A module-level `prevImage` tracks the last screenshot. When a beat's screen differs (a click navigated or swapped state), the resolver inserts a short load bar automatically; a `loading: true` flag forces a full-length bar for a fresh route.

```ts
// walkthroughData.ts — the authoring DSL.
type Side = "left" | "right" | "top" | "bottom";
type RawBeat = {
  screen: number;                                   // index into this step's captured screens (the STATE)
  caption: string;                                  // the lower-third line, synced to THIS beat
  cursorTo?: string;                                // target name → cursor destination (and the click pulse)
  click?: boolean;
  type?:  { target: string; value: string; prefix?: string };
  roll?:  { target: string; to: number; prefix?: string; suffix?: string; decimals?: number };
  callout?: { target: string; label: string; side: Side };
  wallet?: { action: string; rows: { label: string; value: string }[] };   // pops the Fireblocks approval
  loading?: boolean;                                // force a full page-load bar (new route)
  hold: number;                                     // frames to dwell after the action — pace to reading speed
};
type RawStep = { name: string; title: string; url: string; beats: RawBeat[] };

// Timing constants (frames @ 30fps)
const MOVE=24, CLICK_GAP=5, AFTER=8, NOCLICK_GAP=3, CALLOUT_DELAY=6;
const LOAD=34, CLICK_LOAD=18, ROLL=26, WALLET_IN=4, WALLET_CURSOR=10, WALLET_CONFIRM=26;
const typeDur = (v: string) => Math.max(18, v.length * 2);

// The choreography — hand-authored, one entry per beat (excerpt):
const CHOREO: RawStep[] = [
  { name:"amount", title:"Say what to hedge", url:"app.crxfx.com/hedge", beats: [
    { screen:0, caption:"Start a hedge — what do you owe?", loading:true, cursorTo:"amount", click:true, hold:10 },
    { screen:0, caption:"Type the amount you owe.", type:{ target:"amount", value:"1,000,000" }, hold:20 },
    { screen:1, caption:"The locked value updates live.", roll:{ target:"hero", to:84315000, prefix:"₹" }, hold:16 },  // screen:1 = the AFTER state
    { screen:1, caption:"Next.", cursorTo:"next", click:true, hold:10 },
  ]},
  { name:"counterparty", title:"Pick your counterparty", url:"app.crxfx.com/counterparties", beats: [
    { screen:0, caption:"Pick the one desk you'll trade with.", loading:true, cursorTo:"select", click:true, hold:16 },
    { screen:1, caption:"It moves no money — one on-chain flag.", callout:{ target:"noMoney", label:"No funds move", side:"left" }, cursorTo:"confirm", click:true, hold:14 },
    { screen:1, caption:"Approve it in your Fireblocks wallet.", wallet:{ action:"Allocate counterparty", rows:[ {label:"Function",value:"preAllocate"}, {label:"Fee",value:"~$0.00"} ] }, hold:22 },
    { screen:2, caption:"Allocated — that desk is now live.", callout:{ target:"locked", label:"Your posted margin", side:"bottom" }, hold:34 },
  ]},
];
```

The resolver — the heart. It reads the manifest, maps every target through `geometry.ts`, computes per-beat frame timings, chains the cursor, and inserts the load bar:

```ts
// walkthroughData.ts — resolve loop.
const STEP_BY_NAME = Object.fromEntries((manifest.steps as ManifestStep[]).map(s => [s.name, s]));
let prevPoint: Point = WINDOW_CENTER;   // cursor chaining: carried across beats
let prevImage = "";                     // load-bar trigger: carried across beats

const resolveStep = (raw: RawStep): ResolvedStep => {
  const m = STEP_BY_NAME[raw.name];
  const beats = raw.beats.map((b, bi) => {
    const screen = m.screens[b.screen];
    const rectOf  = (n: string): Rect  => toCanvas(screen.targets[n]);          // canvas-space rect
    const pointOf = (n: string): Point => toCanvasPoint(screen.targets[n]);     // canvas-space center

    // Load bar on a forced load OR any screen change since the last beat.
    const isNav = prevImage !== "" && screen.image !== prevImage;
    const loadDur = b.loading ? LOAD : isNav ? CLICK_LOAD : 0;
    prevImage = screen.image;

    // Wallet beat: cursor glides to Approve and confirms; everything timed off WALLET_* constants.
    if (b.wallet) {
      const approveFrame = WALLET_CURSOR + MOVE + CLICK_GAP, confirmedFrame = approveFrame + WALLET_CONFIRM;
      const cursor = { from: prevPoint, to: WALLET_APPROVE_POINT, startFrame: WALLET_CURSOR, moveDuration: MOVE, clickFrame: approveFrame };
      prevPoint = WALLET_APPROVE_POINT;
      return { image: screen.image, url: raw.url, caption: b.caption, len: confirmedFrame + b.hold,
        loadBar: loadDur ? { dur: loadDur } : undefined, cursor,
        wallet: { action: b.wallet.action, rows: b.wallet.rows, startFrame: WALLET_IN, approveFrame, confirmedFrame } };
    }

    // Normal beat: load → (cursor move) → click → action → hold.
    const a = loadDur, lead = b.cursorTo ? MOVE : 0;
    const clickFrame   = b.click ? a + lead + CLICK_GAP : undefined;
    const actionStart  = a + lead + (b.click ? AFTER : NOCLICK_GAP);
    const to = b.cursorTo ? pointOf(b.cursorTo) : prevPoint;        // no cursorTo → hold position
    const cursor = { from: prevPoint, to, startFrame: a, moveDuration: MOVE, clickFrame };
    prevPoint = to;                                                  // chain forward

    const clickPulse = b.cursorTo && b.click ? { rect: rectOf(b.cursorTo), atFrame: clickFrame! } : undefined;
    let actionDur = b.click ? 12 : 0, type, roll, callout;
    if (b.type)   { const d = typeDur(b.type.value); type = { rect: rectOf(b.type.target), value: b.type.value, startFrame: actionStart, dur: d, prefix: b.type.prefix }; actionDur = Math.max(actionDur, d); }
    if (b.roll)   { const rect = rectOf(b.roll.target); roll = { rect, to: b.roll.to, startFrame: actionStart, dur: ROLL, ...b.roll, decimals: b.roll.decimals ?? 0, fontSize: Math.round(rect.h*0.82) }; actionDur = Math.max(actionDur, ROLL); }
    if (b.callout){ callout = { rect: rectOf(b.callout.target), label: b.callout.label, side: b.callout.side, appearFrame: actionStart + CALLOUT_DELAY, index: bi + 1 }; actionDur = Math.max(actionDur, 22); }

    return { image: screen.image, url: raw.url, caption: b.caption, len: actionStart + actionDur + b.hold,
      loadBar: loadDur ? { dur: loadDur } : undefined, cursor, clickPulse, type, roll, callout };
  });
  return { name: raw.name, title: raw.title, durationInFrames: beats.reduce((s,b) => s + b.len, 0), beats };
};

export const STEPS = CHOREO.map(resolveStep);
export const TOTAL_FRAMES = STEPS.reduce((s, st) => s + st.durationInFrames, 0);
```

### 5. The player — one Sequence per beat.

The player lays each beat as a back-to-back `<Sequence>`. The beat's screenshot mounts (the click in the *previous* beat is what swapped it — the "it did something" feel); overlays mount only for the beat that uses them; the lower-third caption belongs to the beat and fades in as it opens, so the words land with the action. Steps and beats hand off on **hard cuts** — never a fade.

```tsx
// WalkthroughVideo.tsx
const BeatScene: React.FC<{ beat: ResolvedBeat; index: number; total: number; title: string }> = ({ beat, index, total, title }) => (
  <AbsoluteFill style={{ background: GROUND }}>
    <DotGrid /> <DotGridVignette />
    <Screen image={beat.image} url={beat.url} />
    {beat.loadBar   && <NavLoadingBar top={SCREEN_TOP} left={SCREEN_LEFT} width={SCREEN_W} startFrame={0} durationFrames={beat.loadBar.dur} />}
    {beat.clickPulse&& <ClickPulse rect={beat.clickPulse.rect} atFrame={beat.clickPulse.atFrame} />}
    {beat.roll      && <NumberRoll {...beat.roll} durationFrames={beat.roll.dur} />}
    {beat.type      && <TypingField {...beat.type} durationFrames={beat.type.dur} />}
    {beat.callout   && <Callout target={beat.callout.rect} {...beat.callout} />}
    {beat.wallet    && <WalletModal {...beat.wallet} />}
    <Cursor {...beat.cursor} />
    <LowerThird index={index} total={total} title={title} caption={beat.caption} />
  </AbsoluteFill>
);

export const WalkthroughVideo: React.FC = () => {
  const out: React.ReactNode[] = []; let stepOffset = 0;
  STEPS.forEach((step, si) => {
    let beatOffset = 0;
    step.beats.forEach((beat, bi) => {
      out.push(<Sequence key={`${step.name}-${bi}`} from={stepOffset + beatOffset} durationInFrames={beat.len} layout="none">
        <BeatScene beat={beat} index={si} total={STEPS.length} title={step.title} /></Sequence>);
      beatOffset += beat.len;
    });
    stepOffset += step.durationInFrames;
  });
  return <AbsoluteFill style={{ background: GROUND }}>{out}</AbsoluteFill>;
};

// Register at the ROOT of Root.tsx (house rule — finished video, top of the Studio sidebar).
export const walkthroughTakerMeta = { id:"WalkthroughTaker", component: WalkthroughVideo,
  durationInFrames: TOTAL_FRAMES, fps: FPS, width: 1920, height: 1080 };
```

The lower-third names the step (`01 / 09 · Say what to hedge`) and the synced caption beneath, fading in over the beat's first ~5 frames.

### 6. Render + verify loop.

This is part of the method, not optional. The engine returns a green ✓ even when the cursor points at empty space.

- **Studio first** — `npx remotion studio --port 3333` → `http://localhost:3333/WalkthroughTaker`. Scrub each beat.
- **Stills at key beats** — render single frames at the click, the type, the roll, the wallet approve, and LOOK. Is the cursor on the button? Did the number land on the figure? Is the callout in whitespace?
- **Full render only when asked** — MP4 to `~/Downloads` (not the repo): `npx remotion render src/index.ts WalkthroughTaker ~/Downloads/WalkthroughTaker.mp4`.
- **Iterate the data, not the engine.** Re-aim a `side`, retime a `hold`, fix a target name in the DSL, re-render. The primitives stay fixed.

## State the gotchas out loud — each cost real time

- **Frame-driven only. NEVER CSS `@keyframes` / `transition`.** They animate in the browser but render as a frozen frame headless. Every motion is a pure function of `useCurrentFrame()`.
- **Never fade between scenes (house rule).** No opacity cross-dissolve, no `@remotion/transitions/fade`. Cuts carry energy; the cursor's continuity and the load bar carry the motion across the cut.
- **Overlays must wear the screenshot's CAPTURED computed style + matching background.** A typed value or rolled number in the wrong font/size/color reads as pasted on. Capture `font/size/weight/color/letterSpacing/background` and pass it; captured style WINS over loose props.
- **The cursor `from` must chain across beats.** Carry `prevPoint` at module level so each beat starts where the last ended. Forget it and the hand teleports every cut.
- **A number roll must land EXACTLY on the static figure and mask it with the real bg color (small bleed).** Clamp so it never overshoots; end on `to` exactly; paint the mask = the card's captured background, bled ~3px, so the unmount is seamless and no static digit peeks at the edges.
- **Resolve a roll/type/click target to the VISIBLE on-screen element.** Apps keep hidden twins (collapsed rows, sr-only live regions parked far right). Reject off-screen on both axes; break text ties toward the viewport centre.
- **A screen STATE change is what makes a click read as "it did something."** Capture the before AND after state and point the next beat at the after `screen` index. A click over an unchanged screenshot looks broken.
- **Derive cursor targets from the SAME constants the component lays out with.** The wallet Approve point is computed from the modal's own PAD/BTN_W/BTN_GAP — never a hand-guessed coordinate, or the cursor misses the button.
- **Pace to reading speed.** A beat holds long enough to read its caption once (~2.5–3 words/sec + a ~0.4s settle), then cuts. Tune `hold` per beat; never park on a finished line.
- **Register at the ROOT of `Root.tsx` with `calculateMetadata` = summed beat frames.** `TOTAL_FRAMES` is the reduce over every beat's `len`; a wrong total truncates the video or pads dead air. `@remotion/*` stay in lockstep at the project version.

## Process

1. **Capture** — mock mode, multi-state per step, rects + computed styles → `walkthrough-video.json` + clean PNGs.
2. **Geometry** — one module: image px → canvas px, window placement with side gutters.
3. **Primitives** — Cursor (bezier + ripple), Callout, TypingField, NumberRoll, NavLoadingBar, ClickPulse, WalletModal, BrowserChrome. Frame-driven, house tokens.
4. **Beat model** — author the DSL against the manifest; the resolver chains the cursor and inserts the load bar.
5. **Player** — one `<Sequence>` per beat, hard cuts, overlays per beat, synced lower-third.
6. **Render + verify** — stills at key beats, LOOK, iterate the data; then full MP4 to `~/Downloads`. Register at the root.

## Quality checks before finishing

- Is every screen captured in mock mode — before AND after each state-changing click — clean, with no overlay?
- Did you capture the computed style of every field you type into or number you roll, and pass it so the overlay wears the screenshot's glyphs?
- Is the geometry transform the single source — do the primitives ever touch the raw manifest? (They must not.)
- Is every primitive frame-driven — zero CSS `@keyframes` or `transition`?
- Are all scene/beat handoffs hard cuts — zero fades?
- Does the cursor chain across beats (never teleports), and does it land on the real control (not a hidden twin)?
- Does every number roll land exactly on the static figure and mask it with the card's real background?
- Does a page-load bar sweep on every navigation / state change, and does each click visibly change the screen?
- Is the wallet popup's cursor target derived from the modal's own layout constants?
- Are captions synced to the action, paced to reading speed, readable over the screenshot?
- Is the finished video registered at the ROOT of `Root.tsx` with `durationInFrames` = summed beat frames?
- Did you RENDER stills at the key beats and LOOK — not trust the green ✓?

If any answer is no — fix before delivering.
