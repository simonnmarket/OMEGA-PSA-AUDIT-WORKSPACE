# CEO-DIRECTIVE-023A — Reforço das Fronteiras Operacionais PSA × AIC

**ID:** CEO-DIRECTIVE-023A  
**Data:** 2026-06-27  
**Emitido por:** CEO / Conselho  
**Status:** ✅ VIGENTE  
**Referências:** ADR-012 · COUNCIL-DIRECTIVE-023 · DEC-GATE-MIG3-001

---

## Objeto

Reafirmar a separação operacional entre os workspaces do PSA e do AIC após o incidente envolvendo a atualização do arquivo `SOVEREIGN_TOPOLOGY.md` no repositório `OMEGA-Kernel-Sovereign`.

---

## Diretriz

O Conselho determina que a separação entre os repositórios permanece obrigatória e passa a ser reforçada como regra permanente de governança.

### PSA — Responsabilidades exclusivas

- Governança documental
- ADRs
- Pareceres
- Relatórios
- Consolidação arquitetural
- Auditoria
- Workspace `OMEGA-PSA-AUDIT-WORKSPACE`

**O PSA não executará operações Git diretamente no repositório `OMEGA-Kernel-Sovereign`, exceto quando houver autorização explícita do Conselho para uma atividade extraordinária.**

### AIC — Responsabilidades exclusivas

- Código-fonte
- Estrutura do Kernel
- Branches
- Commits
- Pull Requests
- Testes
- Integração técnica
- Workspace `OMEGA-Kernel-Sovereign`

Toda alteração oriunda do PSA que afete o Kernel deverá ser entregue como orientação documental ao AIC, cabendo ao AIC aplicar a alteração em seu próprio workspace e sincronizar o repositório.

---

## Registro do incidente

O incidente referente ao `SOVEREIGN_TOPOLOGY.md` foi classificado como operacional, sem impacto técnico ou funcional.

Nenhuma inconsistência arquitetural foi identificada.

---

## Ação corretiva — Fluxo oficial

```
PSA → Documento / Parecer → Conselho → Diretiva → AIC → Alteração no Kernel → PSA valida
```

Esse fluxo torna obrigatória a preservação da independência entre os ambientes e elimina sobreposição de responsabilidades.

---

## Sobre o caso atual

Como o PSA confirmou que apenas um documento arquitetural foi alterado, o Conselho considera aceitável concluir essa sincronização uma única vez para encerrar o ciclo do MIG-3.

Entretanto, isso não deverá se tornar padrão.

---

## Regra permanente a partir de TASK-0024

- **PSA nunca mais faz commit no repositório do Kernel.**
- **AIC nunca mais altera documentos oficiais do PSA.**
- Toda comunicação entre PSA e AIC ocorre por `SYNC-IN`, `SYNC-OUT`, pareceres e diretivas do Conselho.

---

## Estado

A presente diretiva não altera o escopo do projeto, não modifica componentes técnicos e apenas reforça a governança institucional já definida no ADR-012.

---

**CEO / Conselho**  
**OMEGA Kernel Sovereign V6**  
**CEO-DIRECTIVE-023A — VIGENTE**
