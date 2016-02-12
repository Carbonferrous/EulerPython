s = 0
for n in range(2, 354295):
	if sum(x**5 for x in [int(i) for i in str(n)]) == n:
		s += n
print(s)
