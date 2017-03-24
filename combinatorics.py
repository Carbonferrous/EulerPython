import math
from math import gcd
import itertools
import numbertheory as nt


def combinations(n, r):
    if r > n - r:
        r = n - r
    res = 1
    for i in range(r):
        res = res * (n - i) // (i + 1)
    return res


# helper of factfact, determines number of times the prime p divides n!
def powpfact(n, p):
    s = 0
    while not n == 0:
        s += n//p
        n = n//p
    return s


# factors n!
def factfact(n):
    for p in nt.primeList(n):
        yield p, powpfact(n, p)
    return
# def permutations(n, r):
# def partitions(n):
# twelve fold way


# generating functions (or at least the beginning of one)
class polynomial(dict):
    def __init__(self):
        super().__init__()

    def __str__(self):
        s = ''
        for k in self:
            s += str(self[k])+'x^'+str(k)+'+'
        return s[:-1]

    def __repr__(self):
        return self.__str__()

    def __iadd__(self, o):
        for a in o:
            self[a] += o[a]
        return self

    def __missing__(self, _):
        return 0

    def __mul__(self, c):
        r = polynomial()
        if type(c) is int or type(c) is float:
            for a in self:
                r[a] = self[a] * c
        if type(c) is polynomial:
            for a in self:
                for o in c:
                    if a+o in r:
                        r[a+o] += self[a]*c[o]
                    else:
                        r[a+o] = self[a]*c[o]
        return r

    def __pow__(self, c):
        assert type(c) is int
        r = polynomial()
        r += {0: 1}
        for i in range(c):
            r = r * self
        return r

    def __add__(self, o):
        r = polynomial()
        r += self
        r += o
        return r

    def evaluate(self, x):
        return sum(self[k]*x**k for k in self)

# def coinCountingStuff(): #dynamic programing

# generalized fibonacci sequences
# probability, statistical distributions


# returns isPandigital(n)
def ispand(n):
    A = sorted(list(c for c in n))
    return '123456789' == ''.join(c for c in A)


# returns fib(n)
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n & 1 == 0:
            return (c, d)
        else:
            return (d, c + d)


# returns fib(n)%m
def _fibmod(n, m):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fibmod(n // 2, m)
        c = a * (b * 2 - a)
        d = a**2 + b**2
        if n & 1 == 0:
            return (c % m, d % m)
        else:
            return (d % m, (c + d) % m)


# returns the period of fib(n+p, m)=fib(n, m)
def _pisano(p):
    for i in range(1, 6*p+3):
        if _fibmod(i, p) == (0, 1):
            return i


def lcm(a, b):
        return (a * b) // gcd(a, b)


def pisano(m):
    pi = 1
    for p, e in nt.factor(m):
        pi = lcm(pi, _pisano(p)*p**(e-1))
    return pi


# interface for _fib(n) and _fibmod(n, m)
def fib(n, m=None):
    if n < 0:
        if m is None:
            return (-1)**(-n+1) * _fib(-n)[0]
        return ((-1)**(-n+1) * _fibmod((-n) % pisano(m), m)[0]) % m
    if m is None:
        return _fib(n)[0]
    return _fibmod(n % pisano(m), m)[0]
