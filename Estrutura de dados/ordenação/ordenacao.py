print('-'*30)
print('Seleção\n')
def ordenacao_selecao(lista):
    for i in range(len(lista)):
        indice_menor = i
        print('seleção ind menor',indice_menor)
        for j in range(i+1, len(lista)):
            print("seleção segundo for",j)
            
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        
        temp = lista[indice_menor]
        # temp =  valor 3 no indice 3
        lista[indice_menor] = lista[i]
        # indice 3          =  valor 50 indice 0
        lista[i] = temp
        # indice 0 =  valor 3 
    return lista

listaex = [50,18,86,3,10,5,57]
print(ordenacao_selecao(listaex))

print('\n')
print('-'*30)
print('bolha\n')

def ordenacao_bolha(lista):
    for i in range(0, len(lista)):# percorre toda a lista
        #print('anterior bolha i',i) 
        #print('tamanho da lista',len(lista)-i)
        print(lista)
        for j in range(1, len(lista)-i):
            #print('proximo bolha j',j)
            if lista[j-1] > lista[j]:
                temp = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = temp
        
    return lista

listaex2 = [83, 31, 4, 29, 82, 30, 37, 29]
print(len(listaex2))
print(ordenacao_bolha(listaex2))

print('\n')
print('-'*30)
print('inserção\n')

def ordenacao_insercao(lista):
    for i in range(0,len(lista)-1):
        x = lista[i+1]
        j = i
        print(lista)
        while j >= 0 and lista[j] > x:
            lista[j+1] = lista[j]
            j -= 1
            #print('j no while',j)
        lista[j+1] = x
    return lista
listaex3 = [0, 19, 38, 95, 55, 34, 87, 64, 51]
#print(len(listaex3))
print(ordenacao_insercao(listaex3))

