# comandos terminal postgreSQL

## instalação:

- pgAdmin Tutorial: https://www.tecmint.com/install-postgresql-with-pgadmin4-on-linux-mint/

- Boson Treinamentos playlist: https://youtube.com/playlist?list=PLucm8g_ezqNoAkYKXN_zWupyH6hQCAwxY

- Boson Treinamentos blog: http://www.bosontreinamentos.com.br/postgresql-banco-dados/instalacao-do-postgresql-e-do-phppgadmin-no-linux/

apt-get update

apt-get install postgresql postgresql-contrib

- criando usuario postgres
  `sudo -u postgres createuser -D -A -P username`

## configurar coneções TCP-IP

- editar arquivo postgresql.conf

  - `sudo nano /etc/postgresql/POSTGRES_VERSION/main/postgresql.conf`

    editar descomentando a linha escrita `listen_adresses = 'localhost'`

    e caso comentado, descomentar a linha escrita `port:5432`

    reiniciar o servico postgres: `service postgresql restart`

- criar servidor pgAdmin

  - `startPg` foi criado esta variavel de ambiente para iniciar o servidor.

## comandos prompt postgres:

- entrar no prompt postgres: `sudo -u postgres psql postgres`

- sair das coisa: `\q`

- criar senha para usuario: `\password user`

- mostrar bancos: `\l`

- conectar ao banco: `\connect dbName`

- mostrar tabelas: `\dt`

- criar banco: `createdb dbName`

- excluir usuario: `DROP USER username`

- excluir banco: `DROP DATABASE dbName`

- obter informaçao sobre onde esta conectado:`\conninfo`

- entrar no linux como postgres: `sudo -i -u postgres`

- utilitario de gerenciamento:`psql`

- mostrar todos comandos SQL disponiveis:`\h`

- buscar informaçao de um comando especifico: `\h comandoSQL`

- mostrar comandos internos do psql: `\?`

- mostrar usuarios:`\du`

- conectar num banco:`\c dbName`

- visualizar as tabelas:`\d`

- visualizar as tabelas administrativas do postgres:`\dS`

- sair do banco p executar algo no linux:`\!`, `\! codigo`

-
