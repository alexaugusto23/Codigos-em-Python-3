'''
Questão 1 (F ́acil): Escreva uma funcao que exiba todos os elementos de uma
pilha.

Questão 2 (F ́acil) : Escrever um programa que insere elementos em uma Pilha A.
Apos isso, transfere todos os seus dados para outra pilha B.

Questão 3 (F ́acil): Escrever uma funcao que receba como parˆametro uma pilha.
A funçao deve retornar a m ́edia aritm ́etica dos elementos da pilha.

Questão 4: (F ́acil): Escrever uma fun ̧c ̃ao que receba como parˆametro uma pilha.
A funcao deve retornar o maior elemento da pilha.

Questão 5 (M ́edio): Construa um programa utilizando um pilha que resolva o
seguinte problema:
    
    Armazene as placas dos carros (apenas os n ́umeros) que est ̃ao estacionados
num rua sem sa ́ıda estreita.
    Dada uma placa verifique se o carro est ́a estacionado na rua. Caso esteja,
informe a seq ̈uˆencia de carros que dever ́a ser retirada para que o carro em
quest ̃ao consiga sair.

Questão 6 (F ́acil): Dada uma sequˆencia contendo n n ́umeros reais (onde n > 0),
imprimi-la na ordem inversa.

Questão 7 (F ́acil): Escreva uma fun ̧c ̃ao que preencha uma pilha passada como
parˆametro com os elementos de um vetor passado como parˆametro.

Questão 8 (M ́edio): Escreva uma fun ̧c ̃ao chamada imprime pares restantes(pilha,
lista) recebe uma pilha e uma lista de inteiros. Para cada um desses n ́umeros
(utilizando uma estrutura de repeti ̧c ̃ao), fa ̧ca como segue:
    se o n ́umero for par, insira-o na pilha.
    se o n ́umero for  ́ımpar, retire um n ́umero da pilha (sem imprimi-lo).
    Ao final, esvazie a pilha imprimindo os elementos (use uma estrutura de
repeti ̧c ̃ao para isso!).

Questão 9 (M ́edio): Escreva uma fun ̧c ̃ao chamada desempilha se zero(p1, p2,
numeros) que recebe como parˆametro 2 pilhas (p1 e p2) e uma lista de inteiros
(numeros). Para cada um desses n ́umeros, fa ̧ca:
    se positivo, inserir na pilha p1.
    se negativo, inserir na pilha p2.
    se zero, retirar e imprimir um elemento de cada pilha, se cada uma delas n ̃ao
estiver vazia. Se uma delas estiver vazia, imprima ’Vazia’ no lugar.

Questão 10 (F ́acil): Escreva uma fun ̧c ̃ao que receba como parˆametro duas pilhas
e verifique de elas s ̃ao iguais. Duas pilhas s ̃ao iguais se possuem os mesmos
elementos, na mesma ordem.

Questão 11 (F ́acil): Construa um programa que leia 10 valores e empilhe-os
conforme forem pares ou  ́ımpares na pilha1 ou pilha2, respectivamente. No final
desempilhe os valores de cada pilha mostrando-os na tela.

Questão 12 (Dif ́ıcil): Escreva uma fun ̧c ̃ao que receba um n ́umero inteiro e
positivo representando um n ́umero decimal, determine o seu equivalente bin ́ario.
Utilize uma pilha no processo e convers ̃ao.
    Exemplo: Dado o n ́umero decimal 18, a sa ́ıda da fun ̧c ̃ao dever ́a ser 10010.

Questão 13 (M ́edio): Escreva uma fun ̧c ̃ao que recebe uma string e utilizando
uma pilha inverte as letras de cada palavra da String preservando a ordem das
palavras. Note que sempre a String  ́e finalizada por ponto,
    Exemplo: ESTE EXERC ́ICIO E MUITO F  ́ ACIL.  ́
    Exemplo da sa ́ıda: ETSE OIC ́ICREXE E OTIUM LIC  ́ AF.  ́

Questão 14 (F ́acil): Uma palavra  ́e pal ́ındromo se a sequˆencia de caracteres que
a constitui  ́e a mesma quer seja lida da esquerda para a direita ou da direita para
a esquerda. Por exemplo, as palavras RADAR, OSSO e MIRIM s ̃ao pal ́ındromos.
Utilizando uma pilha, escreva uma fun ̧c ̃ao para reconhecer se uma dada palavra  ́e
pal ́ındromo.

Questão 15  - Desafio (Difícil): Suponha que queremos decidir se uma dada sequência de
parˆenteses e colchetes est ́a bem formada. Por exemplo:
B ( ( ) [ ( ) ] ) est ́a bem formada.
B ( [ ) ] n ̃ao est ́a bem formada.
B ( ( ( ) ) n ̃ao est ́a bem formada.
E possível resolver esse problema utilizando pilhas.  ́
Pede-se: implemente uma fun ̧c ̃ao para resolvˆe-lo.

'''

# EX 15
class Pilha:
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('Pilha vazia')
        return self.items.pop()

    def top(self):
        if self.is_empty():
            raise Exception('Pilha vazia')
        return self.items[-1]

    def __len__(self):
        return len(self.items)

# Função que verifica se a expressão está bem formada:
def verifica_expressao(expressao):
    bem_formada = True
    pilha = Pilha()
    for c in expressao:
        if c == '(' or c == '[':
            pilha.push(c)
        else: # ou seja, se encontrar um ) ou ]
            if pilha.is_empty():
                bem_formada = False
            else:
                item = pilha.pop()
                if c == ')' and item != '(':
                    bem_formada = False
                elif c == ']' and item != '[':
                    bem_formada = False
    if not pilha.is_empty():
        bem_formada = False
    return bem_formada

# Programa principal:
expressao = input('Informe a expressao: ')
resultado = verifica_expressao(expressao)
if resultado:
    print('A expressão está bem formada!')
else:
    print('A expressão está mal formada!')