import psycopg2

connection = psycopg2.connect(
    host="127.0.0.1",  # host = "localhost",
    user="postgres",
    password="1901705",
    dbname="DBImpacta"
)
cursor = connection.cursor()
cursor.execute("SELECT id_cliente, nome, comentario FROM cliente_sorvertunes")
rows = cursor.fetchall()  # um resultado de uma intrução SELECT
for row in rows:
    print("valores: ", row[0], row[1], row[2])
cursor.close()
connection.close()


# -----------------------------
'''
connection = psycopg2.connect(
    host="dbimpacta.postgresql.dbaas.com.br",
    user="dbimpacta",
    password="impacta#2020",
    dbname="dbimpacta"
)
cursor = connection.cursor()
cursor.execute("SELECT id_cliente, nome, comentario FROM cliente_SORVERTUNES")
row = cursor.fetchone()  # todos os resultados de uma intrução SELECT
print("valores: ", row[0], row[1], row[2])
cursor.close()
connection.close()
'''