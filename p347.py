import numbertheory
def M(p, q, n):
    b = 0
    c = int(n/q)//p
    while not c == 0:
        c = c//p
        b += 1
    m = 0
    for i in range(1, b + 1):
        k = p**i*q
        while q*k <= n:
            k *= q
        if k > m:
            m = k
    return m
n = 10000000
primes = list(numbertheory.primeList(n//2))
s = 0
t = 0
for i, q in enumerate(primes):
    for p in primes[:i]:
        if p*q > n:
            break
        k = M(p, q, n)
#        print(p, q, M(p, q, n))
        t += 1
        s += k
print(s, t)
# 11109800204052 1903878
