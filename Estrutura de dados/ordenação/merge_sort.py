def intercala(a,b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
            c.append(a[i])
            i += 1
    while j < len(b):
            c.append(b[j])
            j += 1
    return c

L1 = [2,3,7,8]
L2 = [1,4,5,611]
L = intercala(L1,L2)
print(L)