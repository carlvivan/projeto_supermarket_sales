import pandas as pd


# Caminho do arquivo CSV
caminho_arquivo = "data/raw/SuperMarket Analysis.csv"


# Leitura dos dados
df = pd.read_csv(caminho_arquivo)


# Exibe as primeiras linhas
print("\n--- PRIMEIRAS 5 LINHAS ---")
print(df.head())


# Exibe quantidade de linhas e colunas
print("\n--- DIMENSÕES DA BASE ---")
print(f"Linhas: {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")


# Exibe os nomes das colunas
print("\n--- COLUNAS ---")
print(df.columns.tolist())


# Exibe os tipos de dados
print("\n--- TIPOS DE DADOS ---")
print(df.dtypes)


# Verifica valores nulos
print("\n--- VALORES NULOS ---")
print(df.isnull().sum())


# Estatísticas descritivas
print("\n--- ESTATÍSTICAS DESCRITIVAS ---")
print(df.describe())