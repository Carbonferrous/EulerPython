import math
import numbertheory
#accounts for 2 and 5
count = 2
primes = list(numbertheory.primeList(1000000))
for prime in primes:
    cyclic = True
    prime = str(prime)
    if '0' not in prime and '2' not in prime and '4' not in prime and '5' not in prime and '6' not in prime and '8' not in prime:
        for x in range(1,len(prime)):
            cyclic = cyclic and numbertheory.isPrime(int(prime[x:]+prime[:x]))
        if cyclic:
            count += 1
            print(prime)
    else:
        pass
print(count)
