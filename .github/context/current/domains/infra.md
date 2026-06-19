# Dominio: infra

## Estado atual

Este repositorio e um pacote Python/CLI local-first. Nao ha Dockerfile, compose, banco, Redis, fila ou servico persistente detectado.

## Implicacoes

- Nao criar banco/cache dentro do compose da aplicacao sem requisito real.
- Nao persistir dados operacionais dentro do repositorio.
- Saidas de captura devem permanecer em diretorios de execucao como `.vision-runs/`, fora de commits.

## Gates

- Validar ausencia de artefatos sensiveis antes de commit.
- Manter `.env` real, dumps, screenshots sensiveis e runs locais fora do versionamento.
