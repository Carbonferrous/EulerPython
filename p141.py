import math
import numbertheory
#a, ar, ar*r
#a = k*s*q**2, r = p/q
#n**2 = k**2*q*p**3+k*q**2
#a**6*n**2 = a**6*k*s*q*(k*s*p**3+q)
#(a**3*n)**2 = k*(s*a**2)*(q*a**2)*(k*(s*a**2)*p**3+(q*a**2))
#97344 8 92 1058 2 1 2 23
#196112016 432 4392 44652 3 4 6 61
#256160025 1089 6534 39204 1 1089 1 6
#576081 81 360 1600 1 1 9 40
#16900 25 75 225 1 25 1 3
#123383587600 67600 202800 608400 1 67600 1 3
#6230016 512 1472 4232 2 4 8 23
#12551169024 27648 70272 178608 3 16 24 61
#1380568336 12544 25872 53361 1 49 16 33
#9 1 2 4 1 1 1 2
#10404 36 72 144 1 36 1 2
#12006225 1225 2450 4900 1 1225 1 2
#13855173264 41616 83232 166464 1 41616 1 2
#9729849600 50625 78975 123201 1 81 25 39
#16394241600 69696 104544 156816 1 17424 2 3
#8534988225 50625 75600 112896 1 9 75 112
#1361388609 21609 30870 44100 1 441 7 10
#37344321 3969 5292 7056 1 441 3 4
#70963776 5832 7452 9522 2 9 18 23
#547674002500 521284 658464 831744 1 1444 19 24
#7322436 1936 2420 3025 1 121 4 5
#142965659664 314928 355752 401868 3 36 54 61
#36869184 5184 5760 6400 1 64 9 10
#878454337159 23

limit = 10**12
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
                a = k*s*q**2
                ar = k*s*p*q
                arr = k*s*p**2
                print(n, a, ar, arr, k, s, q, p)
print(su, len(found))
