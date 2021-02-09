class Televisao():
    def __init__(self):
        self.canal = 0
        self.volume = 0
        self.status =  False
        self.msg = "A televisão está desligada por isso não podemos executar a sua solicitação"

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
    

    def trocar_canal(self):
        if (self.status == True):
            try:
                valor = int(input("Digite o canal desejado: "))
                if (type(valor) == int):
                    self.canal = valor
                else:
                    valor = int(input("Digite novamente o canal desejado: "))
                    self.canal = valor
                print(f"Canal trocado: {self.canal}")
            except:
                print("Atenção !!! Digite somente números!!!")
                valor = int(input("Digite o canal desejado: "))
                if (type(valor) == int):
                    self.canal = valor
                else:
                    valor = int(input("Digite novamente o canal desejado: "))
                    self.canal = valor
                print(f"Canal trocado: {self.canal}")
        else:
            print(self.msg)
    
    def troca_volume(self):
        if (self.status == True):
            try: 
                valor = int(input("Digite o volume desejado: "))
                if (type(valor) == int):
                    self.volume = valor
                else:
                    valor = int(input("Digite novamente o volume desejado: "))
                    self.volume = valor
                print(f"Volume trocado: {self.volume}")
            except:
                print("Atenção !!! Digite somente números!!!")
                valor = int(input("Digite o volume desejado: "))
                if (type(valor) == int):
                    self.volume = valor
                else:
                    valor = int(input("Digite novamente o volume desejado: "))
                    self.volume = valor
                print(f"Volume trocado: {self.volume}")
        else:
            print(self.msg)

    
    def aumenta_canal(self):
        if (self.status == True):
            aumentar = input("Para aumentar o canal digite: Sim ou Não! ")
            if (aumentar.lower() == "sim"):
                self.canal += 1
                print(f"Canal aumentado para: {self.canal}")
            elif(aumentar.lower() == "sim"):
                print(f"O canal não foi alterado: {self.canal}")
            else: 
                print("Essa função não existe!!!")
        else:
            print(self.msg)
        
    
    def diminui_canal(self):
        if (self.status == True):
            diminuir = input("Para diminuir o canal digite: Sim ou Não! ")
            if (diminuir.lower() == "sim"):
                self.canal -= 1
                print(f"Canal diminuido para: {self.canal}")
            elif(diminuir.lower() == "sim"):
                print(f"O canal não foi alterado: {self.canal}")
            else: 
                print("Essa função não existe!!!")
        else:
            print(self.msg)

    
    def aumenta_volume(self):
        if (self.status == True):
            aumentar = input("Para aumentar o volume digite: Sim ou Não! ")
            if (aumentar.lower() == "sim"):
                self.volume += 1
                print(f"Volume aumentado para: {self.volume}")
            elif(aumentar.lower() == "sim"):
                print(f"Volume não foi alterado: {self.volume}")
            else: 
                print("Essa função não existe!!!")
        else:
            print(self.msg)
    
    def diminui_volume(self):
        if (self.status == True):
            diminuir = input("Para diminuir o volume digite: Sim ou Não! ")
            if (diminuir.lower() == "sim"):
                self.volume -= 1
                print(f"Volume diminuído para: {self.volume}")
            elif(diminuir.lower() == "sim"):
                print(f"Volume não foi alterado: {self.volume}")
            else: 
                print("Essa função não existe!!!")
        else:
            print(self.msg)

tv = Televisao()
tv.troca_status()
tv.trocar_canal()

