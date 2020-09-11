import requests
''
def procura_cpf(pont,uf):
    dic_acoes = {"acao":"gerar_cpf","pontuacao":'S',"cpf_estado":"SP"}
    dic_acoes['pontuacao'] = pont
    dic_acoes['cpf_estado'] = uf
    requisicao = requests.post('https://www.4devs.com.br/ferramentas_online.php',dic_acoes)
    print (f'\nURL:{requisicao.url}\nStatus:{requisicao.status_code}\nRequest:{requisicao.request}\n')   
    #print(dir(requisicao))
    resposta = requisicao.text
    #print("\n",resposta)
    return resposta

pontuacao_input = str(input("Deseja pontuação ? S/N:")).upper()
uf_input = str(input("Digite a UF do estado:")).upper()
cpf = procura_cpf(pontuacao_input,uf_input)
print(f"O CPF gerado foi {cpf}")