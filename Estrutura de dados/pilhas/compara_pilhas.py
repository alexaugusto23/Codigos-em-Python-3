def compara_pilhas(pilha1, pilha2):

    pilha3 = []
    pilha4 = []
    resultado = 0
    tam_p1 = len(pilha1)
    tam_p2 = len(pilha2)

    if pilha1.is_empty() and pilha2.is_empty():
        return True
    elif len(pilha1) != len(pilha2):
        return False
    else: 
        for i in range(tam_p1):
            #print(pilha1.getval(),pilha2.getval())
            item1 = pilha1.pop()
            item2 = pilha2.pop()
            if item1 == item2:
                resultado += 1
            pilha3.append(item1)
            pilha4.append(item2)
        #print(pilha1.getval(),pilha2.getval())
        #print(resultado)
        #print(pilha3)
        #print(pilha4)

        for i in range(len(pilha3)):
            item1 = pilha3.pop()
            item2 = pilha4.pop()

            pilha1.push(item1)
            pilha2.push(item2)
        #print("2 for")
        #print(pilha1.getval(),pilha2.getval())
        #print(pilha3)
        #print(pilha4)

        if resultado == tam_p1 and tam_p2:
            return True
        return False


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

    def getval(self):
        return self.items

empilha1 = Pilha()
empilha2 = Pilha()
empilha1.push(1)
empilha1.push(2)
empilha1.push(3)

empilha2.push(1)
empilha2.push(2)
empilha2.push(3)

#print(empilha1,empilha2)
#print("-=-"*10)
print('chamando função compara pilhas')
resultado = compara_pilhas(empilha1, empilha2)
print(f"Imprimindo resutado da função {resultado}")


