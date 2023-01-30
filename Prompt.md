# comandos prompt postgres:

- entrar no prompt postgres: 
 ```bash 
 sudo -u postgres psql postgres
 ```

- entrar no linux como postgres: 
```bash 
sudo -i -u postgres
```

- entrar com user em um banco especifico:
```bash
psql -U username dbName
```

- abrir prompt postgres:
```bash
sudo -i -u postgres
```


- criar banco: 
``` bash
createdb dbName
```


- sair das coisa: `\q`

- criar senha para usuario: `\password user`

- mostrar bancos: `\l`

- conectar ao banco: `\connect dbName`

- mostrar tabelas: `\dt`

- excluir usuario: `DROP USER username`

- excluir banco: `DROP DATABASE dbName`

- obter informaçao sobre onde esta conectado:`\conninfo`



- utilitario de gerenciamento:`psql`

- mostrar todos comandos SQL disponiveis:`\h`

- buscar informaçao de um comando especifico: `\h comandoSQL`

- mostrar comandos internos do psql: `\?`

- mostrar usuarios:`\du`

- conectar num banco:`\c dbName`

- visualizar as tabelas:`\d`

- visualizar as tabelas administrativas do postgres:`\dS`

- sair do banco p executar algo no linux:`\!`, `\! codigo`

- criando user com auxilio da cli `create user --interactive Username`
