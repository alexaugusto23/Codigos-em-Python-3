import requests
''
def procura_cpf(pont,uf):
    dic_acoes = {"acao":"gerar_cpf","pontuacao":'',"cpf_estado":""}
    dic_acoes['pontuacao'] = pont
    dic_acoes['cpf_estado'] = uf
    requisicao = requests.post('https://www.4devs.com.br/ferramentas_online.php',dic_acoes)
    print (f'\nURL:{requisicao.url}\nStatus:{requisicao.status_code}\nRequest:{requisicao.request}\n')   
    print(dir(requisicao))
    #print("\n",resposta)
    return requisicao.text, requisicao.raw

pontuacao_input = str(input("Deseja pontuação ? S/N:")).upper()
uf_input = str(input("Digite a UF do estado:")).upper()
cpf = procura_cpf(pontuacao_input,uf_input)
print(f"O CPF gerado foi {cpf}")

'''
Siginificado do cpf:

EX: CPF XXX.XXX.XX"9" - YY

0 - Rio Grande do Sul.
1 - Distrito Federal, Goiás, Mato Grosso, 
Mato Grosso do Sul e Tocantins.
2 - Amazonas, Pará, Roraima, Amapá, Acré e 
Rondônia.
3 - Ceará, Maranhão e Piauí.
4 - Paraíba, Pernambuco, Alagoas e Rio Grande do Norte.
5 - Bahia e Sergipe.
6 - Minas Gerais.
7 - Rio de Janeiro e Espírito Santo.
8 - São Paulo.
9 - Paraná e Santa Catarina.
'''