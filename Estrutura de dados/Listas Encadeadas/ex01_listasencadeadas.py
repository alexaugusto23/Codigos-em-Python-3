class No:
    def __init__(self,dado,prox):
        self.dado = dado.lower()
        self.prox = prox

def percorre_lista_enc(cabeca):
    no_atual = cabeca
    while no_atual != None:
        print(no_atual.dado)
        no_atual = no_atual.prox

def existe_item(cabeca, item):
    item.lower()
    no_atual = cabeca
    while no_atual != None:
        if no_atual.dado == item:
            return True
        no_atual = no_atual.prox
    return False

def existe_item_dois(cabeca, item):
    existe = False
    no_atual = cabeca
    while no_atual != None:
        if no_atual.dado == item:
            existe = True
            break
            return True
        no_atual = no_atual.prox
    return False

cabeca = None # Inicializa o nó cabeça da lista
ultimo = None # Inicializa um apontador auxiliar para o último nó da lista

cabeca = No("João",None)
ultimo = cabeca

novo_no = No("Pedro",None)
ultimo.prox = novo_no
ultimo = novo_no

novo_no = No("Maria",None)
ultimo.prox = novo_no
ultimo = novo_no

novo_no = No("Bia",None)
ultimo.prox = novo_no
ultimo = novo_no

novo_no = No("Jose",None)
ultimo.prox = novo_no
ultimo = novo_no

novo_no = No("Thiago",None)
ultimo.prox = novo_no
ultimo = novo_no

novo_no = No("Isabel",None)
ultimo.prox = novo_no
ultimo = novo_no

novo_no = No("Andre",None)
novo_no.prox = cabeca
cabeca = novo_no

novo_no = None

nome = input('Informe o nome que deseja procurar:')
resultado = existe_item(cabeca, nome)
print(f"O nome exite na lista: {resultado}")

