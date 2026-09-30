---
name: ai-receptionist-chat-capture
description: "Capture leads 24/7, including after hours. Runs the Get-Found 4-phase method (Discovery, Design, Build, Optimize) as an agent and proves results against a baseline: Missed-call rate near 0; after-hours bookings. This skill should be used when a business owner asks for help with ai receptionist & chat capture, when the Get-Found command center routes a next best move here, or when a scheduled Get-Found heartbeat reaches this skill."
metadata:
  rank: 54
  channel: "Conversion"
  department: "Closer"
  autonomy: "Agent-heavy"
  cadence: "Daily"
  edition: "Get-Found Full OS"
---

# AI Receptionist & Chat Capture

**Get-Found #54 of 100** · Department: Closer (Conversion & Sales) · Channel: Conversion · Autonomy: Agent-heavy · Monitor: Daily

Part of the Get-Found agent, built on Jerid Wempen's 4-Phase System. Mission: help businesses of every industry get found, get chosen and grow.

## Purpose

Capture leads 24/7, including after hours.

## Agent operating mode

**Agent-heavy.** Do everything except the human step. Human step: A voice/chat receptionist has to be set up and test-called on the phone or chat platform (for example GoHighLevel) by a person. Prepare that step so it takes the owner minutes (exact text, links, checklist), add it to the approvals queue, and continue with the rest of the work.

Before starting:

1. Read the Business Brain (`get-found/business-brain.md` in the connected folder or project). If it is missing, run the `business-brain-setup` skill first.
2. Read `get-found/scoreboard.md` for any existing baseline for this skill's KPIs.
3. Check which connectors are live (see the plugin's CONNECTORS.md) and use them before asking the owner for anything.

After finishing:

- Append what changed to `get-found/action-log.md` (date, skill, change, link, expected KPI effect).
- Record new KPI values in `get-found/scoreboard.md`.
- Put anything that publishes, sends, spends or changes a live account into `get-found/approvals.md` and wait for a yes.

## Triggers

- The owner asks for help with ai receptionist & chat capture, or the Visibility Audit flagged it as a gap.
- A lead waits longer than 5 minutes for a first response

## Phase 1: Discovery & Assessment

Goal: define the current state and record a baseline.

- Audit missed calls and chats.
- Record the baseline for every KPI below in the scoreboard (metric, current value, source, date).
- Summarize the top gaps between current and desired state, ranked by impact on revenue.

Output: audit report + baseline scorecard + gap list.

## Phase 2: Architecture & Design

Goal: blueprint the fix before building anything.

- Design scripts and handoff rules.
- Map dependencies (tools, accounts, people, content) and what must happen first.
- Run a quick failure-mode check: list 3-5 things that could go wrong, their impact, and the mitigation built into the plan.
- Get the owner's sign-off on the plan, targets and anything that spends money or publishes publicly.

Output: plan with owners and dates + risk table + sign-off.

## Phase 3: Implementation & Deployment

Goal: build and launch in stages without breaking what works.

- Deploy.
- Build in small sprints; QA each piece against the plan (accuracy, links, tracking, compliance, brand voice from the Business Brain).
- Launch in stages with a rollback path; log every change in the action log.

Output: live assets (or, in the Visibility Audit edition, a build brief) + launch log.

## Phase 4: Optimization & Governance

Goal: prove the result and keep it from degrading.

- Review transcripts.
- Re-check on a **daily** cadence through the Get-Found heartbeat.
- Compare every KPI to the Phase 1 baseline; report the change in plain language with the dollar impact where possible.
- Write a short SOP so the business (or its team) can repeat the work, and set the next review date.

Output: results report vs. baseline + SOP + review schedule.

## Measurable result

**Missed-call rate near 0; after-hours bookings.** Targets are goals measured against the Phase 1 baseline, not guarantees; state any assumption behind a target.

## Channel guidance

- Fix the biggest leak first; one change at a time so results can be attributed.
- Every page needs one clear next step and proof near it.
- Test for statistical confidence before declaring winners.

## Approval gates and guardrails

- Never fabricate data, reviews, testimonials, citations or results. Label estimates as estimates.
- Get explicit owner approval before publishing, sending messages, changing live accounts or spending money.
- Follow platform rules and applicable law (FTC endorsements, CAN-SPAM, TCPA, privacy, and industry rules such as RESPA, fair housing or HIPAA).

## Related skills

- `pricing-page-transparency` (Pricing Page & Offer Transparency, #53)
- `landing-page-blueprint` (Landing Page Blueprint, #66)
- `lead-magnet-factory` (Lead Magnet Factory, #67)
