from numbertheory import primeList
import numbertheory
def residues(n, m):
    for i in range(m):
        yield pow(i, n, m)

n = 13
for m in primeList(1000):
    t = numbertheory.totient(m)
    r = list(residues(n, m))
    r = list(set(r))
    r.sort()
    if m % n == 1 and numbertheory.isPrime(m):
        print(m , len(r), r)
