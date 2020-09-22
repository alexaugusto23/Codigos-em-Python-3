import requests

def procura_cep(cep):
    resposta = requests.get('https://viacep.com.br/ws/'+cep+'/json/')
    print (f'\nURL:{resposta.url}\nStatus:{resposta.status_code}\nRequest:{resposta.request}\n')   
    #print(dir(a))
    dic = resposta.json()
    return dic

cep_input = str(input("Digite o cep: "))
end = procura_cep(cep_input)
#print(end,'\n')
print('CEP:', end['cep'])
print('LOGRADOURO:', end['logradouro']) 
print('BAIRRO:', end['bairro']) 
print('LOCALIDADE:', end['localidade']) 
print('UF:', end['uf'])