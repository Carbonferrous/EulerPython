from numbertheory import totient

def teration(a, n, m):
	if n == 0 or m == 1:
		return 1
	return pow(a, teration(a, n-1, totient(m)),m)

print(teration(1777, 1855, 10**500))
