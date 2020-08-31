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

andares = [-3,-2,-1,0,1,2,3,4,5,8,7,8,9,10]

 

andar_max = max(andares)

print(andar_max)

 

andares = [-3,-2,-1,0,1,2,3,4,5,8,7,8,9,10]

 

andar_min = min(andares)

print(andar_min)

 

andar_atual = 10

 

for i in andares:

  andar_max2 = i 

print("teste max andar2",andar_max2)

 

for i in andares[::-1]:

  andar_min2 = i 

print("teste min andar2",andar_min2)
