import requests

def procura_cep(cep):
    a = requests.get('https://viacep.com.br/ws/'+cep+'/json/')
    print (f'\nURL:{a.url}\nStatus:{a.status_code}\nRequest:{a.request}\n')   
    #print(dir(a))
    dic = a.json()
    return dic

cep_input = str(input("Digite o cep: "))
end = procura_cep(cep_input)
#print(end,'\n')
print('CEP:', end['cep'])
print('LOGRADOURO:', end['logradouro']) 
print('BAIRRO:', end['bairro']) 
print('LOCALIDADE:', end['localidade']) 
print('UF:', end['uf'])