
dicio1 = { 12345: [8,6], 56234: [10,2], 14685: [8,9]}
lista = [2,4,6,8,10]


'''
for elem in lista:
    print(elem)

for elem in dicio1:
    print(elem)

for elem in dicio1:
    print(elem,dicio1[elem])

for elem in dicio1:
    print(elem)
    for elem2 in dicio1[elem]:
        print(elem2)

for elem in dicio1:
    print(elem, end = ' ')
    for elem2 in dicio1[elem]:
        print(elem2, end = ' ')
    print('\n')

'''


dicio2 = {14685:{'ac1':10,'ac2':5},14234:{'ac1':6,'ac2':8}}
lista = [2,4,6,8,10]
for elem in dicio2:
    print(elem)
    for elem2 in dicio2[elem]:
        print(dicio2[elem][elem2])




