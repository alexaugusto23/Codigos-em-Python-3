# Sequência Fibonacci

contador = 0
ant = 0
prox = 1
lista_numeros = []
n = int(input())
if n <= 0:
    n = None
else:
    lista_numeros.append(ant)
    lista_numeros.append(prox)
    print(ant, end = ' ')
    print(prox, end = ' ')
        
    for i in range (2,n):
        soma = ant + prox
        
        lista_numeros.append(soma) 
        ant = prox
        #print(ant)
        prox = soma
        
        print(soma, end = ' ')
        #print(prox)
    #print(lista_numeros)

