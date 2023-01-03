# join

clausulas join sao usadas para combinar dados provenientes de duas ou mais tabelas em um unico conjunto de resultados, baseado em condiçoes de join especificadas.

- `inner join`: retorna linhas quando houver pelo menos uma correspondencia em ambas as tabelas.

- `outer join`: retorna linhas mesmo quando nao houver pelo menos uma correspondencia em uma das tabelas (ou ambas). O outer join divide-se em left join, right join e cross join.

**inner join seria a intersecção de duas tabelas.**

## clausula on

a clausula `on` determina a condicao de join, que indica como as tabelas devem ser comparadas.

no geral a comparacao ocorre por meio de um relacionamento entre chave orunarua bna oruneura tabela e chave estrangeira na segunda tabela.

```SQL
select colunas
from tabela1
    [inner] join tabela2
    on tabela1.coluna = tabela2.coluna
    [inner] join tabelaN
    on tabela1.coluna = tabelaN.coluna
where condicoes



select pedidos.cod_pedidos, produtos.nome_produtos, pedidos.qtde from pedidos
inner join produtos
on pedidos.cod_produto = produtos.cod_produto;


select PE.cod_pedido, PR.nome_produto, PE.qtde
from pedidos PE
inner join produtos PR
on PE.cod_produtos = PR.cod_produto
where PE.cod_pedido = 9

```
