def palavra_mais_frequente():
    arquivo = open(file="Alice.txt", mode="r", encoding="utf8")
    s = arquivo.read()
    # cria uma lista com todas as palavras do arquivo em minúsculo
    lista = s.lower().split()
    
    dic = {}
    for palavra in lista:
        if palavra not in dic:
            dic[palavra] = 1
        else:
            dic[palavra] += 1
    maximo = 0    
    for palavra in dic:
        temp = dic[palavra]
        if temp > maximo:
            maximo = temp
            palavra_cand = palavra 
    print(palavra_cand, maximo)


palavra_mais_frequente()