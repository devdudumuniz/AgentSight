# Instruções de backend (`agentsight`)

- Linguagem real detectada: Python (CLI + pacote instalável).
- Entry point: `agentsight.cli:main` exposto via `agentsight`.
- Validar sempre:
  - políticas (`policy.py`)
  - capture (`capture.py`)
  - evidência (`evidence.py`)
  - redaction (`redact.py`)
- Estrutura de teste: `tests/` com `pytest`.
