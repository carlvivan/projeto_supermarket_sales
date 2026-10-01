import pandas as pd


# ==========================================
# 1. LEITURA DA BASE ORIGINAL
# ==========================================

caminho_arquivo = "data/raw/SuperMarket Analysis.csv"

df = pd.read_csv(caminho_arquivo)

print("\n--- BASE ORIGINAL ---")
print(f"Linhas: {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")


# ==========================================
# 2. VERIFICAÇÃO DE VALORES NULOS
# ==========================================

print("\n--- VALORES NULOS ANTES DO TRATAMENTO ---")
print(df.isnull().sum())


# ==========================================
# 3. RENOMEAÇÃO DAS COLUNAS
# ==========================================

df = df.rename(columns={
    "Invoice ID": "id_venda",
    "Branch": "filial",
    "City": "cidade",
    "Customer type": "tipo_cliente",
    "Gender": "genero",
    "Product line": "linha_produto",
    "Unit price": "preco_unitario",
    "Quantity": "quantidade",
    "Tax 5%": "imposto",
    "Sales": "valor_total",
    "Date": "data_venda",
    "Time": "hora_venda",
    "Payment": "forma_pagamento",
    "cogs": "custo_mercadoria",
    "gross margin percentage": "margem_percentual",
    "gross income": "receita_bruta",
    "Rating": "avaliacao"
})


print("\n--- COLUNAS APÓS RENOMEAÇÃO ---")
print(df.columns.tolist())


# ==========================================
# 4. CONVERSÃO DOS TIPOS NUMÉRICOS
# ==========================================

colunas_numericas = [
    "preco_unitario",
    "quantidade",
    "imposto",
    "valor_total",
    "custo_mercadoria",
    "margem_percentual",
    "receita_bruta",
    "avaliacao"
]

for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(df[coluna], errors="coerce")


# ==========================================
# 5. CONVERSÃO DA DATA
# ==========================================

df["data_venda"] = pd.to_datetime(
    df["data_venda"],
    format="%m/%d/%Y",
    errors="coerce"
)


# ==========================================
# 6. CONVERSÃO DA HORA
# ==========================================

df["hora_venda"] = pd.to_datetime(
    df["hora_venda"],
    format="mixed",
    errors="coerce"
).dt.time


# ==========================================
# 7. TRATAMENTO DOS VALORES NULOS
# ==========================================

print("\n--- VALORES NULOS APÓS CONVERSÕES ---")
print(df.isnull().sum())

print("\n--- EXEMPLO DOS DADOS APÓS CONVERSÃO ---")
print(df.head())


# Remove registros que possuem valores nulos
# nas colunas essenciais
colunas_obrigatorias = [
    "id_venda",
    "filial",
    "cidade",
    "linha_produto",
    "preco_unitario",
    "quantidade",
    "valor_total",
    "data_venda",
    "hora_venda",
    "forma_pagamento"
]

df = df.dropna(subset=colunas_obrigatorias)


# ==========================================
# 8. REMOÇÃO DE DUPLICIDADES
# ==========================================

duplicados = df.duplicated().sum()

print("\n--- DUPLICIDADES ---")
print(f"Duplicidades encontradas: {duplicados}")

df = df.drop_duplicates()


# ==========================================
# 9. CRIAÇÃO DA COLUNA DIA DA SEMANA
# ==========================================

df["dia_semana"] = df["data_venda"].dt.day_name()


# ==========================================
# 10. TRADUÇÃO DOS DIAS DA SEMANA
# ==========================================

dias_semana = {
    "Monday": "Segunda-feira",
    "Tuesday": "Terça-feira",
    "Wednesday": "Quarta-feira",
    "Thursday": "Quinta-feira",
    "Friday": "Sexta-feira",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}

df["dia_semana"] = df["dia_semana"].map(dias_semana)


# ==========================================
# 11. CONFERÊNCIA FINAL
# ==========================================

print("\n--- BASE TRATADA ---")
print(f"Linhas: {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")

print("\n--- TIPOS DE DADOS ---")
print(df.dtypes)

print("\n--- PRIMEIRAS 5 LINHAS ---")
print(df.head())


# ==========================================
# 12. SALVAR A BASE TRATADA
# ==========================================

caminho_saida = "data/processed/vendas_tratadas.csv"

df.to_csv(
    caminho_saida,
    index=False,
    encoding="utf-8-sig"
)

print("\n--- EXPORTAÇÃO CONCLUÍDA ---")
print(f"Arquivo salvo em: {caminho_saida}")