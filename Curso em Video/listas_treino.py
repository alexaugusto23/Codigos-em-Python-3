def compara_pilhas(pilha1, pilha2):
    pilha3 = []
    pilha4 = []
    resultado = 0
    resposta = None

    if is_empty(pilha1) and is_empty(pilha2):
        return True
    else: 
        for item in range (len(pilha1)):
            push(pilha3,pop(pilha1))
            push(pilha4,pop(pilha2))

            if pilha3 == pilha4:
                resultado += 1

        
        for item in range (len(pilha3)):
            push(pilha1,pop(pilha3))
            push(pilha2,pop(pilha4))

    if resultado == len(pilha1) and len(pilha2):
        return True
    else:
        return False

def is_empty(lista):
    return len(lista) == 0

def push(lista, item):
    lista.append(item)

def pop(lista):
    return lista.pop()

def top(lista):
    return lista[-1]