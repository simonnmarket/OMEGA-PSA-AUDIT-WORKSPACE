# TASK-0021 — MIG-1 CHARTER: Indicator Engine

**ID:** TASK-0021  
**Componente:** MIG-1 — Indicator Engine  
**Data:** 2026-06-24  
**Emitido por:** PSA (Autoridade Documental)  
**Destinatários:** CFO · Conselho · AIC (revisão técnica)  
**Status:** SUBMETIDO PARA REVISÃO DO CONSELHO  
**Autoridade:** CFO-DIR-20260624-TASK0021

---

## Referências

- ADR-012 — Plano Mestre V6
- ADR-004 — Eliminação dos 8 Filtros PASS Hardcoded
- ADR-006 — Correção Mandatória Key Mismatch RSI
- DEC-15 — Ratificação do Plano Mestre
- DEC-18 — GATE-0 FECHADO
- MIGRATION_ALLOWLIST v3.0
- BUG_REGISTRY (BUG-001, BUG-003)
- KNOWLEDGE_MASTER_INDEX (FND-10, FND-11)
- SYNC_PROTOCOL v2.0
- CFO-RATIFICATION-002

---

# 1. Executive Summary

A MIG-1 é a primeira migração técnica do programa OMEGA Kernel Sovereign V6. Seu objetivo é reconstruir o **Indicator Engine** — componente responsável por calcular indicadores técnicos que alimentam todas as decisões de trading do sistema.

O Indicator Engine do V5.5 possui dois bugs críticos documentados (BUG-001 e BUG-003) que tornam o sistema **completamente inoperante**: o RSI key mismatch produz confiança=0.0 em 100% das iterações, resultando em HOLD eterno. Os 8 filtros PASS hardcoded mascaram falhas reais e criam falsa sensação de segurança.

Sem resolver a MIG-1, **nenhuma outra MIG produz resultado útil**, pois todas as camadas downstream dependem de indicadores válidos.

---

# 2. Objetivo da MIG-1

Construir um Indicator Engine soberano que:

1. Produza indicadores com **chaves canônicas padronizadas** (`rsi_14`, `ema_fast`, `ema_slow`, etc.)
2. **Nunca** retorne `None` para indicadores obrigatórios
3. **Elimine** os 8 filtros PASS hardcoded (ADR-004)
4. **Corrija** o key mismatch RSI (ADR-006)
5. Exponha **contrato formal** de entrada/saída
6. Garanta **telemetria** rastreável por ID em cada cálculo

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

## BUG-003 — 8 Filtros PASS Hardcoded

| Campo | Detalhe |
|-------|---------|
| **Causa raiz** | 8 filtros em `shadow_loop_v33_final.py` (linhas 1917-1937) retornam literalmente `PASS` sem avaliar nenhuma condição real. |
| **Impacto** | Falsa segurança. Nenhuma condição de risco é efetivamente verificada. Qualquer sinal — válido ou corrompido — passa sem restrição. |
| **Relação com Indicator Engine** | Os filtros operam sobre indicadores. Se os filtros são fake, o Indicator Engine não tem camada de proteção contra dados inválidos. A MIG-1 deve garantir que indicadores sejam **validados de forma real**. |
| **Mitigação proposta** | Remover os 8 filtros PASS. Substituir por avaliação real baseada em indicadores canônicos (ou remover se redundantes com a Camada 5 — Signal Validation). |
| **Finding:** | FND-10 |
| **ADR:** | ADR-004 |

---

## Bugs NÃO resolvidos pela MIG-1

| Bug | Razão | MIG responsável |
|-----|-------|-----------------|
| BUG-002 | Market Data — escopo MIG-2 | MIG-2 |
| BUG-004 | Múltiplos launchers — escopo MIG-6 | MIG-6 |
| BUG-006 | Risk Engine — escopo MIG-4 | MIG-4 |

---

# 4. Escopo Incluído

| Item | Descrição |
|------|-----------|
| Padronização de chaves | Definir e implementar dicionário canônico de indicadores |
| Eliminação de `None` | Nenhum indicador pode retornar `None` silenciosamente |
| Remoção dos 8 PASS | Eliminar filtros hardcoded (ADR-004) |
| Correção key mismatch | `rsi_14` como chave única e canônica (ADR-006) |
| Contrato formal | `IndicatorContract` com entrada/saída tipadas |
| Interface pública | API clara: `calculate(market_data) → IndicatorResult` |
| Testes unitários | Cobertura de todos os indicadores com dados válidos e inválidos |
| Telemetria | Cada cálculo registrado com timestamp + indicator_id + valor |
| Documentação | Especificação técnica do componente |

---

# 5. Escopo Excluído

| Item | Razão | MIG responsável |
|------|-------|-----------------|
| Market Data Engine | Camada de dados separada | MIG-2 |
| Position Manager | Gerenciamento de posição | MIG-3 |
| Risk Engine | Cálculo SL/TP | MIG-4 |
| Signal Validation | Camada 5 arquitetural | MIG-5 |
| Execution Engine | Envio de ordens | MIG-6 |
| Runtime Engine | Launcher/runtime | Não MIG (já definido) |
| Deployment | Deploy do sistema | Pós-GATE-MIG6 |
| Produção | Operação real | GATE-REAL |
| Gestão de ordens | Order Manager | MIG-6 |
| Estratégia | Lógica de decisão | Componente nativo V6 |

---

# 6. Dependências

## Técnicas
| Dependência | Status | Nota |
|-------------|--------|------|
| GATE-0 GOVERNANÇA FECHADO | ✅ Satisfeita | DEC-18 · CFO-RATIFICATION-002 |
| Estrutura de diretórios V6 | ✅ Satisfeita | TASK-0001 (scaffold) |
| CI ativo (ruff + pytest) | ✅ Satisfeita | TASK-0002 |
| Definição de chaves canônicas | ⏳ Pendente | Será definida no Charter (este doc) |

## Documentais
| Dependência | Status |
|-------------|--------|
| ADR-004 (eliminar 8 PASS) | ✅ Aprovada |
| ADR-006 (key mismatch RSI) | ✅ Aprovada |
| ADR-012 (Plano Mestre) | ✅ Consolidada |
| MIGRATION_ALLOWLIST | ✅ v3.0 |

## Operacionais
| Dependência | Status |
|-------------|--------|
| Aprovação deste Charter pelo Conselho | ⏳ Pendente |
| Parecer técnico do AIC | ⏳ Pendente |
| Ratificação CFO | ⏳ Pendente |

---

# 7. Critérios de Aceite

Todos os critérios são **mensuráveis e binários** (SIM/NÃO):

| # | Critério | Métrica |
|---|----------|---------|
| CA-01 | Nenhum indicador retorna `None` | `assert all(v is not None for v in result.values())` |
| CA-02 | Chave `rsi_14` presente no output | `assert "rsi_14" in result` |
| CA-03 | Chave `ema_fast` presente no output | `assert "ema_fast" in result` |
| CA-04 | Chave `ema_slow` presente no output | `assert "ema_slow" in result` |
| CA-05 | Zero filtros PASS hardcoded no código | `grep -r "PASS" indicator_engine/ == 0 results` |
| CA-06 | Contrato `IndicatorContract` definido e importável | `from contracts import IndicatorContract` |
| CA-07 | Testes unitários passam (CI verde) | `pytest tests/test_indicator_engine.py → PASSED` |
| CA-08 | Telemetria ativa (logs com timestamp + ID) | Evidência de log por iteração |
| CA-09 | Dados inválidos → erro explícito (não None) | Teste com dados corrompidos → `IndicatorError` raised |
| CA-10 | Nenhuma alteração fora de `indicator_engine/` | `git diff --stat` limitado ao diretório |

---

# 8. Evidências Obrigatórias

| # | Artefato | Formato | Responsável |
|---|----------|---------|-------------|
| EV-01 | Testes unitários passando | output pytest (CI) | AIC |
| EV-02 | Log de telemetria sample (5 iterações) | JSON / texto | AIC |
| EV-03 | Diff do PR (git diff) | PR no GitHub | AIC |
| EV-04 | Comparativo antes/depois (BUG-001 corrigido) | Tabela com valores | AIC + PSA |
| EV-05 | Snapshot do contrato final | `IndicatorContract` completo | AIC |
| EV-06 | Relatório de cobertura de testes | coverage report | AIC |
| EV-07 | Parecer PSA de validação | Documento formal | PSA |

---

# 9. Riscos

## Técnicos

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Indicadores dependem de Market Data (MIG-2) | Média | Alto | Usar dados mock **apenas em testes** — nunca em produção |
| Mudança de chaves quebra downstream | Alta | Alto | Contrato formal + versionamento |
| Regressão de performance | Baixa | Médio | Benchmark antes/depois |

## Operacionais

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Escopo creep (começar a corrigir MIG-2/4) | Média | Alto | Restrição explícita: apenas `indicator_engine/` |
| Alteração de runtime acidental | Baixa | Crítico | Checklist PR obrigatório (SYNC_PROTOCOL §4) |

## Documentais

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Divergência PSA ↔ AIC | Baixa | Médio | SYNC_PROTOCOL v2.0 ativo |
| Charter desatualizado pós-implementação | Média | Baixo | Atualização obrigatória no fechamento do GATE-MIG1 |

## Governança

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Implementação iniciada sem aprovação | Baixa | Crítico | DEC-18 + restrição operacional registrada |
| AIC altera escopo sem Conselho | Baixa | Alto | PSA audita diff do PR |

---

# 10. Estratégia de Rollback

## Gatilhos de rollback

- CI vermelho após merge que não se resolve em 24h
- Indicadores produzem resultados inconsistentes em testes
- Escopo excedido (alterações fora de `indicator_engine/`)
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
| 1 | Todos os CA-01..CA-10 satisfeitos | AIC + PSA |
| 2 | Todas as evidências EV-01..EV-07 produzidas | AIC + PSA |
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
| 3 | `tests/test_indicator_engine.py` | AIC | OMEGA-Kernel-Sovereign |
| 4 | Log de telemetria sample | AIC | governance/ |
| 5 | Relatório de cobertura | AIC | governance/ |
| 6 | Comparativo BUG-001 antes/depois | AIC + PSA | OMEGA-PSA-AUDIT-WORKSPACE |
| 7 | Parecer PSA MIG-1 | PSA | OMEGA-PSA-AUDIT-WORKSPACE |
| 8 | SYNC-OUT AIC (MIG-1) | AIC | OMEGA-PSA-AUDIT-WORKSPACE |
| 9 | DEC de fechamento GATE-MIG1 | Conselho | Ambos os repos |

---

# 13. Aprovações Necessárias

```
PSA produz Charter (TASK-0021)
  ↓
AIC emite parecer técnico
  ↓
CFO ratifica Charter
  ↓
Conselho aprova início de implementação
  ↓
AIC implementa (escopo indicator_engine/ apenas)
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

# 14. Definição de Chaves Canônicas (Proposta)

Para eliminar definitivamente o key mismatch, propõe-se o seguinte dicionário canônico:

| Chave | Indicador | Tipo | Obrigatória |
|-------|-----------|------|-------------|
| `rsi_14` | RSI período 14 | float (0-100) | ✅ |
| `ema_fast` | EMA rápida | float | ✅ |
| `ema_slow` | EMA lenta | float | ✅ |
| `atr_14` | ATR período 14 | float (>0) | ✅ |
| `macd_line` | MACD line | float | Opcional |
| `macd_signal` | MACD signal | float | Opcional |
| `volume` | Volume | int (≥0) | ✅ |

> **Nota:** Esta é uma proposta do PSA. O AIC deve validar se cobre os indicadores necessários para a estratégia V6 e propor adições/alterações no parecer técnico.

---

# 15. Restrições Operacionais Reiteradas

- ❌ Nenhuma implementação antes da aprovação deste Charter
- ❌ Nenhuma alteração fora de `indicator_engine/` e `contracts/`
- ❌ Nenhum mock de dados em código de produção
- ❌ Nenhuma dependência de Market Data Engine (MIG-2) em runtime
- ✅ Mocks permitidos **apenas** em `tests/`

---

**PSA (Cascade) — 2026-06-24**  
**Referência:** CFO-DIR-20260624-TASK0021 · ADR-012 · DEC-18  
**Status:** SUBMETIDO PARA REVISÃO DO CONSELHO
