'''
Quando chamar a função subir 
dicionário como parâmetro e nome 
string para cálculo da média.
ex: dicionario = {'Ana':[8,6],'Laura':[9,7.66]'}
ex: nome='Ana'
Média de Ana = 7

'''

def calcular_media(dicionario, nome):
 
    if nome in dicionario:
        media = sum(dicionario[nome])/2
    else:
        return 0 
    return media

dicionario = {'Ana':[8,6],'Laura':[9,7.66]}
nome='Laura'
a=calcular_media(dicionario, nome)
print('Media de',nome,'é:',a)