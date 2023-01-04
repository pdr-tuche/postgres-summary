from tb_pessoaQuery import *

criar_tabela()
criar_colunas()
preencher_colunas()

data = pegar_dados("*", "tb_pessoa")
print(data)
