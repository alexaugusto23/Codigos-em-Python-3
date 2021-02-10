class Filme:

    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:

    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas 

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração0: {vingadores.duracao}")

atantla = Serie('atlanta', 2018, 2)
print(f"Nome: {atantla.nome} - Ano: {atantla.ano} - Temporadas: {atantla.temporadas}")