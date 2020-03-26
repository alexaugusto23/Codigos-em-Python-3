
def cpf_para_num(cpf):
    cpf=int(cpf)
    cpf_formatado = ""
    for digito in cpf:
        cpf_formatado=cpf_formatado+digito
        if len(cpf_formatado) == 3:
            cpf_formatado=cpf_formatado+"."
        if len(cpf_formatado) == 7:
            cpf_formatado=cpf_formatado+"."
        if len(cpf_formatado) == 11:
            cpf_formatado=cpf_formatado+"-"
    return (cpf_formatado)

def num_para_cpf(cpf):
    cpf=str(cpf)
    cpf_formatado = ""
    for digito in cpf:
        cpf_formatado=cpf_formatado+digito
        if len(cpf_formatado) == 3:
            cpf_formatado=cpf_formatado+"."
        if len(cpf_formatado) == 7:
            cpf_formatado=cpf_formatado+"."
        if len(cpf_formatado) == 11:
            cpf_formatado=cpf_formatado+"-"
    return (cpf_formatado)

#cpf=36059729851
#x=num_para_cpf(cpf)
cpf='360.597.298-51'
x=cpf_para_num(cpf)
print(x)