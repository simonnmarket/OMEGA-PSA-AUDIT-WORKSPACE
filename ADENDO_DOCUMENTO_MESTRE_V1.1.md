# ADENDO AO DOCUMENTO-MESTRE v1.1 — FECHAMENTO PRÉ-CONSELHO

**Natureza:** resposta formal à "Solicitação Complementar ao AIC — Fechamento Pré-Conselho v1.0"
**Data:** 2026-06-18
**Autor:** AIC / Tech Lead
**Missão desta rodada:** converter diagnóstico forte em dossiê incontestável — fechar itens abertos, provar runtime, mapear precedência de autoridade, separar ação técnica de governança, instituir preservação forense.

---

## DIRETRIZ DE INTEGRIDADE APLICADA

- Cada conclusão tem âncora `arquivo:linha` **ou** evidência de runtime, marcada com: **[VERIFICADO] / [REFUTADO] / [NÃO MATERIAL] / [INCONCLUSIVO]**.
- Distinção rígida entre **fato observado**, **inferência**, **hipótese**, **recomendação**.
- Nenhuma ação destrutiva foi executada nesta coleta. Apenas leitura.
- **Runtime prevalece** sobre o que o código "parece permitir".

---

# ENTREGÁVEL 1 — FECHAMENTO DOS ITENS ABERTOS (BLOCO I)

## CT-05 — OHLCV histórico CSV no loop legacy → [VERIFICADO] (contaminante só no Universo B; NÃO MATERIAL para o caminho oficial v33)

**Fato observado (fluxo exato do dado):**
1. `scripts/run_omega_24x7.ps1:217-219` arranca `omega_paper_loop_24x7.py --pre-sync-ohlcv`.
2. `omega_paper_loop_24x7.py:129` define `EXPORT_SCRIPT = scripts/export_ohlcv_mt5.py` (exporta MT5 → CSV).
3. `shadow_loop.py:669` → `OHLCV = Path(os.getenv("OMEGA_OHLCV_PATH", ROOT/"data"/"ohlcv"))`.
4. `shadow_loop.py:681 check_harmonic_ohlcv_inputs` exige `{asset}_{tf}.csv`.
5. `shadow_loop.py:2513 run_harmonic` → subprocess `core_engines/omega_harmonic_engine_v3.py --lookback 3 --lookahead 5` (linha 2532-2537) → produz `harmonic_events_{asset}_{tf}.json`.

**Função consumidora:** Motor Harmônico V3 (componente de decisão **somente** do Universo B / `shadow_loop.py`).

**Efeito sobre sinal/gate/execução:**
- Fail-safe confirmado: se o CSV não existir, `run_harmonic` retorna `None` (`shadow_loop.py:2516-2531, 2531`) — não há harmônico, sem crash.
- **Look-ahead de rotulagem [VERIFICADO]:** `omega_harmonic_engine_v3.py:114` lê `future_px = df.iloc[i + lookahead]["linha"]` e rotula `outcome` com base no futuro (linhas 125-138). **Porém** o laço é `for i in range(lookback, n - lookahead)` (linha 111) — as últimas `lookahead` (5) barras **nunca** são rotuladas. Logo, **não injeta conhecimento do futuro na entrada da barra corrente.**

**Conclusão:** dependência de CSV é exclusiva do legacy, fail-safe, e **não pertence ao caminho oficial `shadow_loop_v33_final.py`**. O look-ahead existe na rotulagem histórica mas **não gera viés de entrada na barra atual**. Classificação: **contaminante de método no Universo B; NÃO MATERIAL para v33**.

---

## CT-06 — Fallback sintético `_get_sample_data()` → [VERIFICADO] — PROIBIDO em produção

**Fato observado (condição de ativação):**
- `agent_ia/core/omega_strategy_catalog.py:1093 build_market_data()` retorna:
  - `_get_sample_data()` em `except ImportError` (linha 1193-1195);
  - `_get_sample_data()` em **qualquer** `except Exception` (linha 1196-1198).
- `_get_sample_data()` (linha 1246-1268) devolve dados **fixos**: `current_price=2650.50, rsi_14=35.0, adx=30.0, ema_50=2645, ema_200=2600, volume_ratio=1.5`.
- Gatilho realista de exceção: `mt5.symbol_info(asset).point` (linha 1169) — se `symbol_info` retornar `None`, `.point` lança `AttributeError` → cai em `_get_sample_data()`.

**Caminho de chamada (no caminho OFICIAL):**
- `agent_ia/core/omega_global_orchestrator.py:227` → `market_data = build_market_data(asset)` (dentro de `get_trading_signal`, usado por `agent_ia.get_signal`).
- `omega_global_orchestrator.py:652` → segunda chamada.
- `core_engines/shadow_loop_v33_final.py:1772` → `build_market_data(symbol, "H1")` (chamada direta pelo motor oficial).

**Efeito real:**
- `mt5.initialize()` falho → `build_market_data` retorna `{}` (linha 1111) → orquestrador faz `if not market_data: return _no_signal` (linha 229-230) → **HOLD seguro**.
- **Risco material:** o ramo de **exceção** retorna dado sintético **não-vazio**, que **passa** o guard `if not market_data` → as estratégias rodam sobre preço fixo 2650.50 → **pode gerar BUY/SELL real a partir de dado falso.**

**Conclusão:** **PROIBIDO em demo/exec.** Recomendação técnica: em `except`, retornar `{}` (ou levantar) para forçar HOLD — nunca dado sintético. Classificação: **contaminante ativo no caminho oficial**.

---

## CT-08 — `OMEGA_TEST_HARNESS` → flag em si [REFUTADO] como alterador de comportamento; precedência env>file [VERIFICADO] e material

**Fato observado:**
- `shadow_loop.py:568 _log_test_harness_status()` apenas **registra log** (linhas 573, 583, 588). Não altera decisão, risco ou execução por si só. → **[REFUTADO]** como behavior-changer.
- **Porém**, o mecanismo de precedência é material: `shadow_loop.py:542-544 _get_flag()` = `os.getenv(key) or _live_flags.get(key, default)` — **env var sobrescreve arquivo persistente, sem gating de ambiente.**
- Flags que de fato mudam comportamento e usam esse mecanismo: `OMEGA_USFE_CONFLUENCE_WEIGHT` (linha 559-561), `OMEGA_RUPTURE_CAPTURE` (linha 592), além das dezenas listadas no `run_omega_24x7.ps1`.

**Conclusão:** a flag `OMEGA_TEST_HARNESS` é **[NÃO MATERIAL]** (log-only). O risco real, **[VERIFICADO]**, é a **ausência de segregação de ambiente na precedência de flags**: qualquer variável de teste exportada no shell vaza para demo/exec. (Entra na Matriz de Autoridade — Entregável 3.)

---

## CT-10 — "8 filtros PASS" cosmético no `shadow_loop_v33_final.py` → [VERIFICADO] — enganoso para auditoria

**Fato observado:** `shadow_loop_v33_final.py:1917-1937` emite estado `SIGNAL_VALIDATED` com **todos os 8 filtros hardcoded** como literal `"PASS"`:
```
filter_trend="PASS", filter_volatility="PASS", filter_liquidity="PASS",
filter_spread="PASS", filter_session="PASS", filter_market_structure="PASS",
filter_risk="PASS", filter_position="PASS"
```
O próprio comentário (linha 1917) admite: *"8 FILTROS INDIVIDUAIS (todos PASS — orquestrador validou internamente)"*. Adicionalmente, `_fa_pass` (linha 1951-1956) marca toda a attrition como `1` (passou).

**Vínculo com lógica de bloqueio/liberação:** **nenhum.** Não há avaliação individual por filtro — os valores são constantes emitidas após o orquestrador já ter decidido. Não bloqueiam nem liberam nada.

**Impacto real:** a trilha de auditoria FOR11 registra "8 dimensões validadas" que **nunca foram avaliadas individualmente**. Cria **confiança falsa** de robustez de validação.

**Conclusão:** **enganoso** (não funcional, não cosmético inócuo). Classificação: defeito de integridade de auditoria.

---

# ENTREGÁVEL 2 — PROVA DE RUNTIME E VERDADE OPERACIONAL (BLOCO II)

> Fonte: `audit/paper/paper_loop_20260611_203401.log`, `logs/decision_trace.jsonl`, `logs/execution_log.jsonl`, inspeção de processos (2026-06-18) e lockfiles.

## Achado central de runtime — a verdade operacional contraria o "projeto declarado"

**A última execução operacional disponível (2026-06-11 22:34:01) FALHOU no arranque, antes de entrar no loop de trading.** [VERIFICADO]

Evidência (`paper_loop_20260611_203401.log`):
- L8: `OMEGA SHADOW LOOP v3.0 | 1 ativos × 6 TFs | equity=USD 10000.00`
- L9: `Risk/trade=0.25% | MaxPos=3 | DD_max=2%`
- L13: `CRITICAL [OMEGA_V3.2] MT5 Bulletproof initialization failed: name 'MT5BulletproofLayer' is not defined`
- L16-19: `NameError: name 'MT5BulletproofLayer' is not defined` em `shadow_loop.py:3389`
- L30-33: erro secundário `UnboundLocalError: cannot access local variable '_erc'` em `shadow_loop.py:3436`

→ O motor legacy (Universo B) **não inicializa o MT5 e aborta**. Nenhuma ordem foi processada nessa execução.

## Logs de "execução" em `logs/` são SINTÉTICOS [VERIFICADO]

- `logs/decision_trace.jsonl`: 10 linhas idênticas `trace_0..trace_9`, **todas** `EURUSD BUY confidence 0.85`, timestamp idêntico `1781120598.92`.
- `logs/execution_log.jsonl`: 10 linhas `FILLED volume 1.0 price 1.1`.
→ Não são ordens reais (EURUSD a "1.1", lote 1.0, 10 idênticas). São **stubs de teste** residentes no diretório operacional. **Qualquer citação destes logs como "prova de operação" seria inválida.**

## Respostas às 10 perguntas obrigatórias de runtime

| # | Pergunta | Resposta | Status |
|---|---|---|---|
| 1 | Último launcher executado? | Universo B — paper loop (`omega_paper_loop_24x7.py` → `shadow_loop.py`), último log 2026-06-11 22:34 | [VERIFICADO] |
| 2 | Processo filho criado? | `shadow_loop.py` (traceback confirma o arquivo) | [VERIFICADO] |
| 3 | Motor entrou em loop? | **Não** — abortou na init MT5 (`shadow_loop.py:3389`) | [VERIFICADO] |
| 4 | Configs lidas em runtime? | `vcb_state.json` (restaurado, L1); `live_flags.json` (fallback); MUTEX `audit\.omega_system.lock` (L4) | [VERIFICADO] |
| 5 | Env vars prevaleceram sobre arquivo? | Precedência env>file confirmada no código (`:544`); enumeração exata da sessão não capturada | [INCONCLUSIVO p/ a sessão] |
| 6 | Flags persistentes consumidas? | `live_flags.json` lido como fallback (USE_AGENT_IA etc.) | [VERIFICADO existência/leitura] |
| 7 | Lock lido/criado/mantido? | `vcb_state.json` restaurado; MUTEX `.omega_system.lock`; órfão `audit/paper/omega_runner.lock` (07/06) | [VERIFICADO] |
| 8 | Função responsável pelo envio de ordem? | **Nenhuma alcançada** (crash). No código: legacy `mt5_send_order` / oficial `mt5_order_manager.send_entry` | [VERIFICADO: 0 ordens] |
| 9 | Divergência sinal × ordem? | Não alcançada nessa execução; estruturalmente é o CT-04 (SL/TP 200/400 fixos no v33) | [VERIFICADO estrutural] |
| 10 | Fallback silencioso no ciclo? | Não alcançado; estruturalmente CT-06 (sintético) + momentum EMA8/21 | [VERIFICADO estrutural] |

## Processos ativos AGORA (2026-06-18)

- Nenhum processo Python de trading em execução. [VERIFICADO]
- Resíduos: `audit/paper/omega_runner.lock` (07/06); `config/live_flags.json` freeze vencido (10/06). [VERIFICADO]

**Divergência projeto declarado × comportamento real:** o "motor operacional 24/7" declarado **não completa sequer a inicialização** na última execução registrada; as únicas trilhas de "decisão/execução" em `logs/` são sintéticas. A verdade operacional é: **não há execução operacional íntegra comprovada nos logs disponíveis.**

---

# ENTREGÁVEL 3 — MATRIZ DE AUTORIDADE E PRECEDÊNCIA OPERACIONAL (BLOCO III)

**Regra geral de precedência observada no código (`shadow_loop.py:544`):**
`variável de ambiente` **>** `config/live_flags.json` **>** `default hardcoded no motor`.
**Exceção crítica:** seleção de motor, lote e SL/TP **não** seguem essa regra — são **hardcoded no launcher/motor** e sobrescrevem inclusive o sinal.

| Dimensão | Fonte de autoridade | Precedência | Ponto de leitura | Ponto de sobrescrita | Efeito operacional | Risco de conflito |
|---|---|---|---|---|---|---|
| Seleção do motor | Hardcode no launcher | Launcher escolhido manualmente | `launch_24h_clean.py:72` (v33) / `omega_paper_loop_24x7.py:130` (legacy) | — | Define qual cérebro decide | **CRÍTICO — autoridade dupla** |
| Seleção do launcher | Operador / `.ps1` | Sem soberano único | 6+ scripts `.ps1` | — | Define universo A ou B | **CRÍTICO** |
| Modo paper/demo/exec | env `OMEGA_24X7_MODE` / `--mode` | env > default | `run_omega_24x7.ps1:22` | shell | Comportamento de execução | Médio |
| Momentum fallback | env vs arquivo | env > file | `run_omega_24x7.ps1:10`="0" vs `live_flags.json:11`="1" | shell sobrescreve arquivo | Liga/desliga 2º cérebro EMA8/21 | **ALTO — valores opostos** |
| Fusão PSA / shadow | env | env | `run_omega_24x7.ps1:140-144` (`PSA_SHADOW_MODE=0`) | shell | PSA pode executar (não só observar) | **ALTO** |
| Gates USFE/SEL/MTF | env + arquivo | env > file | `live_flags.json` + `_get_flag` | shell | Aprova/bloqueia sinal | Médio |
| Hard stop / DD / VCB | env | env > default | `shadow_loop.py:156,674-676,716,721` | shell | Circuit breakers | Médio |
| Lock singleton | Hardcode | — | `omega_paper_loop_24x7.py:119-128`; MUTEX `.omega_system.lock`; `omega_runner.lock` | — | Unicidade de processo (sem TTL) | **ALTO — sem TTL/escopo** |
| Lote | Hardcode (v33) vs env (legacy) | Hardcode v33 ignora risco | `shadow_loop_v33_final.py:2070`=0.01 / `shadow_loop.py:716` `OMEGA_RISK_PER_TRADE` | motor | Tamanho da posição | **ALTO — modelos divergentes** |
| SL/TP | Hardcode (v33) sobrescreve sinal | Hardcode > sinal | `shadow_loop_v33_final.py:2063-2064`=200/400 pts vs sinal `:1896-1897` | motor | Risco por trade; ledger≠ordem | **CRÍTICO (CT-04)** |
| Símbolo/universo | Hardcode (v33) vs env/json (legacy) | depende do motor | `launch_24h_clean.py:67` triade / `OMEGA_CEO_PRIORITY_SYMBOLS` `shadow_loop.py:725` | shell/json | Define ativos operados | Médio |
| Flags persistentes | `live_flags.json` | abaixo de env | `shadow_loop.py:544` | env sobrescreve | Estado herdado (freeze 09/06) | **ALTO — temporal** |
| Variáveis de ambiente | Shell / `.ps1` | **Máxima** | `os.getenv` em todo o motor | — | Controle de fato do sistema | **ALTO — sem gating de ambiente** |
| Defaults hardcoded | Motor | **Mínima** | múltiplos | env/file sobrescrevem | Comportamento base | Baixo |

**Conclusões explícitas:**
- **Conflitos ativos:** momentum (env "0" vs file "1"); dois motores; lote/SLTP com modelos divergentes.
- **Precedências perigosas:** env > tudo, **sem gating de ambiente** → teste vaza para exec.
- **Autoridade dupla:** seleção de motor e de launcher não têm soberano.
- **Sem soberania clara:** locks sem TTL/escopo; SL/TP hardcode sobrepõe a inteligência do sinal.

---

# ENTREGÁVEL 4 — MATRIZ DE REMEDIAÇÃO POR AUTORIDADE DE APROVAÇÃO (BLOCO IV)

## Classe A — Pode ser feito já (baixo risco, reversível)

| Ação | Justificativa | Risco | Reversibilidade | Dependência |
|---|---|---|---|---|
| Instituir Zona de Preservação Forense (Entregável 5) | Impedir perda de prova | Nulo | Total | Nenhuma |
| Congelar criação de novos launchers/flags | Conter expansão sem soberania | Nulo | Total | Aval CEO |
| Inventariar artefatos (feito no Doc-Mestre + este adendo) | Base de decisão | Nulo | Total | Nenhuma |
| Declarar componentes não-soberanos (sem remover) | Reduz ambiguidade | Nulo | Total | Nenhuma |
| Marcar `logs/decision_trace.jsonl` e `execution_log.jsonl` como sintéticos (sem apagar) | Evitar citação indevida | Nulo | Total | Nenhuma |

## Classe B — Recomendável, depende de validação técnica

| Ação | Justificativa | Risco | Reversibilidade | Dependência |
|---|---|---|---|---|
| Repontar `.ps1` para o launcher soberano | Eliminar Universo B acidental | Médio | Alta (backup) | Eleição do motor (Classe C) |
| Mover variantes/backows `shadow_loop_*` para `legacy/` não-importável | Impedir import acidental | Médio | Alta | Preservação concluída |
| Bloquear `_get_sample_data()` em produção (CT-06) → HOLD | Impedir dado sintético | Baixo | Alta | Teste de regressão |
| Acoplar execução ao SL/TP do sinal (CT-04) | Ledger = ordem | Médio | Alta | Teste em demo |
| Corrigir/!remover "8 filtros PASS" cosmético (CT-10) | Integridade de auditoria | Baixo | Alta | Decisão de formato FOR11 |
| Isolar ambientes `{dev,test,demo,exec}` | Segregação mandatória | Médio | Alta | Aval Conselho |
| Corrigir bug `MT5BulletproofLayer`/`_erc` no legacy **ou** descontinuá-lo | Motor B está quebrado | Médio | Alta | Eleição do motor |

## Classe C — Exige deliberação do Conselho

| Ação | Justificativa | Risco | Reversibilidade | Dependência |
|---|---|---|---|---|
| Eleição formal do motor soberano único | Fim da autoridade dupla | Alto | — | Conselho |
| Reclassificação oficial de motores (soberano/legacy/desativado) | Governança | Alto | — | Conselho |
| Autorização de saneamento estrutural irreversível | Limpeza de resíduos | Alto | Parcial | Conselho |
| Autorização para retomar evolução/calibração | Sair do congelamento | Alto | — | Conselho |

---

# ENTREGÁVEL 5 — ZONA DE PRESERVAÇÃO FORENSE (BLOCO V)

**Regra:** os itens abaixo **NÃO devem ser alterados, apagados, sobrescritos, movidos ou "limpos"** até deliberação. Prazo de preservação: **até decisão formal do Conselho**. Condição de liberação: autorização explícita do CEO/Conselho registrada.

| Item | Caminho | Motivo de preservação | Risco se alterado |
|---|---|---|---|
| Flags congeladas | `config/live_flags.json` | Prova de mistura temporal (freeze 09/06) | Perda da prova CT-03 |
| Lock órfão | `audit/paper/omega_runner.lock` | Prova de resíduo temporal (07/06) | Perda da prova CT-02 |
| MUTEX global | `audit/.omega_system.lock` | Prova de mecanismo de lock sem TTL | Perda de evidência de autoridade |
| Estado VCB | `audit/paper/vcb_state.json` | Estado restaurado em runtime (L1 do log) | Perda de rastro de runtime |
| Log do último run | `audit/paper/paper_loop_20260611_203401.log` | **Prova do crash do motor B** | Perda da prova central de runtime |
| Logs sintéticos | `logs/decision_trace.jsonl`, `logs/execution_log.jsonl` | Prova de stubs de teste em diretório operacional | Perda da prova de contaminação |
| Motores concorrentes | `core_engines/shadow_loop.py`, `shadow_loop_v33_final.py` | Objeto da disputa de soberania | Perda do objeto de análise |
| Variantes shadow_loop | 8× `shadow_loop_*BACKUP*/v33*/_diagnostic/_original/_micro_retry` (`core_engines/`) | Prova de proliferação | Perda do inventário |
| Wrapper paper | `scripts/omega_paper_loop_24x7.py` | Elo Universo B | Perda do rastro de cadeia |
| Scripts `.ps1` | `scripts/run_omega_24x7*.ps1`, `omega_demo_go_live.ps1`, `run_p0_smoke_ceo.ps1`, `psa_night_experiment_start.ps1` | Prova de quem arranca o legacy | Perda da prova de autoridade |
| Fallback sintético | `agent_ia/core/omega_strategy_catalog.py` (1093-1268) | Prova CT-06 | Perda do objeto |
| Catálogo/orquestrador | `agent_ia/core/omega_global_orchestrator.py` | Prova de chamada a `build_market_data` (227,652) | Perda do rastro |
| Documento-Mestre v1.0 + este adendo | pasta do Conselho (Etapa 180626) | Base de deliberação | Perda da narrativa íntegra |

---

# RECLASSIFICAÇÃO FINAL DOS ITENS (resumo)

| ID | Item | Status final | Classificação |
|---|---|---|---|
| CT-04 | Execução ignora SL/TP do sinal (200/400 fixos) | [VERIFICADO] | Contaminante ativo (v33) |
| CT-05 | OHLCV CSV + harmonic lookahead | [VERIFICADO] | Contaminante só no Universo B; NÃO MATERIAL p/ v33 |
| CT-06 | `_get_sample_data()` sintético no caminho oficial | [VERIFICADO] | PROIBIDO em produção |
| CT-08 | `OMEGA_TEST_HARNESS` (flag) | [REFUTADO] (log-only) | NÃO MATERIAL (flag); precedência env>file [VERIFICADO] material |
| CT-10 | "8 filtros PASS" hardcoded | [VERIFICADO] | Enganoso para auditoria |
| RT-01 | Motor B crasha no arranque (11/06) | [VERIFICADO] | Falha operacional crítica |
| RT-02 | Logs de execução sintéticos em `logs/` | [VERIFICADO] | Resíduo de teste em diretório operacional |

---

# CRITÉRIOS DE ACEITAÇÃO (autoavaliação)

- [x] Os 4 itens prioritários (CT-05, CT-06, CT-08, CT-10) saíram de estado aberto.
- [x] Existe prova de **runtime** (não só estrutural): crash do motor B + logs sintéticos.
- [x] Precedência de autoridade formalmente mapeada (Entregável 3).
- [x] Separação ação técnica (A/B) vs governança (C) (Entregável 4).
- [x] Lista explícita de preservação forense (Entregável 5).
- [x] Toda conclusão com marcação de status.

---

# LIMITAÇÕES

- A enumeração exata de env vars **da sessão de 11/06** não foi capturada (o log não registra o ambiente completo) → item de runtime #5 fica **[INCONCLUSIVO]** para aquela sessão; a precedência env>file é, porém, **[VERIFICADO]** no código.
- Não há logs de execução íntegra recente do motor oficial `v33_final` nos diretórios inspecionados; ausência de prova **não é** prova de ausência — fica **[INCONCLUSIVO]** se o v33 já operou integralmente.
- Nada foi alterado, movido ou apagado para produzir este adendo.

---

# VEREDITO PRÉ-CONSELHO

A verdade operacional é **mais grave que o diagnóstico estrutural**: além da contaminação arquitetural (dois motores, sem segregação, resíduos temporais), o **motor operacional 24/7 não inicializa** na última execução registrada, e os únicos logs de "execução" são **sintéticos**. Portanto, o material é:
- **suficiente** para congelamento prudencial e preservação de prova **agora**;
- **suficiente** para o Conselho deliberar sobre **eleição de motor soberano** e **segregação TEST/EXEC**;
- as correções técnicas (Classe B) só devem ocorrer **após** a eleição do motor (Classe C).

**Recomendação:** congelamento imediato + preservação forense (Classe A, executável já com aval), deliberação do Conselho sobre motor soberano (Classe C), e só então saneamento técnico (Classe B).

---

*Fim do Adendo v1.1 — AIC / Tech Lead — 2026-06-18.*
