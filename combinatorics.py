import math
import itertools

def combinations(n, r):
    if r > n - r:
        r = n - r
    res = 1
    for i in range(r):
        res =  res * (n - i) // (i + 1)
    return res

#def permutations(n, r):
#def partitions(n):
#twelve fold way
#generating functions
#def coinCountingStuff(): #dynamic programing

#generalized fibonacci sequences
#probability, statistical distributions

#returns isPandigital(n)
def ispand(n):
    A = sorted(list(c for c in n))
    return '123456789' == ''.join(c for c in A)


#returns fib(n)
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

#returns fib(n)%m
def _fibmod(n, m):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fibmod(n // 2, m)
        c = a * (b * 2 - a)
        d = a**2 + b**2
        if n & 1 == 0:
            return (c%m, d%m)
        else:
            return (d%m, (c + d)%m)

import numbertheory as nt
#returns the period of fib(n+p, m)=fib(n, m)
def _pisano(p):
    for i in range(1, 6*p+3):
        if _fibmod(i, p) == (0, 1):
            return i
from fractions import gcd
def lcm(a, b):
        return (a * b) // gcd(a, b)
def pisano(m):
    pi = 1
    for p, e in nt.factor(m):
        pi = lcm(pi, _pisano(p)*p**(e-1))
    return pi
#interface for _fib(n) and _fibmod(n, m)
def fib(n, m = None):
    if n < 0:
        if m == None:
            return (-1)**(-n+1) * _fib(-n)[0]
        return ((-1)**(-n+1) * _fibmod((-n) % pisano(m), m)[0])%m
    if m == None:
        return _fib(n)[0]
    return _fibmod(n % pisano(m), m)[0]
