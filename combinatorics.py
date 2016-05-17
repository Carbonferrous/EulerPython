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

#interface for _fib(n) and _fibmod(n, m)
def fib(n, m = None):
    if m == None:
        return _fib(n)[0]
    return _fibmod(n, m)[0]
