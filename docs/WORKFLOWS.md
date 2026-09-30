# Workflows: Run Loop, Event Triggers, Heartbeat & Approvals

Everything below is taken verbatim from `get-found-command-center` and `get-found-heartbeat`.

## Start of every run & the operating loop

1. Load `get-found/business-brain.md`. If it does not exist, run `business-brain-setup` and stop after it finishes.
2. Load `get-found/scoreboard.md`, `get-found/action-log.md` and `get-found/approvals.md` (create empty ones if missing).
3. Check which connectors are live. Prefer connected data, then exports, then public data and web research. Never ask the owner for something a connector or the website already shows.
4. Surface anything waiting in the approvals queue before starting new work.

## The operating loop

1. **Discover:** if there is no Visibility Score yet, run `get-found-visibility-audit` first.
2. **Design:** rank the open gaps with the next-best-move formula; pick the top 1-3 for this cycle.
3. **Deploy:** hand each move to its department agent (or run the skill directly), respecting approval gates.
4. **Govern:** log results, update the scoreboard, and let the heartbeat and event triggers choose the next cycle.

## Event triggers (13 automatic chains)

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

## Heartbeat — scheduled cadences

The heartbeat creates one Claude scheduled task per cadence. Each prompt is standalone because every scheduled run starts fresh.
Counts: **8 daily · 14 weekly · 66 monthly · 12 quarterly** skill checks.

**Daily (weekdays, early morning)** — skills: `reviews-everywhere-engine`, `speed-to-lead-system`, `customer-service-reply-assistant`, `ai-receptionist-chat-capture`, `google-ads-search-launcher`, `meta-ads-launch-scale`, `retargeting-architecture`, `reputation-crisis-response`
> Run the Get-Found daily check. Load get-found/business-brain.md. Using the get-found-command-center skill, check: new reviews and reply drafts, lead response times, paid spend anomalies, and any event trigger conditions. Queue anything public in get-found/approvals.md. Report in under 10 lines.

**Weekly (Monday morning)** — skills: `gbp-google-maps-optimizer`, `answer-first-content-engine`, `reddit-quora-forum-presence`, `customer-database-reactivation`, `social-presence-builder`, `short-form-video-script-engine`, `proposal-quote-follow-up`, `email-sms-nurture-architect`, `linkedin-company-leader-authority`, `owner-kpi-dashboard`, `content-repurposing-editorial-ops`, `google-lsa-yelp-ads`, `owned-newsletter-builder`, `hyperlocal-neighborhood-marketing`
> Run the Get-Found weekly cycle with the get-found-command-center skill: load the Business Brain and scoreboard, pick the top 1-3 next best moves, complete them up to the approval gates, and report Visibility Score movement, work done, approvals waiting and next move.

**Monthly (first business day)** — skills: `ai-search-visibility`, `local-seo-citation-cleanup`, `website-verification-readiness`, `apple-maps-bing-directories`, `on-page-seo-optimizer`, `ai-brand-accuracy-correction`, `conversion-leak-finder`, `technical-seo-indexing`, `organic-ai-search-analytics`, `google-ai-overviews-ai-mode`, `offer-message-clarifier`, `lean-marketing-plan`, `tracking-attribution-setup`, `zero-click-serp-capture`, `website-speed-core-web-vitals`, `service-area-location-pages`, `social-search-optimization`, `youtube-video-seo`, `comparison-best-of-content`, `content-refresh-decay-recovery`, `help-center-faq-knowledge-base`, `organic-traffic-to-lead-converter`, `case-study-testimonial-engine`, `real-photo-asset-library`, `local-link-authority-building`, `helpful-content-quality-audit`, `industry-b2b-review-platforms`, `branded-search-brand-serp`, `topical-authority-pillar-hub`, `digital-pr-newswire-original-data`, `awards-best-of-lists`, `ai-crawler-access-agent-readiness`, `referral-program-builder`, `customer-feedback-nps-loop`, `pricing-page-transparency`, `founder-led-brand-channel`, `customer-story-video`, `cash-flow-marketing-budget-forecast`, `sales-script-objection-handler`, `image-visual-voice-search`, `ecommerce-product-seo-free-listings`, `multi-location-seo-governance`, `landing-page-blueprint`, `lead-magnet-factory`, `brand-voice-style-system`, `seasonal-campaign-planner`, `customer-onboarding-retention`, `loyalty-upsell-repeat-purchase`, `community-builder`, `co-marketing-partnership-builder`, `pricing-margin-optimizer`, `marketing-sop-stack-governance`, `customer-journey-mapper`, `agentic-commerce-business-agent`, `marketplace-app-store-seo`, `multilingual-international-seo`, `first-party-data-identity`, `ugc-creator-program`, `podcast-guest-placement`, `webinar-workshop-funnel`, `launch-pre-launch-sales`, `new-market-expansion`, `influencer-growth-accelerator`, `retail-media-network-launcher`, `nonprofit-google-ad-grants`, `rebrand-rollout`
> Run the Get-Found monthly review with the get-found-command-center skill: re-test AI answers and listings accuracy, run each monthly-cadence skill's Phase 4 check, update the scoreboard and send the owner a one-page monthly report against baseline.

**Quarterly (first week of the quarter)** — skills: `get-found-visibility-audit`, `keyword-prompt-intent-research`, `schema-entity-knowledge-panel`, `eeat-author-authority`, `competitor-visibility-gap-report`, `ai-policy-data-safety`, `marketing-compliance-guardrails`, `seo-safe-website-migration`, `ltv-cac-channel-mix`, `employer-brand-recruiting`, `website-accessibility-wcag`, `platform-risk-fmea-resilience`
> Run the Get-Found quarterly re-score: run get-found-visibility-audit in full, re-benchmark competitors, compare to the previous quarter, and rewrite the 90-day plan.

### Heartbeat rules

- Scheduled runs never skip approval gates; anything that publishes, sends, spends or changes a live account waits in the approvals queue.
- If a run cannot reach a connector, it reports which one and continues with what it can do.
- Keep scheduled reports short; link to the files instead of repeating them.

## Approval gates (never skipped)

- Publishing anything public, sending any message to customers or prospects, changing a live account, or spending money requires an explicit yes from the approver named in the Business Brain.
- Batch approvals: collect items in `get-found/approvals.md` with a one-line summary, preview and expected KPI effect so the owner can approve many in one pass.
- Research, drafting, internal reports and scoreboard updates run without approval.

## End-of-run report

End every run with a short report:

1. Visibility Score now vs. baseline (points and plain language).
2. What was done this cycle, with links.
3. What is waiting for approval.
4. The next best move and why.
