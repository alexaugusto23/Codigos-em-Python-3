class Televisao():
    def __init__(self):
        self.canal = 0
        self.volume = 0
        self.status =  False

    def status_on_off(self, valor):
        self.status = valor

    
    def status_on_off(self):
        if self.status == True:
            print('Ligada!!!')
        else:
            print('Desligada!!!')

    def trocar_canal(self, novo_canal):
        troca = self.canal = novo_canal
        return troca
    
    def troca_volume(self, novo_volume):
        troca = self.volume = novo_volume
        return troca
    
    def aumenta_canal(self):
        self.canal += 1
    
    def diminui_canal(self):
        self.canal -= 1
    
    def aumenta_volume(self):
        self.canal += 1
    
    def diminui_volume(self):
        self.canal -= 1

tv = Televisao()
tv.status_on_off()