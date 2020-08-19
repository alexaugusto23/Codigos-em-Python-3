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

print("-------------------------")

def soma_lista(lista):
    soma = 0
    i = 0
    while i < len(lista):
        soma += lista[i]
        i += 1
    return soma

print("-------------------------")

def maior_linha(matriz):
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    linha_maior_soma = 0
    i = 0
    while i < n_linhas:
        soma_atual = 0
        j = 0
        while j < n_colunas:
            soma_atual += matriz[i][j]
            j += 1
        if soma_atual > linha_maior_soma or i == 0:
            linha_maior_soma = soma_atual
            i += 1
    return linha_maior_soma