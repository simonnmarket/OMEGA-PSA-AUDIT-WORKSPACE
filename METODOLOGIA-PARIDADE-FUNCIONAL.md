# METODOLOGIA DE PARIDADE FUNCIONAL

**ID:** METODOLOGIA-PARIDADE-FUNCIONAL  
**Data:** 2026-06-27  
**Status:** VIGENTE  
**Responsável:** Principal Solution Architect PSA  
**Referência:** OMEGA-CONSTITUTION-001 · ETAPA-3.5

---

## 1. Objetivo

Definir critérios objetivos e reprodutíveis para demonstrar que um componente do OMEGA-Kernel-Sovereign possui **paridade funcional** com seu equivalente no OMEGA_OS_Kernel.

---

## 2. Definição de Paridade Funcional

> Paridade funcional significa que **entradas equivalentes** produzem **decisões equivalentes** dentro das **tolerâncias aprovadas** pelo Conselho.

A paridade não exige cópia de código. Exige cópia de comportamento.

---

## 3. Critérios por Domínio

### 3.1 Indicadores e Motores Estatísticos

- **Entrada:** série de preços idêntica.
- **Saída:** valores do indicador dentro de tolerância ε.
- **Tolerância:** ε = 1e-3 (0.1%) para indicadores normalizados.
- **Método:** comparação de Golden Outputs do legado vs. Sovereign.

### 3.2 Sinais de Decisão

- **Entrada:** mesmo estado de mercado e portfólio.
- **Saída:** sinal discreto (comprar / vender / neutro).
- **Tolerância:** 0% divergência.
- **Método:** comparação exata para cada cenário de teste.

### 3.3 Risk Engine

- **Entrada:** exposição, volatilidade, correlações.
- **Saída:** tamanho de posição, SL, TP, limites.
- **Tolerância:** ε = 1e-4 para preços; ε = 1e-6 para volumes.
- **Método:** comparação de decisões de risco para portfólios de referência.

### 3.4 Execution Engine

- **Entrada:** ordem, preço, volume, broker.
- **Saída:** ordem enviada, status, slippage.
- **Tolerância:** 0% divergência para lógica; tolerância para slippage conforme mercado.
- **Método:** simulação em ambiente de teste e shadow mode.

### 3.5 Position Management

- **Entrada:** eventos de abertura, modificação, fechamento, mark price.
- **Saída:** estado de posição, PnL, exposição.
- **Tolerância:** ε = 1e-6 para volumes; ε = 1e-4 para preços.
- **Método:** replay de eventos e comparação de snapshots.

---

## 4. Métodos de Prova

### 4.1 Golden Outputs

Capturar saídas do OMEGA_OS_Kernel para entradas canônicas e usá-las como baseline de referência.

### 4.2 Shadow Mode

Executar OMEGA_OS_Kernel e OMEGA-Kernel-Sovereign em paralelo com mesmas entradas e comparar saídas em tempo real ou em batch.

### 4.3 Regression Suite de Paridade

Testes automatizados que comparam saídas entre legado e Sovereign. Devem fazer parte do CI.

### 4.4 Análise Estatística

Para componentes estocásticos, usar testes como:

- Kolmogorov-Smirnov
- Comparação de médias e variâncias
- Backtest comparativo

### 4.5 Prova Formal

Para algoritmos críticos, documentar equivalência matemática ou usar invariantes verificáveis.

---

## 5. Tolerâncias Padrão

| Tipo de Saída | Tolerância (ε) | Observação |
|---------------|----------------|------------|
| Preços | 1e-4 | 4 casas decimais |
| Volumes | 1e-6 | 6 casas decimais |
| Indicadores | 1e-3 | 0.1% |
| Sinais discretos | 0% | Devem ser idênticos |
| Timestamps | 1ms | Sincronização de mercado |
| PnL | 1e-4 | Em moeda base |

Tolerâncias específicas podem ser ajustadas pelo Conselho por componente.

---

## 6. Critérios de Descarte

Um componente pode ser classificado como DESCARTAR apenas se:

- Não existir evidência de uso operacional nos últimos 12 meses;
- Seu descarte for aprovado pelo Conselho;
- O impacto funcional for documentado;
- Uma alternativa equivalente já existir no Sovereign.

---

## 7. Critérios de Reescrita

Reescrita só é autorizada quando:

- O componente legado está contaminado e não pode ser portado;
- A equivalência funcional puder ser demonstrada;
- O Conselho aprovar a reescrita formalmente.

---

## 8. Integração com CI

O CI do OMEGA-Kernel-Sovereign deverá incluir, além dos testes atuais, uma **fase de paridade** que:

- carrega Golden Outputs do legado;
- executa os componentes equivalentes do Sovereign;
- compara saídas dentro das tolerâncias;
- falha se a paridade não for atingida.

---

## 9. Assinatura

**Principal Solution Architect PSA**  
**2026-06-27**
