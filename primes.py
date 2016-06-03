

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

#Some Strong pseudoprimes
#Carmichael number and strong pseudoprime of primes below 300
p1 = 29674495668685510550154174642905332730771991799853043350995075531276838753171770199594238596428121188033664754218345562493168782883
n1 = p1*(313*(p1-1)+1)*(353*(p1-1)+1)

#Carmichael number and strong pseudoprime base 2, 3, 5, 11
n2 = 13618186946913248902029336585225618237728639469119284611739065110030838492720163

#random pseudoprime or something
n3 = 1913321727956758256045006260999587791041

import timeit
from cryptography import randprime
x = randprime(64)
y = randprime(64)
n = x * y
print(timeit.timeit('list(factor(n))', setup='from numbertheory import factor\nn=' + str(n), number=1))
