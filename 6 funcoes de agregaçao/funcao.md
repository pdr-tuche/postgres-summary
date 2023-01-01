# funcoes de agregacao

computar um valor unico a partir de um conjunto de valores de entrada.

funcoes basicas

- COUNT

  ```SQL
  select count (*) from clientes //contando quantos clientes da tabela

  select count (*) as "qtde clientes" from clientes


  select count (coluna) from clientes //retorna o numero de itens nesta coluna ignorando nulos

  select count ( distinct coluna) from clientes //distinct retorna  produtos sem nomes repetidos

  ```

- MAX
- MIN
- SUM

  ```SQL
  select max(coluna) from produtos
  select min(coluna) from produtos
    //retornba valor maximop ou minimo
    select sum (preco) from produtos
    //soma de todos os precos;

  ```

- AVG

```SQL
    select avg (preco) from produtos;
    //media de preco

    select round(avg(preco),2) from ṕrodutods
    // media com arredondamento cm precisao de duas casas decimais

select round(avg(preco),2) from produtos
where nome_produto ='refrigerante';
media do preco dos refrigerantes



```
