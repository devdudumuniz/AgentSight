# Módulo: redaction

## O que faz
Detecta padrões textuais (`email`, `cpf`, token-like) e aplica blur por região.

## Entrada principal
- `detect_sensitive_text`, `redact_image_regions`, `redact_regions`

## Riscos
- Cobertura de PII baseada em regex, sem OCR/ML por padrão.
- Integração atual cobre regiões explícitas; detecção automática de regiões sensíveis ainda depende de OCR/classificação futura.
