class Produto:
    def __init__ (self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao



class Mouse:
    def __init__(self, nome, preco, descricao):
        super().__init(nome, preco, descricao)

class Livro: 