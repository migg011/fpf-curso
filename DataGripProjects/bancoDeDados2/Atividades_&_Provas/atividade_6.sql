-- 5. Crie uma função classificar_categoria_por_preco(p_categoria_id INTEGER) que calcule o preço
-- médio dos produtos da categoria e retorne 'Categoria Premium' (média > R$ 500), 'Categoria
-- Intermediária' (entre R$ 100 e R$ 500) ou 'Categoria Popular' (média < R$ 100).

create or replace function classificar_categoria_por_preco(p_categoria_id integer)
returns text
language plpgsql
as $$
declare
    v_media numeric;
begin
    select avg(produtos.preco)
    into v_media
    from produtos
    where produtos.categoria_id = p_categoria_id;

    if v_media > 500 then
        return 'Categoria Premium';
    elsif v_media >= 100 and v_media <= 500 then
        return 'Categoria Intermediária';
    elsif v_media < 100 then
        return 'Categoria Popular';
    else
        return 'Invalido';
    end if;
end;
$$;


-- 6. Crie uma função pode_cancelar_pedido(p_pedido_id INTEGER) que retorne uma mensagem
-- explicando se o pedido pode ser cancelado, considerando as regras: não pode cancelar se já
-- estiver 'Entregue'; não pode cancelar se já estiver 'Cancelado'; nos demais casos, pode
-- cancelar. Utilize IF com múltiplas saídas antecipadas (como no Exemplo 8).

create or replace function pode_cancelar_pedido(p_pedido_id integer)
returns text
language plpgsql
as $$
declare
    v_status text;
begin
    select pedidos.status
    into v_status
    from pedidos
    where pedidos.id = p_pedido_id;

    if v_status = 'Entregue' then
        return 'não pode cancelar';
    end if;

    if v_status = 'Cancelado' then
        return 'não pode cancelar, pois ja esta cancelado';
    end if;

    return 'pode cancelar';
end;
$$;


-- 7. Crie uma função de tabela avaliar_clientes_vip() (sem parâmetros) que percorra todos os
-- clientes com um FOR, e para cada um utilize IF/ELSIF/ELSE para classificar como 'VIP' (total
-- gasto > R$ 2.000), 'Regular' (entre R$ 500 e R$ 2.000) ou 'Ocasional' (< R$ 500), retornando
-- nome, total gasto e classificação.

create or replace function avaliar_cliente_vip()
returns table (
    nome varchar,
    total_gasto numeric,
    classificacao varchar
)
language plpgsql
as $$
declare
    v_cliente record;
begin
    for v_cliente in
        select c.nome, sum(p.valor_total) as total_gasto
        from pedidos p
        join clientes c on c.id = p.cliente_id
        group by c.id, c.nome
    loop
        nome := v_cliente.nome;
        total_gasto := v_cliente.total_gasto;

        if total_gasto > 2000 then
            classificacao := 'VIP';
        elsif total_gasto >= 500 and total_gasto <= 2000 then
            classificacao := 'Regular';
        elsif total_gasto < 500 then
            classificacao := 'Ocasional';
        else
            classificacao := 'Invalido';

        end if;

        return next;

        end loop;
end;
$$;

select * from avaliar_cliente_vip();

-- 8. Crie uma função verificar_forma_pagamento_valida(p_forma VARCHAR) que
-- retorne TRUE apenas se a forma de pagamento informada estiver entre 'Pix', 'Cartão de
-- Crédito', 'Cartão de Débito' ou 'Boleto' (utilize IF com IN), e FALSE caso contrário.

create or replace function verificar_forma_pagamento_valida(p_forma varchar)
returns boolean
language plpgsql
as $$
begin
    if p_forma in ('Pix','Cartão de Crédito','Cartão de Débito','Boleto' ) then
        return TRUE;
    else
        return FALSE;
    end if;
end;
$$;