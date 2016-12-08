from numbertheory import isPrime, factor, primeList, modinv
# 2*n**2 - 1 == 0 mod p
# n**2 == modinv(2, p) mod p


# solves R**2 == n mod p where p is an odd prime
def modsqrt(n, p):
    assert p % 2 == 1
    assert legendre(n, p) == 1
    Q = p - 1
    S = 0
    while Q % 2 == 0:
        S += 1
        Q = Q//2
    if S == 1:
        return pow(n, (p+1)//4, p), p - pow(n, (p+1)//4, p)
    z = 2
    while legendre(z, p) != -1:
        z += 1
    c = pow(z, Q, p)
    R = pow(n, (Q+1)//2, p)
    t = pow(n, Q, p)
    M = S
    while t % p != 1:
        for i in range(1, M):
            if pow(t, 2**i, p) == 1:
                break
        b = pow(c, 2**(M-i-1), p)
        R = (R*b) % p
        t = (t*b**2) % p
        c = pow(b, 2, p)
        M = i
    return R, p-R


def legendre(a, p):
    l = pow(a, p//2, p)
    if l not in [0, 1]:
        l = -1
    return l


def t(n):
    return 2*n**2-1

#count = 0
#for n in range(200):
#   print(n, t(n), list(factor(t(n))))
#print(count)


count = 0
pl = primeList(5*10**7)
next(pl)
for p in pl:
    if legendre(modinv(2, p), p) == 1:
        a, b = modsqrt(modinv(2, p), p)
        if t(a) == p or t(b) == p:
            count += 1
print(count)

#tlist = [1]*(5*10**7)
#tlist[0] = 0
#pl = primeList(5*10**7)
#next(pl)
#for p in pl:
#    if legendre(modinv(2, p), p) == 1:
#        a, b = modsqrt(modinv(2, p), p)
#        tlist[a::p] = [0]*len(tlist[a::p])
#        tlist[b::p] = [0]*len(tlist[b::p])
#print(sum(tlist))
