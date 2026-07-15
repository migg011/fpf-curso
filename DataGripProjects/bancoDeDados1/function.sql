create or replace function calcular_valor_pedido(p_pedido_id integer)
returns numeric(10,2)
language plpgsql
as $$
declare
    v_total numeric(10,2);
begin
    select sum(quantidade * valor_unitario)
    into v_total
    from itens_pedido
    where pedido_id = p_pedido_id;
    return coalesce(v_total, 0);
end;
$$;

-----

create or replace function pedido_inconsistente(p_pedido_id integer)
returns boolean
language plpgsql
as $$
declare
    v_valor_registrado numeric(10,2);
    v_valor_calculado numeric(10,2);
begin
    select valor_total into v_valor_registrado
    from pedidos where id = p_pedido_id;

    v_valor_calculado := calcular_valor_pedido(p_pedido_id);

    return v_valor_registrado <> v_valor_calculado;
end;
$$;

select id, status, pedido_inconsistente(id)
from pedidos;

create or replace function dias_desde_pedido(p_data_pedido date)
returns integer
language plpgsql
as $$
begin
    return current_date - p_data_pedido;
end;
$$;

-----

create or replace function produtos_com_baixo_estoque(limite int)
returns table(id int, nome varchar, quantidade_estoque int) as $$
begin
    return query
    select p.id, p.nome, p.quantidade_estoque
    from produtos p
    where p.quantidade_estoque < limite;
end;
$$ language plpgsql;

select * from produtos_com_baixo_estoque(50);

-----

create or replace function item_do_pedido(p_pedido_id integer)
returns table (
    produto        varchar,
    quantidade     integer,
    valor_unitario numeric,
    subtotal       numeric
)
language plpgsql
as $$
begin
    return query
    select
        pr.nome,
        ip.quantidade,
        ip.valor_unitario,
        (ip.quantidade * ip.valor_unitario)::numeric as subtotal
    from itens_pedido ip
    join produtos pr on pr.id = ip.produto_id
    where ip.pedido_id = p_pedido_id;
end;
$$;

select * from item_do_pedido(10);

-----

create or replace function nome_completo_pedido(p_pedido_id integer)
returns table (
    x varchar
)
language plpgsql
as $$
begin
    return query
    select ('pedido #' || p.id || ' - ' || c.nome || ' - ' || p.status)::varchar
    from pedidos p
    join clientes c on p.cliente_id = c.id
    where p.id = p_pedido_id;
end;
$$;

select * from nome_completo_pedido(10);

-----

----- FUNCAO DE FORMATAÇÃO PARA REAIS
create function formatar_reais(p_valor numeric)
returns text
language plpgsql
as $$
    begin
        return to_char(p_valor, 'L999G999G999D99');
    end;
$$;

-----

create or replace function classificar_pedido(p_valor_pedido numeric)
returns text
language plpgsql
as $$
begin
    if p_valor_pedido > 500 then
        return 'Pedido caro';
    else
        return 'Pedido barato';
    end if;
end;
$$;

select
    id,
    valor_total,
    classificar_pedido(valor_total) as classificacao
from pedidos;

-----

create or replace function calcular_desconto(p_valor_total numeric)
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
        elsif p_valor_total <= 100 then
        v_percentual := 10;
        else
        v_percentual := 15;
    end if;

    return (v_percentual || '%');
end;
$$;

select
    id,
    formatar_reais(valor_total) as valor_total,
    calcular_desconto(valor_total) as percentual_desconto
from pedidos;

-----

create or replace function elegivel_frete_gratis(p_pedido_id integer)
returns boolean
language plpgsql
as $$
declare
    v_valor_total numeric;
    v_status varchar;
begin
    select valor_total, pedidos.status
    into v_valor_total, v_status
    from pedidos
    where id = p_pedido_id;

    if v_valor_total >= 200 and v_status <> 'Cancelado' then
        return true;
        else
            return false;
    end if;
end;
$$;

select elegivel_frete_gratis(9);

-----

create or replace function status_do_pedido(p_pedido_id integer)
returns text
language plpgsql
as $$
declare
    v_status varchar;
begin
    select status into v_status
    from pedidos
    where id = p_pedido_id;

    if v_status is null then
        return 'Pedido não entrados';
    elsif v_status = 'Entregue' then
        return 'Pedudo já finalizado';
    else
        return 'Pedido em andamento';
    end if;
end;
$$;

-----

--LOOPING
create or replace function avaliar_itens_pedido(p_pedido_id integer)
returns table (produto varchar, quantidade integer, situacao text)
language plpgsql
as $$
declare
    r_item record;
begin
    for r_item in
        select pr.nome, ip.quantidade, pr.quantidade_estoque
        from itens_pedido ip
        join produtos pr on pr.id = ip.produto_id
        where ip.pedido_id = p_pedido_id
    loop
        produto := r_item.nome;
        quantidade := r_item.quantidade;

        if r_item.quantidade_estoque = 0 then
            situacao := 'Sem estoque para reposição';
            elsif r_item.quantidade_estoque < r_item.quantidade then
            situacao := 'Estoque abaixo do vendido';
            else
            situacao := 'Estoque OK';
        end if;

        return next;

        end loop;
end;
$$;

select * from avaliar_itens_pedido(10);

-----

create or replace function pode_marcar_entregue(p_pedido_id integer)
returns text
language plpgsql
as $$
declare
    v_status          varchar;
    v_valor_total     numeric;
    v_valor_calculado numeric;
    v_tem_pagamento   boolean;
begin
    select status, valor_total
    into v_status, v_valor_total
    from pedidos
    where id = p_pedido_id;

    if v_status is null then
        return 'erro: pedido não encontrado';
    end if;

    if v_status = 'entregue' then
        return 'erro: pedido já está marcado como entregue';
    end if;

    if v_status = 'cancelado' then
        return 'erro: pedido cancelado não pode ser entregue';
    end if;

    select sum(quantidade * valor_unitario)
    into v_valor_calculado
    from itens_pedido
    where pedido_id = p_pedido_id;

    if v_valor_total <> v_valor_calculado then
        return 'erro: valor do pedido inconsistente, corrija antes de liberar';
    end if;

    select exists (
        select 1 from pagamentos where pedido_id = p_pedido_id
    ) into v_tem_pagamento;

    if not v_tem_pagamento then
        return 'erro: pedido sem pagamento registrado';
    end if;

    return 'ok: pedido pode ser marcado como entregue';
end;
$$;

select pode_marcar_entregue(10);






