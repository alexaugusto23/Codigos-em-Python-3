import irpf_corrigido

def formata_cpf(cpf):
    cpf_string = str(cpf)
    bloco1 = cpf_string[:3]
    bloco2 = cpf_string[3:6]
    bloco3 = cpf_string[6:9]
    bloco4 = cpf_string[9:]
    cpf_string = bloco1 + '.' + bloco2 + '.' + bloco3 + '-' + bloco4
    return cpf_string

lista_receita = {12345678900: [100000.0, 15000.0], 98765432100: [35000.0, 3000.0], 14725836900: [21000.0, 0.0]}

for cpf in lista_receita:
    irpf_corrigido.calcula_ir_bruto(lista_receita, cpf)
    irpf_corrigido.calcula_deducao(lista_receita, cpf)
    irpf_corrigido.calcula_irpf_final(lista_receita, cpf)

    cpf_string = formata_cpf(cpf)
    ir = round(lista_receita[cpf][2], 2)
    if ir > 0:
        print("CPF:", cpf_string, "-", "Deverá pagar R$", ir, "de IRPF.")
    elif ir < 0:
        print("CPF:", cpf_string, "-", "Receberá restituição de R$", str(-ir) + ".")
    else:
        print("CPF:", cpf_string, "-", "Sem pendências com a Receita.")