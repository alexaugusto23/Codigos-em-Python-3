import psycopg2

def inserir_cliente(nome, comentario):
    try:
        connection = psycopg2.connect(
            host = "127.0.0.1", # host = "localhost", 
            user = "postgres",
            password = "1901705",
            dbname = "DBImpacta"
        )
        cursor = connection.cursor()
        sql = "INSERT INTO cliente_sorvertunes (nome, comentario) VALUES (%s, %s)"
        cursor.execute(sql, [nome, comentario])
        connection.commit()
        cursor.close()
        connection.close()
        print("Registro Inserido com sucesso")
    except Exception as erro:
        print(erro)


inserir_cliente("Priscila", "Teste Priscila")
inserir_cliente("Jose Carlos", "Teste de inserção")

#connection.rollback(). Cancela operação