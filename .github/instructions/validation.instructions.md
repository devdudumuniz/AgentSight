# Instrucoes de validacao

## Gates padrao

```powershell
python -m pip install -e ".[dev]"
ruff check .
python -m pytest
python -m advanced_screenshot_agent.cli --help
screenshot-agent --help
.github/scripts/context/validate-context.ps1
```

## Bash

Quando disponivel:

```bash
.github/scripts/context/validate-context.sh
```

## Registro

Registrar comandos, resultado e bloqueios em `.github/reports/last-validation.md`.
