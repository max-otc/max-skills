# The Circle corpus — verbatim pattern library

Every line in this file is quoted verbatim from developers.circle.com (mined 2026-06; USDC, CCTP, Wallets, StableFX, xReserve, Circle Mint, Gas Station, finality concepts, CCTP technical guide, three quickstarts). Consult the section that matches the page mode you are rewriting. These are the patterns to reproduce — not to copy word-for-word, but to match in shape.

## Page openers

The first sentence names the product and makes the claim in plain words; the term lands one clause later.

> "USDC is a digital dollar issued by Circle, also known as a stablecoin, running on many of the world's leading blockchains."

> "Cross-Chain Transfer Protocol (CCTP) is a permissionless onchain utility that facilitates native USDC transfers across blockchains."

> "Circle Wallets helps you add secure, embedded wallets to your application so your users can hold and use digital assets without the usual complexity of keys, infrastructure, and chain-specific details."

> "StableFX is an institutional-grade stablecoin FX engine built on Arc that combines Request-for-Quote (RFQ) execution with onchain settlement."

> "Gas Station enables developers to build experiences that abstract gas - both for end-users and developers."

The second sentence often names the audience by firm type:

> "This permissioned platform is designed for financial institutions including payment service providers, fintechs, crypto OTC desks, and prime brokers."

> "It is typically used by exchanges, institutional traders, wallet providers, banks, and consumer-app companies."

## Product overview anatomy

The canonical page order: intro → **Key features** → **What you can build** → **How it works** → **Get started** → **Related products**.

**Key features** = bold label + colon + imperative benefit phrase:

> "**Aggregated Liquidity:** Access competitive rates from multiple liquidity providers through a single API call"
> "**24/7 Settlement:** Trade and settle around the clock with sub-second finality on Arc"
> "**Simplified Operations:** Replace multiple bilateral agreements with one integration"

**What you can build** = imperative use-case sentences, one per line:

> "Build payment systems with real-time currency conversion and settlement that enable instant international transfers."
> "Implement automated treasury operations for managing multi-currency stablecoin positions."
> "Offer FX liquidity directly in your platform without building your own matching engine."

**Get started** closers point at the two or three reader tracks by role:

> "Whether you're looking to consume liquidity as a **taker** or provide liquidity as a **maker**, these quickstart guides will help you integrate:"

**Related products** closers draw the boundary between two products in one sentence pair:

> "Gas Station allows you to sponsor network fees for your users. If you want to allow users to pay their network fees with USDC themselves, see the Circle Paymaster."

## Quickstart anatomy

**The guide contract** — opener names the deliverable and the tools, in two sentences:

> "This guide walks you through transferring USDC on EVM testnets using Viem and Node.js. You'll build a simple script that checks your balance and sends test transfers."

> "This guide demonstrates how to transfer USDC from Ethereum Sepolia to Arc testnet using CCTP. You use the viem framework to interact with CCTP contracts and the CCTP API to retrieve attestations."

**Prerequisites** — always the same stem, then a checklist of completed states:

> "Before you begin, ensure that you've: Installed Node.js v22+, Prepared a testnet wallet on the selected chain funded with: Testnet USDC for the transfer, Testnet native tokens for gas fees"

**Step openers** — one sentence stating the step's goal, before any command:

> "This step shows you how to prepare your project and environment."
> "In this step, you'll build a script in TypeScript that transfers USDC"

**Code introductions** — imperative + colon, or "the following":

> "Create a `tsconfig.json` file:"
> "Open `.env` in your editor and add:"
> "In `index.ts`, add the following script."
> "Run the script using the following command:"
> "Request a tradable quote for a USDC to EURC trade using the create a quote endpoint."

**Outcome confirmations** — the sentence after the code says what the reader sees, how to verify, or what state was reached:

> "You'll see output similar to the following:"
> "To verify the transfer, copy the transaction hash URL from the `Explorer:` line and open it in your browser."
> "If the signed data is accepted, the API returns a blank 200 response."
> "A trade is funded when the status is taker_funded."
> "Verify that the response contains 'status': 'pending_settlement'"
> "The function processes the attestation and mints USDC to the specified Arc testnet wallet address."

**Recap closers** — name what was learned, then the key points:

> "In this quickstart, you learned how to check balances and transfer USDC on EVM testnets using one multi-chain Viem script in Node.js. Here are the key points to remember:"

> "Once the script runs and the transfer is finalized, a confirmation receipt is logged in the console."

## Concept-page register

**Flow narration** — the machine narrated in present tense, one actor-verb sentence per step, often numbered:

> "A user deposits USDC from their wallet app into xReserve smart contract on the source blockchain."
> "The xReserve contract emits a deposit event and locks the funds, holding them in reserve."
> "The xReserve attestation service generates and signs a deposit attestation."
> "The remote blockchain mints USDC-backed stablecoins on their blockchain and emits a mint event."

**Trade-off sentences** — a because-clause carries the causality; the mitigation is named in the same sentence:

> "Because of the faster finality time, Fast Transfers are subject to a global allowance to mitigate reorganization risks."
> "Attestations are issued after hard finality, when the transaction is unlikely to be reversed by a chain reorganization, typically in minutes."
> "The finality characteristics of L2 chains depend on when batches are posted and when those batches achieve finality on Ethereum L1."

**Table and diagram introductions** — always announced, always "the following" or "the table below":

> "The table below shows the average time for attestations to become available when using Fast Transfer (`minFinalityThreshold` ≤ 1000):"
> "The following diagram shows how xReserve handles deposits and withdrawals."

**Decision guidance** — the criterion stated as a flat fact:

> "The right wallet product depends on who controls the wallet."
> "The required finality level depends on whether you use Fast Transfer or Standard Transfer."

## Reference register

**Function references** — contract and method named precisely, behavior in present tense:

> "A token depositor calls the TokenMessengerV2#depositForBurn function to deposit a native token (such as USDC), which delegates to the TokenMinterV2 contract to burn the token."

**Parameter descriptions** — terse noun phrases, no sentence ceremony:

> "Version identifier - use 1 for CCTP"
> "Source domain ID"
> "Unique message nonce (see CCTP V2 Nonces)"
> "Minimum finality threshold before allowed to attest"

**Conditional behavior** — exact trigger, exact consequence, exact numbers:

> "If you exceed 35 requests per second, the service blocks all API requests for the next 5 minutes and returns an HTTP 429 response."
> "Iris will not attest to a message at a confirmation level below the specified minimum threshold."

**Concrete numbers with typical times** — never vague:

> "typically in seconds" · "typically in minutes" · "which typically takes ~65 blocks (15-19 minutes) after the batch is posted"

## Callout register

Complete sentences inside callouts; often a bold label naming the topic; the You/Us split and the benefit show up here too:

> "The StableFX API handles both offchain and onchain steps, so you don't need to interact with smart contracts directly."

> "**Blockchains without Fast Transfer:** Some blockchains don't support Fast Transfer as a source blockchain because their standard attestation times are already fast."

> "Rate limit: The attestation service rate limit is 35 requests per second."

> "In production, use a secure key management solution and never expose or share private keys."

> "This prevents credentials from leaking into your shell history or version control."

> "Reach out to your Circle representative to get an API key for StableFX."

## Page blueprints — section order by mode

The same skeletons repeat across the whole corpus. Sentence-case headings, drawn from a fixed vocabulary.

**Product overview** (Wallets, Gateway, CCTP, StableFX — identical skeleton):

1. Intro — definition sentence (plain claim, term second), then the audience named by firm type.
2. `## Key features` — 3-4 items, bold label + colon + imperative benefit; rendered as cards or accordions.
3. `## What you can build` — imperative use-case sentences. (Product *families* use `## Products` with a card per product instead.)
4. `## How it works` — optional; flow narration or a diagram, announced.
5. `## Get started` — opens on the decision criterion ("The right wallet product depends on who controls the wallet:"), then routes by role or product, as cards.
6. `## Related products` / `## Explore key topics` — one boundary sentence pair to the sibling product, then a comparison table or cards. *"CCTP and Gateway offer different approaches to crosschain transfers. This table compares the two approaches."*

**Quickstart / tutorial** (dev-controlled wallet, StableFX taker):

1. Title `Quickstart: <Imperative phrase>` — *"Quickstart: Create a Dev-Controlled Wallet"*.
2. Guide-contract intro (two sentences: walks-through + you'll-build).
3. `## Prerequisites` — "Before you begin, ensure that you've:" + completed states.
4. `## Step 1. <Verb phrase>` … with decimal sub-steps `### 1.1. <Verb phrase>` — every step title verb-first: *"Set up your project"*, *"Create the script"*, *"Run the script"*.
5. `## Next steps` — *"Now that you have a developer-controlled wallet, you can:"* + role-routed links.

Callouts sit *inside* steps: a Tip between the step heading and its code, a Note after the code sample.

**Concept page** (fees, finality, how-xReserve-works):

1. Title = noun phrase ("CCTP Fees", "Finality and Block Confirmations").
2. Opens on the **governing fact** — the one rule that organizes the whole page: *"CCTP charges fees on Fast Transfers only."* / *"Before signing an attestation, Circle waits for blockchain transactions to achieve the appropriate level of transaction finality."*
3. One section per aspect, noun-phrase headings, tables announced.
4. Closes on practical guidance ("Fee optimization strategies") or the boundary to a related concept.

**What-is intro page** (what-is-usdc):

1. Question title ("What is USDC?"), definition paragraph first.
2. A problem/contrast narrative section (before/after shape, below).
3. An action section ("How to access USDC") routing each reader type to its door.

## Title, description, and heading grammar

- **Product titles** are bare nouns: "Circle Wallets", "StableFX", "Gas Station".
- **Quickstart titles**: `Quickstart: <Imperative>` — "Quickstart: Create an FX Trade as a Taker".
- **Concept titles**: noun phrases. **Intro titles**: "What is X?".
- **Frontmatter descriptions** are imperative benefit summaries, one or two sentences: *"Add secure, embedded wallets to your application with Circle's APIs and SDKs. Manage keys, sign transactions, and support multiple blockchains."* / *"Use the StableFX API to create an FX trade on the taker side"* / *"Get started with developer-controlled wallets by creating a wallet set and a wallet within it."*
- **Headings are sentence case**, drawn from a fixed vocabulary: Key features · What you can build · Products · How it works · Get started · Prerequisites · Next steps · Related products · Explore key topics. Section headings are noun phrases; step headings are verb-first imperatives.
- A heading may take **no intro sentence** when a component (card group, table) directly follows — but a table or diagram is still announced when prose precedes it.

## Paragraph shapes — how an idea is wrapped

Paragraphs run one to three sentences, almost always two. One idea per paragraph. Five recurring wrappers:

**Claim + support.** The claim, then the sentence that backs it with mechanism or benefit:

> "USDC is a digital dollar issued by Circle, also known as a stablecoin, running on many of the world's leading blockchains. Designed to represent US dollars on the internet, USDC is backed 100% by highly liquid cash and cash-equivalent assets so that it's always redeemable 1:1 for USD."

**Before / after contrast.** The old burden, then the new state — used for problem narrative:

> "Before USDC, businesses needed traditional banking solutions to accept payments, send remittances to vendors and suppliers, and manage their corporate treasuries. In contrast to USDC, legacy payment methods are slow, expensive, and limited by their lack of interoperability with other systems."

**You / Us split.** The burden removed, then who carries it and what you get instead:

> "You don't manage raw private keys. Circle secures keys with MPC or passkeys depending on wallet product; you get APIs to create wallets, sign transactions, and authorize actions."

**Governing fact.** One flat sentence that rules the page or section; elaboration follows in its own paragraphs:

> "CCTP charges fees on Fast Transfers only."
> "The right wallet product depends on who controls the wallet."

**Warning three-beat.** Bold prohibition → reason → the right action:

> "**Do not hardcode fee values.** Fees can change at any time. Always retrieve the current fee by calling the fee API at least once per week."

## The lexicon — workhorse phrases

| Job | Circle's phrase |
|---|---|
| Open a guide | "This guide walks you through…" / "This guide demonstrates how to…" |
| Promise the deliverable | "You'll build…" |
| Prerequisites stem | "Before you begin, ensure that you've:" |
| Open a step | "In this step, you'll…" / "This step shows you how to…" |
| Introduce code | "…using the following command:" / "add the following script." |
| Confirm output | "You'll see output similar to the following:" |
| Verify | "To verify the transfer, …" |
| State machine behavior | "returns" / "emits" / "mints" / "burns" / "locks" / "issues" |
| Introduce a table | "The table below shows…" |
| Introduce a diagram | "The following diagram shows how…" |
| Remove a burden | "so you don't need to…" / "without the usual complexity of…" |
| Hedge a duration honestly | "typically in seconds" / "typically takes ~65 blocks (15-19 minutes)" |
| Decision criterion | "The right X depends on who/whether…" |
| Recap | "In this quickstart, you learned how to…" |

## Tense rules observed

- **Present tense** for everything the system does: "the contract emits", "the API returns", "Circle waits".
- **"You'll"** only for the reader's future inside this guide: "You'll build", "You'll see output".
- **Present perfect** for prerequisites: "ensure that you've: Installed…, Prepared…, Funded…".
- **Imperative** for every action the reader takes now: "Create", "Open", "Run", "Call", "Sign".

## What never appears

No exclamation marks. No "seamless", "powerful", "robust", "blazing", "effortless", "world-class", "cutting-edge". No "simply" or "just" before an instruction. No jokes, no aphorisms, no rhetorical fragments. The warmth is structural: short clear arcs, burdens named and removed, exact numbers.
