import datetime
import hashlib
from datetime import date
today = date.today()
print(today)


senha = 'Mag#2923'
salt = str(today)
secret = senha + salt
#hexadecimal format: f85113f50d37a1a15fb948d88c60647d9461d61de7d85c42a4e752ce05208752
x = hashlib.sha256(secret.encode('utf-8')).hexdigest()
print(x)

#byte format: b'L\xe7of\x1bQ\xab~y\xad\xa0\xbb\x04\xe2\x10 4z\t2\x07\xdeT\n\x8b\xa4\xfb\xb6#J\x86W'
y = hashlib.sha256(x.encode('utf-8')).digest() 
print(y)

#dir = dir(hashlib)
#print(dir)
