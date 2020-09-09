class Retangulo: 

    def __init__ (self, comprimento, altura):
        self.__comprimento = comprimento 
        self.__altura = altura

    def area(self):
        return self.__comprimento * self.__altura
    
    def perimetro(self):
        return (self.__comprimento * self.__altura) * 2
    
    def get_comprimento(self):
        return self.__comprimento
    
    def get_altura(self):
        return self.__altura
    
    def set_comprimento(self, valor):
            return self.__comprimento = valor
    
    def set_altura(self, valor):
        return self.__altura = valor

ret1 = Retangulo(5,10)
print(ret1.area())
print(ret1.perimetro())
print('endereco na memoria',ret1)