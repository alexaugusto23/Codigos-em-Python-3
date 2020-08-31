'''
Definição da Classe Cachoro:
- Atributos: nome, peso, idade, cor
- Metodo: Latir, Andar

'''


class Cachorro:
    nome = None
    peso = None
    idade = None
    cor = None

    def __init__(self, nome, idade):
        print("Criação do objeto")
        self.nome = nome
        self.idade = idade

    def latir(self):
        print("Au Au")

    def andar(self):
        if self.idade > 10:
            print(self.nome, "não andou, está cansado")
        else:
            print(self.nome, "andou")


meu_cachorro = Cachorro("Rex", 5)
meu_cachorro.peso = 8.0
print(meu_cachorro.nome)
meu_cachorro.latir()
meu_cachorro.andar()

meu_cachorro2 = Cachorro("Snoopy", 11)
meu_cachorro2.andar()
