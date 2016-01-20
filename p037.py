import math
def isPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    divisor = 5
    while divisor ** 2 <= n:
        if n % divisor == 0:
            return False
        if n % (divisor + 2) == 0:
            return False
        divisor = divisor + 6
    return True
def primeList(length):
    Plist = []
    for x in range(0, 4*(4 ** (length-2))):
        num = 
count = 0
for n in range(2,10):
    primes = primeList(n)
    for prime in primes:
        cyclic = True
        prime = str(prime)
        for x in range(1,len(prime)):
            cyclic = cyclic and isPrime(int(prime[x:])) and isPrime(int(prime[:x]))
        if cyclic and len(prime) >= 2:
            count = count + 1
            print(prime)
print(count)
