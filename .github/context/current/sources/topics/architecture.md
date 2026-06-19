# Tópico: Arquitetura

## Visão geral
Camada de captura segura separada por política, captura, evidência e redaction.

## Fontes relacionadas
- `docs/architecture.md`
- `agentsight/cli.py`
- `agentsight/capture.py`
- `agentsight/policy.py`
- `agentsight/evidence.py`
- `agentsight/redact.py`
- `agentsight/adapters/playwright.py`

## Fatos confirmados
- Estrutura monobloco simples sem serviços externos.

## Inferências
- Existe oportunidade de separar `EvidenceRun` persistente e cadeia de hashes.

## Decisões existentes
- ADRs locais de estrutura e loading order.
