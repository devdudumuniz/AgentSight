# ADR-0001: Governaça do agente de contexto

## Status
Aceita

## Decisão
- Um único agente principal executável: `.github/agents/main.agent.md`.
- `archive` é histórico imutável.
- Contexto profundo (fontes e tópicos) ativo em `.github/context/current/sources/`.

## Motivo
Evitar divergência de leitura e decisões contraditórias.

