def soma_numeros(n):
    if n == 1: # caso trivial a soma de 1 até 1 é igual a 1
        return 1
    else:
        return n + soma_numeros(n-1) # passo chave de recursão

resultado = soma_numeros(5)
print(f"O somatorio é: {resultado}")