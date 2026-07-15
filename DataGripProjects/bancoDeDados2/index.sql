create index idx_produtos_nome on public.produtos(nome);

create index idx_pedidos_data_pedido on public.pedidos(data_pedido);

create index idx_pedido_data_cliente
on public.pedidos(data_pedido, cliente_id);

SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'pedidos';

reindex table public.pedidos;

reindex index idx_produtos_nome;



