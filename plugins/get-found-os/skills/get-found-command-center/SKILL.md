---
name: get-found-command-center
description: "The Get-Found orchestrator (Get-Found Full OS). This skill should be used when the owner says 'run Get-Found', 'what should I work on', 'next best move', 'how visible is my business', 'run my weekly Get-Found cycle', 'get-found report', or when a scheduled Get-Found heartbeat fires. It reads the Business Brain, keeps the Visibility Score, picks the next best move and routes work to the right skill or department agent."
metadata:
  edition: "Get-Found Full OS"
  version: "1.0.0"
---

# Get-Found Command Center

The brain of the Get-Found agent. It never tries to do everything at once: it finds the biggest gap, fixes it, proves
it, and moves to the next one.

This is the **Get-Found Full OS** edition with 100 skills. It diagnoses, builds, publishes (after approval) and monitors, continuously, using the 4-phase loop below.

## Start of every run

1. Load `get-found/business-brain.md`. If it does not exist, run `business-brain-setup` and stop after it finishes.
2. Load `get-found/scoreboard.md`, `get-found/action-log.md` and `get-found/approvals.md` (create empty ones if missing).
3. Check which connectors are live. Prefer connected data, then exports, then public data and web research. Never ask the owner for something a connector or the website already shows.
4. Surface anything waiting in the approvals queue before starting new work.

## The operating loop

1. **Discover:** if there is no Visibility Score yet, run `get-found-visibility-audit` first.
2. **Design:** rank the open gaps with the next-best-move formula; pick the top 1-3 for this cycle.
3. **Deploy:** hand each move to its department agent (or run the skill directly), respecting approval gates.
4. **Govern:** log results, update the scoreboard, and let the heartbeat and event triggers choose the next cycle.

## Next-best-move formula

For each open gap, score:

`priority = (Visibility Score points at stake × revenue weight) ÷ effort`

- **Points at stake:** from `references/visibility-score.md`.
- **Revenue weight:** 3 if the gap sits between a buyer and a booked job/sale (conversion, speed to lead, maps, reviews), 2 if it drives qualified traffic, 1 if it builds long-term authority.
- **Effort:** 1 (under an hour of agent work, no human step), 2 (a day, or one small human step), 3 (multi-week or needs a developer/owner-heavy step).
- Ties go to the skill with the higher Get-Found rank (lower number).
- Never run more than 3 moves in a cycle. One change at a time per channel so results can be attributed.

## Routing

| Department | Focus | Skills in this edition |
| --- | --- | --- |
| Scout | Research & Intelligence | 1, 4, 7, 11, 17, 21, 39, 80 |
| Mapmaker | Listings & Entity | 2, 5, 9, 12, 45, 63, 81, 82, 92, 98 |
| Reputation Desk | Reviews, Proof & Referrals | 3, 37, 43, 48, 50, 52, 100 |
| Publisher | Content Engine | 6, 10, 23, 24, 25, 27, 28, 29, 30, 33, 42, 46, 57, 61, 68, 72, 83 |
| Engineer | Technical & Tracking | 8, 13, 15, 20, 22, 49, 62, 84, 86, 97 |
| Closer | Conversion & Sales | 14, 18, 31, 34, 35, 36, 40, 53, 54, 59, 66, 67, 70, 71 |
| Media Buyer | Paid Media | 60, 64, 65, 85, 95, 96 |
| COO-CFO | Measurement, Money & Operations | 16, 19, 51, 58, 69, 76, 77, 78, 79, 87, 93, 99 |
| Amplifier | Authority, Social & Community | 26, 32, 38, 41, 44, 47, 55, 56, 73, 74, 75, 88, 89, 90, 91, 94 |

Full routing table with autonomy and cadence: `references/skill-catalog.md`. For multi-step work inside one department,
hand off to that department's agent; for a single task, run the skill directly.

## Event triggers

When the heartbeat or any skill detects one of these conditions, queue the chain in order:

| Condition | Chain |
| --- | --- |
| A review of 1-2 stars, or 3+ negative reviews in 7 days | `reputation-crisis-response` → `reviews-everywhere-engine` → `ai-brand-accuracy-correction` |
| A page loses 20%+ clicks month over month in Search Console | `content-refresh-decay-recovery` → `helpful-content-quality-audit` → `google-ai-overviews-ai-mode` |
| The business adds a new service, product or location | `service-area-location-pages` → `schema-entity-knowledge-panel` → `gbp-google-maps-optimizer` → `answer-first-content-engine` → `pricing-page-transparency` |
| A lead waits longer than 5 minutes for a first response | `speed-to-lead-system` → `ai-receptionist-chat-capture` |
| An AI engine states a wrong fact about the business | `ai-brand-accuracy-correction` → `schema-entity-knowledge-panel` → `local-seo-citation-cleanup` |
| A competitor passes the business in map rank or AI answers | `competitor-visibility-gap-report` → `gbp-google-maps-optimizer` → `ai-search-visibility` |
| Cost per lead rises 25%+ over 14 days on any paid channel | `meta-ads-launch-scale` → `google-ads-search-launcher` → `conversion-leak-finder` → `retargeting-architecture` |
| Website conversion rate drops 20%+ week over week | `conversion-leak-finder` → `website-speed-core-web-vitals` → `tracking-attribution-setup` |
| Peak season is 6 weeks away (from the Business Brain calendar) | `seasonal-campaign-planner` → `customer-database-reactivation` → `owned-newsletter-builder` |
| Any single channel exceeds 40% of leads or revenue | `platform-risk-fmea-resilience` → `ltv-cac-channel-mix` |
| NAP data drifts on any priority listing | `local-seo-citation-cleanup` → `apple-maps-bing-directories` |
| A new customer becomes a promoter (NPS 9-10) or leaves a 5-star review | `referral-program-builder` → `case-study-testimonial-engine` → `customer-feedback-nps-loop` |
| The site is being redesigned, re-platformed or rebranded | `seo-safe-website-migration` → `rebrand-rollout` |

## Approval gates (never skipped)

- Publishing anything public, sending any message to customers or prospects, changing a live account, or spending money requires an explicit yes from the approver named in the Business Brain.
- Batch approvals: collect items in `get-found/approvals.md` with a one-line summary, preview and expected KPI effect so the owner can approve many in one pass.
- Research, drafting, internal reports and scoreboard updates run without approval.

## Reporting

End every run with a short report:

1. Visibility Score now vs. baseline (points and plain language).
2. What was done this cycle, with links.
3. What is waiting for approval.
4. The next best move and why.

## Guardrails

- Never fabricate data, reviews, testimonials or AI citations; label estimates.
- Follow platform rules and the compliance rules in the Business Brain (FTC, CAN-SPAM, TCPA, RESPA, fair housing, HIPAA as applicable).
- Targets are goals measured against a baseline, never guarantees.
