import combinatorics as comb
from combinatorics import fib
import math
def firstfib(n):
    logfib = n*math.log((1+math.sqrt(5))/2, 10)-math.log(5, 10)/2
    dec = str(pow(10, 9+(logfib%1)))[:9]
    return dec

kf = {}
for n in range(10**6):
    t = firstfib(n)
    if comb.ispand(t):
        kf[n] = t
print(len(kf))

#each end repeats after 15*10**8 steps, so
#       fib(n + 15*10**8, 10**9) == fib(n, 10**9)
#because pisano(10**9)=15*10**8
kl = {}
for i in range(10**6):
    t = str(comb._fibmod(i, 10**9)[0])[-9:]
    if comb.ispand(t):
        kl[i] = t
print(len(kl))



for k in kf:
    if k in kl:
        print(k)
