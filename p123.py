import numbertheory

##if n is odd, return 2*n*p
##if n is even, return 2

primes =  numbertheory.primeList(10**6)
n = 1
p = next(primes)
while 2*n*p < 10**10:
    n += 2
    next(primes)
    p = next(primes)
print(n, p)
