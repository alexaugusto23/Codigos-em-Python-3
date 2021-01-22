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
        if self.tabela[posicao] is None: 
            self.tabela[posicao] = [item]
        else:
            self.tabela[posicao].append(item)

    def remover(self, item):
        posicao = self.hash(item)
        if self.tabela[posicao] is not None:  
            for i in range(len(self.tabela[posicao])):  
                if item == self.tabela[posicao][i]:
                    self.tabela[posicao].pop(i)  
                    break
            if len(self.tabela[posicao]) == 0: 
                self.tabela[posicao] = None


    def buscar(self, item):
        posicao = self.hash(item)
        if self.tabela[posicao] is not None:
            for i in range(len(self.tabela[posicao])): 
                if item == self.tabela[posicao][i]:
                    return True
        return False


    def fator_de_carga(self):
        count = 0 
        for i in range(len(self.tabela)):
            if self.tabela[i] is not None:
                for x in range(len(self.tabela[i])):
                    count += 1
        return count / self.tamanho_tabela

        


    def eh_primo(self, numero):
        divisores = 0
        for div in range(1, numero+1):
            if numero % div == 0:
                divisores += 1
        if divisores == 2:
            return True
        return False


    def redimensionar(self, novo_tamanho, tamanho_primo):
        count = novo_tamanho
        primobolean = self.eh_primo(count)
        tabela_antiga =[]
        tb_alterada = []

        for i in range(len(self.tabela)):
            if self.tabela[i] is not None:
                tabela_antiga.append(self.tabela[i])

        for x in tabela_antiga:
            tb_alterada.extend(x)
            
        if tamanho_primo == True:
            while primobolean == False:
                count += 1
                primobolean = self.eh_primo(count)

            self.tamanho_tabela = count
            self.tabela = [None] * count
            for i in range(len(tb_alterada)):
                self.adicionar(tb_alterada[i])
        else:
            self.tamanho_tabela = count
            self.tabela = [None] * count
            for i in range(len(tb_alterada)):
                self.adicionar(tb_alterada[i])  