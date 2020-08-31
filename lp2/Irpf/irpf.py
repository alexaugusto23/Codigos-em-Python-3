# ALEXSANDO AUGUSTO IGNACIO RA 1901705
def calcula_ir_bruto(dicionario):
    if (dicionario < 22847.76):
        resultado = 0
    elif(dicionario  > 22847.77 and dicionario < 33919.80):
        resultado = dicionario *0.075
    elif(dicionario > 33919.81 and dicionario < 45012.60):
        resultado = dicionario*0.15
    elif(dicionario  > 45012.61 and dicionario < 55976.16):
        resultado = dicionario*0.225
    elif(dicionario > 55976.16):
        resultado = dicionario*0.275

    return resultado

def calcula_deducao(dicionario):
    if (dicionario < 22847.76):
        resultado2 = 0
    elif(dicionario  > 22847.77 and dicionario < 33919.80):
        resultado2 = dicionario *0.075
        resultado2 -= 1713.58
    elif(dicionario > 33919.81 and dicionario < 45012.60):
        resultado2 = dicionario*0.15
        resultado2 -= 4257.57
    elif(dicionario  > 45012.61 and dicionario < 55976.16):
        resultado2 = dicionario*0.225
        resultado2 -= 7633.51
    elif(dicionario > 55976.16):
        resultado2 = dicionario*0.275
        resultado2 -= 10432.32


    return resultado2

def calcula_irpf_final(IR_devido,IR_retido):
    Restituicao_a_receber = IR_retido-IR_devido 
    return Restituicao_a_receber

def num_para_cpf(cpf):
    cpf=str(cpf)
    cpf_fortmatado = ""
    for digito in cpf:
        cpf_fortmatado=cpf_fortmatado+digito
        if len(cpf_fortmatado) == 3:
            cpf_fortmatado=cpf_fortmatado+"."
        if len(cpf_fortmatado) == 7:
            cpf_fortmatado=cpf_fortmatado+"."
        if len(cpf_fortmatado) == 11:
            cpf_fortmatado=cpf_fortmatado+"-"
    return (cpf_fortmatado)