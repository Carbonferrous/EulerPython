import numbertheory

def n(p1, p2):
    size = len(str(p1))
    k = ((p2-p1)*pow(10**size, p2 - 2, p2))%p2
    return k*10**size+p1

primes = numbertheory.primeList(10**9)
next(primes)#2
next(primes)#3
p1 = next(primes)#5
total = 0
for p2 in primes:
    total += n(p1, p2)
    p1 = p2
print(total)
