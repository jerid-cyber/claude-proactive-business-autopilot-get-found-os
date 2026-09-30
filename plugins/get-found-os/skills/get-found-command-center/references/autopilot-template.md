# Get-Found Autopilot
status: active            # active | PAUSE | complete
mode: shadow              # shadow | live
workspace: <durable location of the get-found/ folder, e.g. Google Drive "Get-Found - <Business>" or a connected folder path>
last_run: <ISO datetime, owner's time zone>
shadow_runs_completed: 0
owner: <name>
approver: <name from the Business Brain>
report_to: <chat | email address>
time_zone: <IANA zone, e.g. America/Denver>
quiet_hours: <e.g. 20:00-07:00; no sends during these hours>

To pause everything, change `status: active` to `status: PAUSE`. Scheduled runs still wake up but stop immediately.

## Limits (per run)
max_tool_calls: 40 | max_actions: 10 | max_retries: 2 | max_moves: 3 | daily_send_cap: 20

## Authority Policy
See the plugin's authority-tiers reference for the tier rules.
- T0 Observe: research, audits, reading connected data
- T1 Prepare: drafts, internal reports, scoreboard, action log
- T2 Execute (action type | scope | content | frequency | daily cap):
  - (none yet: everything starts in shadow mode)
- T3 Approval required: everything else

## Graduations
- <date> <action type> moved T3 -> T2 (<n> clean approvals, approved by <name>)

## Approval streaks
| action type | clean approvals in a row | last result |
| --- | --- | --- |

## Monthly batch pointer
next_monthly_batch: A      # A | B | C | D

## Not applicable
not_applicable: []         # skills that do not fit this business; scheduled runs skip them

## Lessons
<!-- One line per owner decision that should change future behavior. Read at the start of every run. -->
- <date> <approved | edited | rejected | undone>: <what> -> <rule to follow from now on>
