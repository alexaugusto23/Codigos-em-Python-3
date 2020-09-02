import math

inicio = int(input('Número inicial: '))
fim = int(input('Número final: '))
if fim > inicio:
	input('Opa! Tenho um desafio para você: pense num número secreto entre %d e %d. Pensou?' % (inicio, fim))
	qtd_numeros = (fim - inicio) + 1
	max_tentativas = math.ceil(math.log(qtd_numeros, 2))
	input('Vou advinhar o número secreto em no máximo %d tentativas. Duvida de mim?' % max_tentativas)
	tentativas = 0
	acabou = False
	while not acabou:
		meio = (inicio + fim) // 2
		tentativas += 1
		opcao = input(' %da tentativa: o número secreto é maior (>), menor (<) ou igual(=) a %d? ' % (tentativas, meio))
		if opcao == '>':
			inicio = meio + 1
		elif opcao == '<':
			fim = meio - 1
		else:
			acabou = True
	print('Eu sabia! O número secreto é %d !!! E advinhei após %d tentativas.' % (meio, tentativas))