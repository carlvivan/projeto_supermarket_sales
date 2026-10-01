# 📊 Projeto Supermarket Sales --- Análise de Dados

## 📌 Sobre o projeto

Este projeto apresenta um fluxo completo de análise de dados utilizando
uma base de vendas de um supermercado.

O projeto foi desenvolvido com foco em **tratamento de dados, ETL, banco
de dados, consultas SQL, análise estatística e visualização de
informações**.

A base original foi tratada com Python e Pandas, armazenada em uma
estrutura organizada e posteriormente utilizada no PostgreSQL para
realização de consultas e análises.

---

## 🎯 Objetivo

O objetivo do projeto é transformar uma base de vendas bruta em uma base
de dados tratada e organizada, permitindo realizar análises sobre:

- quantidade de vendas;
- faturamento;
- filiais;
- linhas de produtos;
- formas de pagamento;
- cidades;
- gênero;
- tipo de cliente;
- dia da semana;
- avaliações dos produtos;
- ticket médio;
- maior venda.

O projeto também busca demonstrar, na prática, um fluxo de trabalho de
análise de dados utilizando **Python, Pandas, PostgreSQL e SQL**.

---

## 🛠️ Tecnologias utilizadas

- **Python 3.12**
- **Pandas**
- **Matplotlib**
- **PostgreSQL**
- **SQL**
- **DBeaver**
- **Visual Studio Code**
- **Git/GitHub**

---

## 📁 Estrutura do projeto

```text
projeto_supermarket_sales/
│
├── data/
│   ├── raw/
│   │   └── SuperMarket Analysis.csv
│   │
│   └── processed/
│       └── vendas_tratadas.csv
│
├── resultados/
│   ├── faturamento_por_filial.png
│   ├── faturamento_por_linha_produto.png
│   ├── vendas_por_dia_semana.png
│   └── formas_pagamento.png
│
├── sql/
│   ├── 01_criar_banco.sql
│   ├── 02_criar_tabelas.sql
│   └── 03_consultas.sql
│
├── src/
│   ├── 01_leitura_dados.py
│   ├── 02_etl_vendas.py
│   └── 03_estatistica.py
│
├── requirements.txt
└── README.md
```

---

# 🔄 ETL --- Tratamento dos dados

O processo de ETL foi realizado utilizando Python e Pandas.

## 1. Leitura da base original

A base original é carregada a partir de:

```text
data/raw/SuperMarket Analysis.csv
```

A leitura é realizada com:

```python
df = pd.read_csv(caminho_arquivo)
```

Também é realizada uma verificação inicial da quantidade de linhas,
colunas e valores nulos.

---

## 2. Renomeação das colunas

As colunas originais foram padronizadas para nomes em português.

Alguns exemplos:

  Original                  Tratada

---

  Invoice ID                id_venda
  Branch                    filial
  City                      cidade
  Customer type             tipo_cliente
  Gender                    genero
  Product line              linha_produto
  Unit price                preco_unitario
  Quantity                  quantidade
  Tax 5%                    imposto
  Sales                     valor_total
  Date                      data_venda
  Time                      hora_venda
  Payment                   forma_pagamento
  cogs                      custo_mercadoria
  gross margin percentage   margem_percentual
  gross income              receita_bruta
  Rating                    avaliacao

---

## 3. Conversão dos tipos de dados

As colunas numéricas foram convertidas para tipos numéricos utilizando
`pd.to_numeric()`.

A coluna `data_venda` foi convertida para data utilizando
`pd.to_datetime()`.

A coluna `hora_venda` também foi convertida para representar somente o
horário da venda.

Após as conversões, foi realizada uma nova verificação dos valores
nulos.

---

## 4. Tratamento de valores nulos

Foram definidas colunas consideradas essenciais para os registros de
vendas:

- id_venda
- filial
- cidade
- linha_produto
- preco_unitario
- quantidade
- valor_total
- data_venda
- hora_venda
- forma_pagamento

Registros que apresentavam valores nulos nessas colunas foram removidos.

---

## 5. Remoção de duplicidades

A base foi verificada quanto à existência de registros duplicados.

Depois da verificação, os registros duplicados foram removidos
utilizando:

```python
df = df.drop_duplicates()
```

---

## 6. Criação do dia da semana

Foi criada uma nova coluna chamada:

```text
dia_semana
```

Ela foi obtida a partir da coluna `data_venda`.

```python
df["dia_semana"] = df["data_venda"].dt.day_name()
```

Como o resultado inicial do Pandas utiliza os nomes dos dias em inglês,
foi realizada uma tradução para português:

```text
Monday      → Segunda-feira
Tuesday     → Terça-feira
Wednesday   → Quarta-feira
Thursday    → Quinta-feira
Friday      → Sexta-feira
Saturday    → Sábado
Sunday      → Domingo
```

---

## 7. Base tratada

Após o processo de tratamento, a base passou a possuir:

- **1.000 linhas**
- **18 colunas**

A base tratada foi exportada para:

```text
data/processed/vendas_tratadas.csv
```

---

# 🗄️ Banco de dados PostgreSQL

A base tratada também foi carregada no PostgreSQL.

Foram utilizadas duas tabelas principais no projeto:

```text
raw_vendas
vendas
```

A tabela `raw_vendas` representa a base de origem utilizada nas análises
iniciais.

A tabela `vendas` representa a base tratada e preparada para as análises
finais.

A importação da base tratada foi realizada utilizando o DBeaver.

---

# 🔎 Consultas SQL

O arquivo:

```text
sql/03_consultas.sql
```

contém as consultas utilizadas no projeto.

As consultas foram organizadas em duas etapas:

### Consultas da base bruta

As consultas iniciais trabalham com:

```text
raw_vendas
```

### Consultas da base tratada

As consultas finais trabalham com:

```text
vendas
```

Entre as análises realizadas estão:

- quantidade total de registros;
- quantidade de vendas por filial;
- faturamento por filial;
- faturamento por linha de produto;
- quantidade de vendas por forma de pagamento;
- ticket médio;
- maior venda;
- avaliação média por linha de produto;
- quantidade de vendas por dia da semana;
- faturamento por cidade;
- faturamento por gênero;
- quantidade de vendas por tipo de cliente;
- faturamento por tipo de cliente.

---

# 📈 Principais resultados

Com base nas consultas realizadas sobre a tabela tratada:

## Total de vendas

```text
1.000 registros
```

## Faturamento total

```text
R$ 322.967,43
```

## Ticket médio

```text
R$ 322,97
```

## Maior venda

```text
R$ 1.042,65
```

## Vendas por filial

  Filial     Vendas

---

  Alex          340
  Cairo         332
  Giza          328

## Faturamento por filial

  Filial        Faturamento

---

  Giza       R\$ 110.568,86
  Alex       R\$ 106.200,57
  Cairo      R\$ 106.198,00

## Faturamento por linha de produto

  Linha de produto             Faturamento

---

  Food and beverages         R\$ 56.144,96
  Sports and travel          R\$ 55.123,00
  Electronic accessories     R\$ 54.337,64
  Fashion accessories        R\$ 54.306,03
  Home and lifestyle         R\$ 53.861,96
  Health and beauty          R\$ 49.193,84

## Formas de pagamento

  Forma de pagamento     Quantidade

---

  Ewallet                       345
  Cash                          344
  Credit card                   311

## Vendas por dia da semana

  Dia               Vendas

---

  Sábado               164
  Terça-feira          158
  Quarta-feira         143
  Sexta-feira          139
  Quinta-feira         138
  Domingo              133
  Segunda-feira        125

## Faturamento por cidade

  Cidade           Faturamento

---

  Naypyitaw     R\$ 110.568,86
  Yangon        R\$ 106.200,57
  Mandalay      R\$ 106.198,00

## Faturamento por gênero

  Gênero        Faturamento

---

  Female     R\$ 194.672,22
  Male       R\$ 128.295,21

## Tipo de cliente

Quantidade de vendas:

  Tipo       Vendas

---

  Member        565
  Normal        435

Faturamento:

  Tipo          Faturamento

---

  Member     R\$ 189.695,16
  Normal     R\$ 133.272,27

---


# ❓ Perguntas de negócio e respostas

As análises realizadas sobre a base tratada permitiram responder às principais
perguntas de negócio propostas para o projeto.

| Pergunta de negócio                                        | Resposta                                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------------------- |
| Qual filial apresentou o maior faturamento?                 | **Giza**, com faturamento de **R$ 110.568,86**.             |
| Qual filial realizou a maior quantidade de vendas?          | **Alex**, com **340 vendas**.                               |
| Qual linha de produto apresentou o maior faturamento?       | **Food and beverages**, com **R$ 56.144,96**.               |
| Qual linha de produto recebeu a melhor avaliação média?  | **Food and beverages**, com avaliação média de **7,11**. |
| Qual foi a forma de pagamento mais utilizada?               | **Ewallet**, com **345 vendas**.                            |
| Qual foi o valor médio das vendas?                         | **R$ 322,97**.                                                    |
| Qual foi a maior venda registrada?                          | **R$ 1.042,65**.                                                  |
| Em qual dia da semana ocorreu a maior quantidade de vendas? | **Sábado**, com **164 vendas**.                            |

## 📌 Principais resultados

- **Maior faturamento por filial:** Giza — R$ 110.568,86.
- **Maior quantidade de vendas por filial:** Alex — 340 vendas.
- **Maior faturamento por linha de produto:** Food and beverages — R$ 56.144,96.
- **Melhor avaliação média:** Food and beverages — 7,11.
- **Forma de pagamento mais utilizada:** Ewallet — 345 vendas.
- **Valor médio das vendas:** R$ 322,97.
- **Maior venda registrada:** R$ 1.042,65.
- **Dia com maior quantidade de vendas:** Sábado — 164 vendas.

---

# 📊 Visualizações

Foram gerados quatro gráficos utilizando Matplotlib:

### Faturamento por filial

Arquivo:

```text
resultados/faturamento_por_filial.png
```

### Faturamento por linha de produto

Arquivo:

```text
resultados/faturamento_por_linha_produto.png
```

### Quantidade de vendas por dia da semana

Arquivo:

```text
resultados/vendas_por_dia_semana.png
```

### Quantidade de vendas por forma de pagamento

Arquivo:

```text
resultados/formas_pagamento.png
```

Os gráficos foram salvos com resolução de **300 DPI**.

---

# 🧮 Análise estatística

O arquivo:

```text
src/03_estatistica.py
```

é responsável pelos cálculos estatísticos e pela geração dos gráficos.

Entre os indicadores calculados estão:

- faturamento total;
- ticket médio;
- quantidade total vendida;
- avaliação média;
- faturamento por filial;
- faturamento por linha de produto;
- vendas por dia da semana;
- quantidade de vendas por forma de pagamento.

---

# ▶️ Como executar o projeto

## 1. Instalar as dependências

Com o Python instalado, execute:

```bash
py -3.12 -m pip install -r requirements.txt
```

## 2. Executar a leitura dos dados

```bash
py -3.12 src/01_leitura_dados.py
```

## 3. Executar o tratamento dos dados

```bash
py -3.12 src/02_etl_vendas.py
```

A base tratada será criada em:

```text
data/processed/vendas_tratadas.csv
```

## 4. Executar as análises estatísticas

```bash
py -3.12 src/03_estatistica.py
```

Os gráficos serão gerados na pasta:

```text
resultados/
```

## 5. Executar as consultas SQL

As consultas estão organizadas em:

```text
sql/03_consultas.sql
```

Elas podem ser executadas no PostgreSQL utilizando o DBeaver.

---

# 📚 Aprendizados

Durante o desenvolvimento deste projeto foram trabalhados conceitos de:

- leitura de arquivos CSV;
- análise exploratória de dados;
- tratamento de valores nulos;
- conversão de tipos de dados;
- tratamento de datas e horários;
- remoção de duplicidades;
- criação de novas colunas;
- transformação de dados com Pandas;
- exportação de dados tratados;
- criação e utilização de banco PostgreSQL;
- consultas SQL;
- agregações com `COUNT`, `SUM`, `AVG` e `MAX`;
- `GROUP BY`;
- `ORDER BY`;
- análise estatística;
- visualização de dados com Matplotlib;
- organização de projetos de análise de dados.

---

# 👤 Sobre o autor

Formação:

- Engenharia Têxtil
- Engenharia Civil

Objetivo profissional:

> Desenvolver novas habilidades e evoluir na área de análise de dados e
> programação.

Este projeto faz parte do desenvolvimento prático de conhecimentos em
**Python, análise de dados, SQL e banco de dados**.

---

# 🚀 Próximos passos

Como evolução do projeto, podem ser acrescentados:

- novos indicadores de desempenho;
- novas consultas SQL;
- análises mais detalhadas das vendas;
- novos gráficos;
- dashboard interativo;
- integração com ferramentas de Business Intelligence;
- documentação de análises adicionais.

---

## 📌 Resumo do fluxo

```text
CSV ORIGINAL
     ↓
PYTHON / PANDAS
     ↓
TRATAMENTO DOS DADOS
     ↓
vendas_tratadas.csv
     ↓
POSTGRESQL
     ↓
SQL / DBeaver
     ↓
ANÁLISES
     ↓
MATPLOTLIB
     ↓
GRÁFICOS E RESULTADOS
```

---

**Projeto desenvolvido para prática e demonstração de conhecimentos em
análise de dados, Python, SQL e PostgreSQL.**
