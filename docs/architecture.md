# AgentSight Architecture

AgentSight is a secure vision layer for AI agents. Its core job is to make visual context scoped, consented, redacted and auditable before an agent consumes it.

## Pipeline

```text
agent/user request
-> CapturePolicy
-> CaptureAdapter
-> RedactionPipeline
-> EvidenceStore
-> MarkdownReport
-> Agent-safe JSON
```

## Modules

- `agentsight.policy`: consent, scope and safety gate.
- `agentsight.adapters.mss_capture`: real desktop capture through `mss`; no placeholder fallback.
- `agentsight.adapters.playwright`: async browser/page/locator capture helpers.
- `agentsight.capture`: orchestration, mock capture, hashing, redaction and evidence write.
- `agentsight.redact`: sensitive text detection, safe masking and region blur.
- `agentsight.evidence`: JSONL events, manifest, hashes and agent export.
- `agentsight.report`: Markdown report generation.
- `agentsight.cleanup`: retention cleanup for local evidence images.
- `agentsight.annotate`: local visual annotation.
- `agentsight.cli`: installable command line interface.

## Capture Sequence

1. CLI or Python API creates a `CaptureConfig`.
2. `CapturePolicy.validate_capture_request()` checks consent, scope, fullscreen and region rules.
3. Real capture calls `mss_capture`; explicit mock capture uses `--mock`.
4. If redaction regions are provided, AgentSight writes a redacted final image and removes the raw temporary image.
5. `EvidenceStore` appends an event to `events.jsonl`.
6. `manifest.json` is updated for the run.
7. The CLI returns agent-safe JSON.

## JSON Schema

Minimum capture event:

```json
{
  "schema_version": "agentsight.capture.v1",
  "event_id": "uuid",
  "label": "checkout",
  "scope": "region",
  "backend": "mss|mock|playwright",
  "image_path": ".vision-runs/run/capture.png",
  "redacted_image_path": ".vision-runs/run/capture.redacted.png|null",
  "sha256": "hex",
  "timestamp_utc": "iso-8601",
  "policy": {
    "consent_required": true,
    "fullscreen_allowed": false
  },
  "warnings": []
}
```

## Design Constraints

- No capture without explicit consent.
- No fullscreen by default.
- No automatic placeholder when real capture fails.
- No external network calls.
- No raw secret values in reports.
- No test depends on a real display.
