# Arquitetura

## Decisão principal

A ferramenta não deve ser “mais um printscreen com IA”. Ela deve ser uma camada de percepção segura para agentes.

## Pipeline

1. **Policy gate**
   - Valida consentimento.
   - Bloqueia fullscreen por padrão.
   - Bloqueia janelas sensíveis por palavras-chave.
   - Futuro: allowlist por processo, domínio e workspace.

2. **Capture engine**
   - Captura tela, região ou elemento.
   - Em navegador, usa adapters Playwright/Selenium.
   - Em desktop, usa backend cross-platform.

3. **Local redaction**
   - Extrai sinais textuais.
   - Detecta padrões sensíveis.
   - Borra regiões em memória antes de persistir a imagem final quando `redaction_regions` é informado.

4. **Evidence graph**
   - Registra imagem, hash, ação, timestamp e política usada.
   - Base para auditoria, replay e PR review.

5. **Agent protocol**
   - Exporta JSON pequeno.
   - Gera relatório Markdown.
   - Evita despejar imagens gigantes no contexto do agente sem necessidade.

## Anti-patterns bloqueados

- Captura de tela inteira por padrão.
- Guardar screenshots sem TTL.
- Enviar imagem bruta para LLM antes de redaction.
- Deixar o agente decidir sozinho o escopo da captura.
- Usar OCR como fonte de verdade sem confidence score.
