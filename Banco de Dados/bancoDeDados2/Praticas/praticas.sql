-- Consulta Simples: Selecione apenas o nome e o preco de todos os produtos.
select nome, preco from produtos;


-- Atualização (Update): Altere o preço do produto 'Fone Bluetooth' para 180.00.
UPDATE produtos set preco = 180.00 where nome = 'Fone Bluetooth';


-- Junção (Join): Liste o nome do cliente e o valor total de todos os seus pedidos.
select clientes.nome, pedidos.valor_total from clientes
inner join pedidos on clientes.id = pedidos.cliente_id;

-----

-- Relatório de Itens (Difícil): Liste o nome do cliente e os nomes dos produtos que ele comprou.
-- (Você precisará unir 4 tabelas: clientes, pedidos, itens_pedido e produtos).
select clientes.nome, produtos.nome
from clientes
inner join pedidos on clientes.id = pedidos.cliente_id
inner join itens_pedido on pedidos.id = itens_pedido.pedido_id
inner join produtos on itens_pedido.produto_id = produtos.id;


-- Liste o nome do cliente, o ID do pedido e o valor total apenas dos pedidos que estão com o status 'entregue'.
select clientes.nome, pedidos.id, pedidos.valor_total
from clientes
inner join pedidos on clientes.id = pedidos.cliente_id
where pedidos.status = 'entregue';


-- Liste o nome do cliente e o nome da categoria de cada produto que ele comprou.
select clientes.nome, categorias.nome
from clientes
inner join pedidos on clientes.id = pedidos.cliente_id
inner join itens_pedido on pedidos.id = itens_pedido.pedido_id
inner join produtos on itens_pedido.produto_id = produtos.id
inner join categorias on produtos.categoria_id = categoria_id;


-- Pedidos e Clientes: Mostre o nome do cliente e a data_pedido de todos os pedidos realizados (una clientes e pedidos).
select clientes.nome, pedidos.data_pedido
from clientes
inner join pedidos on clientes.id = pedidos.cliente_id;


-- Produtos e Itens: Liste o nome do produto e a quantidade de cada item vendido (una produtos e itens_pedido).
select produtos.nome, itens_pedido.quantidade
from produtos
inner join itens_pedido on produtos.id = itens_pedido.produto_id;


-- Filtro por Status: Mostre o nome do cliente e o valor_total apenas dos pedidos que estão com o status 'pendente'.
select clientes.nome, pedidos.valor_total
from clientes
inner join pedidos on clientes.id = pedidos.cliente_id
where pedidos.status = 'pendente';

SELECT COUNT(*) FROM pedidos;






