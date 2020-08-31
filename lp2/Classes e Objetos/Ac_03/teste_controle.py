import controle

elevador1 = [0,1,2,3,4,5]
andares = [-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
lista_elevador = ["um","dois"]

teste_controle = controle.Elevador(8,andares)
teste_predio = controle.Predio(max(andares),min(andares),lista_elevador)
print(teste_predio.get_elevadores())
teste_predio.chamar(1)

print("\n------------------------\n")
print("Capacidade: ",teste_controle.get_capacidade())
print("Andares disponiveis: ",teste_controle.get_andares())
print("\n------------------------\n")
teste_controle.entrar()
print(teste_controle.get_quant_pessoas())
teste_controle.entrar()
print(teste_controle.get_quant_pessoas())
teste_controle.entrar()
print(teste_controle.get_quant_pessoas())
teste_controle.entrar()
print(teste_controle.get_quant_pessoas())
teste_controle.sair()
print(teste_controle.get_quant_pessoas())
teste_controle.sair()
print(teste_controle.get_quant_pessoas())
teste_controle.sair()
print(teste_controle.get_quant_pessoas())
print("\n------------------------\n")
print(teste_controle.get_andar_atual())
teste_controle.subir()
print(teste_controle.get_andar_atual())
teste_controle.subir()
print(teste_controle.get_andar_atual())
teste_controle.subir()
print(teste_controle.get_andar_atual())
teste_controle.descer()
print(teste_controle.get_andar_atual())
teste_controle.deslocar_para(10)
print(teste_controle.get_andar_atual())





