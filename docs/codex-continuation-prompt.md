```text
Você está continuando o desenvolvimento do projeto agentsight.

Objetivo:
Transformar a base inicial em uma ferramenta open source de alto nível para dar visão segura a agentes de IA, superando fluxos simples de screenshot usados por Codex, Claude Code, Cursor e similares.

Regras obrigatórias:
- Não remover policy gate.
- Não permitir fullscreen por padrão.
- Não enviar imagem bruta para LLM antes de redaction quando redaction estiver ativado.
- Não criar mock enganoso como se fosse captura real.
- Não aceitar teste fake.
- Não expor secrets, endpoints privados ou dados do ambiente.
- Comentários complexos devem ser em português Brasil, com tom leve quando fizer sentido.
- Toda mudança precisa ter teste, documentação e validação local.

Prioridades técnicas:
1. Implementar adapter Playwright completo:
   - screenshot full page
   - screenshot por locator
   - before/after hooks
   - export JSON por fluxo
2. Implementar redaction local:
   - OCR opcional
   - regex sensível
   - blur por região
   - relatório de hits sem vazar valor integral
3. Implementar retention cleanup:
   - apagar capturas vencidas
   - preservar manifest de auditoria sem imagem
4. Melhorar CLI:
   - capture
   - annotate
   - redact
   - report
   - cleanup
5. Criar exemplos:
   - exemplo web com Playwright
   - exemplo desktop básico
   - skill para Claude/Codex
6. Criar GitHub Actions honesto:
   - ruff
   - pytest
   - build package

Validação mínima antes de finalizar:
- python -m pip install -e ".[dev]"
- ruff check .
- pytest
- python -m agentsight.cli --help
- agentsight --help

Entrega esperada:
- Código funcional.
- README atualizado.
- Docs com arquitetura e threat model.
- Issues abertas para fases futuras.
- Nenhum segredo no diff.

Direção de produto:
O diferencial não é tirar print. Qualquer gambiarra tira print.
O diferencial é criar um Vision Runtime governado, auditável, redigido, local-first e pronto para empresas.
```
