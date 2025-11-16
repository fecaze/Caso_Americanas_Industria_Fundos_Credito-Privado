# Caso_Americanas_Industria_Fundos_Credito-Privado

## Trabalho Final de Curso - Engenharia Física (UFSCar)

## Tema: “Análise quantitativa do impacto de eventos corporativos e macroeconômicos sobre fundos de crédito privado no Brasil (2022–2024)”

## Objetivo: mensurar e explicar o impacto de eventos corporativos e macroeconômicos sobre fundos de renda fixa brasileiros (CVM) entre 2022–2024, com ênfase em diferenças entre gestoras Top 15 e Bottom 15 por PL.

## Metodologia:
1. Pegando dados fundos e classes da CVM (18/08/2025), somente aqueles que aderiram a 175 
    - Parâmetros: 
        - Renda Fixa e Crédito Privado
        - Não Exclusivos
        - Não Cotas
        - Ativos/Funcionando
        - Nasceram antes de 2022
2. Pegando e consolidando 'cotas', 'capliq' e 'pl' de 2022-24 (CVM)
3. Merge entre 1. e 2. (histórico apenas dos fundos selecionados) + Retorno Diário dos fundos + Retorno diário do CDI e SELIC
4. Top 20 assets pelo PL somado 31/12/2024 e o históricos de fundos sob gestão


ANÁLISE
1. Descritivo inicial
    - Retorno acumulado e comparação com o CDI acumulado como benchmark.
    - PL acumulada
    - Captação acumulada

2. Estudo de Evento (caso Americanas – jan/2023)
    - Identificar o evento (13/jan/2023, quando saiu o fato relevante da fraude contábil).
    - Definir janela −20,+60 −20,+60 dias úteis ao redor do evento.
    Calcular:
        - AR (Abnormal Return) = retorno fundo − retorno CDI.
        - AAR (Average Abnormal Return): média dos AR por grupo 
        - CAAR (Cumulative AAR): acumulado na janela.
        - Testar se a queda foi estatisticamente significativa (t-test). ???


3. Análise de Risco
    - Volatilidade histórica (desvio-padrão diário/mensal).
    - Máximo drawdown (maior queda acumulada).
    - Ratio de Sharpe ou Índice de Informação (retorno em excesso sobre CDI / risco).
    - Conclusão: mostrar se Top entrega retorno ajustado ao risco superior.


4. Captação e PL
    - Evolução do PL total dos grupos.
    - Captação líquida mensal acumulada.
    - Mostra se após o evento (Americanas) houve saída forte nos fundos do Bottom.



6. Discussão e Conclusão
    - Qual a evidência empírica: fundos sofreram mais com Americanas?
    - Implicação para investidores: gestoras mais sólidas entregam resiliência.
    - Implicação acadêmica: eficiência da gestão em fundos de crédito privado em eventos de stress.



Americanas (jan/23)
Light (jun/23)
Mudanças regulatórias (ex.: Resolução CVM 175 em 2023–24)
Decisões de política monetária (cortes da Selic em 2023–24)











