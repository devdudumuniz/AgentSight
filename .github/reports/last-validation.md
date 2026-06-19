# Last Validation

## Data: 2026-06-19

Status: READY_FOR_REVIEW.

## Gates executados

- `python -m pip install --upgrade pip`: pip atualizado de `26.0.1` para `26.1.2`.
- `python -m pip install -e ".[dev,capture]"`: instalou `agentsight-0.1.0` editavel com extras dev/capture.
- `ruff check .`: `All checks passed!`.
- `python -m pytest`: `20 passed in 2.00s`.
- `python -m build`: gerou `agentsight-0.1.0.tar.gz` e `agentsight-0.1.0-py3-none-any.whl`.
- `python -m agentsight.cli --help`: exibiu comandos `capture`, `annotate`, `redact`, `report`, `cleanup`, `doctor`.
- `agentsight --help`: exibiu comandos `capture`, `annotate`, `redact`, `report`, `cleanup`, `doctor`.
- `agentsight doctor`: retornou JSON `agentsight.doctor.v1` com Python, Pillow, mss, `.vision-runs` gravavel e plataforma OK.
- `agentsight capture --mock --label demo --scope region --region 0,0,200,120 --consent --output .vision-runs/demo --json`: gerou evento `ce0c25cd-e986-4174-aea0-758bf385611c`, backend `mock`, schema `agentsight.capture.v1`.
- `agentsight report --run .vision-runs/demo`: gerou Markdown com tabela de evidencia e imagem relativa.
- `agentsight cleanup --root .vision-runs --retention-hours 0 --keep-manifest`: apagou a imagem mock e preservou JSON/eventos/manifest.

## Validacao de contexto

- `.github/scripts/context/validate-context.ps1`: `VALIDATION_OK`.
- `.github/scripts/context/validate-context.sh` via Git Bash: `VALIDATION_OK`.

## Higiene

- `dist/`, `build/`, `agentsight.egg-info/` e `__pycache__/` gerados por build/test foram removidos.
- `.vision-runs/` permanece ignorado por git; o fluxo de aceite preservou JSON/eventos/manifest apos cleanup.

## Resultado

AgentSight esta funcional como runtime minimo open source: instalavel, testavel, buildavel, com CLI real, mock explicito, policy gate, redaction local, evidence store, report e cleanup.
