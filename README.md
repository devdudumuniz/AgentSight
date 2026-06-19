# AgentSight

**AgentSight - Secure Vision Layer for AI Agents.**

[![CI](https://github.com/devdudumuniz/AgentSight/actions/workflows/ci.yml/badge.svg)](https://github.com/devdudumuniz/AgentSight/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

AgentSight gives AI agents scoped, policy-controlled visual context without turning your workstation into an uncontrolled screenshot recorder.

It is not a screenshot tool. It is a governed vision runtime:

```text
policy gate -> scoped capture -> local redaction -> evidence trail -> agent-safe JSON
```

## What It Does

- Requires explicit consent before capture.
- Blocks fullscreen capture by default.
- Captures only scoped regions unless policy allows more.
- Applies local redaction to explicit regions before keeping the final image.
- Writes audit evidence to `events.jsonl` and `manifest.json`.
- Generates Markdown reports for QA, PR review and agent handoff.
- Exposes stable JSON for Codex, Claude Code, Cursor, Zuza and internal agents.
- Never sends images, OCR, metadata or reports to external services.

## What It Is Not

- Not a background screen recorder.
- Not a replacement for user approval.
- Not an OCR cloud pipeline.
- Not a way to bypass privacy controls.
- Not a visual automation loop that clicks without governance.

## Installation

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev,capture]"
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev,capture]"
```

## Quickstart

Explicit mock capture for CI, docs and agent testing:

```bash
agentsight capture --mock --label demo --scope region --region 0,0,200,120 --consent --output .vision-runs/demo --json
agentsight report --run .vision-runs/demo
agentsight cleanup --root .vision-runs --retention-hours 0 --keep-manifest
```

Real region capture with `mss`:

```bash
agentsight capture --label checkout --scope region --region 100,100,800,600 --consent --output .vision-runs/checkout --json
```

Real fullscreen capture is blocked unless explicitly allowed:

```bash
agentsight capture --label full --scope fullscreen --consent --allow-fullscreen --output .vision-runs/full --json
```

Region redaction before final persistence:

```bash
agentsight capture --mock --label redacted --scope region --region 0,0,400,240 --redact-regions 20,20,180,60 --consent --output .vision-runs/redacted --json
```

`screenshot-agent` remains as a temporary legacy alias for compatibility. New usage should call `agentsight`.

## CLI

```bash
agentsight --help
agentsight doctor
agentsight capture --help
agentsight annotate --help
agentsight redact --help
agentsight report --help
agentsight cleanup --help
```

Commands:

- `capture`: policy-controlled capture with real or explicit mock backend.
- `annotate`: draw local visual annotations.
- `redact`: blur explicit image regions and return a redaction report.
- `report`: generate a Markdown evidence report from a run.
- `cleanup`: remove expired images while preserving manifests when requested.
- `doctor`: verify Python, Pillow, optional `mss`, platform and writable `.vision-runs`.

## Python API

```python
from pathlib import Path

from agentsight.capture import CaptureConfig, capture

result = capture(
    CaptureConfig(
        label="demo",
        output_dir=Path(".vision-runs/demo"),
        scope="region",
        region=(0, 0, 200, 120),
        consent=True,
        mock=True,
    )
)

print(result["schema_version"])
print(result["image_path"])
```

## Agent-Safe JSON

Every capture returns stable JSON:

```json
{
  "schema_version": "agentsight.capture.v1",
  "event_id": "...",
  "label": "demo",
  "scope": "region",
  "backend": "mock",
  "image_path": ".vision-runs/demo/demo.png",
  "redacted_image_path": null,
  "sha256": "...",
  "timestamp_utc": "...",
  "policy": {
    "consent_required": true,
    "fullscreen_allowed": false
  },
  "warnings": ["mock_capture"]
}
```

## Security Model

- Consent is required by default.
- Fullscreen is denied by default.
- Sensitive window titles are blocked by policy keywords.
- Mock capture is explicit via `--mock`; real capture failures do not turn into placeholders.
- Redaction reports mask secrets and do not include raw sensitive values.
- `.vision-runs/`, temporary images, secrets and local env files are ignored by git.

## GitHub Topics

Suggested repository topics:

`ai-agents`, `computer-use`, `visual-evidence`, `privacy`, `redaction`, `qa-automation`, `agent-tools`, `python-cli`, `playwright`, `local-first`

## Status

`v0.1` functional runtime foundation:

- Policy gate: implemented.
- Scoped region capture: implemented via `mss` extra.
- Explicit mock capture: implemented.
- Local region redaction: implemented.
- Evidence store: implemented.
- Markdown report: implemented.
- Cleanup: implemented.
- CI lint/test/build/CLI smoke: configured.

Not yet complete:

- OCR-driven sensitive-region detection.
- Browser workflow capture beyond the adapter primitives.
- MCP/server mode.
- Enterprise policy profiles.
