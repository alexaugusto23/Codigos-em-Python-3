'''
Questao 1: Faça as seguintes modificações na classe Ponto:

B1 - F ́acil) Modifique o construtor para que as coordenadas x e y sejam
opcionais. Caso nenhum valor seja passado como parâmetro, o construtor
deve iniciar as coordenadas x e y com valor zero (Dica: parâmetros default).

B2 - Facil) Implemente o m etodo distancia() que recebe um ponto p
pertencente a outro objeto do tipo Ponto e calcula a distância euclidiana
entre dois pontos. (Dica: ver rodap ́e 1).

B3 - F́acil) Implemente o m ́etodo transladar() que recebe dois parˆametros dx e
dy, correspondentes aos deslocamentos no eixo x e y respectivamente, e
translada um objeto da classe Ponto.

OBS: Dados dois pontos com coordenadas 
(x1, y1) e (x2, y2), a 
distância euclidiana d entre eles  ́e definida por:
d = p raiz (x2 − x1) 2 + (y2 − y1) 2.
'''


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

# Supondo p1 = (0, 0) e p2 = (3, 5), a 
# distância euclidiana deve ser: 5.830951894845301
#Supondo p1 = (3, 2) e p2 = (-5, -8), a 
# distancia euclidiana deve ser: 12.806248474865697

    def transladar(self):
        pass

p1 = Ponto(0,0)
p2 = Ponto(3,5)
print(p1.distancia(p2))

p3 = Ponto(3,2)
p4 = Ponto(-5,-8)
print(p3.distancia(p4))

'''
print( p1 == p2 ) # imprime True
p3 = Ponto(2, 0)
print ( p3 == p1 ) # imprime False
'''