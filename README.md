# Caso Americanas & Indústria de Fundos de Crédito Privado (Brasil, 2022–2024)

Trabalho de Conclusão de Curso em Engenharia Física – Universidade Federal de São Carlos (UFSCar)  
Autor: Felipe Faria Cazetta  

---

## 🎯 Tema

**“Análise quantitativa do impacto de eventos corporativos e macroeconômicos sobre fundos de crédito privado no Brasil (2022–2024)”**

O repositório foca principalmente no **caso Americanas (jan/2023)** como estudo de caso central, mas está estruturado para analisar também outros eventos relevantes que afetaram fundos de crédito privado no período.

---

## ✅ Objetivo

Mensurar e explicar o impacto de **eventos corporativos** e **macroeconômicos** sobre fundos brasileiros de renda fixa (segmento de **crédito privado**, segundo a CVM) entre **2022 e 2024**, com ênfase em diferenças entre:

- **Gestoras Top 15** por PL consolidado (31/12/2024)  
- **Gestoras Bottom 15** por PL consolidado (31/12/2024)  

Principais perguntas empíricas:

- Fundos de gestoras maiores sofrem menos (em retorno e captação) em eventos de estresse?
- Há evidência de **retorno ajustado ao risco superior** nos fundos das grandes gestoras?
- Eventos como o caso Americanas geram realocação estrutural de PL entre gestoras?

---

## 🧾 Dados

### 1. Seleção inicial de fundos (CVM – posição em 18/08/2025)

Filtros aplicados:

- Categoria: **Renda Fixa** / **Crédito Privado**
- Somente fundos que **aderiram à Resolução CVM 175**
- **Não exclusivos**
- **Não fundos de cotas**
- Situação: **ativos / em funcionamento**
- Data de início: **fundos nascidos antes de 2022**

### 2. Séries históricas (2022–2024)

Para o conjunto de fundos selecionados são extraídos e consolidados (via CVM):

- **cotas** (preço da cota diária)
- **capliq** (captação líquida)
- **PL** (patrimônio líquido)

A partir disso, são construídas:

- Séries de **retorno diário dos fundos**
- Séries de **retorno diário do CDI** e da **SELIC** (benchmarks)

### 3. Classificação por gestora

- Cálculo do **PL total por gestora em 31/12/2024**
- Definição dos grupos:
  - **Top 15 gestoras** por PL
  - **Bottom 15 gestoras** por PL  
- (Opcional) Top 20 gestores / fundos por PL para análises adicionais de concentração.

---

## 🧪 Metodologia

### 1. Consolidação e pré-processamento

1. Merge entre:
   - base cadastral dos fundos (filtros acima)  
   - histórico de cotas / capliq / PL (2022–2024)
2. Cálculo do **retorno diário** dos fundos:
   - \( R_{i,t} = \frac{Cota_{i,t}}{Cota_{i,t-1}} - 1 \)
3. Construção do benchmark:
   - Retorno diário do **CDI**
   - Retorno diário da **SELIC**

---

### 2. Análise Descritiva

Para cada grupo (Top 15 x Bottom 15) e, quando relevante, por fundo:

- **Retorno acumulado** no período, com comparação versus **CDI acumulado**.
- Evolução da **PL consolidada** (nível e crescimento).
- **Captação líquida acumulada**, com foco em:
  - períodos pré e pós-eventos
  - possíveis migrações de PL entre grupos.

---

### 3. Estudo de Evento – Caso Americanas (jan/2023)

Evento principal:

- **13/01/2023** – divulgação do fato relevante sobre a fraude contábil da Americanas.

#### 3.1. Janela de evento

- Janela principal: **[-20, +60] dias úteis** ao redor do evento.
- Possibilidade de testar outras janelas (ex.: [-10, +20]) em análises de robustez.

#### 3.2. Métricas

Para cada fundo \( i \) e dia \( t \):

- **Retorno anormal (AR)**  
  \[
  AR_{i,t} = R_{i,t} - R^{CDI}_t
  \]

- **AAR (Average Abnormal Return)** – média de AR por grupo (Top x Bottom) em cada dia da janela.

- **CAAR (Cumulative AAR)** – soma acumulada da AAR ao longo da janela de evento.

#### 3.3. Testes estatísticos

- Testes de significância para verificar se:
  - AAR/CAAR diferem estatisticamente de zero.
  - Há diferença relevante entre **Top 15** e **Bottom 15**.

Metodologias previstas:

- **t-test** (Student / Welch) para AAR/CAAR.
- (Opcional / robustez): uso de **erros-padrão robustos** (ex.: Newey–West) para lidar com autocorrelação/heteroscedasticidade.

---

### 4. Análise de Risco

Cálculo de métricas de risco para fundos e grupos:

- **Volatilidade histórica** (desvio-padrão dos retornos, em base diária e escalada para mensal/anual quando necessário).
- **Máximo drawdown** (maior queda acumulada a partir de um pico).
- **Sharpe Ratio** ou **Índice de Informação**:
  - \[
    \text{Sharpe} = \frac{R_{fundo} - R_{CDI}}{\sigma_{fundo}}
    \]
- Comparação entre grupos:
  - **Retorno bruto**
  - **Retorno em excesso sobre CDI**
  - **Retorno ajustado ao risco**

Objetivo: verificar se **Top 15** de gestoras entrega melhor relação retorno–risco que **Bottom 15**, especialmente em períodos de estresse.

---

### 5. Captação & PL Pós-Evento

Análise dinâmica da reação dos investidores:

- Evolução do **PL total** dos grupos no tempo.
- **Captação líquida mensal** (e acumulada):
  - Antes do evento (Americanas)
  - Após o evento (jan/2023 em diante)
- Identificação de:
  - **Saída forte de recursos** dos fundos mais afetados.
  - **Possível migração de PL** de gestoras menor porte (Bottom) para maior porte (Top).

---

## 📌 Outros eventos considerados

Além do caso Americanas (jan/2023), a infraestrutura do projeto permite analisar:

- **Light (jun/2023)** – evento corporativo relevante no setor elétrico.
- **Mudanças regulatórias**:
  - Ex.: **Resolução CVM 175** (2023–2024) e seus impactos na indústria de fundos.
- **Decisões de política monetária**:
  - Ciclo de cortes da **SELIC (2023–2024)** e seus efeitos sobre fundos de crédito privado.

Esses eventos podem ser tratados como janelas adicionais de estudo de evento, utilizando a mesma lógica de AR, AAR, CAAR e testes estatísticos.

---

## 🗂 Estrutura do Repositório (sugestão)

```text
.
├── data/
│   ├── raw/          # Dados brutos da CVM (cotas, PL, capliq, cadastro de fundos)
│   ├── interim/      # Bases tratadas / merges intermediários
│   └── processed/    # Painéis finais prontos para análise
├── notebooks/
│   ├── 01_exploratorio.ipynb
│   ├── 02_estudo_evento_americanas.ipynb
│   └── 03_risco_capitacao.ipynb
├── src/
│   ├── data/         # Scripts de extração e limpeza de dados
│   ├── features/     # Cálculo de retornos, AR, AAR, CAAR, métricas de risco
│   ├── models/       # Testes estatísticos, agregações por grupo
│   └── visualization/# Gráficos de retorno, PL, captação, CAAR, etc.
├── reports/
│   ├── figures/      # Gráficos usados no TCC
│   └── tables/       # Tabelas de resultados
└── README.md
