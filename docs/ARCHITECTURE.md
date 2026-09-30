# Architecture

## Layers

| Layer | Component | Role |
| --- | --- | --- |
| Memory | `get-found/business-brain.md`, `scoreboard.md`, `action-log.md`, `approvals.md` | Plain-Markdown shared state every skill reads and writes |
| Onboarding | `business-brain-setup` + `references/business-brain-template.md` | Research-first setup; one round of questions; flags conflicting facts |
| Orchestration | `get-found-command-center` + `references/skill-catalog.md`, `references/visibility-score.md` | Keeps the Visibility Score, ranks gaps, routes work, fires event chains, enforces approval gates |
| Scheduling | `get-found-heartbeat` | Creates daily/weekly/monthly/quarterly scheduled tasks with standalone prompts |
| Specialists | 9 agents in `agents/` | Run multi-step department work through the 4 phases |
| Execution | 100 ranked skills in `skills/` | Each: purpose, autonomy mode, triggers, 4 phases, measurable result, channel guidance, guardrails, related skills |

## Anatomy of a ranked skill

Every ranked `SKILL.md` has the same structure:

1. **Frontmatter** — `name`, trigger-rich `description`, and `metadata` (`rank`, `channel`, `department`, `autonomy`, `cadence`, `edition`)
2. **Header** — rank, department, channel, autonomy, monitor cadence
3. **Purpose**
4. **Agent operating mode** — before/after checklist (Business Brain, scoreboard, connectors, action log, approvals)
5. **Triggers** — owner asks, audit gap, and the event conditions that route here
6. **Phase 1 Discovery & Assessment** → **Phase 2 Architecture & Design** → **Phase 3 Implementation & Deployment** → **Phase 4 Optimization & Governance**, each with a stated output
7. **Measurable result** — the KPI target, measured against the Phase 1 baseline
8. **Channel guidance** — answer-first writing, fact consistency, AI-citation strategy, platform rules
9. **Approval gates and guardrails**
10. **Related skills**

## Data flow

```
Owner request / heartbeat / event trigger
        │
        ▼
command center ── reads ──▶ business-brain.md, scoreboard.md, approvals.md
        │ next-best-move formula (points × revenue weight ÷ effort), max 3 moves
        ▼
department agent or skill ── runs 4 phases ──▶ connectors → exports → public data/web research
        │
        ├──▶ scoreboard.md   (baseline + new KPI values)
        ├──▶ action-log.md   (every change)
        └──▶ approvals.md    (anything public / sent / spent / live — waits for a yes)
```

## Autonomy modes

| Mode | Count | Meaning |
| --- | --- | --- |
| Autopilot | 50 | Agent runs all phases; stops only at approval gates |
| Agent-heavy | 44 | Agent does nearly all work; preps one short human step |
| Human-led, agent-coached | 6 | Human does core work (filming, photography, interviews); agent plans, coaches and packages |
