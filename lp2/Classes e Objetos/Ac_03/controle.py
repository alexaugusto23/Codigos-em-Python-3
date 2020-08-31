# Atividade Contínua 3
# ALEXSANDRO AUGUSTO IGNÁCIO - RA 1901705

class Elevador:
    __andares = None
    __capacidade = None
    __andar_atual = 0
    __quant_pessoas = 0

    def __init__(self, capacidade, andares):
        self.__capacidade = capacidade
        self.__andares = andares

    def entrar(self):
        if self.__quant_pessoas < self.__capacidade:
            self.__quant_pessoas += 1
            print("Pessoas Entrando no elevador: ")
            if self.__quant_pessoas > self.__capacidade:
                self.__quant_pessoas = self.__capacidade
                print("Quantidade Máxima atingida")

    def sair(self):
        if self.__quant_pessoas >= 1 and self.__quant_pessoas <= self.__capacidade:
            self.__quant_pessoas -= 1
            print("Saindo do elevador")
            if self.__quant_pessoas <= 0:
                print("Elevador Vazio")

    def subir(self):
        andar_max = max(self.__andares)
        andar_min = min(self.__andares)
        if self.__andar_atual > andar_min and self.__andar_atual < andar_max:
            self.__andar_atual += 1
            print("Subindo para: ")
            if self.__andar_atual > andar_max:
                self.__andar_atual = andar_max
                print("Chegou ao ultimo andar: ",self.__andar_atual)

    def descer(self):
        andar_max = max(self.__andares)
        andar_min = min(self.__andares)
        if self.__andar_atual <= andar_max:
            self.__andar_atual -= 1
            print("Descendo para: ")
            if self.__andar_atual == andar_min:
                self.__andar_atual = andar_min
                print("Chegou ao ultimo subsolo: ")

    def deslocar_para(self, andar):
        self.__andar_atual = andar
        print("Indo para: ")

    # Get
    def get_andares(self):
        return self.__andares

    def get_capacidade(self):
        return self.__capacidade

    def get_andar_atual(self):
        return self.__andar_atual

    def get_quant_pessoas(self):
        return self.__quant_pessoas

    # Set
    def set_andares(self,andares_set):
        self.__andares = andares_set

    def set_capacidade(self, capacidade_set):
        self.__capacidade = capacidade_set

    def set_andar_atual(self, andar_atual_set):
        self.__andar_atual = andar_atual_set

    def set_quant_pessoas(self, pessoas_set):
        self.__quant_pessoas = pessoas_set


class Predio:
    __elevadores = None
    __andar_alto = None
    __andar_baixo = None

    def __init__(self, andar_alto, andar_baixo, elevadores):
        self.__elevadores = elevadores
        self._andar_alto = andar_alto
        self.__andar_baixo = andar_baixo

    def chamar(self,andar):
        print("não consegui fazer essa lógica")

    def __embarque(self, indice_elevador):
        self.__elevadores = indice_elevador
        print(self.__elevadores)

    def __desembarque(self, indice_elevador):
        self.__elevadores = indice_elevador
        print(self.__elevadores)

    # Get
    def get_elevadores(self):
        return self.__elevadores

    def get_andar_alto(self):
        return self.__andar_alto

    def get_andar_baixo(self):
        return self.__andar_baixo