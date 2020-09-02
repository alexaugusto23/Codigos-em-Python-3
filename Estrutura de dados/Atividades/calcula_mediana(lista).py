def calcula_mediana(lista):
    ordenacao_selecao(lista)
    index = 0
    if (len(lista) % 2 == 1):
        index = len(lista)//2
        return lista[index]
    else:
        index = len(lista)//2
        return (float(lista[index-1]+lista[index])/2)


def ordenacao_selecao(lista):
    for i in range(len(lista)):
        indice_menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        temp = lista[indice_menor]
        lista[indice_menor] = lista[i]
        lista[i] = temp


lista1 = [8, 2, 1, 10, 4]   #4
#lista1= [20, 40, 65, 87]    #52,5
print (lista1)
mediana = calcula_mediana(lista1)
print(mediana)