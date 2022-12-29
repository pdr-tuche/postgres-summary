# criacao padrao do banco

```SQL
CREATE DATABASE banco_teste;
with
OWNER = propietarioDOBANCO
ENCODING = "UTF8"
LC_collate = 'pt_BR.UTF-8'//colacao dos caracteres
LC_CTYPE = 'pt_BR.UTF-8' // tipos de caracteres
TABLESPACE = 'pg_default'
CONNECTION LIMIT = -1;//LIMITACOES DE CONECAO -1 == INFINITO
```

# este e o codigo p gerar tudo padrao

```SQL
CREATE DATABASE banco_teste
```

- todas as configurações acima sao default
