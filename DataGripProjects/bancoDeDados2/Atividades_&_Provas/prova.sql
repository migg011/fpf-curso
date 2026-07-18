-- aluno: Antônio Miguel

-- Modelo de dados utilizado:
--  clientes (id, nome, email, senha, endereço, telefone)
--  categorias (id, nome, descrição)
--  produtos (id, categoria_id, nome, descrição, preco, quantidade_estoque, imagem, marca)
--  pedidos (id, cliente_id, data_pedido, status, valor_total)
--  itens_pedido (id, pedido_id, produto_id, quantidade, valor_unitario)
--  pagamentos (id, pedido_id, forma_pagamento, data_pagamento)

-- 1. Crie uma view chamada vw_clientes_ativos que liste o nome e o email de todos os clientes
-- que possuem pelo menos um pedido com status diferente de 'Cancelado'. (0 a 1,0)

create or replace view vw_clientes_ativos as
    select
        c.nome,
        c.email
from clientes c
join pedidos on c.id = pedidos.cliente_id
where pedidos.status <> 'Cancelado';

select * from vw_clientes_ativos;

-- 2. Crie uma função escalar valor_medio_produto(p_categoria_id INTEGER) que retorne o preço
-- médio dos produtos de uma categoria,formatado no padrão brasileiro (R$ 0.000,00). (0 a 1,0)

create or replace function valor_medio_produto(p_categoria_id integer)
returns text
language plpgsql
as $$
declare
    v_media numeric;
begin
    select avg(preco)
    into v_media
    from produtos
    where categoria_id = p_categoria_id;

    return to_char(v_media, 'L999G999G999D99');
end;
$$;

select * from valor_medio_produto(10);

-- 3. Crie uma função de tabela pedidos_do_dia(p_data DATE) que retorne o nome do cliente, o
-- status e o valor total de todos os pedidos realizados em uma data específica. (0 a 1,0)

create or replace function pedidos_do_dia(p_data date)
returns table(
    nome_cleinte varchar,
    status varchar,
    valor_total numeric
)
language plpgsql
as $$
begin
    return query
    select
        clientes.nome,
        pedidos.status,
        pedidos.valor_total
    from pedidos
    join clientes on clientes.id = pedidos.cliente_id
    where pedidos.data_pedido = p_data;
end;
$$;

-- 4. Crie uma função escalar classificar_cliente(p_cliente_id INTEGER) que
-- utilize IF/ELSIF/ELSE para retornar 'Cliente Ouro' (total gasto > R$3.000),'Cliente  Prata' (entre
-- R$1.000 e R$3.000) ou 'Cliente Bronze' (<R$1.000). (0 a 1,0)

create or replace function classificar_cliente(p_cliente_id integer)
returns text
language plpgsql
as $$
declare
    v_total numeric;
begin
    select coalesce(sum(valor_total), 0)
    into v_total
    from pedidos
    where cliente_id = p_cliente_id;

    if v_total > 3000 then
        return 'Cliente Ouro';
    elseif v_total >= 1000 then
        return 'Cliente Prata';
    else
        return 'Cliente Bronze';
    end if;
end;
$$;

-- 5. Crie uma função escalar produto_disponivel_para_venda(p_produto_id INTEGER,
-- p_quantidade_desejada INTEGER) que retorne TRUE se o quantidade_estoque do produto for maior
-- ou igual à quantidade desejada, ou FALSE caso contrário. (0 a 1,0)

create or replace function produto_disponivel_para_venda(
    p_produto_id integer,
    p_quantidade_desejada integer
)
returns boolean
language plpgsql
as $$
declare
    v_estoque integer;
begin
    select quantidade_estoque
    into v_estoque
    from produtos
    where id = p_produto_id;

    return v_estoque >= p_quantidade_desejada;
end;
$$;


-- Aluno: João Marçião


-- 6. Crie uma procedure atualizar_email_cliente(p_cliente_id IN INTEGER, p_novo_email IN
-- VARCHAR) que atualize o email de um cliente. (0 a 1,0)

CREATE OR REPLACE PROCEDURE atualizar_email_cliente(
p_cliente_id INTEGER,
    p_novo_email VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN

    update clientes
    set email = p_novo_email
    where clientes_id = p_cliente_id;

END;
$$;


-- 7. Crie uma procedure calcular_frete(p_valor_pedido IN NUMERIC, p_valor_frete OUT NUMERIC)
-- que devolva o valor do frete conforme a regra: pedidos acima de R$300,00 têm  frete grátis (0); pedidos entre R$100,01 e R$ 300,00 pagam
-- R$35,00. Utilize IF/ELSIF/ELSE.


CREATE OR REPLACE PROCEDURE calcular_frete(
    p_valor_pedido NUMERIC,
    OUT p_valor_frete NUMERIC
)
language plgsql
AS $$
BEGIN
    IF p_valor_pedido > 300 THEN
        p_valor_frete := 0;

    ELSIF p_valor_pedido > 100 THEN
        p_valor_frete := 20;

    ELSE
        p_valor_frete := 35;

    END IF;

END;
$$;

-- 8. Crie uma procedure ajustar_quantidade_estoque(p_produto_id IN INTEGER, p_ajuste IN INTEGER,
-- p_ajuste IN INTENGER, p_estoque_final INOUT INTEGER) que some (ou subtraia, se p_ajuste for negativo) o valor
-- de p_ajuste ao coloque do produto, devolvendo o valor final através do parÂmetro INOUT

create or replace procedure ajustar_quantidade_ESTOQUE(
    p_produto_id INTEGER,
    p_ajuste integer,
    INOUT p_estoque_final integer
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT estoque
    INTO p_estoque_final
    FROM produtos
    WHERE produto_id = p_produto_id;

    p_estoque_final := p_estoque_final + p_ajuste;

    UPDATE produtos
    SET estoque = p_estoque_final
    WHERE produto_id = p_produto_id;

END;
$$;


-- 9 Crie uma função de tabela historico_pagamentos_cliente(p_cliente_id INTEGER) que retorne, para um cliente, o número do pedido, a forma de pagamento
-- e a data de pagamento de todos os seus pedidos  pagos, ordenada da data mais recente para a mais antiga.

CREATE OR REPLACE FUNCTION historico_pagamentos_cliente(
    p_cliente_id INTEGER
)

RETURNS TABLE (
    pedido_id INTEGER,
    forma_pagamento VARCHAR,
    data_pagamento DATE
)
LANGUAGE plpgsql
AS $$
BEGIN

    RETURN QUERY

    SELECT
        p.pedido_id,
        pg.forna_pagamento,
        pg.data_pagamento
    FROM pedidos p
    JOIN pagamentos pg
        ON p.pedido_id = pg.pedido_id
    WHERE p.cliente_id = p_cliente_id
        AND pg.data_pagamento IS NOT NULL
    ORDER BY pg.data_pagamento DESC;

    END
    $$;

-- 10 Crie uma procedure processar_devolucao(p_pedido_id IN INTEGER, p_mensagem OUT TEXT) que só permita marcar o pedido como 'Devolvido' se o status atual
-- for 'Entregie;' caso contrário, devolva uma mensagem de erro explicando o motivo (use IF com saída antecipada)


CREATE OR REPLACE PROCEDURE processar_devolucao(
    p_pedido_id INTEGER,
    OUT p_mensagem TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_status VARCHAR;
BEGIN

    select status
    into v_status
    from pedidos
    where pedido_id = p_pedido_id;

    IF v_status IS NULL THEN
        p_mensagem := 'Pedido não encontrado.';
        RETURN;
    END IF;

    IF v_status <> 'Entregue' THEN
        p_mensagem := 'O pedido não pode ser devolvido.';
        RETURN;
    END IF;

    UPDATE pedidos
    SET status = 'Devolvido'
    WHERE pedido_id = p_pedido_id;

    p_mensagem := 'Pedido devolvido com sucesso.';

END;
$$;





