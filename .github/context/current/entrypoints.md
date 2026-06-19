# Entry points reais

- CLI principal: `agentsight`
  - Script: `agentsight.cli:main`
  - Configurado em `pyproject.toml` (`[project.scripts]`)

- Entrada Python direta:
  - `python -m agentsight.cli ...` (uso local)

## Alias legado

- `screenshot-agent` aponta para `agentsight.cli:main` apenas por compatibilidade temporaria.
- Novos comandos devem usar `agentsight`.
