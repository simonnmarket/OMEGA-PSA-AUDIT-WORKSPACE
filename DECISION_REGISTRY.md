# DECISION_REGISTRY — Conselho OMEGA OS

## Índice por TYPE + STATUS

### TYPE: OPERATIONAL (Decisões operacionais imediatas)

| ID | Decisão | Status | Data | Vínculo |
|----|---------|--------|------|---------|
| DEC-01 | Congelamento prudencial imediato do sistema. Proibir novos launchers, flags e execuções | ✅ APROVADO | 2026-06-18 | ADR-001 |
| DEC-02 | Preservar artefatos PF-01..PF-09 sem alteração, movimentação ou limpeza | ✅ APROVADO | 2026-06-18 | ADR-001 |
| DEC-03 | Nenhuma ação Classe B antes de eleição formal do motor soberano | ✅ APROVADO | 2026-06-18 | ADR-002 |
| DEC-08 | Correção mandatória key mismatch RSI (FND-11) antes de qualquer execução | ✅ APROVADO | 2026-06-18 | ADR-006 |

### TYPE: TECHNICAL (Decisões técnicas de implementação)

| ID | Decisão | Status | Data | Vínculo |
|----|---------|--------|------|---------|
| DEC-04 | Implementar gating OMEGA_ENV: variáveis TEST_/DEV_ só aceitam override em env=test/dev | ✅ APROVADO | 2026-06-18 | ADR-005, ADR-011 |
| DEC-05 | Proibição total de fallback sintético em qualquer caminho produtivo (FND-06) | ✅ APROVADO | 2026-06-18 | ADR-003 |
| DEC-06 | Eliminação dos 8 filtros PASS hardcoded: substituir por avaliação real ou remover | ✅ APROVADO | 2026-06-18 | ADR-004 |

### TYPE: STRATEGIC (Decisões de reconstrução V6 — ADR-007)

| ID | Decisão | Status | Data | Vínculo |
|----|---------|--------|------|---------|
| DEC-V6-1 | Congelar V5.5 como OMEGA_V55_FROZEN (read-only) | ✅ APROVADO | 2026-06-21 | ADR-007 |
| DEC-V6-2 | Criar repositório OMEGA-KERNEL-SOVEREIGN V6 (histórico limpo) | ✅ APROVADO | 2026-06-21 | ADR-007 |
| DEC-V6-3..9 | Allow-list MIG-1..6, PSA=autoridade documental, Proibir legacy, GATE-0, FASE 1.5, Proteção Git, Contratos antes código | ✅ APROVADO | 2026-06-21 | ADR-007 |

### TYPE: GOVERNANCE (Decisões de governança documental)

| ID | Decisão | Status | Data | Vínculo |
|----|---------|--------|------|---------|
| DEC-GOV-01 | Unicidade Documental Obrigatória — cada domínio = 1 projeto CANONICAL | ✅ APROVADO | 2026-06-21 | — |
| DEC-GOV-02 | Separação Definitiva: Fluxo Ativo vs Evidência Selada (3 camadas) | ✅ APROVADO | 2026-06-22 | DEC-1, DEC-7/CFO-01, GATE-1, GATE-1.5, ADR-007 |
| DEC-14 | Escopo Negativo Absoluto — NENHUM MIG AUTORIZADO até GATE-0 GOVERNANÇA fechado | ✅ APROVADO | 2026-06-23 | CFO |
| DEC-15 | Ratificação do Plano Mestre (ADR-012) — Regra CFO-03 vigente | ✅ APROVADO | 2026-06-23 | CEO + CFO |
| DEC-16 | CFO-RAT-20260623-03 — ADR-012 = Plano Mestre oficial, Modelo 6 MIGs ratificado, Mapeamento BUG↔MIG canônico | ✅ APROVADO | 2026-06-23 | CEO + CFO |
| DEC-17 | CFO-RATIFICATION-001 — PSA integrado, Taskade removido, PSA = autoridade documental oficial | ✅ APROVADO | 2026-06-24 | CFO |
| DEC-18 | CFO-RATIFICATION-002 — GATE-0 GOVERNANÇA FECHADO, ETAPA 0 CONCLUÍDA, MIG-1 Charter autorizado | ✅ RATIFICADO | 2026-06-24 | Conselho (CEO + CFO) |
| DEC-19 | SIVR-0 aprovado como EXECUTION PROOF MIG-1 — 100/100 ciclos XAUUSD M1 MT5 demo real | ✅ APROVADO | 2026-06-24 | CFO + Conselho |
| DEC-20 | TASK-0022 — MIG-2 CHARTER autorizado (somente planejamento; implementação bloqueada) | ✅ AUTORIZADO | 2026-06-24 | CFO + Conselho |
| DEC-21 | Opção A adotada: sequência canônica MIG-1→MIG-2→...→MIG-6; SIVR-1 mantido como objetivo estratégico futuro sem implementação autorizada; nenhum componente execution/order/reconciliation antes de charter+gate aprovados | ✅ RATIFICADO | 2026-06-24 | Conselho |

### TYPE: GATE (Decisões de portão — GATE-0)

| ID | Decisão | Status | Data | Vínculo |
|----|---------|--------|------|---------|
| DEC-GATE0-1 | Runtime soberano único declarado (V6) | ✅ RATIFICADO | 2026-06-22 | ADR-008 · TASK-0011 |
| DEC-GATE0-2 | Launcher soberano: deployment/omega_run.py (fail-closed) | ✅ RATIFICADO | 2026-06-22 | ADR-009 · TASK-0012 |
| DEC-GATE0-3 | Fluxo soberano: dados→indicadores→estratégia→risco→execução→telemetria | ✅ RATIFICADO | 2026-06-22 | ADR-010 · TASK-0013 |
| DEC-GATE0-4 | Ambiente soberano: OMEGA_ENV ∈ {dev,test,demo,exec} (gating obrigatório) | ✅ RATIFICADO | 2026-06-22 | ADR-011 · TASK-0014 |

### TYPE: GATE (Decisões de portão — GATE-MIG1)

| ID | Decisão | Status | Data | Vínculo |
|----|---------|--------|------|---------|
| DEC-GATE-MIG1 | GATE-MIG1 FECHADO — MIG-1 Indicator Engine validado, SIVR-0 PASS, EXECUTION PROOF registrado | ✅ FECHADO | 2026-06-24 | DEC-19 · SIVR-0-CLOSURE-001 · TASK-0021 |

---

## Tasks V6 Concluídas (Log de Execução)

| Task | Descrição | Status | Evidência |
|------|-----------|--------|-----------|
| TASK-0001 | Scaffold inicial V6: estrutura limpa + GATE-0 + FASE 1.5 + allow-list | ✅ CONCLUÍDA | commit 7362246 |
| TASK-0002 | CI (ruff + pytest) + testes de governança | ✅ CONCLUÍDA | commit 3761193 · PR #1 mergeado |
| GOV-SETUP | Repo GitHub OMEGA-Kernel-Sovereign + ruleset protect-main | ✅ CONCLUÍDA | PR obrigatório, sem force-push, status check CI |

---

## Mapeamento DEC ↔ ADR (canônico)

| DEC | ADR | Relação |
|-----|-----|---------|
| DEC-1 | ADR-001 | Congelar V5.5 |
| DEC-2 | ADR-007 | Criar V6 |
| DEC-3 | ADR-002 | Eleição motor (supersedido) |
| DEC-4 | ADR-005 + ADR-011 | Gating ambiente |
| DEC-5 | ADR-003 | Proibir fallback |
| DEC-6 (filtros) | ADR-004 | Eliminar 8 PASS |
| DEC-6 (GATE-0) | ADR-008 + ADR-009 + ADR-010 + ADR-011 | Soberania V6 |
| DEC-8 | ADR-006 | RSI key mismatch |
| DEC-GOV-02 | ADR-007 | Separação ativo/selado |

---

## DEC-GOV-01 — Unicidade Documental Obrigatória (2026-06-21)

**TYPE:** GOVERNANCE | **STATUS:** ✅ APROVADO

**Regra:** cada domínio funcional possui exatamente 1 projeto com status CANONICAL. Nenhum segundo projeto pode ter a mesma função sem deliberação explícita do Conselho. Antes de criar qualquer projeto/campo, verificar autoridade primária existente. Projetos duplicados devem ser marcados DEPRECATED imediatamente e arquivados pelo operador.

**Projetos afetados:**
- ADR canônico → P9m78VQ8uEgARdnb
- Rastreabilidade canônica → oQzEmD1CsdAJFeD2
- Depreciados: j1gwum17FqHGqvqm, bXbRyP9GqAKLdQub

---

## DEC-GOV-02 — Separação Definitiva: Fluxo Ativo vs Evidência Selada (2026-06-22)

**TYPE:** GOVERNANCE | **STATUS:** ✅ APROVADO

**Aprovação:** CFO ✅ · CEO ✅ · CTO/TL ✅ | **Task:** TASK-0019 | **Vínculo:** DEC-1, DEC-7/CFO-01, GATE-1, GATE-1.5, ADR-007

**Modelo 3 camadas:**
- 🟢 **ATIVO** — Desenvolvimento V6
- 🟡 **ARQUIVADO** — Superseded
- 🧊 **SELADO** — Forense imutável

**Regra:** evidência preservada, não apagada. Código V5.5 proibido no fluxo ativo — referência apenas por ID canônico.

**Repo:** https://github.com/simonnmarket/OMEGA-Kernel-Sovereign | Executada via TASK-0019.1..7

---

## Próximo Task Livre

**TASK-0021** (conforme TASK-0018, TASK-0019 e TASK-0020 já concluídas)

---

## DEC-17 — CFO-RATIFICATION-001: Integração Operacional PSA (2026-06-24)

**TYPE:** GOVERNANCE | **STATUS:** ✅ APROVADO

**Aprovação:** CFO ✅

**Decisões ratificadas:**
- PSA considerado operacionalmente integrado
- Segregação PSA/AIC ratificada
- OMEGA-PSA-AUDIT-WORKSPACE reconhecido como autoridade documental oficial
- Taskade removido da governança ativa
- PSA substitui Taskade em todos os artefatos futuros

**Vínculo:** CFO-SYNC-001 · PSA-CONFIRMATION-001
