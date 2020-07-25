lista_telefone = {}
nomes = []
concluir = None

print("----------------------------")
print("Olá Seja Bem vindo a Agenda.")
print("----------------------------\n")

while concluir != 0:
  
  nomes.append(input("Digite o nome na agenda: "))

  celular = (int(input("Digite o celular na agenda: ")))

  for i in nomes:
    a = i
  lista_telefone[a] = celular 

  concluir = input("Digite sair ou n para continuar a cadastrar contatos: ")
  if concluir == 'sair':
    concluir = 0
  else:
    concluir =1

print("\n")
print("nomes",nomes)
print("celular",celular)
print("dicionario",lista_telefone)