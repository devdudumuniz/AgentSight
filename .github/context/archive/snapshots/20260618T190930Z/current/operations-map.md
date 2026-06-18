# Mapa operacional

## Rotina de desenvolvimento
1. Ler contexto atual (`.github/context/current/*`).
2. Executar alteração pontual no alvo.
3. Rodar validações (ruff/pytest quando alterado código ou dependência).
4. Atualizar documentação/contexto necessário.

## Operações críticas já existentes
- Empacotamento em `pyproject.toml`.
- Execução de testes via `pytest`.
- Verificação de estilo via `ruff`.

## Gaps conhecidos
- Ausência de script de release/documentação de deploy no repositório.
- A camada de release ainda é manual; não há pipeline de publicação automatizada.
