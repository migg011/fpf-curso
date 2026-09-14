
--Procedure

create or replace procedure exemplo_parametros(
    p_entrada in integer,
    p_saida out integer,
    p_ida_volta inout integer
)
language plpgsql
as $$
begin
    p_saida := p_entrada * 2;
    p_ida_volta := p_ida_volta + p_entrada;
end;
$$;

call exemplo_parametros(2, 0, 3);

-----

create or replace procedure cancelar_pedidos_antigos()
language plpgsql
as $$
begin
    update pedidos
    set status = 'Cancelado'
    where status = 'Pendente'
    and current_date - data_pedido > 60;
end;
$$;

call cancelar_pedidos_antigos();

-----

create or replace procedure reajustar_preco_categoria(
    p_categoria in integer,
    p_percentual in numeric
)
language plpgsql
as $$
begin
    update produtos
    set preco = preco + (preco * p_percentual / 100)
    where categoria_id = p_percentual;
end;
$$;

call reajustar_preco_categoria(2,10);

-----

create or replace procedure registrar_pagamento(
    p_pedido_id in integer,
    p_forma_pagamento in varchar,
    p_pagamento_id out integer
)
language plpgsql
as $$
begin
    insert into pagamentos(pedido_id, forma_pagamento,data_pagamento)
    values (p_pedido_id, p_forma_pagamento, current_date)
    returning id into p_pagamento_id;
end;
$$;

call registrar_pagamento(10, 'Pix', null);

-----

create or replace procedure dar_baixa_estoque(
    p_produto_id in integer,
    p_quantidade in integer,
    p_estoque_final inout integer
)
language plpgsql
as $$
begin
    select quantidade_estoque into p_estoque_final
    from produtos
    where id = p_produto_id;

    if p_estoque_final < p_quantidade then
        raise exception 'Estoque isuficiente para o produto %', p_produto_id;
    end if;

    update produtos
    set quantidade_estoque = quantidade_estoque - p_quantidade
    where id = p_produto_id;

    p_estoque_final := p_estoque_final - p_quantidade;

end;
$$;

call dar_baixa_estoque(5,3,0);

-----

create or replace procedure finalizar_pedido(
    p_pedido_id in integer,
    p_mensagem out text
)
language plpgsql
as $$
declare
    v_tem_pagamento boolean;
    v_status varchar;
begin
    select status into v_status
    from pedidos
    where id = p_pedido_id;

    if v_status is null then
        p_mensagem := 'Erro: pedido não encontrado';
        return;
    end if;

    select exists (
        select 1 from pagamentos where pedido_id = p_pedido_id
    ) into v_tem_pagamento;

    if not v_tem_pagamento then
        p_mensagem := 'Erro: pedido sem pagamento registrado';
        return;
    end if;

    update pedidos
    set status = 'Entregue'
    where id = p_pedido_id;

    p_mensagem := 'Pedido finalizado com sucesso';

end;
$$;

call finalizar_pedido(10, null);

-----

create or replace procedure processar_baixa_estoque_pedido(p_pedido_id in integer)
language plpgsql
as $$
declare
    r_item record;
begin
    for r_item in
        select produto_id, quantidade
        from itens_pedido
        where pedido_id = p_pedido_id
    loop
        update produtos
        set quantidade_estoque = quantidade_estoque - r_item.quantidade
        where id = r_item.produto_id;

        --confirma a baixa de cada item individualmente
        commit;
        end loop;
end;
$$;

call processar_baixa_estoque_pedido(10)

-----

