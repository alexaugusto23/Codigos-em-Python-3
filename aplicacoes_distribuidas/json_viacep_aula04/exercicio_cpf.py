import requests
''
def procura_cpf(UF,pontuacao):
    pontuacao.upper()
    requisicao = requests.post('https://www.4devs.com.br/ferramentas_online.php',{"acao":"gerar_cpf","pontuacao":"+pontuacao+","cpf_estado":"+UF+"})
    print (f'\nURL:{requisicao.url}\nStatus:{requisicao.status_code}\nRequest:{requisicao.request}\n')   
    #print(dir(requisicao))
    resposta = requisicao.text
    #print("\n",resposta)
    return resposta

#procura_cpf()

'''
uf_input = str(input("Digite a UF do estado: "))
 = procura_cep(uf_input)
#print(end,'\n')
