""" Algoritimos de ordenação """


def ordenacao_selecao(lista):
    for i in range(len(lista)):
        indice_menor = i
        #print('seleção ind menor',indice_menor)
        #print(lista)
        print(lista)
        for j in range(i+1, len(lista)):
            #print("seleção segundo for",j)
            
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        
        temp = lista[indice_menor]
        # temp =  valor 3 no indice 3
        lista[indice_menor] = lista[i]
        # indice 3          =  valor 50 indice 0
        lista[i] = temp
        # indice 0 =  valor 3 
        
    return lista


def ordenacao_bolha(lista):
    print(lista)
    for i in range(0, len(lista)):# percorre toda a lista
        #print('anterior bolha i',i) 
        #print('tamanho da lista',len(lista)-i)
        #print(lista)
        for j in range(1, len(lista)-i):
            #print('proximo bolha j',j)
            if lista[j-1] > lista[j]:
                temp = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = temp  
        print(lista)
    return lista


def ordenacao_insercao(lista):
    for i in range(0,len(lista)-1):
        x = lista[i+1]
        j = i
        while j >= 0 and lista[j] > x:
            lista[j+1] = lista[j]
            j -= 1
            #print('j no while',j)
        lista[j+1] = x
        print(lista)
    return lista


lista1 = [17,21,20,56,31,95,49]
lista2 = [42,87,37,14,84,97,30]
lista3 = [65,91,60,75,57,79,66]
lista4 = [74,44,14,13,56,69,50]


print('\n')
#print('SELEÇÃO  \n' ,ordenacao_selecao(lista4))
print('\n')
print('BOLHA    \n' ,ordenacao_bolha(lista4))
print('\n')
#print('INSERÇÃO \n' ,ordenacao_insercao(lista4))
print('\n')