# CEO-DIRECTIVE-024 — Política Oficial de Isolamento de Workspaces e Fronteiras Operacionais

**ID:** CEO-DIRECTIVE-024  
**Data:** 2026-06-27  
**Emitido por:** CEO / Conselho  
**Destinatários:** PSA · AIC  
**Base:** ADR-012 · CEO-DIRECTIVE-023A · DEC-GATE-MIG3-001  
**Status:** DIRETRIZ PERMANENTE — VIGENTE IMEDIATAMENTE

---

## 1. Objetivo

Estabelecer definitivamente as fronteiras operacionais entre o PSA e o AIC, eliminando sobreposição de responsabilidades, conflitos de repositório e ciclos de sincronização indevidos.

Esta diretiva complementa a CEO-DIRECTIVE-023A e passa a integrar permanentemente o modelo de governança do OMEGA Kernel Sovereign V6.

---

## 2. Princípio Geral

Cada agente é responsável exclusivamente pelo seu ambiente oficial de trabalho.

Nenhum agente deverá executar operações Git, commits, merges ou alterações diretas no repositório pertencente ao outro agente.

Esta regra aplica-se a todas as etapas futuras do programa.

---

## 3. Workspaces Oficiais

### PSA

**Workspace oficial:** `OMEGA-PSA-AUDIT-WORKSPACE`

**Responsabilidades exclusivas:**

- Governança
- ADRs
- Diretivas
- Pareceres
- Auditorias
- Consolidação documental
- Planejamento institucional
- Evidências de conformidade

O PSA não altera diretamente o repositório `OMEGA-Kernel-Sovereign`.

### AIC

**Workspace oficial:** `OMEGA-Kernel-Sovereign`

**Responsabilidades exclusivas:**

- Código-fonte
- Arquitetura implementada
- Contratos
- Testes
- Branches
- Commits
- Pull Requests
- Merge
- Integração técnica

O AIC não altera documentos oficiais do PSA.

---

## 4. Fluxo Oficial de Trabalho

O fluxo institucional passa a ser obrigatório:

```
Conselho
  ↓
PSA produz documentação oficial
  ↓
Conselho delibera
  ↓
AIC implementa exclusivamente em seu workspace
  ↓
AIC emite SYNC-OUT
  ↓
PSA realiza validação independente
  ↓
Conselho delibera Gate
  ↓
Encerramento da etapa
```

Nenhum fluxo alternativo deverá ser utilizado.

---

## 5. Regra para Alterações Arquiteturais

Quando um documento produzido pelo PSA afetar a arquitetura do Kernel:

1. O PSA produz o documento.
2. O Conselho aprova.
3. O PSA encaminha a orientação documental.
4. O AIC reproduz a alteração em seu próprio repositório.
5. O PSA apenas valida posteriormente.

O PSA não deverá executar commits ou merges no Kernel.

---

## 6. Tratamento do Incidente MIG-3

O incidente envolvendo o arquivo `architecture/SOVEREIGN_TOPOLOGY.md` fica oficialmente classificado como:

**INCIDENTE OPERACIONAL DE FRONTEIRA ENTRE WORKSPACES**

Resultado da análise:

- nenhum impacto técnico;
- nenhuma alteração funcional;
- nenhuma inconsistência arquitetural;
- nenhuma perda de rastreabilidade.

A sincronização residual será executada exclusivamente pelo AIC.

Após essa sincronização, o incidente será considerado encerrado.

---

## 7. Regra Permanente

A partir desta diretiva:

- **PSA nunca altera diretamente o Kernel.**
- **AIC nunca altera diretamente o Workspace PSA.**

Toda comunicação institucional ocorrerá exclusivamente por:

- Diretivas;
- Pareceres;
- Charters;
- SYNC-IN;
- SYNC-OUT;
- Deliberações do Conselho.

---

## 8. Aplicação Imediata

Esta política passa a reger integralmente:

- TASK-0024 (MIG-4)
- MIG-5
- MIG-6
- DEMO
- SHADOW MODE
- GATE-REAL
- EXECUÇÃO REAL

---

## 9. Próxima Etapa

Após o AIC concluir a sincronização documental pendente do arquivo `SOVEREIGN_TOPOLOGY.md` e emitir o respectivo `SYNC-OUT`:

- o PSA realizará apenas a validação documental;
- o incidente será encerrado;
- o Conselho considerará o ciclo MIG-3 definitivamente concluído;
- poderá ser iniciada a **TASK-0024 — MIG-4 Risk Engine Charter**.

---

## 10. Deliberação

O Conselho considera encerrada a discussão referente à propriedade dos workspaces.

A presente diretiva estabelece a política oficial e permanente de separação de responsabilidades entre PSA e AIC, preservando a rastreabilidade, a independência entre documentação e implementação e a integridade do modelo de governança do OMEGA Kernel Sovereign V6.

---

**CEO / Conselho**  
**OMEGA Kernel Sovereign V6**
