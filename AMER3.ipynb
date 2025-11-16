# AMER3 (Americanas) — gráfico 2022 até hoje (Yahoo Finance)

import datetime as dt
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# 1) Parâmetros
ticker = "AMER3.SA"          # símbolo no Yahoo para Americanas na B3
inicio = "2022-01-01"
fim = dt.date.today().isoformat()

# 2) Baixar preços ajustados (fecha) do Yahoo
df = yf.download(ticker, start=inicio, end=fim, auto_adjust=True, progress=False)

if df.empty:
    raise SystemExit("Sem dados retornados. Verifique conexão e o ticker 'AMER3.SA'.")

# 3) Preparar base (fechamento ajustado)
preco = df[("Close", ticker)].rename("Preço (ajustado)")

# 4) Plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(preco.index, preco.values, linewidth=1.5)
ax.set_title("AMER3", fontsize=12)
ax.set_xlabel("Data")
ax.set_ylabel("Preço (R$)")

# Formatação de datas e grade
ax.xaxis.set_major_formatter(DateFormatter("%b/%Y"))
ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

# 5) (Opcional) Marcar eventos relevantes — edite datas se quiser
eventos = {
    "": "2023-01-11",
    # "Queda acentuada no pregão": "2023-01-13",
    # "Pedido de RJ": "2023-01-19",
}
for nome, data_str in eventos.items():
    d = pd.to_datetime(data_str)
    if preco.index.min() <= d <= preco.index.max():
        ax.axvline(d, linestyle=":", linewidth=1)
        ax.text(d, ax.get_ylim()[1], f"  {nome}\n({d.date()})",
                va="top", ha="left", fontsize=8)

plt.tight_layout()

plt.show()
