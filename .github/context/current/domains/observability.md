# Dominio: observabilidade

## Estado atual

O projeto nao possui backend persistente nem servico HTTP. A observabilidade atual e baseada em metadata de captura, hashes, timestamps e relatorios Markdown.

## Fatos confirmados

- `capture.py` grava metadata JSON por captura.
- `evidence.py` representa eventos com `event_id`, `sha256`, `timestamp_utc` e `action`.
- `report` gera saida Markdown a partir dos JSONs de uma run.

## Lacunas

- Nao ha logs estruturados padronizados.
- Nao ha correlation-id por run alem de `EvidenceRun.run_id`.
- Nao ha metricas de CLI, taxa de redaction ou falhas de captura.

## Proxima evolucao segura

Padronizar `run_id`, `event_id`, `capture_backend`, `policy_id` e resultado de redaction em todos os outputs JSON.
