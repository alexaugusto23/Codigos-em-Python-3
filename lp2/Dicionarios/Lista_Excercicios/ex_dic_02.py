num_pessoas =int(input('Quantidade de pessoas no cadastro: '))

cadastro = {}
for i in range (1,num_pessoas+1):
    print("Pessoa ",i)
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = int(input("CPF: "))
    cadastro[cpf] = [nome,idade]
    print("\n")
for chave in cadastro:
    print(chave, end= ' ', )
    for chave2 in cadastro[chave]:
        print(chave2, end= ' ')
    print("\n")
