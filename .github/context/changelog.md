# Changelog de contexto

## 2026-06-18
- Estrutura completa de agente de contexto implantada em `.github`.
- Adicionado agente principal único: `.github/agents/main.agent.md`.
- Consolidado camada de fontes inspirada em NotebookLM em `.github/context/current/sources/`.
- Criados `manifest.json`, `roadmap`, `gates`, `reports`, `decisions` e scripts de contexto.
- Registradas equipes de domínio/módulo/perfil baseadas no código e documentação existentes.
- Snapshot inicial criado em `.github/context/archive/snapshots/2026-06-18T000000Z`.
- Validação executada:
  - `validate-context.ps1`: `VALIDATION_OK`.
  - `ruff check .`: `All checks passed!`
  - `python -m pytest`: `9 passed`.
  - `bash` indisponível no ambiente para scripts `.sh` (BLOCKED_BY_ENVIRONMENT).
- Revisão de alinhamento estrutural e funcional executada nesta sessão:
  - removido agente legado `./.github/zuza-code-orchestrator.agent.md`, mantendo apenas `main.agent.md` como executável;
  - corrigidos caminhos de fonte de `topics/privacy.md` para `topics/security.md`;
  - alinhados `README.md`, workflow de CI e entrypoint do módulo CLI ao root real do repositório;
  - adicionada regressão para `python -m advanced_screenshot_agent.cli --help`;
  - validação executada com sucesso:
    - `python -m pip install -e ".[dev]"`;
    - `ruff check .`;
    - `python -m pytest` (`10 passed`);
  - `python -m advanced_screenshot_agent.cli --help`;
  - `screenshot-agent --help`;
  - `.github/scripts/context/validate-context.ps1`;
  - `.github/scripts/context/validate-context.sh` via Git Bash.
- Snapshot de revisão final criado em `.github/context/archive/snapshots/20260618T190930Z`.
