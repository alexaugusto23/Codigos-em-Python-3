class Motor:
    def __init__ (self, cilindrada, potencia):
        self.cilindrada = int (cilindrada)
        self.potencia = int (potencia)

    def exibir(self):
        print("Dados do Motor: ")
        print("Cilindrada", self.cilindrada)
        print("Potencia: ", self.potencia)

class Veiculo:
    def __init__ (self,
                  peso,
                  velocidade_maxima,
                  preco,
                  tipo_motor):
        self.peso = int (peso)
        self.velocidade_maxima = int (velocidade_maxima)
        self.preco = float (preco)
        self.tipo_motor = tipo_motor

    def exibir(self):
        print("Peso: ", self.peso) 
        print("Velocidade_maxima", self.velocidade_maxima)
        print("Preço: ", self.preco)
        self.tipo_motor.exibir()


class CarroPasseio(Veiculo):
    def __init__(self,
                  peso,
                  velocidade_maxima,
                  preco,
                  tipo_motor,
                  cor,
                  modelo):
        super().__init__(peso,
                         velocidade_maxima,
                         preco,
                         tipo_motor)
        self.cor = str(cor)
        self.modelo = str(modelo)
    
    def exibir(self):
        super().exibir()
        print("Cor:", self.cor)
        print("Modelo:", self.modelo)



class Caminhao(Veiculo):
    def __init__(self, 
                  peso, 
                  velocidade_maxima, 
                  preco, 
                  tipo_motor,
                  toneladas,
                  altura,
                  comprimento):
        super().__init__(peso, 
                         velocidade_maxima, 
                         preco, 
                         tipo_motor)
        self.toneladas = int(toneladas)
        self.altura = float(altura)
        self.comprimento = float(comprimento)

    def exibir(self):
        super().exibir()
        print("Toneladas:", self.toneladas)
        print("Altura:", self.altura)
        print("Comprimento:", self.comprimento)

print("\n")
motor1 = Motor(1000, 100)
carro = CarroPasseio(800, 200, 30000.00, motor1, "Preto", "Gol")
carro.exibir()
print("\n")
motor2 = Motor(8000, 4000)
caminhao = Caminhao(4000, 250, 120000.0, motor2, 4, 2.5, 10.0)
caminhao.exibir()
print("\n")