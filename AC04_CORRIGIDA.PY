# Alexsandro Augusto Ignácio RA 1901705
from abc import ABC, abstractmethod


class Parte(ABC):
    def __init__(self, codigo, nome, descricao, valor):
            self.codigo = int(codigo)
            self.nome = nome 
            self.descricao = descricao
            self.valor = float (valor)

    @abstractmethod
    def calcular_valor (self):
        pass

    @abstractmethod
    def exibir (self):
        pass


class Parafuso(Parte):
    def __init__(self, codigo, nome, descricao, valor, comprimento, diametro):
        super().__init__(codigo, nome, descricao, valor)
        self.comprimento = float(comprimento)
        self.diametro = float(diametro)

    def calcular_valor (self):
        return self.valor

    def exibir (self):
        print("Código: ", self.codigo)
        print("Nome: ", self.nome)
        print("Descrição: ", self.descricao)
        print("Valor: ", self.valor)
        print("Comprimento: ",self.comprimento)
        print("Diamentro: ",self.diametro)


class Motor(Parte):
    def __init__(self, codigo, nome, descricao, valor, potencia, corrente, rpm):
        super().__init__(codigo, nome, descricao, valor)
        self.potencia = float(potencia)
        self.corrente = float(corrente)
        self.rpm = int(rpm)

    def calcular_valor (self):
        return self.valor

    def exibir (self):
        print("Código: ", self.codigo)
        print("Nome: ", self.nome)
        print("Descrição: ", self.descricao)
        print("Valor: ", self.valor)
        print("Potencia: ",self.potencia)
        print("Corrente: ",self.corrente)
        print("RPM: ",self.rpm)


class Item:
    def __init__(self, parte, quantidade):
        self.parte = parte
        self.quantidade = quantidade

    def calcular_valor(self):
        valor = self.quantidade * self.parte.calcular_valor()
        return valor

    def exibir (self):
        print("Partes: ", self.parte)
        print("Quantidade: ", self.quantidade)


motor = Motor(123,'V8','motor',20,1000,100,5)
motor.exibir()

print('\n------------------------------\n')

parafuso = Parafuso(562,'Sextavado','seis faces',1.00,6,2)
parafuso.exibir()

print('\n------------------------------\n')

item = Item(motor,10)
print(item.calcular_valor())