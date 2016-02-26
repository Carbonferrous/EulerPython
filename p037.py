import math
import numbertheory

s = 0
primes = list(numbertheory.primeList(1000000))
for prime in primes:
    cyclic = True
    prime = str(prime)
    for x in range(1,len(prime)):
        cyclic = cyclic and numbertheory.isPrime(int(prime[x:])) and numbertheory.isPrime(int(prime[:x]))
    if cyclic and len(prime) >= 2:
        s += int(prime)
        print(prime)
print(s)
