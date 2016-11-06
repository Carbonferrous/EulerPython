import numbertheory
from numbertheory import factor
import math


def mobius(n):
    if n == 1:
        return 1
    k = 0
    for p, e in factor(n):
        if e > 1:
            return 0
        k += 1
    return (-1) ** int(k % 2 == 1)


def squarefree(n):
    d = 1
    for p in numbertheory.primeList(int(math.sqrt(n))):
        d *= p ** 2
        n *= p ** 2 - 1
    return n/d


def sqrfree(n):
    return sum(mobius(i)*((n-1)//i**2) for i in range(1, int(math.sqrt(n-1))+1))


print(sqrfree(2**50))
