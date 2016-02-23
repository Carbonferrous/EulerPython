def p(n ,prin = 0):
    a = list(range(1,n+1))
    if prin == 1:
        print(a, len(a))
    while len(a) > 1:
        a = a[1::2]
        if prin == 1:
            print(a, len(a))
        if len(a) == 1:
            break
        if len(a) & 1 == 0:
            a = a[::2]
        else:
            a = a[1::2]
        if prin == 1:
            print(a, len(a))
    return a[0]

def s(n):
    return sum(list(p(n) for n in range(1, n + 1)))

LIMIT = 4095
a = list(p(n) for n in range(1,LIMIT + 1))
b = list(set(a))
b.sort()
print(list((a.count(x)) for x in b))
c = list(enumerate(list(p(n) for n in range(1,LIMIT+1)),1))
for n in c:
    if n[1] == 24:
        print("{0:b}".format(n[0]), end = None)
        
