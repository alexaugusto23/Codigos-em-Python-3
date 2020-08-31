# Alexsandro Augusto Ignacio RA 1901705


class Aluno:
    def __init__(self, amostra):
        lista = []
        for l in amostra:
            lista.append(l.strip())
        self.nome = str(lista[0])
        self.ra = int(lista[1])
        x = lista[2:7]
        notas_ac = []
        for atividades in x:
            notas_ac.append(float(atividades))
        self.nota_ac = notas_ac
        self.nota_prova = float(lista[7])
        self.faltas = int(lista[8])
        self.media = 6.0
        self.aprovado = None

    def calcular_aprovacao(self):

        menor = min(self.nota_ac)
        maior = []
        remover = False
        for valor in self.nota_ac:
            if valor != menor or remover:
                maior.append(valor)
            else:
                retirar = True
        atividades = sum(maior) / len(maior)
        mf = ((atividades * 0.5) + (self.nota_prova * 0.5))
        self.frequencia = (60 - self.faltas) / 60 * 100
        if (mf >= 6 and self.frequencia >= 75):
           self.media = mf
           self.aprovado = 'Aprovado'
        else:
            self.aprovado = "Reprovado"
            self.media = mf
        return self.aprovado, self.media

    def escrever_situacao(self, situacao):
        escreve = open('situacao.txt', 'w')
        escreve.write(str(self.ra) + ': ' + self.nome + '\n')
        escreve.write(str(f'{self.media:.1f}') + '\n')
        escreve.write(str(f'{self.frequencia:.1f}') + '%' + '\n')
        escreve.write(str(self.aprovado))


arquivo = open('entrada.txt', 'r')
aluno = Aluno(arquivo)
situacao = aluno.calcular_aprovacao()
aluno.escrever_situacao(situacao)

gravacao = open('situacao.txt', 'r')
armazena_grava = gravacao.read()
print(armazena_grava)
arquivo.close()
gravacao.close