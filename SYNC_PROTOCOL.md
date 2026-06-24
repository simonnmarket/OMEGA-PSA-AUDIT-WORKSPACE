# SYNC_PROTOCOL.md

**Projeto:** OMEGA Kernel Sovereign V6  
**Versão:** 2.0  
**Data:** 2026-06-24  
**Autoridade:** CFO-RAT-20260623-03 · CFO-RATIFICATION-001 · ADR-012 · DEC-15  
**Status:** APROVADO — ATUALIZADO (Taskade removido)

---

## 1. OBJETIVO

Definir o protocolo oficial e obrigatório de sincronização entre:
- **PSA** (Autoridade Documental — `OMEGA-PSA-AUDIT-WORKSPACE`)
- **AIC** (Autoridade Técnica — `OMEGA-Kernel-Sovereign`)
- **Conselho** (Autoridade de Aprovação)

Toda sincronização deve ser rastreável, reversível e auditável.

---

## 2. PRINCÍPIO FUNDAMENTAL

```
PSA (OMEGA-PSA-AUDIT-WORKSPACE) = FONTE DA VERDADE DOCUMENTAL
AIC (OMEGA-Kernel-Sovereign) = FONTE DA VERDADE TÉCNICA
Conselho (CEO + CFO) = APROVADOR FINAL
```

Nenhuma decisão de governança é válida se não estiver registrada pelo PSA.  
Nenhuma alteração técnica é válida se não houver ADR ou DEC correspondente aprovado pelo Conselho.

---

## 3. FLUXO OFICIAL DE SINCRONIZAÇÃO

```
Conselho aprova decisão
  ↓
PSA gera artefatos documentais (OMEGA-PSA-AUDIT-WORKSPACE)
  - ADR correspondente
  - DEC no DECISION_REGISTRY
  - Atualização dos registries (BUG, MIGRATION_ALLOWLIST)
  ↓
PSA emite pacote SYNC-IN para AIC
  ↓
AIC cria branch: TASK-XXXX-sync (OMEGA-Kernel-Sovereign)
  ↓
AIC aplica arquivos sob governance/ APENAS
  ↓
AIC commit: "[TASK-XXXX] <descrição>"
  ↓
AIC abre PR
  ↓
Conselho/CFO revisa checklist obrigatório
  ↓
Conselho aprova merge
  ↓
AIC realiza merge
  ↓
PSA registra conclusão no SYNC_LOG.md
  ↓
Gate correspondente = FECHADO
```

---

## 4. CHECKLIST OBRIGATÓRIO DE PR

Antes de qualquer merge, verificar:

- [ ] Branch parte de `main` (ou branch base designada)
- [ ] Apenas arquivos sob `governance/` foram modificados
- [ ] **Nenhum** arquivo em `runtime/` foi alterado
- [ ] **Nenhum** arquivo em `strategy/` foi alterado
- [ ] **Nenhum** arquivo em `execution/` foi alterado
- [ ] **Nenhum** arquivo em `deployment/` foi alterado
- [ ] **Nenhum** arquivo em `telemetry/` foi alterado
- [ ] **Nenhum** arquivo em `contracts/` foi alterado
- [ ] **Nenhum** arquivo em `tests/` foi alterado
- [ ] **Nenhum** código Python foi alterado
- [ ] Todos os IDs (ADR, DEC, BUG, MIG) são canônicos
- [ ] BUG-005, BUG-007, BUG-008 permanecem como EVIDÊNCIA FORENSE
- [ ] SYNC_LOG.md foi atualizado com esta sincronização

**Se qualquer item falhar: PR = REJEITADO**

---

## 5. CONVENÇÃO DE BRANCHES

| Tipo | Padrão | Exemplo |
|------|--------|---------|
| Sincronização documental | `TASK-XXXX-sync` | `TASK-0018-sync` |
| Correção documental | `TASK-XXXX-fix-doc` | `TASK-0018-fix-doc` |
| MIG técnico (futuro) | `MIG-X-<componente>` | `MIG-1-indicator-engine` |

---

## 6. CONVENÇÃO DE COMMITS

```
[TASK-XXXX] <ação em imperativo>
```

Exemplos:
- `[TASK-0018] Add ADR-001 to ADR-008 governance sync`
- `[TASK-0018] Add ADR-012 Plano Mestre + DEC-15`
- `[TASK-0019] Add SYNC_PROTOCOL.md and SYNC_LOG.md`

---

## 7. FREQUÊNCIA DE SINCRONIZAÇÃO

- **Por task concluída:** obrigatório antes de fechar qualquer gate
- **Por ratificação do Conselho:** imediato — máximo 24h após aprovação
- **Por correção documental:** imediato — não acumular correções

---

## 8. ARQUIVOS SEMPRE ATUALIZADOS EM CADA SYNC

| Arquivo | Obrigação |
|---------|-----------|
| `governance/adr/INDEX.md` | Sempre que um ADR for adicionado/alterado |
| `governance/knowledge_extraction/DECISION_REGISTRY.csv` | Toda nova DEC |
| `governance/knowledge_extraction/BUG_REGISTRY.csv` | Toda alteração de status/MIG de bug |
| `governance/MIGRATION_ALLOWLIST.md` | Toda alteração de escopo de MIG |
| `governance/SYNC_LOG.md` | **Toda sincronização, sem exceção** |

---

## 9. REGRAS DE CONFLITO

Se houver conflito entre PSA e AIC (documentação vs código):
1. **Parar** — não fazer merge
2. **Notificar** o Conselho imediatamente
3. **Identificar** qual versão é a mais recente e aprovada
4. **Conselho decide** qual versão prevalece
5. **Registrar** a resolução como DEC no DECISION_REGISTRY

---

## 10. VIOLAÇÕES

Constituem violação deste protocolo:
- Merge sem checklist aprovado
- Alteração de arquivos fora de `governance/` durante ETAPA 0
- Commit sem ID rastreável (TASK-XXXX ou ADR-XXX ou DEC-XX)
- Divergência entre PSA e AIC por mais de 24h
- MIG iniciado sem gate anterior fechado

**Toda violação deve ser registrada como BUG no BUG_REGISTRY com status VIOLATION.**

---

*Última atualização: 2026-06-24*  
*Autoridade: CFO-RAT-20260623-03 · CFO-RATIFICATION-001 · ADR-012*  
*Nota: Taskade removido da governança por decisão do Conselho (2026-06-24)*
