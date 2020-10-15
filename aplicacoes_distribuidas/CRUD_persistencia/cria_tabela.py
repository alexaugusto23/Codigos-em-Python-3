import psycopg2

sql_create = '''CREATE TABLE cliente_SORVERTUNES (id_cliente SERIAL 
                PRIMARY KEY, nome varchar(50), comentario 
                varchar(200))'''

def create_table():
    try:
        connection = psycopg2.connect(
            host = "127.0.0.1", # host = "localhost", 
            user = "postgres",
            password = "1901705",
            dbname = "DBImpacta"
        )
        cursor = connection.cursor()
        cursor.execute(sql_create)
        connection.commit()
        cursor.close()
        connection.close()
        print("Tabela criada")
    except:
        print("Erro ao criar a Tabela")            

create_table()

# ---------------------------------

import psycopg2

sql_create = '''CREATE TABLE cliente_jadir2 (id_cliente SERIAL 
                PRIMARY KEY, nome varchar(50), comentario 
                varchar(200))'''

def create_table():
    try:
        connection = psycopg2.connect(
            host = "dbimpacta.postgresql.dbaas.com.br",
            user = "dbimpacta",
            password = "impacta#2020",
            dbname = "dbimpacta"
        )
        cursor = connection.cursor()
        cursor.execute(sql_create)
        connection.commit()
        cursor.close()
        connection.close()
        print("Tabela criada")
    except:
        print("Erro ao criar a Tabela")            

create_table()