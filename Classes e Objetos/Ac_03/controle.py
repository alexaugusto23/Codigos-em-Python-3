# Atividade Contínua 3
# ALEXSANDRO AUGUSTO IGNÁCIO - RA 1901705



class Elevador:
        __andares = None
        __capacidade = None
        __andar_atual = 0
        __quant_pessoas = None

    def __init__(self, capacidade, andares):
        self.__capacidade = capacidade
        self.__andares = andares

    def entrar(self):
        if self.__quant_pessoas <= self.__capacidade:
            self.__quant_pessoas += 1
        else:
            print("Acima da Quantidade permitida")

    def sair(self):
        if self.__quant_pessoas >= 1 and self.__quant_pessoas <= self.__capacidade:
            self.__quant_pessoas -= 1

    def subir(self):


    def descer(self):


    def deslocar_para(self, andar):



class Predio:

    def __init__(self, andar_alto, andar_baixo, elevadores):


    def chamar(self, andar):


    def __embarque(self, indice_elevador):


    def __desembarque(self, indice_elevador):
