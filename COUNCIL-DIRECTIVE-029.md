# COUNCIL-DIRECTIVE-029

**ID:** COUNCIL-DIRECTIVE-029  
**Data:** 2026-06-27  
**Emitido por:** Conselho OMEGA  
**Destinatário:** PSA  
**Referência:** OMEGA-CONSTITUTION-001 · COUNCIL-DIRECTIVE-025 · CEO-DIRECTIVE-026 · CEO-DIRECTIVE-027 · COUNCIL-DIRECTIVE-028  
**Status:** APROVADO — METODOLOGIA OBRIGATÓRIA PARA A FASE 2 (ARCHITECTURE MAP)

---

## 1. Objeto

Esta Diretiva estabelece a metodologia institucional obrigatória para execução da FASE 2 da ETAPA 3.5 — **ARCHITECTURE MAP**.

Esta Diretiva não autoriza qualquer implementação, alteração arquitetural, migração de código ou criação de novos componentes.

Seu objetivo exclusivo é garantir que a identificação da arquitetura do patrimônio técnico seja realizada de forma objetiva, auditável, reproduzível e totalmente aderente à Constituição do Programa.

---

## 2. Contexto

A FASE 1 produziu o inventário estrutural do patrimônio técnico por meio do SYSTEM_MAP.md.

O Conselho reconhece que o mapeamento estrutural não representa conhecimento arquitetural suficiente para orientar decisões de migração.

Antes de qualquer nova implementação, torna-se obrigatória a construção do mapa arquitetural institucional.

---

## 3. Objetivo da FASE 2

A FASE 2 possui apenas um objetivo:

**Identificar e documentar a arquitetura existente do OMEGA_OS_Kernel sem modificá-la.**

A FASE 2 não possui como objetivo:

- reconstruir arquitetura;
- redesenhar arquitetura;
- simplificar arquitetura;
- otimizar arquitetura;
- criar novos componentes;
- substituir componentes existentes;
- validar equivalência funcional;
- propor melhorias.

---

## 4. Natureza da documentação

Todo o ARCHITECTURE_MAP deverá ser estritamente descritivo.

São permitidas apenas informações comprovadas por evidências presentes no patrimônio técnico.

São proibidas interpretações, inferências ou recomendações técnicas.

---

## 5. Evidência obrigatória

Toda afirmação deverá possuir referência objetiva de origem.

Cada componente identificado deverá informar, no mínimo:

- Nome
- Domínio
- Tipo
- Localização
- Arquivos associados
- Dependências conhecidas
- Interfaces
- Entradas
- Saídas
- Componentes consumidores
- Componentes provedores
- Evidência de origem

Nenhuma descrição poderá ser baseada em interpretação pessoal.

---

## 6. Proibições

Durante a execução da FASE 2 é expressamente proibido:

- modificar qualquer arquivo do OMEGA_OS_Kernel;
- modificar qualquer arquivo do OMEGA-Kernel-Sovereign;
- reconstruir componentes;
- substituir lógica existente;
- emitir recomendações de redesign;
- classificar componentes como obsoletos sem evidência;
- assumir inexistência de funcionalidades não analisadas.

---

## 7. Princípio da Evidência Primária

Todo componente identificado deverá estar vinculado à sua evidência primária.

Exemplos de evidências aceitáveis:

- código-fonte;
- documentação técnica;
- contratos;
- testes;
- comentários técnicos;
- ADRs;
- histórico institucional.

Não serão aceitas conclusões sem rastreabilidade.

---

## 8. Princípio da Neutralidade

O PSA atuará exclusivamente como auditor técnico.

É vedado emitir julgamentos de qualidade durante a produção do ARCHITECTURE_MAP.

O documento deverá representar o patrimônio técnico exatamente como encontrado.

---

## 9. Ausência de evidência

O Conselho estabelece como princípio permanente:

> **Ausência de evidência não constitui evidência de ausência.**

Nenhum componente poderá ser considerado inexistente enquanto não forem concluídas todas as verificações previstas pela metodologia institucional.

---

## 10. Separação entre descrição e análise

A ETAPA 3.5 passa a ser dividida em duas naturezas distintas:

**Descrição**

- SYSTEM_MAP
- ARCHITECTURE_MAP
- FUNCTIONAL_MAP
- PARITY_MATRIX

**Análise**

Somente após aprovação do Conselho poderão ser produzidos documentos contendo:

- análises;
- recomendações;
- propostas de migração;
- decisões de descarte;
- propostas de reconstrução.

---

## 11. Critério de conclusão da FASE 2

A FASE 2 somente será considerada concluída quando:

- todos os domínios arquiteturais identificados estiverem documentados;
- todas as dependências principais estiverem registradas;
- toda informação possuir evidência rastreável;
- não existir interpretação misturada com descrição.

---

## 12. Entregáveis esperados

A FASE 2 deverá produzir exclusivamente:

- ARCHITECTURE_MAP.md
- ARCHITECTURE_INDEX.md
- EVIDENCE_INDEX.md

Nenhum outro documento poderá ser produzido sem autorização posterior do Conselho.

---

## 13. Próxima etapa

Após aprovação formal do ARCHITECTURE_MAP, o Conselho deliberará sobre a abertura da FASE 3 — FUNCTIONAL MAP.

Nenhuma atividade relacionada à Matriz de Paridade Funcional, MIG-4 ou demais migrações poderá ser iniciada antes da conclusão e aprovação institucional da FASE 2.

---

## 14. Deliberação

O Conselho determina que esta metodologia passa a integrar permanentemente a Constituição do Programa.

Todas as fases futuras de inventário, análise e migração deverão observar os mesmos princípios:

- Governança antes da execução.
- Evidência antes da interpretação.
- Patrimônio técnico antes da reconstrução.
- Descrição antes da decisão.
- Paridade funcional antes da substituição.

---

**Conselho OMEGA**

**COUNCIL-DIRECTIVE-029**

**Documento normativo de metodologia — FASE 2 (ARCHITECTURE MAP)**

**Vigência imediata após registro pelo PSA.**
