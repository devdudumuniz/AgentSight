# Domain: Agent Runtime

## Objetivo
Oferecer uma interface estável para agentes consumirem evidência visual.

## Pontos de atenção
- `capture_screen` e metadados JSON estão no ciclo quente do runtime.
- `report` atual apenas concatena evidências por arquivos locais.
- Adapters web ainda são mínimos e dependem de integração futura.

## Fontes
- `advanced_screenshot_agent/capture.py`
- `advanced_screenshot_agent/cli.py`
- `advanced_screenshot_agent/adapters/playwright.py`

