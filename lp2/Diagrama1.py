from abc import ABC, abstractclassmethod


class Cadastro():

    def __init__(self):
        self.pessoa = []

    def cadastrar_pessoa(pessoa):
        self.pessoa.append(pessoa)

    def exibir_cadastro():
        for i in self.pessoa:
            print("Nome: ", i.nome)


class Pessoa(ABC):

    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    @abstractclassmethod
    def exibir_dados():
        print("Nome: ", self.nome)
        print("Data: ", self.nascimento)


class Data():
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


class Cliente(Pessoa):
    def __init__(self, nome, data, codigo):
        super().__init__(nome,data)
        self.codigo = codigo

    def exibir_dados(self):
        super().exibir()
        print("Codigo: ", self.codigo)


class Funcionario(Pessoa):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario
    
    def calcular_imposto():
        return self.salario * 1.03
    
    def exibir_dados(self):
        super().exibir()
        print("Salario: ", self.salario)


class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario

    def calcular_imposto():
        return self.salario * 1.05
    
    def exibir_dados(self):
        super().exibir()
        print("Salario: ", self.salario)

data = Data(29,1,2000)
cliente = Cliente("alex",data,123)
print(cliente.nascimento.dia,'-',cliente.nascimento.mes,'-',cliente.nascimento.ano)