# ADR-0002: Ordem de leitura do agente principal

## Status
Aceita

## Contexto
Evitar respostas inconsisntentes quando o agente consulta múltiplos níveis de contexto.

## Decisão
Definir ordem de leitura explícita no `main.agent.md`, priorizando:
`manifest` -> `project-brief` -> `architecture-map` -> `module-index` -> `sources`.

## Consequências
- Respostas mais previsíveis.
- Menos inferência não rastreável.
