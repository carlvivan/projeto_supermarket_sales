-- =========================================================
-- PROJETO SUPERMARKET SALES
-- CONSULTAS SQL
-- Banco: PostgreSQL
-- Tabela: raw_vendas
-- =========================================================


-- =========================================================
-- 1. PRIMEIRAS LINHAS DA BASE
-- =========================================================

SELECT *
FROM raw_vendas
LIMIT 10;


-- =========================================================
-- 2. QUANTIDADE TOTAL DE REGISTROS
-- =========================================================

SELECT
    COUNT(*) AS quantidade_registros
FROM raw_vendas;


-- =========================================================
-- 3. QUANTIDADE DE VENDAS POR FILIAL
-- =========================================================

SELECT
    "Branch" AS filial,
    COUNT(*) AS quantidade_vendas
FROM raw_vendas
GROUP BY "Branch"
ORDER BY quantidade_vendas DESC;


-- =========================================================
-- 4. FATURAMENTO POR FILIAL
-- =========================================================

SELECT
    "Branch" AS filial,
    ROUND(SUM(CAST("Sales" AS NUMERIC)), 2) AS faturamento
FROM raw_vendas
GROUP BY "Branch"
ORDER BY faturamento DESC;


-- =========================================================
-- 5. FATURAMENTO POR LINHA DE PRODUTO
-- =========================================================

SELECT
    "Product line" AS linha_produto,
    ROUND(SUM(CAST("Sales" AS NUMERIC)), 2) AS faturamento
FROM raw_vendas
GROUP BY "Product line"
ORDER BY faturamento DESC;


-- =========================================================
-- 6. QUANTIDADE DE VENDAS POR FORMA DE PAGAMENTO
-- =========================================================

SELECT
    "Payment" AS forma_pagamento,
    COUNT(*) AS quantidade_vendas
FROM raw_vendas
GROUP BY "Payment"
ORDER BY quantidade_vendas DESC;


-- =========================================================
-- 7. VALOR MÉDIO DAS VENDAS
-- =========================================================

SELECT
    ROUND(AVG(CAST("Sales" AS NUMERIC)), 2) AS ticket_medio
FROM raw_vendas;


-- =========================================================
-- 8. MAIOR VENDA
-- =========================================================

SELECT
    ROUND(MAX(CAST("Sales" AS NUMERIC)), 2) AS maior_venda
FROM raw_vendas;


-- =========================================================
-- 9. AVALIAÇÃO MÉDIA POR LINHA DE PRODUTO
-- =========================================================

SELECT
    "Product line" AS linha_produto,
    ROUND(AVG(CAST("Rating" AS NUMERIC)), 2) AS avaliacao_media
FROM raw_vendas
GROUP BY "Product line"
ORDER BY avaliacao_media DESC;


-- =========================================================
-- 10. QUANTIDADE DE VENDAS POR DIA DA SEMANA
-- =========================================================

SELECT
    CASE EXTRACT(
        ISODOW
        FROM TO_DATE("Date", 'MM/DD/YYYY')
    )
        WHEN 1 THEN 'Segunda-feira'
        WHEN 2 THEN 'Terça-feira'
        WHEN 3 THEN 'Quarta-feira'
        WHEN 4 THEN 'Quinta-feira'
        WHEN 5 THEN 'Sexta-feira'
        WHEN 6 THEN 'Sábado'
        WHEN 7 THEN 'Domingo'
    END AS dia_semana,

    COUNT(*) AS quantidade_vendas

FROM raw_vendas

GROUP BY EXTRACT(
    ISODOW
    FROM TO_DATE("Date", 'MM/DD/YYYY')
)

ORDER BY EXTRACT(
    ISODOW
    FROM TO_DATE("Date", 'MM/DD/YYYY')
);


-- =========================================================
-- 11. TICKET MÉDIO
-- =========================================================

SELECT
    ROUND(AVG(CAST("Sales" AS NUMERIC)), 2) AS ticket_medio
FROM raw_vendas;


-- =========================================================
-- 12. AVALIAÇÃO MÉDIA GERAL
-- =========================================================

SELECT
    ROUND(AVG(CAST("Rating" AS NUMERIC)), 2) AS avaliacao_media
FROM raw_vendas;


-- =========================================================
-- 13. QUANTIDADE DE PRODUTOS VENDIDOS POR LINHA
-- =========================================================

SELECT
    "Product line" AS linha_produto,
    SUM(CAST("Quantity" AS INTEGER)) AS quantidade_vendida
FROM raw_vendas
GROUP BY "Product line"
ORDER BY quantidade_vendida DESC;


-- =========================================================
-- 14. FATURAMENTO POR FORMA DE PAGAMENTO
-- =========================================================

SELECT
    "Payment" AS forma_pagamento,
    ROUND(SUM(CAST("Sales" AS NUMERIC)), 2) AS faturamento
FROM raw_vendas
GROUP BY "Payment"
ORDER BY faturamento DESC;


-- =========================================================
-- 15. CONFERÊNCIA DO FATURAMENTO TOTAL
-- =========================================================

SELECT
    COUNT(*) AS quantidade_vendas,
    ROUND(SUM(CAST("Sales" AS NUMERIC)), 2) AS faturamento_total,
    ROUND(AVG(CAST("Sales" AS NUMERIC)), 2) AS ticket_medio
FROM raw_vendas;


-- =========================================================
-- 16. FATURAMENTO POR CIDADE
-- =========================================================

SELECT
    "City" AS cidade,
    ROUND(SUM(CAST("Sales" AS NUMERIC)), 2) AS faturamento
FROM raw_vendas
GROUP BY "City"
ORDER BY faturamento DESC;


-- =========================================================
-- 17. FATURAMENTO POR GÊNERO
-- =========================================================

SELECT
    "Gender" AS genero,
    ROUND(SUM(CAST("Sales" AS NUMERIC)), 2) AS faturamento
FROM raw_vendas
GROUP BY "Gender"
ORDER BY faturamento DESC;


-- =========================================================
-- 18. QUANTIDADE DE VENDAS POR TIPO DE CLIENTE
-- =========================================================

SELECT
    "Customer type" AS tipo_cliente,
    COUNT(*) AS quantidade_vendas
FROM raw_vendas
GROUP BY "Customer type"
ORDER BY quantidade_vendas DESC;


-- =========================================================
-- 19. FATURAMENTO POR TIPO DE CLIENTE
-- =========================================================

SELECT
    "Customer type" AS tipo_cliente,
    ROUND(SUM(CAST("Sales" AS NUMERIC)), 2) AS faturamento
FROM raw_vendas
GROUP BY "Customer type"
ORDER BY faturamento DESC;


-- ============================================================
-- ANÁLISES DA TABELA TRATADA
-- ============================================================


-- ============================================================
-- 20. QUANTIDADE TOTAL DE REGISTROS - TABELA TRATADA
-- ============================================================

SELECT
    COUNT(*) AS quantidade_registros
FROM vendas;


-- ============================================================
-- 21. QUANTIDADE DE VENDAS POR FILIAL
-- ============================================================

SELECT
    filial,
    COUNT(*) AS quantidade_vendas
FROM vendas
GROUP BY filial
ORDER BY quantidade_vendas DESC;


-- ============================================================
-- 22. FATURAMENTO POR FILIAL
-- ============================================================

SELECT
    filial,
    ROUND(SUM(valor_total), 2) AS faturamento
FROM vendas
GROUP BY filial
ORDER BY faturamento DESC;


-- ============================================================
-- 23. FATURAMENTO POR LINHA DE PRODUTO
-- ============================================================

SELECT
    linha_produto,
    ROUND(SUM(valor_total), 2) AS faturamento
FROM vendas
GROUP BY linha_produto
ORDER BY faturamento DESC;


-- ============================================================
-- 24. QUANTIDADE DE VENDAS POR FORMA DE PAGAMENTO
-- ============================================================

SELECT
    forma_pagamento,
    COUNT(*) AS quantidade_vendas
FROM vendas
GROUP BY forma_pagamento
ORDER BY quantidade_vendas DESC;


-- ============================================================
-- 25. TICKET MÉDIO
-- ============================================================

SELECT
    ROUND(AVG(valor_total), 2) AS ticket_medio
FROM vendas;


-- ============================================================
-- 26. MAIOR VENDA
-- ============================================================

SELECT
    ROUND(MAX(valor_total), 2) AS maior_venda
FROM vendas;


-- ============================================================
-- 27. AVALIAÇÃO MÉDIA POR LINHA DE PRODUTO
-- ============================================================

SELECT
    linha_produto,
    ROUND(AVG(avaliacao), 2) AS avaliacao_media
FROM vendas
GROUP BY linha_produto
ORDER BY avaliacao_media DESC;


-- ============================================================
-- 28. QUANTIDADE DE VENDAS POR DIA DA SEMANA
-- ============================================================

SELECT
    dia_semana,
    COUNT(*) AS quantidade_vendas
FROM vendas
GROUP BY dia_semana
ORDER BY quantidade_vendas DESC;


-- ============================================================
-- 29. FATURAMENTO POR CIDADE
-- ============================================================

SELECT
    cidade,
    ROUND(SUM(valor_total), 2) AS faturamento
FROM vendas
GROUP BY cidade
ORDER BY faturamento DESC;


-- ============================================================
-- 30. FATURAMENTO POR GÊNERO
-- ============================================================

SELECT
    genero,
    ROUND(SUM(valor_total), 2) AS faturamento
FROM vendas
GROUP BY genero
ORDER BY faturamento DESC;


-- ============================================================
-- 31. QUANTIDADE DE VENDAS POR TIPO DE CLIENTE
-- ============================================================

SELECT
    tipo_cliente,
    COUNT(*) AS quantidade_vendas
FROM vendas
GROUP BY tipo_cliente
ORDER BY quantidade_vendas DESC;


-- ============================================================
-- 32. FATURAMENTO POR TIPO DE CLIENTE
-- ============================================================

SELECT
    tipo_cliente,
    ROUND(SUM(valor_total), 2) AS faturamento
FROM vendas
GROUP BY tipo_cliente
ORDER BY faturamento DESC;