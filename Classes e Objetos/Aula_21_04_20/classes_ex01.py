class Animal:
    def __init__(self, nome): #Construtor
        self.nome = nome

    def talk(self):
        return "..."

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