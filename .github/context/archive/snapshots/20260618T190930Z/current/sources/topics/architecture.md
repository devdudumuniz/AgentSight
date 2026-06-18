# Tópico: Arquitetura

## Visão geral
Camada de captura segura separada por política, captura, evidência e redaction.

## Fontes relacionadas
- `docs/architecture.md`
- `advanced_screenshot_agent/cli.py`
- `advanced_screenshot_agent/capture.py`
- `advanced_screenshot_agent/policy.py`
- `advanced_screenshot_agent/evidence.py`
- `advanced_screenshot_agent/redact.py`
- `advanced_screenshot_agent/adapters/playwright.py`

## Fatos confirmados
- Estrutura monobloco simples sem serviços externos.

## Inferências
- Existe oportunidade de separar `EvidenceRun` persistente e cadeia de hashes.

## Decisões existentes
- ADRs locais de estrutura e loading order.
