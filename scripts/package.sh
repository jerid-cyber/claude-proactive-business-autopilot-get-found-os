#!/usr/bin/env bash
# Build the installable plugin file: dist/get-found-os.plugin (a zip of the plugin folder).
# Upload this file in Claude (Cowork / desktop) to install, or attach it to a GitHub Release.
# Usage: bash scripts/package.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PLUGIN_DIR="$ROOT/plugins/get-found-os"
VERSION="$(python3 -c "import json;print(json.load(open('$PLUGIN_DIR/.claude-plugin/plugin.json'))['version'])")"
mkdir -p "$ROOT/dist"
python3 "$ROOT/scripts/validate.py"
rm -f "$ROOT/dist/get-found-os.plugin" "$ROOT/dist/get-found-os-v$VERSION.plugin"
( cd "$PLUGIN_DIR" && zip -rq "$ROOT/dist/get-found-os.plugin" . -x "*.DS_Store" -x "setup/*" )
cp "$ROOT/dist/get-found-os.plugin" "$ROOT/dist/get-found-os-v$VERSION.plugin"
echo "Built dist/get-found-os.plugin and dist/get-found-os-v$VERSION.plugin"
