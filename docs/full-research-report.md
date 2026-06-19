# Full Research Report — AgentSight

## Síntese

O estado atual dos agentes com visão de tela segue um padrão recorrente: capturar screenshot, enviar ao modelo, receber ações de mouse/teclado, executar e repetir. Isso funciona, mas cria riscos enormes quando aplicado em máquinas reais: captura excessiva, persistência de dados sensíveis, prompt injection visual e ausência de trilha auditável.

## Referências estudadas

- Claude Computer Use: screenshot, mouse/keyboard e loop em ambiente isolado.
- OpenAI Computer Use: o modelo olha a UI por screenshot, retorna ações, o harness executa e envia nova screenshot.
- Playwright: screenshot de página, full page, buffer e elemento específico.
- Skills comunitárias: captura antes/depois, relatórios Markdown, anotações visuais.
- Chronicle/Codex e Microsoft Recall: mostram o risco de captura recorrente de tela e memória visual sem controles fortes.

## Direção técnica

O projeto precisa ir além do “print + LLM”. A proposta correta é um Vision Runtime:

1. Capture Firewall
2. Redaction local-first
3. Evidence Graph
4. Agent-safe JSON protocol
5. Human approval gates
6. Retention cleanup
7. CI visual + PR review

## Métricas futuras

- Click accuracy
- Privacy leak rate
- Redaction precision/recall
- Visual regression detection rate
- Token cost per visual task
- Time-to-debug
- False positive rate em prompt injection visual

## Decisão de arquitetura

Python é escolhido para a base inicial por velocidade de adoção e integração com agentes. Rust pode entrar depois para um runtime nativo de captura e segurança em Windows/macOS/Linux.
