---
name: max-blacklist
description: Use when checking text for banned words, AI slop, or AI tells — "run the blacklist", "banned words", "slop check", "AI tells", "which sentence structures are banned", "lint this prose".
---

# max-blacklist — the ban-word and sentence-structure system

`ste-lint.py` matches the `words.txt` dictionary. Run it and read the score. Never scan for words yourself.

## Run it

```bash
python3 ste-lint.py <file>        # or stdin; score = violations per 100 words
python3 ste-lint.py --json <file> # full hit list
python3 ste-lint.py --ban "<phrase>" [--as pattern] [--fix "<text>"]
python3 ste-lint.py --allow "<phrase>"
python3 ste-lint.py --words       # effective lists
python3 ste-lint-code.py <src>    # prose inside source code: comments, docstrings, log strings
python3 md-structure.py --all <file.md>  # document-level tells: bold-lead runs, templated sections
```

`words.txt` sits beside `ste-lint.py`. `STE_WORDS` overrides the path.

Score per 100 words: **< 2.0 PASS**, **2.0–4.0 SOFT**, **> 4.0 FAIL**.

## words.txt sections

- `[options]`: rule toggles (possessive, code_token, ...)
- `[banned]`: literal ban words
- `[phrasal]`: multi-word bans
- `[hedge]`: hedging words
- `[address]`: second person. Rewrite to the imperative.
- `[pattern]`: regexes, including the sentence-structure rules
- `[allow]`, `[compound-allow]`, `[term-of-art]`: exemptions

## Sentence-structure rules (the headline of the system)

Each `[pattern]` rule names an AI-typical sentence SHAPE and was measured on a 1.8M-character corpus before it shipped. Format: id, shape, example caught.

- 7 X-not-Y appositive: "findings, not filler"
- 9 negative litany: "no admin, no clock, no proof"
- 10 second negation: "two clocks, not one, and not bounded alike"
- 11 antithesis pair: "The guard is not in the code. It is X."
- 12 repeated numeral: "two calls, two appends"
- 13 commentary tail: ", and that is all this enforces"
- 14 rhetorical question: mid-line "?" answered by the writer
- 15 appositive gloss: "Foo.sol, the contract that decides X, passed"
- 16 emphatic tail: "full stop", "and no more"
- 17 pointer restatement: "This is the freeze class."
- 18 pseudo-cleft: "What the loop tests is X"
- 19 elliptical mirror: "Warnings pass; errors do not."
- 20 negated alternative, no comma: "moves the copy and not the lens's"
- 21 never-coordination: "binds a proof and never asks where"
- 22 emphatic "at all": "cannot deposit at all"
- 23 doubled absence: "no nonce and no deadline"
- 24 is-what frame: "is what makes the feed forward"
- 25 commentary tail, verb form: ", and that ties Rust to Rust"
- 26 exclusivity tail: "and no other field"
- 27 pointer restatement on That: "That is the point:"
- 28 participial opener: "Bounded at the core's cap."
- 29 the X-half frame: "the payout half"
- 30 negated-alternative tail: ", never a constant"
- 31 semicolon in prose: two clauses joined by ";"
- 32 colon before a clause: "buckets: this one credits X"
- 33 fronted subordinate opener: "Once X, then Y" (owner ban, not an AI tell)
- 34 false agency: "a complaint becomes a fix", "the culture shifts"
- 35 faceless source: "research shows", "the data tells us"
- 36 throat-clearing opener: "Here's what I mean"
- 37 contracted antithesis: "It isn't X. It's Y."
- 38 reframe on a named noun: "The question isn't speed"
- 39 dramatic fragmentation: "That's it. That's the rule."
- 40 narrator at a distance: "This is why", "People tend to"
- 41 transformation arc: "stops being X and starts being Y"
- 42 importance announced: "The implications are significant"
- 43 ready-made figure: "a double-edged sword", "a silver bullet"
- 44 copulative avoidance: "functions as" for "is"
- 45 vague connection: "associated with", "in connection with"
- 46 significance frame: "a testament to", "plays a crucial role"
- 47 outline conclusion: "Despite these challenges", "Looking ahead"
- 48 curly quotation mark: the model's quote, not the keyboard's
- 49 summative closer: "the key takeaway is", "that's why it matters"
- 50 uncited authority: "experts agree", "widely accepted"
- 51 universalizing claim: "most people want", "everyone knows"

Other `[pattern]` rules catch hyphen compounds, `re-` prefixes, dashes and arrows, path:line citations, `§`, and full-capital words.

Many rules are FLAG AND TRIAGE. One instance can be a good sentence. A density is the tic. Each rule's words.txt comment records its measured hit count and innocent rate.

## False positives

A hit is a false positive only when the token is not prose: a name, an identifier, a machine artifact. Jargon IS prose and must fire. Renaming or excusing it is not triage.

## New rules

A new `[pattern]` rule ships only with a measured false-positive rate under ~30% on a real corpus. words.txt comments record the rules measured and cut. Do not rebuild them.

## Imported lists

On 2026-09-19, rules 34 to 51 and about 1,400 dictionary entries came from five published lists: `sam-paech/slop-score` (dated 2025-11-22, the oldest of the five), `hardikpandya/stop-slop`, `JMill/deslop`, Wikipedia's *Signs of AI writing* and `berelevant-ai/slopless`. Every candidate was counted over two frozen CRX corpora first. Three or more hits dropped it. words.txt names each drop, word by word, with the reason.

slopless was installed and measured before its phrase data was copied. Its structure rules are literal lists over a sentence splitter, so they port to regex and no Node process runs here.
