import math
import numbertheory

m = 0

for b in numbertheory.primeList(1000):
	for a in range(-999, 1000):
		n = 0
		while n ** 2 + a * n + b > 0 and numbertheory.isPrime(n ** 2 + a * n + b):
			n += 1
		if n > m:
			m = n
			print(a,b,a*b,m)
