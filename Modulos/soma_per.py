# Modulo para soma de percentual de salário ou aumento

def soma10(sala):
    soma = sala *1.1
    return soma

def soma50(sala):
    soma = sala*1.5
    return soma

def soma_aumento(sala,aumento):
    som_aum = sala+aumento
    return som_aum 

if __name__ == '__main__':
    print('Execução no Arquivo')
else:
    print('Execução no Módulo')    