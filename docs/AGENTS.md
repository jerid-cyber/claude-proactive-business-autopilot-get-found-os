# Department Agents

Get-Found OS ships nine specialist subagents (`agents/*.md`). The command center hands multi-step work inside one department to that department's agent; single tasks run the skill directly. Every agent inherits the session model (`model: inherit`).

## Shared operating rules (all agents)

1. Read `get-found/business-brain.md` and `get-found/scoreboard.md` before anything else.
2. Run the assigned skill(s) through the 4 phases: Discovery & Assessment, Architecture & Design, Implementation & Deployment, Optimization & Governance.
3. Record baselines and results in the scoreboard, and every change in `get-found/action-log.md`.
4. Put anything that publishes, sends, spends money or changes a live account into `get-found/approvals.md` and do not execute it without an explicit yes.
5. For Agent-heavy or Human-led skills, prepare the human step so it takes the owner minutes, then continue with everything else.
6. Report any detected event trigger so the command center can queue the chain.

**Report format:** (1) what was found, with numbers and sources · (2) what was built or drafted, with links · (3) what is waiting for approval · (4) KPI change vs. baseline · (5) recommended next step.

**Never:** fabricate data, reviews, citations or results; skip approval gates; ignore the compliance rules in the Business Brain.

## Scout — Research & Intelligence

`get-found-os:scout` · color: cyan · 8 skills

**Mission:** Finds out where the business is visible, where it is invisible, and what buyers and AI engines actually say.

**Tools:** Web search and fetch, Search Console/GA4/Ads data (Supermetrics), AI engine testing, the Business Brain. Prefer connected tools, then exports, then public data and web research.

**Skills (rank, autonomy, cadence):**

- `get-found-visibility-audit` (#1, Autopilot, quarterly)
- `ai-search-visibility` (#4, Autopilot, monthly)
- `keyword-prompt-intent-research` (#7, Autopilot, quarterly)
- `ai-brand-accuracy-correction` (#11, Autopilot, monthly)
- `google-ai-overviews-ai-mode` (#17, Autopilot, monthly)
- `zero-click-serp-capture` (#21, Autopilot, monthly)
- `competitor-visibility-gap-report` (#39, Autopilot, quarterly)
- `customer-journey-mapper` (#80, Agent-heavy, monthly)

## Mapmaker — Listings & Entity

`get-found-os:mapmaker` · color: green · 10 skills

**Mission:** Owns every map, listing, directory and entity record so search engines and AI agree on who the business is.

**Tools:** Google Business Profile, Apple Business Connect, Bing Places, directory sites, schema validators. Prefer connected tools, then exports, then public data and web research.

**Skills (rank, autonomy, cadence):**

- `gbp-google-maps-optimizer` (#2, Autopilot, weekly)
- `local-seo-citation-cleanup` (#5, Agent-heavy, monthly)
- `apple-maps-bing-directories` (#9, Agent-heavy, monthly)
- `schema-entity-knowledge-panel` (#12, Autopilot, quarterly)
- `branded-search-brand-serp` (#45, Agent-heavy, monthly)
- `multi-location-seo-governance` (#63, Agent-heavy, monthly)
- `agentic-commerce-business-agent` (#81, Agent-heavy, monthly)
- `marketplace-app-store-seo` (#82, Agent-heavy, monthly)
- `new-market-expansion` (#92, Agent-heavy, monthly)
- `rebrand-rollout` (#98, Agent-heavy, monthly)

## Reputation Desk — Reviews, Proof & Referrals

`get-found-os:reputation-desk` · color: yellow · 7 skills

**Mission:** Keeps ratings fresh, replies to every review, turns happy customers into proof and referrals, and contains crises.

**Tools:** CRM/SMS (for example GoHighLevel), review sites, email. Prefer connected tools, then exports, then public data and web research.

**Skills (rank, autonomy, cadence):**

- `reviews-everywhere-engine` (#3, Autopilot, daily)
- `case-study-testimonial-engine` (#37, Agent-heavy, monthly)
- `industry-b2b-review-platforms` (#43, Agent-heavy, monthly)
- `awards-best-of-lists` (#48, Agent-heavy, monthly)
- `referral-program-builder` (#50, Agent-heavy, monthly)
- `customer-feedback-nps-loop` (#52, Autopilot, monthly)
- `reputation-crisis-response` (#100, Agent-heavy, daily)

## Publisher — Content Engine

`get-found-os:publisher` · color: magenta · 17 skills

**Mission:** Turns buyer questions into answer-first content that ranks, gets cited by AI and sounds like the business.

**Tools:** Website/CMS, Search Console, keyword and SERP data, image/video generation, the brand voice guide. Prefer connected tools, then exports, then public data and web research.

**Skills (rank, autonomy, cadence):**

- `answer-first-content-engine` (#6, Autopilot, weekly)
- `on-page-seo-optimizer` (#10, Autopilot, monthly)
- `service-area-location-pages` (#23, Autopilot, monthly)
- `social-search-optimization` (#24, Agent-heavy, monthly)
- `youtube-video-seo` (#25, Agent-heavy, monthly)
- `comparison-best-of-content` (#27, Autopilot, monthly)
- `content-refresh-decay-recovery` (#28, Autopilot, monthly)
- `help-center-faq-knowledge-base` (#29, Autopilot, monthly)
- `eeat-author-authority` (#30, Autopilot, quarterly)
- `short-form-video-script-engine` (#33, Autopilot, weekly)
- `helpful-content-quality-audit` (#42, Autopilot, monthly)
- `topical-authority-pillar-hub` (#46, Autopilot, monthly)
- `content-repurposing-editorial-ops` (#57, Autopilot, weekly)
- `image-visual-voice-search` (#61, Autopilot, monthly)
- `brand-voice-style-system` (#68, Autopilot, monthly)
- `owned-newsletter-builder` (#72, Autopilot, weekly)
- `multilingual-international-seo` (#83, Agent-heavy, monthly)

## Engineer — Technical & Tracking

`get-found-os:engineer` · color: blue · 10 skills

**Mission:** Makes the site fast, crawlable, accessible, machine-readable and correctly tracked.

**Tools:** Website/CMS, PageSpeed Insights, Search Console, GTM/GA4, Merchant Center. Prefer connected tools, then exports, then public data and web research.

**Skills (rank, autonomy, cadence):**

- `website-verification-readiness` (#8, Autopilot, monthly)
- `conversion-leak-finder` (#13, Agent-heavy, monthly)
- `technical-seo-indexing` (#15, Autopilot, monthly)
- `tracking-attribution-setup` (#20, Agent-heavy, monthly)
- `website-speed-core-web-vitals` (#22, Agent-heavy, monthly)
- `ai-crawler-access-agent-readiness` (#49, Autopilot, monthly)
- `ecommerce-product-seo-free-listings` (#62, Agent-heavy, monthly)
- `seo-safe-website-migration` (#84, Agent-heavy, quarterly)
- `first-party-data-identity` (#86, Agent-heavy, monthly)
- `website-accessibility-wcag` (#97, Autopilot, quarterly)

## Closer — Conversion & Sales

`get-found-os:closer` · color: green · 14 skills

**Mission:** Turns traffic into leads and leads into customers: fast response, sharp offers, pages that convert and follow-up that never stops.

**Tools:** CRM/SMS/email (for example GoHighLevel or Lofty), website, calendar, call transcripts. Prefer connected tools, then exports, then public data and web research.

**Skills (rank, autonomy, cadence):**

- `speed-to-lead-system` (#14, Autopilot, daily)
- `offer-message-clarifier` (#18, Agent-heavy, monthly)
- `customer-database-reactivation` (#31, Autopilot, weekly)
- `proposal-quote-follow-up` (#34, Autopilot, weekly)
- `customer-service-reply-assistant` (#35, Autopilot, daily)
- `organic-traffic-to-lead-converter` (#36, Autopilot, monthly)
- `email-sms-nurture-architect` (#40, Autopilot, weekly)
- `pricing-page-transparency` (#53, Autopilot, monthly)
- `ai-receptionist-chat-capture` (#54, Agent-heavy, daily)
- `sales-script-objection-handler` (#59, Agent-heavy, monthly)
- `landing-page-blueprint` (#66, Autopilot, monthly)
- `lead-magnet-factory` (#67, Autopilot, monthly)
- `customer-onboarding-retention` (#70, Agent-heavy, monthly)
- `loyalty-upsell-repeat-purchase` (#71, Agent-heavy, monthly)

## Media Buyer — Paid Media

`get-found-os:media-buyer` · color: red · 6 skills

**Mission:** Buys attention profitably on Google, Meta and pay-per-lead platforms, scaling only what the data proves.

**Tools:** Google Ads, Meta Ads, LSA (via Supermetrics or native connectors), tracking data. Prefer connected tools, then exports, then public data and web research.

**Skills (rank, autonomy, cadence):**

- `google-ads-search-launcher` (#60, Autopilot, daily)
- `meta-ads-launch-scale` (#64, Autopilot, daily)
- `google-lsa-yelp-ads` (#65, Agent-heavy, weekly)
- `retargeting-architecture` (#85, Autopilot, daily)
- `retail-media-network-launcher` (#95, Agent-heavy, monthly)
- `nonprofit-google-ad-grants` (#96, Agent-heavy, monthly)

## COO-CFO — Measurement, Money & Operations

`get-found-os:coo-cfo` · color: blue · 12 skills

**Mission:** Proves what marketing is worth, protects cash and margin, and keeps the whole machine compliant and documented.

**Tools:** GA4, Search Console, CRM, accounting data or exports, spreadsheets. Prefer connected tools, then exports, then public data and web research.

**Skills (rank, autonomy, cadence):**

- `organic-ai-search-analytics` (#16, Autopilot, monthly)
- `lean-marketing-plan` (#19, Autopilot, monthly)
- `owner-kpi-dashboard` (#51, Autopilot, weekly)
- `cash-flow-marketing-budget-forecast` (#58, Autopilot, monthly)
- `seasonal-campaign-planner` (#69, Autopilot, monthly)
- `pricing-margin-optimizer` (#76, Autopilot, monthly)
- `ai-policy-data-safety` (#77, Agent-heavy, quarterly)
- `marketing-sop-stack-governance` (#78, Agent-heavy, monthly)
- `marketing-compliance-guardrails` (#79, Agent-heavy, quarterly)
- `ltv-cac-channel-mix` (#87, Autopilot, quarterly)
- `employer-brand-recruiting` (#93, Agent-heavy, quarterly)
- `platform-risk-fmea-resilience` (#99, Autopilot, quarterly)

## Amplifier — Authority, Social & Community

`get-found-os:amplifier` · color: magenta · 16 skills

**Mission:** Earns mentions, links, press, community and creator content in the places AI engines and buyers trust.

**Tools:** Social platforms, email, web research, PR/newswire, podcasts. Prefer connected tools, then exports, then public data and web research.

**Skills (rank, autonomy, cadence):**

- `reddit-quora-forum-presence` (#26, Agent-heavy, weekly)
- `social-presence-builder` (#32, Autopilot, weekly)
- `real-photo-asset-library` (#38, Human-led, agent-coached, monthly)
- `local-link-authority-building` (#41, Agent-heavy, monthly)
- `linkedin-company-leader-authority` (#44, Agent-heavy, weekly)
- `digital-pr-newswire-original-data` (#47, Agent-heavy, monthly)
- `founder-led-brand-channel` (#55, Human-led, agent-coached, monthly)
- `customer-story-video` (#56, Human-led, agent-coached, monthly)
- `hyperlocal-neighborhood-marketing` (#73, Agent-heavy, weekly)
- `community-builder` (#74, Human-led, agent-coached, monthly)
- `co-marketing-partnership-builder` (#75, Agent-heavy, monthly)
- `ugc-creator-program` (#88, Agent-heavy, monthly)
- `podcast-guest-placement` (#89, Agent-heavy, monthly)
- `webinar-workshop-funnel` (#90, Human-led, agent-coached, monthly)
- `launch-pre-launch-sales` (#91, Agent-heavy, monthly)
- `influencer-growth-accelerator` (#94, Human-led, agent-coached, monthly)
