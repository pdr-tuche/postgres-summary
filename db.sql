CREATE DATABASE db_python;

CREATE TABLE tb_pessoa(
	id INT PRIMARY KEY,
	nome VARCHAR(20) NOT NULL,
	sobrenome VARCHAR(40) NOT NULL
);

INSERT INTO tb_pessoa (id, nome, sobrenome)
VALUES
(1,'Fulano','de Tal'),
(2,'Beltrano','Silveira');

SELECT * FROM tb_pessoa;