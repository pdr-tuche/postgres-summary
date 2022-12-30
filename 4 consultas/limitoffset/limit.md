```SQL
select coluna
from tabela
order by coluna
limit contagem | all
offset deslocamento


contagem = quantidade de linhas a exibir
all = mostrar todas as linhas
deslocamento = quantas linhas devem ser puladas antes de iniciar a contagem do limit



//ver 4 produtos mais baratos

select * from produtos
order by preco
limit 4


//3 produtos mais caros
select * from produtos
order by preco desc
limit 3;


select * from produtos
order by preco desc
limit 3 offset 2; //o offset tira os dois primeiros


select * from produtos
order by preco desc
offset 2; //o offset vai ignorar os dois primeiros da lista





```
