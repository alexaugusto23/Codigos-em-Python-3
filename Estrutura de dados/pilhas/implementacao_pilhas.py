# Função is_empty: testa se a pilha est́a vazia
def is_empty(lista):
    return len(lista) == 0

# Função push: empilha um item
def push(lista, item):
    lista.append(item)

# Função pop: desempilha um item
def pop(lista):
    if is_empty(lista):
        raise Exception('Pilha vazia') # o comando raise gera um erro caso o usu ́ario tente desempilhar de uma Pilha vazia.
    return lista.pop()

# Função top: devolve o elemento no topo da pilha se ela não estiver vazia
def top(lista):
    if is_empty(lista):
        raise Exception('Pilha vazia')
    return lista[-1]


items = [] # Cria uma lista vazia. As fun ̧c~oes v~ao manipular essa lista como uma pilha.
push(items, 1) # empilha o item 1
push(items, 2) # empilha o item 2
push(items, 3) # empilha o item 3
push(items, 4) # empilha o item 4
print('Pilha vazia?', is_empty(items)) # Testa se a pilha est ́a vazia (False)
print('Topo:', top(items)) # Mostra o elemento no topo da lista (n ́umero 4)
print(pop(items)) # Desempilha e imprime (n ́umero 4)
print(pop(items)) # Desempilha e imprime (n ́umero 3)
print(pop(items)) # Desempilha e imprime (n ́umero 2)
print(pop(items)) # Desempilha e imprime (n ́umero 1)
print('Pilha vazia?', is_empty(items)) # Testa se a pilha est ́a vazia (True)
