-- questao 1
SELECT pedidos.id, pedidos.valor_total, SUM(itens_pedido.quantidade * itens_pedido.valor_unitario) AS soma_calculada
FROM pedidos
INNER JOIN itens_pedido ON pedidos.id = itens_pedido.pedido_id
GROUP BY pedidos.id, pedidos.valor_total HAVING pedidos.valor_total <> SUM(itens_pedido.quantidade * itens_pedido.valor_unitario);

UPDATE pedidos SET valor_total = subquery.soma_real FROM (
    SELECT pedido_id, SUM(quantidade * valor_unitario) AS soma_real
    FROM itens_pedido
    GROUP BY pedido_id
)
AS subquery WHERE pedidos.id = subquery.pedido_id AND pedidos.valor_total <> subquery.soma_real;


-- questao 2
SELECT clientes.nome, pedidos.data_pedido, pedidos.status, AVG(pedidos.valor_total) AS media_valor_total
FROM pedidos
INNER JOIN clientes ON clientes.id = pedidos.cliente_id
WHERE EXTRACT(MONTH FROM pedidos.data_pedido) = 6 AND EXTRACT(YEAR FROM pedidos.data_pedido) = 2024
GROUP BY clientes.nome, pedidos.data_pedido, pedidos.status;


-- questao 3
SELECT
    UPPER(clientes.nome) AS nome_maiusculo,
    UPPER(SPLIT_PART(clientes.email, '@', 2)) AS dominio_maiusculo,
    LENGTH(clientes.email) AS tamanho_total_email
FROM clientes;


-- questao 4
SELECT
    TO_CHAR(pedidos.data_pedido, 'DD/MM/YYYY') AS data_formatada,
    TO_CHAR(pedidos.data_pedido, 'TMMonth') AS nome_mes_extenso,
    DATE_PART('month', pedidos.data_pedido) AS numero_do_mes
FROM pedidos;


-- questao 5
SELECT pedidos.id, pedidos.data_pedido,
    CURRENT_DATE - pedidos.data_pedido AS dias_passados,
    AGE(NOW(), pedidos.data_pedido) AS diferenca_completa
FROM pedidos;


-- questao 6
SELECT produtos.nome,
    TO_CHAR(produtos.preco, 'L9G999G990D99') AS preco_pt_br,
    ROUND(produtos.preco, 0) AS preco_arredondado,
    TRUNC(produtos.preco, 0) AS preco_truncado
FROM produtos;


-- questao 7
SELECT produtos.categorias,
    MAX(produtos.preco) AS maior_preco,
    MIN(produtos.preco) AS menor_preco,
    TO_CHAR(AVG(produtos.preco), 'L9G999G990D99') AS media_formatada
FROM produtos GROUP BY produtos.categorias;


-- questao 8
UPDATE pedidos SET status = UPPER(SUBSTRING(pedidos.status FROM 1 FOR 1)) || LOWER(SUBSTRING(pedidos.status FROM 2));


-- questao 9
SELECT VERSION() AS versao_sistema,
    pg_size_pretty(pg_database_size(current_database())) AS tamanho_banco_atual,
    pg_size_pretty(pg_total_relation_size('clientes')) AS tamanho_tabela_cliente,
    pg_size_pretty(pg_total_relation_size('produtos')) AS tamanho_tabela_produto,
    pg_size_pretty(pg_total_relation_size('pedidos')) AS tamanho_tabela_pedido,
    pg_size_pretty(pg_total_relation_size('itens_pedido')) AS tamanho_tabela_itens,
    pg_size_pretty(pg_total_relation_size('categorias')) AS tamanho_tabela_categorias,
    pg_size_pretty(pg_total_relation_size('pagamentos')) AS tamanho_tabela_pagamentos;