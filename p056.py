import math
m = 0
for a in range(1, 100):
        for b in range(1, 100):
                n = sum(x for x in [int(i) for i in str(a**b)])
                if n > m:
                        m = n
print(m)
