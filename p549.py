import numbertheory
import math


def powpfact(n, p):
    s = 0
    while not n == 0:
        s += n//p
        n = n//p
    return s


#def factfact(n):
#    for p in numbertheory.primeList(n):
#        yield p, powpfact(n, p)
#    return


def s(n):
#    factors = list((primes[i], e) for i, e in enumerate(fac[n]) if not e == 0)
    factors = list(numbertheory.factor(n))
    m = max(list(p for p, e in factors))
    for p, e in factors:
        while powpfact(m, p) < e:
            m += 1
    return m


#def factorList(n):
#    fac = []
#    for p in primes:
#        f = [0]*(n + 1)
#        for e in range(1, int(math.log(n, p)) + 1):
#            f[p**e::p**e] = list(k + 1 for k in f[p**e::p**e])
#        fac += [f]
#    return list(map(list, zip(*fac)))

n = 10**8
#primes = list(numbertheory.primeList(n))
#fac = factorList(n)
#print(sum(s(i) for i in range(2, n+1)))
#for i in range(2, n+1):
#    print(i, s(i), list(numbertheory.factor(i)))

l = [0]*(n-1)
for p in numbertheory.primeList(n):
    k = p
    ke = 1
    for e in range(1, int(math.log(n, p))+1):
        if ke < e:
            k += p
            ke = powpfact(k, p)
        l[p**e-2::p**e] = list(max(k, i) for i in l[p**e-2::p**e])
print(sum(l))
# 476001479068717
