class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume
        self.status =  False
    
    def status_on_off(self):
        if self.status == True:
            print('Ligado!!!')
        else:
            print

    def trocar_canal(self, novo_canal):
        troca = self.canal = novo_canal
        return troca
    
    def trocar_volume(self, novo_volume):
        troca = self.volume = novo_volume
        return troca