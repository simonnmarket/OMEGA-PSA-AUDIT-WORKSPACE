# MIGRATION TRACEABILITY MATRIX

**ID:** MIGRATION-TRACEABILITY-MATRIX  
**Data:** 2026-06-27  
**Status:** EM ELABORAÇÃO  
**Responsável:** Principal Solution Architect PSA  
**Referência:** OMEGA-CONSTITUTION-001 · ETAPA-3.5 · METODOLOGIA-PARIDADE-FUNCIONAL

---

## 1. Objetivo

Mapear cada componente do OMEGA_OS_Kernel para o OMEGA-Kernel-Sovereign, indicando:

- identificação no legado;
- responsabilidade funcional;
- dependências;
- estado atual;
- destino no Sovereign;
- decisão institucional.

---

## 2. Estrutura da Matriz

| ID | Componente Legado | Caminho Legado | Função | Dependências | Criticidade | Classificação | Destino MIG | Status Sovereign | Proprietário | Decisão |
|----|---------------------|----------------|--------|--------------|-------------|---------------|-------------|------------------|--------------|---------|
| C-001 | Runtime Launcher | `runtime/launcher.py` | Inicialização segura | Kernel, Config | Alta | PORTAR | MIG-0 | Não iniciado | AIC | Aguardar |
| C-002 | Indicator Engine | `engines/indicators.py` | Cálculo de indicadores | Market Data | Alta | PORTAR | MIG-1 | Parcial (RSI/EMA) | AIC | Validar arquitetura; aguardar paridade |
| C-003 | Kalman Filter | `engines/kalman.py` | Filtro adaptativo | Indicator Engine | Alta | PORTAR | MIG-1 | Não iniciado | AIC | Pendente |
| C-004 | Confluence Engine | `engines/confluence.py` | Agregação de sinais | Multi-factor | Alta | PORTAR | MIG-1 | Não iniciado | AIC | Pendente |
| C-005 | Multi-Factor Model | `engines/multifactor.py` | Modelo de fatores | Dados macro | Alta | PORTAR | MIG-1 | Não iniciado | AIC | Pendente |
| C-006 | Market Data Engine | `market_data/engine.py` | Feed de dados | Provider | Alta | PORTAR | MIG-2 | Parcial | AIC | Validar arquitetura; aguardar paridade |
| C-007 | Position Manager | `position/manager.py` | Estado de posições | Execution, Risk | Alta | PORTAR | MIG-3 | Parcial | AIC | Validar arquitetura; aguardar paridade |
| C-008 | Risk Engine | `risk/engine.py` | Gestão de risco | Position, Market | Crítica | PORTAR | MIG-4 | Não iniciado | AIC | Suspenso até ETAPA 3.5 |
| C-009 | Strategy Engine | `strategy/engine.py` | Geração de sinais | Indicators, Risk | Crítica | PORTAR | MIG-5 | Não iniciado | AIC | Suspenso até ETAPA 3.5 |
| C-010 | Execution Engine | `execution/engine.py` | Envio de ordens | Position, Broker | Crítica | PORTAR | MIG-6 | Não iniciado | AIC | Suspenso até ETAPA 3.5 |
| C-011 | Telemetry | `telemetry/` | Telemetria e audit | Todos | Média | PORTAR | MIG-6 | Não iniciado | AIC | Pendente |
| C-012 | Config Manager | `config/manager.py` | Configuração operacional | Runtime | Média | PORTAR | MIG-0 | Não iniciado | AIC | Pendente |

---

## 3. Classificações Possíveis

- **PORTAR** — migrar funcionalmente para Sovereign.
- **REESCREVER** — reconstruir com equivalência demonstrada.
- **DESCARTAR** — eliminar com justificativa aprovada.
- **REFERÊNCIA FORENSE** — manter apenas como documentação.

---

## 4. Regras de Preenchimento

1. Todo componente do legado deve ter um ID único.
2. A classificação deve ser justificada tecnicamente.
3. Dependências devem ser listadas por ID.
4. O destino MIG deve ser consistente com ADR-012.
5. Status deve ser atualizado semanalmente.
6. Decisões institucionais devem ser rastreáveis a DECISION_REGISTRY.

---

## 5. Estado Atual

A matriz está em elaboração. A primeira versão completa será entregue ao final da ETAPA 3.5.

---

## 6. Assinatura

**Principal Solution Architect PSA**  
**2026-06-27**
