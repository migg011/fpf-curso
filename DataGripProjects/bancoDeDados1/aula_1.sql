CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome varchar(100),
    email VARCHAR(100) unique,
    senha varchar(100) unique,
    endereco varchar(100),
    telefone varchar(100)
);

CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nome varchar(100) unique,
    descricao varchar(1000)
);

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome varchar(100),
    descricao varchar(1000),
    preco float,
    quantidade_estoque int,
    categoria_id int,
    imagem varchar(100),
    marca varchar(100),
    FOREIGN KEY (categoria_id) references categorias(id)
);


CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INT,
    data_pedido DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) DEFAULT 'pendente',
    valor_total NUMERIC(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE TABLE itens_pedido (
    id SERIAL PRIMARY KEY,
    pedido_id INT,
    produto_id INT,
    quantidade INT,
    valor_unitario NUMERIC(10,2),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

CREATE TABLE pagamentos (
    id SERIAL PRIMARY KEY,
    pedido_id INT,
    forma_pagamento VARCHAR(50),
    data_pagamento DATE,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
);

INSERT INTO categorias (nome)
VALUES ('Eletrônicos'), ('Livros');

INSERT INTO produtos (nome, preco, categoria_id)
VALUES('Smartphone', 1500.00, 1), ('SQL para Iniciantes', 80.00, 2), ('Fone Bluetooth', 200.00, 1);

INSERT INTO clientes (nome, email)
VALUES ('Ana Silva', 'ana@email.com'), ('Bruno Costa', 'bruno@email.com');

INSERT INTO pedidos (cliente_id, valor_total, status)
VALUES (1, 1500.00, 'entregue'), (2, 280.00, 'pendente');

INSERT INTO clientes (nome, email, senha, endereco, telefone)
values ('João', 'João Silva', 'senha123', 'Rua A, 123, São Paulo', '11987654321');

update clientes set nome = 'João Silva'
where nome = 'João';

update clientes set email = 'joaosilva@gmail.com'
where email = 'João Silva';

UPDATE clientes SET senha = 'senha123456'
WHERE nome = 'João Silva';

SELECT * from clientes
where nome ilike 'JO%';

select * from clientes where id in (3,7,9);
select * from clientes where id between 3 and 8;

--selecionando todos os pedidos e seus respectivos clientes.
select p.*, c.nome
from pedidos p
inner join public.clientes c on c.id = p.cliente_id;

-- selecionando os campos data de pedido, valor do produto, status e com o nome do cliente
-- ordenado de maneira crescente/decrecente  (order by + coluna nome + asc/desc).
select p.data_pedido, p.valor_total as valor_do_pedido, p.status, c.nome
from pedidos p
inner join public.clientes c on c.id = p.cliente_id
order by c.nome asc; --/desc


-- selecionando todos os pedidos e seus respectivos clientes, iremos substituir email antigo
-- por um novo: Vamos criar uma coluna com um novo email onde sera
-- baseado no nome do cliente utilizando join com a tabela de cliente.
select
    p.id,
    p.data_pedido,
    p.status,
    p.valor_total,
    p.cliente_id || ' - ' || c.nome as id_nome_cliente,
    c.email as email_antigo,
    replace(c.nome, ' ', '_') || '@outlook.com' as novo_email
from pedidos p
inner join public.clientes c on p.cliente_id = c.id;


-- consulta de clientes e a quantidade de pedidos usando inner join e filtrando somente
-- os pedidos 'entregue'

select c.nome, c.email, count(p.id) as qnt_pedido, sum(p.valor_total) as total_pedidos
from clientes c
inner join pedidos p on c.id = p.cliente_id
where p.status = 'entregue'
group by c.nome, c.email
order by c.nome asc;

-- consulta de clientes agrupando por status de pedidos
select
    c.nome,
    c.email,
    status,
    count(p.id) as qnt_pedido,
    sum(p.valor_total) as total_pedido
from clientes as c
inner join pedidos p on c.id = p.cliente_id
group by c.nome, c.email, status
order by c.nome asc;

-- consultas com a agregação sum
select sum(valor_total) as soma_total
from pedidos
where cliente_id = 1;

select c.nome, sum(p.valor_total) as valor
from pedidos p
inner join clientes c on c.id = p.cliente_id
group by c.nome ;

--atividade

--1
SELECT
    c.nome AS nome_cliente,
    p.data_pedido,
    p.status AS status_pedido,
    pr.nome AS nome_produto,
    ip.valor_unitario AS valor_item
FROM pedidos p
INNER JOIN clientes c ON p.cliente_id = c.id
INNER JOIN itens_pedido ip ON ip.pedido_id = p.id
INNER JOIN produtos pr ON ip.produto_id = pr.id;

--2
SELECT
    c.nome AS nome_cliente,
    p.status AS status_pedido,
    p.valor_total
FROM pedidos p INNER JOIN clientes c ON p.cliente_id = c.id
WHERE p.data_pedido BETWEEN '2024-08-01' AND '2024-08-31'
ORDER BY p.valor_total DESC
LIMIT 10;

--3
UPDATE pedidos SET status = 'cancelado'
WHERE id IN (39, 42, 99, 26, 71) AND status = 'pendente';









