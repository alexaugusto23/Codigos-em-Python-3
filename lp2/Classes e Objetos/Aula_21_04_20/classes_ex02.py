class SerVivo:
    def __init__(self, nome):#Construtor
        self.nome = nome

    def talk(self):
        return "NADA"

class Animal(SerVivo):
    def __init__(self, nome): #Construtor
        super().__init__(nome)

class Gato(Animal):
    def __init__(self, nome): #Construtor
        super().__init__(nome)
    
    def talk(self):
        return "Miau!"

class Cachorro(Animal):
    def __init__(self, nome): #Construtor
        super().__init__(nome)
    
    def talk(self):
        return "Au Au!"

cat = Gato('cat')
dog = Cachorro('dog')
capivara = Animal('capivara')
lista_animal = [cat, dog,capivara]

for animal in lista_animal:
    print(animal.nome, ":", animal.talk())

print("\n.............\n")

def teste(animal):
    print(animal.talk())

teste(dog)
teste(cat)
teste(capivara)

