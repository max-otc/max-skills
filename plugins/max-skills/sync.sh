#!/usr/bin/env bash
# Re-copies every canonical skill directory into the bundle. Run after editing
# any individual skill so the bundle does not drift.
#
# The canonical copy is plugins/<skill>/skills/<skill>/ — the whole directory,
# not just SKILL.md, because some skills ship reference files alongside it.
set -euo pipefail
cd "$(dirname "$0")/.."

for dir in */; do
  skill="${dir%/}"
  [ "$skill" = "max-skills" ] && continue
  src="$skill/skills/$skill"
  [ -d "$src" ] || { echo "missing canonical skill dir: $src" >&2; exit 1; }
  dest="max-skills/skills/$skill"
  rm -rf "$dest"
  mkdir -p "$dest"
  cp -R "$src/." "$dest/"
  echo "synced $skill"
done

echo "Bundle synced."
