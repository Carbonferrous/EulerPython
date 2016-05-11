from math import sqrt
import numbertheory

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


