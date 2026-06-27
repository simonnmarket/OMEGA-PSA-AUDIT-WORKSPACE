# ADR-012 — Plano Mestre de Execução OMEGA Kernel Sovereign V6

**Status:** APROVADO — CEO + CFO  
**Data:** 2026-06-23  
**Decisores:** CEO + CFO — OMEGA Kernel Sovereign V6  
**Origem:** CFO-DIR-20260623-02 · CFO-RAT-20260623-03 · CFO-RATIFICATION-001  
**Referência:** DEC-15  
**Atualização:** 2026-06-24 — Taskade removido, PSA assume autoridade documental  
**Atualização:** 2026-06-27 — COUNCIL-DIRECTIVE-025: OMEGA-CONSTITUTION-001 institucionalizada; ETAPA 3.5 inserida; MIG-1/2/3 reclassificados como Gates Arquiteturais; MIG-4/5/6 suspensos
**Supersede:** ADR-009 (VOID — ID realocado para evitar colisão)  
**Nota:** ADR-009, ADR-010, ADR-011 reservados para uso futuro do Conselho.

---

## Contexto

Após a conclusão da estrutura de governança (ADR-001 a ADR-008), o Conselho identificou a necessidade de um plano único, sequencial e obrigatório que governe a construção do V6 desde a etapa documental até a autorização de operação real.

O AIC identificou colisão de ID (ADR-009 já existia) antes do merge. O Conselho ratificou a correção via CFO-RAT-20260623-03: o Plano Mestre passa a utilizar ADR-012.

Sem este plano, existe risco de:
- Execução paralela de atividades fora de sequência
- Correções sem rastreabilidade por ID
- MIGs iniciados antes de gates anteriores fechados
- Pressão para acelerar etapas sem validação formal

---

## Decisão

A partir desta data, o projeto opera sob **execução sequencial de etapas e gates formais**.

---

## Modelo de Governança

```
Conselho (CEO + CFO)
  ↓
PSA (Autoridade Documental — OMEGA-PSA-AUDIT-WORKSPACE)
  ↓
AIC (Execução Técnica — OMEGA-Kernel-Sovereign)
  ↓
GitHub V6 (Fonte Oficial de Código)
  ↓
Validação (DEMO → SHADOW)
  ↓
Operação Real
```

**Regras imutáveis:**
- PSA é a fonte oficial de governança documental
- GitHub V6 é a fonte oficial de código
- AIC executa — não decide
- Conselho aprova — não executa
- Nenhuma alteração operacional ocorre sem rastreabilidade por ID

---

## Regra CFO-03 — Foco Operacional

Fica **proibido** interromper o roadmap principal para:
- Auditorias paralelas
- Investigações do legado
- Otimizações prematuras
- Novos runtimes ou launchers
- Alterações de estratégia
- Revisões históricas

Qualquer nova descoberta → **BACKLOG** → analisada somente após etapa ativa concluída.

**Exceções autorizadas:**
- Risco financeiro · Risco jurídico · Risco de segurança · Risco de perda de dados

---

## Modelo Oficial: 6 MIGs (Ratificado CFO-RAT-20260623-03)

| MIG | Componente | Bugs Associados | Pré-condição |
|-----|-----------|-----------------|--------------|
| MIG-1 | Indicator Engine | BUG-001 · BUG-003 | GATE-0 FECHADO |
| MIG-2 | Market Data Engine | BUG-002 | GATE-MIG1 |
| MIG-3 | Position Manager | — | GATE-MIG2 |
| MIG-4 | Risk Engine | BUG-006 | GATE-MIG3 |
| MIG-5 | Signal Validation Layer | Arquitetural | GATE-MIG4 |
| MIG-6 | Execution Engine Sovereign | BUG-004 · BUG-009 · BUG-010 | GATE-MIG5 |

**Não migrar — Classificação EVIDÊNCIA FORENSE:**
- BUG-005 · BUG-007 · BUG-008

---

## Roadmap Sequencial Oficial

### ETAPA 0 — GOVERNANÇA
**Gate:** GATE-0 GOVERNANÇA  
**Tasks:** TASK-0018 · TASK-0019 · TASK-0020  
**Entregáveis:** ADRs · Registries · SYNC_PROTOCOL.md · SYNC_LOG.md  
**Status:** ✅ CONCLUÍDA (DEC-18 · CFO-RATIFICATION-002 · 2026-06-24)

### ETAPA 1 — MIG-1: Indicator Engine
**Gate:** GATE-MIG1 | **Bugs:** BUG-001 · BUG-003  
**Critério:** Nenhum indicador `None` · Chaves canônicas · CI verde  
**Status:** ✅ FECHADO (DEC-GATE-MIG1 · SIVR-0-CLOSURE-001 · 2026-06-24)

### ETAPA 2 — MIG-2: Market Data Engine
**Gate:** GATE-MIG2 | **Bug:** BUG-002  
**Proibição absoluta:** fallback sintético · dados artificiais  
**Critério:** Dados reais · Integridade confirmada · CI verde · CA-01..CA-08  
**Status:** ✅ FECHADO (DEC-GATE-MIG2 · GATE-MIG2-PARECER-PSA-001 · 2026-06-25)

### ETAPA 3 — MIG-3: Position Manager
**Gate:** GATE-MIG3 (ARQUITETURAL)  
**Critério:** Estados rastreáveis · Telemetria ativa · CI verde · CA-01..CA-08  
**Status:** ✅ FECHADO ARQUITETURAL (DEC-GATE-MIG3-001 · COUNCIL-DIRECTIVE-025 · 2026-06-27)

### ETAPA 3.5 — Inventário e Matriz de Paridade Funcional
**Gate:** Nenhum (etapa institucional)  
**Entregáveis:** OMEGA-CONSTITUTION-001 · ETAPA-3.5-PLANO · METODOLOGIA-PARIDADE-FUNCIONAL · MIGRATION-TRACEABILITY-MATRIX · CRITERIOS-GATE-FUNCIONAL  
**Critério:** Inventário completo do OMEGA_OS_Kernel · Matriz de rastreabilidade aprovada · Critérios de paridade definidos  
**Status:** 🟡 EM ANDAMENTO (COUNCIL-DIRECTIVE-025 · prazo: 14 dias)

### ETAPA 4 — MIG-4: Risk Engine
**Gate:** GATE-MIG4 | **Bug:** BUG-006  
**Critério:** SL/TP derivam do sinal · Zero parâmetros fixos desconectados · CI verde · Gate Funcional futuro  
**Status:** ⏸️ SUSPENSO até aprovação da ETAPA 3.5 (COUNCIL-DIRECTIVE-025)

### ETAPA 5 — MIG-5: Signal Validation Layer
**Gate:** GATE-MIG5 | **Escopo:** Arquitetural  
**Critério:** Validação desacoplada · Telemetria completa · CI verde · Gate Funcional futuro  
**Status:** ⏸️ SUSPENSO até aprovação da ETAPA 3.5 (COUNCIL-DIRECTIVE-025)

### ETAPA 6 — MIG-6: Execution Engine Sovereign
**Gate:** GATE-MIG6 | **Bugs:** BUG-004 · BUG-009 · BUG-010  
**Componentes:** Order Manager · Trade Mode Validation · Broker Connector · Environment Gating  
**Critério:** Caminho único de execução · DEMO/REAL segregados · CI verde · Gate Funcional futuro  
**Status:** ⏸️ SUSPENSO até aprovação da ETAPA 3.5 (COUNCIL-DIRECTIVE-025)

### ETAPA 7 — DEMO
**Gate:** GATE-DEMO | **Duração mínima:** 5 dias úteis  
**Critério:** Operação estável sem intervenção

### ETAPA 8 — SHADOW MODE
**Gate:** GATE-SHADOW | **Duração mínima:** 10 dias úteis  
**Critério:** Consistência operacional comprovada

### ETAPA 9 — GATE-REAL
> **Sem ADR específico aprovado pelo Conselho: EXECUÇÃO REAL PROIBIDA**

### ETAPA 10 — EXECUÇÃO REAL CONTROLADA
Capital reduzido · Monitoramento diário obrigatório

---

## Critérios de Parada Imediata
- Divergência PSA ↔ AIC
- Perda de rastreabilidade
- Múltiplos runtimes ou launchers
- Indicadores inválidos em produção
- Execução fora do ambiente autorizado

---

## Definição de Sucesso
MIG-1..6 aprovados · GATE-DEMO · GATE-SHADOW · GATE-REAL · Governança íntegra · Telemetria completa · Rastreabilidade ponta a ponta

---

## Referências
CFO-DIR-20260623-02 · CFO-RAT-20260623-03 · CFO-RATIFICATION-001 · ADR-001..008 · DEC-15  
GATE-0 · GATE-MIG1..6 · GATE-DEMO · GATE-SHADOW · GATE-REAL  
*Nota: Taskade removido da governança por CFO-RATIFICATION-001 (2026-06-24). PSA substitui em todos os artefatos.*
