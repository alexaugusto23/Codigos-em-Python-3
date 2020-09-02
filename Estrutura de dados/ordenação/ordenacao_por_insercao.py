# Ordenação por inserção ou insert sort

def ordenacao_insercao(lista):
    for i in range(0,len(lista)-1): # i varia de 0 at ́e len(lista)-2, ou seja, da 1a at ́e a pen ́ultima posi ̧c~ao da lista
        # Insere lista[i+1] em lista[0],...,lista[i].
        x = lista[i+1] # guarda o valor de lista[i+1] em x, pois ele ser ́a perdido nos deslocamentos `a direita (while abaixo).
        j = i
        while j >= 0 and lista[j] > x:
            lista[j+1] = lista[j] # desloca lista[j] 1 posi ̧c~ao para a direita
            j -= 1
        lista[j+1] = x # copia x na posi ̧c~ao adequada da sublista ordenada
    return lista

lista1 = [5,6,3,78,84,54]
resultado = ordenacao_insercao(lista1)
print(resultado)