-- 1. Crie uma função situacao_estoque(p_produto_id INTEGER) que retorne 'Esgotado’ se
-- quantidade_estoque = 0, 'Estoque baixo' se for menor ou igual a 5, ou 'Estoque OK' caso contrário.
-- Utilize IF/ELSIF/ELSE.

create or replace function situacao_estoque(p_produto_id integer)
returns text
language plpgsql
as $$
declare v_quantidade_estoque integer;
begin

    select produtos.quantidade_estoque
    into v_quantidade_estoque
    from produtos
    where produtos.id = p_produto_id;

    if v_quantidade_estoque = 0 then
        return 'Esgotado';
    elsif v_quantidade_estoque <= 5 then
        return 'Estoque baixo';
    else
        return 'Estoque OK';
    end if;
end;
$$;

-- 2. Crie uma função pedido_urgente(p_pedido_id INTEGER) que retorne TRUE se o pedido tiver
-- mais de 15 dias desde data_pedido e o status ainda for 'Pendente', ou FALSE caso contrário.'

create or replace function pedido_urgente(p_pedido_id integer)
returns boolean
language plpgsql
as $$
declare
    v_data_pedido date;
    v_status_pedido text;
begin
    select pedidos.data_pedido, pedidos.status
    into v_data_pedido, v_status_pedido
    from pedidos
    where pedidos.id = p_pedido_id;

    if (current_date - v_data_pedido) > 15 and v_status_pedido = 'Pendente' then
        return True;
    else
        return False;
    end if;
end;
$$;


-- 3. Crie uma função faixa_etaria_cliente(p_idade INTEGER) que retorne 'Menor de
-- idade', 'Adulto' ou 'Idoso' conforme a idade informada (considere idoso a partir de 60 anos).

create or replace function faixa_estaria_cliente(p_idade integer)
returns text
language plpgsql
as $$
begin
    if p_idade < 18 then
        return 'Menor de idade';
    elsif p_idade >= 18 and p_idade < 60 then
        return 'Adulto';
    elsif P_idade >= 60 then
        return 'Idoso';
    else
        return 'Invalido';
    end if;
end;
$$;


-- 4. Crie uma função validar_email_cliente(p_cliente_id INTEGER) que retorne 'Email válido' se o
-- campo email contiver o caractere '@', ou 'Email inválido' caso
-- contrário. Utilize POSITION ou LIKE dentro da condição do IF.

create or replace function validar_email_cliente(p_cliente_id integer)
returns text
language plpgsql
as $$
    declare
        v_email text;
begin
    select clientes.email
    into v_email
    from clientes
    where clientes.id = p_cliente_id;

    if v_email like '%@%' then
        return 'Email Valido';
    else
        return 'Email Invalido';
    end if;
end;
$$