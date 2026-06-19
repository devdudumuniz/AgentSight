# Changelog de contexto

## 2026-06-19 - redaction integrada
- `capture` passou a suportar `--region`, `--redact-region` e `--no-redact`.
- Redaction regional agora e aplicada em memoria antes de salvar a imagem final quando regioes sao informadas.
- Metadata de captura registra `redact_applied`, `redaction_regions` e `redaction_regions_count`.
- Testes de regressao adicionados para redaction integrada, conflito `redact=False` com regioes e CLI help.
- README, roadmap, contexto de modulo e riscos atualizados para refletir o estado real.

## 2026-06-19
- Completada a estrutura obrigatoria do agente de contexto conforme prompt mestre v2.
- `main.agent.md` endurecido como unico agente executavel, com hot/warm/cold memory, evidence layer, estados oficiais, criterios de qualidade, parada, rollback e checklist minimo.
- Adicionados arquivos hot obrigatorios ausentes: `project-state.md`, `active-scope.md` e `known-risks.md`.
- Adicionados controles de governanca em `technical-debt.md`, `regression-watchlist.md`, `open-decisions.md`, `non-goals.md` e `ADR-0003-governance-model.md`.
- Adicionados runbook de testes, dominios de QA/observabilidade/infra e perfis de coordenacao, desenvolvimento, QA, docs e seguranca.
- Criadas instrucoes faltantes: `context-loading`, `execution`, `documentation` e `validation`.
- Criado `docs-sync.prompt.md`.
- Criadas skills operacionais: `context-refresh`, `context-audit`, `source-deep-dive`, `regression-recovery`, `gate-validation` e `roadmap-sync`.
- Evidence layer ampliada para registrar `pyproject.toml`, CI, codigo runtime e testes como fontes reais com cards dedicados.
- `manifest.json` atualizado para versao `1.1.0`, representando hot/warm/cold memory, evidence layer, arquivos e diretorios obrigatorios.
- `validate-context.ps1` e `validate-context.sh` endurecidos para validar manifesto, hot memory, diretorios obrigatorios, agente unico e proibicao de `archive/latest`.

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
