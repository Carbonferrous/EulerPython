import numbertheory
LIMIT = 100000
l = [0]*LIMIT
l[0] = 1
plist = numbertheory.primeList(LIMIT*2+1)
next(plist)
for x in plist:
    for y in range(int((LIMIT - x//2)**.5)):
        l[x//2+y**2] = 1
for x in range(LIMIT):
    if l[x] == 0:
        print(2*x+1)
        break
