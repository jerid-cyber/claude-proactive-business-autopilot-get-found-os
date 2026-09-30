#!/usr/bin/env bash
# One-time setup: replace the YOUR-GITHUB-USERNAME placeholder with your real GitHub
# username (or org) everywhere in this repo, so every install link and badge works.
# Usage: bash scripts/set-github-owner.sh jeridwempen
set -euo pipefail
if [ $# -ne 1 ]; then echo "Usage: bash scripts/set-github-owner.sh <github-username-or-org>"; exit 1; fi
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
grep -rl "YOUR-GITHUB-USERNAME" "$ROOT" --exclude-dir=.git --exclude-dir=dist --exclude=set-github-owner.sh \
  | while read -r f; do sed -i.bak "s/YOUR-GITHUB-USERNAME/$1/g" "$f" && rm -f "$f.bak"; echo "updated $f"; done
echo "Done. Commit the changes: git commit -am 'Set GitHub owner'"
