---
name: max-clean-computer
description: Use when this Mac is low on disk, or Max says "clean storage", "free disk", "clean temp", "disk full", "ENOSPC", "max-clean-computer".
---

# max-clean-computer

Delete only storage that rebuilds itself, and only what is safe while builds run: measure → check liveness → clean by tier → report GB recovered.

**Do the FULL pass every time.** The first pass (2026-09-10) stopped at one target and 7 GB; the full pass found 42 GB. "Cleaned the obvious caches" is not done. Done = every Scan row ran, every idle build dir in the Tiers is gone, the Hold table is in the report.

## Iron rule

Never delete a cargo `target/`, `program/target`, `.next`, or forge `out/` while its lane is hot. Hot = any of:
```bash
ps aux | grep -E 'rustc|cargo|solc-|forge|next-server' | grep -v grep   # live compilers / servers
lsof +D <dir> 2>/dev/null | grep -v com.apple | head -3                 # open files; com.apple = Spotlight, NOT a consumer
find <dir> -mmin -30 \( -name '*.rlib' -o -name '*.o' \) | head -1      # recent writes (find = bfs: -newermt '-30 minutes' is INVALID, returns nothing)
```
- Always `lsof` first: a running binary inside (`target/release/vkey`) makes the dir hot. Spotlight (`com.apple`, `mds`, 1,600 open files) in `lsof +D` is noise.
- Reading `du` while a build writes: the numbers move; that dir is hot.
- Solc: `pgrep -f solc-` (binary is `solc-0.8.24`; `-x solc` never matches).
- Stay off the dirs another session's `cargo-sweep` walks (`pgrep -fl cargo-sweep`).

Before touching anything, map every live compiler to its lane:
```bash
for p in $(pgrep -f 'rustc|cargo|solc-|forge|next'); do echo "$p $(lsof -p $p 2>/dev/null | awk '$4=="cwd"{print $NF}')"; done | sort -k2 | uniq -f1 -c
```
Any hit → skip that dir this pass.

## Scan: run ALL of it, in one command

Depth 6, not 4: `find -maxdepth 4` misses `prover/program/target`, `frontend/.next` and scratchpad builds.
```bash
df -h / | tail -1; sysctl vm.swapusage
cd ~; du -sh -- */ .[a-zA-Z]*/ 2>/dev/null | sort -rh | head -30          # whole home, dotdirs included
du -sh ~/Library/* ~/Library/"Application Support"/* ~/Library/Caches/* 2>/dev/null | sort -rh | head -25
# EVERY build dir at ANY depth, incl. program/target, .next, node_modules, scratchpads:
find ~/wt-* ~/crx-* ~/Downloads ~/contracts-* /private/tmp/claude-501 -maxdepth 6 -type d \
  \( -name node_modules -o -name target -o -name out -o -name .next -o -name dist -o -name cache -o -name artifacts \) -prune 2>/dev/null \
  | xargs -I{} du -sm {} 2>/dev/null | sort -rn | awk '$1>150'
du -sh ~/.cargo/registry/* ~/.local/share/* ~/.claude/* 2>/dev/null | sort -rh | head -15
docker system df; docker images --format '{{.Repository}}:{{.Tag}} {{.Size}}'
# colima VM disk: host file vs guest usage — the gap is untrimmed freed blocks
du -sh ~/.colima/_lima/_disks/colima/datadisk; colima ssh -- df -h /var/lib/docker | tail -1
```
Typical layout on this Mac: prover targets 7–15 GB each in `~/wt-*/prover/target` (all `debug/`, no `release/`); `prover/program/target` 0.3–1 GB each; per ui worktree `frontend/.next` ~1.1 GB and `frontend/node_modules` ~1.6 GB. Disk pressure is always cargo targets, then `.next`, never forge `out/`.

## Tiers

| Tier | What | Command |
|---|---|---|
| Always safe | VSCode ShipIt, Chrome, colima, bun caches | `for d in com.microsoft.VSCode.ShipIt Google colima bun; do [ -d ~/Library/Caches/$d ] && rm -rf ~/Library/Caches/$d/*; done` (loop, never a zsh brace-glob: it aborts the whole line on one missing dir; Chrome's open Cache_Data files refuse: ignore) |
| Always safe | npm, pip, brew, uv | `npm cache clean --force; pip3 cache purge; brew cleanup -s --prune=all; uv cache clean` (uv cache = `~/.cache/uv`; `~/.local/share/uv` is python installs, NOT cache) |
| Always safe | cargo registry tarballs | `rm -rf ~/.cargo/registry/cache/*` |
| Always safe | **colima VM disk trim**: freed guest blocks return to APFS only after a trim (host `datadisk` 14 G file vs 7 G used, 2026-09-10) | `colima ssh -- sudo fstrim -av` then `du -sh ~/.colima/_lima/_disks/colima/datadisk`. Non-destructive: VM stays up, SP1 image untouched. Reclaimed 6.6 G first run |
| Always safe | Chrome service-worker caches | `find ~/Library/"Application Support"/Google/Chrome -type d \( -name CacheStorage -o -name ScriptCache \) -prune -exec rm -rf {} +` |
| Always safe | Downloads repo clones: build outputs only (`node_modules`, `.next`, `out`, `dist`, forge `cache`) | `rm -rf` those subdirs, never the clone |
| Idle only | **prover `target/debug`**: the prize, 7–15 GB each | liveness passes → `rm -rf <wt>/prover/target/debug`. Try `cargo sweep --time 1 <wt>/prover` first; when it prints "Cleaned nothing" (everything built <1 day ago), go straight to rm: the sweep is not the last word; "Cleaned nothing" means fresh, not needed. Idle 4 h+ with no open files = idle, even in a lane another session integrates (its forge/solc never touch prover/target). Rebuild 10–40 min |
| Idle only | `prover/program/target` (guest ELF build) | `rm -rf <wt>/prover/program/target` |
| Idle only | `frontend/.next` | no `next-server`/`next start` with cwd in that worktree → `rm -rf <wt>/frontend/.next` (`next build` regenerates) |
| Idle only | whole cargo target dirs of dead lanes | liveness passes → `rm -rf <repo>/target` |
| Idle only | `node_modules` of dead repos | repo confirmed dead (memory: live lanes list) → rm; `npm i` rebuilds |
| Hold, report | `~/.cargo/registry/src` (2 GB+) | regenerable, but every live rustc reads it: only when NO compiler runs |
| Never | `~/Downloads` (key files `.crx-*`), `~/.Trash`, `~/.rustup`, `~/.sp1/toolchains`, `~/.local/share/solana`, live scratchpads `/private/tmp/claude-501/*`, Docker volumes, SP1 docker image (7 GB amd64, re-pull is slow), `~/.claude/projects` (logs + memory), `~/legal-hold-2026-10-09` and `~/legal-hold-symmio-2026-10-11`: legal holds, `~/Archive/canton-purge-2026-10-10` (holds the gas key), `~/crx-held-lanes-*` (git bundles), `~/Music`. Trash and Downloads are not regenerable | — |

Order: biggest idle prover target first, then `.next`, then colima trim, then caches.

## Report

Two lines + the Hold table:
```
X GiB → Y GiB free; cleaned: <dir size, …>; skipped hot: <lane list>
Held (Max's call): crx-held-lanes N G · ~/.colima N G (after trim; what remains = SP1 image + VM OS) · registry/src N G · <dead-looking node_modules>
```
Always print the Hold table; Max decides on it on a max-ask sheet, never the agent. Swap >80% (`sysctl vm.swapusage`): report it, add no agents (memory: swap thrash rule).
