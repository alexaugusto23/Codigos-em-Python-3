import classe_proprietario

class Carro:
    modelo = None
    cor = None
    ano = None
    marca = None
    __veloc_atual = 0

    def __init__(self,nome):
        self.proprietario = nome 

    def acelera(self):
        self.__veloc_atual += 1

    def freia():
        if self.veloc_atua != 0:
            self.__veloc_atua = 0
            
    def get_proprietario(self):
        return self.proprietario

class Endereco:

pro1 = classe_proprietario.Endereco("rua margarida", 0)

carro1 = Carro("Alex1235")
print(nome.get_proprietario())