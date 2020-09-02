lista = [4,10,8,13,11]
index = 0
menor = 0
maior = 0
aux = 0


for i in range(0,len(lista)-1):
    if (lista[i] < lista[i+1]):
        menor = lista[i]
        index += 1
        aux = menor[index]
        

print(lista)



