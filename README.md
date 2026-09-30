<div align="center">

# Get-Found OS

**A 100-skill AI marketing operating system for Claude.**
Get found in Google, Google Maps and AI answers — get chosen — and grow.

One orchestrator · nine specialist department agents · 100 ranked skills · one 4-phase method

![Version](https://img.shields.io/badge/version-1.0.0-2563eb)
![Skills](https://img.shields.io/badge/skills-103-16a34a)
![Agents](https://img.shields.io/badge/agents-9-9333ea)
![Claude](https://img.shields.io/badge/Claude-Cowork%20%7C%20Code-d97706)
![License](https://img.shields.io/badge/license-Proprietary-6b7280)
[![Validate](https://github.com/YOUR-GITHUB-USERNAME/get-found-os/actions/workflows/validate.yml/badge.svg)](https://github.com/YOUR-GITHUB-USERNAME/get-found-os/actions/workflows/validate.yml)

**[⬇ Download the plugin](https://github.com/YOUR-GITHUB-USERNAME/get-found-os/releases/latest/download/get-found-os.plugin)** ·
[Install](#install) · [Quick start](#quick-start) · [How it works](#how-it-works) · [All 100 skills](docs/SKILLS.md)

</div>

---

## What it is

Get-Found OS turns Claude into a full marketing department for a local or growing business. It is built on
**Jerid Wempen's 4-Phase System** — *Discovery & Assessment → Architecture & Design → Implementation & Deployment →
Optimization & Governance* — and applies that method to every channel a buyer (or an AI engine) uses to find a business:

- **Maps & listings** — Google Business Profile, Apple Maps, Bing, directories, NAP consistency, schema and knowledge panel
- **AI answers** — Share of Model Voice in ChatGPT, Gemini, Perplexity, Claude and Google AI Overviews / AI Mode; correcting wrong facts AI states
- **Search** — keyword & prompt research, on-page and technical SEO, location pages, topical authority, content refresh
- **Reviews & proof** — review generation and replies everywhere, case studies, NPS, referrals, crisis response
- **Social & video** — social search, YouTube SEO, short-form scripts, LinkedIn authority, creators and community
- **Paid** — Google Ads, Meta Ads, LSA/Yelp, retargeting, retail media, Google Ad Grants
- **Conversion & sales** — speed-to-lead, AI receptionist, landing pages, offers, pricing pages, nurture, proposals, reactivation
- **Money & operations** — tracking & attribution, KPI dashboard, LTV/CAC, cash-flow budgeting, compliance, SOPs, platform risk

The **Command Center** keeps a single **Visibility Score (0–100)**, picks the *next best move* with a published formula,
routes it to the right department agent, and proves the result against a recorded baseline. The **Heartbeat** puts the
whole system on a daily / weekly / monthly / quarterly schedule.

**Nothing is published, sent, spent or changed in a live account without an explicit yes.**

---

## What's inside

| Component | Count | Details |
| --- | --- | --- |
| Ranked Get-Found skills | **100** | Each runs the full 4-phase method with a KPI target — [full catalog](docs/SKILLS.md) |
| Core system skills | **3** | `get-found-command-center` (orchestrator), `business-brain-setup` (onboarding), `get-found-heartbeat` (scheduling) |
| Department agents | **9** | Scout, Mapmaker, Reputation Desk, Publisher, Engineer, Closer, Media Buyer, COO-CFO, Amplifier — [details](docs/AGENTS.md) |
| Reference files | **3** | Business Brain template, 100-skill routing catalog, Visibility Score rubric |
| Event-trigger chains | **13** | Automatic skill chains for reviews, traffic drops, new services, slow leads, CPL spikes and more — [details](docs/WORKFLOWS.md) |
| Scheduled cadences | **4** | Daily, weekly, monthly, quarterly heartbeat prompts |

### The nine department agents

| Agent | Department | Skills | Mission |
| --- | --- | --- | --- |
| **Scout** | Research & Intelligence | 8 | Finds where the business is visible, where it's invisible, and what buyers and AI engines actually say |
| **Mapmaker** | Listings & Entity | 10 | Owns every map, listing, directory and entity record so search engines and AI agree on who the business is |
| **Reputation Desk** | Reviews, Proof & Referrals | 7 | Keeps ratings fresh, replies to every review, turns happy customers into proof and referrals, contains crises |
| **Publisher** | Content Engine | 17 | Turns buyer questions into answer-first content that ranks, gets cited by AI and sounds like the business |
| **Engineer** | Technical & Tracking | 10 | Makes the site fast, crawlable, accessible, machine-readable and correctly tracked |
| **Closer** | Conversion & Sales | 14 | Turns traffic into leads and leads into customers: fast response, sharp offers, pages that convert, follow-up that never stops |
| **Media Buyer** | Paid Media | 6 | Buys attention profitably on Google, Meta and pay-per-lead platforms, scaling only what the data proves |
| **COO-CFO** | Measurement, Money & Operations | 12 | Proves what marketing is worth, protects cash and margin, keeps the machine compliant and documented |
| **Amplifier** | Authority, Social & Community | 16 | Earns mentions, links, press, community and creator content in the places AI engines and buyers trust |

---

## Install

### Option A — Claude desktop / Cowork (one click)

1. **[Download `get-found-os.plugin`](https://github.com/YOUR-GITHUB-USERNAME/get-found-os/releases/latest/download/get-found-os.plugin)** from the latest release
   (or use `dist/get-found-os.plugin` in this repo).
2. In Claude, open **Customize → Plugins** (or drag the file into a chat) and upload `get-found-os.plugin`.
3. Accept the plugin. All 103 skills and 9 agents appear under the `get-found-os:` namespace.

### Option B — Claude Code (plugin marketplace)

This repo is a Claude plugin marketplace. In Claude Code run:

```bash
/plugin marketplace add YOUR-GITHUB-USERNAME/get-found-os
/plugin install get-found-os@get-found
```

Update later with `/plugin marketplace update get-found`.

### Option C — Team / organization marketplace

Admins can add `https://github.com/YOUR-GITHUB-USERNAME/get-found-os` as a GitHub-synced plugin marketplace in their
organization's plugin settings, so everyone on the team gets the plugin and future updates automatically.

Full instructions, including private-repo installs and troubleshooting: **[docs/INSTALL.md](docs/INSTALL.md)**.

---

## Quick start

Say these to Claude, in order:

| Step | Say | What happens |
| --- | --- | --- |
| 1 | **"Set up Get-Found for my business"** | `business-brain-setup` researches your website, GBP, reviews, socials and AI answers, pre-fills the Business Brain and asks only for what it couldn't find (offers, best customers, competitors, season, compliance, approver, spend limit) |
| 2 | **"Run my Visibility Audit"** | `get-found-visibility-audit` scores all 7 pillars and sets your baseline Visibility Score (0–100) |
| 3 | **"Put Get-Found on a schedule"** | `get-found-heartbeat` creates daily, weekly, monthly and quarterly scheduled tasks |
| 4 | **"What's my next best move?"** | `get-found-command-center` ranks every open gap and runs the top 1–3 moves |

Or call any skill directly: *"Optimize my Google Business Profile"*, *"Fix what ChatGPT says about us"*,
*"Build a speed-to-lead system"*, *"Launch Meta ads"*, *"Write our location pages"* …

### Work files

Everything the system knows and does is kept in plain Markdown in a `get-found/` folder (your connected folder, or the Claude project):

| File | Purpose |
| --- | --- |
| `get-found/business-brain.md` | Master record: NAP+, offers & pricing, best customers, markets & competitors, brand voice, compliance rules, seasonality, connected accounts, approval rules |
| `get-found/scoreboard.md` | Visibility Score by pillar and every KPI baseline + current value, with source and date |
| `get-found/action-log.md` | Every change: date, skill, change, link, expected KPI effect |
| `get-found/approvals.md` | Batch approval queue — one-line summary, preview and expected KPI effect for anything public, sent, spent or live |

---

## How it works

```
                        ┌──────────────────────────────┐
  Owner / Heartbeat ──▶ │   get-found-command-center   │ ◀── Event triggers (13 chains)
                        │ reads Business Brain + Score │
                        │ ranks gaps → next best move  │
                        └──────────────┬───────────────┘
                                       │ routes 1–3 moves per cycle
   ┌────────┬──────────┬───────────┬───┴──────┬─────────┬─────────┬────────────┬─────────┬───────────┐
   ▼        ▼          ▼           ▼          ▼         ▼         ▼            ▼         ▼
 Scout  Mapmaker  Reputation   Publisher  Engineer   Closer   Media Buyer  COO-CFO  Amplifier
                     Desk
   │  each agent runs its skills through the 4 phases:                                 │
   │  1 Discovery & Assessment → 2 Architecture & Design →                             │
   │  3 Implementation & Deployment → 4 Optimization & Governance                      │
   └──────────────▶ scoreboard.md · action-log.md · approvals.md (waits for a yes) ◀────┘
```

### The 4-phase method (inside every skill)

| Phase | Goal | Output |
| --- | --- | --- |
| **1. Discovery & Assessment** | Define the current state; record a baseline for every KPI | Audit report + baseline scorecard + ranked gap list |
| **2. Architecture & Design** | Blueprint the fix; map dependencies; 3–5 item failure-mode check; owner sign-off | Plan with owners and dates + risk table + sign-off |
| **3. Implementation & Deployment** | Build in small sprints, QA against the plan, launch in stages with rollback | Live assets + launch log |
| **4. Optimization & Governance** | Track KPIs on cadence, compare to baseline, write an SOP, set next review | Results vs. baseline + SOP + review schedule |

### Visibility Score (0–100)

| Pillar | Points | Full marks look like |
| --- | --- | --- |
| Maps & listings | 15 | Top-3 map pack on core terms; GBP complete and posting weekly; NAP 95%+ consistent; Apple/Bing verified |
| AI answers | 20 | Named in 40%+ of buyer prompts across ChatGPT, Gemini, Perplexity, Claude and Google AI; 95%+ accurate |
| Search | 15 | 90%+ of buyer intents mapped to a page; priority pages indexed; target terms top 10 |
| Reviews & proof | 15 | 4.5+ on every site that matters; a new review every 2 weeks per site; 100% replies in 24h |
| Social & video | 10 | Active, consistent profiles; search-optimized video; profile-to-site clicks tracked |
| Paid | 10 | Tracking verified; cost per lead at or below target; no wasted spend |
| Conversion | 15 | Lead response under 5 minutes; clear offer; site conversion at or above industry median |

Unmeasured pillars score 0 until evidence exists. Full re-score quarterly; AI answers and Maps re-scored monthly.

### Next-best-move formula

```
priority = (Visibility Score points at stake × revenue weight) ÷ effort
```

- **Revenue weight:** 3 = sits between a buyer and a booked job (conversion, speed-to-lead, maps, reviews) · 2 = drives qualified traffic · 1 = long-term authority
- **Effort:** 1 = under an hour, no human step · 2 = a day or one small human step · 3 = multi-week or developer/owner-heavy
- Ties go to the lower Get-Found rank. Max 3 moves per cycle, one change at a time per channel so results can be attributed.

### Event triggers & heartbeat

13 conditions automatically queue skill chains — e.g. a 1–2★ review runs `reputation-crisis-response → reviews-everywhere-engine → ai-brand-accuracy-correction`;
a 25%+ cost-per-lead spike runs `meta-ads-launch-scale → google-ads-search-launcher → conversion-leak-finder → retargeting-architecture`.
The heartbeat schedules 8 daily, 14 weekly, 66 monthly and 12 quarterly skill checks. Full tables: **[docs/WORKFLOWS.md](docs/WORKFLOWS.md)**.

---

## Connectors

The agents work with whatever is connected and fall back to exports, public data and web research. More connections = less asking.

| Need | Recommended connector | Used by | Without it |
| --- | --- | --- | --- |
| Search, ads and analytics data | Supermetrics (Google Ads, Meta Ads, GA4, Search Console) or native Google connectors | Scout, Engineer, Media Buyer, COO-CFO | Owner exports CSVs |
| CRM, SMS, email, pipelines, review requests | GoHighLevel (or Lofty/HubSpot) via connector or Zapier | Closer, Reputation Desk | Agent drafts; owner sends |
| Email and calendar | Gmail and Google Calendar | Closer, Reputation Desk, Amplifier | Drafts delivered in chat |
| Files and reports | Google Drive (or a connected folder) | All | Files delivered in chat |
| Website | WordPress / Webflow / Shopify connector | Publisher, Engineer | Copy and code delivered for manual paste |
| Google Business Profile | GBP connector or Zapier | Mapmaker, Reputation Desk | Agent drafts posts/replies; owner posts |
| Keyword and SERP data | DataForSEO, Semrush or Ahrefs connector | Scout, Publisher | Web research and Search Console only |
| AI engine testing | Web search plus manual prompt runs (ChatGPT, Gemini, Perplexity) | Scout | Agent provides the prompt set; owner pastes results |
| Images and video | Image/video generation connector (e.g. OpenArt) | Publisher, Amplifier | Shot lists and briefs only |

Connect tools in Claude's connector settings. **Never paste passwords or API keys into chat or into the Business Brain.**

---

## Safety & guardrails

- **Approval gates are never skipped.** Publishing anything public, messaging customers or prospects, changing a live account or spending money requires an explicit yes from the approver named in the Business Brain. Approvals are batched in `approvals.md` so the owner can clear many in one pass.
- **No fabrication.** Never invents data, reviews, testimonials, AI citations or results; estimates are labeled.
- **Compliance built in.** FTC endorsement rules, CAN-SPAM, TCPA, privacy law and industry rules (RESPA, fair housing, HIPAA as applicable), plus platform policies.
- **No secrets stored.** The Business Brain records *which tool* holds payment details, passwords or customer data — never the data itself.
- **Targets are goals, not guarantees** — always measured against the Phase 1 baseline.

---

## Repository layout

```
get-found-os/
├── .claude-plugin/
│   └── marketplace.json          # Makes this repo an installable Claude plugin marketplace
├── plugins/
│   └── get-found-os/             # ← the plugin itself (upload/zip this folder)
│       ├── .claude-plugin/plugin.json
│       ├── README.md
│       ├── CONNECTORS.md
│       ├── agents/               # 9 department agents
│       └── skills/               # 103 skills (100 ranked + 3 core), each skills/<name>/SKILL.md
│           ├── business-brain-setup/references/business-brain-template.md
│           └── get-found-command-center/references/{skill-catalog.md, visibility-score.md}
├── dist/get-found-os.plugin      # Prebuilt installable plugin file
├── docs/                         # INSTALL, ARCHITECTURE, AGENTS, WORKFLOWS, SKILLS (full catalog), DEPLOY
├── scripts/                      # validate.py, build_catalog.py, package.sh, set-github-owner.sh
└── .github/workflows/            # CI validation + automatic release packaging
```

---

## Maintaining & releasing

```bash
python3 scripts/validate.py        # check manifests, 103 skills, 9 agents, all cross-references
python3 scripts/build_catalog.py   # regenerate docs/SKILLS.md after editing skills
bash scripts/package.sh            # build dist/get-found-os.plugin
git tag v1.0.1 && git push --tags  # GitHub Actions builds and attaches the .plugin to a Release
```

When you change the plugin, bump `version` in **both** `plugins/get-found-os/.claude-plugin/plugin.json` and
`.claude-plugin/marketplace.json`, and add an entry to [CHANGELOG.md](CHANGELOG.md). See **[docs/DEPLOY.md](docs/DEPLOY.md)**.

---

## Author & license

Created by **Jerid Wempen** — [TitanOne Realty Group](https://titanonerealty.com) / TitanOne Media.
Mission: help businesses of every industry get found, get chosen and grow.

**Proprietary — © 2026 Jerid Wempen. All rights reserved.** See [LICENSE](LICENSE). Public visibility of this repository
does not grant a license to copy, modify, resell or redistribute the plugin.
