# Advanced Screenshot Agent Skill

Use esta skill em tarefas de:
- inspeção visual de interface,
- validação de fluxo por evidência visual,
- documentação operacional de bugs visuais.

## Regras obrigatórias
- `--fullscreen` apenas com justificativa explícita no task.
- Preferir captura de região/elemento.
- Aplicar redaction antes de persistência/compartilhamento quando houver potencial de dado sensível.
- Emitir relatório objetivo com metadados (imagem/hash/horário).

## Procedimento

1. Identificar fluxo de mudança e risco de PII.
2. Executar ação (quando aplicável).
3. Capturar antes e depois.
4. Comparar metadados em JSON + evidência redigida.
5. Registrar decisões em:
   - `.github/context/current/assumptions.md`
   - `.github/context/current/runbooks/troubleshooting.md`

## Dependências de contexto
- `.github/context/current/sources/topics/security.md`
- `.github/context/current/domains/security.md`
- `.github/context/current/modules/capture.md`

## Comandos úteis

```powershell
screenshot-agent capture --label estado-inicial --output .vision-runs/current --consent
screenshot-agent capture --label estado-final --output .vision-runs/current --consent
screenshot-agent report --run .vision-runs/current
```

## Critério de aprovação

A evidência só deve ser tratada como válida quando:
- a captura mostra a tela correta,
- não há dados sensíveis sem redaction,
- o relatório cita o fluxo testado,
- o JSON de evidência contém hash e timestamp.
