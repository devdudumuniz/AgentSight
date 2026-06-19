# Card de fonte: advanced_screenshot_agent

- titulo: Código runtime do AgentSight
- tipo: Código
- localizacao: `advanced_screenshot_agent/`
- resumo executivo: Implementa CLI, captura, policy gate, redaction regional em memoria, redaction textual auxiliar, criptografia auxiliar, evidencias e adapter Playwright minimo.
- conceitos-chave: consentimento, fullscreen bloqueado, metadata JSON, sha256, redaction regional, EvidenceRun.
- pontos críticos: `capture.py` pode marcar backend `placeholder` em ambiente sem display; isso precisa ser tratado como evidencia de ambiente, nao captura real.
- riscos: redaction depende de regioes explicitas; captura por janela sem regiao ainda nao esta implementada.
- relacao com o projeto: fonte primaria para qualquer afirmacao funcional.
- modulos afetados: capture, policy, redaction, evidence, cli.
- limitacoes da fonte: cobertura de adapters e retention ainda incompleta.
- como o agente deve usar esta fonte: sempre preferir leitura do codigo a suposicoes de roadmap.
