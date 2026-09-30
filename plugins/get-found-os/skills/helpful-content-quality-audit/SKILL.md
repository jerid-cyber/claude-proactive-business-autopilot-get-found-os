---
name: helpful-content-quality-audit
description: "Make sure AI-assisted content helps readers and does not sink rankings. Runs the Get-Found 4-phase method (Discovery, Design, Build, Optimize) as an agent and proves results against a baseline: Low-quality pages fixed or removed; rankings on audited pages up. This skill should be used when a business owner asks for help with helpful content & ai-content quality audit, when the Get-Found command center routes a next best move here, or when a scheduled Get-Found heartbeat reaches this skill."
metadata:
  rank: 42
  channel: "Organic"
  department: "Publisher"
  autonomy: "Autopilot"
  cadence: "Monthly"
  edition: "Get-Found Full OS"
---

# Helpful Content & AI-Content Quality Audit

**Get-Found #42 of 100** · Department: Publisher (Content Engine) · Channel: Organic · Autonomy: Autopilot · Monitor: Monthly · New in Version 3

Part of the Get-Found agent, built on Jerid Wempen's 4-Phase System. Mission: help businesses of every industry get found, get chosen and grow.

## Purpose

Make sure AI-assisted content helps readers and does not sink rankings.

## Agent operating mode

**Autopilot.** Run every phase yourself. Stop only at the approval gates below. Work from connected tools first; fall back to exports, public data and web research.

Before starting:

1. Read the Business Brain (`get-found/business-brain.md` in the connected folder or project). If it is missing, run the `business-brain-setup` skill first.
2. Read `get-found/scoreboard.md` for any existing baseline for this skill's KPIs.
3. Check which connectors are live (see the plugin's CONNECTORS.md) and use them before asking the owner for anything.

After finishing:

- Append what changed to `get-found/action-log.md` (date, skill, change, link, expected KPI effect).
- Record new KPI values in `get-found/scoreboard.md`.
- Put anything that publishes, sends, spends or changes a live account into `get-found/approvals.md` and wait for a yes.

## Triggers

- The owner asks for help with helpful content & ai-content quality audit, or the Visibility Audit flagged it as a gap.
- A page loses 20%+ clicks month over month in Search Console

## Phase 1: Discovery & Assessment

Goal: define the current state and record a baseline.

- Audit pages for thin, generic or unverified content.
- Record the baseline for every KPI below in the scoreboard (metric, current value, source, date).
- Summarize the top gaps between current and desired state, ranked by impact on revenue.

Output: audit report + baseline scorecard + gap list.

## Phase 2: Architecture & Design

Goal: blueprint the fix before building anything.

- Design an edit standard.
- Map dependencies (tools, accounts, people, content) and what must happen first.
- Run a quick failure-mode check: list 3-5 things that could go wrong, their impact, and the mitigation built into the plan.
- Get the owner's sign-off on the plan, targets and anything that spends money or publishes publicly.

Output: plan with owners and dates + risk table + sign-off.

## Phase 3: Implementation & Deployment

Goal: build and launch in stages without breaking what works.

- Rewrite with real experience or remove.
- Build in small sprints; QA each piece against the plan (accuracy, links, tracking, compliance, brand voice from the Business Brain).
- Launch in stages with a rollback path; log every change in the action log.

Output: live assets (or, in the Visibility Audit edition, a build brief) + launch log.

## Phase 4: Optimization & Governance

Goal: prove the result and keep it from degrading.

- Track rankings.
- Re-check on a **monthly** cadence through the Get-Found heartbeat.
- Compare every KPI to the Phase 1 baseline; report the change in plain language with the dollar impact where possible.
- Write a short SOP so the business (or its team) can repeat the work, and set the next review date.

Output: results report vs. baseline + SOP + review schedule.

## Measurable result

**Low-quality pages fixed or removed; rankings on audited pages up.** Targets are goals measured against the Phase 1 baseline, not guarantees; state any assumption behind a target.

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

- `local-link-authority-building` (Local Link & Authority Building, #41)
- `industry-b2b-review-platforms` (Industry & B2B Review Platforms, #43)
- `linkedin-company-leader-authority` (LinkedIn Company & Leader Authority, #44)
