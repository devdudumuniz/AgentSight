# AgentSight Skill

Use this skill when an agent needs visual evidence from a UI, QA workflow, PR review or local debugging session.

## When To Use

- Validate a visible UI state.
- Capture before/after evidence.
- Produce an auditable local report.
- Give an AI agent scoped visual context.

## When Not To Use

- Screens with passwords, tokens, banking data or private messages unless explicitly approved.
- Background or continuous recording.
- Fullscreen capture without human approval.
- Any flow where a mock image would be presented as real evidence.

## Commands

```bash
agentsight doctor
agentsight capture --mock --label demo --scope region --region 0,0,200,120 --consent --output .vision-runs/demo --json
agentsight report --run .vision-runs/demo
agentsight cleanup --root .vision-runs --retention-hours 24 --keep-manifest
```

Real region capture:

```bash
agentsight capture --label checkout --scope region --region 100,100,800,600 --consent --output .vision-runs/checkout --json
```

## Safety Rules

- Always request explicit user consent.
- Prefer region or locator capture.
- Use `--mock` only when mock evidence is acceptable and label it as mock.
- Use `--redact-regions` before retaining sensitive regions.
- Never attach `.vision-runs/` blindly to public issues or PRs.

## Response Format

Report:

- command executed;
- run directory;
- event id;
- whether capture was real or mock;
- whether redaction was applied;
- report path or Markdown output;
- warnings from AgentSight JSON.
