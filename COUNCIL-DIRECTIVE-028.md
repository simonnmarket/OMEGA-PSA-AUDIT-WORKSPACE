# COUNCIL-DIRECTIVE-028

## REORGANIZAÇÃO METODOLÓGICA DA ETAPA 3.5

### CARTOGRAFIA INSTITUCIONAL COMO ETAPA OBRIGATÓRIA ANTES DO INVENTÁRIO TÉCNICO

**ID:** COUNCIL-DIRECTIVE-028  
**Data:** 2026-06-27  
**Emitido por:** Conselho  
**Destinatário:** PSA  
**Hierarquia:** Constituição do Programa → Diretiva do Conselho  
**Status:** OBRIGATÓRIA

---

## 1. Objeto

Esta Diretiva reorganiza metodologicamente a execução da ETAPA 3.5.

Não altera o escopo aprovado pela COUNCIL-DIRECTIVE-025 nem pela CEO-DIRECTIVE-027.

Seu objetivo é estabelecer uma sequência de trabalho que preserve o contexto arquitetural do patrimônio técnico antes da análise individual de componentes.

---

## 2. Motivação

Durante a reconstrução do programa foi identificado que análises iniciadas diretamente sobre componentes específicos aumentam significativamente o risco de interpretações parciais do sistema, perda de contexto arquitetural e reimplementações sem equivalência funcional demonstrada.

A ETAPA 3.5 passa, portanto, a ser executada em fases sucessivas de descoberta, compreensão e documentação.

---

## 3. Princípio Metodológico

Fica estabelecido o seguinte princípio permanente:

> Nenhum componente poderá ser analisado isoladamente antes que o contexto estrutural do sistema tenha sido completamente documentado.

A compreensão deverá evoluir do geral para o específico.

Nunca do específico para o geral.

---

## 4. Nova Sequência Oficial da ETAPA 3.5

A execução deverá obedecer obrigatoriamente à seguinte ordem:

### FASE 0 — Congelamento Institucional

- confirmação do modo somente leitura;
- confirmação da integridade do patrimônio técnico;
- registro das evidências de origem.

### FASE 1 — Cartografia Institucional

Objetivo: Produzir o mapa estrutural completo do OMEGA_OS_Kernel.

Utilizar como base:
- tree.txt;
- estrutura física dos diretórios;
- organização do repositório.

Entregável obrigatório: SYSTEM_MAP.md

Nenhum código deverá ser interpretado nesta fase.

### FASE 2 — Arquitetura Estrutural

Identificar:
- domínios;
- subdomínios;
- engines;
- pipelines;
- packages;
- agentes;
- serviços;
- camadas;
- interfaces.

Entregável: ARCHITECTURE_MAP.md

### FASE 3 — Mapa de Dependências

Documentar:
- quem chama quem;
- quem depende de quem;
- fluxo entre módulos;
- acoplamentos;
- pontos críticos.

Entregável: DEPENDENCY_MAP.md

### FASE 4 — Fluxo Operacional

Reconstruir documentalmente o ciclo completo do sistema.

```
entrada de dados
   ↓
processamento
   ↓
análises
   ↓
decisão
   ↓
risco
   ↓
execução
   ↓
monitoramento
   ↓
auditoria
```

Entregável: SYSTEM_FLOW_MAP.md

### FASE 5 — Inventário Técnico

Somente após aprovação das fases anteriores.

Nesta etapa inicia-se a análise individual de:
- módulos;
- classes;
- componentes;
- contratos;
- estratégias;
- engines.

Seguindo integralmente a metodologia definida pela CEO-DIRECTIVE-027.

### FASE 6 — Matriz de Paridade Funcional

Comparação entre:
```
OMEGA_OS_Kernel
   ↓
OMEGA-Kernel-Sovereign
```

Classificando:
- portado;
- equivalente;
- parcial;
- pendente;
- descartado por decisão do Conselho.

### FASE 7 — Plano de Recuperação

Somente após conclusão da matriz de paridade.

Produzir:
- prioridades;
- dependências;
- riscos;
- ordem de migração.

Nenhum desenvolvimento poderá ocorrer antes desta etapa.

---

## 5. Hierarquia Obrigatória de Análise

Toda documentação deverá seguir obrigatoriamente a seguinte hierarquia:

```
Sistema
   ↓
Domínio
   ↓
Subdomínio
   ↓
Pipeline
   ↓
Engine
   ↓
Módulo
   ↓
Classe
   ↓
Método
   ↓
Função
```

É vedada a inversão dessa sequência.

---

## 6. Novo Artefato Obrigatório

Antes de qualquer inventário técnico o PSA deverá produzir:

**SYSTEM_MAP.md**

Esse documento passa a representar oficialmente a cartografia institucional do patrimônio técnico.

Seu objetivo será permitir ao Conselho compreender a estrutura global do sistema antes da análise dos componentes individuais.

---

## 7. Utilização do tree.txt

O arquivo `tree.txt` deixa de ser apenas uma listagem de arquivos.

Passa a ser considerado evidência institucional da organização física do patrimônio técnico.

Ele deverá servir como fonte primária para construção da cartografia institucional.

---

## 8. Critério para Início da Leitura de Código

A leitura detalhada de arquivos-fonte somente poderá iniciar após:

- conclusão do SYSTEM_MAP.md;
- conclusão do ARCHITECTURE_MAP.md;
- conclusão do DEPENDENCY_MAP.md;
- conclusão do SYSTEM_FLOW_MAP.md;

e ciência formal do Conselho.

---

## 9. Comunicação Institucional

O PSA permanece atuando exclusivamente no `OMEGA-PSA-AUDIT-WORKSPACE`.

Nenhum acesso de escrita ao `OMEGA-Kernel-Sovereign` permanece autorizado.

Nenhuma modificação poderá ocorrer no `OMEGA_OS_Kernel`.

Toda análise será conduzida em modo exclusivamente leitura.

---

## 10. Resultado Esperado

Ao final da reorganização metodológica da ETAPA 3.5 o Programa deverá possuir:

- compreensão estrutural completa do patrimônio técnico;
- cartografia institucional do sistema;
- mapa das dependências;
- mapa dos fluxos operacionais;
- contexto suficiente para iniciar o inventário técnico sem perda de significado arquitetural;
- base documental para construção da Matriz de Paridade Funcional prevista na Constituição do Programa.

---

## 11. Deliberação

Esta Diretiva entra em vigor imediatamente após registro pelo PSA.

A partir deste momento, nenhuma análise individual de componentes deverá ser iniciada antes da conclusão da Cartografia Institucional prevista nesta Diretiva.

O objetivo institucional permanece inalterado: recuperar integralmente o patrimônio técnico do OMEGA_OS_Kernel com equivalência funcional demonstrável, preservando contexto arquitetural, rastreabilidade e governança em todas as etapas do Programa.

---

**Conselho**  
**2026-06-27**
