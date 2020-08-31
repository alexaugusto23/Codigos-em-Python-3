andar_atual = 10
andares = [-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

for i in andares:
    temp = i
    if temp == andar_atual:
        andar = temp

    else: 
        andar_no = temp
        print("Esse andar não existe")
        print(andar_no)
print("você chegou ao seu andar")
print(andar)