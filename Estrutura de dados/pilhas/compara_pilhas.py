def compara_pilhas(pilha1, pilha2):
    pilha3 = []
    pilha4 = []
    resultado = 0

    if is_empty(pilha1) and is_empty(pilha2):
        return True
    else: 
        for item in range (len(pilha1)):
            push(pilha3,pop(pilha1))
            print("desempilha pilha 1")
            print(f"Pilha 1: {pilha1}")
            print(f"Pilha 3: {pilha3}")

            print("-"*10)

            push(pilha4,pop(pilha2))
            print("desempilha pilha 2")
            print(f"Pilha 2: {pilha2}")
            print(f"Pilha 4: {pilha4}")

                    
            print("-"*10)
            print("Compara pilhas")
            if pilha3 == pilha4:
                resultado += 1
            
            print("-"*10)

            push(pilha1,pop(pilha3))
            print("Empilhando pilha 1")
            print(f"Pilha 1: {pilha1}")
            print(f"Pilha 3: {pilha3}")

            print("-"*10)

            push(pilha2,pop(pilha4))
            print("desempilha pilha 2")
            print(f"Pilha 2: {pilha2}")
            print(f"Pilha 4: {pilha4}")

            print("-"*10)
            print(f"o valor de resultado é: {resultado}")

    if resultado == len(pilha1) and len(pilha2):
        return True
    else:
        return False

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
    
empilha1 = []
empilha2 = []
empilha1.append(1)
empilha1.append(2)
empilha1.append(3)

empilha2.append(1)
empilha2.append(2)
empilha2.append(3)

print(empilha1,empilha2)
print("-=-"*10)
print('chamando função compara pilhas')
resultado = compara_pilhas(empilha1, empilha2)
print(f"Imprimindo resutado da função {resultado}")
