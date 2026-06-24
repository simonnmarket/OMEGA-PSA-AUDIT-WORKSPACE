# SIVR-0 — PSA CHECKLIST DE ACEITAÇÃO

**ID:** SIVR-0-CHECKLIST-PSA  
**Data:** 2026-06-24  
**Emitido por:** PSA  
**Destinatário:** AIC · CFO · Conselho  
**Autoridade:** CEO-DECISÃO-SIVR-20260624  
**Status:** EMITIDO

---

## Pergunta PSA

> "O sistema está corretamente especificado para ser testado?"

**Resposta:** ✅ SIM — com as restrições abaixo.

---

## Escopo Autorizado SIVR-0

```
OHLCV (arquivo local, dataset fixo)
        ↓
SIVR Bridge (mínimo — sem MT5, sem broker)
        ↓
Indicator Engine (MIG-1)
        ↓
Output estruturado: { timestamp, rsi, ema }
        ↓
Logs determinísticos por ciclo
```

## Bloqueios explícitos

- ❌ MT5 ou qualquer conexão broker
- ❌ BUY/SELL/ordens de qualquer tipo
- ❌ Estratégia ou lógica de decisão
- ❌ Risk Engine
- ❌ Dados sintéticos gerados em runtime (apenas dataset fixo)
- ❌ Dependência de V5.5 ou qualquer arquivo legacy

---

## Critérios de Aceitação PSA (C1–C6)

| ID | Critério | Verificável por | Pass condition |
|----|----------|-----------------|----------------|
| C1 | Execução contínua sem erro | AIC log | Zero exceptions em 100+ ciclos |
| C2 | Determinismo | PSA audit | Mesmo dataset → mesmo RSI/EMA em toda execução |
| C3 | Integridade MIG-1 | AIC log | Zero `None`, zero `NaN`, zero silent crash |
| C4 | Independência do legacy | PSA scope check | `git diff --stat` zero fora de escopo SIVR |
| C5 | Observabilidade | AIC log | Log JSON por ciclo com timestamp + rsi + ema |
| C6 | Fluxo completo | AIC log | Nenhum ciclo interrompido antes do output |

---

## Output mínimo exigido por ciclo

```json
{
  "cycle": 1,
  "timestamp": "2026-06-24T21:00:00",
  "rsi": 60.14,
  "ema": 45.87
}
```

---

## Artefatos que o AIC deve entregar ao PSA

| # | Artefato | Formato |
|---|----------|---------|
| EV-SIVR-01 | Log completo da execução (100+ ciclos) | JSON |
| EV-SIVR-02 | Dataset OHLCV usado (hash SHA256) | txt |
| EV-SIVR-03 | Evidência de determinismo (2 runs, diff = 0) | diff output |
| EV-SIVR-04 | Confirmação zero legacy (grep) | txt |
| EV-SIVR-05 | Summary: ciclos executados, falhas, duração | txt |

---

**PSA (Cascade) — 2026-06-24**
