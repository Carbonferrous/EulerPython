from math import factorial
from numbertheory import primeListRange
def sol(p):
    return sum(factorial(p-i) % p for i in range(1, 6)) % p
primes, siv = primeListRange(5, 10**8)
s = 0
for p in primes:
    s += sol(p)
    print(p, sol(p))
print(s)
