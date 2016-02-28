import math
import bitarray
import itertools

def primeList(n):
    m = (n - 1) // 2
    if m < 0:
        return
    B = bitarray.bitarray(m)
    B.setall(True)
    i = 0
    p = 3
    if n > 1:
        yield 2

    while n >= p ** 2:
        if B[i]:
            yield p
            j = 2*i**2+6*i+3
            B[j::2*i+3] = False
        i += 1
        p += 2
    for x in range(i, m):
        if B[x]:
            yield p + 2 * (x - i)

def lucky(n):
    if n >= 3:
        yield 1
        siv = list(range(1, n+1))
        temp = siv
    elif n > 0:
        yield 1
        return
    else:
        return
    a = 1
    d = 2
    while a < len(siv):
        temp = list(filter(lambda x: x[0] % d != 0, list(enumerate(siv,1))))
        siv = list(temp[b][1] for b in range(0,len(temp)))
        if a >= len(siv):
            break
        d = siv[a]
        yield siv[a]
        a += 1

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n & 1 == 0 or n % 3 == 0 or n == 1 or n < 0:
        return False
    divisor = 5
    while divisor <= math.sqrt(n):
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor = divisor + 6
    return True

def primeFactor(n):
    if n <= 0:
        return
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

def numDivisor(n):
    if n <= 0:
        return
    p = primeFactor(n)
    t = 1
    for div, exp in p:
        t *= exp + 1
    return t

def sumDivisor(n):
    if n <= 0:
        return
    p = primeFactor(n)
    t = 1
    for div, exp in p:
        t *= (div ** (exp + 1) - 1) // (div - 1)
    return t

def divisorList(n, x):
    if n <= 0:
        yield 0
        return
    elif n == 1:
        yield 0
        yield 1
        return
    elif n == 2:
        yield 0
        yield 1
        yield 1 + 2**x
        return
    else:
        pass
    divList = [1]*(n + 1)
    yield 0
    yield divList[1]
    for div in range(2, n+1):
        for i in range(div, n+1, div):
            divList[i] += div**x
        yield divList[div]


def totient(n):
    if n <= 0:
        return 0
    PrimeFactors = list(primeFactor(n))
    div = [PrimeFactors[x][0] for x in range(0,len(PrimeFactors))]
    for x in div:
        n = n * (x - 1) // x
    return n

def totientList(n):
    if n <= 0:
        yield 0
        return
    elif n == 1:
        yield 0
        yield 1
        return
    else:
        pass
    divList = list(range(n+1))
    yield 0
    yield divList[1]
    x = 2
    for div in primeList(n):
        for i in range(div, n+1, div):
            divList[i] = divList[i] * (div - 1) // div
        while x <= div:
            yield divList[x]
            x += 1
    while x <= n:
        yield divList[x]
        x += 1

def reciperiod(n):
    #returns period of 1/n
    if n <= 0:
        return 0
    count = 1
    LIMIT = 1000
    while 10**count % n != 1 and count < LIMIT:
    	count += 1
    if count == LIMIT:
        return 0
    else:
        return count

def contfracsqrt(n):
    m = 0
    d = 1
    a0 = int(math.sqrt(n))
    a = a0
    yield a
    while a != 2 * a0:
        m = d * a - m
        d = int((n - m ** 2) / d)
        a = int((a0 + m) / d)
        yield a

def contfrac2real(a):
    n = a[len(a) - 1]
    d = 1
    for i in range(len(a) - 2, -1, -1):
        n, d = d, n
        n = a[i] * d + n
    return [n, d]
