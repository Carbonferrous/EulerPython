import math
import numbertheory

count = 0
for n in range(2, 10001):
    if int(math.sqrt(n)) ** 2 == n:
        pass
    else:
        if len(list(numbertheory.contfracsqrt(n))) % 2 == 0:
            count += 1
print(count)
