import sqlite3

conn = sqlite3.connect("galeria.db")

cursor = conn.cursor()

def criar_table():
      sql = """
      CREATE TABLE albuns(titulo text, artista text, data_lancamento text,
      data_publicacao text, midia text)    
      """

      cursor.execute(sql)
      conn.commit()

def grava_album():
      sql = "INSERT INTO albuns VALUES('Glow', 'Andy Hunter', '24/07/2012', 'Xplore Records', 'MP3')"

      cursor.execute(sql)
      conn.commit()

def grava_muitos():
      albuns = [('Exodus', 'Andy Hunter', '09/07/2002', 'Sparrow Records', 'CD'),
                ('Until We have Faces', 'Red', '01/02/2011', 'Essential Records','CD')]
     

      cursor.executemany("INSERT INTO albuns VALUES(?,?,?,?,?)", albuns)
      conn.commit()

def atualiza ():
      sql= """
      UPDATE albuns SET artista = 'John Doe'
      WHERE artista = 'Andy Hunter'
      """

      cursor.execute(sql)
      conn.commit()

def excluir ():
      sql = """
      DELETE FROM albuns where artista = 'John Doe'
      """

      cursor.execute(sql)
      conn.commit()

def excluirlinha ():
      sql = """
      DELETE FROM rows albuns where id = 2
      """

      cursor.execute(sql)
      conn.commit()

def listar ():
      sql = """
      SELECT rowid, * FROM albuns ORDER BY artista 
      """
      cursor.execute(sql)
      
      for row in cursor.fetchall():
            print(row)
      
      
      
      



      
      
