# TASK-0023-V6-VALIDATION-001 — Validação Integrada do Baseline V6

**ID:** TASK-0023-V6-VALIDATION-001  
**Data:** 2026-06-27  
**Emitido por:** Conselho / PSA + AIC (validação conjunta)  
**Referência:** ADR-012 · DEC-GATE-MIG1 · DEC-GATE-MIG2 · DEC-GATE-MIG3  
**Estado:** 🟡 EM VALIDAÇÃO (pré-MIG-4 gate)

---

## 1. Objetivo

Validar o funcionamento integrado do baseline V6 composto por:

- MIG-1 — Indicator Engine
- MIG-2 — Market Data Engine
- MIG-3 — Position Manager

Este teste não introduz novo código e não altera arquitetura.

Apenas verifica se os módulos já aprovados operam como **pipeline coerente e determinístico**.

---

## 2. Escopo da Validação

### Fluxo obrigatório de integração

```
[MIG-2] Market Data
      ↓
[MIG-1] Indicator Engine
      ↓
[MIG-3] Position Manager
```

---

## 3. Critérios de Validação (CA-V6-01 → CA-V6-06)

### CA-V6-01 — Consistência de dados

- MIG-2 fornece OHLCV válido
- Nenhum NaN ou fallback sintético

### CA-V6-02 — Determinismo MIG-1

- Indicadores idênticos para input idêntico
- Sem variação entre execuções

### CA-V6-03 — Integração MIG-3

- PositionManager aceita eventos sem erro
- Ledger consistente após múltiplos ciclos

### CA-V6-04 — Fluxo end-to-end

- snapshot → indicator → position update funciona sem quebra

### CA-V6-05 — Isolamento de execução

- Nenhum `order_send()` presente
- Nenhuma dependência MIG-6 ativada

### CA-V6-06 — Reprodutibilidade

- Execuções repetidas produzem o mesmo estado final

---

## 4. Regras de Governança

- ❌ Nenhuma criação de MIG-4 neste teste
- ❌ Nenhuma execução real de mercado
- ❌ Nenhum order execution permitido
- ❌ Nenhuma alteração de código estrutural

---

## 5. Resultado Esperado

| Item | Resultado esperado |
|------|--------------------|
| MIG-1 + MIG-2 | Input consistente |
| MIG-3 | Estado determinístico |
| Pipeline | Sem quebra de fluxo |
| Repetição | Estado idêntico em múltiplas execuções |

---

## 6. Saídas esperadas da validação

- V6_VALIDATION_REPORT.md
- Snapshot de execução determinística
- Confirmação de “READY FOR MIG-4”

---

## 7. Critério de aprovação

O baseline V6 será considerado **VALIDADO** se:

- CA-V6-01 a CA-V6-06 = PASS
- Nenhuma divergência entre módulos
- Estado final reprodutível

---

## 8. Resultado institucional

- MIG-1 → VALIDADO
- MIG-2 → VALIDADO
- MIG-3 → VALIDADO
- V6 BASELINE → 🔄 EM VALIDAÇÃO

---

## 9. Próximo passo (condicional)

Se aprovado:

> Autorizar abertura de DEC-MIG4-001 — Risk Engine Charter

Se reprovado:

> Corrigir apenas camada de integração (sem alterar módulos internos)

---

**FIM DO DOCUMENTO**
