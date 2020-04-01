'''
Uma classe que permite cadastrar pessoas
- Atributos: nome, email e telefone. 
- Métodos: Um método deve exibir o cartão de visita desta pessoa. 
- Criar construtor
'''


class Pessoa:
    tel_trabalho = None

    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def cartao(self):
        print("Nome: " + self.nome)
        print("E-mail: " + self.email)
        print("Telefone: " + self.telefone)


paulo = Pessoa("Paulo", "paulo@email.com", "9999999")
paulo.cartao()

mari = Pessoa("Mariana", "mari@email.com.br", "8999999")
mari.cartao()