import psycopg2 as pg

USER = "postgres"
PASS = "postgres"
HOST = "localhost"
PORT = "5432"
BASE = "db_python"


def conecta_db_pessoa():
    conexao = pg.connect(user=USER, password=PASS,
                         host=HOST, port=PORT, database=BASE)
    return conexao


def exec(sql):
    con = conecta_db_pessoa()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()


def criar_tabela():
    sql = 'DROP TABLE IF EXISTS tb_pessoa'
    exec(sql)


def criar_colunas():
    sql = '''CREATE TABLE tb_pessoa(
        id INT PRIMARY KEY,
        nome VARCHAR(20) NOT NULL,
        sobrenome VARCHAR(40) NOT NULL
    );
    '''
    exec(sql)


def preencher_colunas():
    sql = '''INSERT INTO tb_pessoa (id, nome, sobrenome)
    VALUES
    (1,'Fulano','de Tal'),
    (2,'Beltrano','Silveira');
    '''
    exec(sql)


def pegar_dados(colunas, tabela):
    if colunas == "":
        sql = "select * from {}".format(tabela)
    else:
        sql = "select {} from {}".format(colunas, tabela)
    con = conecta_db_pessoa()
    cur = con.cursor()
    cur.execute(sql)
    dataSet = cur.fetchall()
    dataSetList = []
    for data in dataSet:
        dataSetList.append(data)
    con.close()
    return dataSetList
