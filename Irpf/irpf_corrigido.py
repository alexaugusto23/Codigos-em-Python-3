def calcula_ir_bruto(dicionario, chave):
    # Função que calcula o imposto bruto, isto é só a alíquota,
    # e armazena como 3o membro na lista valor.
    rendimento = dicionario[chave][0]
    if rendimento <= 22847.76:
        bruto = 0
    elif rendimento <= 33919.80:
        bruto = rendimento * 0.075
    elif rendimento <= 45012.60:
        bruto = rendimento * 0.15
    elif rendimento <= 55976.16:
        bruto = rendimento * 0.225
    else:
        bruto = rendimento * 0.275
    dicionario[chave].append(bruto)


def calcula_deducao(dicionario, chave):
    # Função que, dado uma pessoa com o IR bruto calculado,
    # faz o desconto da dedução e atualiza o 3o membro da lista valor.
    rendimento = dicionario[chave][0]
    bruto = dicionario[chave][2]
    if rendimento <= 22847.76:
        liquido = bruto
    elif rendimento <= 33919.80:
        liquido = bruto - 1713.58
    elif rendimento <= 45012.60:
        liquido = bruto - 4257.57
    elif rendimento <= 55976.16:
        liquido = bruto - 7633.51
    else:
        liquido = bruto - 10432.32
    dicionario[chave][2] = liquido


def calcula_irpf_final(dicionario, chave):
    # Função que, dado uma pessoa com IR líquido já calculado,
    # desconta a parte retida na fonte e atualiza o 3o membro
    # da lista valor
    dicionario[chave][2] -= dicionario[chave][1]