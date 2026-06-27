# CEO-DIRECTIVE-026

## Protocolo Permanente de Isolamento dos Workspaces, Preservação do Patrimônio Técnico e Comunicação Institucional

**ID:** CEO-DIRECTIVE-026  
**Data:** 2026-06-27  
**Emitido por:** CEO / Conselho  
**Destinatário:** PSA — Program Steward Auditor  
**Status:** ✅ DIRETRIZ PERMANENTE — VIGENTE IMEDIATAMENTE  
**Hierarquia:** Subordinada apenas à OMEGA-CONSTITUTION-001

---

## 1. Objetivo

Estabelecer regras permanentes para:

- isolamento físico e lógico entre os workspaces do Programa;
- preservação do patrimônio técnico do OMEGA_OS_Kernel;
- prevenção de conflitos operacionais entre PSA e AIC;
- padronização da comunicação institucional;
- proteção da rastreabilidade do Programa OMEGA.

---

## 2. Princípios Permanentes

### 2.1 Um Workspace, Um Responsável

Cada repositório possui um único responsável institucional. Nenhum agente poderá atuar diretamente em repositório sob responsabilidade de outro agente.

### 2.2 Separação entre Governança e Implementação

- Documentação institucional pertence ao PSA.
- Implementação de software pertence ao AIC.
- Essas responsabilidades não poderão ser misturadas.

### 2.3 Patrimônio Técnico

O OMEGA_OS_Kernel constitui patrimônio técnico do Programa. Seu conteúdo será utilizado exclusivamente como fonte oficial para:

- inventário;
- rastreabilidade;
- análise funcional;
- comprovação de paridade.

Nenhuma atividade deverá descaracterizar ou modificar esse patrimônio.

### 2.4 Conselho como Autoridade de Coordenação

Toda interação entre PSA e AIC deverá ocorrer mediante fluxo institucional aprovado pelo Conselho. Não haverá coordenação operacional direta entre PSA e AIC.

---

## 3. Responsabilidades do PSA

**Workspace exclusivo:** `OMEGA-PSA-AUDIT-WORKSPACE`

### Autorizado

- elaborar documentos institucionais;
- produzir Constituição;
- produzir ADRs;
- emitir pareceres;
- elaborar Charters;
- manter registros oficiais;
- produzir metodologia de paridade;
- elaborar inventários;
- validar tecnicamente o Kernel em modo somente leitura.

### Proibido

- alterar código do Kernel;
- criar branches do Kernel;
- executar merge no Kernel;
- realizar commit no Kernel;
- executar push no Kernel;
- modificar qualquer arquivo pertencente ao workspace do AIC.

---

## 4. Responsabilidades do AIC

**Workspace exclusivo:** `OMEGA-Kernel-Sovereign`

### Autorizado

- implementar código;
- executar testes;
- executar CI;
- criar branches;
- realizar merge;
- atualizar arquitetura do Kernel;
- implementar componentes autorizados.

### Proibido

- alterar documentação oficial do PSA;
- modificar Constituição;
- editar registros institucionais do PSA;
- alterar documentos de governança pertencentes ao PSA.

---

## 5. Status do OMEGA_OS_Kernel

O repositório `OMEGA_OS_Kernel` passa a ser oficialmente classificado como **Patrimônio Técnico Congelado**:

- somente leitura;
- nenhuma implementação;
- nenhum commit;
- nenhum merge;
- nenhuma reorganização estrutural;
- nenhuma limpeza de código.

Utilização restrita a: leitura, inventário, comparação, rastreabilidade e comprovação de paridade funcional.

---

## 6. Protocolo Oficial de Comunicação

O fluxo institucional obrigatório é:

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
   ↓
PSA
```

Não será admitida emissão direta de diretivas técnicas entre PSA e AIC sem validação do Conselho.

---

## 7. Inventário da ETAPA 3.5

O inventário deverá produzir um **Inventário Canônico do Patrimônio Técnico do Programa**. Cada componente deverá conter, no mínimo:

- nome do componente;
- localização no legado;
- responsabilidade funcional;
- objetivo de negócio;
- dependências;
- integrações;
- módulos consumidores;
- criticidade operacional;
- evidências de utilização;
- destino proposto (portar, reescrever com equivalência, descartar ou referência);
- MIG responsável;
- critério futuro de comprovação de equivalência funcional.

---

## 8. Preservação do Conhecimento

Fica vedada qualquer substituição de componentes existentes por implementações simplificadas sem decisão formal do Conselho. A existência de um componente legado implica sua análise individual antes de qualquer decisão de reimplementação.

---

## 9. Critério de Continuidade

A ETAPA 3.5 só será concluída após aprovação pelo Conselho de:

- Inventário Canônico;
- Matriz de Rastreabilidade;
- Metodologia de Paridade Funcional;
- Critérios de Gate Funcional.

Enquanto esses documentos não forem aprovados, MIG-4, MIG-5 e MIG-6 permanecem suspensos e qualquer nova implementação permanece bloqueada.

---

## 10. Registro de Incidentes

Todo incidente envolvendo workspace incorreto, sincronização indevida, alteração em repositório não autorizado ou comunicação institucional fora do protocolo deverá ser registrado pelo PSA como incidente de governança, contendo:

- causa raiz;
- impacto;
- ações corretivas;
- ações preventivas;
- validação de encerramento.

---

## 11. Disposição Final

Esta Diretiva complementa a OMEGA-CONSTITUTION-001 e integra permanentemente a governança do Programa.

---

**CEO / Conselho**  
**2026-06-27**
