import itertools
import math

size = {2, 3, 4, 5, 6, 9}
perm = list(''.join(x) for x in itertools.permutations('123456789'))
a = 1
t = ''
for s in size:
    a = 1
    t = ''
    while len(t) <= 9:
        t = ''
        for n in range(1,s+1):
            t += str(a*n)
        #print(a, t, s)
        if t in perm:
            print(t)
        a += 1
