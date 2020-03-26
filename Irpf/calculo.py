# ALEXSANDO AUGUSTO IGNACIO RA 1901705
import irpf
cpf=int(input('Digite o CPF: '))
#dicionario = 100000.0 
#IR_retido = 15000.0
dicionario = 35000.0 
IR_retido = 3000.0
#dicionario = 21000.0 
#IR_retido = 0.0

teste = irpf.calcula_ir_bruto(dicionario)
teste2 = irpf.calcula_deducao(dicionario)
IR_devido=teste2
ir_liq = irpf.calcula_irpf_final(IR_devido,IR_retido)

if ir_liq < 0:
    print('CPF: ',irpf.num_para_cpf(cpf),'-','Deverá pagar R$',"%.2f"%ir_liq,'de IRPF.')
elif ir_liq > 0:
    print('CPF: ',irpf.num_para_cpf(cpf),'-','Receberá restituição de R$',"%.2f."%ir_liq)
elif ir_liq == 0:
    print('CPF: ',irpf.num_para_cpf(cpf),'-','Sem pendências com a Receita.')