CREATE TABLE raw_vendas (
    "Invoice ID" VARCHAR(50),
    "Branch" VARCHAR(10),
    "City" VARCHAR(100),
    "Customer type" VARCHAR(50),
    "Gender" VARCHAR(20),
    "Product line" VARCHAR(150),
    "Unit price" VARCHAR(50),
    "Quantity" VARCHAR(50),
    "Tax 5%" VARCHAR(50),
    "Sales" VARCHAR(50),
    "Date" VARCHAR(50),
    "Time" VARCHAR(50),
    "Payment" VARCHAR(50),
    "cogs" VARCHAR(50),
    "gross margin percentage" VARCHAR(50),
    "gross income" VARCHAR(50),
    "Rating" VARCHAR(50)
);


CREATE TABLE vendas (
    id_venda VARCHAR(50) PRIMARY KEY,
    filial VARCHAR(10) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    tipo_cliente VARCHAR(50),
    genero VARCHAR(20),
    linha_produto VARCHAR(150) NOT NULL,
    preco_unitario NUMERIC(10,2) CHECK (preco_unitario >= 0),
    quantidade INTEGER CHECK (quantidade > 0),
    imposto NUMERIC(10,2) CHECK (imposto >= 0),
    valor_total NUMERIC(12,2) CHECK (valor_total >= 0),
    data_venda DATE,
    hora_venda TIME,
    forma_pagamento VARCHAR(50) NOT NULL,
    custo_mercadoria NUMERIC(12,2) CHECK (custo_mercadoria >= 0),
    margem_percentual NUMERIC(10,2),
    receita_bruta NUMERIC(12,2) CHECK (receita_bruta >= 0),
    avaliacao NUMERIC(4,2) CHECK (avaliacao >= 0 AND avaliacao <= 10),
    dia_semana VARCHAR(20)
);