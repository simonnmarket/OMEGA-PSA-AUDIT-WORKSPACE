# PSA-ANALYSIS-COUNCIL-DIRECTIVE-029-REVISAO-CEO

## Análise Crítica da Revisão do COUNCIL-DIRECTIVE-029 e Recomendação de Convergência

**ID:** PSA-ANALYSIS-COUNCIL-DIRECTIVE-029-REVISAO-CEO  
**Data:** 2026-06-27  
**Emissor:** Principal Solution Architect PSA  
**Referência:** COUNCIL-DIRECTIVE-029 (vigente no PSA workspace) · COUNCIL-DIRECTIVE-029-REVISAO-CEO.md · COUNCIL-DIRECTIVE-028 · OMEGA-CONSTITUTION-001 · ETAPA-3.5-PLANO.md  
**Status:** ⚠️ ANÁLISE CRÍTICA — CONFLITO DE VERSÕES IDENTIFICADO

---

## 1. Resumo Executivo

Foi recebida uma nova versão do `COUNCIL-DIRECTIVE-029` com título e escopo distintos da versão já vigente no `OMEGA-PSA-AUDIT-WORKSPACE`.

| Versão | Título | Status no PSA workspace |
|--------|--------|---------------------------|
| COUNCIL-DIRECTIVE-029 (vigente) | Metodologia obrigatória para FASE 2 — ARCHITECTURE MAP | ✅ VIGENTE após `SYNC-VALIDATION-PSA-006` |
| COUNCIL-DIRECTIVE-029-REVISAO-CEO | Autorização para execução da ETAPA 3.5 — Inventário Institucional | ⏳ Recebida para análise; **não incorporada** |

Este parecer identifica **conflitos substantivos** entre as versões e recomenda que o Conselho delimite qual delas é a autoridade vigente antes que a FASE 2 seja executada.

---

## 2. Pontos de Convergência (positivos)

Ambas as versões concordam com os pontos fundamentais:

- O PSA deve executar inventário em modo **READ ONLY**.
- Nenhuma implementação de software está autorizada.
- O `OMEGA_OS_Kernel` é a fonte oficial e Patrimônio Técnico Congelado.
- MIG-4, MIG-5, MIG-6 e TASK-0024 permanecem suspensos.
- A comunicação institucional segue o fluxo Conselho → PSA → Conselho → AIC → Conselho.
- `CEO-DIRECTIVE-026` permanece vigente.
- O objetivo final é produzir conhecimento técnico comprovado para a Matriz de Paridade Funcional.

A recomendação do CEO (foco em evidências técnicas, redução de novos documentos de governança) é **tecnicamente sólida e institucionalmente desejável**.

---

## 3. Conflitos Identificados

### 3.1 Conflito de escopo e título

- Versão vigente: diretiva específica da **FASE 2** (`ARCHITECTURE MAP`).
- Nova versão: diretiva geral de **autorização para toda a ETAPA 3.5**.

**Impacto:** Se a nova versão prevalecer, ela pode ser interpretada como revogando a metodologia detalhada da FASE 2, mesmo que isso não seja a intenção.

### 3.2 Conflito de sequência de fases

| Versão vigente (COUNCIL-DIRECTIVE-028) | Nova versão |
|----------------------------------------|-------------|
| FASE 0 — Congelamento Institucional | (não presente) |
| FASE 1 — Cartografia Institucional (`SYSTEM_MAP`) | FASE 1 — `SYSTEM MAP` (concluída) |
| FASE 2 — Arquitetura Estrutural (`ARCHITECTURE_MAP`) | FASE 2 — `ARCHITECTURE MAP` |
| FASE 3 — Mapa de Dependências (`DEPENDENCY_MAP`) | FASE 3 — `FUNCTIONAL MAP` |
| FASE 4 — Fluxo Operacional (`SYSTEM_FLOW_MAP`) | FASE 4 — `DECISION MAP` |
| FASE 5 — Inventário Técnico | FASE 5 — `PROCESS MAP` |
| FASE 6 — Matriz de Paridade Funcional | FASE 6 — `PARITY MATRIX` |
| FASE 7 — Plano de Recuperação | FASE 7 — `EXECUTIVE REPORT` |

**Impacto:** As fases 3, 4, 5, 6 e 7 possuem nomes, objetivos e entregáveis diferentes. Isso gera ambiguidade sobre qual sequência deve ser executada.

### 3.3 Conflito de entregáveis

- Versão vigente: `ARCHITECTURE_MAP.md`, `ARCHITECTURE_INDEX.md`, `EVIDENCE_INDEX.md` (FASE 2).
- Nova versão: entrega por fase de "documento técnico, evidências, estatísticas, limitações, riscos e recomendações", sem especificação de nomes de artefatos.

**Impacto:** A versão vigente é mais operacional. A nova versão é mais genérica.

### 3.4 Conflito de classificações na Matriz de Paridade

- Versão anterior (`COUNCIL-PROPOSAL-002`): Portado, Reimplementado, Equivalente, Parcialmente equivalente, Não equivalente, Obsoleto, Experimental, Descontinuado por decisão formal.
- Nova versão: PORTAR, REIMPLEMENTAR, MANTER, DESCARTAR, FORENSE, INDEFINIDO.

**Impacto:** Classificações distintas para o mesmo artefato. Isso afeta a consistência do `DECISION_REGISTRY` e da metodologia.

### 3.5 Conflito de hierarquia documental

- A versão vigente foi aprovada e registrada no `DECISION_REGISTRY` como `✅ VIGENTE`.
- A nova versão utiliza o mesmo ID (`COUNCIL-DIRECTIVE-029`), o que tecnicamente implica revisão ou revogação.

**Impacto:** Se ambas coexistirem com o mesmo ID, o `DECISION_REGISTRY` ficará inconsistente e a execução poderá ser contestada.

### 3.6 Conflito sobre o papel do PSA

- A versão vigente delega ao PSA a implementação documental de diretivas.
- A recomendação do CEO diz que "o PSA não deve mais produzir novas diretivas de governança por iniciativa própria".

**Impacto:** A recomendação é válida, mas deve ser formalizada como instrução, não apenas como nota anexa. Caso contrário, o PSA pode não ter clareza sobre quais documentos ainda pode produzir (ex.: análises, pareceres de validação, relatórios técnicos).

---

## 4. Análise Crítica da Nova Versão

### 4.1 Pontos Fortes

- **Clareza sobre a fonte única:** reafirma `OMEGA_OS_Kernel` como Patrimônio Técnico Congelado.
- **Boa lista de levantamentos:** cobre estrutural, arquitetural, funcional, operacional, módulos, agentes, pipelines, estratégias, serviços, contratos, integrações, motores matemáticos, decisão, risco, execução e inteligência.
- **Critério de qualidade detalhado:** exige responsabilidade, entradas, saídas, dependências, regras, interações e posição na arquitetura.
- **Critério de encerramento objetivo:** as 8 perguntas são claras e acionáveis.
- **Restrições permanentes:** reforça a suspensão de MIGs.
- **Recomendação do CEO:** direciona o foco para evidências técnicas, que é o objetivo central da ETAPA 3.5.

### 4.2 Pontos Fracos

- **Imprecisão na sequência:** FASE 3-7 da nova versão não estão alinhadas com a COUNCIL-DIRECTIVE-028, que ainda está vigente.
- **Ausência de metodologia da FASE 2:** a versão vigente detalha a metodologia `ARCHITECTURE MAP`; a nova versão apenas o nomeia sem especificar regras de evidência, neutralidade ou separação descrição/análise.
- **Classificações conflitantes:** a Matriz de Paridade Funcional precisa de uma única taxonomia.
- **Risco de duplicidade de ID:** usar `COUNCIL-DIRECTIVE-029` para dois escopos diferentes invalida a rastreabilidade.
- **FASE 0 omitida:** a COUNCIL-DIRECTIVE-028 inclui FASE 0 (Congelamento Institucional); a nova versão começa em FASE 1.
- **Entregáveis não nomeados:** a nova versão não nomeia os artefatos, dificultando a revisão institucional.

---

## 5. Recomendações do PSA

### 5.1 Recomendação principal

**O Conselho deve deliberar sobre a autoridade da versão vigente versus a nova versão.**

Sugere-se uma das três alternativas:

| Alternativa | Descrição |
|-------------|-----------|
| **A** — Manter a versão vigente como COUNCIL-DIRECTIVE-029 e rejeitar a nova versão como rascunho. | Preserva a metodologia detalhada da FASE 2 e a sequência da COUNCIL-DIRECTIVE-028. |
| **B** — Revogar a versão vigente e substituir pela nova versão, ajustando-a para alinhar com COUNCIL-DIRECTIVE-028. | Requer nova validação e reincorporação. |
| **C** — Dividir: a nova versão vira COUNCIL-DIRECTIVE-030 (autorização geral da ETAPA 3.5), mantendo COUNCIL-DIRECTIVE-029 como metodologia da FASE 2. | Esta é a opção institucionalmente mais limpa. |

### 5.2 Recomendação operacional

**Recomenda-se a Alternativa C**, pois:

- Evita conflito de ID.
- Preserva a metodologia já validada da FASE 2.
- Mantém a autorização geral da ETAPA 3.5 como documento separado.
- Permite que o PSA siga a sequência da COUNCIL-DIRECTIVE-028 sem ambiguidade.

### 5.3 Recomendação sobre a recomendação do CEO

A recomendação do CEO de foco em evidências técnicas deve ser **incorporada como nota oficial** em um documento apropriado (ex.: `COUNCIL-DIRECTIVE-030` ou `CEO-DIRECTIVE` operacional), com o seguinte alcance:

- O PSA **não** criará novas diretivas de governança por iniciativa própria.
- O PSA **continuará** produzindo:
  - documentos técnicos de inventário;
  - análises críticas solicitadas;
  - pareceres de validação (`SYNC-VALIDATION-PSA-NNN`);
  - relatórios de progresso ao Conselho.
- Novas diretivas de governança só serão criadas por solicitação explícita do Conselho ou do CEO.

### 5.4 Recomendação sobre classificações

Adotar uma taxonomia única para a Matriz de Paridade Funcional. Sugestão de síntese entre as versões:

| Classificação | Origem |
|---------------|--------|
| Portado | Ambas |
| Reimplementado / Reimplementar | Ambas |
| Equivalente | COUNCIL-PROPOSAL-002 |
| Parcialmente equivalente | COUNCIL-PROPOSAL-002 |
| Não equivalente | COUNCIL-PROPOSAL-002 |
| Mantido (sem migração necessária) | Nova versão |
| Descartado / Descartar | Ambas |
| Forense | Nova versão |
| Obsoleto | COUNCIL-PROPOSAL-002 |
| Experimental | COUNCIL-PROPOSAL-002 |
| Indefinido | Nova versão |
| Descontinuado por decisão formal | COUNCIL-PROPOSAL-002 |

---

## 6. Parecer Preliminar

> **O PSA emite parecer NEUTRO-CONDIÇIONAL sobre a COUNCIL-DIRECTIVE-029-REVISAO-CEO.**

O documento é tecnicamente valioso, mas **não pode ser incorporado como substituto da COUNCIL-DIRECTIVE-029 vigente** sem deliberação do Conselho, devido aos conflitos de ID, fases e classificações.

A FASE 2 (`ARCHITECTURE_MAP`) não deve ser iniciada até que a autoridade da versão vigente seja confirmada.

---

## 7. Ações Solicitadas ao Conselho

1. **Deliberar** se a versão vigente (`COUNCIL-DIRECTIVE-029`) permanece, se será revogada ou se a nova versão receberá novo ID (`COUNCIL-DIRECTIVE-030`).
2. **Definir** a sequência oficial de fases: a da `COUNCIL-DIRECTIVE-028` (8 fases) ou a da nova versão (7 fases).
3. **Uniformizar** a taxonomia da Matriz de Paridade Funcional.
4. **Formalizar** a recomendação do CEO sobre foco em evidências técnicas em diretiva executiva apropriada.
5. **Registrar** a deliberação no `DECISION_REGISTRY.md`.

---

## 8. Referências

- `COUNCIL-DIRECTIVE-029.md` (vigente no PSA workspace)
- `COUNCIL-DIRECTIVE-029-REVISAO-CEO.md` (nova versão recebida)
- `COUNCIL-DIRECTIVE-028.md`
- `OMEGA-CONSTITUTION-001.md`
- `ETAPA-3.5-PLANO.md`
- `COUNCIL-PROPOSAL-002.md`
- `SYNC-VALIDATION-PSA-006.md`

---

**Principal Solution Architect PSA**  
**2026-06-27**
