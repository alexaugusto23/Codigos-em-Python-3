class Funcionario:
    __matricula = None
    __nome = None
    __salario = None

    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    def get_matricula(self):
        return self.__matricula
    
    def set_matricula(self,matricula):
        self.__matricula = matricula
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        self.__nome = nome
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self,salario):
        self.__salario = salario

    

