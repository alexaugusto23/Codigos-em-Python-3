Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "Marcos"
'Marcos'
>>> 'Antonio'
'Antonio'
>>> '''
texto multinilha
para teste
na aula de python
'''
'\ntexto multinilha\npara teste\nna aula de python\n'
>>> 
>>> "Texto para ser fatiado" [0:6]
'Texto '
>>> "Texto para ser fatiado" [0:10]
'Texto para'
>>> "Texto para ser fatiado" [3:10]
'to para'
>>> "Texto para ser fatiado" [:6]
'Texto '
>>> "Texto para ser fatiado" [:10]
'Texto para'
>>> "Texto para ser fatiado" [0:10:3]
'Ttpa'
>>> "Fatiamento com valor negativo" [3:-4]
'iamento com valor nega'
>>> "Fatiamento com valor negativo" [::-1]
'ovitagen rolav moc otnemaitaF'
>>> 
>>> 
>>> 
>>> nome = "ana"
>>> 
>>> nome == nome [::=-1]
SyntaxError: invalid syntax
>>> nome == nome (::=-1)
SyntaxError: invalid syntax
>>> nome == nome [::-1]
True
>>> nome = "arara"
>>> nome == nome [::-1]
True
>>> nome = "Marcos"
>>> 
>>> nome
'Marcos'
>>> nome [0] = "b"
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    nome [0] = "b"
TypeError: 'str' object does not support item assignment
>>> nome = 'B' + nome [1:]
>>> nome
'Barcos'
>>> nome.startswith('B')
True
>>> nome.startswith('b')
False
>>> nome.endswith('r')
False
>>> nome
'Barcos'
>>> nome.replace('r','3')
'Ba3cos'
>>> nome
'Barcos'
>>> nome = nome.replace('r', '3')
>>> nome
'Ba3cos'
>>> 
>>> texto = "Testando split no python"
>>> 
>>> s = texto.split()
>>> s
['Testando', 'split', 'no', 'python']
>>> texto = "testando; novos;delimitadores"
>>> s= texto.split(';')
>>> s
['testando', ' novos', 'delimitadores']
>>> 
>>> data = ['18', '05', '1979']
>>> '/'.join(data)
'18/05/1979'
>>> 
