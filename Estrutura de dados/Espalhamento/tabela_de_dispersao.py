class TabelaDispersao:
    
    def __init__(self, tamanho_tabela):
        self.tamanho_tabela = tamanho_tabela
        self.tabela = [None] * tamanho_tabela

    def hash_int(self, item):
        return item % self.tamanho_tabela

    def hash_string(self, item):
        soma = 0
        for pos in range(len(item)):
            soma = soma + (ord(item[pos]) * (pos+1))
        return soma % self.tamanho_tabela

    def hash(self, item):
        if type(item) is int:
            posicao = self.hash_int(item)
        else:
            posicao = self.hash_string(str(item))
        return posicao
    
    def adicionar(self, item):
        posicao = self.hash(item)
        if self.tabela[posicao] is None:  # verifica se o slot é None
            self.tabela[posicao] = [item]
        else:
            self.tabela[posicao].append(item)

    def remover(self, item):
        posicao = self.hash(item)
        if self.tabela[posicao] is not None:  # se o slot não é None, então ele é uma lista (encadeamento)
            for i in range(len(self.tabela[posicao])):  # percorre a lista do slot para remover o item, se ele existir
                if item == self.tabela[posicao][i]:
                    self.tabela[posicao].pop(i)  # remove o item da lista daquele slot específico
                    break
            if len(self.tabela[posicao]) == 0:  # se a lista ficar vazia, mudamos o valor do slot para None
                self.tabela[posicao] = None


    def buscar(self, item):
        posicao = self.hash(item)
        if self.tabela[posicao] is not None:   # se o slot não é None, então ele é uma lista (encadeamento)
            for i in range(len(self.tabela[posicao])):  # percorre a lista do slot para procurar o item, se ele existir
                if item == self.tabela[posicao][i]:
                    return True
        return False


    def fator_de_carga(self):
        count = 0
        for i in range (0, len(self.tabela)):
            if len(self.tabela[i]) >1:
                for j in range (0, len(self.tabela[i])):
                    #print(self.tabela[i][j])
                    if self.tabela[i][j] != None:
                        count += 1
                else:
                    break
        for i in range (1, len(self.tabela)):
            #print(i)
            if self.tabela[i] != None:
                count += 1

        #print("Final do contador",count)
        #print(self.tamanho_tabela)

        resultado = count/self.tamanho_tabela

        return resultado

    def eh_primo(self,numero):
        divisores = 0
        for div in range(1,numero+1):
            if numero % div == 0:
                divisores += 1 
            if divisores == 2:
                return True
        return False

    def redimensionar(self,novo_tamanho, tamanho_primo):
        pass




# Programa principal
tabela = TabelaDispersao(11)
tabela.adicionar(11)
tabela.adicionar(22)
tabela.adicionar(10)
tabela.adicionar(29)
tabela.adicionar('gato')

print("-="*10)
print("tabela")
print(tabela.tabela)
print("-="*10)
print("\n")


print("-="*10)
print("fator de carga")
red = tabela.fator_de_carga()
print(red)
print("-="*10)
print("\n")

print("-="*10)
print("he primo")
print(tabela.eh_primo(11))
print("-="*10)
print("\n")

print("-="*10)
print("redimensionar")
print(tabela.redimensionar(14, tabela.eh_primo(tabela.tamanho_tabela)))
print("-="*10)
print("\n")

print("-="*10)
print("tabela_redimensionada")
print(tabela.tabela)
print("-="*10)
print("\n")

'''
print('Existe toga?', tabela.buscar('toga'))
print('Existe gato?', tabela.buscar('gato'))
print('Existe 44?', tabela.buscar(44))
print('Existe 54?', tabela.buscar(54))
print('Existe 3.4?', tabela.buscar(3.4))
'''