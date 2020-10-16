import psycopg2
try:
    connection = psycopg2.connect(
        host = "127.0.0.1", # host = "localhost", 
        user = "postgres",
        password = "1901705",
        dbname = "DBImpacta"
    )
except psycopg2.OperationalError:
    print('NÃO CONECTADO')
else:
    print('CONECTADO')

'''
Banco de Dados (PostgreSQL) remotamente:
host = "dbimpacta.postgresql.dbaas.com.br",
user = "dbimpacta",
password = “impacta#2020",
dbname = "dbimpacta"
Nome da tabela >> grupo
Campos:
RA(PK) >> integer
Nome do aluno >> varchar(50)
Email do aluno >> varchar(50)
Logradouro >> varchar(50)
Numero >> varchar(5)
Cep >> varchar(10)
Complemento >> varchar(20)
'''