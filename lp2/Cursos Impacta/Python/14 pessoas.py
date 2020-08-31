Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: F:\HD ALEX ARQUIVOS\Desktop Alex\FACULDADE IMPACTA ADS\Python\pessoas.py 
>>> from pessoas import Pessoa
>>> p.salvar()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    p.salvar()
NameError: name 'p' is not defined
>>> p.Pessoa ()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    p.Pessoa ()
NameError: name 'p' is not defined
>>> p = Pessoa()
>>> p.nome = "João"
>>> p.Pessoa()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    p.Pessoa()
AttributeError: 'Pessoa' object has no attribute 'Pessoa'
>>> p = Pessoa ()
>>> p.salvar()
Salvando
>>> 
 RESTART: F:\HD ALEX ARQUIVOS\Desktop Alex\FACULDADE IMPACTA ADS\Python\pessoas.py 
>>> from pessoas import Pessoa
>>> 
>>> p = Pessoa ()
>>> p.nome = "Ana"
>>> p.nome
'Ana'
>>> 
 RESTART: F:\HD ALEX ARQUIVOS\Desktop Alex\FACULDADE IMPACTA ADS\Python\pessoas.py 
>>> from pessoas import Pessoa
>>> p = Pessoa ()
>>> p.nome = "Maria"
>>> p.salvar()
Salvando Maria
>>> 
 RESTART: F:\HD ALEX ARQUIVOS\Desktop Alex\FACULDADE IMPACTA ADS\Python\pessoas.py 
>>> from pessoas import Pessoa
>>> p = Pessoa ()
>>> p.nome = "José"
>>> p.salvar (João)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    p.salvar (João)
NameError: name 'João' is not defined
>>> p.salvar ("João")
Salvando João
>>> 
