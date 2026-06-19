# Dominio: QA

## Escopo

Qualidade de codigo, testes unitarios, gates de contexto e validacao operacional do CLI.

## Fontes

- `pyproject.toml`
- `tests/`
- `.github/workflows/ci.yml`
- `.github/gates/`
- `.github/scripts/context/`

## Gates atuais

- `ruff check .`
- `python -m pytest`
- `python -m agentsight.cli --help`
- `agentsight --help`
- `.github/scripts/context/validate-context.ps1`
- `.github/scripts/context/validate-context.sh` quando Bash estiver disponivel.

## Riscos

- Sem typecheck obrigatorio no CI atual.
- Testes visuais ainda nao provam captura real em todos os ambientes desktop.
