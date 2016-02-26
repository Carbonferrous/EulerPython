import itertools
import math
import numbertheory

for n in list(map(int, [''.join(p) for p in itertools.permutations('1234567')]))[::-1]:
	if numbertheory.isPrime(n):
		print(n)
		break
