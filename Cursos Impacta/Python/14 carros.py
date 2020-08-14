Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: F:\HD ALEX ARQUIVOS\Desktop Alex\FACULDADE IMPACTA ADS\Python\carros.py 
>>> from carros import Carro
>>> c = Carro ("Ponte")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    c = Carro ("Ponte")
TypeError: Carro() takes no arguments
>>> 
 RESTART: F:\HD ALEX ARQUIVOS\Desktop Alex\FACULDADE IMPACTA ADS\Python\carros.py 
>>> from carros import Carro
>>> c = Carro ("Ponte")
>>> c.caminho
'Ponte'
>>> from carros import Carro
>>> c = Carro ("Ponte")
>>> c.andar()
Andando pela Ponte
>>> c.caminho = "Praia"
>>> c.andar()
Andando pela Praia
>>> 
 RESTART: F:\HD ALEX ARQUIVOS\Desktop Alex\FACULDADE IMPACTA ADS\Python\carros.py 
>>> from carros import Fusca
>>> f = Fusc("Avenida")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    f = Fusc("Avenida")
NameError: name 'Fusc' is not defined
>>> f = Fusca("Avenida")
>>> type (f)
<class 'carros.Fusca'>
>>> f.andar ()
Andando pela Avenida
>>> 
 RESTART: F:\HD ALEX ARQUIVOS\Desktop Alex\FACULDADE IMPACTA ADS\Python\carros.py 
>>> from carros import Fusca
>>> f = Fusca("Praia")
>>> f.andar()
Andando pela Praia
>>> f.correr
<bound method Fusca.correr of <carros.Fusca object at 0x03845B90>>
>>> f.correr()
Andando pela pista
>>> 
 RESTART: F:\HD ALEX ARQUIVOS\Desktop Alex\FACULDADE IMPACTA ADS\Python\carros.py 
>>> 
 RESTART: F:\HD ALEX ARQUIVOS\Desktop Alex\FACULDADE IMPACTA ADS\Python\carros.py 
>>> from carros import Ferrari
>>> Ferrari = Ferrari ("Avenida")
>>> ferrari.andar()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    ferrari.andar()
NameError: name 'ferrari' is not defined
>>> Ferrari.andar("Avenida")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    Ferrari.andar("Avenida")
TypeError: andar() takes 1 positional argument but 2 were given
>>> ferrari = Ferrari ("Avenida")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    ferrari = Ferrari ("Avenida")
TypeError: 'Ferrari' object is not callable
>>> from carros import Ferrari
>>> ferrari = Ferrari ("Avenida")
>>> ferrari.andar()
Correndo muito
>>> 
