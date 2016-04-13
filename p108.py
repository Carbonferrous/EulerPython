import numbertheory
def sol(l): #counts solutions from a list of exponents of primes
    s = 1
    for exp in l:
        s *= 2 * exp + 1
    s = (s + 1) // 2
    return s

def num(l): #creates n from list of exponents of primes
    n = 1
    a = numbertheory.primeList(500)
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
LIMIT = 20
MINSOL = 4000000
MAX = 10
l = [0]*LIMIT
bestSol = num([MAX]*LIMIT)
while l[LIMIT - 1] < 1:
    if num(l) < bestSol and sol(l) > MINSOL:
        bestSol = num(l)
    l = increment(l, MAX)
print(bestSol)
