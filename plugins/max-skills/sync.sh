#!/usr/bin/env bash
# Re-copies each canonical SKILL.md into the bundle. Run after editing
# any individual skill so the bundle does not drift.
set -euo pipefail
cd "$(dirname "$0")/skills"
for skill in max-video max-hook max-explainer-video max-persona-research max-marketing; do
  cp "../../$skill/skills/$skill/SKILL.md" "$skill/SKILL.md"
done
echo "Bundle synced."
