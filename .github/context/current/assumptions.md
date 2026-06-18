# Assunções operacionais

- Projeto de pacote Python único (single package), não monorepo.
- Sem dependência de serviços externos obrigatórios (DB, cache, fila) no escopo atual.
- Sem banco próprio, sem deploy infra dedicado neste repositório.
- `.github/context/current/` é fonte canônica ativa.
- Arquivos em `.github/context/archive/` não são editados por rotina operacional.

