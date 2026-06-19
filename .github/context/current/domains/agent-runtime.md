# Domain: Agent Runtime

## Objetivo
Oferecer uma interface estável para agentes consumirem evidência visual.

## Pontos de atenção
- `capture_screen` e metadados JSON estão no ciclo quente do runtime.
- `report` atual apenas concatena evidências por arquivos locais.
- Adapters web ainda são mínimos e dependem de integração futura.

## Fontes
- `agentsight/capture.py`
- `agentsight/cli.py`
- `agentsight/adapters/playwright.py`
