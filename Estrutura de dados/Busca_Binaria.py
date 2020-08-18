# Busca Binária

def busca_indice(lista, alvo):
    for item in lista:
        if item == alvo:
            return True
    return False

# Testando a busca
numeros = [5, 11 ,13 ,33 ,61, 73 ,79 ,80 ,85]
print(busca_indice(numeros,5))
print(busca_indice(numeros,85))
print(busca_indice(numeros,7))

print("-------------------------")

def busca_indice(lista, alvo):
    for i in range(0, len(lista)):
        if lista[i] == alvo:
            return i
    return -1

# Testando a busca
numeros = [5, 11 ,13 ,33 ,61, 73 ,79 ,80 ,85]
print(busca_indice(numeros,5))
print(busca_indice(numeros,85))
print(busca_indice(numeros,7))
