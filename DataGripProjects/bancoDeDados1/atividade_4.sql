-- 1
create or replace function nome_completo_pedido(p_pedido_id integer)
returns table (
    v_resultado_texto varchar
)
language plpgsql
as $$
begin
    return query
    select 'pedido #' || pedidos.id || ' - ' || clientes.nome || ' - ' || pedidos.status
    from pedidos
    join clientes on pedidos.cliente_id = clientes.id
    where pedidos.id = p_pedido_id;
end;
$$;


-- 2
create or replace function cliente_tem_pedido_pendente(p_cliente_id integer)
returns boolean
language plpgsql
as $$
declare
    v_quantidade integer;
begin
    select count(1)
    into v_quantidade
    from pedidos
    where pedidos.cliente_id = p_cliente_id and pedidos.status = 'Pendente';

    if v_quantidade > 0 then
        return true;
    else
        return false;
    end if;
end;
$$;


-- 3
create or replace function total_itens_pedido(p_pedido_id integer)
returns integer
language plpgsql
as $$
declare
    v_total integer;
begin
    select count(itens_pedido.quantidade)
    into v_total
    from itens_pedido
    where itens_pedido.pedido_id = p_pedido_id;

    return v_total;
end;
$$;


-- 4
create or replace function produto_em_estoque(p_produto_id integer)
returns boolean
language plpgsql
as $$
declare
    v_estoque integer;
begin
    select produtos.quantidade_estoque
    into v_estoque
    from produtos
    where produtos.id = p_produto_id;

    if v_estoque > 0 then
        return true;
    else
        return false;
    end if;
end;
$$;


-- 5
create or replace function desconto_aplicavel(p_valor_total numeric)
returns text
language plpgsql
as $$
declare
    v_percentual numeric;
begin
    if p_valor_total <= 100 then
        v_percentual := 0;
    elsif p_valor_total <= 500 then
        v_percentual := 5;
    else
        v_percentual := 10;
    end if;

    return (v_percentual || '%');
end;
$$;


-- 6
create or replace function pagamentos_do_pedido(p_pedido_id integer)
returns table (
    v_forma_pagamento varchar,
    v_data_pagamento  timestamp
)
language plpgsql
as $$
begin
    return query
    select pagamentos.forma_pagamento, pagamentos.data_pagamento
    from pagamentos
    where pagamentos.pedido_id = p_pedido_id;
end;
$$;


-- 7
create or replace function top_clientes(p_limite integer)
returns table (
    v_nome        varchar,
    v_total_gasto numeric
)
language plpgsql
as $$
begin
    return query
    select clientes.nome, sum(pedidos.valor_total)
    from pedidos
    join clientes on clientes.id = pedidos.cliente_id
    group by clientes.nome
    order by sum(pedidos.valor_total) desc;
end;
$$;


-- 8
create or replace function produtos_sem_venda(p_categoria_id integer)
returns table (
    v_id   integer,
    v_nome varchar
)
language plpgsql
as $$
begin
    return query
    select produtos.id, produtos.nome
    from produtos
    left join itens_pedido on produtos.id = itens_pedido.produto_id
    where produtos.categoria_id = p_categoria_id
      and itens_pedido.produto_id is null;
end;
$$;


-- 9
create or replace function clientes_por_forma_pagamento(p_forma_pagamento varchar)
returns table (
    v_nome_cliente   varchar,
    v_numero_pedido  integer,
    v_data_pagamento timestamp
)
language plpgsql
as $$
begin
    return query
    select clientes.nome, pedidos.id, pagamentos.data_pagamento
    from pagamentos
    join pedidos on pedidos.id = pagamentos.pedido_id
    join clientes on clientes.id = pedidos.cliente_id
    where pagamentos.forma_pagamento = p_forma_pagamento;
end;
$$;


-- 10
create or replace function categorias_com_produto_caro(p_valor_minimo numeric)
returns table (
    v_categoria         varchar,
    v_produto_mais_caro varchar,
    v_preco_maximo      numeric
)
language plpgsql
as $$
begin
    return query
    select categorias.nome, produtos.nome, produtos.preco
    from produtos
    join categorias on categorias.id = produtos.categoria_id
    where (produtos.categoria_id, produtos.preco) in (
        select sub_produtos.categoria_id, max(sub_produtos.preco)
        from produtos as sub_produtos
        group by sub_produtos.categoria_id
    ) and produtos.preco >= p_valor_minimo;
end;
$$;


-- 11
create or replace function pedidos_com_multiplos_itens(p_quantidade_minima integer)
returns table (
    v_id           integer,
    v_nome_cliente varchar,
    v_data_pedido  date
)
language plpgsql
as $$
begin
    return query
    select pedidos.id, clientes.nome, pedidos.data_pedido
    from pedidos
    join clientes on clientes.id = pedidos.cliente_id
    join itens_pedido on pedidos.id = itens_pedido.pedido_id
    group by pedidos.id, clientes.nome, pedidos.data_pedido
    having count(itens_pedido.produto_id) > p_quantidade_minima;
end;
$$;


-- 12
create or replace function historico_precos_categoria(p_categoria_id integer)
returns table (
    v_nome_produto   varchar,
    v_preco_atual    numeric,
    v_preco_formatado text
)
language plpgsql
as $$
begin
    return query
    select produtos.nome, produtos.preco, to_char(produtos.preco, 'L999G999G999D99')
    from produtos
    where produtos.categoria_id = p_categoria_id
    order by produtos.preco desc;
end;
$$;