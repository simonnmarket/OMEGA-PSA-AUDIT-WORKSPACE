# CFO-DIRECTIVE-20260624-PSA-CHARTER-REVISION-001

**Data:** 2026-06-24  
**Emitido por:** CFO  
**Destinatário:** PSA  
**Referência:** TASK-0021 — MIG-1 Charter + AIC-PARECER-MIG1-001  
**Status:** REVISÃO OBRIGATÓRIA

---

## 1. OBJETIVO

Autorizar e instruir revisão técnica obrigatória do TASK-0021 — MIG-1 CHARTER com base no parecer do AIC-PARECER-MIG1-001.

---

## 2. BASE DA REVISÃO

A revisão deve incorporar integralmente as seguintes observações do AIC:

### 2.1 Dependências ocultas

- D-01: MarketDataSnapshot em contracts/
- D-02: definição de stack numérica (numpy/pure Python)
- D-03: parâmetros EMA/RSI V6
- D-04: definição de telemetry/logging
- D-05: divergência ADR-004/006 vs ADR-010
- D-06: inconsistência DEC-16 vs DEC-18

### 2.2 Divergências documentais críticas

PSA workspace vs V6 canonical:

- BUG-003 → redefinir escopo MIG-1 vs MIG-5
- BUG-006 → alinhar origem causal (não implementação direta)
- BUG-004 → validar launcher separation (MIG-6)
- ETAPA 0 → confirmar status FINAL (não "em progresso")

### 2.3 Critérios de aceite

Revisar obrigatoriamente:

- CA-05 (false positive PASS detection)
- CA-10 (escopo contracts/tests incoerente)

---

## 3. INSTRUÇÃO

O PSA deverá:

1. Atualizar TASK-0021 → MIG-1 CHARTER REV-1
2. Corrigir inconsistências estruturais apontadas
3. Harmonizar PSA ↔ V6 canonical registry
4. Ajustar MIGRATION_ALLOWLIST
5. Revalidar ADR-012 vs DEC-16/18

---

## 4. RESTRIÇÕES

Esta diretiva **NÃO** autoriza:

- implementação de MIG-1
- criação de branch de execução
- alteração em runtime/
- alteração em strategy/
- alteração em execution/
- alteração em deployment/

---

## 5. OBJETIVO FINAL

Gerar versão revisada:

**TASK-0021 — MIG-1 CHARTER REV-1**

compatível com parecer AIC-PARECER-MIG1-001.

---

## 6. STATUS

**MIG-1 IMPLEMENTAÇÃO = BLOQUEADA**

Revisão obrigatória antes de qualquer avanço.

---

**Assinatura:** CFO — OMEGA Kernel Sovereign V6  
**Data:** 2026-06-24
