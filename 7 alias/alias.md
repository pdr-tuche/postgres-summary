# alias AS "apelido"

```SQL
    select coluna1 as "Produto"
    from produtos
    where qtd_estoque >5;

    durante a consulta, o as ira entender a coluna 1 como Produto

    select nome_cliente as "nome",
    sobrenome_cliente as 'sobrenome'
    from cliente as CL;

    select cod_pedito as "codigo do pedido",
    qtde as "quanditade"
    from pedidos as p
    order by "Quantidade" desc;
    selecionadno duas tabelas do p ordenando por quanidade



```
