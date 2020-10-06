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
