import math
import itertools
import random
#generates primes up to n
def primeList(n):
    m = (n - 1) // 2
    if m < 0:
        return
    B = [True] * m
    i = 0
    p = 3
    if n > 1:
        yield 2

    while n >= p ** 2:
        if B[i]:
            yield p
            j = 2*i**2+6*i+3
            B[j::2*i+3] = [False] * len(B[j::2*i+3])
        i += 1
        p += 2
    for x in range(i, m):
        if B[x]:
            yield p + 2 * (x - i)

#generates lucky numbers up to n
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
#following tests return as follows -1:Definetly not prime, 0: passed the test, but no promises, 1:Definetly prime
def _isPrimeTrialDivision(n, bound = 1000):
    if n < 2:
        return -1
    for p in primeList(bound):
        if p ** 2 > n:
            return 1
        if n % p == 0:
            return -1
    return 0

def _isPrimeMillerRabin(n, bound = 12):
    if n < 2:
        return -1
    d = n - 1
    s = 0
    while d & 1 == 0:
        d = d >> 1
        s += 1
    for a in primeList(min(n-1, bound)):
        aPrime = False
        if pow(a, d, n) == 1:
            continue
        for r in range(s):
            if pow(a, d*2**r, n) == n-1:
                aPrime = True
                break
        if not aPrime:
            return -1
    return 0

#Uses a combination of primality tests
def isPrime(n, trialDivision = 1000, millerRabin = 12):
    t = _isPrimeTrialDivision(n, trialDivision)
    if t == -1:
        return False
    if t == 1:
        return True
    m = _isPrimeMillerRabin(n, millerRabin)
    if m == -1:
        return False
    return True

#trivial divison factoring of n
def _trialFactor(n):
    if n <= 0:
        return
    #check 2
    exp = _exponent(n, 2)
    n = n // 2**exp
    if exp > 0:
        yield (2, exp)
    #check 3
    div = 3
    exp = _exponent(n, div)
    n = n // div**exp
    if exp > 0:
        yield (3, exp)
    #begin trial division with increments of 6
    div = 5
    while div <= math.sqrt(n):
        #check div
        exp = _exponent(n, div)
        n = n // div**exp
        if exp > 0:
            yield (div, exp)
        #check div + 2
        exp = _exponent(n, div + 2)
        n = n // (div + 2)**exp
        if exp > 0:
            yield (div + 2, exp)
        #increment div
        div = div + 6
    if n != 1:
        yield (n, 1)

#Pollard's rho algorithm to find random factors
def _rhofactor(n):
    d = n
    while d == n:
        x = random.randint(1, n)
        c = random.randint(1, n)
        y = x
        f = lambda a:(a ** 2 + c)%n
        d = 1
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = math.gcd(abs(x - y), n)
    if isPrime(d):
        return d
    return _rhofactor(d)

#probably efficient factoring
def factor(n):
    if n <= 0:
        return
    #trial division
    for div in primeList(1000):
        exp = _exponent(n, div)
        n = n // div**exp
        if exp > 0:
            yield (div, exp)
    #rho factoring
    while not isPrime(n) and n != 1:
        div = _rhofactor(n)
        exp = _exponent(n, div)
        n = n // div**exp
        yield (div, exp)
    #make sure n is 1
    if n != 1:
        yield (n, 1)

#finds exponent of p in n
def _exponent(n, p):
    if n % p != 0:
        return 0
    i = 0
    while n % p**(2**i) == 0:
        i += 1
    i -= 1
    return 2**i + _exponent(n//p**2**i, p)

#returns number of divisors of n
def numDivisor(n):
    if n <= 0:
        return
    p = primeFactor(n)
    t = 1
    for div, exp in p:
        t *= exp + 1
    return t

#returns sum of divisors of n
def sumDivisor(n):
    if n <= 0:
        return
    p = primeFactor(n)
    t = 1
    for div, exp in p:
        t *= (div ** (exp + 1) - 1) // (div - 1)
    return t

#generates sigma up to n, each divisor is raised to power x
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

#returns totient of n
def totient(n):
    if n <= 0:
        return 0
    PrimeFactors = list(primeFactor(n))
    div = [PrimeFactors[x][0] for x in range(0,len(PrimeFactors))]
    for x in div:
        n = n * (x - 1) // x
    return n

#generates totient of numbers up to n, beginning with 0
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

#returns period of 1/n
def reciperiod(n):
    if n <= 2:
        return 0
    if n % 2 == 0 or n % 5 == 0:
        while n % 2 == 0:
            n = n // 2
        while n % 5 == 0:
            n = n // 5
        return reciperiod(n)
    count = 1
    current = 10 % n
    while current != 1:
        current = (10 * current) % n
        count += 1
    return count

#continued fraction of sqrt(n), stops after it repeats
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

#continued fraction list to real fraction
def contfrac2real(a):
    n = a[len(a) - 1]
    d = 1
    for i in range(len(a) - 2, -1, -1):
        n, d = d, n
        n = a[i] * d + n
    return [n, d]

#infinite precision sqrt decimal generator
def sqrtGen(n):
    numberS = str(n)
    if "." not in numberS:
        numberS += "."
    a = numberS.split(".")[0]
    b = numberS.split(".")[1]
    if len(a) & 1 == 1:
        a = "0" + a
    if len(b) & 1 == 1:
        b = b + "0"
    numberS = a + b + "00"
    c = 0
    p = 0
    x = 0
    y = 0
    d = len(a)//2
    while True:
        c = 100 * c + int(numberS[0:2])
        numberS = numberS[2:] + "00"
        for x in range(9, -1, -1):
            if x * (20 * p + x) <= c:
                break
        y = x * (20 * p + x)
        p = 10 * p + x
        c -= y
        yield x

#traverses the pythagorean tree with specific path using 'u', 'a', 'd'
def pythagTreeTraverse(traversal):
    uad = {'u':lambda m, n: (2*m-n, m),
           'a':lambda m, n: (2*m+n, m),
           'd':lambda m, n: (m+2*n, n)}
    uad['U'] = uad['u']
    uad['A'] = uad['a']
    uad['D'] = uad['d']
    m, n = 2, 1
    for t in traversal:
        m, n = uad[t](m, n)
    return (m**2-n**2, 2*m*n, m**2+n**2)

#generates pythagorean triplets with limits restricting the search space
def pythag(limits = lambda m,n: True):
    #a, b, c = m**2-n**2, 2*m*n, m**2+n**2
    uad = {'u':lambda m, n: (2*m-n, m), #increases at rate approaching 1 (smaller than d)
           'a':lambda m, n: (2*m+n, m), #increases at rate approaching 2sqrt2+3
           'd':lambda m, n: (m+2*n, n)} #increases at rate approaching 1
    l = limits #function of m,n to define when to continue
    root = [(2, 1)]
    branch = []
    while len(root) > 0:
        for m, n in root:
            yield (m**2-n**2, 2*m*n, m**2+n**2)
            p, q = uad['u'](m, n)
            if l(p, q):
                branch += [(p, q)]
            p, q = uad['d'](m, n)
            if l(p, q):
                branch += [(p, q)]
            p, q = uad['a'](m, n)
            if l(p, q):
                branch += [(p, q)]
        root = branch
        branch = []

#extended euclidian algorithm
def egcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

#modular multiplicative inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
