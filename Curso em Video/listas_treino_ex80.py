lista = []
for i in range (0,5): #(n-1)
    n = int(input("Digite um valor: "))
    if i == 0 or n > lista[len(lista)-1]:
        print(lista)
        lista.append(n)
        print("valor de n",n)
        print("valor de i = pos dentro da lista",len(lista)-1)
        print("valor dento de i = pos dentro da lista",lista[len(lista)-1])
        print(lista)
        print("Adicionado na posição ao final da lista")
        '''
        input: n = 1
        N [ ]
        i [ ]
        range (0,5) do for:
        |1| i == 0
        |2| i == 1
        |3| i == 2
        |4| i == 3
        |5| i == 4

        teste lógico:
        i == 0 verdadeiro
        if  i == 0 or n > lista[len(lista)-1]
        if  0 == 0 or 1 > lista[len(0)-1]
        lista[0] = 1

        N [1]
        i [0] 
        
        or

        input: n = 3
        N [1]
        i [0] 

        teste lógico:
        3 > lista[0]  |1| verdadeiro
        lista [1] = 3
        N [1 3]
        i [0 1] 






        
        '''
    else:
        pos = 0
        while (pos < len(lista)):
            if (n <= lista[pos]):
                lista.insert(pos,n)
                print(f"Adicionado na posição {pos}")
                break
                '''
                input: n = 25
                N [ 1 3 50 63 ]   
                i [ 0 1 02 03 ]
                
                teste lógico:
                0 = 25 <  lista[0] n vale: 01  = Falso
                1 = 25 <  lista[1] n vale: 03  = Falso 
                2 = 25 <  lista[2] n vale: 50  = Verdadeiro

                lista[2] = 25
                lista[3] = 50
                lista[4] = 63

                lista incrementa um posição e um valor

                N [ 1 3 25 50 63 ]   
                i [ 0 1 02 03 04 ]

                '''
            pos +=1
print("=-"*30)
print("Os valores digitados em ordem foram", lista)