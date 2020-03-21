import soma_per

sala = float(input('Digite o salario: '))
aumento = float(input('Digite o Aumento: '))
soma_sala_per=soma_per.soma10(sala)
soma_sala_per2=soma_per.soma50(sala)
soma_sala_per3=soma_per.soma_aumento(sala,aumento)

print('Salário R$ {} com aumento de 10 % por cento: R$ {}'.format(sala,soma_sala_per))
print('Salário R$ {} com aumento de 50 % por cento: R$ {}'.format(sala,soma_sala_per2))
print('Salário R$ {} + aumento de R$ {} é igual: R$ {}'.format(sala,aumento,soma_sala_per3))