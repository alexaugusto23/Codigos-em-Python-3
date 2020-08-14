Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> dir (random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_os', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> random.randodm()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    random.randodm()
AttributeError: module 'random' has no attribute 'randodm'
>>> random.random()
0.7471218494595775
>>> random.random()
0.2571317090043196
>>> random.random()
0.4352274851962571
>>> random.random()
0.054735217695083715
>>> random.randint(10, 20)
11
>>> random.randint(10, 20)
19
>>> random.randint(10, 20)
11
>>> random.randint(10, 20)
20
>>> help(random.choice)
Help on method choice in module random:

choice(seq) method of random.Random instance
    Choose a random element from a non-empty sequence.

>>> x = ['gol', 'astra', 'fusca', 'palio', 'uno',]
>>> 
>>> random.choice(x)
'palio'
>>> random.choice(x)
'uno'
>>> random.choice(x)
'gol'
>>> 
>>> random.choice(x)
'astra'
>>> random.shuffle(x)
>>> 
>>> x
['fusca', 'gol', 'palio', 'uno', 'astra']
>>> x
['fusca', 'gol', 'palio', 'uno', 'astra']
>>> x
['fusca', 'gol', 'palio', 'uno', 'astra']
>>> random.shuffle(x)
>>> x
['astra', 'fusca', 'uno', 'palio', 'gol']
>>> import string
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> string.digits
'0123456789'
>>> string.hexdigits
'0123456789abcdefABCDEF'
>>> string.capwords('teste de capitalize no curso de pyton')
'Teste De Capitalize No Curso De Pyton'
>>> 
