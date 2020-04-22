from abc import ABC, abstractclassmethod
from random import uniform

class Pessoa(ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    @abstractclassmethod
    def get_cpf(self, cpf):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.ra = int(uniform(1, 1000))

    def get_cpf(self):
        return self.cpf
    
    def reset_ra(self):
        self.ra = 0

class Professor(Pessoa):
    def __init__(self, nome, cpf, cargo):
        super().__init__ (nome, cpf)
        self.__cargo = cargo

a1 = Aluno("Alex",123456)
print(a1.get_cpf())

#https://en.wikipedia.org/wiki/Edsger_W._Dijkstra
