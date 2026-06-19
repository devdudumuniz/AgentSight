# Instrucoes de carregamento de contexto

## Ordem obrigatoria

1. `.github/context/manifest.json`
2. `.github/context/current/project-brief.md`
3. `.github/context/current/project-state.md`
4. `.github/context/current/active-scope.md`
5. `.github/context/current/architecture-map.md`
6. `.github/context/current/module-index.md`
7. `.github/context/current/entrypoints.md`
8. `.github/context/current/known-risks.md`

## Sob demanda

- Dominios, modulos, perfis e runbooks devem ser lidos somente quando a tarefa exigir.
- Roadmap, gates e reports devem orientar priorizacao e conclusao.
- Sources devem ser usadas para respostas profundas ou decisoes baseadas em evidencia.

## Regra

`archive/snapshots` e historico. Nunca usar como estado atual sem comparar com `context/current`.
