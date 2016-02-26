import numbertheory

m = 0
for d in range(2, 1000):
	if numbertheory.reciperiod(d) > m:
		m = numbertheory.reciperiod(d)
		print(d, m)
