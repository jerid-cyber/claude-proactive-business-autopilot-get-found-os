---
name: hyperlocal-neighborhood-marketing
description: "Win Nextdoor, local groups and neighborhood word of mouth. Runs the Get-Found 4-phase method (Discovery, Design, Build, Optimize) as an agent and proves results against a baseline: Neighborhood leads; recommendations received. This skill should be used when a business owner asks for help with hyperlocal neighborhood marketing, when the Get-Found command center routes a next best move here, or when a scheduled Get-Found heartbeat reaches this skill."
metadata:
  rank: 73
  channel: "Community"
  department: "Amplifier"
  autonomy: "Agent-heavy"
  cadence: "Weekly"
  edition: "Get-Found Full OS"
---

# Hyperlocal Neighborhood Marketing

**Get-Found #73 of 100** · Department: Amplifier (Authority, Social & Community) · Channel: Community · Autonomy: Agent-heavy · Monitor: Weekly

Part of the Get-Found agent, built on Jerid Wempen's 4-Phase System. Mission: help businesses of every industry get found, get chosen and grow.

## Purpose

Win Nextdoor, local groups and neighborhood word of mouth.

## Agent operating mode

**Agent-heavy.** Do everything except the human step. Human step: Nextdoor and local groups have no posting API and need a real neighbor account; the agent drafts, the owner posts. Prepare that step so it takes the owner minutes (exact text, links, checklist), add it to the approvals queue, and continue with the rest of the work.

Before starting:

1. Read the Business Brain (`get-found/business-brain.md` in the connected folder or project). If it is missing, run the `business-brain-setup` skill first.
2. Read `get-found/scoreboard.md` for any existing baseline for this skill's KPIs.
3. Check which connectors are live (see the plugin's CONNECTORS.md) and use them before asking the owner for anything.

After finishing:

- Append what changed to `get-found/action-log.md` (date, skill, change, link, expected KPI effect).
- Record new KPI values in `get-found/scoreboard.md`.
- Put anything that publishes, sends, spends or changes a live account into `get-found/approvals.md` and wait for a yes.

## Triggers

- The owner asks for help with hyperlocal neighborhood marketing, or the Visibility Audit flagged it as a gap.
- Routed by the command center's next-best-move ranking.

## Phase 1: Discovery & Assessment

Goal: define the current state and record a baseline.

- Map neighborhoods and groups.
- Record the baseline for every KPI below in the scoreboard (metric, current value, source, date).
- Summarize the top gaps between current and desired state, ranked by impact on revenue.

Output: audit report + baseline scorecard + gap list.

## Phase 2: Architecture & Design

Goal: blueprint the fix before building anything.

- Design helpful posts and offers.
- Map dependencies (tools, accounts, people, content) and what must happen first.
- Run a quick failure-mode check: list 3-5 things that could go wrong, their impact, and the mitigation built into the plan.
- Get the owner's sign-off on the plan, targets and anything that spends money or publishes publicly.

Output: plan with owners and dates + risk table + sign-off.

## Phase 3: Implementation & Deployment

Goal: build and launch in stages without breaking what works.

- Engage.
- Build in small sprints; QA each piece against the plan (accuracy, links, tracking, compliance, brand voice from the Business Brain).
- Launch in stages with a rollback path; log every change in the action log.

Output: live assets (or, in the Visibility Audit edition, a build brief) + launch log.

## Phase 4: Optimization & Governance

Goal: prove the result and keep it from degrading.

- Track.
- Re-check on a **weekly** cadence through the Get-Found heartbeat.
- Compare every KPI to the Phase 1 baseline; report the change in plain language with the dollar impact where possible.
- Write a short SOP so the business (or its team) can repeat the work, and set the next review date.

Output: results report vs. baseline + SOP + review schedule.

## Measurable result

**Neighborhood leads; recommendations received.** Targets are goals measured against the Phase 1 baseline, not guarantees; state any assumption behind a target.

## Channel guidance

- Give before you ask; be helpful in the group before promoting.

## Approval gates and guardrails

- Never fabricate data, reviews, testimonials, citations or results. Label estimates as estimates.
- Get explicit owner approval before publishing, sending messages, changing live accounts or spending money.
- Follow platform rules and applicable law (FTC endorsements, CAN-SPAM, TCPA, privacy, and industry rules such as RESPA, fair housing or HIPAA).

## Related skills

- `community-builder` (Community Builder, #74)
- `co-marketing-partnership-builder` (Co-Marketing Partnership Builder, #75)
- `ugc-creator-program` (UGC & Creator Program, #88)
