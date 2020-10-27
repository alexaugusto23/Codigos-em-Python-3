def soma_pares(num):
    soma = 0
    if num % 2 == 0:
        soma += num
    if num == 0:
        return 0
    else:
        return soma + soma_pares(num - 1) 