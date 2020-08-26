def reposiciona_maior(lista):
    for i in range(1,len(lista)):
        aux = 0
        maior = lista[0]
        if (lista[i-1] > lista[1]):
            maior = lista[i]
    aux = lista[0]
    lista [0] = lista [len(lista)-1]
    lista [len(lista)-1] = aux
    return lista 

lista1 = [90, 69, 95, 16, 5, 70]
resultado = reposiciona_maior(lista1)
print(resultado)