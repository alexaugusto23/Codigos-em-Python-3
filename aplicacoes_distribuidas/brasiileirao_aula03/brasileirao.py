'''
Grupo - MAAPSystems 
Alexsandro augusto Ignácio  RA 1901705  
Adriel Vicente da Conceição RA 1901842
Ariane Santos Cavalcante    RA 1902296
Micaella Borges Leal        RA 1902427
'''
    
'''
Nessa atividade, vamos usar dados do campeonato brasileiro 2018
(brasileirão) para estudar como acessar listas, dicionários,
e estruturas encadeadas (listas dentro de dicionários dentro de listas).

Os dados estão fornecidos em um arquivo (ano2018.json) que você 
pode abrir no firefox, para tentar entender melhor.

Se quiser ver os dados dentro do python, pode chamar a função
pega_dados.
'''

import json

def pega_dados():
    with open('ano2018.json') as f:
        dados = json.load(f)
    return dados

'''
1. Crie uma função datas_de_jogo, que procura nos dados do brasileirão
recebidas no parâmetro e devolve uma lista de todas as datas em que houve jogo.

As datas devem ter o mesmo formato que tinham nos dados do brasileirão.

Dica: busque em dados['fases'].

Observe que essa função (e todas as demais) recebem os dados dos
jogos num parâmetro chamado "dados". Essa variável contém todas as
informações que foram lidas do arquivo JSON que acompanha essa atividade.
'''

def datas_de_jogo(dados):
    resposta = []
    for data in dados['fases']['2700']['jogos']['data']:
        resposta.append(data)
    return resposta

'''
2. Crie uma função data_de_um_jogo, que recebe a id numérica de um jogo
e devolve a data em que ele ocorreu.

Se essa nao é uma id válida, você deve devolver a string 'não encontrado'.
Cuidado! Se você devolver uma string ligeiramente diferente, o teste
vai falhar.

(você provavelmente vai querer testar sua função no braço e não
somente fazer os meus testes. Para isso, note que muitos números
nesse arquivo estão representados não como números, mas como strings)
'''

def data_de_um_jogo(dados, id_jogo):
    for x in dados['fases']['2700']['jogos']['id']:
        if (id_jogo == x):
            return dados['fases']['2700']['jogos']['id'][id_jogo]['data']
    return 'não encontrado'

'''
3. Nos nossos dados, cada time tem um id, uma identificação numérica.
(você pode consultar as identificações numéricas em dados['equipes']).

Essas ids também aparecem nos jogos (onde? dê uma procurada!)

A próxima função recebe a id numérica de um jogo, e devolve as
ids numéricas dos dois times envolvidos.

Vou deixar um código pra você lembrar como retornar duas ids em
um único return.

def ids_dos_times_de_um_jogo(dados, id_jogo):
    time1 = 12
    time2 = 13
    return time1, time2 # Assim, retornamos as duas respostas em um único return.
'''

def ids_dos_times_de_um_jogo(dados, id_jogo):
    for x in dados ['fases']['2700']['jogos']['id']:
        if (id_jogo == x):
            t1 = dados['fases']['2700']['jogos']['id'][id_jogo]['time1']
            t2 = dados['fases']['2700']['jogos']['id'][id_jogo]['time2']  
    return t1, t2

'''
4. A próxima função recebe a id_numerica de um time e deve retornar o seu 'nome-comum'.
'''

def nome_do_time(dados, id_time):
        for x in dados ['equipes']:
            if (id_time == x):
                return dados ['equipes'][id_time]['nome-comum']


'''
5. A próxima função "cruza" as duas anteriores. Recebe uma id de um jogo
e retorna os "nome-comum" dos dois times.
'''

def nomes_dos_times_de_um_jogo(dados, id_jogo):
    for x in dados ['fases']['2700']['jogos']['id']:
        if (id_jogo == x):
            t1 = dados['fases']['2700']['jogos']['id'][id_jogo]['time1']
            t2 = dados['fases']['2700']['jogos']['id'][id_jogo]['time2']
            nome1 = dados ['equipes'][t1]['nome-comum']
            nome2 = dados ['equipes'][t2]['nome-comum']
            return nome1,nome2


'''
6. Façamos agora a busca "ao contrário". Conhecendo
o nome-comum de um time, queremos saber a sua id.
Se o nome comum não existir, retorne 'não encontrado'.
'''

def id_do_time(dados, nome_time):
    dic_time_id = {}
    for x in dados ['equipes']:
        dic_time_id [dados ['equipes'][x]['nome-comum']] = x
        #print(x)
        #print(dados ['equipes'][x]['nome-comum'])
    #print(dic_time_id)
    for chave in dic_time_id:
        if (chave == nome_time):
            return dic_time_id[chave]
    return print('não encontrado')

'''
dados = pega_dados()
id_do_time(dados, 'Cruzeiro')
'''

'''

7. Agora, façamos uma busca "fuzzy". Queremos procurar por 'Fla'
e achar o Flamengo. Ou por 'Paulo' e achar o São Paulo.

Nessa busca, você recebe um nome, e verifica os campos
'nome-comum', 'nome-slug', 'sigla' e 'nome',
tomando o cuidado de aceitar times se a string
buscada aparece dentro do nome (A string "Paulo"
aparece dentro de "São Paulo").

Sua resposta deve ser uma lista de ids de times que "batem"
com a pesquisa (e pode ser vazia, se não achar ninguém).
'''


def busca_imprecisa_por_nome_de_time(dados, nome_time):
    dict_busca = {}
    lista_id = []

    for x in dados ['equipes']:
        dict_busca [x] = dados['equipes'][x]['nome'], dados['equipes'][x]['nome-comum'],dados['equipes'][x]['nome-slug'], dados['equipes'][x]['sigla']
    #print(dict_busca)
    for chave in dict_busca:
        #print(chave)
        for palavra in dict_busca[chave]:
            #print(palavra)
            palavra.strip()
            if (nome_time in palavra):
                lista_id.append(chave)
                return lista_id


'''
8. Agora, a ideia é receber a id de um time e retornar as
ids de todos os jogos em que ele participou.
'''


def ids_de_jogos_de_um_time(dados, time_id):
    dic_ids_de_jogos = {}
    lista_jogos = []
    #cont = 0
    for x in dados ['fases']['2700']['jogos']['id']:
        dic_ids_de_jogos [x] = dados['fases']['2700']['jogos']['id'][x]['time1']
    #print(dic_ids_de_jogos)
    for chave in dic_ids_de_jogos:
        #print(chave)
        for valor in dic_ids_de_jogos[chave]:
            #print(valor)
            if print(time_id == dic_ids_de_jogos[chave][1]):
                return


'''
dados = pega_dados()
print(ids_de_jogos_de_um_time(dados, '695'))
'''

'''
9. Usando as ids dos jogos em que um time participou, podemos descobrir
em que dias ele jogou.

Note que essa função recebe o nome-comum do time, não a sua id.

Ela retorna uma lista das datas em que o time jogou.
'''
def datas_de_jogos_de_um_time(dados, nome_time):
    pass

'''
10. A próxima função recebe apenas o dicionário dos dados do brasileirão.

Ela devolve um dicionário, com quantos gols cada time fez.
'''
def dicionario_de_gols(dados):
    pass

'''
11. A próxima função recebe apenas o dicionário dos dados do brasileirão.

Ela devolve a id do time que fez mais gols no campeonato.
'''
def time_que_fez_mais_gols(dados):
    pass

'''
12. A próxima função recebe apenas o dicionário dos dados do brasileirão

Ela devolve um dicionário. Esse dicionário conta, para cada estádio,
quantas vezes ocorreu um jogo nele.

Ou seja, as chaves são ids de estádios e os valores associados,
o número de vezes que um jogo ocorreu no estádio.
'''
def dicionario_id_estadio_e_nro_jogos(dados):
    pass

'''
13. A próxima função recebe apenas o dicionário dos dados do brasileirão

Ela retorna o número de times que o brasileirão qualifica para a libertadores.
Ou seja, devolve quantos times são classificados para a libertadores (consultando
o dicionário de faixas).

Note que esse número está nos dados recebidos no parâmetro e você deve pegar esse
número daí. Não basta retornar o valor correto, tem que acessar os dados
fornecidos.
'''
def qtos_libertadores(dados):
    pass

'''
14. A próxima função recebe um tamanho, e retorna uma lista
com len(lista) = tamanho, contendo as ids dos times melhor classificados.
'''
def ids_dos_melhor_classificados(dados, numero):
    pass

'''
15. A próxima função usa as duas anteriores para retornar uma 
lista de todos os times classificados para a libertadores em
virtude do campeonato brasileiro.

Lembre-se de consultar a estrutura, tanto para obter a classificação, quanto
para obter o número correto de times a retornar.

A função só recebe os dados do brasileirão.
'''
def classificados_libertadores(dados):
    pass

'''
16. Da mesma forma que podemos obter a informação dos times classificados
para a libertadores, também podemos obter os times na zona de rebaixamento.

A próxima função recebe apenas o dicionário de dados do brasileirão,
e retorna uma lista com as ids dos times rebaixados.

Consulte a zona de rebaixamento do dicionário de dados, não deixe
ela chumbada da função.
'''
def rebaixados(dados):
    pass

'''
17. A próxima função recebe (além do dicionario de dados do brasileirão) uma id de time.
Ela retorna a classificação desse time no campeonato.
Se a id nao for válida, ela retorna a string 'não encontrado'.
'''

def classificacao_do_time_por_id(dados, time_id):
    cont = 0
    dic_classificacao = {}
    classificacao = dados ['fases']['2700']['classificacao']['grupo']
    #print(classificacao)
    
    for chave in classificacao:
        for valor in classificacao[chave]:
            #print (valor)
            cont += 1 
            #print (cont)
            dic_classificacao [valor] = cont
    #print("\n")
   # print(dic_classificacao,'\n')

    for chave in dic_classificacao:
        if print(chave == time_id):
            return print(dic_classificacao[chave])
    return print('não encontrado')

dados = pega_dados()
print(classificacao_do_time_por_id(dados, '695'))

