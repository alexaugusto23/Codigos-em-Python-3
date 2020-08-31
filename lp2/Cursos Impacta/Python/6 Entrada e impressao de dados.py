Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: F:\HD ALEX ARQUIVOS\Desktop Alex\FACULDADE IMPACTA ADS\Python\5 Entrada e impressao de dados.py 
digite um número inteiro: 5
digite o segundo número inteiro: 5
10
>>> print ("Imprimindo")
Imprimindo
>>> print ("Imprimindo", "Com", " Python")
Imprimindo Com  Python
>>> print ("Imprimindo", "o númeor", 5)
Imprimindo o númeor 5
>>> print ("Imprimindo", "o número", 5)
Imprimindo o número 5
>>> a = 10
>>> print ("Imprimindo", "o número", a)
Imprimindo o número 10
>>> print ("Eu tirei %d na prova" %a)
Eu tirei 10 na prova
>>> print ("Eu tirei %s na prova" %"Dez")
Eu tirei Dez na prova
>>> print ("Eu tirei %2f na prova" %9.5)
Eu tirei 9.500000 na prova
>>> print ("Eu tirei %.2f na prova" %9.5)
Eu tirei 9.50 na prova
>>> print ("Eu tirei %2f na prova" %9.58774873)
Eu tirei 9.587749 na prova
>>> print ("Eu tirei %.2f na prova" %9.58774873)
Eu tirei 9.59 na prova
>>> print ("Teste de %s, para dia %d. Float %.3f" %("marcadores", 4, 25.394838, 4))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print ("Teste de %s, para dia %d. Float %.3f" %("marcadores", 4, 25.394838, 4))
TypeError: not all arguments converted during string formatting
>>> print ("Teste de %s, para dia %d. Float %.3f" %("marcadores", 4, 25.3948384))
Teste de marcadores, para dia 4. Float 25.395
>>> 
