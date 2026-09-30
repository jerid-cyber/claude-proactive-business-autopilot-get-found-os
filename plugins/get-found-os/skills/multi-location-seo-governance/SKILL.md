---
name: multi-location-seo-governance
description: "Keep 5-500 locations consistent and ranking on maps and AI. Runs the Get-Found 4-phase method (Discovery, Design, Build, Optimize) as an agent and proves results against a baseline: % of locations meeting standard; calls per location. This skill should be used when a business owner asks for help with multi-location seo governance, when the Get-Found command center routes a next best move here, or when a scheduled Get-Found heartbeat reaches this skill."
metadata:
  rank: 63
  channel: "Organic"
  department: "Mapmaker"
  autonomy: "Agent-heavy"
  cadence: "Monthly"
  edition: "Get-Found Full OS"
---

# Multi-Location SEO Governance

**Get-Found #63 of 100** · Department: Mapmaker (Listings & Entity) · Channel: Organic · Autonomy: Agent-heavy · Monitor: Monthly

Part of the Get-Found agent, built on Jerid Wempen's 4-Phase System. Mission: help businesses of every industry get found, get chosen and grow.

## Purpose

Keep 5-500 locations consistent and ranking on maps and AI.

## Agent operating mode

**Agent-heavy.** Do everything except the human step. Human step: Location managers approve and carry out some changes at each location. Prepare that step so it takes the owner minutes (exact text, links, checklist), add it to the approvals queue, and continue with the rest of the work.

Before starting:

1. Read the Business Brain (`get-found/business-brain.md` in the connected folder or project). If it is missing, run the `business-brain-setup` skill first.
2. Read `get-found/scoreboard.md` for any existing baseline for this skill's KPIs.
3. Check which connectors are live (see the plugin's CONNECTORS.md) and use them before asking the owner for anything.

After finishing:

- Append what changed to `get-found/action-log.md` (date, skill, change, link, expected KPI effect).
- Record new KPI values in `get-found/scoreboard.md`.
- Put anything that publishes, sends, spends or changes a live account into `get-found/approvals.md` and wait for a yes.

## Triggers

- The owner asks for help with multi-location seo governance, or the Visibility Audit flagged it as a gap.
- Routed by the command center's next-best-move ranking.

## Phase 1: Discovery & Assessment

Goal: define the current state and record a baseline.

- Audit every location's profile, pages and reviews.
- Record the baseline for every KPI below in the scoreboard (metric, current value, source, date).
- Summarize the top gaps between current and desired state, ranked by impact on revenue.

Output: audit report + baseline scorecard + gap list.

## Phase 2: Architecture & Design

Goal: blueprint the fix before building anything.

- Design standards.
- Map dependencies (tools, accounts, people, content) and what must happen first.
- Run a quick failure-mode check: list 3-5 things that could go wrong, their impact, and the mitigation built into the plan.
- Get the owner's sign-off on the plan, targets and anything that spends money or publishes publicly.

Output: plan with owners and dates + risk table + sign-off.

## Phase 3: Implementation & Deployment

Goal: build and launch in stages without breaking what works.

- Roll out by wave.
- Build in small sprints; QA each piece against the plan (accuracy, links, tracking, compliance, brand voice from the Business Brain).
- Launch in stages with a rollback path; log every change in the action log.

Output: live assets (or, in the Visibility Audit edition, a build brief) + launch log.

## Phase 4: Optimization & Governance

Goal: prove the result and keep it from degrading.

- Audit monthly.
- Re-check on a **monthly** cadence through the Get-Found heartbeat.
- Compare every KPI to the Phase 1 baseline; report the change in plain language with the dollar impact where possible.
- Write a short SOP so the business (or its team) can repeat the work, and set the next review date.

Output: results report vs. baseline + SOP + review schedule.

## Measurable result

**% of locations meeting standard; calls per location.** Targets are goals measured against the Phase 1 baseline, not guarantees; state any assumption behind a target.

## Channel guidance

- Measure in both worlds: rankings/clicks AND brand mentions, AI citations and Share of Model Voice, since most searches now end without a click.
- Write answer-first: the direct answer in the first 1-2 sentences, then proof, then detail.
- Keep facts identical everywhere (site, GBP, listings, schema, reviews); AI engines cross-check sources.
- Earn presence on the third-party sites AI engines cite (Reddit, YouTube, LinkedIn, review platforms, trusted press).
- Never publish fake reviews, undisclosed self-promotion, doorway pages or unedited mass AI content.

## Approval gates and guardrails

- Never fabricate data, reviews, testimonials, citations or results. Label estimates as estimates.
- Get explicit owner approval before publishing, sending messages, changing live accounts or spending money.
- Follow platform rules and applicable law (FTC endorsements, CAN-SPAM, TCPA, privacy, and industry rules such as RESPA, fair housing or HIPAA).

## Related skills

- `ecommerce-product-seo-free-listings` (Ecommerce Product SEO & Free Listings, #62)
- `image-visual-voice-search` (Image, Visual & Voice Search, #61)
- `ai-crawler-access-agent-readiness` (AI Crawler Access & Agent-Readiness, #49)
