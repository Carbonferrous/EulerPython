import math
s = 0
for n in range(3, 2540161):
	if sum(math.factorial(x) for x in [int(i) for i in str(n)]) == n:
		s += n
print(s)
