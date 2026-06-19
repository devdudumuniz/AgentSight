# Codex Usage

Use AgentSight when a coding agent needs local visual evidence.

```bash
agentsight capture --mock --label layout-check --scope region --region 0,0,320,180 --consent --output .vision-runs/layout-check --json
agentsight report --run .vision-runs/layout-check
```

Rules for agents:

- Do not capture without explicit consent.
- Treat `mock_capture` as non-real UI evidence.
- Prefer redacted images.
- Do not upload `.vision-runs/` unless the user explicitly asks and the content was reviewed.
