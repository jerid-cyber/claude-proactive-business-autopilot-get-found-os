---
name: get-found-heartbeat
description: "Puts the Get-Found agent on a schedule (Get-Found Full OS). This skill should be used when the owner says 'put Get-Found on autopilot', 'schedule my Get-Found runs', 'run this every week', 'set up the heartbeat', 'pause Get-Found', 'change my Get-Found schedule', 'turn off Get-Found', or after the first Visibility Audit is complete."
metadata:
  edition: "Get-Found Full OS"
  version: "1.1.0"
---

# Get-Found Heartbeat

Turn Phase 4 (Optimization & Governance) into scheduled tasks so the agent keeps working without being asked. The
heartbeat only wakes the agent; the command center decides what to do, under the authority policy in
`get-found/autopilot.md`.

## Setup steps

1. **Check the prerequisites.** Confirm the Business Brain and a first Visibility Score exist; if not, run
   `business-brain-setup` and `get-found-visibility-audit` first.
2. **Confirm durable memory.** Every scheduled run starts in a fresh session, so the `get-found/` workspace must live in
   Google Drive, a connected folder, or a Claude project the scheduled runs can reach. If it currently lives only in
   session space, move it first. Write the exact location as `workspace:` in `get-found/autopilot.md` and read it back.
   Do not schedule anything until this is true.
3. **Confirm the autopilot file.** Create `get-found/autopilot.md` from the command center's
   `references/autopilot-template.md` if missing. Leave `mode: shadow` and no T2 permissions. Ask the owner for time
   zone, quiet hours, report channel and daily send cap; fill them in.
4. **Mark skills that do not apply.** Ask once, or infer from the Business Brain, which skills do not fit this business
   (for example `nonprofit-google-ad-grants` for a for-profit, `ecommerce-product-seo-free-listings` without a store).
   List them under `not_applicable:` in `autopilot.md` so runs skip them.
5. **Pick cadences and times.** Recommend all four cadences below; ask which to turn on and which local day and time
   suit the owner.
6. **Create the scheduled tasks.** Use the scheduled-task tools (never local cron, which stops when the session ends).
   Create one task per cadence with the prompts below, replacing `<WORKSPACE>` with the exact location and
   `<TZ>` with the owner's time zone. Each prompt must be standalone because every run starts fresh.
7. **Report.** Tell the owner what was scheduled, which approval setting each task got, and that a run needing
   approval for a tool will stop if nobody is there to approve it. Explain that the first 3 to 5 runs are shadow runs:
   everything that goes outside the business waits in `get-found/approvals.md`.
8. **Offer a first run now** so the owner sees a real report before the schedule takes over. Fix any gaps it exposes.

## Cadences and task prompts

**Daily (weekdays, early morning)** — skills: `reviews-everywhere-engine`, `speed-to-lead-system`, `customer-service-reply-assistant`, `ai-receptionist-chat-capture`, `google-ads-search-launcher`, `meta-ads-launch-scale`, `retargeting-architecture`, `reputation-crisis-response`
> Use the get-found-command-center skill to run the Get-Found daily check. Workspace: <WORKSPACE>. Time zone: <TZ>. Load business-brain.md and autopilot.md from the workspace; stop if status is PAUSE. Process approvals first. Check only what is new since last_run: new reviews and reply drafts, lead response times, paid spend anomalies, and event trigger conditions. Apply the authority policy and action keys to every action. Record results in the workspace, read them back, and report in under 10 lines.

**Weekly (Monday morning)** — skills: `gbp-google-maps-optimizer`, `answer-first-content-engine`, `reddit-quora-forum-presence`, `customer-database-reactivation`, `social-presence-builder`, `short-form-video-script-engine`, `proposal-quote-follow-up`, `email-sms-nurture-architect`, `linkedin-company-leader-authority`, `owner-kpi-dashboard`, `content-repurposing-editorial-ops`, `google-lsa-yelp-ads`, `owned-newsletter-builder`, `hyperlocal-neighborhood-marketing`
> Use the get-found-command-center skill to run the Get-Found weekly cycle. Workspace: <WORKSPACE>. Time zone: <TZ>. Load business-brain.md, autopilot.md and scoreboard.md; stop if status is PAUSE. Process approvals first, then pick the top 1-3 next best moves, complete them up to the approval gates under the authority policy, verify results with evidence, record and read back, and report Visibility Score movement, work done, approvals waiting, blockers and next move.

**Monthly batches (weekly, Thursday)** — the monthly-cadence skills are split into four batches so each run stays
within its limits. One batch runs each Thursday, rotating A → B → C → D using `next_monthly_batch` in
`autopilot.md`, so every monthly skill still gets its check each month.

- **Batch A, search & AI visibility:** `ai-search-visibility`, `google-ai-overviews-ai-mode`, `ai-brand-accuracy-correction`, `organic-ai-search-analytics`, `zero-click-serp-capture`, `social-search-optimization`, `youtube-video-seo`, `image-visual-voice-search`, `branded-search-brand-serp`, `ai-crawler-access-agent-readiness`, `agentic-commerce-business-agent`, `marketplace-app-store-seo`, `multilingual-international-seo`, `ecommerce-product-seo-free-listings`, `retail-media-network-launcher`, `nonprofit-google-ad-grants`
- **Batch B, listings, site & tracking:** `local-seo-citation-cleanup`, `apple-maps-bing-directories`, `website-verification-readiness`, `on-page-seo-optimizer`, `technical-seo-indexing`, `website-speed-core-web-vitals`, `tracking-attribution-setup`, `service-area-location-pages`, `multi-location-seo-governance`, `first-party-data-identity`, `industry-b2b-review-platforms`, `conversion-leak-finder`, `landing-page-blueprint`, `organic-traffic-to-lead-converter`, `pricing-page-transparency`, `offer-message-clarifier`
- **Batch C, content & authority:** `comparison-best-of-content`, `content-refresh-decay-recovery`, `help-center-faq-knowledge-base`, `helpful-content-quality-audit`, `topical-authority-pillar-hub`, `case-study-testimonial-engine`, `real-photo-asset-library`, `customer-story-video`, `local-link-authority-building`, `digital-pr-newswire-original-data`, `awards-best-of-lists`, `founder-led-brand-channel`, `podcast-guest-placement`, `brand-voice-style-system`, `lead-magnet-factory`, `ugc-creator-program`, `influencer-growth-accelerator`
- **Batch D, customers, money & growth:** `lean-marketing-plan`, `cash-flow-marketing-budget-forecast`, `pricing-margin-optimizer`, `marketing-sop-stack-governance`, `customer-journey-mapper`, `referral-program-builder`, `customer-feedback-nps-loop`, `customer-onboarding-retention`, `loyalty-upsell-repeat-purchase`, `sales-script-objection-handler`, `seasonal-campaign-planner`, `community-builder`, `co-marketing-partnership-builder`, `webinar-workshop-funnel`, `launch-pre-launch-sales`, `new-market-expansion`, `rebrand-rollout`

> Use the get-found-command-center skill to run the Get-Found monthly batch. Workspace: <WORKSPACE>. Time zone: <TZ>. Load business-brain.md and autopilot.md; stop if status is PAUSE. Read next_monthly_batch, run the Phase 4 check of each skill in that batch from the get-found-heartbeat skill (skipping anything under not_applicable), queue fixes as moves or approvals under the authority policy, then advance next_monthly_batch. Record and read back, and report in under 10 lines.

**Monthly report (first business day)**
> Use the get-found-command-center skill to run the Get-Found monthly report. Workspace: <WORKSPACE>. Time zone: <TZ>. Load business-brain.md, autopilot.md and scoreboard.md; stop if status is PAUSE. Re-test AI answers and listing accuracy, update the scoreboard, and send the owner a one-page monthly report against baseline, including approval rate by action type and any graduation proposals.

**Quarterly (first week of the quarter)** — skills: `get-found-visibility-audit`, `keyword-prompt-intent-research`, `schema-entity-knowledge-panel`, `eeat-author-authority`, `competitor-visibility-gap-report`, `ai-policy-data-safety`, `marketing-compliance-guardrails`, `seo-safe-website-migration`, `ltv-cac-channel-mix`, `employer-brand-recruiting`, `website-accessibility-wcag`, `platform-risk-fmea-resilience`
> Use the get-found-command-center skill to run the Get-Found quarterly re-score. Workspace: <WORKSPACE>. Time zone: <TZ>. Load business-brain.md and autopilot.md; stop if status is PAUSE. Run get-found-visibility-audit in full, re-benchmark competitors, compare to the previous quarter, review the authority policy and Lessons, and rewrite the 90-day plan.

## Maintain

- **Pause:** set `status: PAUSE` in `autopilot.md`. Runs keep waking but stop at Load. Disable the scheduled tasks only
  for a long pause.
- **Resume:** set `status: active`.
- **Change cadence or time:** update the scheduled task itself (not only the file) and note it in the action log.
- **Review:** hand off to the command center's Maintain → Review.
- **Retire:** set `status: complete`, write a final summary to the workspace, and disable or delete the scheduled
  tasks.

## Rules

- Scheduled runs never skip approval gates; anything in T3 waits in the approvals queue, and shadow mode treats T2 as T3.
- Runs obey the per-run limits in `autopilot.md` and stop cleanly when they hit one.
- If a run cannot reach a connector or the workspace, it reports which one and continues with what it can do; if it
  cannot reach the workspace at all, it makes no changes and reports that first.
- Keep scheduled reports short; link to the files instead of repeating them.
