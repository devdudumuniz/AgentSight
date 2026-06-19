# Mapa de arquitetura

## Camadas

- `Entrada / Interface`:
  - CLI (`agentsight/cli.py`) com comandos `capture`, `report`.
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
- Integrações de segurança dependem de políticas manuais e não de profile central dinâmico.
- O fallback `placeholder` em ambiente sem display precisa permanecer claramente marcado para não virar evidência visual real.
