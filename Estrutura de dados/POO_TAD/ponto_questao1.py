'''
Questao 1: Faça as seguintes modificações na classe Ponto:

B1 - F ́acil) Modifique o construtor para que as coordenadas x e y sejam
opcionais. Caso nenhum valor seja passado como parâmetro, o construtor
deve iniciar as coordenadas x e y com valor zero (Dica: parâmetros default).

B2 - Facil) Implemente o m etodo distancia() que recebe um ponto p
pertencente a outro objeto do tipo Ponto e calcula a distância euclidiana
entre dois pontos. (Dica: ver rodap ́e 1).

B3 - F́acil) Implemente o método transladar() que recebe dois parâmetros dx e
dy, correspondentes aos deslocamentos no eixo x e y respectivamente, e
translada um objeto da classe Ponto.

'''

# Supondo p1 = (0, 0) e p2 = (3, 5), a 
# distância euclidiana deve ser: 5.830951894845301
#Supondo p1 = (3, 2) e p2 = (-5, -8), a 
# distancia euclidiana deve ser: 12.806248474865697

class Ponto:


    def __init__ (self, x = 0 ,y =0):
        self.x = float(x)
        self.y = float(y)
    
    def obter_coordenadas(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
    def igual(self, p):
        return (self.x == p.x) and (self.y == p.y)

    def distancia(self, p2):
        return (((p2.x - self.x) ** 2) + ((p2.y - self.y))  ** 2) **0.5

    def transladar(self, dx, dy):
        self.x += dx
        self.y += dy
        return self.x, self.y

p1 = Ponto(1,9)
p2 = Ponto(3,5)
print(p1.distancia(p2))
print(p1.transladar(p2.x,p2.y))
print(p1.obter_coordenadas())

p3 = Ponto(3,2)
p4 = Ponto(-5,-8)
print(p3.distancia(p4))

'''
print( p1 == p2 ) # imprime True
p3 = Ponto(2, 0)
print ( p3 == p1 ) # imprime False
'''