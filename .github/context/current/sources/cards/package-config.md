# Card de fonte: pyproject.toml

- titulo: Configuração do pacote Python
- tipo: Código/config
- localizacao: `pyproject.toml`
- resumo executivo: Define build backend, metadados do pacote, dependencias, extras de desenvolvimento, entrypoint `agentsight`, ruff e pytest.
- conceitos-chave: setuptools, pacote editavel, CLI entrypoint, pytest, ruff, mypy.
- pontos críticos: `requires-python >=3.10`; `agentsight = agentsight.cli:main`.
- riscos: mypy esta em `dev`, mas ainda nao e gate obrigatorio no CI.
- relacao com o projeto: fonte primaria para instalar, testar e empacotar o AgentSight.
- modulos afetados: package, CLI, QA.
- limitacoes da fonte: nao descreve comportamento de produto.
- como o agente deve usar esta fonte: validar comandos de build/test/lint e entrypoints antes de sugerir scripts novos.
