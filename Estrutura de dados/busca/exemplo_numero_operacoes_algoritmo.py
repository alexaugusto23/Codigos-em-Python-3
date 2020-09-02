def soma_lista(lista):
	soma = 0  # 1 atribuição
	i = 0  # 1 atribuição
	while i < len(lista): # n+1 comparações
		soma += lista[i] # n atribuições/op. aritméticas
		i += 1 # n atribuições/op. aritméticas
	return soma

# Vamos considerar n = len(lista)

# Total op. aritméticas: 2*n
# Total comparações lógicas: n+1
# Total de atribuições: 2*n + 2

# Conclusão: o algoritmo tem complexidade O(n)
