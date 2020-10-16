import psycopg2
connection = psycopg2.connect(
host = "127.0.0.1", # host = "localhost", 
user = "postgres",
password = "1901705",
dbname = "DBImpacta"

)
column_names = []
data_rows = []
cursor = connection.cursor()
cursor.execute("SELECT * FROM cliente_sorvertunes")
column_names = [desc[0] for desc in cursor.description]
for row in cursor:
    data_rows.append(row)
print("Nome das colunas: {}\n".format(column_names))
print("Valores das colunas:", data_rows[0])