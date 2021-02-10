class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
        return
    
    def dar_like(self):
        self.__likes += 1
        
   

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0
        self.duracao = duracao
                 
class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0
        self.temporadas = temporadas
    

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

atlanta.nome = "teste"
atlanta.dar_like()
atlanta.dar_like()
vingadores.dar_like()

print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração0: {vingadores.duracao} - Likes {vingadores.likes}")
print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes {atlanta.likes}")
