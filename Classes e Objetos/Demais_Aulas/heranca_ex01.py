class Animal:
    def __init__(self, nome, comprimento, num_patas, cor, vel_media):
        self.nome = nome
        self.comprimento = comprimento
        self.num_patas = num_patas
        self.cor = cor 
        self.vel_media = vel_media
    
    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Comprimento:", self.comprimento)
        print("Num_patas:", self.num_patas)
        print("Cor:", self.cor)
        print("Vel_media:", self.vel_media)


class Peixe(Animal):
    def __init__(self, nome, comprimento, num_patas, cor, vel_media, caracteristica):
        super().__init__(nome, comprimento, num_patas, cor, vel_media)
        self.caracteristica = caracteristica
        if caracteristica == "morto":
            raise TypeError
        else:
            self.caracteristica = caracteristica

    def exibir_dados_peixe(self):
        super().exibir_dados()
        print("Caracteristica:", self.caracteristica)

tipo_peixe = Peixe ("Tilápia", "35 cm", 3, "Dourado", "15 km", "morto")
tipo_peixe.exibir_dados_peixe()