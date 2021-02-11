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
    
    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.likes}"

        
 
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        str = "minutos"
        return f"{self.nome} - {self.ano} - {self.likes} - {self.duracao} {str}"
                 
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        str = "temporada" if self.temporadas <= 1 else "temporadas"
        return f"{self.nome} - {self.ano} - {self.likes} - {self.temporadas} {str}"
    

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
et = Filme('et', 1990, 140)
atlanta = Serie('atlanta', 2018, 2)
secret_key = Serie('secret key', 2017, 1)
filmes_e_series = [vingadores, et, atlanta, secret_key]

atlanta.dar_like()
atlanta.dar_like()
vingadores.dar_like()


for programa in filmes_e_series:
    print(programa)
