import psycopg2

def deletar_registros():
    try:
        connection = psycopg2.connect(
            host = "127.0.0.1", # host = "localhost", 
            user = "postgres",
            password = "1901705",
            dbname = "DBImpacta"
        )
        cursor = connection.cursor()
        destruir = "DROP TABLE cliente_sorvertunes"
        cursor.execute(destruir)
        connection.commit()
        cursor.close()
        connection.close()
        print("Tabela deletada com sucesso")
    except Exception as erro:
        print(erro)

deletar_registros()
