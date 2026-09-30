# Get-Found Full OS

All 100 Get-Found skills run by one orchestrator and nine specialist department agents.

Built on Jerid Wempen's 4-Phase System (Discovery & Assessment, Architecture & Design, Implementation & Deployment,
Optimization & Governance). Version 1.1.0.

## What's inside

- **100 Get-Found skills**
- **3 core skills:** `get-found-command-center` (orchestrator), `business-brain-setup` (onboarding), `get-found-heartbeat` (scheduling)
- **9 department agent(s):**
- **Scout** (Research & Intelligence): 8 skills
- **Mapmaker** (Listings & Entity): 10 skills
- **Reputation Desk** (Reviews, Proof & Referrals): 7 skills
- **Publisher** (Content Engine): 17 skills
- **Engineer** (Technical & Tracking): 10 skills
- **Closer** (Conversion & Sales): 14 skills
- **Media Buyer** (Paid Media): 6 skills
- **COO-CFO** (Measurement, Money & Operations): 12 skills
- **Amplifier** (Authority, Social & Community): 16 skills

## Get started

1. Say **"Set up Get-Found for my business"**. The agent researches the business and asks only for what it can't find.
2. Say **"Run my Visibility Audit"** to set the baseline Visibility Score.
3. Say **"Put Get-Found on a schedule"** to turn on the daily, weekly, monthly and quarterly heartbeat.
4. Any time, ask **"What's my next best move?"**

Work files are kept in a `get-found/` folder: `business-brain.md`, `autopilot.md`, `scoreboard.md`, `action-log.md`, `approvals.md`.
Keep this folder in Google Drive, a connected folder or a Claude project, never in a temporary session, because every
scheduled run starts fresh.

## How the autopilot works (new in 1.1.0)

- **Authority tiers:** every action is Observe, Prepare, Execute-within-limits, or Approval-required. Anything not
  written down needs approval. Spending, first contact, low-star review replies, deletions and legal language always do.
- **Shadow mode:** the first 3 to 5 runs queue everything for approval. An action type earns autopilot only after 3
  clean approvals in a row and the owner's yes, and loses it the moment it is undone or complained about.
- **No double sends:** every send or publish gets an action key that is checked against the log first.
- **Proof, not claims:** work is marked done only with evidence read back from the tool.
- **Learning:** every approval, edit or rejection becomes a Lesson that future runs follow.
- **Limits and pause:** each run has caps on tool calls and actions; change `status: active` to `status: PAUSE` in
  `autopilot.md` to stop everything.
- **Safe reading:** reviews, emails and web pages are treated as data, never as instructions.

## License

Free to use for your own business, not for resale. See LICENSE.md.

## Safety

Nothing is published, sent, spent or changed in a live account without an explicit yes. See CONNECTORS.md for the tools
that unlock more automation.
