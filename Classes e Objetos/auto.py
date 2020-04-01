class CarroCorrida:
    # Atributos
    __numero_carro = None
    __nome_piloto = None
    __velocidade_max = None
    __velocidade_atual = None
    __ligado = None
    __desligado = None
    # Init
    def __init__(self,vel_max):
        self.__ligado = False
        self.__desligado = 0
        self.__velocidade_atual = 0.0
        self.__velocidade_max = vel_max
    # Get
    def get_numero_carro(self):
        return self.__numero_carro
    
    def get_nome_piloto(self):
        return self.__nome_piloto

    def get_velocidade_max(self):
        return self.__velocidade_max
    
    def get_velocidade_atual(self):
        return self.__velocidade_atual

    def get_ligado(self):
        return self.__ligado
    
    def get_desligado(self):
        return self.__desligado
    # Set
    def set_numero_carro(self, numero):
        self.__numero_carro = numero
    
    def set_nome_piloto(self, nome):
        self.__nome_piloto = nome

    def set_velocidade_max(self, maxima):
        self.__velocidade_max = maxima
    
    def set_velocidade_atual(self, atual):
        self.__velocidade_atual = atual

    def set_ligado(self, status):
        self.__ligado = status
    
    def ligar(self):
        if self.__ligado == False:
            self.__ligado = True
            print("O carro já esta ligado!")

    def desligar(self):
        if self.__ligado == True and self.__velocidade_atual == 0:
            self.__desligado = True
            print("O carro foi desligado com sucesso!")
        elif self.__velocidade_atual != 0:
            print("Pare o carro primeiro.")
        else:
            print("O carro já estava desligado.")

    def acelerar(self,n):
        if self.__ligado == True:
            if self.__velocidade_atual + n > self.__velocidade_max:
                self.__velocidade_atual = self.__velocidade_max
            else:
                self.__velocidade_atual += n
            print("Carro Acelerou")
        else:
            print("Carro desligado não acelera! Tem certeza que você é piloto mesmo?") 

    def desacelerar(self,n):
        if self.__ligado == True:
            if self.__velocidade_atual + n > self.__velocidade_max:
                self.__velocidade_atual = self.__velocidade_max
            else:
                self.__velocidade_atual -= n
            print("Carro Desacelerou")
        else:
            print("Carro desligado não acelera! Tem certeza que você é piloto mesmo?") 

    def frear (self):
        if self.__ligado == True and self.__velocidade_atual != 0:
            self.__velocidade_atual = 0
            print("Carro parou com sucesso!")
        elif self._ligado == True and self.__velocidade_atual == 0:
            print("Não precisa frear, carro já está parado")
        else:
            print("Carro está desligado")     
    
