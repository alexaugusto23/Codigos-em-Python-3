'''
Questao 2: Implemente o TAD Retangulo:
    B1 - Facil) Implemente os dados/atributos da classe: armazene as coordenadas
    x e y do canto superior esquerdo, a largura e a altura, conforme a figura
    abaixo.
    B2 - Facil) Implemente o metodo area() que calcula a  ́area do retˆangulo.
    B3 - Facil) Implemente o metodo perimetro() que calcula o perımetro (a soma
    dos quatro lados) do retˆangulo.
    B4 - Médio) Implemente o método interseccao() que recebe um parâmetro r
    com outra instãncia da classe Retangulo e verifica se os retângulos se
    intersectam.

'''

class Retangulo: 

    def __init__ (self, x =0 , y = 0, largura = 0,  altura = 0):
        self.__largura = largura 
        self.__altura = altura
        self.__x = float(x)
        self.__y = float(y) 

    def area(self):
        return self.__largura * self.__altura
    
    def perimetro(self):
        return (self.__largura + self.__altura) * 2
    
    def interseccao(self, r):
        if (self.__x == r.__x or self.__y == r.__y):
            return f"\nRetangulo 1 está em intersecção com Retangulo 2: \nposição:|{self.__x},{self.__y}| |{r.__x},{r.__y}|"
        else:
            return f"\nOs retangulos não tem intersecção: \nposição:|{self.__x},{self.__y}| |{r.__x},{r.__y}|\n"
    
    def get_largura(self):
        return self.__largura
    
    def get_altura(self):
        return self.__altura
    
    def set_largura(self, valor):
        self.__largura = valor
    
    def set_altura(self, valor):
        self.__altura = valor

cord_r_1 = Retangulo(0,1,5,10)
cord_r_2 = Retangulo(1,2,5,10)

#print(cord_r_1.area())
#print(cord_r_1.perimetro())
#print('endereco na memoria',cord_r_1)
print(cord_r_1.interseccao(cord_r_2))