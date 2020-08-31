def calcular_media(dicionario, nome):
 
    if nome in dicionario:
        media = sum(dicionario[nome])/len(dicionario[nome])
    else:
        return 0 
    return media

dicionario = {'Ana':[8,6],'Laura':[9,7.66]}
nome='Laura'
a=calcular_media(dicionario, nome)
print('Media de',nome,'é:',a)