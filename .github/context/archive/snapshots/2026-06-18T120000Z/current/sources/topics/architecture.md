# Tópico: Arquitetura

## Visão geral
Camada de captura segura separada por política, captura, evidência e redaction.

## Fontes relacionadas
- `docs/architecture.md`
- `advanced_screenshot_agent/*`

## Fatos confirmados
- Estrutura monobloco simples sem serviços externos.

## Inferências
- Existe oportunidade de separar `EvidenceRun` persistente e cadeia de hashes.

## Decisões existentes
- ADRs locais de estrutura e loading order.

