import math
import itertools

def primeList(n):
    m = (n - 1) // 2
    B = [True]*m
    i = 0
    p = 3
    yield 2

    while n >= p ** 2:
        if B[i]:
            yield p
            j = 2*i**2+6*i+3
            B[j::2*i+3] = [False]*len(B[j::2*i+3])
        i += 1
        p += 2
    for x in range(i, m):
        if B[x]:
            yield p + 2 * (x - i)

def primeFactor(n):
    exp = 0
    while n & 1 == 0:
        n = n >> 1
        exp += 1
    if exp > 0:
        yield (2, exp)

    div = 3
    exp = 0
    while n % div == 0:
        n = n // div
        exp += 1
    if exp > 0:
        yield (3, exp)
    
    div = 5
    while div <= math.sqrt(n):
        exp = 0
        while n % div == 0:
            n = n // div
            exp += 1
        if exp > 0:
            yield (div, exp)
        exp = 0
        while n % (div + 2) == 0:
            n = n // (div + 2)
            exp += 1
        if exp > 0:
            yield (div + 2, exp)
        div = div + 6
    if n != 1:
        yield (n, 1)

def sigma(n):
    p = list(primeFactor(n))
    t = 1
    for div, exp in p:
        t *= (div ** (exp + 1) - 1)//(div - 1)
    return t
def amicable(n, p):
    if n in p or n in [-1, 0, 1]:
        return 1
    else:
        return sigma(n) - n

LIMIT = 1000000
p = list(primeList(LIMIT))
c = [-1, -1] + [0]*LIMIT
for x in range(2, LIMIT + 1):
    t = [x]
    if c[x] == 0:
        a = amicable(x, p)
        while a != x and (a not in t) and a < LIMIT and c[a] != -1:
            t += [a]
            a = amicable(a, p)
        if a == x:
            for b in t:
                c[b] = 1
            print(t)
        else:
            if a > LIMIT or a == 1:
                for b in t:
                    c[b] = -1
            c[x] = -1

