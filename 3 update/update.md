```SQL
update tabela
set coluna = novo valor
where coluna = valor id

update produtos
set descricao = 'mudado descricao'
where code_produto = 11; //ira mudar a descricao do produto 11


update produtos
set preco = 3.90
where nome_produto = 'sabonete' // mudar preco para aquele com nome do produto

update produtos
set qtde_estoque = qtde_estoque -4
where nome_produto = 'esfregão'
```
