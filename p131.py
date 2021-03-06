##Brute force search results
##p n k
##7 1 2
##19 8 12
##37 27 36
##61 64 80
##127 216 252
##271 729 810
##331 1000 1100
##397 1331 1452
##547 2197 2366
##631 2744 2940
##919 4913 5202
##1657 12167 12696
##1801 13824 14400
##1951 15625 16250
##2269 19683 20412
##2437 21952 22736
##2791 27000 27900
##3169 32768 33792
##3571 39304 40460
##4219 50653 52022
##4447 54872 56316
##5167 68921 70602
##5419 74088 75852
##6211 91125 93150
##Cuban primes are of the form 3*x**2 + 3*x + 1
##173 below 10**6
##338507 below 25*10**12

import math, numbertheory
cubpri = []
count = 0
#10**6 ==> 577, 25*10**12 ==> 2886751
for x in range(1, 2886751):
    cp = 3*x*(x + 1) + 1
    if numbertheory.isPrime(cp):
        count += 1
        cubpri += [cp]
print(count)

