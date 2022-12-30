Operador de comparacao
intervalo de dados

```SQL
select
from
where coluna between valor1 and valor2;

select
from
where coluna not between valor1 and valor2;



example

select nome_produto , preco
from produtos
where
    preco between 3.50 and 5.00;


select nome_produto , preco
from produtos
where
    preco between 3.50 and 5.00 or
    preco between 10.00 and 20.00;
```
