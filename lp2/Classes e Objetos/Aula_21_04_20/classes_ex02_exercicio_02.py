class Produto:
    
    def __init__ (self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def get_descricao(self):
        return self.descricao
    
    def exibir(self):
        print("Nome: ", self.nome) 
        print("Preço:", self.preco)
        print("Descrição: ", self.descricao)

class Mouse(Produto):
    
    def __init__(self, nome, preco, descricao, tipo):
        super().__init__(nome, preco, descricao)
        self.tipo = tipo
    
    def get_descricao(self):
        return self.descricao + self.tipo
    
    def exibir(self):
        super().exibir()
        print("Tipo: ", self.tipo)


class Livro(Produto):
    
    def __init__(self, nome, preco, descricao, autor):
        super().__init__(nome, preco, descricao)
        self.autor = autor
    
    def get_descricao(self):
        return self.descricao + self.autor 
    
    def exibir(self):
        super().exibir()
        print("Autor: ", self.autor)

livro = Livro("Dragons",15.90,"Aventura","Alex")
mouse = Mouse("Supermouse",45,"Ergonomico","direito")

livro.exibir()
print("\n")
mouse.exibir()
print("\n--------")

carrihno = [livro,mouse]
carrinho.get_descricao()
