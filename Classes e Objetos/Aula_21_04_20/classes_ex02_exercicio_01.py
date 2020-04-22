class Animal:
    def __init__(self, nome, idade):#Construtor
        self.nome = nome
        self.idade = idade

    def som(self):
        print("O animal emitiu um som")


class Cachorro(Animal):
    def __init__(self, nome, idade): #Construtor
        super().__init__(nome, idade)
    
    def som(self):
        print("au au!")




class Cavalo(Animal):
    def __init__(self, nome, idade): #Construtor
        super().__init__(nome, idade)
    
    def som(self):
        print("ih ih ih!")

class Preguica(Animal):
    def __init__(self, nome, idade): #Construtor
        super().__init__(nome, idade)
    
    def som(self):
        print("ZzZzZzZzZz")

class Veterinario:
    def examinar(self,animal):
        animal.som()

class Zoologico:
    def __init__(self): #Construtor
        self.lista = []
    
    def lista_zoo(self,animal):
        self.lista.append(animal)
        for animal_lista in self.lista:
            #print(animal_lista)
            animal_lista.som()


'''
Outro jeito de fazer
class Zoologico:
    def __init__(self): #Construtor
        self.lista = []

    def lista_zoo_inserir(animal):
        self.lista.append(animal)
    
    def lista_zoo_percorre(animal):
        for i in self.lista:
            animal.som()
        print(self.lista)

'''

dog_zeca = Cachorro('Zeca',10)
cavalo = Cavalo('Petruquio',11)
pri_pregui = Preguica('Pregui',12)

lista_animal = [dog_zeca, cavalo, pri_pregui]

for animal in lista_animal:
    print(animal.nome, ":", animal.som(),"\nIdade",animal.idade)

print("\n---------------------------\n")
print("Classe Veterinario\n")

vet = Veterinario()
vet.examinar(dog_zeca)
vet.examinar(cavalo)
vet.examinar(pri_pregui)

print("\n---------------------------\n")
print("Classe Zoologico\n")

zoo = Zoologico()
zoo.lista_zoo(dog_zeca)
zoo.lista_zoo(cavalo)
zoo.lista_zoo(pri_pregui)

print("\n---------------------------\n")



