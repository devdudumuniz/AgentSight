# Advanced Screenshot Agent Skill

Use esta skill quando precisar verificar visualmente uma interface, capturar evidência de bug, gerar documentação visual ou validar UI após alteração de código.

## Regras de segurança

- Não capture tela inteira sem autorização explícita.
- Prefira janela, região ou elemento.
- Não capture telas com senhas, tokens, banco, dados pessoais ou documentos sensíveis.
- Use redaction quando houver qualquer chance de dados sensíveis.
- Gere relatório Markdown apenas com imagens redigidas.

## Fluxo recomendado

1. Rodar a aplicação ou teste relevante.
2. Capturar estado inicial.
3. Executar a ação.
4. Capturar estado final.
5. Gerar relatório.
6. Avaliar layout, texto, sobreposição, estados vazios, loaders e erros.

## Comandos

```bash
screenshot-agent capture --label estado-inicial --output .vision-runs/current --consent
screenshot-agent capture --label estado-final --output .vision-runs/current --consent
screenshot-agent report --run .vision-runs/current
```

## Critério de aprovação

A interface só pode ser considerada validada quando:
- A captura mostra a tela correta.
- Não há dados sensíveis sem redaction.
- O relatório cita o fluxo testado.
- A evidência tem metadata JSON com hash e timestamp.
