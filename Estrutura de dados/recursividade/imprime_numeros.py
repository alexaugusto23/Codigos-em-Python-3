def imprime_numeros(n):
    if n == 1:
        print(n)
    else:
        print(n)
        imprime_numeros(n-1)

def imprime_numeros_pares(n):
    if n <= 1:
        print(n)
    else:
        print(n)
        imprime_numeros(n-2)

print(imprime_numeros(10))
print("x"*30)
print(imprime_numeros_pares(10))