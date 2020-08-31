# Exercicio 79
lista79 = []
decisao_user = False
while (decisao_user != "N"):
    valor = int(input("Digite um valor:"))
    if valor not in lista79:
        lista79.append(valor)
    else:
        print("Valor duplicado!, não adicionado.")
    decisao_user = str(input("Deseja continuar? [S/N]: ")).upper()
lista79.sort()
print("\n")
print("=-"*30)
print("\nLista",lista79)

# Exercicio 79 Resolvido
numeros = list()
while True:
    n = int(input("Digite um valor:"))
    if (n not in numeros):
        numeros.append(n)
        print("Valor adcioando")
    else:
        print("Valor duplicado")
    r = str("input(Deseja continuar? [S/N]:"))
    if (r in 'Nn'):
        break
numeros.sort()
print("\n")
print("=-"*30)
print("\nLista",numeros)