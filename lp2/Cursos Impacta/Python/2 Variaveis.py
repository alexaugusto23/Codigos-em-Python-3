Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> print (a)
10
>>> 42
42
>>> type (42)
<class 'int'>
>>> id 42
SyntaxError: invalid syntax
>>> 
>>> id (42)
1826449136
>>> b = 42
>>> id (b)
1826449136
>>> 42
42
>>> 3,14
(3, 14)
>>> 3.14
3.14
>>> 'Texto'
'Texto'
>>> c - 3.14
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    c - 3.14
NameError: name 'c' is not defined
>>> c = 3.14
>>> var1 = 'Nome'
>>> var2 = 'Sobrenome'
>>> var1 + var2
'NomeSobrenome'
>>> dir(var1)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> var1 + c
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    var1 + c
TypeError: can only concatenate str (not "float") to str
>>> var1 + str(c)
'Nome3.14'
>>> 
