##Non rigorously checked brute force solutions to n
##10
##315410
##927070
##2525870
##8146100
##16755190
##39313460
##97387280
##119571820
##121288430
##130116970
##139985660
##
##sum = 821107610

from numbertheory import isPrime
s = 0
for n in [10, 315410,927070,2525870,8146100,16755190,39313460,97387280,119571820,121288430,130116970,139985660]:
    if all(isPrime(n**2 + c, trialDivision = 5, millerRabin = 500) for c in [1, 3, 7, 9, 13, 27]) and all(not isPrime(n**2 + c, trialDivision = 5, millerRabin = 500) for c in [5, 11, 15, 17, 19, 21, 23, 25]):
        s += n
        print(n)
print(s)
##for n in range(10, 150*10**6, 10):
##    if n % 3 == 0 or n % 7 == 0 or n % 13 == 0:
##        continue
##    if all(isPrime(n**2 + c, trialDivision = 5, millerRabin = 8) for c in [1, 3, 7, 9, 13, 27]):
##        s += n
##        print(n, n**2 + 1, n**2 + 3, n**2 + 7, n**2 + 9, n**2 + 13, n**2 + 27)
