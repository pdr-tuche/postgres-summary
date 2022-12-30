```SQL
INSERT INTO nome_tabela (coluna1, coluna2, coluna3, ...)
VALUES (dado1, dado2, dado3, ...);


INSERT INTO clientes (cod_cliente, nome_cliente, sobrenome_cliente)
VALUES
(1,'Fulano','de Tal'),
(2,'Beltrano','Silveira');

INSERT INTO produtos (cod_produto, nome_produto, descricao, preco_produto, qtde_estoque)
VALUES
(1,'alcool gel', 'garrafa de alcool gel de 1L', 12.90, 20),
(2, 'LUVAS DE PREDERO', 'caixa de luva de predero', 32.50, 25),
(3, 'pasta de dente', 'tubo de pasta de dente colgatxi', 3.60, 12),
(4, 'sabonete', 'sabonete antibateriao', 3.5, 5 ),
(5, 'enxaguante Bucal','antiseptico bucal 500ml', 17.00, 20);


INSERT INTO pedidos (cod_cliente, cod_produto, qtde_vendida)
VALUES
(1,2,3),
(2,3,2),
(1,3,4);

```
