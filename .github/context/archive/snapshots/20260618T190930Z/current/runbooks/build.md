# Runbook: Build e validação local

## Objetivo
Assegurar integridade mínima do projeto após mudança.

## Comandos
- `python -m pip install -e ".[dev]"`
- `ruff check .`
- `pytest`

## Critérios de aceitação
- Sem falhas de lint e testes.
- Relatar saída completa em `reports/last-validation.md`.

