import math
import numbertheory
#a, ar, ar*r
#a = k*s*q**2, r = p/q
#n**2 = k**2*q*p**3+k*q**2
#a**6*n**2 = a**6*k*s*q*(k*s*p**3+q)
#(a**3*n)**2 = k*(s*a**2)*(q*a**2)*(k*(s*a**2)*p**3+(q*a**2))
#97344 2 1 2 23
#196112016 3 4 6 61
#256160025 1 1089 1 6
#576081 1 1 9 40
#16900 1 25 1 3
#6230016 2 4 8 23
#1380568336 1 49 16 33
#9 1 1 1 2
#10404 1 36 1 2
#12006225 1 1225 1 2
#9729849600 1 81 25 39
#8534988225 1 9 75 112
#1361388609 1 441 7 10
#37344321 1 441 3 4
#70963776 2 9 18 23
#7322436 1 121 4 5
#36869184 1 64 9 10

limit = 10**10
limsq = int(math.sqrt(limit))
sq = list(n**2 for n in range(1, limsq))
su = 0
found = []
#for k in range(1, int((math.sqrt(32*limit+1)-1)/16)):
#    for p in range(1, int((limit-1)**(1/3))):
#        for q in range(1, p):
#            n = k*q*(k*p**3+q)
#            if n > limit:
#                break
#            if n in sq:
#                if n not in found:
#                    found += [n]
#                su += n
#                print(n, k, q, p)
#print('asdf', len(found))
#found = []
for q, p in numbertheory.farey(200):
    if q == 0:
        continue
#    las = int((math.sqrt(32*limit+1)-1)/16)
    for k in range(1, 10):
        for s in sq:
            n = k*s*q*(k*s*p**3+q)
            if n > limit:
                break
            if n in sq and n not in found:
                found += [n]
                su += n
                print(n, k, s, q, p)
print(su, len(found))
