# PSA-ANALYSIS-COUNCIL-DIRECTIVE-029

## Análise Crítica e Sugestões do Principal Solution Architect PSA

**ID:** PSA-ANALYSIS-COUNCIL-DIRECTIVE-029  
**Data:** 2026-06-27  
**Referência:** COUNCIL-DIRECTIVE-029 · OMEGA-CONSTITUTION-001 · COUNCIL-DIRECTIVE-025 · COUNCIL-DIRECTIVE-028 · CEO-DIRECTIVE-026 · CEO-DIRECTIVE-027  
**Status:** PARECER FAVORÁVEL — com observações críticas e sugestões

---

## 1. Resumo Executivo

A COUNCIL-DIRECTIVE-029 estabelece a metodologia obrigatória para a FASE 2 da ETAPA 3.5 (ARCHITECTURE MAP). Sua estrutura é tecnicamente robusta, institucionalmente coerente e metodologicamente necessária.

Este parecer emite análise **favorável à aprovação e incorporação**, com críticas construtivas e sugestões operacionais destinadas a evitar ambiguidades na execução.

---

## 2. Análise Crítica por Seção

### 2.1 Objeto (Seção 1)

**Crítica:** Clara e correta. A diretiva limita-se a metodologia, excluindo explicitamente implementação, alteração arquitetural, migração ou criação de componentes.

**Sugestão:** Manter essa redação sem alterações. A clareza da proibição é um ponto forte.

### 2.2 Contexto (Seção 2)

**Crítica:** Reconhece corretamente a insuficiência do `SYSTEM_MAP.md` para decisões de migração. A transição estrutural → arquitetural é a progressão lógica da COUNCIL-DIRECTIVE-028.

**Sugestão:** O `SYSTEM_MAP.md` deveria ser citado explicitamente como pré-requisito validado, reforçando a sequência de fases.

### 2.3 Objetivo da FASE 2 (Seção 3)

**Crítica:** A redação "A FASE 2 possui apenas um objetivo" é forte e necessária. A lista de exclusões é abrangente.

**Sugestão:** Aclarar que "validar equivalência funcional" também não se aplica à comparação com OMEGA-Kernel-Sovereign, já que ainda estamos na fase descritiva do legado. Isso evitará confusão com a FASE 6.

### 2.4 Natureza da documentação (Seção 4)

**Crítica:** A exigência de descrição estritamente descritiva é fundamental. A proibição de interpretações e inferências é um controle de qualidade importante.

**Sugestão:** Adicionar uma nota operacional sobre o limite entre descrição e interpretação. Por exemplo, afirmar "o módulo X é chamado pelo módulo Y" é descrição se baseada em importação visível; afirmar "o módulo X é responsável por risco" é interpretação se não houver comentário ou documentação explícita.

### 2.5 Evidência obrigatória (Seção 5)

**Crítica:** A lista de 11 campos mínimos é excelente e obrigatória. Garante rastreabilidade.

**Sugestão:** Criar uma seção complementar na CEO-DIRECTIVE operacional definindo o formato de registro de cada campo (ex.: tabela, JSON, YAML) para garantir consistência entre `ARCHITECTURE_MAP.md`, `ARCHITECTURE_INDEX.md` e `EVIDENCE_INDEX.md`.

### 2.6 Proibições (Seção 6)

**Crítica:** Abrangente e necessária. Reforça o isolamento de workspaces.

**Observação:** A proibição de "modificar qualquer arquivo do OMEGA-Kernel-Sovereign" é redundante dado o STANDBY do AIC, mas reforça a barreira institucional.

### 2.7 Princípio da Evidência Primária (Seção 7)

**Crítica:** Lista de evidências aceitáveis é adequada.

**Sugestão:** Diferenciar evidência primária de evidência secundária. Código-fonte e contratos são primárias; comentários técnicos e histórico institucional são secundárias. A diretiva poderia exigir que, quando a evidência for secundária, isso seja explicitamente registrado.

### 2.8 Princípio da Neutralidade (Seção 8)

**Crítica:** Essencial para a qualidade do ARCHITECTURE_MAP.

**Sugestão:** Incluir exemplo de linguagem neutra: substituir "módulo mal projetado" por "módulo com N dependências circulares identificadas"; substituir "implementação frágil" por "módulo sem tratamento de exceção visível em seus métodos públicos".

### 2.9 Ausência de evidência (Seção 9)

**Crítica:** Um dos princípios mais importantes. Evita conclusões prematuras.

**Sugestão:** Elevar este princípio a cláusula constitucional. Ele é tão fundamental quanto o Princípio 3.7 (Gate ≠ equivalência funcional).

### 2.10 Separação entre descrição e análise (Seção 10)

**Crítica:** A distinção é clara e necessária. A nomenclatura `FUNCTIONAL_MAP` é introduzida aqui como fase futura, o que é consistente.

**Sugestão:** Aclarar que `PARITY_MATRIX` também é descritiva, embora comparativa. Não contém análise nem recomendação, apenas mapeamento de correspondências.

### 2.11 Critério de conclusão (Seção 11)

**Crítica:** Os 4 critérios são mensuráveis.

**Sugestão:** Adicionar critério de cobertura: "todos os componentes listados no `SYSTEM_MAP.md` como potencialmente arquiteturais foram avaliados ou explicitamente postergados com justificativa".

### 2.12 Entregáveis (Seção 12)

**Crítica:** Os 3 entregáveis são bem definidos.

**Sugestão:** Definir brevemente o propósito de cada um:

- `ARCHITECTURE_MAP.md`: documento descritivo principal;
- `ARCHITECTURE_INDEX.md`: índice de componentes com metadados estruturados;
- `EVIDENCE_INDEX.md`: referências cruzadas entre componentes e evidências primárias.

### 2.13 Próxima etapa (Seção 13)

**Crítica:** Condiciona corretamente a FASE 3 à aprovação da FASE 2.

**Sugestão:** Nenhuma.

### 2.14 Deliberação (Seção 14)

**Crítica:** A integração permanente à Constituição é adequada. Os 5 princípios são memoráveis e alinhados.

**Sugestão:** Considerar adicionar estes princípios como cláusula constitucional 3.9 (ou 3.10), formalizando a separação descrição/análise e o princípio da evidência primária.

---

## 3. Alinhamento com Governança Vigente

| Documento | Alinhamento | Observação |
|-----------|-------------|------------|
| `OMEGA-CONSTITUTION-001` | Total | Deve ser atualizada com referência e novo princípio constitucional. |
| `COUNCIL-DIRECTIVE-025` | Total | Reforça a ETAPA 3.5. |
| `COUNCIL-DIRECTIVE-028` | Total | FASE 2 já prevista; esta diretiva detalha a metodologia. |
| `CEO-DIRECTIVE-026` | Total | Preservação do patrimônio técnico e isolamento. |
| `CEO-DIRECTIVE-027` | Total | Recuperação com paridade funcional. |
| `SYSTEM_MAP.md` | Pré-requisito | FASE 1 concluída; FASE 2 pode iniciar. |

---

## 4. Riscos Identificados

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| Confusão entre descrição e interpretação | Média | Alto | Exemplos de linguagem neutra na CEO-DIRECTIVE. |
| Registro inconsistente dos 11 campos mínimos | Média | Médio | Template estruturado em `ARCHITECTURE_INDEX.md`. |
| Pressão para iniciar FASE 3 antes da aprovação | Baixa | Alto | Bloqueio institucional no DECISION_REGISTRY. |
| Uso de evidências secundárias sem classificação | Média | Médio | Campo obrigatório "tipo de evidência" no índice. |
| Aumento de escopo além do descritivo | Média | Alto | Revisão formal do Conselho antes de aprovação. |

---

## 5. Sugestões para Incorporação Constitucional

Recomenda-se a adição de um novo princípio constitucional:

### 3.9 Separação entre descrição e análise

> Durante as fases de inventário e cartografia, toda documentação será estritamente descritiva. Análises, recomendações, propostas de migração e decisões de descarte só poderão ser produzidas após aprovação formal do Conselho.

### 3.10 Princípio da evidência primária

> Toda afirmação sobre um componente do patrimônio técnico deverá estar vinculada a evidência primária rastreável. Ausência de evidência não constitui evidência de ausência.

---

## 6. Recomendações de Execução

1. **Aprovar e incorporar** a COUNCIL-DIRECTIVE-029 à Constituição.
2. **Atualizar** `DECISION_REGISTRY.md`, `ADR-012_PLANO_MESTRE.md` e `ETAPA-3.5-PLANO.md`.
3. **Emitir** `SYNC-VALIDATION-PSA-006` confirmando a incorporação.
4. **Preparar templates** para `ARCHITECTURE_MAP.md`, `ARCHITECTURE_INDEX.md` e `EVIDENCE_INDEX.md`.
5. **Iniciar FASE 2** somente após a validação formal.
6. **Manter AIC em STANDBY** até aprovação da FASE 2.

---

## 7. Parecer Final

> **O Principal Solution Architect PSA emite parecer FAVORÁVEL à incorporação integral da COUNCIL-DIRECTIVE-029.**

A diretiva é metodologicamente correta, institucionalmente coerente e estrategicamente necessária. As observações e sugestões deste parecer visam aprimorar a operacionalização, não contestar a intenção do Conselho.

---

## 8. Referências

- `COUNCIL-DIRECTIVE-029.md`
- `OMEGA-CONSTITUTION-001.md`
- `COUNCIL-DIRECTIVE-028.md`
- `CEO-DIRECTIVE-027.md`
- `CEO-DIRECTIVE-026.md`
- `SYSTEM_MAP.md`

---

**Principal Solution Architect PSA**  
**2026-06-27**
