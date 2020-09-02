import time
import random

def lista_telefonica_aleatoria(tamanho):
	dicionario = {}
	random.seed(0) # gera sempre a mesma lista
	while len(dicionario) < tamanho:
		novo_numero = str(random.randint(20000000, 99999999))
		novo_numero = '{0}-{1}'.format(novo_numero[0:4], novo_numero[4:8])
		if novo_numero not in dicionario:
			dicionario[novo_numero] = None
	return sorted(dicionario.keys())

def busca_sequencial(lista, x):
	i = 0
	while i < len(lista):
		if lista[i] == x:
			return i
		i += 1
	return -1

def busca_binaria(lista, x):
	inicio = 0
	fim = len(lista)-1
	while inicio <= fim:
		meio = (inicio + fim) // 2
		if x == lista[meio]:
			return meio
		elif x > lista[meio]:
			inicio = meio + 1
		else:
			fim = meio - 1
	return -1

# Programa principal:
tamanho_da_lista = int(input('Informe o tamanho da lista: '))
print('Criando a lista...', end='', flush=True)
lista = lista_telefonica_aleatoria(tamanho_da_lista)
print('OK')
print('Dicas de números para procurar: %s, %s, %s, %s, %s' % (lista[0], 
	lista[tamanho_da_lista//4], lista[tamanho_da_lista//2], lista[int(tamanho_da_lista//1.33333333)], lista[-1]))
telefone = input('\nInforme o # de telefone que deseja procurar: ')
while telefone != '0':
	t0_sequencial = time.time()
	posicao_sequencial = busca_sequencial(lista, telefone)
	t_total_sequencial = (time.time() - t0_sequencial) * 1000

	t0_binaria = time.time()
	posicao_binaria = busca_binaria(lista, telefone)
	t_total_binaria = (time.time() - t0_binaria) * 1000

	print('Resultados:')
	print('Busca sequencial: total %.4fms,  índice %d' % (t_total_sequencial, posicao_sequencial))
	print('Busca binaria: total %.4fms,  índice %d' % (t_total_binaria, posicao_binaria))
	razao = t_total_sequencial/t_total_binaria
	print('Razao busca_sequencial/busca_binaria: %.1fx.' % razao)

	telefone = input('\nInforme o # de telefone que deseja procurar: ')



