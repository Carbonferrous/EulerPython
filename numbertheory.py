import math
def primeList(n):
    primes = []
    isPrime = [True] * (n + 1)
    maxTest = int(math.sqrt(n)+1)
    isPrime[0] = False
    isPrime[1] = False
    for x in range(2, maxTest):
        if isPrime[x]:
            for j in range(2*x, n+1, x):
                isPrime[j] = False
    for i in range(0, n+1):
	    if isPrime[i]:
		    primes.append(i)
    return primes
def isPrime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    divisor = 5
    while divisor <= math.sqrt(n):
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor = divisor + 6
    return True
def primeFactor(n):
    divisor = 2
    divList = []
    while n % divisor == 0:
        n = n // divisor
        divList.append(divisor)
    divisor = divisor + 1
    while n % divisor == 0:
        n = n // divisor
        divList.append(divisor)
    divisor = 5
    while divisor <= math.sqrt(n):
        if n % divisor == 0:
            n = n // divisor
            divList.append(divisor)
        elif n % (divisor + 2) == 0:
            n = n // (divisor + 2)
            divList.append((divisor + 2))   
        else:
            divisor = divisor + 6
    if n != 1:
        divList.append(n)
    countList = [divList.count(x) for x in list(set(divList))]
    divList = list(set(divList))
    return sorted(list(zip(divList, countList)))
def totient(n):
    PrimeFactors = primeFactor(n)
    div = [PrimeFactors[x][0] for x in range(0,len(PrimeFactors))]
    for x in div:
        n = n * (x - 1) // x
    return n
