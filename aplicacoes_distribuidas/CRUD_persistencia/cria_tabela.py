import psycopg2

sql_create = '''CREATE TABLE cliente_sorvertunes (id_cliente SERIAL 
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