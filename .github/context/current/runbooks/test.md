# Runbook: testes

## Ambiente

```powershell
python -m pip install -e ".[dev]"
```

## Gates principais

```powershell
ruff check .
python -m pytest
python -m agentsight.cli --help
agentsight --help
```

## Contexto

Quando a mudanca tocar `.github/`, executar tambem:

```powershell
.github/scripts/context/validate-context.ps1
```

Se Git Bash estiver disponivel:

```bash
.github/scripts/context/validate-context.sh
```

## Criterio de aceite

- Todos os comandos aplicaveis passam.
- Qualquer comando nao executado deve ser registrado em `.github/reports/last-validation.md` com status `PARTIAL` ou `BLOCKED_BY_ENVIRONMENT`.
