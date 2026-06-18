# Mapa de arquitetura

## Camadas

- `Entrada / Interface`:
  - CLI (`advanced_screenshot_agent/cli.py`) com comandos `capture`, `report`.
- `Domínio de captura`:
  - `capture.py` (orquestra captura e metadados),
  - `policy.py` (governança de segurança),
  - `adapters/playwright.py` (integração web).
- `Privacidade`:
  - `redact.py` (remoção/blur de regiões),
  - `crypto.py` (criptografia de arquivos).
- `Evidência`:
  - `evidence.py` (eventos/manifesto),
  - `annotate.py` (anotações visuais).

## Dependências externas
- Bibliotecas de captura e imagem (`mss`, `PIL`).
- Opcional: visão/OCR/Playwright conforme futuras metas.

## Riscos arquitetônicos
- Persistência local sem política única de retenção no CLI atual.
- CI legado com path incorreto.
- Integrações de segurança dependem de políticas manuais e não de profile central dinâmico.

