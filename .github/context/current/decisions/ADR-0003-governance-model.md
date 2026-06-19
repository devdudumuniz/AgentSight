# ADR-0003 - Modelo de governanca operacional

## Status

Aceita em 2026-06-19.

## Contexto

O projeto precisa de memoria ativa, historico versionado, fontes reais e gates para impedir que respostas ou entregas sejam marcadas como concluidas sem evidencia.

## Decisao

Manter `.github/` como base canonica de governanca, separando:

- hot memory em `.github/context/current/`;
- warm memory em dominios, modulos, perfis, runbooks, roadmap, gates e reports;
- cold memory em `.github/context/archive/snapshots/`;
- evidence layer em `.github/context/current/sources/`;
- um unico agente executavel em `.github/agents/main.agent.md`.

## Consequencias

- Toda atualizacao relevante de contexto deve atualizar changelog e relatorios.
- `validate-context` deve falhar quando a estrutura obrigatoria estiver incompleta.
- Snapshots sao historicos e nao substituem `context/current`.
