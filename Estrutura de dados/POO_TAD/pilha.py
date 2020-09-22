# Implementa̧cao de pilha atraves de 
# func̃oes que manipulam uma lista

# Fuņcão is_empty: testa 
# se a pilha est ́a vazia
def is_empty(lista):
    return len(lista) == 0

# Funcão push: empilha um item
def push(lista, item):
    lista.append(item)

# Função pop: desempilha um item
def pop(lista):
    if is_empty(lista):
        raise Exception('Pilha vazia') # o comando raise gera um erro caso o usu ́ario tente desempilhar de uma Pilha vazia.
    return lista.pop()

# Fun ̧cão top: devolve o elemento 
# no topo da pilha se ela não estiver vazia
def top(lista):
    if is_empty(lista):
        raise Exception('Pilha vazia')
    return lista[-1]

listav = [1,5,6,4]
print(top(listav))

listav[len(listav)-1]

item = []
print('Tipo de dado da variavel', type(item))
push(item,'Vitor')
push(item,'Priscila')
push(item,'Fabiola')
print('Desempilhando: ',pop(item))
print('Desempilhando: ',pop(item))







