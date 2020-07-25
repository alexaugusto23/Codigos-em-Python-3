'''
lanchonete = {'Salgado':4.5,'Lanche': 6.5,'Suco': 3.0,'Refrigerante': 3.5,'Doce':1.0}
print('\n-----------------------\n')
for produto in lanchonete:
    print(produto)
print('\n-----------------------\n')     
for produto in lanchonete:
    print(lanchonete[produto])
print('\n-----------------------\n') 
for produto in lanchonete:
    print(produto,lanchonete[produto])
print('\n-----------------------\n') 
for chave in lanchonete:
    valor = float(input('Novo valor: '))
    lanchonete[chave]=valor
for produto in lanchonete:
    print(produto,lanchonete[produto])
print('\n-----------------------\n') 
'''
'''
lanchonete2 = {}
for i in range (5):
    produto = input('Produto: ')
    lanchonete2[produto] = []
    print(lanchonete2)

for produto in lanchonete2:
    valor = float(input('Digite o valor: '))
    lanchonete2[produto].append(valor)
    print(lanchonete2)
'''

lanchonete3 = {}
lanchonete3 ['a'] = None
lanchonete3 ['a'] = 1
lanchonete3 ['b'] = 2
lanchonete3 ['c'] = 3
print(lanchonete3)

print(lanchonete3.items())
print(lanchonete3.keys())
print(lanchonete3.values())

#lanchonete3[0]= 'a'
#print(lanchonete3)
#lanchonete3.clear()



#for a,b in l.items():
#    print(f'{a} = {b}')











