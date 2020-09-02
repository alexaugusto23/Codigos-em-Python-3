# Ordenação pelo método da bolha ou bubble sort

def ordenacao_bolha(lista):
    for i in range(0, len(lista)): # repetimos o processo len(lista) vezes
        for j in range(1, len(lista)-i):# a cada repeti ̧c~ao do processo, comparamos lista[j-1] com lista[j] at ́e o final da sublista n~ao-ordenada
            if lista[j-1] > lista[j]:
                temp = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = temp
    return lista

lista1 = [5,6,3,78,84,54]
resultado = ordenacao_bolha(lista1)
print(resultado)