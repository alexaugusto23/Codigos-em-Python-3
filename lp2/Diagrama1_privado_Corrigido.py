from abc import ABC, abstractmethod


class Cadastro:
    def __init__(self):
        self.__lista_pessoas = []
    
    def cadastrar_pessoa(self, pessoa):
        self.__lista_pessoas.append(pessoa)
    
    def exibir_cadastro(self):
        for pessoa in self.__lista_pessoas:
            pessoa.exibir_dados()


class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    @abstractmethod
    def exibir_dados(self):
        pass


class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def exibir(self):
        print(self.__dia, "/", self.__mes, "/", self.__ano)


class Cliente(Pessoa):
    def __init__(self, nome, nascimento, codigo):
        super().__init__(nome, nascimento)
        self.codigo = codigo

    def exibir_dados(self):
        print("CLIENTE:", self.nome, self.codigo)
        self.nascimento.exibir()


class Funcionario(Pessoa):
    def __init__(self, nome, nascimento, salario):
        super().__init__(nome, nascimento)
        self.salario = salario

    def exibir_dados(self):
        print("FUNCIONARIO:", self.nome, self.salario)
        self.nascimento.exibir()

    def calcular_impostos(self):
        return self.salario * 0.03


class Gerente(Funcionario):
    def __init__(self, nome, nascimento, salario, area):
        super().__init__(nome, nascimento, salario)
        self.area = area

    def calcular_impostos(self):
        return self.salario * 0.05

    def exibir_dados(self):
        print("GERENTE:", self.nome, self.salario)
        self.nascimento.exibir()


if __name__ == "__main__":
    cad = Cadastro()
    func = Funcionario("Fernando", Data(27, 11, 1987), 2500.0)
    cliente = Cliente("Carlos", Data(17, 5, 1977), 73)
    gerente = Gerente("Gabriel", Data(8, 8, 1988), 4000, "adm")
    cad.cadastrar_pessoa(func)
    cad.cadastrar_pessoa(cliente)
    cad.cadastrar_pessoa(gerente)
    cad.exibir_cadastro()