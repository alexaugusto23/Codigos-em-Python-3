a=0
for n in range(1,542):
    divisores=0
    for div in range(1,n+1):
        if n % div == 0:
            divisores += 1 
    if divisores == 2:
    	a=a+1
    	print('Contagem: ',a,'do número Primo: ',n)    	
print('\n')