'''
Uma classe que simula uma calculadora de 4 operações,
calculando dois números fornecidos pelo usuário e exibindo
o resultado quando solicitado.
'''


class Calculadora:
    x = 0
    y = 0
    resultado = 0

    def somar(self, x, y):
        self.resultado = x + y

    def subtrair(self, x, y):
        self.resultado = x - y

    def multiplica(self, x, y):
        self.resultado = x * y

    def exibir(self):
        print(self.resultado)


calc = Calculadora()
calc.somar(10, 20)
calc.exibir()
calc.subtrair(40, 21)
calc.exibir()
calc.multiplica(5, 7)
calc.exibir()