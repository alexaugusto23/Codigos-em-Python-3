# Atividade Contínua 3
import math

class Elevador:
    __andar_atual = 0
    __quantidade_pessoas = 0

    def __init__(self, capacidade, andares):
        self.__capacidade = capacidade
        self.__atendidos = andares
        if 0 not in self.__atendidos:
            self.__atendidos.append(0)
        self.__atendidos.sort()

    def entrar(self):
        if self.__quantidade_pessoas < self.__capacidade:
            self.__quantidade_pessoas += 1

    def sair(self):
        if self.__quantidade_pessoas > 0:
            self.__quantidade_pessoas -= 1

    def subir(self):
        if self.__andar_atual < self.__atendidos[-1]:
            i = self.__atendidos.index(self.__andar_atual)
            self.__andar_atual = self.__atendidos[i + 1]

    def descer(self):
        if self.__andar_atual > self.__atendidos[0]:
            i = self.__atendidos.index(self.__andar_atual)
            self.__andar_atual = self.__atendidos[i - 1]

    def deslocar_para(self, andar):
        if andar in self.__atendidos:
            self.__andar_atual = andar

    def get_atendidos(self):
        return self.__atendidos

    def get_andar_atual(self):
        return self.__andar_atual

    def get_quantidade_pessoas(self):
        return self.__quantidade_pessoas

    def resumo(self):
        print("Andar atual:", self.__andar_atual)
        print("Andares atendidos:", self.__atendidos)
        print("Pessoas/Capacidade", self.__quantidade_pessoas,
              "/", self.__capacidade)
        print("########################################")

class Predio:

    def __init__(self, andar_alto, andar_baixo, elevadores):
        self.__andar_alto = andar_alto
        self.__andar_baixo = andar_baixo
        controle_atendidos = {}
        for i in range(self.__andar_baixo, self.__andar_alto + 1):
            controle_atendidos[i] = False
        for elevador in elevadores:
            for andar in elevador.get_atendidos():
                if andar in controle_atendidos:
                    controle_atendidos[andar] = True
                else:
                    # Elevador atende um andar que não existe
                    raise ValueError
        for andar in controle_atendidos:
            if controle_atendidos[andar] == False:
                # Algum andar não foi atendido
                raise ValueError
        self.__elevadores = elevadores

    def chamar(self, andar):
        # Primeiramente, calculei a distância que
        # cada elevador está do andar chamado.
        # negativo significa que o elevador precisa descer
        # positivo significa que o elevador precisa subir
        dist_andar = []
        for elevador in self.__elevadores:
            if andar in elevador.get_atendidos():
                dist_andar.append(andar - elevador.get_andar_atual())
            else:
                # Distância "infinita", caso ele não consiga atender o andar.
                # Meu "infinito" foi o tamanho do prédio + 1,
                # afinal, nenhuma distância será maior que isso.
                dist_andar.append(self.__andar_alto - self.__andar_baixo + 1)

        # Sabendo a distância de cada elevador pro andar, agora posso escolher
        # Suponho que vai ser o elevador indice 0 que vai atender, e se eu
        # encontrar um melhor, eu altero.
        indice = 0
        for i in range(len(dist_andar)):
            # Checo a distância absoluta (função fabs() do módulo math)
            if math.fabs(dist_andar[i]) < math.fabs(dist_andar[indice]):
                indice = i
            # Caso a distância seja igual,
            # vejo se o elevador[i] vai descer (negativo)
            elif math.fabs(dist_andar[i]) == math.fabs(dist_andar[indice]):
                if dist_andar[i] < dist_andar[indice]:
                    indice = i
                # Caso elevador[i] esteja no mesmo sentido,
                # vou checar as pessoas dentro dele.
                elif dist_andar[i] == dist_andar[indice]:
                    if self.__elevadores[i].get_quantidade_pessoas() \
                       < self.__elevadores[indice].get_quantidade_pessoas():
                        indice = i

        # Agora que tenho qual elevador vai atender o chamado, desloco ele.
        self.__elevadores[indice].deslocar_para(andar)
        if andar > 0:
            self.__embarque(indice)
        else:
            self.__desembarque(indice)

    def __embarque(self, indice_elevador):
        self.__elevadores[indice_elevador].entrar()

    def __desembarque(self, indice_elevador):
        while self.__elevadores[indice_elevador].get_quantidade_pessoas() > 0:
            self.__elevadores[indice_elevador].sair()

    def resumo(self):
        print("########################################")
        for e in self.__elevadores:
            print("Elevador", self.__elevadores.index(e))
            e.resumo()
