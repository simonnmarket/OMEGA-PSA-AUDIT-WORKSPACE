# MIGRATION_ALLOWLIST.md

**Projeto:** OMEGA Kernel Sovereign V6  
**Versão:** 3.0 — Modelo Oficial 6 MIGs  
**Data:** 2026-06-23  
**Autoridade:** CFO-RAT-20260623-03 · ADR-012 · DEC-15  
**Status:** APROVADO PARA EXECUÇÃO

---

## PRINCÍPIO

Esta allowlist é o **único documento** que autoriza execução de MIGs.  
Nenhum MIG pode ser iniciado sem:
1. Gate anterior fechado
2. ADR correspondente aprovado pelo Conselho
3. ID rastreável registrado no DECISION_REGISTRY

---

## MODELO OFICIAL: 6 MIGs

### MIG-1 — Indicator Engine
**Gate de entrada:** GATE-0 GOVERNANÇA FECHADO  
**Gate de saída:** GATE-MIG1  
**Bugs associados:** BUG-001 · BUG-003  
**Escopo autorizado:**
- Padronização das chaves canônicas de indicadores (`rsi_14`, `ema_fast`, `ema_slow`)
- Eliminação de indicadores `None`
- Remoção dos 8 filtros PASS hardcoded (ADR-004)
- Correção do key mismatch RSI (ADR-006)
**Proibido neste MIG:** qualquer alteração fora de `indicator_engine/`  
**Critério de aceite:** Nenhum `None` · Chaves canônicas · CI verde  
**Status:** ✅ GATE-MIG1 FECHADO (DEC-GATE-MIG1 · 2026-06-24)

---

### MIG-2 — Market Data Engine
**Gate de entrada:** GATE-MIG1 FECHADO  
**Gate de saída:** GATE-MIG2  
**Bug associado:** BUG-002  
**Proibição absoluta:** fallback sintético · dados artificiais · mock de mercado  
**Escopo autorizado:**
- `contracts/market_data_contract.py` — OHLCVBar, MarketDataSnapshot, DataProvider, MarketDataEngine
- `market_data/` — SovereignMarketDataEngine, DataValidator, MockDataProvider, MT5DataProvider
- `tests/test_market_data.py` — CA-01 a CA-08
**Critério de aceite:** Dados reais · Integridade confirmada · CI verde · CA-01..CA-08  
**Status:** ✅ GATE-MIG2 FECHADO (DEC-GATE-MIG2 · 2026-06-25)

---

### MIG-3 — Position Manager
**Gate de entrada:** GATE-MIG2 FECHADO  
**Gate de saída:** GATE-MIG3  
**Bugs associados:** — (sem bug canônico obrigatório)  
**Proibição absoluta:** `order_send()` · Execution Engine · Risk Engine · Reconciliation Engine · SIVR-1  
**Escopo autorizado:**
- `contracts/position_contract.py` — PositionTicket, PositionSnapshot, ExposureSummary, PositionEvent, PositionManager Protocol
- `position_manager/` — SovereignPositionManager, PositionLedger, PositionValidator, ExposureCalculator
- `position_manager/sync/` — MockBrokerSync (CI), Mt5PositionSync (read-only)
- `tests/test_position_manager.py` — CA-01 a CA-08
**Critério de aceite:** CA-01..CA-08 · Zero `order_send` · Fail-closed · Integração MIG-2 · CI verde  
**Status:** ✅ GATE-MIG3 FECHADO (DEC-GATE-MIG3-001 · 2026-06-27)

---

### MIG-4 — Risk Engine
**Gate de entrada:** GATE-MIG3 FECHADO  
**Gate de saída:** GATE-MIG4  
**Bug associado:** BUG-006  
**Escopo autorizado:**
- SL derivado exclusivamente do sinal
- TP derivado exclusivamente do sinal
- Eliminação de parâmetros fixos desconectados do sinal
**Critério de aceite:** SL/TP do sinal · Zero fixos desconectados · CI verde

---

### MIG-5 — Signal Validation Layer
**Gate de entrada:** GATE-MIG4 FECHADO  
**Gate de saída:** GATE-MIG5  
**Escopo:** Arquitetural (sem bug canônico isolado)  
**Escopo autorizado:**
- Separação formal entre camada de decisão e camada de execução
- Validação de sinais antes de chegar à execução
- Telemetria completa da camada de validação
**Critério de aceite:** Sinais validados · Camadas desacopladas · Telemetria · CI verde

---

### MIG-6 — Execution Engine Sovereign
**Gate de entrada:** GATE-MIG5 FECHADO  
**Gate de saída:** GATE-MIG6  
**Bugs associados:** BUG-004 · BUG-009 · BUG-010  
**Componentes:** Order Manager · Trade Mode Validation · Broker Connector · Environment Gating  
**Escopo autorizado:**
- Caminho único e soberano de execução de ordens
- Controle de ambiente (DEMO e REAL estritamente segregados)
- Validação de modo de trade antes de qualquer envio
**Critério de aceite:** Caminho único · DEMO/REAL segregados · CI verde

---

## BUGS — NÃO MIGRAR

| ID | Razão | Classificação |
|----|-------|---------------|
| BUG-005 | Evidência de falha histórica — preservada para referência | EVIDÊNCIA FORENSE |
| BUG-007 | Evidência de falha histórica — preservada para referência | EVIDÊNCIA FORENSE |
| BUG-008 | Evidência de falha histórica — preservada para referência | EVIDÊNCIA FORENSE |

**Nota forense:** Os IDs históricos FND/RT (nomenclatura anterior) podem permanecer somente como nota em rodapé de ADRs — nunca como referência primária.

---

## MAPEAMENTO CANÔNICO BUG ↔ MIG

| Bug ID | Título Canônico | MIG | Gate |
|--------|----------------|-----|------|
| BUG-001 | Indicadores None | MIG-1 | GATE-MIG1 |
| BUG-002 | Dados sintéticos / mercado falso | MIG-2 | GATE-MIG2 |
| BUG-003 | 8 Filtros PASS Hardcoded (remoção MIG-1, substituição MIG-5) | MIG-1 + MIG-5 | GATE-MIG1 / GATE-MIG5 |
| BUG-004 | Múltiplos launchers / runtimes | MIG-6 | GATE-MIG6 |
| BUG-005 | — | NÃO MIGRAR | FORENSE |
| BUG-006 | Key mismatch RSI / Risk Engine | MIG-4 | GATE-MIG4 |
| BUG-007 | — | NÃO MIGRAR | FORENSE |
| BUG-008 | — | NÃO MIGRAR | FORENSE |
| BUG-009 | Broker Connector instável | MIG-6 | GATE-MIG6 |
| BUG-010 | Environment Gating ausente | MIG-6 | GATE-MIG6 |

---

## REGRA DE ESCOPO — ETAPA 0

Durante a ETAPA 0 (GATE-0 GOVERNANÇA), é expressamente proibida qualquer alteração nos seguintes diretórios:

- runtime/ — PROIBIDO
- strategy/ — PROIBIDO
- execution/ — PROIBIDO
- deployment/ — PROIBIDO
- telemetry/ — PROIBIDO
- contracts/ — PROIBIDO
- tests/ — PROIBIDO

Escopo autorizado exclusivo: `governance/`

---

## SEQUÊNCIA DE GATES

```
GATE-0 GOVERNANÇA (✅ FECHADO — DEC-18)
  ↓
GATE-MIG1 (✅ FECHADO ARQUITETURAL — DEC-GATE-MIG1 · 2026-06-24)
  ↓
GATE-MIG2 (✅ FECHADO ARQUITETURAL — DEC-GATE-MIG2 · 2026-06-25)
  ↓
GATE-MIG3 (✅ FECHADO ARQUITETURAL — DEC-GATE-MIG3-001 · 2026-06-27)
  ↓
ETAPA 3.5 — INVENTÁRIO E MATRIZ DE PARIDADE FUNCIONAL (🟡 EM ANDAMENTO — COUNCIL-DIRECTIVE-025)
  ↓
GATE-MIG4 (⏸️ SUSPENSO — COUNCIL-DIRECTIVE-025)
  ↓
GATE-MIG5 (⏸️ SUSPENSO — COUNCIL-DIRECTIVE-025)
  ↓
GATE-MIG6 (⏸️ SUSPENSO — COUNCIL-DIRECTIVE-025)
  ↓
GATE-DEMO (5 dias úteis)
  ↓
GATE-SHADOW (10 dias úteis)
  ↓
GATE-REAL (ADR específico obrigatório)
  ↓
EXECUÇÃO REAL CONTROLADA
```

**Nota:** A partir de COUNCIL-DIRECTIVE-025, cada Gate-MIG possui dupla dimensão:
- **Gate Arquitetural:** valida estrutura, contratos, CI, determinismo.
- **Gate Funcional:** valida paridade de comportamento com OMEGA_OS_Kernel.

---

*Última atualização: 2026-06-27*  
*Autoridade: OMEGA-CONSTITUTION-001 · COUNCIL-DIRECTIVE-025 · DEC-RESET-001 · CFO-RAT-20260623-03 · ADR-012 · DEC-15 · DEC-18 · DEC-MIG2-001 · DEC-GATE-MIG2 · DEC-MIG3-001 · DEC-GATE-MIG3-001*  
*Revisão: MIG-1/MIG-2/MIG-3 reclassificados como Gates Arquiteturais; ETAPA 3.5 inserida; MIG-4/5/6 suspensos; Constituição vigente*
