import math
def sol(l): #counts solutions from a list of exponents of primes
    s = 1
    for exp in l:
        s *= 2 * exp + 1
    s = (s + 1) // 2
    return s

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

def num(l): #creates n from list of exponents of primes
    n = 1
    a = primeList(10**3)
    for x in l:
        n *= next(a) ** x
    return n

def increment(l, MAX):
    for x in range(len(l)):
        if l[x] >= MAX - 1:
            l[x] = 0
            continue
        l[x] += 1
        break
    return l

def satisfied(l):
    return all(l[i] >= l[i+1] for i in range(len(l)-1))

def tester(d, MINSOL = 4000000, MAX = 7, R = 5):
    LIMIT = int(math.log(MINSOL, 3))+d
    l = [1]*LIMIT
    bestSol = num([MAX]*LIMIT)
    while l[R] <= 1:
        if num(l) < bestSol and sol(l) > MINSOL:
            bestSol = num(l)
        l = increment(l, MAX)
        while not satisfied(l):
            l = increment(l, MAX)
    return bestSol
s = int(input().strip())
r = 5
m = 8
best = num([m]*(int(math.log(s, 3))+1))
for d in range(-2, 3):
    t = tester(d, s, m, r)
    if t < best:
        best = t
print(best)

