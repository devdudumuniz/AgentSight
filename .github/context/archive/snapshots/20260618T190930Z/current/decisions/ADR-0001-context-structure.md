# ADR-0001: Estrutura de contexto em `.github`

## Status
Aceita

## Contexto
Necessidade de centralizar contexto operacional, decisões e evidências sem espalhar em múltiplas pastas.

## Decisão
Definir `.github/context/current/` como fonte ativa única e `.github/context/archive/` como histórico congelado.

## Consequências
- Redução de ambiguidades de leitura.
- Maior rastreabilidade de mudanças em `changelog` e `reports`.

