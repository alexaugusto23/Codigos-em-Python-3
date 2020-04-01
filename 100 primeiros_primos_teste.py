def numero_primos():
    primos=""
    qtdprimos=0
    
    for n in range(0,542):
        divisores=0
        for div in range(1,n+1):
            if n % div == 0:
                divisores += 1 
        if divisores == 2:
            qtdprimos +=1
            primos = primos + str(n) + " "
            if qtdprimos % 10 == 0:
                primos= primos + "= " + str(qtdprimos) + "\n" 
       
    return primos 

x=numero_primos()
print(x)