# Exercicio 78
lista_ex78 = []
tamanho_lista = int(input("Digite o tamanho da lista: "))
for qtd in range(0,tamanho_lista):
    lista_ex78.append(int(input(f"Digite os valor para a posição {qtd}: ")))
print("=-"*30)
print("Os valores digitados foram: ",lista_ex78)
print("Maior elemento da lista: ",max(lista_ex78))
print("Menor elemento da lista: ",min(lista_ex78))    
'''
"""
# Exercicio 78 resolvido
tamanho_lista_2 = int(input("Digite o tamanho da lista: "))
menor = 0
maior = 0
lista_exec_78 = []
for qtd in range(0,tamanho_lista_2):
    lista_exec_78.append(int(input(f"Digite os valor para a posição {qtd}: ")))
    if (qtd == 0):
        maior = menor =  lista_exec_78[qtd]
    else:
        if (lista_exec_78 [qtd] > maior):
            maior = lista_exec_78[qtd]
        if (lista_exec_78[qtd] < menor):
            menor = lista_exec_78[qtd]

print("=-"*30)
print("Os valores digitados foram: ",lista_exec_78)
print("Maior elemento da lista: ",maior)
print("Menor elemento da lista: ",menor)  
"""