import math
import bitarray
import itertools

def primeList(n):
    m = (n - 1) // 2
    B = bitarray.bitarray(m)
    B.setall(True)
    i = 0
    p = 3
    yield 2

    while n > p ** 2:
        if B[i]:
            yield p
            j = 2*i**2+6*i+3
            B[j::2*i+3] = False
        i += 1
        p += 2
    for x in range(i, m):
        if B[x]:
            yield p + 2 * (x - i)

def isPrime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    divisor = 5
    while divisor <= math.sqrt(n):
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor = divisor + 6
    return True

def primeFactor(n):
    divisor = 2
    divList = []
    while n % divisor == 0:
        n = n // divisor
        divList.append(divisor)
    divisor = divisor + 1
    while n % divisor == 0:
        n = n // divisor
        divList.append(divisor)
    divisor = 5
    while divisor <= math.sqrt(n):
        if n % divisor == 0:
            n = n // divisor
            divList.append(divisor)
        elif n % (divisor + 2) == 0:
            n = n // (divisor + 2)
            divList.append((divisor + 2))   
        else:
            divisor = divisor + 6
    if n != 1:
        divList.append(n)
    countList = [divList.count(x) for x in list(set(divList))]
    divList = list(set(divList))
    return sorted(list(zip(divList, countList)))

def numDivisor(n):
    f = primeFactor(n)
    n = 1
    for x in f:
        n = n * (x[1] + 1)
    return n

def totient(n):
    PrimeFactors = primeFactor(n)
    div = [PrimeFactors[x][0] for x in range(0,len(PrimeFactors))]
    for x in div:
        n = n * (x - 1) // x
    return n

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
