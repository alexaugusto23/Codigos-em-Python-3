class Televisao():
    def __init__(self):
        self.canal = 0
        self.volume = 0
        self.status =  False
        self.msg = "Televisão desligada"

    def troca_status(self):
        print("A Televisão está: ")
        self.status_on_off()
        status = input("Ligar ou Desligar Televisão: ")
                
        if (status.lower() == "ligar"):
            self.status = True
            self.status_on_off()
        elif (status.lower() == "desligar"):
            self.status = False
            self.status_on_off()
        else:
            print("Esse modo não existe!!!")

    
    def status_on_off(self):
        if self.status == True:
            print('Ligada!!!')
        else:
            print('Desligada!!!')
    

    def trocar_canal(self, novo_canal):
        if (self.status == True):
            troca = self.canal = novo_canal
            print(f"Canal trocado: {self.canal}")
        else:
            print(self.msg)
    
    def troca_volume(self, novo_volume):
        if (self.status == True):
            troca = self.volume = novo_volume
            print(f"Volume trocado: {self.volume}")
        else:
            print(self.msg)

    
    def aumenta_canal(self):
        if (self.status == True):
            self.canal += 1
            print(f"Canal mudado para: {self.canal}")
        else:
            print(self.msg)
        
    
    def diminui_canal(self):
        if (self.status == True):
            self.canal -= 1
            print(f"Canal mudado para: {self.canal}")
        else:
            print(self.msg)
    
    def aumenta_volume(self):
        if (self.status == True):
            self.volume += 1
            print(f"Volume diminuído para: {self.volume}")
        else:
            print(self.msg)
    
    def diminui_volume(self):
        if (self.status == True):
            self.volume -= 1
            print(f"Volume diminuído para: {self.volume}")
        else:
            print(self.msg)

tv = Televisao()
tv.troca_status()
tv.aumenta_canal()
tv.aumenta_canal()
