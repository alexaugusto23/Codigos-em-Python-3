lista = []

lista.append(2)
lista.append(3)
lista.append(6)
lista.append(8)

for val in enumerate (lista):
    print(val)

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

lista2 = []

for cont in range (0,5):
    lista2.append(int(input('Digite um valor: ')))
for val in lista2:
    print(val)

