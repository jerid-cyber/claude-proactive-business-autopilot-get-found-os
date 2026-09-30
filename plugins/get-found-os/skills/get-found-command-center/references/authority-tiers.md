# Authority Tiers

Every action the Get-Found agent takes sits in exactly one tier. Tiers depend on **risk and reversibility**, never on how
confident the model feels. Self-reported confidence is not calibrated, so it is never a gate.

| Tier | The agent may | Examples |
| --- | --- | --- |
| **T0 Observe** | Read and analyze | Read GBP insights, reviews, Search Console, GA4, ad accounts, CRM, inbox; run AI-answer tests; web research |
| **T1 Prepare** | Create drafts and internal files nobody outside sees | Review-reply drafts, content drafts, audits, scoreboard updates, action log, internal reports, proposed changes |
| **T2 Execute within limits** | Reversible internal changes and pre-approved messages, only inside a written permission | Tag or move a CRM lead, update a CRM field, send an approved template to a named audience with a frequency cap, reply to a 5-star review using an approved pattern |
| **T3 Approval required** | Only queue the action in `get-found/approvals.md` | See the list below |

## Always T3 (never graduate)

- Spending money, raising a budget or bid, launching or unpausing a paid campaign.
- First contact with a person or organization the business has never contacted.
- Replying publicly to any review of 1-3 stars, or anything in a reputation crisis.
- Publishing or changing the master business record (name, address, phone, hours, categories).
- Deleting anything (pages, listings, posts, contacts, campaigns, files).
- Legal, contract, pricing or guarantee language; anything touching the compliance rules in the Business Brain.
- Website changes that affect URLs, redirects, robots.txt, canonical tags or tracking code.
- Anything not listed in `get-found/autopilot.md`. **When an action is not listed, it is T3.**

## Default map for Get-Found actions

| Action type (key prefix) | Starting tier | Can graduate to T2? |
| --- | --- | --- |
| Research, audits, AI-answer tests (`research`) | T0 | n/a |
| Drafts, briefs, reports, scoreboard (`draft`) | T1 | n/a |
| Reply to a 4-5 star review (`review-reply`) | T3 | Yes |
| Review request to a customer who just completed a job (`review-request`) | T3 | Yes |
| Speed-to-lead first reply to an inbound lead who contacted the business (`lead-reply`) | T3 | Yes |
| Follow-up to an existing lead or quote in an approved sequence (`follow-up`) | T3 | Yes |
| GBP post from an approved content calendar (`gbp-post`) | T3 | Yes |
| Social post from an approved content calendar (`social-post`) | T3 | Yes |
| Publish a blog or FAQ post already approved as a draft (`publish-content`) | T3 | Yes |
| CRM field, tag or stage update (`crm-update`) | T3 | Yes |
| Pause an ad that breaches the spending rule in the Business Brain (`ad-pause`) | T3 | Yes (pausing only) |
| Forum or Reddit answer (`forum-post`) | T3 | No |
| Anything in "Always T3" | T3 | No |

## Writing a T2 permission

Each T2 permission in `get-found/autopilot.md` must state all four fields:

```
- <action type> | scope: <who/what> | content: <template or rule> | frequency: <per contact/per item> | daily cap: <n>
```

Example:

```
- review-reply | scope: Google reviews rated 4-5 stars with no reply | content: reply pattern "5-star v2" in brand voice, no incentives, no personal data | frequency: one reply per review | daily cap: 10
```

Where possible, also enforce the limit in the tool itself (draft-only access, a dedicated CRM tag, a sender with a
sending limit). A limit that only exists in the prompt is weaker.

## Shadow mode and graduation

- New installs start with `mode: shadow`. In shadow mode, every T2 action is treated as T3 and queued.
- Keep shadow mode for at least the first 3 to 5 runs.
- An action type may graduate to T2 only when (a) it is marked "can graduate" above, (b) the owner approved it at least
  3 times in a row with no edits, and (c) the owner says yes to the graduation. Record it:
  `- <date> <action type> moved T3 -> T2 (<n> clean approvals, approved by <name>)`.
- Switching `mode: live` is the owner's call. Live mode only affects action types that have a written T2 permission.
- **Demote immediately** when a T2 action is undone, edited after the fact, or complained about: move it back to T3 and
  add a Lesson.
