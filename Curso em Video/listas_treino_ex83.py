# Exercicio 83

expr = str(input("Digite a expressão: "))

pilha = []
for simb in expr:
    if (simb == '('):
        print(pilha)
        pilha.append('(')
        print(pilha)
    elif (simb == ')'):
        if len(pilha) > 0:
            print(pilha)
            pilha.pop()
            print(pilha)
        else:
            print(pilha)
            pilha.append(')')
            print(pilha)
            break
if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão não é válida')