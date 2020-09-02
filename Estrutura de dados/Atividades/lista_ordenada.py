'''
Construa a função 
lista_ordenada(lista), 
que recebe uma lista como 
parâmetro e devolve True se a 
lista está ordenada (em ordem 
crescente) e False caso contrário.

Dica: dizemos que uma lista 
está ordenada quando 
lista[0] <= lista[1] <= 
lista[2] <= ... <= lista[n-1], 
onde n é o tamanho da lista.
'''
'''
def lista_ordenada(lista):
    lista_ordenada = []
    tam = len(lista)
    for i in range(tam):
        menor = lista[0]
        for j in range(len(lista)):
            if lista[j] < menor:
                menor = lista[j]
                pos_menor = j
        lista_ordenada.append(menor)
        lista.remove(menor)
    for i in lista_ordenada:
        print(i) 
'''
'''

def lista_ordenada(lista):
    n = len(lista)
    for i in range(0,n):
        print("Ìndices",i,end = " ")
        print("valores",lista[i])
       # n = +1
       # n -= 1
        #print("lista ",lista[i],n)
'''

def lista_ordenada(lista):
    for i in range(1,len(lista)):
        #print("elemento1",lista[i-1],i, end = " ")
        #print("elemento2", lista[i], i)
        if lista[i -1] > lista[i]:
            return False
    return True

lista1 = [3, 1, 2, 4]
lista2 = [1, 2, 3]
lista_ordenada(lista1)

'''
def lista_ordenada(sequencia):
    for i in range (1, len(sequencia):
        if sequencia[i -1] > sequencia[i]:
            return False
	return True
'''