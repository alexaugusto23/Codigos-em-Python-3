print("##################################")
print("Bem vindos ao jogo da Adivinhação!")
print("##################################")

numero_secreto = 42

chute = int(input ("Digite o seu número: "))

print("Você digitou", chute)

if (numero_secreto == chute):
    print("Você acertou")
    print("Número Secreto: ", numero_secreto)
else:
    print("Você errou!!!")

print("\nO Jogo Terminou !!!")