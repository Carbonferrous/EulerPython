def period(n):
	count = 1
	LIMIT = 1000
	while 10**count % n != 1 and count < LIMIT:
		count += 1
	if count == LIMIT:
		return 0
	else:
		return count

m = 0
for d in range(2, 1000):
	if period(d) > m:
		m = period(d)
		print(d, m)
