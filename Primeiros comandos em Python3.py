# primeiros comandos para armazenar variáveis

nome = 'Alex'
idade = '23'
peso = '88.0'

print (nome, 'tem',idade,'anos e pesa', peso,'Kilos')

nome = 'Rafael'
idade = '38'
peso = '74.8'

print (nome, 'tem',idade,'anos e pesa', peso,'Kilos')

nome = input ('Qual é seu nome?')
idade = input ('Qual a sua idade ?')
peso = input ('Qual o seu peso ?')

print (nome, 'tem',idade,'anos e pesa', peso,'Kilos')

nome = input ('Qual é seu nome?')
idade = input ('Qual a sua idade ?')
peso = input ('Qual o seu peso ?')

print (nome,idade,peso)

nome = input ('Qual é seu nome?')
print('Olá Seja bem-vindo',nome)


# digite o seu nome

dia = input ('Digite o dia de seu nascimento:')
mes = input ('Digite o Mes de seu nascimento:')
ano = input ('Digite o Ano de seu nascimento:')
print('Sua data de Nascimento é:',dia,'-',mes,'-',ano)
print('Sim','ou ','Não','?')
resposta = input ('Digite uma resposta:')
if resposta == 'Sim' or 'sim':
    print('Você passou de teste')
else:
    print('Tente de novo')

# soma de produtos

a = int (input('Digite valor A:'))
b = int (input('Digite valor B:'))
c = a+b
print ('A soma dos números A e B é:',c)    



