faturamento = {
    'SP':67836.43,
    'RJ': 36678.66,
    'MG' : 29229.88,
    'ES' : 27165.48,
    'Outros' : 19849.53
}

lista_val = []

for estados in faturamento:
    lista_val.append(faturamento[estados])
    print(lista_val)
total_mes = sum(lista_val)
print("valor total do mês",total_mes)

for estados in faturamento:
    percentual = (faturamento[estados] / total_mes) * 100
    print ("{} teve representação de: % {:.2f}".format(estados,percentual))

