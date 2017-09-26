import numbertheory
import math
# (2x-N)**2 + (2y-N)**2 = 2*N**2
# N = q_1**1*q_2**2*q_3**3 where q is a prime congruent 1 mod 4
# N*prod(p**a_i) where p is a prime not congruent 1 mod 4 is also a solution
# f(N) = 420

def r(n):
    s = 0
    for d in numbertheory.divisorList(n):
        s += (d % 4 == 1) - (d % 4 == 3)
    return 4*s

def f(n):
    return r(n**2)

#q = [n for n in numbertheory.primeList(int(10**11/21125)) if n % 4 == 1]
#print(len(q))
limit = 10**11
s = 0
for q3 in numbertheory.primeList(int((limit/(5**2*13))**(1/3))):
    if not q3 % 4 == 1:
        continue
    for q2 in numbertheory.primeList(int((limit/(q3**3*5))**(1/2))):
        if not q2 % 4 == 1:
            continue
        for q1 in numbertheory.primeList(int(limit/(q3**3*q2**2))):
            if not q1 % 4 == 1:
                continue
            if not (q1 == q2 or q2 == q3 or q1 == q3):
                n = q3**3*q2**2*q1
                m = int(math.log(limit, 2) - math.log(n, 2))
#                print(n, f(n), m, n*(2**(m+1)-1))
                s += n*(2**(m+1)-1)
print(s)
    
#(x-N/2)**2 + (y-N/2)**2 = N**2/2
#(2*x-N)**2 + (2*y-N)**2 = 2*N**2 = a**2 + b**2

#div = [0]*(10**8+1)
#print('finished allocating space')
#for i in range(1, 10**8+1, 4):
#    div[i] += 1
#for i in range(3, 10**8+1, 4):
#    div[i] -= 1
#print('finished siving')
#for i, d in enumerate(div):
#    if d == 53:
#        print(i)
