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
def primeList(n):
    isPrimeList = [True]*(n+1)
    maxTest = int(math.sqrt(n)+1)
    isPrimeList[0] = False
    isPrimeList[1] = False
    for x in range(2,maxTest):
        if isPrimeList[x]:
            for j in range(2*x, n+1, x):
                isPrimeList[j] = False
    return list(filter(lambda x: isPrimeList[x], range(0,n)))
count = 0
primes = primeList(100000000)
for prime in primes:
    cyclic = True
    prime = str(prime)
    if '0' not in prime and '2' not in prime and '4' not in prime and '5' not in prime and '6' not in prime and '8' not in prime:
        for x in range(1,len(prime)):
            cyclic = cyclic and isPrime(int(prime[x:])) and isPrime(int(prime[:x]))
        if cyclic and len(prime) >= 2:
            count = count + 1
            print(prime)
    else:
        pass
print(count)
