# KNOWLEDGE MASTER INDEX — OMEGA Kernel Sovereign V6

## GATE-1.5 · Índice Mestre de Conhecimento Acumulado

Propósito: impedir que V6 reconstrua os mesmos erros do V5.5. Todo FND, FMED, RT, DEC, ADR, VOT e PF catalogado aqui deve ser consultado antes de qualquer decisão de arquitetura ou código no V6.

## Findings (FND) — Problemas Descobertos

* FND-02 — Lockfiles órfãos sem referência ao runtime ativo (sem consumidor declarado)
* FND-03 — Flags congeladas/expiradas: definidas sem consumidor ou consumidas sem definição explícita

* FND-01 — Dois motores concorrentes sem soberano definido
* FND-04 — SL/TP não derivam do sinal da estratégia
* FND-06 — Fallback sintético _get_sample_data() retorna preço fixo 2650.50 em qualquer exceção — gera BUY/SELL sobre dado falso
* FND-08 — Launchers divergentes: env vars e flags com override sem gating de ambiente
* FND-10 — 8 filtros literalmente PASS sem avaliação individual (shadow_loop_v33_final.py:1917-1937) — confiança falsa
* FND-11 — Key mismatch RSI: armazenado como 'rsi' (linha 1777), extraído como 'rsi_14' (linha 1556) → RSI=None → confiança=0.0 → 100% HOLD eterno

## Runtime Facts (RT) — Comportamentos Observados em Execução

* RT-01 — Motor legacy não inicializa: NameError: MT5BulletproofLayer. Falha silenciosa, sem propagação de erro rastreável.
* RT-02 — Logs de execução são sintéticos. Não refletem operação real.
* RT-03 — Última execução observada: 100% HOLD eterno. Causa raiz confirmada: BUG-001 (RSI key mismatch → confiança=0.0). Refuta FMED-05B.

## ADRs Formais Emitidas

* ADR-008 · Separação MIG-5 (Signal Validation) / MIG-6 (Execution Engine Sovereign) — **APROVADO CFO 2026-06-23**
* DEC-14 · Escopo Negativo Absoluto — **NENHUM MIG AUTORIZADO** até GATE-0 GOVERNANÇA fechado (PR TASK-0018-SYNC mergeado + revisão aprovada) · CFO 2026-06-23

  * DEC-15 — Ratificação do Plano Mestre (ADR-009) · CEO + CFO · 2026-06-23 · Regra CFO-03 vigente — nenhuma atividade paralela sem aprovação
* ADR-012 · Plano Mestre de Execução V6 — Roadmap sequencial MIG-1..6 → DEMO → SHADOW → REAL — Regra CFO-03 — **APROVADO CEO + CFO 2026-06-23** · CFO-DIR-20260623-02 · CFO-RAT-20260623-03 · *ADR-009 = VOID (ID reservado, não usar)*
* DEC-16 · CFO-RAT-20260623-03 — (1) ADR-012 = Plano Mestre oficial (ADR-009 VOID) · (2) Modelo 6 MIGs ratificado · (3) Mapeamento BUG↔MIG canônico aprovado · BUG-005/007/008 = EVIDÊNCIA FORENSE · **APROVADO CEO + CFO 2026-06-23**

* ADR-001 · Congelamento Prudencial e Preservação Forense — ACEITE
* ADR-002 · Eleição de Motor Soberano Único — SUPERSEDIDO por ADR-007
* ADR-003 · Proibição Fallback Sintético — PENDENTE (aguarda V6)
* ADR-004 · Eliminação 8 Filtros PASS — PENDENTE (aguarda V6)
* ADR-005 · Segregação Mandatória dev/test/demo/exec — PENDENTE (aguarda V6)
* ADR-006 · Correção Mandatória Key Mismatch RSI — PENDENTE (aguarda V6 MIG-1)
* ADR-007 · Reconstrução Soberana V6 — APROVADO CONSELHO 2026-06-21

## Links dos 5 Registries — GATE-1.5

1. MATRIZ EXECUTIVA DE RASTREABILIDADE — bXbRyP9GqAKLdQub (11 campos · DEC/FND/RT/ACT/MIG completos)
2. KNOWLEDGE_MASTER_INDEX — PztRauR1qqycZGts (este projeto)
3. BUG_REGISTRY — 5nVprzrMFFHNf2Lt
4. FIX_REGISTRY — V3BrNbEfkfD2QpJS
5. DECISION_REGISTRY — DP9yLaoY7iqTNbyP
6. RUNTIME_REGISTRY — NJyqhR6f5aNy7owv

---

# OMEGA-KERNEL-SOVEREIGN V6 — Status Atual

Repo: https://github.com/simonnmarket/OMEGA-Kernel-Sovereign · CI: ativo (ruff + pytest) · Atualizado: 2026-06-21

## Tasks Concluídas (V6)

* [x] TASK-0001 — Scaffold inicial V6: estrutura limpa + GATE-0 + FASE 1.5 + allow-list · commit 7362246
* [x] TASK-0002 — CI (ruff + pytest) + testes de governança · commit 3761193 · PR #1 mergeado
* [x] GOV-SETUP — Repo GitHub + ruleset protect-main: PR obrigatório, sem force-push, status check CI ativo

## Gates GO/NO-GO — Estado Atual

* [x] GATE-0 — Declaração de Soberania (runtime/launcher/fluxo/ambiente) · APROVADO · Ata 2026-06-22 · TASK-0011..0015 concluídas
* [ ] GATE-1 — V5.5 congelado read-only + snapshot/hash · PENDENTE · TASK-0003..0006
* [ ] GATE-1.5 — 5 registries preenchidos e validados (arquivo:linha) · PENDENTE · TASK-0007..0010
* [ ] GATE-2 — V6 sobe em dev: 1 runtime + CI verde + telemetria com IDs · FUNDAÇÃO OK (CI ativo, estrutura limpa)
* [ ] GATE-3 — MIG-1..6: contrato + interface + teste + aprovação Conselho · PENDENTE (MIG-6 adicionado por DEC-CFO-20260623-T18)

  * GATE-MIG1 — MIG-1 concluído: indicadores canônicos, BUG-006+007 resolvidos, CI verde · PRÉ-CONDIÇÃO: GATE-0 FECHADO
  * GATE-MIG2 — MIG-2 concluído: dados reais, zero fallback sintético, CI verde · PRÉ-CONDIÇÃO: GATE-MIG1
  * GATE-MIG3 — MIG-3 concluído: posições rastreáveis, telemetria ativa, CI verde · PRÉ-CONDIÇÃO: GATE-MIG2
  * GATE-MIG4 — MIG-4 concluído: SL/TP derivam do sinal (BUG-003 resolvido), CI verde · PRÉ-CONDIÇÃO: GATE-MIG3
  * GATE-MIG5 — MIG-5 concluído: validação de sinal desacoplada, telemetria, CI verde · PRÉ-CONDIÇÃO: GATE-MIG4
  * GATE-MIG6 — MIG-6 concluído: execução soberana, DEMO/REAL segregados, CI verde · PRÉ-CONDIÇÃO: GATE-MIG5
  * GATE-DEMO — 5 dias úteis em conta DEMO, operação estável · PRÉ-CONDIÇÃO: GATE-MIG6
  * GATE-SHADOW — 10 dias úteis shadow mode, consistência operacional · PRÉ-CONDIÇÃO: GATE-DEMO
  * GATE-REAL — ADR específico aprovado pelo Conselho · **SEM ESTA APROVAÇÃO: EXECUÇÃO REAL PROIBIDA** · PRÉ-CONDIÇÃO: GATE-SHADOW
* [ ] GATE-DEMO — Execução DEMO após MIG-1..5 completos · PENDENTE

## Backlog V6 — Tasks Abertas

### FASE 1 — Congelar V5.5

* [ ] TASK-0003 — Definir caminho oficial do legacy a congelar (OMEGA_V55_FROZEN)
* [ ] TASK-0004 — Gerar snapshot imutável (hash/inventário de arquivos)
* [ ] TASK-0005 — Marcar diretório como OMEGA_V55_FROZEN (read-only) no GitHub
* [ ] TASK-0006 — Registrar congelamento em RUNTIME_REGISTRY + Taskade

### FASE 1.5 — Extração de Conhecimento · governance/knowledge_extraction/

* [ ] TASK-0007 — Validar BUG_REGISTRY com evidência arquivo:linha no snapshot (FND-02/03/04/06/08/11 + RT-01)
* [ ] TASK-0008 — Validar FIX_REGISTRY: FMED-02..05B (FMED-05B = REFUTADO confirmado)
* [ ] TASK-0009 — Consolidar este KNOWLEDGE_MASTER_INDEX (atualização contínua)
* [ ] TASK-0010 — Fechar RUNTIME_REGISTRY: motores, launchers, flags, lockfiles/orfãos (FND-02 + FND-03)

### GATE-0 — Declaração de Soberania · governance/DECLARACAO_SOBERANIA_GATE0.md

* [x] TASK-0011 — Definir o runtime soberano do V6 · RATIFICADO Ata 2026-06-22
* [x] TASK-0012 — Definir o launcher soberano: deployment/omega_run.py (fail-closed, exige OMEGA_ENV) · RATIFICADO
* [x] TASK-0013 — Definir o fluxo soberano: dados→indicadores→estratégia→risco→execução→telemetria · RATIFICADO
* [x] TASK-0014 — Definir o ambiente soberano: OMEGA_ENV ∈ {dev, test, demo, exec} · RATIFICADO
* [x] TASK-0015 — Assinaturas Conselho: CEO / CTO / CFO / CQO / COO · Ata 2026-06-22

### FASE 3 — Migração Controlada (contratos primeiro)

* MIG-6 — Execution Engine Sovereign (Order Manager, Broker Connector, Trade Mode Validation, Environment Gating, Execution Pipeline) · **NOVO — DEC-CFO-20260623-T18**

  * [ ] Contrato
  * [ ] Interface
  * [ ] Teste verde
  * [ ] Aprovação Conselho

* MIG-1 — EMA/Indicator Engine (resolve FND-11: RSI key mismatch, FND-10: 8 PASS hardcoded)

  * [ ] Contrato
  * [ ] Interface
  * [ ] Teste verde
  * [ ] Aprovação Taskade

* MIG-2 — MT5 Connector (falha ⇒ HOLD obrigatório; sem fallback sintético — FND-06)

  * [ ] Contrato
  * [ ] Interface
  * [ ] Teste verde
  * [ ] Aprovação Taskade

* MIG-3 — Position Manager

  * [ ] Contrato
  * [ ] Interface
  * [ ] Teste verde
  * [ ] Aprovação Taskade

* MIG-4 — Risk Manager Adaptive (SL/TP derivam do sinal — FND-04)

  * [ ] Contrato
  * [ ] Interface
  * [ ] Teste verde
  * [ ] Aprovação Taskade

* MIG-5 — Signal Validation Layer (validar sinais, consistência, integridade, contratos — SEM enviar ordens) · **REDEFINIDO DEC-CFO-20260623-T18**

  * [ ] Contrato
  * [ ] Interface
  * [ ] Teste verde
  * [ ] Aprovação Taskade

### Infra / Manutenção

* [x] TASK-0018 — PASSO 2: ADR-008..011 criados (branch task-0018-sync · commit 6bf7e4e) — sem colisão de numeração · aguarda PASSO 3 (merge PR)
* [x] TASK-0018 — SYNC PR governance/ · Branch: TASK-0018-SYNC · **ARTEFATOS ENTREGUES AO AIC** · Aprovado DEC-CFO-20260623-T18 · Escopo: 4 arquivos modificados + 10 criados em governance/ · BUG-006=RESERVADO · Nenhum arquivo operacional alterado · PRÓXIMO: AIC executa Git → PR → revisão obrigatória → merge → GATE-0 GOVERNANÇA FECHADO
* [x] TASK-0019 — SYNC_PROTOCOL.md · Protocolo oficial de sincronização Taskade ↔ GitHub · **CONCLUÍDA** · CFO-RAT-20260623-03
* [x] TASK-0020 — SYNC_LOG.md · Registro contínuo de sincronizações · **CONCLUÍDA** · CFO-RAT-20260623-03 · SYNC-0001 registrado

* [ ] TASK-0016 — Limpar aviso Node no CI: atualizar actions/checkout@v5 + setup-python@v6
* [ ] TASK-0017 — Confirmar 'Require status checks = ci' ativo no ruleset do GitHub

## Definition of Done (DoD) — Convenções Obrigatórias

1. Toda task tem ID rastreável: TASK-xxxx / MIG-x / DEC-x / FND-xx / ADR-xxx
2. Todo commit usa prefixo: [TASK-xxxx] mensagem
3. Nada entra em main sem PR + CI verde + aprovação
4. Componente 'Done' = contrato + interface + teste verde + aprovação Taskade
5. Alteração fora do fluxo Conselho→Taskade→Spec→Impl→Teste→Merge→Deploy = NÃO OFICIAL
