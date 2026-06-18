# Instruções de backend (`advanced_screenshot_agent`)

- Linguagem real detectada: Python (CLI + pacote instalável).
- Entry point: `advanced_screenshot_agent.cli:main` exposto via `screenshot-agent`.
- Validar sempre:
  - políticas (`policy.py`)
  - capture (`capture.py`)
  - evidência (`evidence.py`)
  - redaction (`redact.py`)
- Estrutura de teste: `tests/` com `pytest`.

