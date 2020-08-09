numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas:
    print("\n##################################")
    print("Bem vindos ao jogo da Adivinhação!")
    print("##################################")
    print("\n -Tentativa {} de {} ".format (rodada, total_de_tentativas))
    chute_str = input ("\nDigite o seu número: ")
    print("\nVocê digitou", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("\nVocê acertou")
    else:
        if(maior):
            print("\nVocê errou! O seu chute foi maior que o número secreto")
        elif(menor):
            print("\nVocê errou! O seu chute foi menor que o número secreto")
    rodada = rodada + 1
    print("\n---------------------------------")

print("\nO Jogo Terminou !!!")