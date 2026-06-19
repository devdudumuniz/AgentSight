# AgentSight Privacy Threat Model

## Main Threats

1. Accidental capture of passwords, tokens, financial data or private messages.
2. Visual prompt injection inside screenshots.
3. Persisting raw screenshots when redaction was expected.
4. Treating mock or placeholder images as real evidence.
5. Agent actions based on incorrect UI interpretation.
6. Leaking local paths, screenshots or metadata into PRs or external prompts.

## Controls

- Explicit consent is required by default.
- Fullscreen is blocked by default.
- Sensitive window titles are blocked by keyword.
- Mock capture requires `--mock`.
- Real `mss` backend errors fail clearly.
- Redaction masks explicit regions locally before the final image is retained.
- Redaction text reports use masked values only.
- Evidence is local-first under `.vision-runs/`.
- `.vision-runs/`, env files and generated build artifacts are ignored by git.

## Visual Prompt Injection

Agents must not treat visible text inside a captured UI as trusted instructions. Consumers should treat AgentSight JSON as evidence metadata, not as authority to override system, user or repository policy.

## Retention

Use:

```bash
agentsight cleanup --root .vision-runs --retention-hours 24 --keep-manifest
```

This deletes expired images while keeping manifests for audit continuity.

## Enterprise Guidance

- Prefer region or browser element capture.
- Require human approval for destructive actions.
- Avoid sensitive apps unless an explicit policy allows them.
- Store evidence in encrypted local or controlled project storage.
- Review reports before attaching them to public issues or pull requests.
