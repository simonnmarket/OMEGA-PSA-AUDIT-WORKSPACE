# COUNCIL-DIRECTIVE-030

## Autorização Geral para Execução da ETAPA 3.5 — Inventário Institucional do Patrimônio Técnico

**ID:** COUNCIL-DIRECTIVE-030  
**Data:** 2026-06-27  
**Emitido por:** Conselho OMEGA / CEO  
**Status:** ✅ VIGENTE  
**Hierarquia:** OMEGA-CONSTITUTION-001 → COUNCIL-RESOLUTION-001 → ADR-012 → COUNCIL-DIRECTIVE-030  
**Título:** Autorização Geral para Execução da ETAPA 3.5 — Inventário Institucional do Patrimônio Técnico  
**Vincula:** COUNCIL-DIRECTIVE-028 (fases 0-7) · COUNCIL-DIRECTIVE-029 (metodologia FASE 2) · CEO-DIRECTIVE-026 (isolamento) · CEO-DIRECTIVE-027 (especificação ETAPA 3.5)

---

## 1. Finalidade

Autorizar formalmente o PSA a executar a ETAPA 3.5 do Programa OMEGA, em conformidade com:

- a `OMEGA-CONSTITUTION-001`;
- a `COUNCIL-RESOLUTION-001` (padrão de documentação e deliberação);
- o `ADR-012_PLANO_MESTRE`;
- a `COUNCIL-DIRECTIVE-028` (fases 0-7);
- a `COUNCIL-DIRECTIVE-029` (metodologia da FASE 2);
- o `CEO-DIRECTIVE-026` (isolamento de workspaces);
- o `CEO-DIRECTIVE-027` (especificação da ETAPA 3.5).

---

## 2. Escopo Autorizado

O PSA está autorizado a executar exclusivamente atividades de **documentação, cartografia, validação e auditoria** do patrimônio técnico existente no `OMEGA_OS_Kernel`.

As atividades autorizadas incluem:

- levantamento estrutural;
- levantamento arquitetural;
- levantamento funcional;
- levantamento operacional;
- levantamento de módulos, agentes, pipelines, estratégias, serviços, contratos implícitos, integrações, motores matemáticos, componentes de decisão, gerenciamento de risco, execução e inteligência.

A sequência obrigatória das fases está definida na `COUNCIL-DIRECTIVE-028`.
A metodologia da FASE 2 está definida na `COUNCIL-DIRECTIVE-029`.

---

## 3. Modo de Operação

Toda a ETAPA 3.5 será executada em modo **READ ONLY**.

É expressamente vedado:

- modificar arquivos do `OMEGA_OS_Kernel`;
- reorganizar diretórios do patrimônio técnico;
- corrigir, otimizar, portar ou implementar código;
- remover ou substituir componentes;
- interpretar comportamentos sem evidência primária;
- autorizar o AIC a executar qualquer implementação.

---

## 4. Fonte Oficial

A única fonte oficial da ETAPA 3.5 é o `OMEGA_OS_Kernel`, classificado como **Patrimônio Técnico Congelado**.

Toda conclusão deverá possuir referência explícita ao patrimônio original.

---

## 5. Critério de Qualidade

Nenhum componente poderá ser resumido genericamente como "indicador", "engine", "agente" ou "módulo" sem descrição completa.

Cada item deverá possuir, quando aplicável:

- responsabilidade;
- entradas;
- saídas;
- dependências;
- regras;
- interações;
- posição na arquitetura.

---

## 6. Critério de Encerramento

A ETAPA 3.5 somente poderá ser considerada concluída quando o Conselho possuir conhecimento suficiente para responder objetivamente:

- O que existe no patrimônio técnico?
- Como funciona?
- Por que existe?
- Onde está?
- Quem utiliza?
- Como interage?
- Qual seu valor técnico?
- Qual sua prioridade de migração?

---

## 7. Restrições Permanentes

Permanecem suspensos até deliberação formal do Conselho sobre os resultados da ETAPA 3.5:

- MIG-4
- MIG-5
- MIG-6
- TASK-0024
- qualquer implementação funcional no `OMEGA-Kernel-Sovereign`;
- qualquer novo componente de execução;
- qualquer alteração no código do AIC.

O AIC permanece em **STANDBY**.

---

## 8. Comunicação Institucional

Toda comunicação obedecerá ao fluxo institucional:

```
Conselho
  ↓
PSA
  ↓
Conselho
  ↓
AIC
  ↓
Conselho
```

É proibida comunicação operacional direta entre PSA e AIC.

O `CEO-DIRECTIVE-026` permanece integralmente vigente.

---

## 9. Entregáveis Obrigatórios

O PSA deverá entregar, por fase, os documentos técnicos e evidências especificados nas diretivas aplicáveis:

- FASE 0: evidências de congelamento institucional;
- FASE 1: `SYSTEM_MAP.md` (já concluído);
- FASE 2: `ARCHITECTURE_MAP.md`, `ARCHITECTURE_INDEX.md`, `EVIDENCE_INDEX.md`;
- FASES 3-7: conforme `COUNCIL-DIRECTIVE-028` e `CEO-DIRECTIVE-027`.

Cada entrega deverá incluir:

- documento técnico;
- evidências;
- estatísticas;
- limitações encontradas;
- riscos identificados;
- recomendações ao Conselho.

Não deverão ser produzidas propostas de implementação sem autorização expressa do Conselho.

---

## 10. Deliberação

O Conselho autoriza o PSA a executar a ETAPA 3.5 nos termos desta Diretiva, das diretivas vinculadas e da Constituição do Programa.

Nenhuma implementação poderá ser retomada até que o Conselho delibere sobre os resultados da Matriz de Paridade Funcional.

---

**Conselho OMEGA / CEO**  
**Principal Solution Architect PSA**  
**2026-06-27**
