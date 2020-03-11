n1=int(input('Digite um valor: '))
n2=int(input('Digite um valor: '))
n3=n1+n2
print('A soma entre',n1,'e',n2,'é igual:',n3)
print('A soma entre {} e {} é igual: {}'.format(n1,n2,n3))

a1=int(input('Digite um valor: '))
a2=float(input('Digite um valor: '))
a3=bool(input('Digite um valor: '))
a4=str(input('Digite um valor: '))

print(a1.isnumeric())
print(a1.isalpha())
print(a1.isalnum())

print(a1,type(a1))
print(a2,type(a2))
print(a3,type(a3))
print(a4,type(a4))
