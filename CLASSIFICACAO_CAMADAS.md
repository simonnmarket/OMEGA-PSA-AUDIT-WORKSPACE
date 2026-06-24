# CLASSIFICAÇÃO DE CAMADAS SOBERANAS — OMEGA Kernel Sovereign V6

**Documento:** CLASSIFICACAO_CAMADAS.md  
**Versão:** 1.0  
**Data:** 2026-06-23  
**Decisão de origem:** DEC-GOV-02 · DEC-CFO-20260623-T18  
**Autoridade:** CFO — OMEGA Kernel Sovereign V6  

---

## Princípio Fundamental

> **Estratégia ≠ Execução. Indicadores ≠ Ordem. Sinal ≠ Trade.**

Cada camada tem **responsabilidade exclusiva**. Nenhuma camada pode invocar responsabilidade de outra camada sem passar pelo contrato formal definido em `contracts/`.

---

## As 6 Camadas Soberanas

### CAMADA 1 — Dados
**MIG associado:** MIG-2 (MT5 Connector)  
**Responsabilidade:** Adquirir dados de mercado reais do broker.  
**Proibições:**
- Fallback sintético (FND-06 — proibido por ADR-003)
- Dado fabricado em qualquer condição de erro

**Comportamento em falha:** Retornar HOLD. Nunca inventar preço.

---

### CAMADA 2 — Indicadores
**MIG associado:** MIG-1 (EMA / Indicator Engine)  
**Responsabilidade:** Calcular indicadores técnicos com chaves padronizadas.  
**Proibições:**
- Key mismatch (FND-11 — rsi vs rsi_14 — proibido por ADR-006)
- Filtros hardcoded sem avaliação (FND-10 — 8 PASS — proibido por ADR-004)

**Saída obrigatória:** dict com chaves canônicas (`rsi_14`, `ema_fast`, `ema_slow`, …)

---

### CAMADA 3 — Estratégia
**MIG associado:** (sem MIG próprio — componente nativo V6)  
**Responsabilidade:** Gerar sinal de direção (BUY / SELL / HOLD) com metadados completos.  
**Proibições:**
- Emitir SL/TP fixos hardcoded
- Acessar broker diretamente

**Saída obrigatória:** `Signal(direction, sl, tp, confidence, timestamp, strategy_id)`

---

### CAMADA 4 — Risco
**MIG associado:** MIG-4 (Risk Manager Adaptive)  
**Responsabilidade:** Calcular parâmetros de risco derivados exclusivamente do sinal.  
**Proibições:**
- SL/TP fixos (FND-04 — proibido por ADR-007)
- Overrides sem aprovação explícita

**Saída obrigatória:** `RiskParams(sl, tp, lot_size, max_exposure)` derivados de `Signal`

---

### CAMADA 5 — Validação de Sinal
**MIG associado:** MIG-5 (Signal Validation Layer) — *redefinido 2026-06-23*  
**Responsabilidade:** Validar sinal, consistência, integridade e contratos antes da execução.  
**Proibições:**
- Enviar ordens (qualquer comunicação com broker)
- Modificar sinal (apenas aceita ou rejeita)

**Saída obrigatória:** `ValidationResult(valid: bool, reason: str)`

---

### CAMADA 6 — Execução
**MIG associado:** MIG-6 (Execution Engine Sovereign) — *criado 2026-06-23*  
**Responsabilidade:** Executar ordens no broker. Única camada autorizada a comunicar com MetaTrader 5 para envio de ordens.  
**Proibições:**
- Lógica de estratégia
- Validação de sinal (responsabilidade da Camada 5)
- Execução sem `OMEGA_ENV` declarado
- Cruzamento DEMO↔REAL

**Componentes internos:** Order Manager · Broker Connector · Trade Mode Validation · Environment Gating · Execution Pipeline

---

## Diagrama de Fluxo Soberano

```
[Broker / MT5]
      │ dados reais
      ▼
CAMADA 1 — Dados
      │ market_data (real ou HOLD)
      ▼
CAMADA 2 — Indicadores
      │ dict{rsi_14, ema_fast, ema_slow, …}
      ▼
CAMADA 3 — Estratégia
      │ Signal(direction, sl, tp, confidence, …)
      ▼
CAMADA 4 — Risco
      │ RiskParams(sl, tp, lot_size, …)
      ▼
CAMADA 5 — Validação de Sinal
      │ ValidationResult(valid=True) → prossegue
      │ ValidationResult(valid=False) → HOLD, log, para aqui
      ▼
CAMADA 6 — Execução
      │ execute(validated_signal, risk_params)
      ▼
[Broker / MT5] — ordem enviada
```

---

## Violações Históricas (V5.5)

| Violação | Camada afetada | Finding | ADR |
|----------|---------------|---------|-----|
| SL/TP fixos 200/400 pts | Risco (C4) | FND-04 | ADR-007 |
| _get_sample_data() fallback | Dados (C1) | FND-06 | ADR-003 |
| RSI key mismatch rsi→rsi_14 | Indicadores (C2) | FND-11 | ADR-006 |
| 8 filtros PASS hardcoded | Indicadores (C2) | FND-10 | ADR-004 |
| Motor legacy/soberano concorrentes | Execução (C6) | FND-01 | ADR-002 |
| env var override sem gating | Validação (C5) | FND-08 | ADR-005 |

---

*Documento permanente — não alterar sem aprovação formal do Conselho.*  
*Emitido por: CFO — OMEGA Kernel Sovereign V6 — 2026-06-23*
