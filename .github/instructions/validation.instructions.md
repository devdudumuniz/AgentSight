# Instrucoes de validacao

## Gates padrao

```powershell
python -m pip install -e ".[dev]"
python -m pip install -e ".[dev,capture]"
ruff check .
python -m pytest
python -m agentsight.cli --help
agentsight --help
agentsight doctor
.github/scripts/context/validate-context.ps1
```

## Bash

Quando disponivel:

```bash
.github/scripts/context/validate-context.sh
```

## Registro

Registrar comandos, resultado e bloqueios em `.github/reports/last-validation.md`.
