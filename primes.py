from numbertheory import _fibmod, primeList, isPrime

def prime(n):
    foundp = [2, 3]
    i = 5
    m = n
    foundn = 2
    while foundn < m:
        sqr = int(.5 + sqrt(i))
        for p in foundp:
            if p > sqr:
                foundp += [i]
                foundn += 1
                break
            if i % p == 0:
                break
        i += 2
    return foundp[-1]

def heuristic(n):
    if n % 2 == 0 or n % 5 not in [2, 3]:
        return False
    return pow(2, n-1, n) == 1 and _fibmod(n+1, n)[0] == 0
