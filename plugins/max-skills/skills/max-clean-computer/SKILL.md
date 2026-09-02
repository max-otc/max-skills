---
name: max-clean-computer
description: Use when this Mac is low on disk, or Max says "clean storage", "free disk", "clean temp", "disk full", "ENOSPC", "max-clean-computer". Finds all recoverable (regenerable) storage and cleans only what is safe while builds run.
---

# max-clean-computer

Free disk by deleting only storage that rebuilds itself. Measure → check liveness → clean by tier → report GB recovered.

## Iron rule

Never delete a cargo `target/` or forge `out/` while its lane is hot. Hot = any of:
```bash
ps aux | grep -E 'rustc|cargo|solc-|forge' | grep -v grep        # live compilers
lsof +D <target-dir> 2>/dev/null | head -3                        # open files (running binaries live in target/release)
find <repo> -newermt '-30 minutes' -name '*.rlib' | head -1       # recent writes
```
Any hit → skip that dir this pass. Solc liveness: `pgrep -f solc-` (binary is `solc-0.8.24`; `-x solc` never matches).

## Scan

```bash
df -h / | tail -1
find ~ -maxdepth 4 -type d -name target -not -path "*/node_modules/*" 2>/dev/null | \
  while read t; do [ -d "$t/debug" ] || [ -d "$t/release" ] || [ -d "$t/riscv32im-succinct-zkvm-elf" ] && du -sh "$t"; done 2>/dev/null | sort -rh
du -sh ~/.cargo ~/.rustup ~/Library/Caches ~/.npm ~/.cache 2>/dev/null
du -sh ~/Library/Caches/* 2>/dev/null | sort -rh | head -10
```
Typical layout on this Mac: prover targets 20 GB+ each in `~/crx-*/prover/target`; disk pressure is always cargo targets, not forge `out/`.

## Tiers

| Tier | What | Command |
|---|---|---|
| Always safe | VSCode ShipIt, Chrome, colima, bun caches | `rm -rf ~/Library/Caches/{com.microsoft.VSCode.ShipIt,Google,colima,bun}/*` |
| Always safe | npm, pip, brew | `npm cache clean --force; pip3 cache purge; brew cleanup -s --prune=all` |
| Always safe | cargo registry tarballs | `rm -rf ~/.cargo/registry/cache/*` |
| Always safe | Chrome service-worker caches (multi-GB across profiles) | `find ~/Library/"Application Support"/Google/Chrome -type d \( -name CacheStorage -o -name ScriptCache \) -prune -exec rm -rf {} +` |
| Default for rust | keep last run, wipe the rest | `cargo sweep --time 1 <repo>/prover` (removes artifacts unused >1 day, keeps the latest build); `cargo sweep --installed` also drops old-toolchain artifacts. Exact keep-last-run: `cargo sweep --stamp` before the build, `cargo sweep --file` after. Installed at `~/.cargo/bin/cargo-sweep`. Safe on warm repos — never during an active compile in that repo |
| Idle only | whole cargo target dirs (dead lanes) | `rm -rf <repo>/target` after liveness check passes |
| Idle only | `target/debug` alone (test-build bloat, often 5–10× release; check `du -sh target/*` first) | `rm -rf <repo>/prover/target/debug`, keep `release/` + `sp1-native-bins/` |
| Always safe | build outputs inside Downloads repo clones (`node_modules`, `.next`, `out`, `dist`, forge `cache`) | size with `du`, then `rm -rf` those subdirs only — never the clone itself |
| Idle only | `node_modules` of dead repos | confirm repo dead first; `npm i` rebuilds |
| Never | `~/Downloads` (holds key files `.crx-*`), `~/.Trash`, `~/.rustup` toolchains, live scratchpads `/private/tmp/claude-501/*`, Docker volumes | — |

Rebuilding a swept prover target costs 10–40 min of compile. Sweep the biggest idle target first.

## Report

One line: `X GiB → Y GiB free; cleaned: <list>; skipped hot: <list>`.

## Common mistakes

- Deleting a target with a running binary inside (`target/release/vkey`) kills that process's backing file — always `lsof` first.
- Reading `du` while a build writes → numbers move; that dir is hot.
- Emptying Trash or Downloads: not regenerable, never in scope.
