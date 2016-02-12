m = 0
for d in range(2, 1000):
	n = 1
	while 10**n % d != 1 and n < 1000:
		n += 1
	if n > m and n != 1000:
		m = n
		print(d, m)
		
