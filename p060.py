# a < b < c < d < e
# a, b, c, d, e != 2, 5
import numbertheory
import itertools


def cconprime(l):
    return all(numbertheory.isPrime(int(str(i)+str(j))) for i, j in itertools.permutations(l[::-1], 2))


p = list(numbertheory.primeList(10000))
p.remove(2)
p.remove(5)

d = {}
for k in p:
    d[k] = []
    for i in p:
        if cconprime([k, i]):
            d[k] += [i]
print('hello')
