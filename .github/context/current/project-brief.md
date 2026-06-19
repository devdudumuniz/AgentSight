# Project Brief - AgentSight

## Nome real identificado
- `agentsight` (definido em `README.md` e `pyproject.toml`)

## Escopo
- Secure vision layer for AI agents.
- Runtime Python/CLI para captura escopada, consentimento, redaction local, trilha de evidencias e JSON seguro para agentes.

## Stack real
- Python 3.10+ (ver `pyproject.toml`)
- Dependencias base: `pillow`, `cryptography`
- Extras: `capture` (`mss`), `ocr`, `vision`, `playwright`, `dev`
- CLI via `setuptools` e `project.scripts` (`agentsight`)
- Alias legado temporario: `screenshot-agent`
- Testes: `pytest`
- Qualidade: `ruff`

## Status técnico atual
- `agentsight/` e o pacote primario.
- `advanced_screenshot_agent/` e apenas shim de compatibilidade com `DeprecationWarning`.
- CLI completa: `capture`, `annotate`, `redact`, `report`, `cleanup`, `doctor`.
- Evidence store unificado em `events.jsonl` e `manifest.json`.
- Mock exige `--mock`; falha real de captura nao vira placeholder automatico.
- Workflow `agentsight-ci` roda Python 3.10, 3.11 e 3.12 com lint, testes, build e smoke do CLI.

## Objetivo do contexto
- Transformar `.github` em base única de operação, memória e decisão.
- Dar suporte a respostas com fonte e evidência quando houver material real.
