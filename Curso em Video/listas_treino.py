'''
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
lista_01 = []
for i in range (0,5):
    lista_01.append(int(input("digite um valor para adicionar na lista: ")))
print(lista_01)

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

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Ana',20],['Maria',45]]
print(galera[0][1])

for p in galera:
    print(f" {p[0]} tem tantos anos de idade {p[1]}")
'''

galera = list()
dado = list()
totmai = 0
totmen = 0
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade")
        totmen += 1

print(f"Temos {totmai} meiores e {totmen} menors de idade")

print(galera)
print(dado)