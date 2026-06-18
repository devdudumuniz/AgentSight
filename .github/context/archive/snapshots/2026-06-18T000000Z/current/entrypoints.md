# Entry points reais

- CLI principal: `screenshot-agent`
  - Script: `advanced_screenshot_agent.cli:main`
  - Configurado em `pyproject.toml` (`[project.scripts]`)

- Entrada Python direta:
  - `python -m advanced_screenshot_agent.cli ...` (uso local)

## Observação

- O workflow atual `.github/workflows/ci.yml` não está alinhado ao caminho da raiz atual (`working-directory` aponta para pasta inexistente para este repo).  

