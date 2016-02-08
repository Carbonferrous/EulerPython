import math

for b in primeList(1000):
	for a in range(-999, 1000):
		n = 0
		while n ** 2 + a * n + b > 0 and isPrime(n ** 2 + a * n + b):
			n += 1
		if n > m:
			m = n
			print(a,b,a*b,m)
