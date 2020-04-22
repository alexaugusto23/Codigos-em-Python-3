class Veiculo:
    def __init__(self, tipo, modelo, km):
        self.tipo = tipo
        self.modelo = modelo
        self.__km = km

    def exemplo(self):
        print("Carro")

    def get_km(self):
        print(self.__km)


class Carro(Veiculo):
    def __init__(self, tipo, modelo, km, portas):
        super().__init__(tipo, modelo, km)
        self.portas = portas
    
    def exibe(self):
        print(self.tipo)
        print(self.modelo)
        self.get_km()
        print(self.portas)
    
    def exemplo(self):
        print("Carro")

palio = Carro("Hatch", "Palio", 50000, 4)
palio.exibe()
palio.exemplo()
