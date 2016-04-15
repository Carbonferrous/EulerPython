import numbertheory

LIMIT = 1000
c = [0]*(LIMIT + 1)
p = numbertheory.primeList(LIMIT)
for x in p:
    for k in range(LIMIT//x + 1):
        c[x*k] += x

b = [0]*(LIMIT + 1)
for n in range(1, LIMIT + 1):
    b[n] = (c[n] + sum(c[k] * b[n - k] for k in range(1, n)))//n

for x in range(1, LIMIT):
	if b[x] > 5000:
		print(x, b[x])
		break
