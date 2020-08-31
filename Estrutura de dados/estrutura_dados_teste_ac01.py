def reposiciona_maior(lista):
    maior = lista[0]
    index = 0
    for i in range(0,len(lista)):
        if (lista[i] > maior):
            maior = lista[i]
            index = i
    #print("maior",maior)
    #print("indice",index)
    aux = maior
    lista [index] = lista [len(lista)-1]
    lista [len(lista)-1] = aux
    return lista 
lista1 = [90, 69, 95, 100, 5, 70]
resultado = reposiciona_maior(lista1)
print(resultado)