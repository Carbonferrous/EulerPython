##Non rigorously checked brute force solutions to n
##10
##315410
##927070
##2525870
##8146100
##16755190
##39313460
from numbertheory import isPrime
s = 0
for n in range(10, 150*10**6, 10):
    if n % 3 == 0 or n % 7 == 0 or n % 13 == 0:
        continue
    if all(isPrime(n**2 + c, millerRabin = 20) for c in [1, 3, 7, 9, 13, 27]):
        s += n
        print(n, n**2, n**2 + 1, n**2 + 3, n**2 + 7, n**2 + 9, n**2 + 13, n**2 + 27)
