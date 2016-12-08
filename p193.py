import numbertheory
from numbertheory import factor, primeList
import math


# generates mobius function list
def mobiuslist(n):
    l = [1]*(n+1)
    for p in primeList(n):
        l[p::p] = [-1*x for x in l[p::p]]
        l[p**2::p**2] = [0] * len(l[p**2::p**2])
    return l


# returns mobius function
def mobius(n):
    if n == 1:
        return 1
    k = 1
    for p, e in factor(n):
        if e > 1:
            return 0
        k *= -1
    return k


def squarefree(n):
    d = 1
    for p in numbertheory.primeList(int(math.sqrt(n))):
        d *= p ** 2
        n *= p ** 2 - 1
    return n/d


def sqrfree(n):
    m = mobiuslist(2**(n//2)+1)
    print('got m')
    return sum(m[i]*(2**n//i**2) for i in range(1, 2**(n//2)+1))


print(sqrfree(50))
