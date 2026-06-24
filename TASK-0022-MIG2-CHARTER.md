# TASK-0022 — MIG-2 CHARTER: Market Data Engine

**ID:** TASK-0022  
**Data:** 2026-06-24  
**Emitido por:** PSA  
**Autorização:** DEC-20 · DEC-21 · Conselho  
**Status:** 🟡 EM ELABORAÇÃO — somente planejamento  
**Referências:** ADR-012 · GATE-MIG1 (fechado) · SIVR-1-DESIGN-001 (referência futura)

---

## 1. Declaração do Problema

**Bug canônico:** BUG-002  
**Categoria:** Market Data Engine  
**Risco:** Pipeline V6 consome dados sem validação de integridade, origem ou frescor — qualquer dado sintético, viciado ou desatualizado pode contaminar decisões de indicadores e sinais.

---

## 2. Escopo da MIG-2

### 2.1 O que MIG-2 entrega

| Componente | Responsabilidade |
|------------|-----------------|
| `market_data/data_provider.py` | Interface canônica de fornecimento de dados OHLCV |
| `market_data/integrity_validator.py` | Validação: frescor, completude, sequência temporal |
| `market_data/data_contract.py` | Tipos: `OHLCVBar`, `MarketDataFeed`, `DataIntegrityError` |
| `tests/test_market_data.py` | CI: integridade, rejeição de dados sintéticos, frescor |

### 2.2 O que MIG-2 NÃO inclui

- ❌ Order management / execution (pertence a MIG-3+)
- ❌ Position tracking (MIG-3)
- ❌ Risk engine (MIG-4)
- ❌ Qualquer lógica de trading ou sinal

---

## 3. Critérios de Aceite (CA)

| ID | Critério | Verificação |
|----|----------|-------------|
| CA-01 | Zero dados sintéticos ou artificiais aceitos em modo demo/exec | CI + inspeção |
| CA-02 | Dados com `timestamp` desatualizado (> threshold) rejeitados com `DataIntegrityError` | pytest |
| CA-03 | Gaps de sequência temporal detectados e reportados | pytest |
| CA-04 | `OHLCVBar` é imutável e tipado (frozen dataclass) | mypy + pytest |
| CA-05 | `DataProvider` é um Protocol — sem acoplamento a MT5 direto | mypy |
| CA-06 | CI verde: ruff + mypy strict + pytest 100% | GitHub Actions |

---

## 4. Dependências do MIG-2

### 4.1 Dependências de entrada (já existentes)

| Componente | Origem | Status |
|------------|--------|--------|
| `contracts/indicator_contract.py` | MIG-1 | ✅ Disponível |
| `indicator_engine/` | MIG-1 | ✅ Disponível |
| `sivr/data_adapter_mt5.py` | SIVR-0 | ✅ Disponível (referência, não dependência direta) |

### 4.2 Dependências para SIVR-1 (contextual — per DEC-21)

O SIVR-1-DESIGN-001 requer os seguintes componentes que dependem de MIG-2:

| Componente SIVR-1 | Depende de MIG-2 | Depende de |
|-------------------|-----------------|------------|
| `execution/order_engine.py` | ✅ Sim | + MIG-3 Charter |
| `state/reconciliation_engine.py` | ✅ Sim | + MIG-4 Charter |
| `sivr/failure_injector.py` | ✅ Sim | + MIG-3 + MIG-4 |

> **Nota PSA:** estas dependências são registradas aqui per instrução do Conselho (DEC-21 §5) como insumo para os charters futuros.

---

## 5. Proibições Absolutas (MIG-2)

- ❌ Fallback sintético: se dados reais indisponíveis, `DataIntegrityError` — nunca dados gerados
- ❌ Dados sem timestamp válido aceitos silenciosamente
- ❌ Qualquer lógica de sinal, ordem ou posição neste módulo
- ❌ Import de módulos de execution layer

---

## 6. Entregáveis Esperados (AIC)

| Artefato | Descrição |
|----------|-----------|
| `market_data/__init__.py` | Exports canônicos do módulo |
| `market_data/data_contract.py` | `OHLCVBar`, `MarketDataFeed`, `DataIntegrityError` |
| `market_data/data_provider.py` | Protocol `DataProvider` + implementação MT5 |
| `market_data/integrity_validator.py` | Validação frescor, gaps, completude |
| `tests/test_market_data.py` | Testes CA-01 a CA-06 |

---

## 7. Gate de Saída (GATE-MIG2)

GATE-MIG2 será considerado elegível para fechamento quando:

1. Todos os CA-01 a CA-06 verificados por PSA
2. CI verde (ruff + mypy strict + pytest)
3. AIC entrega SYNC-OUT com evidência de execução
4. PSA valida e emite resultado
5. CFO/Conselho delibera PASS/FAIL

---

## 8. Sequência pós-MIG-2 (contextual)

```
GATE-MIG1 ✅ FECHADO
    ↓
TASK-0022 MIG-2 Charter (este documento)
    ↓
MIG-2 Implementação + SIVR-MIG2
    ↓
GATE-MIG2
    ↓
TASK-0023 MIG-3 Charter (Position Manager)
    ↓
... (MIG-4, MIG-5, MIG-6)
    ↓
SIVR-1 (todos os charters e gates necessários concluídos)
```

---

**PSA — 2026-06-24**  
**TASK-0022 em elaboração. Aguarda revisão AIC e aprovação CFO/Conselho para implementação.**
