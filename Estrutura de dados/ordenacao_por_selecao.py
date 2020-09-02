def ordenacao_selecao(lista):
    for i in range(len(lista)):
        indice_menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        temp = lista[indice_menor]
        lista[indice_menor] = lista[i]
        lista[i] = temp

numeros = [4,10,8,13,11]
print(numeros)
ordenacao_selecao(numeros)
print(numeros)


