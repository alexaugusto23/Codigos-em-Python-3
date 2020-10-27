def soma_pares_melhorada(num):
    soma = 0
    if num % 2 == 0:
        soma += num
    if num == 0:
        return 0
    else:
        return soma + soma_pares_melhorada(num - 1) 


resultado = soma_pares_melhorada(3)
print(f"O somatorio é: {resultado}")