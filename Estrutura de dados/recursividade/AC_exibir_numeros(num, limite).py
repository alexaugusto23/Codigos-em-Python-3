def exibir_numeros(num, limite):
    if num == (limite + 1):
        return 1
    else:
        print(num)
        return exibir_numeros(num + 1, limite) 



resultado = exibir_numeros(1, 10)
print(f"range {resultado}")

'''
-4
5

-4
-3
-2
-1
0
1
2
3
4
5

1
10

1
2
3
4
5
6
7
8
9
10
'''