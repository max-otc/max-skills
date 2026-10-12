# Anchors for cites inside an artifact

Part of `max-plan-itteration`. Default since 2026-09-13.

Line cites (`:N`) shift on every insert. On the CRX plans three fixers added cite faults from stale line maps, two thirds of forty defects were cite/count drift, and the gate (two consecutive CLEAN) could not close.

- Every citable line ends `[@name]` (`row-210`, `sheet-48`, `fence-dsar`, `p12-3-token-rule`, or `t-<old-line>` when nothing better fits). Reference: `` `@name` ``; cross-artifact: `` other `@name` ``.
- Fences: anchor the line above the opener; inside, a trailing `#` comment or a comment line above, never inside a quoted body.
- `:N` cites survive only for line 3 / frozen history and `file:N` cites into source files.
- The gate is anchor integrity by script, not "every cite lands": definitions unique across artifacts, every reference resolves, zero bare `:N` outside the allowed places, enumerations (marker lists, fence lists) name anchors. Counts in prose stay derived by script. Fixers never "re-land" anything; readers never "sample cites".
- Convert an existing artifact in one dedicated round before resuming reads: anchor every cited line, rewrite cites by old line number, then a cross-artifact pass.
- Spec of record: `anchors-spec.md`, written with the CRX plans (session scratch r77). Copy its rules into the artifact's head.
- Trap: a blind `:N`→`@name` substitution also converts source-file line numbers that collide with a minted anchor. Classify every cite per occurrence by its clause first; write source cites with the filename adjacent (`` `cd.sh:147` ``).
- Trap: a bare `:N` in a sentence naming several scripts belongs to the sentence's file context (the deploy span walked), not the nearest filename token. Six of ten nearest-token attributions were wrong at source.
- Mint cross-artifact anchors from the other artifact's cite targets mapped by content, never by reading its numbers against another version of your own file.
