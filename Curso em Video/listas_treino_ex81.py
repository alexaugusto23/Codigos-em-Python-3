# Exercicio 81
lista = []
while (True):
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        resp = str(input("Quer continuar ? [S/N]: ")).upper()
        if resp == 'N':
            break
    else:
        print(f"\nO elementos {n} não foi adicionado porque está duplicado\n")
        resp = str(input("Quer continuar ? [S/N]: ")).upper()
        if resp == 'N':
            break

print("Ordem em que os elementos foram digitados: ",lista)
lista.sort(reverse=True)
print("Ordem em que os elementos foram digitados: ",lista)
print(f"Foi digitado {len(lista)} elementos na lista")
if 5 in lista: 
    print("O valor 5 está dentro da lista")
else:
    print("O valor 5 não está dentro da lista")



'''    
    indice = 0
    maior
for i in range (0,len(lista)-1):
    if lista[i] > lista[i+1]:
        maior = 
        lista[i] = 
'''

#