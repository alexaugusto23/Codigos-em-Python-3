def hash(palavra, tamanho_tabela):
    soma = 0
    for pos in range(len(palavra)):
        soma = soma + ord(palavra[pos])
    return soma % tamanho_tabela

print(hash('impacta', 23))
print(hash('faculdade', 23))
print(hash('atividade', 23))
'''
Resultado
22
1
19
'''
'''
ord('1')
105
ord('m')
109
ord('p')
112
ord('a')
97
ord('c')
99
ord('t')
116
ord('a')
97

somando tudo = 735

h(735) = 735 % 23
h(735) = 22

ord('f')
102
ord('a')
97
ord('c')
99
ord('u')
117
ord('l')
108
ord('d')
100
ord('a')
97
ord('d')
100
print(ord('e'))
01010

somando tudo = 921
h(921) = 921 % 23
h(921) = 1

print('\n')
print(ord('f'))
print(ord('a'))
print(ord('c'))
print(ord('u'))
print(ord('l'))
print(ord('d'))
print(ord('a'))
print(ord('d'))
print(ord('e'))

 ‘atividade’
>>> ord('a')
97
>>> ord('t')
116
>>> ord('i')
105
>>> ord('v')
118
>>> ord('i')
105
>>> ord('d')
100
>>> ord('a')
97
>>> ord('d')
100
>>> ord('e')
101
Somando tudo: 97 + 116 + 105 + 118 + 105 + 100 + 97 + 100 + 101
= 939
h(939) = 939 % 23
h(939) = 19

'''










