# OMEGA-CONSTITUTION-001

## Constituição do Programa OMEGA Kernel Sovereign

**ID:** OMEGA-CONSTITUTION-001  
**Data:** 2026-06-27  
**Emitido por:** Conselho / CEO  
**Responsável pela incorporação:** Principal Solution Architect PSA  
**Status:** ✅ VIGENTE  
**Classificação:** Documento de maior hierarquia do Programa  
**Referências:** COUNCIL-DIRECTIVE-025 · COUNCIL-SYNC-REQUEST-002 · DEC-RESET-001 · CEO-DIRECTIVE-024 · CEO-DIRECTIVE-026

---

## 1. Propósito

Esta Constituição estabelece a base permanente do Programa OMEGA Kernel Sovereign. Ela define a missão institucional, os princípios de governança, a política de migração e a hierarquia documental do programa.

Nenhum outro documento do Programa pode contrariar esta Constituição.

---

## 2. Missão Institucional

> Recuperar integralmente o patrimônio técnico do OMEGA_OS_Kernel dentro da arquitetura soberana do OMEGA-Kernel-Sovereign, preservando comportamento funcional, eliminando apenas elementos contaminados e garantindo rastreabilidade completa entre legado e arquitetura V6.

A missão não é desenvolver um novo sistema de trading independente. É preservar o conhecimento operacional acumulado ao longo de milhares de horas de engenharia, em uma arquitetura limpa, auditável e funcionalmente equivalente.

---

## 3. Princípios Permanentes

### 3.1 Preservação sobre reconstrução

O padrão oficial é **preservar comportamento**, não **reimplementar por conveniência**.

### 3.2 Arquitetura não substitui funcionalidade

Arquitetura limpa, CI verde, contratos formais e Gates Arquiteturais aprovados **não** demonstram equivalência funcional com o legado.

### 3.3 Rastreabilidade obrigatória

Toda implementação deverá possuir rastreabilidade explícita a um item do inventário do OMEGA_OS_Kernel.

### 3.4 Independência PSA × AIC

O PSA define e audita a governança. O AIC executa implementação. Nenhuma operação de código pode substituir deliberação do Conselho.

### 3.5 Duplo gate

Cada componente deverá passar por:

- **Gate Arquitetural** — valida estrutura, contratos, CI, isolamento, determinismo.
- **Gate Funcional** — valida comportamento equivalente ao legado.

### 3.6 Isolamento de workspaces e patrimônio técnico congelado

- O PSA atua exclusivamente no `OMEGA-PSA-AUDIT-WORKSPACE`.
- O AIC atua exclusivamente no `OMEGA-Kernel-Sovereign`.
- O `OMEGA_OS_Kernel` é **Patrimônio Técnico Congelado** — somente leitura, sem modificações.
- Toda comunicação entre PSA e AIC ocorre mediante fluxo institucional aprovado pelo Conselho.
- Detalhamento operacional em CEO-DIRECTIVE-026.

---

## 4. Política de Migração

A sequência obrigatória para toda implementação futura é:

```
Legado
   ↓
Inventário
   ↓
Mapeamento funcional
   ↓
Contrato
   ↓
Implementação soberana
   ↓
Teste de Paridade
   ↓
Integração
   ↓
Gate Funcional
```

Fica vedada a criação de novos componentes sem inventário prévio do comportamento correspondente no legado, salvo autorização expressa do Conselho.

---

## 5. Hierarquia Documental

A governança do Programa obedece a seguinte ordem de autoridade:

1. **Constituição do Programa** (OMEGA-CONSTITUTION-001)
2. **ADRs** — decisões arquiteturais de largo alcance
3. **Decisões do Conselho** — DEC, CEO-DIRECTIVE, COUNCIL-DIRECTIVE
4. **Charters** — mandatos de cada etapa (MIG)
5. **Tasks** — trabalhos específicos
6. **Registros Operacionais** — relatórios, validações, logs

---

## 6. Definições

- **OMEGA_OS_Kernel:** sistema legado de trading institucional, fonte do patrimônio técnico a ser recuperado.
- **OMEGA-Kernel-Sovereign:** arquitetura V6 soberana, limpa e auditável, destinada a hospedar o patrimônio funcional recuperado.
- **Gate Arquitetural:** validação de estrutura, contratos, CI, governança e determinismo.
- **Gate Funcional:** validação de comportamento equivalente ao legado.
- **Paridade funcional:** entradas equivalentes produzem decisões equivalentes dentro das tolerâncias aprovadas.
- **Inventário:** catálogo oficial de componentes do legado com classificação de destino.
- **Matriz de Rastreabilidade:** mapeamento Legado → Componente → Responsabilidade → Dependências → Status → Destino MIG → Decisão.

---

## 7. Classificação de Componentes

Todo componente do legado deverá ser classificado em uma das seguintes categorias:

- **PORTAR** — migrar funcionalmente para o Sovereign.
- **REESCREVER** — reconstruir com equivalência funcional demonstrada.
- **DESCARTAR** — eliminar, com justificativa institucional aprovada.
- **REFERÊNCIA FORENSE** — manter apenas como documentação/comprovação.

A classificação é de responsabilidade do Conselho, com parecer técnico do PSA.

---

## 8. Suspensões em Vigor

Até aprovação formal da ETAPA 3.5 e da nova estrutura de governança, permanecem suspensos:

- TASK-0024
- MIG-4
- MIG-5
- MIG-6

O AIC permanece em **STANDBY**, sem autorização para novos módulos, implementações, contratos ou funcionalidades.

---

## 9. Entregáveis Obrigatórios

O PSA deverá produzir:

1. OMEGA-CONSTITUTION-001 (este documento)
2. Plano Oficial da ETAPA 3.5
3. Metodologia Oficial de Paridade Funcional
4. Migration Traceability Matrix
5. Critérios de Gate Funcional

---

## 10. Revisão

Esta Constituição só poderá ser alterada mediante deliberação formal do Conselho.

---

**Conselho / CEO**  
**Principal Solution Architect PSA**  
**2026-06-27**
