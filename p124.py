import numbertheory

n = 100000
l = [1]*n
for p in numbertheory.primeList(n):
    l[p-1::p] = list(i*p for i in l[p-1::p])
s = []
for i, e in enumerate(l, 1):
    s += [(e, i)]
s.sort()
print(s[10000-1][1])