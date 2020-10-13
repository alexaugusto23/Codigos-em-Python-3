faturamento = {2020:{5:{
    1 : 1800.00,
    2 : 2500.25,
    3 : 3650.58,
    4 : 10000.00,
    5 : 6526.55,
    6 : 65423.56,
    7 : 10.20,
    8 : 300.00,
    9 : 6549.15,
    10 : 1654.55,
    11 : 8000.20,
    12 : 16542.54,
    13 : 1652.45,
    14 : 6452.54,
    15 : 6875.58,
    16 : 13000.00,
    17 : 4650.00,
    18 : 7591.22,
    19 : 456.55,
    20 : 959.55,
    21 : 22.22,
    22 : 35.90,
    23 : 700.00,
    24 : 66589.55,
    25 : 615.55,
    26 : 659.54,
    27 : 3549.33,
    28 : 3116.79,
    29 : 135.46,
    30 : 134.65,
    31 : 132.00,
}}}
soma = 0
lista_val = []
for i in faturamento[2020][5]:
    #print(faturamento[2020][5][i])
    lista_val.append(faturamento[2020][5][i])
print("menor valor de maio",min(lista_val))
print("maior valor de maio",max(lista_val))
print("média do mês",sum(lista_val)/len(lista_val))

#print(faturamento)
