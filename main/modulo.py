class Animais():
    def __init__(self, especie):
        self.especie = especie
        self.idade = 10

    def especie_get(self):
        return self.especie
    
    def idade_get(self):
        return self.idade

    def nomes():
        print('dog 1')
        print('dog 2')

class Animais2():

    def nomes():
        print('dog 3')
        print('dog 4')

if __name__ == "__main__":
    Animais().nomes()
    Animais2().nomes()