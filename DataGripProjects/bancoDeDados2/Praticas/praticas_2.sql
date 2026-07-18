-- Crie uma função de tabela chamada calcular_bonus_funcionarios() (sem parâmetros)
-- que percorra todos os funcionários com um FOR. Para cada funcionário, calcule o
-- total de vendas realizado por ele e defina o bônus com base nas seguintes regras:
--
-- Total de vendas maior que R$ 10.000: bônus de 15% do salário base.
--
-- Total de vendas entre R$ 5.000 e R$ 10.000 (inclusive): bônus de 8% do salário base.
--
-- Total de vendas menor que R$ 5.000: bônus de R$ 0.
--
-- Retorno da tabela:
--
-- nome_funcionario (varchar)
--
-- salario_base (numeric)
--
-- total_vendas (numeric)
--
-- bonus (numeric)

create or replace function calcular_bonus_funcionario()
returns table(
    nome_funcionario varchar,
    salario_base numeric,
    total_vendas numeric,
    bonus numeric
)
language plpgsql
as $$
declare
    v_funcionario record;
begin
    for v_funcionario in
        select f.nome, sum(v.valor_venda) as total_vendas, f.salario_base
        from vendas v
        join funcionario f on f.id = v.funcionario_id
        group by f.id, f.nome
    loop
        nome_funcionario := v_funcionario.nome;
        salario_base := v_funcionario.salario_base;
        total_vendas := v_funcionario.total_vendas;

        if total_vendas > 10000 then
            bonus := salario_base * 0.15;
        elsif total_vendas >= 5000 and total_vendas <= 10000 then
            bonus := salario_base * 0.08;
        elsif total_vendas < 5000 then
            bonus := 0;
        else
            bonus := 0;
        end if;

        return next;

    end loop;

end;
$$;