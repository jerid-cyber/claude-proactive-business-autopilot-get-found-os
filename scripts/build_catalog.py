#!/usr/bin/env python3
"""Regenerate docs/SKILLS.md from the SKILL.md frontmatter in the plugin.

Usage:  python3 scripts/build_catalog.py
Run this after adding or editing a skill so the public catalog stays accurate.
"""
import os
import re
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN = os.path.join(ROOT, "plugins", "get-found-os")
SKILLS = os.path.join(PLUGIN, "skills")
OUT = os.path.join(ROOT, "docs", "SKILLS.md")

DEPT_ORDER = OrderedDict([
    ("Scout", "Research & Intelligence"),
    ("Mapmaker", "Listings & Entity"),
    ("Reputation Desk", "Reviews, Proof & Referrals"),
    ("Publisher", "Content Engine"),
    ("Engineer", "Technical & Tracking"),
    ("Closer", "Conversion & Sales"),
    ("Media Buyer", "Paid Media"),
    ("COO-CFO", "Measurement, Money & Operations"),
    ("Amplifier", "Authority, Social & Community"),
])


def meta(fm, key):
    m = re.search(rf'^\s+{key}:\s*"?([^"\n]+)"?\s*$', fm, re.M)
    return m.group(1).strip() if m else None


def load():
    rows = []
    for slug in sorted(os.listdir(SKILLS)):
        path = os.path.join(SKILLS, slug, "SKILL.md")
        if not os.path.isfile(path):
            continue
        text = open(path, encoding="utf-8").read()
        fm = re.match(r"---\n(.*?)\n---", text, re.S).group(1)
        desc = re.search(r'^description:\s*"?(.*?)"?\s*$', fm, re.M).group(1)
        purpose = desc.split(" Runs the Get-Found")[0]
        kpi = re.search(r"against a baseline: (.*?)\. This skill", desc)
        title = re.search(r"^# (.+)$", text, re.M).group(1)
        rank = meta(fm, "rank")
        rows.append({
            "slug": slug, "title": title, "purpose": purpose,
            "kpi": kpi.group(1) if kpi else "",
            "rank": int(rank) if rank else None,
            "channel": meta(fm, "channel"), "dept": meta(fm, "department"),
            "autonomy": meta(fm, "autonomy"), "cadence": meta(fm, "cadence"),
        })
    return rows


def main():
    rows = load()
    core = [r for r in rows if r["rank"] is None]
    ranked = sorted([r for r in rows if r["rank"] is not None], key=lambda r: r["rank"])
    out = []
    out.append("# Get-Found OS — Complete Skill Catalog\n")
    out.append(f"**{len(ranked)} ranked Get-Found skills + {len(core)} core system skills = {len(rows)} skills total.** "
               "Generated from each skill's `SKILL.md` frontmatter by `scripts/build_catalog.py` — do not edit by hand.\n")
    out.append("Every ranked skill runs the same 4-phase method (Discovery & Assessment → Architecture & Design → "
               "Implementation & Deployment → Optimization & Governance) and proves its result against a recorded baseline.\n")
    out.append("**Autonomy levels:** *Autopilot* = the agent runs every phase and stops only at approval gates. "
               "*Agent-heavy* = the agent does nearly everything and preps one short human step. "
               "*Human-led, agent-coached* = a person does the core work (filming, photos, interviews) and the agent plans, coaches and packages it.\n")
    out.append("## Core system skills\n")
    out.append("| Skill | What it does |\n| --- | --- |")
    for r in core:
        out.append(f"| `{r['slug']}` — {r['title']} | {r['purpose']} |")
    out.append("")
    out.append("## All 100 skills by rank\n")
    out.append("| # | Skill | Department | Channel | Autonomy | Cadence | Purpose | KPI target |")
    out.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for r in ranked:
        out.append(f"| {r['rank']} | `{r['slug']}`<br>{r['title']} | {r['dept']} | {r['channel']} | {r['autonomy']} | "
                   f"{r['cadence']} | {r['purpose']} | {r['kpi']} |")
    out.append("")
    out.append("## Skills by department agent\n")
    for dept, focus in DEPT_ORDER.items():
        items = [r for r in ranked if r["dept"] == dept]
        out.append(f"### {dept} — {focus} ({len(items)} skills)\n")
        for r in items:
            out.append(f"- **#{r['rank']} `{r['slug']}`** ({r['autonomy']}, {r['cadence']}): {r['purpose']}")
        out.append("")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write("\n".join(out))
    print(f"Wrote {OUT}: {len(rows)} skills")


if __name__ == "__main__":
    main()
