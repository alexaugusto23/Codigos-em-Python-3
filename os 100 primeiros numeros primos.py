# Sem lista
n = 0
divisores = 0

for n in range(1,101):
    divisores=0

    for div in range(1,n+1):
        if n % div == 0:
            divisores += 1 

    if divisores == 2:
        print(n, end=' ')

print('\n')

# Com lista

n = 0
divisores = 0
primos=[]

for n in range(1,101):
    divisores=0

    for div in range(1,n+1):
        if n % div == 0:
            divisores += 1 

    if divisores == 2:
        primos.append(n)

print(primos)
