from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, titular, agencia, conta, saldo):
            self.titular = titular
            self.agencia = int(agencia)
            self.conta = int(conta)
            self.saldo = float(saldo)

    @abstractmethod
    def exibir_dados(self):
        print("Nome: ", self.titular)
        print("Agência: ", self.agencia)
        print("Conta: ", self.conta)
        print("Saldo: ", self.saldo)


class Conta_Corrente(Conta):
    def __init__(self, titular, agencia, conta, saldo, limite):
        super().__init__(titular, agencia, conta, saldo)
        self.limite = limite

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError
        else:
            self.saldo += valor

    def sacar(self, valor):
        if valor > 0 and self.saldo+self.limite >= valor:
            self.saldo -= valor
        else:
            raise ValueError

    def transferir(self,conta_dest, valor):
        self.sacar(valor)
        return conta_dest.depositar(valor)


class Conta_Poupanca(Conta):
    def __init__(self, titular, agencia, conta, saldo):
        super().__init__(titular, agencia, conta, saldo)

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError
        else:
            self.saldo += valor

    def sacar(self, valor):
        if valor > 0:
            self.saldo -= valor
        else:
            raise ValueError

    def transferir(self,conta_dest, valor):
        self.sacar(valor)
        conta_dest.depositar(valor)

    def calcula_rend(self, taxa):
        self.saldo = saldo + (self.saldo * taxa / 100)


class Conta_Investimento(Conta):
    def __init__(self, titular, agencia, conta, saldo, taxa_adm):
        super().__init__(titular, agencia, conta, saldo)
        self.taxa_adm = 3

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError
        else:
            self.saldo += valor

    def sacar(self, valor):
        if valor > 0:
            self.saldo -= valor
        else:
            raise ValueError

    def transferir(self,conta_dest, valor):
        self.sacar(valor)
        return conta_dest.depositar(valor)

    def calcula_rend(self, taxa):
        self.saldo = self.saldo + (self.saldo * taxa / 100) - (self.saldo * self.taxa_adm / 100)

#if __name__ == "__main__":
    pass

conta1 = Conta_Corrente("Alex",643,10344911,0,0)
dep = Conta_Corrente.depositar(conta1,100)
print(conta1)
print(dep.saldo)

