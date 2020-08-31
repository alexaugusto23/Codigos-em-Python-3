Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lista = [1,2,3,4,5]
>>> lista
[1, 2, 3, 4, 5]
>>> lista[1]
2
>>> lista [0]
1
>>> for x in lista: print (x)

1
2
3
4
5
>>> 
>>> for x in lista:
	print (x)

	
1
2
3
4
5
>>> lista = [1, 'Antonio', 3.14, 'Nova String', True]
>>> lista
[1, 'Antonio', 3.14, 'Nova String', True]
>>>  for x in lista:
	print (x)
	
SyntaxError: unexpected indent
>>>  for x in lista:
	print (x)
	
SyntaxError: unexpected indent
>>> for x in lista: print (x)

1
Antonio
3.14
Nova String
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> lista [2]
3.14
>>> lista[2] = 'PI'
>>> lista
[1, 'Antonio', 'PI', 'Nova String', True]
>>> lista.append ('Novo valor')
>>> lista
[1, 'Antonio', 'PI', 'Nova String', True, 'Novo valor']
>>> lista.pop()
'Novo valor'
>>> lista
[1, 'Antonio', 'PI', 'Nova String', True]
>>> lista.pop()
True
>>> lista
[1, 'Antonio', 'PI', 'Nova String']
>>> lista.remove('Antonio')
>>> lista
[1, 'PI', 'Nova String']
>>> lista.insert(2, 'Insert')
>>> lista.insert(0,'Inicio')
>>> lista
['Inicio', 1, 'PI', 'Insert', 'Nova String']
>>> lista.reverse()
>>> lista
['Nova String', 'Insert', 'PI', 1, 'Inicio']
>>> lista.sort()lista.remove(1)
SyntaxError: invalid syntax
>>> lista.remove(1)
>>> lista
['Nova String', 'Insert', 'PI', 'Inicio']
>>> lista.sort()
>>> lista
['Inicio', 'Insert', 'Nova String', 'PI']
>>> lista.sort(reverse=True)
>>> lista
['PI', 'Nova String', 'Insert', 'Inicio']
>>> tupla = (3, 4 , 'Nome')
>>> tulpa
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    tulpa
NameError: name 'tulpa' is not defined
>>> tupla
(3, 4, 'Nome')
>>> tupla2 = 3,5,'Nome','Sobrenome'
>>> tupla2
(3, 5, 'Nome', 'Sobrenome')
>>> s = set ()
>>> s
set()
>>> s.add(1)
>>> s
{1}
>>> s.add(12)
>>> s
{1, 12}
>>> s.add(13)
>>> s
{1, 12, 13}
>>> s.add(14)
>>> 
>>> s
{1, 12, 13, 14}
>>> s.add(14)
>>> s
{1, 12, 13, 14}
>>> s.pop ()
1
>>> s
{12, 13, 14}
>>> s.removr(13)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s.removr(13)
AttributeError: 'set' object has no attribute 'removr'
>>> s.revome(13)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s.revome(13)
AttributeError: 'set' object has no attribute 'revome'
>>> s.remove(13)
>>> s
{12, 14}
>>> d = {}
>>> d
{}
>>> type(d)
<class 'dict'>
>>> d ['nome'] = "Marcos"
>>> d ['sobrenome'] = 'Almeida'
>>> d
{'nome': 'Marcos', 'sobrenome': 'Almeida'}
>>> d['data_nascimento'] = '18/05/1979'
>>> d
{'nome': 'Marcos', 'sobrenome': 'Almeida', 'data_nascimento': '18/05/1979'}
>>> d['telefone'] = '1199998533'
>>> d
{'nome': 'Marcos', 'sobrenome': 'Almeida', 'data_nascimento': '18/05/1979', 'telefone': '1199998533'}
>>> d.pop('telefone')
'1199998533'
>>> d
{'nome': 'Marcos', 'sobrenome': 'Almeida', 'data_nascimento': '18/05/1979'}
>>> d.popitem()
('data_nascimento', '18/05/1979')
>>> d
{'nome': 'Marcos', 'sobrenome': 'Almeida'}
>>> d.values()
dict_values(['Marcos', 'Almeida'])
>>> d.keys()
dict_keys(['nome', 'sobrenome'])
>>> 
