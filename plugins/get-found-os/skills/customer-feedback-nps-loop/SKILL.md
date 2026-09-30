---
name: customer-feedback-nps-loop
description: "Hear customers, fix issues and route promoters to reviews. Runs the Get-Found 4-phase method (Discovery, Design, Build, Optimize) as an agent and proves results against a baseline: NPS trend; promoter-to-review rate. This skill should be used when a business owner asks for help with customer feedback & nps loop, when the Get-Found command center routes a next best move here, or when a scheduled Get-Found heartbeat reaches this skill."
metadata:
  rank: 52
  channel: "Retention"
  department: "Reputation Desk"
  autonomy: "Autopilot"
  cadence: "Monthly"
  edition: "Get-Found Full OS"
---

# Customer Feedback & NPS Loop

**Get-Found #52 of 100** · Department: Reputation Desk (Reviews, Proof & Referrals) · Channel: Retention · Autonomy: Autopilot · Monitor: Monthly

Part of the Get-Found agent, built on Jerid Wempen's 4-Phase System. Mission: help businesses of every industry get found, get chosen and grow.

## Purpose

Hear customers, fix issues and route promoters to reviews.

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

- The owner asks for help with customer feedback & nps loop, or the Visibility Audit flagged it as a gap.
- A new customer becomes a promoter (NPS 9-10) or leaves a 5-star review

## Phase 1: Discovery & Assessment

Goal: define the current state and record a baseline.

- Design NPS and feedback asks.
- Record the baseline for every KPI below in the scoreboard (metric, current value, source, date).
- Summarize the top gaps between current and desired state, ranked by impact on revenue.

Output: audit report + baseline scorecard + gap list.

## Phase 2: Architecture & Design

Goal: blueprint the fix before building anything.

- Route promoters and detractors.
- Map dependencies (tools, accounts, people, content) and what must happen first.
- Run a quick failure-mode check: list 3-5 things that could go wrong, their impact, and the mitigation built into the plan.
- Get the owner's sign-off on the plan, targets and anything that spends money or publishes publicly.

Output: plan with owners and dates + risk table + sign-off.

## Phase 3: Implementation & Deployment

Goal: build and launch in stages without breaking what works.

- Automate.
- Build in small sprints; QA each piece against the plan (accuracy, links, tracking, compliance, brand voice from the Business Brain).
- Launch in stages with a rollback path; log every change in the action log.

Output: live assets (or, in the Visibility Audit edition, a build brief) + launch log.

## Phase 4: Optimization & Governance

Goal: prove the result and keep it from degrading.

- Report themes.
- Re-check on a **monthly** cadence through the Get-Found heartbeat.
- Compare every KPI to the Phase 1 baseline; report the change in plain language with the dollar impact where possible.
- Write a short SOP so the business (or its team) can repeat the work, and set the next review date.

Output: results report vs. baseline + SOP + review schedule.

## Measurable result

**NPS trend; promoter-to-review rate.** Targets are goals measured against the Phase 1 baseline, not guarantees; state any assumption behind a target.

## Channel guidance

- Keeping a customer costs less than finding one; tie every touch to a customer moment.
- Route happy customers to reviews and referrals.

## Approval gates and guardrails

- Never fabricate data, reviews, testimonials, citations or results. Label estimates as estimates.
- Get explicit owner approval before publishing, sending messages, changing live accounts or spending money.
- Follow platform rules and applicable law (FTC endorsements, CAN-SPAM, TCPA, privacy, and industry rules such as RESPA, fair housing or HIPAA).

## Related skills

- `customer-onboarding-retention` (Customer Onboarding & Retention, #70)
- `loyalty-upsell-repeat-purchase` (Loyalty, Upsell & Repeat Purchase, #71)
- `customer-database-reactivation` (Customer Database Reactivation, #31)
