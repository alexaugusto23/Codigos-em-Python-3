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