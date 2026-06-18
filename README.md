# Advanced Screenshot Agent

Ferramenta base para dar visão operacional a agentes de IA com captura seletiva de tela, anotação semântica, redaction local, retenção controlada e trilha auditável.

## Objetivo

Criar uma camada open source para agentes como Codex, Claude Code, Cursor, Copilot, Zuza ou agentes internos conseguirem:

- Capturar tela, janela, região ou elemento web.
- Gerar metadados estruturados da interface.
- Aplicar redaction de dados sensíveis antes de persistir ou enviar contexto.
- Produzir evidências visuais para QA, PR review, documentação e agentes autônomos.
- Evitar o antipadrão “captura tudo, guarda tudo, depois vemos a LGPD chorando no canto”.

## Diferencial técnico

As soluções atuais normalmente fazem apenas screenshot + análise visual. Este projeto nasce com quatro camadas adicionais:

1. **Capture Firewall**: política declarativa de escopo permitido.
2. **Vision Evidence Graph**: grafo de evidências com origem, ação, coordenadas, hashes e cadeia temporal.
3. **Local-first redaction**: mascaramento antes de salvar ou compartilhar.
4. **Agent-safe protocol**: saída JSON estável para LLMs, sem depender de scraping visual improvisado.

## Estrutura

```text
.
├── advanced_screenshot_agent/
│   ├── __init__.py
│   ├── capture.py
│   ├── annotate.py
│   ├── redact.py
│   ├── crypto.py
│   ├── evidence.py
│   ├── policy.py
│   ├── cli.py
│   └── adapters/
│       ├── __init__.py
│       └── playwright.py
├── docs/
│   ├── architecture.md
│   ├── research-notes.md
│   ├── privacy-threat-model.md
│   ├── roadmap.md
│   └── codex-continuation-prompt.md
├── skills/
│   └── advanced-screenshot-agent.skill.md
├── tests/
│   ├── test_policy.py
│   ├── test_redact.py
│   └── test_evidence.py
├── pyproject.toml
└── .github/workflows/ci.yml
```

## Uso local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

screenshot-agent capture --label home-screen --output .vision-runs/demo
screenshot-agent report --run .vision-runs/demo
```

No Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
screenshot-agent capture --label home-screen --output .vision-runs/demo
```

## Status

Base inicial para continuação pelo Codex. Ainda não é release.
