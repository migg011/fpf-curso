--sintaxe
-- create view nome_da_view as
-- select colunas
-- from tabela
-- --where condição;

--exemplo
create view view_total_pedido_por_cliente as
select c.nome, sum(p.valor_total) as valor
from pedidos p
inner join clientes c on c.id = p.cliente_id
group by c.nome;

--criando view
create view view_total_pedido_por_cliente as
select c.nome, sum(p.valor_total) as total_pedidos
from clientes c
join pedidos p on c.id = p.cliente_id
group by c.nome;


-- executando uma view
select *
from view_total_pedido_por_cliente;


-- executando uma view com clausula where

-- select *
-- from view_total_pedido_por_cliente
-- where total_pedidos > 2000;


---- recriando view
create or replace view view_clientes_vip as
select c.nome, sum(p.valor_total) as total_pedidos
from clientes c
join pedidos p on c.id = p.cliente_id
group by c.nome
having sum(p.valor_total) > 3000;

-----

CREATE VIEW view_total_pedido_por_cliente AS
SELECT
    c.nome, SUM(p.valor_total) AS valor
FROM pedidos p
INNER JOIN clientes c ON c.id = p.cliente_id
GROUP BY c.nome;

select * from view_total_pedido_por_cliente;

-----

create or replace view view_clientes_vip as
    select c.nome, SUM(p.valor_total) as total_pedidos
from clientes c
join pedidos p on c.id = cliente_id
group by c.nome
having sum(p.valor_total) > 3000;

DROP VIEW IF EXISTS view_vendas_totais_cliente;

-----

--atividade 1

-- 1 – Crie uma view que exibe informações dos pedidos feitos por clientes, incluindo o valor total, o status e a
-- data do pedido.
CREATE or replace view view_pedidos AS
    select
        c.nome as nome_cliente, p.id as id_produto_solicitado ,p.data_pedido,p.status, p.valor_total
    from pedidos p
    inner join clientes c on c.id = p.cliente_id;

select * from view_pedidos;



-- 2 – Crie uma view para listar os itens de cada pedido com o valor de cada item, quantidade comprada e o
-- total por item.
CREATE or replace view view_listas_pedido AS
    select ip.pedido_id as id_pedido,p.nome as nome_produto, ip.valor_unitario, ip.quantidade as quantidade_comprada, (ip.valor_unitario * ip.quantidade) as total_item
    from itens_pedido ip
    inner join produtos p on p.id = ip.produto_id;

select * from view_listas_pedido;



-- 3 – Crie uma view que exibe as vendas totais por cliente, somando o valor total dos pedidos de cada um e o
-- número de pedidos comprados
CREATE or replace view view_vendas_totais_cliente AS
    select
        c.id as cliente_id, c.nome as cliente_nome, count(p.id) as total_pedidos_feitos, sum(p.valor_total) as valor_total_gasto
    from clientes c
    inner join pedidos p on c.id = p.cliente_id
    group by c.id, c.nome;

select * from view_vendas_totais_cliente;



-----

--atividade 2

-- 1. Crie uma view chamada vw_resumo_pedidos que exiba, para cada pedido: o nome do cliente, a data do pedido
-- formatada como DD/MM/YYYY, o status (com a primeira letra em maiúscula) e o valor total formatado no padrão brasileiro
-- (R$ 0.000,00).
CREATE or replace view vw_resumo_pedidos AS
    select
        c.nome as nome_cliente,
        to_char(p.data_pedido, 'DD/MM/YYYY') as data_pedido,
        initcap(p.status) as status,
        to_char(p.valor_total, '"R$ "999G999G990D99') as valor_total
    from pedidos p
    inner join clientes c on c.id = p.cliente_id;

select * from vw_resumo_pedidos;



-- 2. Crie uma view chamada vw_faturamento_por_cliente que mostre o nome de cada cliente, a quantidade total de
-- pedidos realizados e a soma de todos os valor_total desses pedidos, ordenada do cliente que mais gastou para o que
-- menos gastou.
CREATE or replace view vw_faturamento_por_cliente AS
    select
        c.nome as nome_cliente,
        count(p.id) as quantidade_pedidos,
        sum(p.valor_total) as total_faturado
    from clientes c
    inner join pedidos p on c.id = p.cliente_id
    group by c.id, c.nome
    order by total_faturado desc;

select * from vw_faturamento_por_cliente;



-- 3. Crie uma view chamada vw_produtos_por_categoria que liste, para cada categoria, o nome da categoria, a
-- quantidade de produtos cadastrados nela e o preço médio dos produtos, formatado em reais. Utilize LEFT JOIN para que
-- categorias sem produtos também apareçam (com quantidade zero).
CREATE or replace view vw_produtos_por_categoria AS
    select
        cat.nome as nome_categoria,
        count(prod.id) as quantidade_produtos,
        to_char(avg(prod.preco), '"R$ "999G999G990D99') as preco_medio
    from categorias cat
    left join produtos prod on cat.id = prod.categoria_id
    group by cat.nome;

select * from vw_produtos_por_categoria;



-- 4. Crie uma view chamada vw_pedidos_inconsistentes que compare o valor_total do pedido com a soma dos itens
-- do pedido, exibindo pedido_id, valor_registrado, valor_calculado e diferenca, mostrando apenas os pedidos
-- com divergência. Depois, escreva uma consulta simples que utilize essa view para contar quantos pedidos estão
-- inconsistentes.
CREATE or replace view vw_pedidos_inconsistentes AS
    select
        p.id as pedido_id,
        p.valor_total as valor_registrado,
        sum(ip.quantidade * ip.valor_unitario) as valor_calculado,
        (p.valor_total - sum(ip.quantidade * ip.valor_unitario)) as diferenca
    from pedidos p
    inner join itens_pedido ip on p.id = ip.pedido_id
    group by p.id, p.valor_total
    having p.valor_total <> sum(ip.quantidade * ip.valor_unitario);

select * from vw_pedidos_inconsistentes;

select count(*) as total_pedidos_inconsistentes from vw_pedidos_inconsistentes;



-- 5. Crie uma view chamada vw_tempo_desde_pedido que mostre, para cada pedido, o nome do cliente, a data do pedido,
-- quantos dias se passaram até hoje (CURRENT_DATE) e essa mesma diferença formatada em anos/meses/dias usando
-- AGE. Em seguida, escreva uma consulta que utilize essa view para listar apenas os pedidos com mais de 30 dias.
CREATE or replace view vw_tempo_desde_pedido AS
    select
        c.nome as nome_cliente,
        p.data_pedido,
        (current_date - p.data_pedido) as dias_passados,
        age(current_date, p.data_pedido) as tempo_formatado
    from pedidos p
    inner join clientes c on c.id = p.cliente_id;

select * from vw_tempo_desde_pedido;

select * from vw_tempo_desde_pedido where dias_passados > 30;



