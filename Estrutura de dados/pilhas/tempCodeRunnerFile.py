def compara_pilhas(pilha1, pilha2):
    pilha3 = []
    pilha4 = []
    resposta = 0
    for i in range(len(pilha1)):
        #print(i)
        pilha3.append(pilha1[i])
    print(pilha3)
    for i in range(len(pilha2)):
        #print(i)
        pilha4.append(pilha2[i])
    print(pilha4)
    
    if len(pilha1) == 0 and len(pilha2) ==0:
        return True
    else:
        for item in range(len(pilha1)):
            if pilha1[item] == pilha2 [item]:
                resposta +=1
        if resposta == len(pilha1) and len(pilha2):
            return True
        else:
            return False