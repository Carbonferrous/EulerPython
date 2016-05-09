import numbertheory

##if n is odd, return 2*n*p
##if n is even, return 2

def r():
    n = 1
    for p in numbertheory.primeList(10**4):
        yield (p, n, ((p-1)**n + (p+1)**n)%p**2, ((p-1)**n + (p+1)**n)%p**2/p)
        n += 1

primes =  r()
for p in primes:
    print(p)
