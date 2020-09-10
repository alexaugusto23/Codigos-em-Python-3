class Retangulo: 

    def __init__ (self, largura, altura):
        self.__largura = largura 
        self.__altura = altura

    def area(self):
        return self.__largura * self.__altura
    
    def perimetro(self):
        return (self.__largura * self.__altura) * 2
    
    def get_largura(self):
        return self.__largura
    
    def get_altura(self):
        return self.__altura
    
    def set_largura(self, valor):
        self.__largura = valor
    
    def set_altura(self, valor):
        self.__altura = valor

ret1 = Retangulo(5,10)
print(ret1.area())
print(ret1.perimetro())
print('endereco na memoria',ret1)