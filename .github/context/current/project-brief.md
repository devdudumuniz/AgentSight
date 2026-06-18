# Project Brief — este projeto

## Nome real identificado
- `advanced-screenshot-agent` (definido em `README.md` e `pyproject.toml`)

## Escopo
- Biblioteca/CLI Python para captura de tela com segurança por política, redaction e trilha de evidências.
- Foco em camada de percepção para agentes de IA com compliance operacional.

## Stack real
- Python 3.10+ (ver `pyproject.toml`)
- Dependências: `pillow`, `mss`, `cryptography`
- CLI via `setuptools` e `project.scripts` (`screenshot-agent`)
- Testes: `pytest`
- Qualidade: `ruff`

## Status técnico atual
- Código funcional mínimo com pontos conhecidos:
  - fluxo de captura (`capture.py`)
  - política de consentimento e validação (`policy.py`)
  - evidência básica (`evidence.py`)
  - redaction por região (`redact.py`)
  - CLI com `capture` e `report` (`cli.py`)
  - adapter Playwright experimental (`adapters/playwright.py`)
- Workflow de CI alinhado à raiz do repositório e cobrindo o pacote Python real.

## Objetivo do contexto
- Transformar `.github` em base única de operação, memória e decisão.
- Dar suporte a respostas com fonte e evidência quando houver material real.
