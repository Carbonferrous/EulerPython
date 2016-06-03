from math import gcd
from numbertheory import divisorList, totient, isPrime, factor
def R(k):
    return (10**k - 1) // 9

##(10**k - 1)*9**-1 == 0 (mod n)
##10**k == 1 (mod 9n)
##k in totient(9n)

def A(n):
    if n % 2 == 0 or n % 5 == 0:
        return 0
    for k in divisorList(totient(9*n)):
        if pow(10, k, 9*n) == 1:
            return k
##print('p129')
##i = 10**6 + 1
##while True:
##	if A(i) > 10**6:
##		print(i, A(i))
##		break
##	i += 2

##print('p130')
##i = 3
##count = 0
##s = 0
##while count < 25:
##    if i % 2 == 0 or i % 5 == 0:
##        i += 1
##        continue
##    if not isPrime(i):
##        if (i - 1) % A(i) == 0:
##            count += 1
##            s += i
####            print(i,  A(i))
##    i += 1
##print(s)

##print('p132')
##10**k == 1 (mod 9n)
##find n where given k yields true
##def rfactor(k):
##    for div, exp in factor(k):
##        R(k) % R(div) == 0

##print('p133')
