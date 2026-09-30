---
name: case-study-testimonial-engine
description: "Create proof stories that rank, convert and build E-E-A-T. Runs the Get-Found 4-phase method (Discovery, Design, Build, Optimize) as an agent and proves results against a baseline: Conversion lift on pages using case studies. This skill should be used when a business owner asks for help with case study & testimonial engine, when the Get-Found command center routes a next best move here, or when a scheduled Get-Found heartbeat reaches this skill."
metadata:
  rank: 37
  channel: "Trust"
  department: "Reputation Desk"
  autonomy: "Agent-heavy"
  cadence: "Monthly"
  edition: "Get-Found Full OS"
---

# Case Study & Testimonial Engine

**Get-Found #37 of 100** · Department: Reputation Desk (Reviews, Proof & Referrals) · Channel: Trust · Autonomy: Agent-heavy · Monitor: Monthly

Part of the Get-Found agent, built on Jerid Wempen's 4-Phase System. Mission: help businesses of every industry get found, get chosen and grow.

## Purpose

Create proof stories that rank, convert and build E-E-A-T.

## Agent operating mode

**Agent-heavy.** Do everything except the human step. Human step: Customer consent and interviews need a person; the agent writes and formats the stories. Prepare that step so it takes the owner minutes (exact text, links, checklist), add it to the approvals queue, and continue with the rest of the work.

Before starting:

1. Read the Business Brain (`get-found/business-brain.md` in the connected folder or project). If it is missing, run the `business-brain-setup` skill first.
2. Read `get-found/scoreboard.md` for any existing baseline for this skill's KPIs.
3. Check which connectors are live (see the plugin's CONNECTORS.md) and use them before asking the owner for anything.

After finishing:

- Append what changed to `get-found/action-log.md` (date, skill, change, link, expected KPI effect).
- Record new KPI values in `get-found/scoreboard.md`.
- Put anything that publishes, sends, spends or changes a live account into `get-found/approvals.md` and wait for a yes.

## Triggers

- The owner asks for help with case study & testimonial engine, or the Visibility Audit flagged it as a gap.
- A new customer becomes a promoter (NPS 9-10) or leaves a 5-star review

## Phase 1: Discovery & Assessment

Goal: define the current state and record a baseline.

- Find the best customer wins.
- Record the baseline for every KPI below in the scoreboard (metric, current value, source, date).
- Summarize the top gaps between current and desired state, ranked by impact on revenue.

Output: audit report + baseline scorecard + gap list.

## Phase 2: Architecture & Design

Goal: blueprint the fix before building anything.

- Design a story template and consent process.
- Map dependencies (tools, accounts, people, content) and what must happen first.
- Run a quick failure-mode check: list 3-5 things that could go wrong, their impact, and the mitigation built into the plan.
- Get the owner's sign-off on the plan, targets and anything that spends money or publishes publicly.

Output: plan with owners and dates + risk table + sign-off.

## Phase 3: Implementation & Deployment

Goal: build and launch in stages without breaking what works.

- Write and publish.
- Build in small sprints; QA each piece against the plan (accuracy, links, tracking, compliance, brand voice from the Business Brain).
- Launch in stages with a rollback path; log every change in the action log.

Output: live assets (or, in the Visibility Audit edition, a build brief) + launch log.

## Phase 4: Optimization & Governance

Goal: prove the result and keep it from degrading.

- Track usage and lift.
- Re-check on a **monthly** cadence through the Get-Found heartbeat.
- Compare every KPI to the Phase 1 baseline; report the change in plain language with the dollar impact where possible.
- Write a short SOP so the business (or its team) can repeat the work, and set the next review date.

Output: results report vs. baseline + SOP + review schedule.

## Measurable result

**Conversion lift on pages using case studies.** Targets are goals measured against the Phase 1 baseline, not guarantees; state any assumption behind a target.

## Channel guidance

- Only use real customers and results, with written consent.
- Put proof next to the decision point.

## Approval gates and guardrails

- Never fabricate data, reviews, testimonials, citations or results. Label estimates as estimates.
- Get explicit owner approval before publishing, sending messages, changing live accounts or spending money.
- Follow platform rules and applicable law (FTC endorsements, CAN-SPAM, TCPA, privacy, and industry rules such as RESPA, fair housing or HIPAA).

## Related skills

- `industry-b2b-review-platforms` (Industry & B2B Review Platforms, #43)
- `awards-best-of-lists` (Awards & Best-Of List Visibility, #48)
- `referral-program-builder` (Referral Program Builder, #50)
