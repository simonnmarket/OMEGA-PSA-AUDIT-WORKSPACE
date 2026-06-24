# TASK-0021 — MIG-1 CHARTER REV-1: Indicator Engine

**ID:** TASK-0021  
**Revisão:** REV-1  
**Componente:** MIG-1 — Indicator Engine  
**Data original:** 2026-06-24  
**Data revisão:** 2026-06-24  
**Emitido por:** PSA (Autoridade Documental)  
**Destinatários:** CFO · Conselho · AIC (revisão técnica)  
**Status:** SUBMETIDO PARA REVISÃO DO CONSELHO  
**Autoridade:** CFO-DIR-20260624-TASK0021 · CFO-DIRECTIVE-20260624-PSA-CHARTER-REVISION-001  
**Base da revisão:** AIC-PARECER-MIG1-001

---

## Changelog REV-1

| Item | Alteração | Origem |
|------|-----------|--------|
| BUG-003 | Redefinido: escopo reclassificado entre MIG-1 e MIG-5 | AIC D-05, §2.2 |
| BUG-006 | Removido de MIG-1 — pertence a MIG-4. Referência causal mantida | AIC §2.2 |
| BUG-004 | Confirmado como MIG-6 — sem impacto em MIG-1 | AIC §2.2 |
| ETAPA 0 | Status corrigido: ✅ CONCLUÍDA (era "EM PROGRESSO") | AIC §2.2, DEC-18 |
| D-01 | Adicionada dependência: MarketDataSnapshot em contracts/ | AIC §2.1 |
| D-02 | Adicionada dependência: decisão de stack numérica | AIC §2.1 |
| D-03 | Adicionada dependência: parâmetros EMA/RSI V6 | AIC §2.1 |
| D-04 | Adicionada dependência: definição de telemetry/logging | AIC §2.1 |
| D-05 | Adicionada nota: harmonização ADR-004/006 vs ADR-010 | AIC §2.1 |
| D-06 | Corrigida inconsistência DEC-16 vs DEC-18 | AIC §2.1 |
| CA-05 | Revisado: critério refinado para evitar falso positivo | AIC §2.3 |
| CA-10 | Revisado: escopo expandido para contracts/ e tests/ | AIC §2.3 |
| Seção 4 | Escopo incluído expandido: contracts/ e tests/ agora explícitos | AIC CA-10 |
| Seção 14 | Chaves canônicas: adicionada decisão de parâmetros | AIC D-03 |

---

## Referências

- ADR-012 — Plano Mestre V6
- ADR-004 — Eliminação dos 8 Filtros PASS Hardcoded
- ADR-006 — Correção Mandatória Key Mismatch RSI
- DEC-15 — Ratificação do Plano Mestre
- DEC-16 — Modelo 6 MIGs ratificado, mapeamento BUG↔MIG canônico
- DEC-18 — GATE-0 FECHADO, ETAPA 0 CONCLUÍDA
- MIGRATION_ALLOWLIST v3.0
- BUG_REGISTRY (BUG-001, BUG-003)
- KNOWLEDGE_MASTER_INDEX (FND-10, FND-11)
- SYNC_PROTOCOL v2.0
- CFO-RATIFICATION-002
- AIC-PARECER-MIG1-001

---

# 1. Executive Summary

A MIG-1 é a primeira migração técnica do programa OMEGA Kernel Sovereign V6. Seu objetivo é reconstruir o **Indicator Engine** — componente responsável por calcular indicadores técnicos que alimentam todas as decisões de trading do sistema.

O Indicator Engine do V5.5 possui dois bugs críticos documentados (BUG-001 e BUG-003) que comprometem a operação: o RSI key mismatch (BUG-001) produz confiança=0.0 em 100% das iterações, resultando em HOLD eterno. Os 8 filtros PASS hardcoded (BUG-003) mascaram falhas reais.

**Nota REV-1:** O escopo de BUG-003 foi refinado conforme parecer AIC. A **remoção** dos 8 filtros PASS é responsabilidade da MIG-1 (eliminar código inerte do Indicator Engine). A **substituição** por validação real de sinais será escopo da MIG-5 (Signal Validation Layer). A MIG-1 remove o problema; a MIG-5 implementa a solução arquitetural.

Sem resolver a MIG-1, nenhuma outra MIG produz resultado útil, pois todas as camadas downstream dependem de indicadores válidos.

---

# 2. Objetivo da MIG-1

Construir um Indicator Engine soberano que:

1. Produza indicadores com **chaves canônicas padronizadas** (`rsi_14`, `ema_fast`, `ema_slow`, etc.)
2. **Nunca** retorne `None` para indicadores obrigatórios
3. **Remova** os 8 filtros PASS hardcoded do código do Indicator Engine (ADR-004)
4. **Corrija** o key mismatch RSI (ADR-006)
5. Exponha **contrato formal** de entrada/saída (`IndicatorContract`)
6. Defina **MarketDataSnapshot** como tipo de entrada (interface mínima para MIG-2)
7. Garanta **telemetria** rastreável por ID em cada cálculo

---

# 3. Problemas Resolvidos

## BUG-001 — Indicadores None (Key Mismatch RSI)

| Campo | Detalhe |
|-------|---------|
| **Causa raiz** | Indicador RSI armazenado como chave `rsi` (linha 1777 do legacy) mas extraído como `rsi_14` (linha 1556). Resultado: `None`. |
| **Impacto** | Confiança = 0.0 → sinal = HOLD → sistema 100% inerte. RT-03 confirma: "Última execução = 100% HOLD eterno". |
| **Relação com Indicator Engine** | É a camada que armazena e expõe os indicadores. A correção deve ser feita **na origem**: padronizar chaves no momento do cálculo e exposição. |
| **Mitigação proposta** | Definir dicionário canônico de chaves. Validação em runtime: se chave ausente → erro explícito (não `None` silencioso). Testes unitários cobrindo todos os indicadores. |
| **Finding:** | FND-11 |
| **ADR:** | ADR-006 |

---

## BUG-003 — 8 Filtros PASS Hardcoded (Escopo Refinado REV-1)

| Campo | Detalhe |
|-------|---------|
| **Causa raiz** | 8 filtros em `shadow_loop_v33_final.py` (linhas 1917-1937) retornam literalmente `PASS` sem avaliar nenhuma condição real. |
| **Impacto** | Falsa segurança. Nenhuma condição de risco é efetivamente verificada. |
| **Escopo MIG-1** | **Remover** os 8 filtros PASS do código do Indicator Engine. Garantir que o Indicator Engine não contenha lógica de validação fake. |
| **Escopo MIG-5 (NÃO MIG-1)** | **Substituir** por validação real de sinais na Signal Validation Layer. A lógica de validação pertence à Camada 5, não à Camada 1 (Indicadores). |
| **Finding:** | FND-10 |
| **ADR:** | ADR-004 |

---

## Bugs NÃO resolvidos pela MIG-1

| Bug | Razão | MIG responsável |
|-----|-------|-----------------|
| BUG-002 | Market Data — escopo MIG-2 | MIG-2 |
| BUG-004 | Múltiplos launchers — escopo MIG-6 | MIG-6 |
| BUG-006 | Risk Engine (SL/TP fixos) — escopo MIG-4. Nota: a causa raiz de BUG-006 é na camada de risco, não no Indicator Engine. A MIG-1 garante que indicadores cheguem corretos ao Risk Engine, mas não altera a lógica de SL/TP. | MIG-4 |
| BUG-009 | Broker Connector — escopo MIG-6 | MIG-6 |
| BUG-010 | Environment Gating — escopo MIG-6 | MIG-6 |

---

# 4. Escopo Incluído (Revisado REV-1)

| Item | Diretório | Descrição |
|------|-----------|-----------|
| Padronização de chaves | `indicator_engine/` | Dicionário canônico de indicadores |
| Eliminação de `None` | `indicator_engine/` | Nenhum indicador retorna `None` silenciosamente |
| Remoção dos 8 PASS | `indicator_engine/` | Eliminar filtros hardcoded (ADR-004) |
| Correção key mismatch | `indicator_engine/` | `rsi_14` como chave canônica (ADR-006) |
| IndicatorContract | `contracts/` | Contrato formal entrada/saída do Indicator Engine |
| MarketDataSnapshot (interface mínima) | `contracts/` | Tipo de dados de entrada — interface mínima necessária para desacoplamento com MIG-2 |
| Testes unitários | `tests/` | Cobertura de indicadores com dados válidos e inválidos |
| Telemetria | `indicator_engine/` | Cada cálculo com timestamp + indicator_id + valor |
| Documentação técnica | `governance/` | Especificação do componente |

**Nota REV-1:** `contracts/` e `tests/` estão **explicitamente incluídos** no escopo, pois o contrato e os testes são entregáveis obrigatórios da MIG-1 (conforme ADR-012 §"contratos antes de código").

---

# 5. Escopo Excluído

| Item | Razão | MIG responsável |
|------|-------|-----------------|
| Market Data Engine | Camada de dados separada | MIG-2 |
| Position Manager | Gerenciamento de posição | MIG-3 |
| Risk Engine | Cálculo SL/TP (BUG-006) | MIG-4 |
| Signal Validation | Camada 5 arquitetural (substituição dos PASS) | MIG-5 |
| Execution Engine | Envio de ordens (BUG-004, BUG-009, BUG-010) | MIG-6 |
| Runtime Engine | Launcher/runtime — já definido | N/A |
| Deployment | Deploy do sistema | Pós-GATE-MIG6 |
| Produção | Operação real | GATE-REAL |
| Gestão de ordens | Order Manager | MIG-6 |
| Estratégia | Lógica de decisão de trading | Componente nativo V6 |
| Implementação de validação real de sinais | Substituição dos PASS por validação | MIG-5 |

---

# 6. Dependências (Revisadas REV-1)

## Técnicas

| ID | Dependência | Status | Nota |
|----|-------------|--------|------|
| DEP-01 | GATE-0 GOVERNANÇA FECHADO | ✅ Satisfeita | DEC-18 · CFO-RATIFICATION-002 |
| DEP-02 | Estrutura de diretórios V6 | ✅ Satisfeita | TASK-0001 (scaffold) |
| DEP-03 | CI ativo (ruff + pytest) | ✅ Satisfeita | TASK-0002 |
| D-01 | MarketDataSnapshot em contracts/ | ⚠️ **NOVA** | O IndicatorContract precisa de um tipo de entrada. Definir `MarketDataSnapshot` como interface mínima (dataclass com OHLCV). Não implementa Market Data Engine (MIG-2), apenas define o contrato de entrada. |
| D-02 | Stack numérica (numpy vs pure Python) | ⚠️ **NOVA** | Decisão necessária antes da implementação: usar numpy (performance) ou pure Python (zero dependências). **Recomendação PSA:** numpy (padrão da indústria para cálculos financeiros). Decisão final: AIC + Conselho. |
| D-03 | Parâmetros EMA/RSI V6 | ⚠️ **NOVA** | Definir períodos canônicos. Proposta: RSI=14, EMA_fast=12, EMA_slow=26, ATR=14. Decisão final: Conselho. |
| D-04 | Framework de telemetry/logging | ⚠️ **NOVA** | Definir se a telemetria usa `logging` stdlib, módulo dedicado em `telemetry/`, ou estrutura própria. **Recomendação PSA:** `logging` stdlib para MIG-1 (minimal), com migração futura para módulo dedicado se necessário. |

## Documentais

| Dependência | Status |
|-------------|--------|
| ADR-004 (eliminar 8 PASS) | ✅ Aprovada |
| ADR-006 (key mismatch RSI) | ✅ Aprovada |
| ADR-012 (Plano Mestre) | ✅ Consolidada |
| MIGRATION_ALLOWLIST v3.0 | ✅ Válida |

## Harmonização ADR (D-05)

O AIC identificou divergência potencial entre ADR-004/006 (escopo MIG-1) e ADR-010 (fluxo soberano). Análise PSA:

- **ADR-004** (Eliminação 8 PASS) → MIG-1 remove, MIG-5 substitui. Sem conflito com ADR-010.
- **ADR-006** (Key mismatch RSI) → MIG-1 corrige na origem. Conforme ADR-010 (fluxo soberano: dados→**indicadores**→estratégia→risco→execução→telemetria). O Indicator Engine é o segundo elo do fluxo.
- **Conclusão:** Não há divergência. ADR-004 e ADR-006 operam dentro do escopo do Indicator Engine, que é o segundo nó do fluxo definido por ADR-010.

## Harmonização DEC (D-06)

O AIC identificou inconsistência entre DEC-16 e DEC-18:

- **DEC-16** (2026-06-23): Ratificou ADR-012 como Plano Mestre, modelo 6 MIGs, mapeamento BUG↔MIG.
- **DEC-18** (2026-06-24): Declarou GATE-0 FECHADO, ETAPA 0 CONCLUÍDA.
- **Análise:** DEC-16 e DEC-18 são **complementares**, não contraditórias. DEC-16 estabeleceu o modelo; DEC-18 confirmou que o modelo foi implementado e fechou o gate. Não há inconsistência factual. A relação é: DEC-16 (define) → DEC-18 (confirma execução).

## Operacionais

| Dependência | Status |
|-------------|--------|
| Aprovação deste Charter REV-1 pelo Conselho | ⏳ Pendente |
| Parecer técnico do AIC sobre REV-1 | ⏳ Pendente |
| Ratificação CFO | ⏳ Pendente |
| Decisão D-02 (stack numérica) | ⏳ Pendente |
| Decisão D-03 (parâmetros) | ⏳ Pendente |

---

# 7. Critérios de Aceite (Revisados REV-1)

| # | Critério | Métrica | Notas REV-1 |
|---|----------|---------|-------------|
| CA-01 | Nenhum indicador retorna `None` | `assert all(v is not None for v in result.values())` | — |
| CA-02 | Chave `rsi_14` presente no output | `assert "rsi_14" in result` | — |
| CA-03 | Chave `ema_fast` presente no output | `assert "ema_fast" in result` | — |
| CA-04 | Chave `ema_slow` presente no output | `assert "ema_slow" in result` | — |
| CA-05 | Zero filtros PASS hardcoded no código do Indicator Engine | `grep -rn "PASS" indicator_engine/ \| grep -v test \| grep -v "#" == 0` — busca refinada excluindo testes e comentários para evitar falso positivo | **Revisado:** critério refinado para evitar match em strings legítimas (ex: nomes de variáveis, docstrings). AIC deve confirmar regex final. |
| CA-06 | Contrato `IndicatorContract` definido e importável | `from contracts.indicator_contract import IndicatorContract` | — |
| CA-07 | Testes unitários passam (CI verde) | `pytest tests/test_indicator_engine.py → PASSED` | — |
| CA-08 | Telemetria ativa (logs com timestamp + ID) | Evidência de log por iteração | — |
| CA-09 | Dados inválidos → erro explícito (não None) | Teste com dados corrompidos → `IndicatorError` raised | — |
| CA-10 | Alterações limitadas ao escopo autorizado | `git diff --stat` limitado a: `indicator_engine/`, `contracts/`, `tests/`, `governance/` | **Revisado:** escopo expandido para incluir `contracts/` e `tests/` como diretórios legítimos da MIG-1 |
| CA-11 | MarketDataSnapshot definido | `from contracts.market_data_snapshot import MarketDataSnapshot` | **NOVO** — interface mínima de entrada |

---

# 8. Evidências Obrigatórias

| # | Artefato | Formato | Responsável |
|---|----------|---------|-------------|
| EV-01 | Testes unitários passando | output pytest (CI) | AIC |
| EV-02 | Log de telemetria sample (5 iterações) | JSON / texto | AIC |
| EV-03 | Diff do PR (git diff) | PR no GitHub | AIC |
| EV-04 | Comparativo antes/depois (BUG-001 corrigido) | Tabela com valores | AIC + PSA |
| EV-05 | Snapshot do contrato final | `IndicatorContract` + `MarketDataSnapshot` | AIC |
| EV-06 | Relatório de cobertura de testes | coverage report | AIC |
| EV-07 | Parecer PSA de validação | Documento formal | PSA |
| EV-08 | Confirmação de remoção dos 8 PASS | grep output + diff | AIC |

---

# 9. Riscos

## Técnicos

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Indicadores dependem de Market Data (MIG-2) | Média | Alto | MarketDataSnapshot como interface mínima — dados reais apenas em MIG-2 |
| Mudança de chaves quebra downstream | Alta | Alto | Contrato formal + versionamento + nenhuma outra MIG ativa |
| Regressão de performance | Baixa | Médio | Benchmark antes/depois |
| Stack numérica incorreta (D-02) | Média | Médio | Decisão formal antes da implementação |

## Operacionais

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Escopo creep (começar a corrigir MIG-2/4/5) | Média | Alto | Escopo explícito: apenas indicator_engine/, contracts/, tests/ |
| Alteração de runtime acidental | Baixa | Crítico | Checklist PR obrigatório (SYNC_PROTOCOL v2.0 §4) |
| Confusão BUG-003 MIG-1 vs MIG-5 | Média | Médio | Escopo refinado neste REV-1: MIG-1=remover, MIG-5=substituir |

## Documentais

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Divergência PSA ↔ AIC | Baixa | Médio | SYNC_PROTOCOL v2.0 ativo |
| Charter desatualizado pós-implementação | Média | Baixo | Atualização obrigatória no fechamento do GATE-MIG1 |

## Governança

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Implementação sem aprovação | Baixa | Crítico | DEC-18 + restrição operacional |
| AIC altera escopo sem Conselho | Baixa | Alto | PSA audita diff do PR |

---

# 10. Estratégia de Rollback

## Gatilhos de rollback

- CI vermelho após merge que não se resolve em 24h
- Indicadores produzem resultados inconsistentes em testes
- Escopo excedido (alterações fora de `indicator_engine/`, `contracts/`, `tests/`)
- Conselho solicita reversão por qualquer motivo

## Critérios

- Rollback = `git revert` do(s) commit(s) da MIG-1
- Nenhuma outra MIG pode ter sido iniciada (sequência garante isso)

## Procedimentos

1. AIC executa `git revert` no branch main
2. CI confirma que voltou ao estado anterior (verde)
3. PSA registra rollback no SYNC_LOG
4. Conselho analisa causa e decide próximos passos
5. Nova tentativa requer Charter atualizado + nova aprovação

---

# 11. Gate MIG-1 (GATE-MIG1)

**Condições obrigatórias para declarar GATE-MIG1 FECHADO:**

| # | Condição | Verificador |
|---|----------|-------------|
| 1 | Todos os CA-01..CA-11 satisfeitos | AIC + PSA |
| 2 | Todas as evidências EV-01..EV-08 produzidas | AIC + PSA |
| 3 | PR mergeado com checklist completo | AIC |
| 4 | CI verde pós-merge | Automatizado |
| 5 | Parecer PSA positivo | PSA |
| 6 | Ratificação CFO | CFO |
| 7 | Nenhuma violação de escopo detectada | PSA (auditoria) |
| 8 | SYNC_LOG atualizado | PSA |

**Após GATE-MIG1 FECHADO → autorizado iniciar planejamento MIG-2.**

---

# 12. Entregáveis

| # | Entregável | Responsável | Destino |
|---|-----------|-------------|---------|
| 1 | `indicator_engine/` — código-fonte V6 | AIC | OMEGA-Kernel-Sovereign |
| 2 | `contracts/indicator_contract.py` | AIC | OMEGA-Kernel-Sovereign |
| 3 | `contracts/market_data_snapshot.py` | AIC | OMEGA-Kernel-Sovereign |
| 4 | `tests/test_indicator_engine.py` | AIC | OMEGA-Kernel-Sovereign |
| 5 | Log de telemetria sample | AIC | governance/ |
| 6 | Relatório de cobertura | AIC | governance/ |
| 7 | Comparativo BUG-001 antes/depois | AIC + PSA | OMEGA-PSA-AUDIT-WORKSPACE |
| 8 | Parecer PSA MIG-1 | PSA | OMEGA-PSA-AUDIT-WORKSPACE |
| 9 | SYNC-OUT AIC (MIG-1) | AIC | OMEGA-PSA-AUDIT-WORKSPACE |
| 10 | DEC de fechamento GATE-MIG1 | Conselho | Ambos os repos |

---

# 13. Aprovações Necessárias

```
PSA produz Charter REV-1 (este documento)
  ↓
AIC emite parecer sobre REV-1 (ou confirma parecer anterior)
  ↓
CFO ratifica Charter REV-1
  ↓
Conselho aprova início de implementação
  ↓
Decisões pendentes (D-02, D-03) formalizadas
  ↓
AIC implementa (escopo: indicator_engine/, contracts/, tests/)
  ↓
AIC produz evidências + abre PR
  ↓
PSA audita PR + emite parecer
  ↓
CFO ratifica fechamento
  ↓
Conselho declara GATE-MIG1 FECHADO
```

---

# 14. Definição de Chaves Canônicas (Revisada REV-1)

| Chave | Indicador | Tipo | Obrigatória | Parâmetro proposto (D-03) |
|-------|-----------|------|-------------|--------------------------|
| `rsi_14` | RSI período 14 | float (0-100) | ✅ | período=14 |
| `ema_fast` | EMA rápida | float | ✅ | período=12 |
| `ema_slow` | EMA lenta | float | ✅ | período=26 |
| `atr_14` | ATR período 14 | float (>0) | ✅ | período=14 |
| `macd_line` | MACD line | float | Opcional | fast=12, slow=26, signal=9 |
| `macd_signal` | MACD signal | float | Opcional | signal=9 |
| `volume` | Volume | int (≥0) | ✅ | — |

> **Nota REV-1:** Os parâmetros propostos são valores padrão da indústria financeira. O AIC e o Conselho devem ratificar ou ajustar antes da implementação. Os parâmetros devem ser configuráveis (não hardcoded) no Indicator Engine V6.

---

# 15. Harmonização MIGRATION_ALLOWLIST

O AIC identificou que o MIGRATION_ALLOWLIST v3.0 lista BUG-003 como "SL/TP fixos desconectados do sinal" associado à MIG-1. Análise:

| Registro atual | Problema | Correção proposta |
|---------------|----------|-------------------|
| BUG-003 → "SL/TP fixos desconectados do sinal" → MIG-1 | Título de BUG-003 mistura escopo de MIG-1 (PASS filters) com MIG-4 (SL/TP) | Separar: BUG-003 = "8 Filtros PASS Hardcoded" (MIG-1 remove, MIG-5 substitui). SL/TP fixos = BUG-006 (MIG-4). |

**Ação necessária:** Atualizar MIGRATION_ALLOWLIST para refletir o título correto de BUG-003.

> **Nota:** Esta atualização será executada pelo PSA após aprovação do Conselho, como parte da consolidação pós-Charter.

---

# 16. Restrições Operacionais Reiteradas

- ❌ Nenhuma implementação antes da aprovação deste Charter REV-1
- ❌ Nenhuma alteração fora de `indicator_engine/`, `contracts/`, `tests/` e `governance/`
- ❌ Nenhum mock de dados em código de produção
- ❌ Nenhuma dependência de Market Data Engine (MIG-2) em runtime
- ❌ Nenhuma lógica de validação de sinais (escopo MIG-5)
- ✅ Mocks permitidos **apenas** em `tests/`
- ✅ MarketDataSnapshot como interface mínima (não implementação completa)

---

**PSA (Cascade) — 2026-06-24**  
**Referência:** CFO-DIR-20260624-TASK0021 · CFO-DIRECTIVE-PSA-CHARTER-REVISION-001 · AIC-PARECER-MIG1-001 · ADR-012 · DEC-18  
**Status:** SUBMETIDO PARA REVISÃO DO CONSELHO
