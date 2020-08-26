# Cria uma lista e substitui um elemento
list_num = [2,5,9,1]
list_num[2] = 3
print(list_num)

# Faz a troca de um elemento do inicio pelo o final usando uma variavel auxiliar
list_num [0] = list_num [3]
aux = list_num[0]
list_num [0] = list_num [3]
list_num [3] = aux
print(list_num)  

lista = [2,5,9,1]
# imprimi o indice e o valor usando a função enumerate
for i,v in enumerate(lista):
    print("indice",i, end = " | ")
    print("valor",v)
print("\n-----------\n")

# faz varredura e imprimi o indice e valor a partir de uma serie
for i in range(0,len(lista)):
    print("indice",i, end = " | ")
    print("valor",lista[i])
print("\n-----------\n")

# faz varredura e imprimi o valor
for valor in lista:
    print("valor",valor)
print("\n-----------\n")

# faz varredura e imprimi o indice
for ind in range (len(lista)):
    print("indice",ind)
print("\n-----------\n")

# adiciona valores com um input
valores2 = list()
for i in range (0,5):
    valores2.append(int(input("digite um valor para adicionar na lista: ")))
print(valores2)

# lista está interligadas
a1 = [2,3,4,7]
b1 = a1
b1[2] = 8
print(f"Lista A: {a1}") 
print(f"Lista B: {b1}") 
print("\n-----------\n")

# lista criando uma cópia
a = [2,3,4,7]
b = a[:]
b[2] = 8
print(f"Lista A: {a}") 
print(f"Lista B: {b}") 
print("\n-----------\n")

# Exercicio 78
lista_ex78 = []
tamanho_lista = int(input("Digite o tamanho da lista: "))
for qtd in range(0,tamanho_lista):
    lista_ex78.append(int(input(f"Digite os valor para a posição {qtd}: ")))
print("Maior elemento da lista: ",max(lista_ex78))
print("Menor elemento da lista: ",min(lista_ex78))    

# Exercicio 79
lista_ex79 = []
decisao_user = "s"
decisao_user.upper()
while (decisao_user == "S"):
    valor = (int(input("Digite um valor:")))
    for i in lista_ex79:
        if (valor != lista_ex79[i]):
            lista_ex79.append(valor)
    decisao_user = input("Deseja continuar: ")
lista_ex79.sort()

# Exercicio 80

# Exercicio 81

# Exercicio 82

# Exercicio 83