# Módulo: redaction

## O que faz
Detecta padrões textuais (`email`, `cpf`, token-like) e aplica blur por região.

## Entrada principal
- `detect_sensitive_text`, `redact_regions`

## Riscos
- Cobertura de PII baseada em regex, sem OCR/ML por padrão.
- Necessita integração com pipeline de decisão para reduzir falsos positivos/negativos.

