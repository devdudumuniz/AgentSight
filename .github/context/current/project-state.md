# Estado atual do projeto

## Status

- estado: READY_FOR_REVIEW
- data-base: 2026-06-19
- repositorio: pacote Python/CLI `agentsight`

## Fatos confirmados

- Produto: AgentSight - Secure Vision Layer for AI Agents.
- Stack principal: Python >= 3.10 com `setuptools`.
- Package manager detectado: `pip` via `pyproject.toml`.
- Testes: `pytest` configurado em `pyproject.toml`.
- Lint: `ruff` configurado em `pyproject.toml`.
- Build: `python -m build` via extra `dev`.
- Typecheck: `mypy` declarado em extra `dev`, ainda sem gate dedicado no CI.
- Docker/Compose: nenhum `Dockerfile` ou compose detectado na raiz atual.
- Agente executavel: somente `.github/agents/main.agent.md`.
- CI: `.github/workflows/ci.yml` instala `.[dev,capture]`, roda `ruff check .`, `python -m pytest`, `python -m build` e smoke de CLI.

## Estado funcional conhecido

- CLI publica `agentsight` com comandos `capture`, `annotate`, `redact`, `report`, `cleanup` e `doctor`.
- `screenshot-agent` existe apenas como alias legado temporario.
- `capture` exige consentimento por politica padrao.
- Captura fullscreen permanece bloqueada por padrao.
- Mock exige flag explicita `--mock`; falhas reais de backend nao viram placeholder.
- `capture` aceita `--scope`, `--region`, `--redact-regions`, `--mock` e `--json`.
- Redaction regional pode ser aplicada em memoria antes de salvar a imagem final.
- Redaction textual por regex existe como detector auxiliar; OCR/classificacao automatica ainda nao estao no fluxo padrao.
- Evidence store grava `events.jsonl` e `manifest.json`.

## Inferencias

- O projeto esta em fase base auditavel, antes de release publico.
- A prioridade tecnica seguinte e validar release v0.1 no GitHub e evoluir OCR/classificacao sensivel e fluxos Playwright.

## Bloqueios atuais

- Nenhum bloqueio de ambiente registrado nesta atualizacao de contexto.
