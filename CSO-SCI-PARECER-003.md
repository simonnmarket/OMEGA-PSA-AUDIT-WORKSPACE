# CSO-SCI-PARECER-003

## Plano de Retomada da FASE 2 com Reaproveitamento de Evidências Históricas

**Emitente:** Chief Science Officer — CSO-Sci  
**Destinatário:** CEO do Programa OMEGA  
**Encaminhamento recomendado:** PSA  
**Data:** 2026-06-28  
**Status:** Parecer oficial para orientação da retomada documental da FASE 2  
**Restrição:** Este parecer não autoriza execução técnica, alteração de código, migração, saneamento ou implementação.

---

## 1. Objeto

Este parecer estabelece o plano científico-institucional de retomada da FASE 2 da ETAPA 3.5, considerando a existência de auditorias, inventários, pareceres, protocolos e dossiês já produzidos nas semanas anteriores.

O objetivo é impedir retrabalho, preservar evidências e orientar o PSA quanto à ordem correta de consolidação documental.

---

## 2. Premissa Central

A FASE 2 não deve iniciar como exploração cega do OMEGA_OS_Kernel.

O Programa já possui massa documental suficiente para iniciar por reaproveitamento, validação e hierarquização de evidências históricas, recorrendo ao código legado apenas para confirmação primária, lacunas ou divergências.

---

## 3. Estado Institucional Confirmado

Permanecem vigentes:

- OMEGA_OS_Kernel em modo read-only.
- AIC Tech Lead em standby.
- MIG-4, MIG-5 e MIG-6 suspensas.
- TASK-0024 suspensa.
- Nenhuma execução técnica autorizada.
- Nenhuma alteração de código autorizada.
- FASE 2 autorizada apenas como cartografia, inventário e validação documental.

---

## 4. Eixo Prioritário da Retomada

O primeiro eixo da FASE 2 deve ser:

**Soberania de Runtime / Universos de Execução**

**Justificativa:**

O incidente do "motor errado" altera a interpretação de todo o ecossistema. Antes de mapear arquitetura ampla, é obrigatório distinguir:

- qual motor era observado pelo Conselho;
- qual motor podia ser executado operacionalmente;
- quais motores eram legados, experimentais, órfãos ou contaminantes;
- quais logs representam execução real;
- quais logs representam teste, stub ou resíduo;
- quais artefatos pertencem a TEST, DEMO ou EXEC.

Sem essa separação, qualquer ARCHITECTURE_MAP corre risco de misturar arquitetura real, intenção institucional e resíduos históricos.

---

## 5. Fontes Documentais Prioritárias

O PSA deve consumir os documentos na seguinte ordem:

1. `DOCUMENTO_MESTRE_SANEAMENTO_OMEGA_20260618.md`
2. `ADENDO_DOCUMENTO_MESTRE_v1.1_FECHAMENTO_PRE_CONSELHO_20260618.md`
3. Pareceres do Conselho em `Etapa 180626\Parecer Conselho`
4. Documentos FOR10, FOR11, FOR12, FOR14 e FOR15
5. Protocolos FMED-01, FMED-02 e FMED-03
6. Relatórios de 14/06 a 17/06
7. Inventários e auditorias de 04/06 a 13/06
8. Pacote AIC de 02/06 como evidência técnica histórica, observando que estava marcado como pendente de acta/não oficial em sua origem

---

## 6. Classificação de Evidência

O PSA deve separar as fontes em três níveis:

| Nível | Tipo | Uso |
|-------|------|-----|
| Evidência Normativa | Resoluções, diretivas, registros ratificados | Determina autoridade vigente |
| Evidência Forense | Documento Mestre, Adendo, CT-01 a CT-10, logs, runtime, FOR/FMED | Sustenta fatos técnicos |
| Evidência Histórica | Pacotes AIC, pareceres iniciais, snapshots, debates anteriores | Ajuda a reconstruir origem e contexto |

---

## 7. Entregável Inicial Recomendado ao PSA

Antes de produzir o ARCHITECTURE_MAP completo, o PSA deve gerar um documento intermediário:

**RUNTIME-SOVEREIGNTY-MAP-001**

**Conteúdo mínimo:**

- Universo A: launcher, motor, cadeia de decisão e status.
- Universo B: launcher, motor, cadeia de decisão e status.
- Inventário de variantes shadow_loop.
- Classificação: soberano, legado, experimental, órfão, contaminante.
- Matriz CT-01 a CT-10.
- Separação TEST / DEMO / EXEC.
- Evidências FOR/FMED correlacionadas.
- Lista de lacunas que exigem confirmação no código.
- Declaração explícita de que nenhuma correção técnica está autorizada.

---

## 8. Risco Principal

O maior risco da retomada é produzir uma arquitetura "limpa" demais, ignorando que o ecossistema real estava contaminado por múltiplos motores, logs sintéticos, flags, lockfiles, scripts concorrentes e ausência de segregação ambiental.

A FASE 2 deve preservar essa complexidade como fato de auditoria, não eliminá-la por simplificação documental.

---

## 9. Recomendação CSO-Sci

Recomendo ao CEO encaminhar este parecer ao PSA com a seguinte instrução:

> O PSA deve iniciar a FASE 2 pela consolidação da soberania de runtime, reaproveitando as evidências históricas já produzidas, antes de avançar para o mapa arquitetural amplo do OMEGA_OS_Kernel.

---

## 10. Parecer Final

**Status:** FAVORÁVEL À RETOMADA DA FASE 2, com condicionante metodológica.

A retomada é adequada desde que o PSA observe a seguinte regra:

> Primeiro evidência histórica, depois confirmação primária, depois arquitetura.

Nenhuma execução técnica, migração, saneamento ou implementação decorre deste parecer.

---

**Assinatura:**  
Chief Science Officer — CSO-Sci  
Programa OMEGA  
2026-06-28
