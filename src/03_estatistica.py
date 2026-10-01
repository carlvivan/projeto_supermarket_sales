import pandas as pd


# ==========================================
# 1. LEITURA DA BASE TRATADA
# ==========================================

caminho_arquivo = "data/processed/vendas_tratadas.csv"

df = pd.read_csv(caminho_arquivo)


# ==========================================
# 2. INFORMAÇÕES DA BASE
# ==========================================

print("\n--- BASE TRATADA ---")
print(f"Linhas: {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")


# ==========================================
# 3. FATURAMENTO TOTAL
# ==========================================

faturamento_total = df["valor_total"].sum()

print("\n--- FATURAMENTO TOTAL ---")
print(f"R$ {faturamento_total:,.2f}")


# ==========================================
# 4. TICKET MÉDIO
# ==========================================

ticket_medio = df["valor_total"].mean()

print("\n--- TICKET MÉDIO ---")
print(f"R$ {ticket_medio:,.2f}")


# ==========================================
# 5. QUANTIDADE TOTAL VENDIDA
# ==========================================

quantidade_total = df["quantidade"].sum()

print("\n--- QUANTIDADE TOTAL VENDIDA ---")
print(quantidade_total)


# ==========================================
# 6. AVALIAÇÃO MÉDIA
# ==========================================

avaliacao_media = df["avaliacao"].mean()

print("\n--- AVALIAÇÃO MÉDIA ---")
print(f"{avaliacao_media:.2f}")


# ==========================================
# 7. FATURAMENTO POR FILIAL
# ==========================================

faturamento_filial = (
    df.groupby("filial")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- FATURAMENTO POR FILIAL ---")
print(faturamento_filial)


# ==========================================
# 8. FATURAMENTO POR LINHA DE PRODUTO
# ==========================================

faturamento_produto = (
    df.groupby("linha_produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- FATURAMENTO POR LINHA DE PRODUTO ---")
print(faturamento_produto)


# ==========================================
# 9. VENDAS POR DIA DA SEMANA
# ==========================================

vendas_dia = (
    df.groupby("dia_semana")
    .size()
    .sort_values(ascending=False)
)

print("\n--- VENDAS POR DIA DA SEMANA ---")
print(vendas_dia)


# ==========================================
# 10. FORMA DE PAGAMENTO
# ==========================================

pagamento = (
    df["forma_pagamento"]
    .value_counts()
)

print("\n--- FORMA DE PAGAMENTO ---")
print(pagamento)

# ==========================================
# 11. GRÁFICOS
# ==========================================

import matplotlib.pyplot as plt
import os


# ==========================================
# CRIAR PASTA DE RESULTADOS
# ==========================================

os.makedirs("resultados", exist_ok=True)


# ==========================================
# GRÁFICO 1 - FATURAMENTO POR FILIAL
# ==========================================

plt.figure(figsize=(8, 5))

ax = faturamento_filial.plot(kind="bar")

plt.title("Faturamento por Filial")
plt.xlabel("Filial")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=0)

for container in ax.containers:
    ax.bar_label(
        container,
        labels=[
            f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            for valor in faturamento_filial
        ],
        padding=3
    )

plt.tight_layout()

plt.savefig(
    "resultados/faturamento_por_filial.png",
    dpi=300
)

plt.close()


# ==========================================
# TRADUÇÃO DAS LINHAS DE PRODUTO
# ==========================================

traducao_produtos = {
    "Food and beverages": "Alimentos e bebidas",
    "Sports and travel": "Esportes e viagens",
    "Electronic accessories": "Acessórios eletrônicos",
    "Fashion accessories": "Acessórios de moda",
    "Home and lifestyle": "Casa e estilo de vida",
    "Health and beauty": "Saúde e beleza"
}

faturamento_produto_pt = faturamento_produto.rename(
    index=traducao_produtos
)


# ==========================================
# GRÁFICO 2 - FATURAMENTO POR PRODUTO
# ==========================================

plt.figure(figsize=(10, 6))

dados_produto = faturamento_produto_pt.sort_values()

ax = dados_produto.plot(kind="barh")

plt.title("Faturamento por Linha de Produto")
plt.xlabel("Faturamento (R$)")
plt.ylabel("Linha de Produto")

for container in ax.containers:
    ax.bar_label(
        container,
        labels=[
            f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            for valor in dados_produto
        ],
        padding=3
    )

plt.tight_layout()

plt.savefig(
    "resultados/faturamento_por_linha_produto.png",
    dpi=300
)

plt.close()


# ==========================================
# GRÁFICO 3 - VENDAS POR DIA DA SEMANA
# ==========================================

ordem_dias = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo"
]

vendas_dia_grafico = (
    df["dia_semana"]
    .value_counts()
    .reindex(ordem_dias)
)

plt.figure(figsize=(10, 5))

ax = vendas_dia_grafico.plot(kind="bar")

plt.title("Quantidade de Vendas por Dia da Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Quantidade de Vendas")
plt.xticks(rotation=45)

for container in ax.containers:
    ax.bar_label(
        container,
        padding=3
    )

plt.tight_layout()

plt.savefig(
    "resultados/vendas_por_dia_semana.png",
    dpi=300
)

plt.close()


# ==========================================
# GRÁFICO 4 - FORMAS DE PAGAMENTO
# ==========================================

pagamento_grafico = pagamento.rename(
    index={
        "eWallet": "Carteira digital",
        "Cash": "Dinheiro",
        "Credit card": "Cartão de crédito"
    }
)

plt.figure(figsize=(8, 5))

ax = pagamento_grafico.plot(kind="bar")

plt.title("Quantidade de Vendas por Forma de Pagamento")
plt.xlabel("Forma de Pagamento")
plt.ylabel("Quantidade de Vendas")
plt.xticks(rotation=0)

for container in ax.containers:
    ax.bar_label(
        container,
        padding=3
    )

plt.tight_layout()

plt.savefig(
    "resultados/formas_pagamento.png",
    dpi=300
)

plt.close()


# ==========================================
# FINALIZAÇÃO
# ==========================================

print("\n--- GRÁFICOS GERADOS ---")
print("1. faturamento_por_filial.png")
print("2. faturamento_por_linha_produto.png")
print("3. vendas_por_dia_semana.png")
print("4. formas_pagamento.png")
print("\nArquivos salvos na pasta: resultados/")