'''
class nome_da_classe:
    #atributos
    #metodos
-------------------------------------
class Cachorro:
    nome = None  # atributo
    idade = None
    pesso = None

    def latir (self): # metodos
        ...
    
    def pegar_bola (self): # metodos
        ...
-------------------------------------

instanciar = Classes()

meu_cachorro = Cachorro() #cria objeto

meu_cachorro.nome = 'Rex' #acessa o atributo da classe
meu_cachorro.peso = 8.0
meu_cachorro.idade = 5

-------------------------------------

Construtor

def __init__ (self,parametros):
    ...

class Cachorro:
    def __init__ (self,nome):
        self.nome = nome

meu_cachorro = Cachorro() # ERRO!
meu_cachorro = Cachorro("REX") # OK!,

-------------------------------------

Exemplo

class ContaBancaria:
    numero = None # Atributos
    saldo = 0
    def __init__ (self, numero): # Construtor
        self.numero = numero
    def creditar(self, valor): # Demais Métodos
        self.saldo += valor
        self.saldo = self.saldo + valor
    def debitar(self, valor):
        self.saldo -= valor
    def consultar_saldo(self):
        return self.saldo

conta1 = ContaBancaria(1234)
conta1.creditar(200.0)
conta1.debitar(50.0)
saldo_atual = conta1.consultar_saldo()
print(saldo_atual)

-------------------------------------

'''

class Cachorro:
    # atributo
    nome = None  
    pesso = None
    idade = None
    cor = None
    
    # metodos
    def __init__ (self, nome):
        print('Criação do Objeto')
        self.nome = nome 
        ...
    
    # metodos
    def pegar_bola (self): 
        ...