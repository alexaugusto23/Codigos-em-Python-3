def conta_ocorrencias(agenda):
    ocorrencias = {}
    numeros = []

    for i in agenda:
        ocorrencias[agenda[i]['telefones'][0]] = 0
        for j in range(len(agenda[i]['telefones'])):
            numeros.append(agenda[i]['telefones'][j])

    for i in numeros:
        if i in ocorrencias:
            ocorrencias[i] += 1
    return ocorrencias

conta_ocorrencias(agenda1)
agenda1 = {
    'lucas': {
        'email': 'lucas.goncalves@faculdadeimpacta.com.br',
        'telefones': [11999888999, 1177788899]
    },
    'maria' : {
        'email': 'maria.aparecida@exemplo.com',
        'telefones': [84999777444,1177788899]
    },
    'jadir': {
        'telefones': [1177788899]
    },
    'leoni' : {
        'email': 'leoni@ibm.com',
        'telefones': [84999777444, 121212122, 67676767, 12324545]
    }