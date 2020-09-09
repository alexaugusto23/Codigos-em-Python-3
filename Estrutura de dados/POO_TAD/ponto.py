class Ponto:


    def __init__ (self, x ,y):
        self.x = x
        self.y = y
    
    def obter_coordenadas(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
    def igual(self, p):
        return (self.x == p.x) and (self.y == p.y)


p1 = Ponto(0, 0)
p2 = Ponto(0, 0)
print( p1 == p2 ) # imprime True
p3 = Ponto(2, 0)
print ( p3 == p1 ) # imprime False