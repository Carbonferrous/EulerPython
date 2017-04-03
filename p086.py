from numbertheory import pythag
#s(m, m, m) = s(m-1, m-1, m-1) + sum(s(m, m-i, m-j) for j in range(i, m) for i in range(m))
#a = m
#b = m-i
#c = m-j
#if i == j == 0, not a solution
#a >= b >= c
#The following statement was tested for minimality
#d**2 = a**2 + (b+c)**2
#d**2 = m**2 + (2*m-i-j)**2
#suppose there is a primitive pythagorean triple r**2 + s**2 = t**2 such that
#m = kr, (2*m-i-j) = ks, and d = kt
#        2*kr-i-j = ks
#        2*k*r-k*s = i+j
#        i + j = 2*m-m*s//r
#        0 < i <= j < m
#        0 < i <= 2*m-m*s//r-i < m
#m % r == 0 and (2*m-i-j) % s == 0 and m/r == (2*m-i-j)/s == k and let d = k*t
#Once a pythagorean triple has been found, count the following solutions
#k*s = 2*m-i-j
#k*s = 2*k*r-i-j
#i+j = 2*m-m*s//r where 0 < i <= j < m
#for i in range(m):
#    j = 2*m-m*s//r-i
#    since j < m, it only counts if 0 < i <= 2*m-m*s//r-i < m
#    from the design of the loop, i <= 2*m-m*s//r-i < m
#i <= 2*m-m*s//r-i and 2*m-m*s//r-i < m
#i <= int(m-(m*s//r)/2) and m-m*s//r < i
#m-m*s//r < i <= int(m-(m*s//r)/2)
#there are int(m-(m*s//r)/2) - m + m*s//r
import math
def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False
pyth = []
a = pythag()
for i in range(1000):
    r, s, t = next(a)
    if r > s:
        r, s = s, r
    if s > 2*r:
        continue
    pyth += [(r, s, t)]

smem = {0:0}
def sol(m):
    if m in smem:
        return smem[m]
    smem[m] = sol(m-1)
    for r, s, t in pyth:
        if m % r == 0:
#            print(r, s, t)
            smem[m] += m-(m*s//r)//2 - max(0, m - m*s//r)
            print('a', m, m*s//r, (m*s//r)/2, m-max(0, m - m*s//r))
            if m*s//r % 2 == 1:
                smem[m] += 1
        if m % s == 0:
            smem[m] += m-(m*r//s)//2 - max(0, m - m*r//s)
            print('b', m, m*r//s, (m*r//s)/2, m-max(0, m - m*r//s))
            if m*r//s % 2 == 1:
                smem[m] += 1
    return smem[m]
#print(sol(100))
n = 12
count = 0
for c in range(1, n+1):
    for b in range(c, n+1):
        for a in range(b, n+1):
            if is_square(a**2+(b+c)**2):
                print(a, b+c, ';', b, c)
                count += 1
print()
print(count, sol(n))