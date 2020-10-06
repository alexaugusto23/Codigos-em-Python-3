def compara_pilhas(pilha1, pilha2):
    pilha3 = []
    pilha4 = []
    if len(pilha1) == 0 and len(pilha2) ==0:
        return True
    else:
        return False

empilha1 = []
empilha2 = []
empilha1.append(1)
empilha1.append(2)
empilha1.append(3)

empilha2.append(4)
empilha2.append(5)
empilha2.append(6)

print(empilha1,empilha2)
print("-=-"*10)
print('chamando função compara pilhas')
resultado = compara_pilhas(empilha1, empilha2)
print(f"Imprimindo resutado da função {resultado}")
