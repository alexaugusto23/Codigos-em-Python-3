# Ordenação pelo método da bolha ou bubble sort (otimizada)

def ordenacao_bolha(lista):
    houveTroca = True # inicializa a flag para for ̧car a primeira execu ̧c~ao do while
    i = 0
    while i < len(lista) and houveTroca:
        houveTroca = False # marca a flag como falsa, pois se n~ao houve troca a lista estar ́a ordenada
        for j in range(1, len(lista)-i):
            if lista[j-1] > lista[j]:
                temp = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = temp
                houveTroca = True # se houve troca, a flag  ́e marcada como verdadeira e o while ser ́a executado mais uma vez
    i += 1


    return lista

lista1 = [5,6,3,78,84,54]
resultado = ordenacao_bolha(lista1)
print(resultado)