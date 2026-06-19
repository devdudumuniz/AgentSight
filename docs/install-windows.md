# Install AgentSight On Windows

## Requirements

- Windows 10/11
- Python 3.10+
- PowerShell

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev,capture]"
```

## Verify

```powershell
agentsight --help
agentsight doctor
agentsight capture --mock --label demo --scope region --region 0,0,200,120 --consent --output .vision-runs/demo --json
agentsight report --run .vision-runs/demo
```

## Troubleshooting

- If real capture fails, verify that `mss` is installed with `python -m pip install -e ".[capture]"`.
- If running headless or over a restricted remote session, use `--mock` for tests and CI.
- Do not use `--allow-fullscreen` unless the capture scope is approved.
- Evidence runs are written under `.vision-runs/` by default and should not be committed.
