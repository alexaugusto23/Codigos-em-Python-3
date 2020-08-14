# chamada função = ler_arquivo('pessoas.txt')

def ler_arquivo (nome_arquivo):
    arquivo = open (nome_arquivo, 'r')

    for linha in arquivo:
        print(linha)

    arquivo.close()    

# chamada função = salvar_arquivo('testeArquivo.txt', 'Testando a escrita de um arquivo')

def salvar_arquivo (nome_arquivo, texto):
    arquivo = open (nome_arquivo, 'w')
    arquivo.write(texto)

    arquivo.close()

