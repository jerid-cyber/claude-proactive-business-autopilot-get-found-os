---
name: get-found-heartbeat
description: "Puts the Get-Found agent on a schedule (Get-Found Full OS). This skill should be used when the owner says 'put Get-Found on autopilot', 'schedule my Get-Found runs', 'run this every week', 'set up the heartbeat', or after the first Visibility Audit is complete."
metadata:
  edition: "Get-Found Full OS"
---

# Get-Found Heartbeat

Turn Phase 4 (Optimization & Governance) into scheduled tasks so the agent keeps working without being asked.

## Steps

1. Confirm the Business Brain and a first Visibility Score exist; if not, run `business-brain-setup` and `get-found-visibility-audit` first.
2. Ask the owner which cadences to turn on (recommend all that apply to this edition) and what local time and day suit them.
3. Create one Cowork scheduled task per cadence, using the prompts below. Each prompt must be standalone because every run starts fresh.
4. Tell the owner what was scheduled and how each run reports (a short summary plus anything waiting in `get-found/approvals.md`).

## Cadences and task prompts

**Daily (weekdays, early morning)** — skills: `reviews-everywhere-engine`, `speed-to-lead-system`, `customer-service-reply-assistant`, `ai-receptionist-chat-capture`, `google-ads-search-launcher`, `meta-ads-launch-scale`, `retargeting-architecture`, `reputation-crisis-response`
> Run the Get-Found daily check. Load get-found/business-brain.md. Using the get-found-command-center skill, check: new reviews and reply drafts, lead response times, paid spend anomalies, and any event trigger conditions. Queue anything public in get-found/approvals.md. Report in under 10 lines.

**Weekly (Monday morning)** — skills: `gbp-google-maps-optimizer`, `answer-first-content-engine`, `reddit-quora-forum-presence`, `customer-database-reactivation`, `social-presence-builder`, `short-form-video-script-engine`, `proposal-quote-follow-up`, `email-sms-nurture-architect`, `linkedin-company-leader-authority`, `owner-kpi-dashboard`, `content-repurposing-editorial-ops`, `google-lsa-yelp-ads`, `owned-newsletter-builder`, `hyperlocal-neighborhood-marketing`
> Run the Get-Found weekly cycle with the get-found-command-center skill: load the Business Brain and scoreboard, pick the top 1-3 next best moves, complete them up to the approval gates, and report Visibility Score movement, work done, approvals waiting and next move.

**Monthly (first business day)** — skills: `ai-search-visibility`, `local-seo-citation-cleanup`, `website-verification-readiness`, `apple-maps-bing-directories`, `on-page-seo-optimizer`, `ai-brand-accuracy-correction`, `conversion-leak-finder`, `technical-seo-indexing`, `organic-ai-search-analytics`, `google-ai-overviews-ai-mode`, `offer-message-clarifier`, `lean-marketing-plan`, `tracking-attribution-setup`, `zero-click-serp-capture`, `website-speed-core-web-vitals`, `service-area-location-pages`, `social-search-optimization`, `youtube-video-seo`, `comparison-best-of-content`, `content-refresh-decay-recovery`, `help-center-faq-knowledge-base`, `organic-traffic-to-lead-converter`, `case-study-testimonial-engine`, `real-photo-asset-library`, `local-link-authority-building`, `helpful-content-quality-audit`, `industry-b2b-review-platforms`, `branded-search-brand-serp`, `topical-authority-pillar-hub`, `digital-pr-newswire-original-data`, `awards-best-of-lists`, `ai-crawler-access-agent-readiness`, `referral-program-builder`, `customer-feedback-nps-loop`, `pricing-page-transparency`, `founder-led-brand-channel`, `customer-story-video`, `cash-flow-marketing-budget-forecast`, `sales-script-objection-handler`, `image-visual-voice-search`, `ecommerce-product-seo-free-listings`, `multi-location-seo-governance`, `landing-page-blueprint`, `lead-magnet-factory`, `brand-voice-style-system`, `seasonal-campaign-planner`, `customer-onboarding-retention`, `loyalty-upsell-repeat-purchase`, `community-builder`, `co-marketing-partnership-builder`, `pricing-margin-optimizer`, `marketing-sop-stack-governance`, `customer-journey-mapper`, `agentic-commerce-business-agent`, `marketplace-app-store-seo`, `multilingual-international-seo`, `first-party-data-identity`, `ugc-creator-program`, `podcast-guest-placement`, `webinar-workshop-funnel`, `launch-pre-launch-sales`, `new-market-expansion`, `influencer-growth-accelerator`, `retail-media-network-launcher`, `nonprofit-google-ad-grants`, `rebrand-rollout`
> Run the Get-Found monthly review with the get-found-command-center skill: re-test AI answers and listings accuracy, run each monthly-cadence skill's Phase 4 check, update the scoreboard and send the owner a one-page monthly report against baseline.

**Quarterly (first week of the quarter)** — skills: `get-found-visibility-audit`, `keyword-prompt-intent-research`, `schema-entity-knowledge-panel`, `eeat-author-authority`, `competitor-visibility-gap-report`, `ai-policy-data-safety`, `marketing-compliance-guardrails`, `seo-safe-website-migration`, `ltv-cac-channel-mix`, `employer-brand-recruiting`, `website-accessibility-wcag`, `platform-risk-fmea-resilience`
> Run the Get-Found quarterly re-score: run get-found-visibility-audit in full, re-benchmark competitors, compare to the previous quarter, and rewrite the 90-day plan.

## Rules

- Scheduled runs never skip approval gates; anything that publishes, sends, spends or changes a live account waits in the approvals queue.
- If a run cannot reach a connector, it reports which one and continues with what it can do.
- Keep scheduled reports short; link to the files instead of repeating them.
