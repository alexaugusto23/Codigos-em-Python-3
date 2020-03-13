num=int(input())
a=num/1000
aux_a=a
b=num%1000
c=b/100
aux_b=c
d=num%100
e=d/10
aux_c=e
f=num%1000
g=f%10
aux_d=g

print(int(aux_d),end='')
print(int(aux_c),end='')
print(int(aux_b),end='')
print(int(aux_a),end='')
