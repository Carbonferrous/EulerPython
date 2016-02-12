import itertools
import math

def isPrime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    divisor = 5
    while divisor <= math.sqrt(n):
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor = divisor + 6
    return True

for n in list(map(int, [''.join(p) for p in itertools.permutations('1234567')]))[::-1]:
	if isPrime(n):
		print(n)
		break
