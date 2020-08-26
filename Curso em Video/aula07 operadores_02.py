'''
n1 = int(input('Um valor: '))
n2 = int (input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))
'''

'''
n1 = int(input('Um valor: '))
n2 = int (input('Outro valor: '))
soma = n1 + n2
print('A soma vale {}'.format(soma))
'''

n1 = int(input('Um valor: '))
n2 = int (input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A Soma {} + {} vale {}'.format(n1,n2,s))
print('A Multiplicação {} X {} vale {}'.format(n1,n2,m))
print('A Divisão {} / {} vale {:.3f}'.format(n1,n2,d))
print('A Divisão de Inteiros {} // {} vale {}'.format(n1,n2,di))
print('A Portência {} ** {} vale {}'.format(n1,n2,e))

# \n         (quebra linha)
# end = ''   (junta quebra na mesma linha.)