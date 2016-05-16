import numbertheory

primes = numbertheory.primeList(10**6+4)
next(primes)#2
next(primes)#3
p1 = next(primes)#5
total = 0
for p2 in primes:
    size = len(str(p1))
    k = 1
    while (k*10**size+p1) % p2 != 0:
        k += 1
    total += k*10**size+p1
    p1 = p2
print(total)
