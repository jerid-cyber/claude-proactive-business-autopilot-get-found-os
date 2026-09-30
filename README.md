# Get-Found OS

![License: PolyForm Internal Use](https://img.shields.io/badge/license-PolyForm%20Internal%20Use-lightgrey.svg)

**The AI marketing department that helps any business get found in Google, Maps and AI answers, then turns that
attention into customers.**

Get-Found OS is a Claude plugin with 100 marketing skills, 9 specialist department agents, and a command center that
runs them on a schedule. Built on Jerid Wempen's 4-Phase System: Discovery & Assessment, Architecture & Design,
Implementation & Deployment, Optimization & Governance.

Version 1.1.0 · Works in Claude Cowork and Claude Code · [Install guide](INSTALL.md) · [Changelog](CHANGELOG.md) ·
[License](LICENSE.md)

---

## Why it's different

Most marketing tools give you a checklist. Get-Found OS acts like a marketing team that works on a schedule. Each week it
finds your biggest visibility gap, fixes it, proves the result against a baseline, and moves on to the next one. It
never publishes, sends or spends without your yes.

## How easy it is to use

You talk to it in plain English. Four sentences take you from install to autopilot:

| Say this | What happens | Your time |
| --- | --- | --- |
| **"Set up Get-Found for my business."** | Researches your website, Google profile, reviews, listings and what AI tools say about you. Then asks one short round of questions for what it couldn't find. Builds your Business Brain. | About 10 minutes |
| **"Run my Visibility Audit."** | Scores you 0 to 100 across Maps, AI answers, Search, Reviews, Social, Paid and Conversion, with evidence for each score. | About 5 minutes to review |
| **"Put Get-Found on a schedule."** | Sets up daily, weekly, monthly and quarterly runs in your time zone. | About 5 minutes |
| **"What's my next best move?"** | Ranks your open gaps by revenue impact and effort and tells you what to do first. | Any time |

After that, most of your job is approving. Each run ends with a report you can read in about 30 seconds: your score
against baseline, what got done (with proof), what's waiting for your approval, and the next move. You approve many
items at once ("approve 1, 3, reject 2").

**How much it can do on its own depends on what you connect.** With nothing connected, it researches, audits, plans
and drafts everything, and you post it. With your CRM, Google Business Profile, analytics, ads and website connected, it
can carry each task through to the approval step, and run the actions you've pre-approved within the limits you set.
See [CONNECTORS.md](plugins/get-found-os/CONNECTORS.md).

## The Visibility Score

One number the whole system works to raise: a 0–100 score across seven pillars, measured from evidence and tracked
against your starting baseline. The audit sets the baseline (target: +20 points in 90 days); AI answers and Maps
pillars are re-checked monthly, the full score quarterly.

| Pillar | Points | What full marks look like |
| --- | --- | --- |
| AI answers | 20 | Named in 40%+ of buyer prompts across ChatGPT, Gemini, Perplexity, Claude and Google AI, with 95%+ accuracy |
| Maps & listings | 15 | Top 3 in the map pack on core terms; Google profile complete and posting weekly; NAP 95%+ consistent |
| Search | 15 | 90%+ of buyer questions mapped to a page; priority pages indexed; target terms in the top 10 |
| Reviews & proof | 15 | 4.5+ stars on every site that matters; a new review every 2 weeks per site; every review answered within 24 hours |
| Conversion | 15 | Leads answered in under 5 minutes; clear offer; site conversion at or above industry median |
| Social & video | 10 | Active, consistent profiles; search-optimized video; profile-to-site clicks tracked |
| Paid | 10 | Tracking verified; cost per lead at or under target; no wasted spend |

The Command Center picks your next move with a simple formula: **Priority = (score points at stake × revenue
weight) ÷ effort**. Gaps closest to money and easiest to fix go first — never more than three moves at a time, one
change per channel, so you always know what caused the result.

## What it can do

### Nine departments, 100 skills

| Department | What it owns | Skills |
| --- | --- | --- |
| **Scout** | Research & intelligence: visibility audit, AI search visibility, AI Overviews, keyword and prompt research, competitor gap reports, AI brand accuracy | 8 |
| **Mapmaker** | Google Business Profile and Maps, citations and NAP cleanup, Apple Maps and Bing, schema and knowledge panel, multi-location | 10 |
| **Reputation Desk** | Reviews on every site that matters, crisis response, case studies, referrals, NPS loop | 7 |
| **Publisher** | Answer-first content, location pages, comparison pages, content refresh, YouTube and short-form video, FAQ hub, E-E-A-T | 17 |
| **Engineer** | Technical SEO, speed and Core Web Vitals, tracking and attribution, AI crawler access, accessibility, safe site migrations | 10 |
| **Closer** | Speed-to-lead, AI receptionist, nurture sequences, reactivating past customers, proposals, landing pages, lead magnets, sales scripts | 14 |
| **Media Buyer** | Google Ads, Meta Ads, Local Services and Yelp ads, retargeting, retail media, nonprofit Ad Grants | 6 |
| **COO-CFO** | KPI dashboard, analytics, budget and cash-flow forecast, LTV/CAC channel mix, pricing and margin, compliance, SOPs | 12 |
| **Amplifier** | Reddit and Quora, social presence, LinkedIn authority, PR, podcasts, awards, community, partnerships, UGC and creators | 16 |

Every skill runs the same four phases: measure a baseline, design the fix, build it in stages, then prove the result
and keep it from slipping.

### It watches for problems and reacts

The command center chains skills together when something happens. For example:

- **A 1-2 star review lands:** crisis response, then a review push, then a check that AI tools haven't picked up a
  wrong story.
- **A lead waits more than 5 minutes:** the speed-to-lead and AI receptionist fixes are queued.
- **An AI engine gets your hours or prices wrong:** correction, schema update, then a citation cleanup.
- **A competitor passes you in the map pack:** gap report, then GBP and AI-visibility work.
- **Cost per lead jumps 25%:** an ad review, then a conversion-leak check.
- **Peak season is 6 weeks out:** seasonal campaign, then reactivating past customers, then a newsletter.

Thirteen triggers ship with it.

### The autopilot (new in 1.1.0)

| Feature | What it means for you |
| --- | --- |
| **Four approval levels** | Look, Draft, Act within limits, Ask first. Anything not written down counts as "ask first." |
| **Shadow mode** | For the first 3 to 5 runs, everything that would leave the business waits for your approval. |
| **Earned autonomy** | After 3 clean approvals in a row, it asks whether that kind of action (like replying to 5-star reviews) can run on its own within a daily cap. It loses that right the moment something is undone or complained about. |
| **Never twice** | Every send or post gets a unique key that's checked first, so a retried run can't double-send. |
| **Proof, not claims** | Work is marked done only when the result is read back from the tool. |
| **Learns your taste** | Every approval, edit or rejection becomes a Lesson that future runs follow. |
| **Safety limits** | Caps on tool calls, actions and daily sends per run. One word (`PAUSE`) stops everything. |
| **Can't be hijacked** | Reviews, emails and web pages are treated as information, never as instructions. |
| **Always asks first** | Spending money, contacting someone new, replying to low-star reviews, deleting anything, legal language. These never go on autopilot. |

### Schedule

| Cadence | What it does |
| --- | --- |
| Weekday mornings | New reviews and reply drafts, lead response times, ad spend anomalies, trigger checks |
| Monday | The weekly cycle: top 1-3 next best moves, carried through to the approval step |
| Thursday | One of four monthly batches (search & AI, listings & site, content & authority, customers & money), so every monthly skill runs once a month |
| 1st business day | One-page monthly report against baseline |
| Quarterly | Full re-score, competitor re-benchmark, new 90-day plan |

## What to expect

- **Week 1:** Business Brain, Visibility Score, a ranked gap list, and the first fixes drafted for approval.
- **Month 1:** Listings and AI-accuracy errors corrected, a review and lead-response routine in place, the first
  answer-first content published, the monthly report.
- **Quarter 1:** A re-score against your baseline. Each skill states a target (for example, GBP calls up 30% in 90 days,
  or a median lead response under 5 minutes). These are goals measured against your baseline, not guarantees.

## You stay in control

Research, drafting, internal reports and scoreboard updates run without asking. Anything that publishes, sends a
message to a customer or prospect, spends money, or changes a live account waits for your explicit yes — batched in
one approvals list with a one-line summary, a preview and the expected effect, so you can clear a week's worth in a
single pass.

Everything lives in a `get-found/` folder you can inspect any time:

| File | What's in it |
| --- | --- |
| `business-brain.md` | Your master business record: offers, customers, competitors, voice, compliance rules, approval limits |
| `scoreboard.md` | Every KPI baseline and the Visibility Score over time, with evidence and dates |
| `action-log.md` | Every change made: date, skill, what changed, link, expected effect |
| `approvals.md` | Everything waiting for your yes |

Built-in guardrails: it never makes up data, reviews, testimonials or AI citations, and it labels estimates. It
follows the compliance rules in your Business Brain (FTC, CAN-SPAM, TCPA, RESPA, fair housing). Targets are goals
measured against your baseline, not guarantees.

## Your data stays yours

The agent keeps its working files in a `get-found/` folder that **you** choose: Google Drive, a folder on your computer,
or a Claude project. It never stores passwords, payment details or customer personal data in those files.

## Quick reference: what to say

You never need to remember a skill name. These phrases cover almost everything:

| Say this | What happens |
| --- | --- |
| "Set up Get-Found for my business" | Builds or rebuilds your Business Brain |
| "Run my Visibility Audit" | Scores all 7 pillars and builds a 90-day plan |
| "How visible is my business?" | Current score vs. baseline, in plain language |
| "What's my next best move?" | Ranks gaps, recommends the top 1–3 |
| "Run my weekly Get-Found cycle" | Executes this week's moves up to the approval gates |
| "Put Get-Found on autopilot" | Sets up daily, weekly, monthly and quarterly runs |
| "Show me my approvals" | Lists everything waiting for your yes |
| "Give me my Get-Found report" | Score, work done, approvals waiting, next move |
| "Have the [agent] handle [task]" | Sends work straight to a specialist |
| "Help me with [any skill topic]" | Runs that skill directly |

## Install

See **[INSTALL.md](INSTALL.md)**. The short version for Claude Code:

```
/plugin marketplace add jerid-cyber/get-found-os
/plugin install get-found-os@get-found
```

## License

Licensed under the [PolyForm Internal Use License 1.0.0](LICENSE.md) — free to use for your internal operations,
including at work; you may not distribute, share copies, or sell it. © 2026 Jerid Wempen / TitanOne. Need different
terms? Contact Jerid Wempen.
