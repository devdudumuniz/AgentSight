# Estado atual do projeto

## Status

- estado: READY_FOR_REVIEW
- data-base: 2026-06-19
- repositorio: pacote Python/CLI `advanced-screenshot-agent`

## Fatos confirmados

- Stack principal: Python >= 3.10 com `setuptools`.
- Package manager detectado: `pip` via `pyproject.toml`.
- Testes: `pytest` configurado em `pyproject.toml`.
- Lint: `ruff` configurado em `pyproject.toml`.
- Typecheck: `mypy` declarado em extra `dev`, sem script dedicado no repositorio.
- Docker/Compose: nenhum `Dockerfile` ou compose detectado na raiz atual.
- Agente executavel: somente `.github/agents/main.agent.md`.
- CI: `.github/workflows/ci.yml` instala `.[dev]`, roda `ruff check .` e `python -m pytest`.

## Estado funcional conhecido

- CLI publica `screenshot-agent` com comandos `capture` e `report`.
- `capture` exige consentimento por politica padrao.
- Captura fullscreen permanece bloqueada por padrao.
- `capture` aceita `--region`, `--redact-region` e `--no-redact`.
- Redaction regional pode ser aplicada em memoria antes de salvar a imagem final.
- Redaction textual por regex existe como detector auxiliar; OCR/classificacao automatica ainda nao estao no fluxo padrao.
- Evidence graph existe em formato basico via `EvidenceRun` e `EvidenceEvent`.

## Inferencias

- O projeto esta em fase base auditavel, antes de release publico.
- A prioridade tecnica seguinte e fechar lacunas de retencao, OCR/classificacao sensivel e adapter Playwright.

## Bloqueios atuais

- Nenhum bloqueio de ambiente registrado nesta atualizacao de contexto.
