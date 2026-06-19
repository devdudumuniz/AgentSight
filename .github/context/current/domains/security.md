# Domain: Security

## Objetivo
Controlar escopo, consentimento e tratamento de dados sensíveis durante captura.

## Fontes
- `agentsight/policy.py`
- `docs/privacy-threat-model.md`
- `README.md`

## Decisões
- Fullscreen bloqueado por padrão (`allow_fullscreen=False`).
- Consentimento explícito obrigatório (`require_user_consent=True`).
- Redaction e mascaramento antes de persistir/compartilhar quando aplicável.
