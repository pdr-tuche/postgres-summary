```SQL
select colunas
from tabela
[where condiçoes]
order by coluna, coluna ASC | DESC
```

- ASC e o padrao

```SQL
select * from produtos
order by nome_produtos;


sekect *from produtos
order by qtde_estoque desc;


ordenando baseado na primeira coluna
select nome_produto, preco from produtos order by nome_produto, preco;

a tabela preco vai ser ordenada baseado na ordenacao do nomeproduto


select nome_produto, descricao form produtos orderby descricao NULLS FRIST | last;

as cescricoes nulas sao exibidas primeiro ou por ultimo





select nome_produto, preco from produtos where preco > 10.00 order by oreci DESC
```
