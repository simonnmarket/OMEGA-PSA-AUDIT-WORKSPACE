# ADR — OMEGA OS Decisões Formais

## Índice

| ADR | Título | Status | Data |
|-----|--------|--------|------|
| ADR-001 | Congelamento Prudencial e Preservação Forense | ACEITE | 2026-06-18 |
| ADR-002 | Eleição de Motor Soberano Único | SUPERSEDIDO por ADR-007 | 2026-06-18 |
| ADR-003 | Proibição de Fallback Sintético | PENDENTE (aguarda V6) | 2026-06-18 |
| ADR-004 | Eliminação dos '8 Filtros PASS' Hardcoded | PENDENTE (aguarda V6) | 2026-06-18 |
| ADR-005 | Segregação Mandatória de Ambientes | PENDENTE (aguarda V6) | 2026-06-18 |
| ADR-006 | Correção Mandatória do Key Mismatch RSI | PENDENTE (aguarda V6 MIG-1) | 2026-06-18 |
| ADR-007 | Reconstrução Soberana OMEGA OS — V6 | APROVADO CONSELHO 2026-06-21 | 2026-06-21 |
| ADR-008 | Runtime Soberano do OMEGA OS V6 | APROVADO CONSELHO 2026-06-22 | 2026-06-22 |
| ADR-009 | Launcher Soberano — deployment/omega_run.py | APROVADO CONSELHO 2026-06-22 | 2026-06-22 |
| ADR-010 | Fluxo Soberano de Execução | APROVADO CONSELHO 2026-06-22 | 2026-06-22 |
| ADR-011 | Ambiente Soberano — OMEGA_ENV | APROVADO CONSELHO 2026-06-22 | 2026-06-22 |

---

## ADR-001 · Congelamento Prudencial e Preservação Forense

**Contexto**
Motor legacy não inicializa (RT-01). Logs de execução são sintéticos (RT-02). Última execução = 100% HOLD (RT-03). Artefatos críticos de governança não estavam persistidos canonicamente.

**Decisão**
Congelamento imediato: proibir novos launchers, flags e execuções até deliberação do Conselho. Preservar integralmente PF-01 a PF-09 sem alteração, movimentação ou limpeza.

**Consequências**
Consenso 6/6. Reversível. Nenhuma capacidade de trading é impactada pois o sistema já está parado.

---

## ADR-002 · Eleição de Motor Soberano Único como Pré-requisito de Saneamento

**Status: SUPERSEDIDO por ADR-007**

**Contexto**
Dois motores concorrentes sem soberano definido (FND-01). Seleção de launcher sem autoridade única. Qualquer saneamento técnico (Classe B) aplicado ao motor errado é trabalho perdido ou perigoso.

**Decisão**
Nenhuma ação de Classe B é autorizada antes da eleição formal do motor soberano pelo Conselho. O motor eleito receberá todas as correções; o alternativo será reclassificado como legacy ou desativado.

**Consequências**
Consenso 6/6. Exige deliberação formal do Conselho. Desbloqueia ACT-B1..B7.

---

## ADR-003 · Proibição de Fallback Sintético em Qualquer Caminho Produtivo

**Status: PENDENTE (aguarda V6)**

**Contexto**
`_get_sample_data()` retorna preço fixo 2650.50 em qualquer exceção de `build_market_data()`, alcançável pelo caminho oficial `v33_final.py:1772`. Dado sintético não-vazio passa o guard e pode gerar BUY/SELL real sobre dado falso (FND-06).

**Decisão**
Em qualquer `except` de `build_market_data()`, retornar `{}` (ou elevar exceção explícita) para forçar HOLD. Nunca retornar dado sintético. Execução pós-correção obrigatória em demo antes de qualquer exec real. Aguarda ACT-C1.

---

## ADR-004 · Eliminação dos '8 Filtros PASS' Hardcoded da Trilha de Auditoria

**Status: PENDENTE (aguarda V6)**

**Contexto**
`shadow_loop_v33_final.py:1917-1937` emite 8 filtros literalmente como PASS sem avaliação individual. A trilha FOR11 registra 'dimensões validadas' que nunca foram testadas, gerando confiança falsa de robustez (FND-10).

**Decisão**
Substituir os literais PASS por resultados reais de avaliação, ou remover a dimensão do relatório se não houver avaliação real. A trilha de auditoria deve refletir somente o que foi de fato avaliado. Aguarda ACT-C1.

---

## ADR-005 · Segregação Mandatória de Ambientes dev / test / demo / exec

**Status: PENDENTE (aguarda V6)**

**Contexto**
`shadow_loop.py:544` aplica env > arquivo sem gating de ambiente. Qualquer variável de teste exportada no shell vaza para demo/exec. Flags de sessão de desenvolvimento podem alterar comportamento de trading real (FND-08).

**Decisão**
Implementar gating de ambiente no `_get_flag()`: variáveis com prefixo `TEST_`/`DEV_` só aceitam override em `OMEGA_ENV=test` ou `OMEGA_ENV=dev`. Em `OMEGA_ENV=exec`, somente o arquivo `config/live_flags.json` é lido; env vars de teste são ignoradas. Aguarda ACT-C1.

---

## ADR-006 · Correção Mandatória do Key Mismatch RSI (FND-11) Antes de Qualquer Execução

**Status: PENDENTE (aguarda V6 MIG-1)**

**Contexto**
`shadow_loop_v33_final.py:1777` armazena o indicador com chave `'rsi'`. A linha `:1556` extrai com `'rsi_14'`. Chave não existe no dict: RSI=None. Guard `:1562` exige `rsi is not None` para calcular confiança. Resultado: confiança permanece 0.0 → 100% HOLD eterno. Confirma RT-03 e refuta FMED-05B.

**Decisão**
Corrigir `:1777` para armazenar chave `'rsi_14'` (harmonizando com a extração em `:1556`), ou corrigir `:1556` para extrair `'rsi'`. Escolha deve ser consistente com o schema de `market_data`. Após correção, run obrigatório em modo demo com inspeção do `strategy_decision_log` para confirmar confiança > 0.0 e presença de BUY/SELL antes de qualquer exec real. Aguarda ACT-C1.

**Consequências**
Este é o item mais urgente da Classe B: sem esta correção, o motor v33 é operacionalmente inerte mesmo com todos os outros fixes aplicados. Entra em pauta como DEC-08.

---

## ADR-007 · Reconstrução Soberana OMEGA OS — V6

**ID:** PROP-SOV-V6-20260621 · **Versão:** 2.0 · **Status:** APROVADO CONSELHO · **Data:** 2026-06-21

**Contexto**
P-SOB (Soberania): ninguém afirma qual é o runtime canônico. 2 motores paralelos, launchers divergentes, código auditado ≠ executado, corrigido ≠ preservado. Problema de governança, não técnico. Qualquer correção sobre runtime contaminado é trabalho perdido.

**Decisão**
Encerrar desenvolvimento no diretório atual. Congelar como OMEGA_V55_FROZEN (evidência forense, read-only). Criar repositório soberano novo OMEGA-KERNEL-SOVEREIGN V6 com histórico limpo, 1 runtime, 1 launcher, segregação dev/test/demo/exec por gating OMEGA_ENV.

**4 Travas Anti-Regressão (impedir que V6 vire V5.5)**

1. GATE-0 obrigatório: sem Declaração de Soberania (4 respostas), nada começa
2. Contratos antes de código: topologia definida por interface, não descoberta depois
3. Proteção Git: PR obrigatório + Task ID em todo commit + CI verde — impossível code path fantasma
4. Taskade = autoridade única: fluxo Conselho→Taskade→Spec→Impl→Teste→Merge→Deploy. Fora do fluxo = NÃO OFICIAL

**Gates GO/NO-GO (sequência obrigatória)**

- [ ] GATE-0 — Declaração de Soberania: runtime + launcher + fluxo + ambiente (CFO-03)
- [ ] GATE-1 — V5.5 congelado read-only, snapshot/hash registrado
- [ ] GATE-1.5 — 5 registries da FASE 1.5 preenchidos: KNOWLEDGE_MASTER_INDEX + BUG_REGISTRY + FIX_REGISTRY + DECISION_REGISTRY + RUNTIME_REGISTRY (CFO-01)
- [ ] GATE-2 — V6 sobe em dev: 1 runtime, telemetria com IDs, zero componente legacy
- [ ] GATE-3 — Componente migrado: contrato + interface + teste verde + aprovação Taskade (CFO-02)
- [ ] GATE-DEMO — Execução DEMO só após GATE-3 completo para MIG-1..5

**Consequências**
Aprovação unânime do Conselho (DEC-1..9 todos aprovados). Repositório atual torna-se OMEGA_V55_FROZEN. Nenhum desenvolvimento novo no legacy. Próximo passo imediato: GATE-0 — Declaração de Soberania.

---

## ADR-008 · Runtime Soberano do OMEGA OS V6

**Repo:** https://github.com/simonnmarket/OMEGA-Kernel-Sovereign | **Implementado no V6** | **Vigência:** 2026-06-22

**Contexto**
V5.5 possuía 2 motores concorrentes sem soberano declarado (FND-01/BUG-007). Código auditado ≠ executado. Qualquer correção aplicada ao motor errado era trabalho perdido. ADR-007 determinou reconstrução soberana V6.

**Decisão**
O V6 possui exatamente 1 runtime soberano declarado. O motor legacy (V5.5) é classificado como OMEGA_V55_FROZEN — read-only, evidência forense. Nenhum componente do V6 importa ou referencia código do diretório frozen. Resolve BUG-007 por exclusão arquitetural e BUG-005 (motor legacy) por descontinuação formal.

**Consequências**
Aprovado unanimidade Conselho — Ata 2026-06-22. TASK-0011 concluída. Desbloqueia GATE-0.

---

## ADR-009 · Launcher Soberano — deployment/omega_run.py

**Repo:** https://github.com/simonnmarket/OMEGA-Kernel-Sovereign | **Implementado no V6** | **Vigência:** 2026-06-22

**Contexto**
V5.5 possuía múltiplos launchers divergentes (FND-08/BUG-004): `shadow_loop.py:544` aplicava env > arquivo sem gating de ambiente. Flags de sessão dev vazavam para exec. ADR-002 determinava eleição formal — substituído por esta decisão concreta.

**Decisão**
O único launcher autorizado do V6 é `deployment/omega_run.py`. Fail-closed: exige OMEGA_ENV declarado explicitamente. Qualquer execução fora deste launcher = não oficial. Supersede ADR-002 com implementação concreta.

**Consequências**
Aprovado unanimidade Conselho — Ata 2026-06-22. TASK-0012 concluída. Resolve BUG-004 por design. Supersede ADR-002.

---

## ADR-010 · Fluxo Soberano de Execução

**Repo:** https://github.com/simonnmarket/OMEGA-Kernel-Sovereign | **Implementado no V6** | **Vigência:** 2026-06-22

**Contexto**
V5.5 não tinha fluxo declarado: componentes acoplados de forma implícita, fallbacks sintéticos em caminho produtivo, RSI key mismatch tornando o motor inerte, 8 filtros PASS hardcoded. Logs sintéticos impediam rastreabilidade real.

**Decisão**
O fluxo soberano do V6 é: dados → indicadores → estratégia → risco → execução → telemetria. Cada etapa é um componente isolado com contrato de interface explícito (MIG-1..5). Falha em qualquer etapa = HOLD obrigatório, sem fallback sintético. Telemetria com IDs rastreáveis em toda decisão.

**Consequências**
Aprovado unanimidade Conselho — Ata 2026-06-22. TASK-0013 concluída. Resolve por design: BUG-001 (RSI→MIG-1), BUG-002 (fallback→MIG-2), BUG-003 (filtros→MIG-1), BUG-006 (SL/TP→MIG-4), BUG-008 (logs→telemetria).

---

## ADR-011 · Ambiente Soberano — OMEGA_ENV ∈ {dev, test, demo, exec}

**Repo:** https://github.com/simonnmarket/OMEGA-Kernel-Sovereign | **Implementado no V6** | **Vigência:** 2026-06-22

**Contexto**
V5.5 sem segregação formal: flags de dev vazavam para exec (BUG-004), lockfiles órfãos sem referência (BUG-009), flags expiradas sem consumidor (BUG-010). ADR-005 definiu a intenção — esta ADR concretiza a implementação.

**Decisão**
`OMEGA_ENV ∈ {dev, test, demo, exec}` é obrigatório em toda execução. Gating: prefixos `TEST_`/`DEV_` só são aceitos em `env=test` ou `env=dev`. Em `exec`: apenas `config/live_flags.json` é lido; env vars de teste são ignoradas. Fail-closed: OMEGA_ENV ausente = recusa de inicialização. MIG-5 implementa os guards de execução.

**Consequências**
Aprovado unanimidade Conselho — Ata 2026-06-22. TASK-0014 concluída. Complementa ADR-005. Resolve BUG-004/009/010 por gating arquitetural. MIG-5 (Execution Engine) é responsável pela implementação.
