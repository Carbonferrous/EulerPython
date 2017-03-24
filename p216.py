from numbertheory import modsqrt, primeList
import math
# 2*n**2 - 1 == 0 mod p
# n**2 == modinv(2, p) mod p
# 5437849 below 5*10**7

L = 10000
pl = primeList(int(math.sqrt(2)*L-1))
n = [True]*L
n[0] = False
n[1] = False
next(pl)
for p in pl:
    if p % 8 == 1 or p % 8 == 7:
        a, b = modsqrt((p+1)//2, p)
        if a > b:
            b, a = a, b
#        print(p, a, b)
        n[b::p] = [False]*len(n[b::p])
        n[a+p::p] = [False]*len(n[a+p::p])
print(sum(n))
