---
name: max-blacklist
description: Use when checking text for banned words, AI slop, or AI tells — "run the blacklist", "banned words", "slop check", "AI tells", "which sentence structures are banned", "lint this prose". Ships the ban-word dictionary, the sentence-structure pattern rules, and the Python linters that score against them.
---

# max-blacklist — the ban-word and sentence-structure system

A dictionary (`words.txt`) matched by a Python engine (`ste-lint.py`). The linter matches the dictionary; the model never scans for words itself. Run the script, read the score.

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

`words.txt` sits beside `ste-lint.py`; `STE_WORDS` overrides the path.

## Thresholds

Per 100 words: **< 2.0 PASS**, **2.0–4.0 SOFT**, **> 4.0 FAIL**.

## Section map of words.txt

| Section | Holds |
|---|---|
| `[options]` | rule toggles (possessive, code_token, ...) |
| `[banned]` | literal ban words |
| `[phrasal]` | multi-word bans |
| `[hedge]` | hedging words |
| `[address]` | second person — rewrite to the imperative |
| `[pattern]` | regexes, including the sentence-structure rules below |
| `[allow]` / `[compound-allow]` / `[term-of-art]` | exemptions |

## The sentence-structure rules

The headline of the system. Each `[pattern]` rule names an AI-typical sentence SHAPE, measured on a 1.8M-character corpus before shipping.

| Rule | Shape | Example it catches |
|---|---|---|
| 7 | X-not-Y appositive | "findings, not filler" |
| 9 | negative litany | "no admin, no clock, no proof" |
| 10 | second negation | "two clocks, not one, and not bounded alike" |
| 11 | antithesis pair | "The guard is not in the code. It is X." |
| 12 | repeated numeral | "two calls, two appends" |
| 13 | commentary tail | ", and that is all this enforces" |
| 14 | rhetorical question | mid-line "?" answered by the writer |
| 15 | appositive gloss | "Foo.sol, the contract that decides X, passed" |
| 16 | emphatic tail | "full stop", "and no more" |
| 17 | pointer restatement | "This is the freeze class." |
| 18 | pseudo-cleft | "What the loop tests is X" |
| 19 | elliptical mirror | "Warnings pass; errors do not." |
| 20 | negated alternative, no comma | "moves the copy and not the lens's" |
| 21 | never-coordination | "binds a proof and never asks where" |
| 22 | emphatic "at all" | "cannot deposit at all" |
| 23 | doubled absence | "no nonce and no deadline" |
| 24 | is-what frame | "is what makes the feed forward" |
| 25 | commentary tail, verb form | ", and that ties Rust to Rust" |
| 26 | exclusivity tail | "and no other field" |
| 27 | pointer restatement on That | "That is the point:" |
| 28 | participial opener | "Bounded at the core's cap." |
| 29 | the X-half frame | "the payout half" |
| 30 | negated-alternative tail | ", never a constant" |
| 31 | semicolon in prose | two clauses joined by ";" |
| 32 | colon before a clause | "buckets: this one credits X" |
| 33 | fronted subordinate opener | "Once X, then Y" (owner ban, not an AI tell) |

Other `[pattern]` rules: hyphen compounds, `re-` prefixes, dashes and arrows, path:line citations, `§`, full-capital words. Many rules are FLAG AND TRIAGE: one instance can be a good sentence; a density is the tic. The dictionary records each rule's measured hit count and innocent rate in its comment.

## False-positive doctrine

A hit is a false positive only when the token is not prose at all — a name, an identifier, a machine artifact. Jargon IS prose and must fire; renaming it or excusing it is not triage.

## New rules

A new `[pattern]` rule ships only with a measured false-positive rate under ~30% on a real corpus. Rules measured and cut are recorded in words.txt comments so nobody rebuilds them.
