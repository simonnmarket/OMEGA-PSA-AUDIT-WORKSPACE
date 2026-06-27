# CRITÉRIOS DE GATE FUNCIONAL

**ID:** CRITERIOS-GATE-FUNCIONAL  
**Data:** 2026-06-27  
**Status:** VIGENTE  
**Responsável:** Principal Solution Architect PSA  
**Referência:** OMEGA-CONSTITUTION-001 · METODOLOGIA-PARIDADE-FUNCIONAL

---

## 1. Objetivo

Definir critérios objetivos para aprovação de um **Gate Funcional**, separando-o definitivamente do **Gate Arquitetural**.

---

## 2. Tipos de Gate

### Gate Arquitetural

Valida:

- contratos bem definidos;
- organização de código;
- isolamento de responsabilidades;
- CI passando;
- governança aplicada;
- determinismo demonstrado.

### Gate Funcional

Valida:

- comportamento equivalente ao legado;
- decisões idênticas para entradas equivalentes;
- algoritmos preservados ou demonstradamente equivalentes;
- filtros e transformações com mesma resposta;
- estratégias com mesma sequência de estados;
- estados de exceção com mesmo tratamento;
- fluxo operacional preservado.

---

## 3. Critérios Gerais de Gate Funcional

Para que um componente seja aprovado no Gate Funcional, deve atender:

### GF-01 — Inventário

O componente possui entrada correspondente no Inventário do OMEGA_OS_Kernel.

### GF-02 — Classificação

A classificação (PORTAR / REESCREVER / DESCARTAR / REFERÊNCIA) foi aprovada pelo Conselho.

### GF-03 — Mapeamento

O componente está vinculado a uma entrada na Migration Traceability Matrix.

### GF-04 — Golden Outputs

Existem saídas de referência do legado para entradas canônicas.

### GF-05 — Teste de Paridade

O componente Sovereign reproduz as Golden Outputs dentro das tolerâncias definidas.

### GF-06 — Shadow Mode

Quando aplicável, o componente foi executado em paralelo com o legado sem divergências críticas.

### GF-07 — Documentação

A equivalência funcional está documentada, incluindo:

- descrição do comportamento legado;
- descrição da implementação Sovereign;
- prova de equivalência;
- tolerâncias aplicadas;
- limitações conhecidas.

### GF-08 — Aprovação do Conselho

O Gate Funcional só é fechado por deliberação do Conselho.

---

## 4. Critérios Específicos por Componente

### Motores de Indicador

- RSI/EMA: comparação direta com golden outputs.
- Kalman: equivalência de resposta a sinais de teste.
- Confluência: mesma agregação de sinais para mesmo conjunto de indicadores.

### Market Data

- Mesmas barras OHLCV para mesma requisição.
- Mesmo tratamento de falhas e fallback.
- Mesma política de staleness.

### Position Manager

- Replay de eventos produz o mesmo estado final.
- PnL calculado igual dentro de tolerância.
- Exposição e net volume consistentes.

### Risk Engine

- Mesmas decisões de sizing para mesma exposição.
- Mesmos SL/TP para mesma estratégia.
- Mesmos limites de risco respeitados.

### Strategy Engine

- Mesma sequência de sinais para mesma série de mercado.
- Mesmos estados internos para mesmas condições.

### Execution Engine

- Mesma lógica de envio de ordens.
- Mesma validação de modo de operação.
- Mesmo tratamento de rejeições e falhas.

---

## 5. Tolerâncias

Ver `METODOLOGIA-PARIDADE-FUNCIONAL.md`.

---

## 6. Processo de Abertura/Fechamento

### Abertura

1. Conselho autoriza a abertura do Gate Funcional para um componente.
2. PSA publica critérios específicos.
3. AIC prepara evidências.

### Fechamento

1. AIC submete evidências de paridade.
2. PSA valida evidências.
3. Conselho delibera.
4. Se aprovado, publica `DEC-GATE-FUNC-<COMPONENTE>-001`.

---

## 7. Assinatura

**Principal Solution Architect PSA**  
**2026-06-27**
