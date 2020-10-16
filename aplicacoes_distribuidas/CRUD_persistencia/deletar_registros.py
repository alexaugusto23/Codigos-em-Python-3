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
        excluir = "DELETE FROM cliente_sorvertunes"
        cursor.execute(excluir)
        connection.commit()
        cursor.close()
        connection.close()
        print("Registros deletados com sucesso")
    except Exception as erro:
        print(erro)

deletar_registros()
