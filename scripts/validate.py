#!/usr/bin/env python3
"""Validate the Get-Found OS repo before committing or releasing.

Checks the marketplace manifest, plugin manifest, every skill, every agent,
and every skill cross-reference in the command center, heartbeat and agents.
Exit code 0 = pass, 1 = fail.   Usage: python3 scripts/validate.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN = os.path.join(ROOT, "plugins", "get-found-os")
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
errors, notes = [], []


def err(msg):
    errors.append(msg)


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return (m.group(1) if m else None), text


# 1. Marketplace manifest
mp_path = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
try:
    mp = json.load(open(mp_path))
    for key in ("name", "owner", "plugins"):
        if key not in mp:
            err(f"marketplace.json missing '{key}'")
    for p in mp.get("plugins", []):
        src = os.path.normpath(os.path.join(ROOT, p.get("source", "")))
        if not os.path.isfile(os.path.join(src, ".claude-plugin", "plugin.json")):
            err(f"marketplace plugin '{p.get('name')}' source has no plugin.json: {p.get('source')}")
    notes.append(f"marketplace.json OK ({len(mp.get('plugins', []))} plugin)")
except Exception as e:  # noqa: BLE001
    err(f"marketplace.json invalid: {e}")

# 2. Plugin manifest
try:
    pj = json.load(open(os.path.join(PLUGIN, ".claude-plugin", "plugin.json")))
    if not KEBAB.match(pj.get("name", "")):
        err("plugin.json 'name' missing or not kebab-case")
    if not re.match(r"^\d+\.\d+\.\d+$", pj.get("version", "")):
        err("plugin.json 'version' is not semver")
    for p in mp.get("plugins", []) if "mp" in globals() else []:
        if p.get("name") == pj["name"] and p.get("version") and p["version"] != pj["version"]:
            err(f"version mismatch: plugin.json {pj['version']} vs marketplace.json {p['version']}")
    notes.append(f"plugin.json OK ({pj['name']} v{pj['version']})")
except Exception as e:  # noqa: BLE001
    err(f"plugin.json invalid: {e}")

# 3. Skills
skills_dir = os.path.join(PLUGIN, "skills")
skills = sorted(d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d)))
ranks = {}
for s in skills:
    path = os.path.join(skills_dir, s, "SKILL.md")
    if not os.path.isfile(path):
        err(f"skills/{s} has no SKILL.md")
        continue
    fm, text = frontmatter(path)
    if fm is None:
        err(f"skills/{s}/SKILL.md has no YAML frontmatter")
        continue
    name = re.search(r'^name:\s*"?([^"\n]+)"?', fm, re.M)
    if not name or name.group(1).strip() != s:
        err(f"skills/{s}: frontmatter name does not match folder")
    if not re.search(r"^description:\s*\S", fm, re.M):
        err(f"skills/{s}: missing description")
    if not KEBAB.match(s):
        err(f"skills/{s}: folder is not kebab-case")
    r = re.search(r"^\s+rank:\s*(\d+)", fm, re.M)
    if r:
        rk = int(r.group(1))
        if rk in ranks:
            err(f"duplicate rank {rk}: {ranks[rk]} and {s}")
        ranks[rk] = s
    for ref in re.findall(r"`(references/[^`]+)`", text):
        if not os.path.isfile(os.path.join(skills_dir, s, ref)):
            err(f"skills/{s}: referenced file missing: {ref}")
missing_ranks = sorted(set(range(1, 101)) - set(ranks))
if missing_ranks:
    err(f"ranks missing from 1-100: {missing_ranks}")
notes.append(f"{len(skills)} skills OK ({len(ranks)} ranked + {len(skills) - len(ranks)} core)")

# 4. Agents
agents_dir = os.path.join(PLUGIN, "agents")
agents = sorted(f for f in os.listdir(agents_dir) if f.endswith(".md"))
routed = set()
for a in agents:
    fm, text = frontmatter(os.path.join(agents_dir, a))
    if fm is None:
        err(f"agents/{a}: no frontmatter")
        continue
    name = re.search(r"^name:\s*(\S+)", fm, re.M)
    if not name or name.group(1) != a[:-3]:
        err(f"agents/{a}: name does not match file")
    if "<example>" not in fm:
        err(f"agents/{a}: description has no <example> blocks")
    for ref in re.findall(r"^- `([a-z0-9-]+)` \(#", text, re.M):
        if ref not in skills:
            err(f"agents/{a}: references unknown skill {ref}")
        routed.add(ref)
unrouted = sorted(set(ranks.values()) - routed)
if unrouted:
    err(f"ranked skills not owned by any agent: {unrouted}")
notes.append(f"{len(agents)} agents OK, {len(routed)} skills routed")

# 5. Cross-references in core skills
for core in ("get-found-command-center", "get-found-heartbeat"):
    text = open(os.path.join(skills_dir, core, "SKILL.md"), encoding="utf-8").read()
    for ref in set(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", text)):
        if ref.startswith("get-found/") or ref in skills:
            continue
        if "-" in ref and not ref.endswith(".md") and ref not in ("business-brain",):
            err(f"{core}: references unknown skill `{ref}`")
notes.append("command center + heartbeat cross-references OK")

print("\n".join("  ✓ " + n for n in notes))
if errors:
    print(f"\nFAILED with {len(errors)} error(s):")
    print("\n".join("  ✗ " + e for e in errors))
    sys.exit(1)
print("\nAll checks passed.")
