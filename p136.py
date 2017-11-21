#(a+d)**2 - a**2 - (a-d)**2 = n
#4*a*d-a**2 = n
#n % 4 in [3, 0]
#a*(4*d-a) = n
#d = (n//a + a)
#d % 4 == 0 and d < a
#d = (n+a**2)/(a*4)
#a > 0, d > 0, a//4 < d < a <= n
#
#n < 3*a**2
#a > sqrt(n/3)

import numbertheory

limit = 50000000
count = sum(1 for p in numbertheory.primeList(limit) if p % 4 == 3)
count += len(list(numbertheory.primeList(limit//4)))
count += len(list(numbertheory.primeList(limit//16)))
print(count)
