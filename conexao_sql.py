# C reate (Criação)
# R ead (Consulta)
# U pdate (Atualização)
# D elete (Destruição)

import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-DV3VOJ6\SQLEXPRESS;'
                      'Database=testDB;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

def inserir():
    for i in range (0,1):
        nome =  input("Digite o Nome: ")
        idade =  input("Digite a Idade: ")
        cidade =  input("Digite a Cidade: ")
        
        query = "INSERT INTO testDB.dbo.pessoas (nome,idade,cidade) VALUES(?,?,?)" 
        cursor = conn.cursor()
        cursor.execute(query,[nome,idade,cidade])
        conn.commit()
        print ("enviado com sucesso")
        print('\n')

def select():
    cursor.execute('SELECT * FROM testDB.dbo.pessoas')

    for row in cursor:
        print(row)

    cursor.execute('''
                    UPDATE testDB.dbo.pessoas 
                    SET IDADE = 31
                    WHERE NOME = 'Alex'
                    ''')
    conn.commit()

def deletar():
    cursor.execute('''
                    DELETE FROM testDB.dbo.pessoas 
                    WHERE NOME = 'Alex'
                    ''')
    conn.commit()
    print ("enviado com sucesso")


#inserir1 = inserir()
#sel = select()

delet = deletar()