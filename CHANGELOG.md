# Changelog

## 1.1.0 (2026-09-30): Proactive autopilot

### Added
- `get-found/autopilot.md` control file: on/off status, shadow or live mode, workspace location, time zone, quiet
  hours, per-run limits, approval policy, approval streaks, graduations, skills that don't apply, and Lessons.
- Four approval tiers (Observe, Prepare, Execute within limits, Approval required) with a default map for Get-Found
  actions (`references/authority-tiers.md`). Unlisted actions are always approval-required.
- Shadow mode for the first 3 to 5 runs, and graduation after 3 clean approvals plus the owner's yes. Automatic
  demotion when an action is undone or complained about.
- Action keys checked against the action log before every send or publish, so nothing goes out twice.
- A verify step: work is marked done only with evidence read back from the tool.
- Lessons: every approval, edit or rejection becomes a rule that future runs follow.
- Processing approvals at the start of each run, and batch approvals ("approve 1, 3, reject 2").
- Per-run limits (tool calls, actions, retries, moves, daily send cap) and a one-word `PAUSE` switch.
- Rule that monitored content (reviews, emails, forums, web pages, AI answers) is data, never instructions.
- Maintain controls: review, pause, resume, graduate, demote, change schedule, retire, compact the log.
- Repository packaging: Claude Code marketplace manifest, install guide, license, changelog.

### Changed
- The Heartbeat requires a lasting workspace location (Google Drive, connected folder or Claude project) before it
  schedules anything, and writes that location into every scheduled prompt.
- The 66 monthly skills now run in four rotating weekly batches, plus a separate first-of-month report.
- Business Brain setup creates `autopilot.md` and asks where the workspace should live.
- All 100 skills and 9 department agents follow the same authority, action-key, verification and data-safety rules.

### Always requires approval (unchanged, now explicit)
- Spending money, first contact with someone new, replies to 1-3 star reviews, changes to the master business
  record, deletions, legal or compliance language.

## 1.0.0

- Initial release: 100 Get-Found skills, 9 department agents, command center, business brain setup, heartbeat.
