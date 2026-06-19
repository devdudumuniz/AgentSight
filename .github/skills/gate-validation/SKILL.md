# Skill: gate-validation

Use antes de declarar qualquer entrega concluida.

## Gates base

```powershell
python -m pip install -e ".[dev]"
ruff check .
python -m pytest
python -m advanced_screenshot_agent.cli --help
screenshot-agent --help
.github/scripts/context/validate-context.ps1
```

## Regras

- Nao declarar sucesso sem resultado objetivo.
- Registrar comando, resultado e erro quando houver.
- Se um gate nao puder rodar, usar `PARTIAL` ou `BLOCKED_BY_ENVIRONMENT`.
