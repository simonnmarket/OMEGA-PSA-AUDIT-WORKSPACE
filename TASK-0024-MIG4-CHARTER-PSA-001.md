# TASK-0024 — MIG-4 Risk Engine Charter

**ID:** TASK-0024-MIG4-CHARTER-PSA-001  
**Data:** 2026-06-27  
**Emitido por:** PSA  
**Destinatários:** Conselho · AIC  
**Status:** 🟡 RASCUNHO — aguardando deliberação do Conselho  
**Referências:** ADR-012 · MIGRATION_ALLOWLIST · DEC-GATE-MIG3-001 · CEO-DIRECTIVE-024 · SYNC-VALIDATION-PSA-001

---

## 1. Contexto

Com o **GATE-MIG3 fechado** (DEC-GATE-MIG3-001) e o `SOVEREIGN_TOPOLOGY.md` ratificado, a etapa seguinte do ADR-012 é a **MIG-4 Risk Engine**.

O Risk Engine é o quarto elo do fluxo soberano:

```
dados → indicadores → estratégia → risco → execução → telemetria
```

Ele deve transformar o sinal da estratégia em uma decisão de risco verificável, produzindo parâmetros de proteção (SL/TP) derivados exclusivamente do sinal, e deve consumir o estado de exposição do MIG-3 para evitar risco acumulado.

---

## 2. Objetivo

Implementar o **SovereignRiskEngine** — componente de risco determinístico, testável e isolado, responsável por:

- calcular Stop-Loss (SL) e Take-Profit (TP) a partir do sinal;
- eliminar parâmetros fixos desconectados do sinal (BUG-006);
- avaliar exposição atual via `ExposureSummary` do MIG-3;
- decidir entre autorizar, reduzir ou bloquear uma nova posição;
- nunca executar ordens (escopo reservado ao MIG-6).

---

## 3. Escopo Autorizado

### 3.1 Contratos

- `contracts/risk_contract.py` — `RiskParameters`, `RiskDecision`, `SignalRiskInput`, `RiskEngine` Protocol.

### 3.2 Implementação

- `risk_engine/` — package principal:
  - `SovereignRiskEngine` — orquestrador;
  - `risk_calculator.py` — cálculo de SL/TP a partir do sinal;
  - `exposure_guard.py` — verificação de exposição acumulada;
  - `position_sizer.py` — sizing determinístico (sem alavancagem implícita).

### 3.3 Integração

- Consumo de `ExposureSummary` e `is_flat()` do MIG-3 (`position_manager/exposure.py`).
- Consumo de `MarketDataSnapshot` do MIG-2 para preço de referência.
- Consumo de sinal canônico do MIG-1 (após MIG-5, via interface estável).

### 3.4 Testes

- `tests/test_risk_engine.py` — critérios CA-01 a CA-08.

---

## 4. Proibições Absolutas

- **Parâmetros fixos de SL/TP desconectados do sinal** (BUG-006).
- **`order_send()` ou qualquer chamada de execução** — reservado ao MIG-6.
- **Mock de mercado ou dados sintéticos** como base de decisão de risco.
- **Sizing com alavancagem implícita ou fórmulas opacas**.
- **Reconciliação posicional** — reservada ao SIVR-1.
- **Escrita direta no MIG-3** — Risk Engine consome estado read-only.

---

## 5. Critérios de Aceite (CA-01..CA-08)

| ID | Critério | Evidência |
|----|----------|-----------|
| CA-01 | SL derivado exclusivamente do sinal | Teste unitário: mesmo sinal ⇒ mesmo SL; sinal alterado ⇒ SL alterado |
| CA-02 | TP derivado exclusivamente do sinal | Teste unitário: mesmo sinal ⇒ mesmo TP; sinal alterado ⇒ TP alterado |
| CA-03 | Zero parâmetros fixos desconectados | Inspeção de código + teste de regressão contra BUG-006 |
| CA-04 | Consumo de `ExposureSummary` do MIG-3 | Teste de integração: `is_flat()` e `total_volume` influenciam decisão |
| CA-05 | Decisão de risco determinística | Teste de propriedade: mesmas entradas ⇒ mesma `RiskDecision` |
| CA-06 | Fail-closed | Ausência de sinal ou exposição inválida ⇒ `HOLD` / `REJECT` |
| CA-07 | Sem `order_send` | `grep -R order_send risk_engine/` vazio; CI de governança |
| CA-08 | CI verde | pytest 100% pass; ruff lint zero; nenhuma regressão em MIG-1/2/3 |

---

## 6. Dependências

| Dependência | Status |
|-------------|--------|
| MIG-3 Position Manager | ✅ Fechado |
| MIG-2 Market Data Engine | ✅ Fechado |
| MIG-1 Indicator Engine | ✅ Fechado |
| MIG-5 Signal Validation | 🔴 Não iniciado — interface de sinal deve ser estável |
| MIG-6 Execution Engine | 🔴 Não iniciado — Risk Engine entrega decisão, não executa |

**Nota:** durante o MIG-4, o sinal pode ser representado por um contrato canônico estável (`SignalRiskInput`) sem depender da implementação completa do MIG-5.

---

## 7. Divergências e Decisões Pendentes

| ID | Tópico | Proposta PSA | Status |
|----|--------|--------------|--------|
| DIV-PSA-M4-01 | Fonte do sinal | Contrato `SignalRiskInput` canônico; MIG-5 preencherá posteriormente | Aguardando AIC |
| DIV-PSA-M4-02 | Granularidade de exposição | `ExposureSummary` do MIG-3 é suficiente para MIG-4; detalhe por ticket fica para SIVR-1 | Aguardando AIC |
| DIV-PSA-M4-03 | Formato de SL/TP | Valores absolutos de preço (não distância fixa em pontos) | Aguardando AIC |

---

## 8. Riscos

| Risco | Mitigação |
|-------|-----------|
| Reintrodução de parâmetros fixos (BUG-006) | CA-03 + teste de regressão + revisão de código |
| Acoplamento prematuro com MIG-5 | Interface `SignalRiskInput` estável e mockável |
| Risk Engine executando ordens | CA-07 + lint de governança proibindo `order_send` |
| Sizing não determinístico | CA-05 + propriedade de reprodutibilidade |

---

## 9. Cronograma Preliminar

| Fase | Duração estimada | Entrega |
|------|------------------|---------|
| Charter aprovado | — | DEC-MIG4-001 |
| Contratos | 1 dia | `contracts/risk_contract.py` |
| Implementação core | 3 dias | `risk_engine/` + tests |
| Integração MIG-3 | 1 dia | Consumo `ExposureSummary` |
| CI e validação | 1 dia | 45+ testes pass, zero lint |
| Parecer PSA | 1 dia | GATE-MIG4-PARECER-PSA-001 |
| Deliberação Gate | — | DEC-GATE-MIG4-001 |

**Total estimado:** 7 dias úteis após aprovação do charter.

---

## 10. Governança e Sequenciamento

- **Implementação bloqueada** até aprovação do Conselho via DEC-MIG4-001.
- **Sem execução financeira** em nenhum ambiente durante o MIG-4.
- **Workspace isolation:** PSA mantém `OMEGA-PSA-AUDIT-WORKSPACE`; AIC mantém `OMEGA-Kernel-Sovereign`. Comunicação por charters, pareceres, diretivas e SYNC-OUT.

---

## 11. Checklist para Aprovação do Conselho

- [ ] Escopo do MIG-4 ratificado
- [ ] CA-01..CA-08 aprovados como critérios oficiais
- [ ] Proibições absolutas aceitas
- [ ] Divergências DIV-PSA-M4-01 a DIV-PSA-M4-03 resolvidas ou delegadas
- [ ] AIC declarou capacidade de execução no prazo estimado
- [ ] PSA emitirá parecer após implementação, antes de DEC-GATE-MIG4-001

---

**PSA**  
**OMEGA Kernel Sovereign V6**  
**TASK-0024-MIG4-CHARTER-PSA-001 — RASCUNHO**
