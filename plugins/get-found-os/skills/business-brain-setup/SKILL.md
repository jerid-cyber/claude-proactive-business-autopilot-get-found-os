---
name: business-brain-setup
description: "Creates or updates the Get-Found Business Brain, the shared record every Get-Found skill reads. This skill should be used when the owner says 'set up Get-Found', 'onboard my business', 'update my business info', 'we changed our hours/prices/services', or when any Get-Found skill finds that get-found/business-brain.md is missing or out of date."
metadata:
  edition: "Get-Found Full OS"
---

# Business Brain Setup

Build the Business Brain with as few owner questions as possible.

## Steps

1. **Research first.** Ask only for the business name and website (or GBP link). Then gather everything public: website pages, Google Business Profile, review sites, social profiles, directory listings, and what AI engines say. Fill as much of `references/business-brain-template.md` as the evidence supports, marking each field with its source.
2. **Ask for the gaps in one round.** Present the pre-filled brain and ask only for what could not be found: offers and pricing, best customers, competitors, peak season, compliance rules, approver and spending limit. Keep it to one short round of questions.
3. **Flag conflicts.** List every fact that differs between sources (for example two phone numbers or different hours). These become the first fixes for the listings and AI-accuracy skills.
4. **Connect tools.** Show which connectors are live and which would unlock more work (see CONNECTORS.md). Suggest connecting the top 2-3 that matter most for this business.
5. **Save.** Write `get-found/business-brain.md`, plus empty `get-found/scoreboard.md`, `get-found/action-log.md` and `get-found/approvals.md` if they do not exist. Save in the connected folder, or in the Claude project when no folder is connected.
6. **Hand off.** Offer to run `get-found-visibility-audit` next to set the baseline, then `get-found-heartbeat` to put the agent on a schedule.

## Rules

- The owner confirms the master business record (name, address, phone, hours) before any skill publishes it anywhere.
- Never store payment details, passwords or customer personal data in the brain; store which tool holds them instead.
- Re-run this skill whenever the owner reports a change; log the change in the action log.
