import modulo 
modulo.Animais.nomes()
modulo.Animais2.nomes()
print('--------------------------------------------')
from modulo import Animais, Animais2
an = Animais('mamute')
print(an.especie_get())
Animais2.nomes()

if __name__ == "__main__":
    print('principal')
else: 
    print('modulo')

