from math import factorial

def toBaseFactorial(n, s):
    perm = list(range(0, s))
    for a in range(s-1, -1, -1):
        b = 0
        while n >= factorial(a):
            n -= factorial(a)
            b += 1
        if n != 0:
            yield perm[b]
            perm.pop(b)
        else:
            yield perm[b-1]
            perm.pop(b-1)

print(list(toBaseFactorial(1000000, 10)))
