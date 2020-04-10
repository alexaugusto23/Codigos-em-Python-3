class Proprietario:
    __data_nasc = None

    def __init__(self,nome,cpf,rg,endereco):
        self.nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.endereco = endereco

class Endereco:
    bairro = None
    cidade = None
    estado = None
    __complemento = None

    def __init__(self, rua, cep):
        self.__rua = rua
        self.__cep = cep
    
    def set_complemento(self,complemento):
        self.__complemento = complemento
    
    def get_rua(self):
        return self.__rua
    
    def get_cep(self):
        return self.__cep
    
    def get_complemento(self):
        return self.__complemento

end = Endereco("rua 01", 12356)
pro1 = Proprietario("Alex",36059729851, 44950273,end)

a=input()

print(pro1.nome)
print(pro1.endereco.get_rua())
print(pro1.endereco.get_cep())
pro1.endereco.set_complemento(a)
print(pro1.endereco.get_complemento())